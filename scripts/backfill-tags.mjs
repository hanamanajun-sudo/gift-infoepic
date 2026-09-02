/**
 * 분류 태그(occasion / relation / ageGroup / budgetTag) 백필.
 *
 * 왜 필요한가: 102개 가이드 중 23개가 네 태그 모두 비어 있었다. 그러면
 * /상황/ /나이/ /관계/ /예산/ 허브 어디에도 안 뜨고, 연관 가이드 계산에서도
 * 후보가 0개가 되어 완전한 막다른 골목이 된다. 최대 유입원인 추석 페이지가 여기 포함돼 있었다.
 * 부분 누락(예산 51 / 나이 49 / 관계 43 / 상황 25)까지 합치면 사이트 내부링크 그래프가
 * 사실상 끊겨 있는 상태다.
 *
 * 사용법:
 *   node --env-file=.env scripts/backfill-tags.mjs            # 미리보기(기본, 아무것도 안 씀)
 *   node --env-file=.env scripts/backfill-tags.mjs --apply    # 실제 반영 + 되돌리기용 스냅샷 저장
 *   node --env-file=.env scripts/backfill-tags.mjs --revert <스냅샷파일>
 *
 * 반영 뒤에는 반드시 `python scripts/dump_cache.py`로 캐시를 다시 뽑아야 빌드에 반영된다.
 *
 * 태그는 "추가"만 한다. 기존 값은 절대 지우지 않는다 — 사람이 손으로 넣은 판단을
 * 규칙 기반 추론이 덮어쓰면 안 되기 때문이다.
 */

import { Client } from '@notionhq/client';
import { readFileSync, writeFileSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const CACHE = join(ROOT, 'src/data/notion-cache.json');

// ── 규칙 ────────────────────────────────────────────────────────────────
// 슬러그와 타이틀에서만 뽑는다. 본문 추론은 오탐이 많아 쓰지 않는다.

const OCCASION_RULES = [
  [/추석/, '추석'], [/설날/, '설날'], [/집들이/, '집들이'],
  [/결혼기념일/, '결혼기념일'], [/결혼축하/, '결혼축하'],
  [/퇴직/, '퇴직'], [/취직축하/, '취직축하'], [/승진축하/, '승진축하'],
  [/환갑/, '환갑'], [/돌잔치/, '돌잔치'], [/백일/, '백일'], [/출산/, '출산'],
  [/입학/, '입학'], [/졸업/, '졸업'],
  [/어린이날/, '어린이날'], [/어버이날/, '어버이날'], [/스승의날|선생님-감사/, '스승의날'],
  [/크리스마스/, '크리스마스'], [/발렌타인/, '발렌타인'], [/화이트데이/, '화이트데이'],
  [/생일선물|생신선물/, '생일'],
];

const RELATION_RULES = [
  [/아내|와이프/, '아내'], [/남편/, '남편'],
  // 부정 전방탐색 필수 — "할아버지"에 "아버지"가, "시어머니"에 "어머니"가 들어 있다.
  // 이걸 안 걸면 할아버지 가이드에 '아빠', 시어머니 가이드에 '엄마'가 붙는다.
  [/엄마|(?<!시)어머니/, '엄마'], [/아빠|(?<!할)아버지/, '아빠'],
  [/^딸-|딸-생일/, '딸'], [/^아들-|아들-생일/, '아들'],
  [/조카/, '조카'], [/베프|^친구-/, '친구'],
  [/남자친구/, '남자친구'], [/여자친구/, '여자친구'],
  [/할머니/, '할머니'], [/할아버지/, '할아버지'],
  [/시어머니/, '시어머니'], [/장인어른/, '장인어른'],
  [/직장상사/, '직장상사'], [/직장동료/, '직장동료'],
  [/선생님/, '선생님'], [/여동생/, '여동생'], [/남동생/, '남동생'],
  [/부모님/, '부모님'],
];

const AGE_RULES = [
  [/^(\d+)세-/, m => `${m[1]}세`],
  [/어린이-선물/, () => '초등학생'],
  [/영아|0-3세/, () => '영아'],
  [/유아|4-6세/, () => '유아'],
  [/초등학생/, () => '초등학생'],
  [/중학생/, () => '중학생'],
  [/고등학생/, () => '고등학생'],
  [/(\d0)대/, m => `${m[1]}대`],
];

const BANDS = [
  [10000, '1만원이하'], [30000, '3만원이하'], [50000, '5만원이하'],
  [100000, '10만원이하'], [200000, '20만원이하'],
];

function schoolBandFor(age) {
  if (age == null) return null;
  if (age <= 6) return '유아';
  if (age <= 12) return '초등학생';
  if (age <= 15) return '중학생';
  if (age <= 19) return '고등학생';
  return null;
}

const bandOf = price => (BANDS.find(([limit]) => price <= limit) ?? [, '20만원이상'])[1];

/**
 * 예산 태그.
 *
 * 밴드 의미는 누적이다 — 2만원짜리 상품은 '3만원이하'에도 '5만원이하'에도 해당한다.
 * 그래서 "중앙값이 들어가는 밴드부터 위로 2칸"까지 단다.
 *
 * 세 가지를 일부러 이렇게 정했다:
 *  1) 기준을 최저가가 아니라 중앙값으로 — 40대 남성 생일선물에 9,000원짜리 벨트가
 *     하나 있다는 이유로 그 페이지를 '1만원이하' 허브에 넣으면, 1만원으로 40대 선물을
 *     찾는 사람에게 10만원짜리 목록을 보여주게 된다.
 *  2) 위로 2칸까지만 — 안 그러면 거의 모든 가이드가 '20만원이하' 허브에 들어가 허브가 무의미해진다.
 *     기존에 사람이 손으로 넣은 태그(예: 12세 남자아이 = 3만·5만·10만)와도 이 폭이 맞는다.
 *  3) 중앙값이 20만원을 넘으면 '20만원이상' 하나만 — 고예산 전용 페이지다.
 *     (게임기 가이드가 중앙값 28만원인데 밴드 인덱스가 -1로 떨어져 1만원이하까지
 *      전부 붙던 버그가 있었다.)
 */
function budgetFor(prices) {
  if (!prices.length) return [];
  const sorted = [...prices].sort((a, b) => a - b);
  const median = sorted[Math.floor(sorted.length / 2)];
  const max = sorted[sorted.length - 1];

  const from = BANDS.findIndex(([, t]) => t === bandOf(median));
  if (from === -1) return ['20만원이상'];

  const tags = new Set();
  for (let i = from; i <= Math.min(from + 2, BANDS.length - 1); i++) tags.add(BANDS[i][1]);
  if (max > BANDS[BANDS.length - 1][0]) tags.add('20만원이상');
  return [...tags];
}

export function proposeFor(guide, prices) {
  const key = `${guide.slug} ${guide.title}`;

  const occasion = [...new Set(OCCASION_RULES.filter(([re]) => re.test(key)).map(([, t]) => t))];

  // 슬러그가 이미 대상을 지목하고 있으면 타이틀은 보지 않는다.
  // "남편 생일선물 TOP6 — 남편·와이프 선물"에서 '와이프'는 *주는 사람*이지 받는 사람이 아닌데,
  // 타이틀까지 훑으면 남편 가이드에 '아내'가 붙어 /관계/아내/ 목록에 끼어든다.
  // 반대로 "40대 남성 생일선물 — 아빠·남편·장인어른"처럼 슬러그가 대상을 안 밝히는 경우엔
  // 타이틀이 실제 대상 목록이므로 그대로 쓴다.
  const slugNamesRelation = RELATION_RULES.some(([re]) => re.test(guide.slug));
  const relationSource = slugNamesRelation ? guide.slug : key;
  const relation = [...new Set(RELATION_RULES.filter(([re]) => re.test(relationSource)).map(([, t]) => t))];

  const age = new Set();
  for (const [re, fn] of AGE_RULES) {
    const m = key.match(re);
    if (m) age.add(fn(m));
  }

  // 0-3세·4-6세는 2026-08-20에 상품을 걷어내고 시기별 분기 네비게이션 허브로 바꾼 페이지다.
  // 여기에 개별 나이를 달면 2세·3세·4세… 개별 가이드와 같은 허브에서 경쟁하게 된다.
  const isNavHub = /^0-3세-아기-선물|^4-6세-유아-선물/.test(guide.slug);
  const range = isNavHub ? null : key.match(/^(\d+)-(\d+)세/);
  if (range) for (let n = Number(range[1]); n <= Number(range[2]); n++) age.add(`${n}세`);

  const numeric = [...age].map(t => Number((t.match(/^(\d+)세$/) ?? [])[1])).filter(Boolean)[0];
  const band = schoolBandFor(numeric ?? guide.recipientAge);
  if (band) age.add(band);

  // 상품 실가격을 우선한다. Notion의 priceMin/Max는 비어 있거나 낡은 경우가 많다.
  const priceBasis = prices.length ? prices : [guide.priceMin, guide.priceMax].filter(Boolean);

  const onlyNew = (proposed, current) => proposed.filter(t => !current.includes(t));
  return {
    occasion: onlyNew(occasion, guide.occasion),
    relation: onlyNew(relation, guide.relation),
    ageGroup: onlyNew([...age], guide.ageGroup),
    budgetTag: onlyNew(budgetFor(priceBasis), guide.budgetTag),
  };
}

// ── 실행 ────────────────────────────────────────────────────────────────

const FIELDS = ['occasion', 'relation', 'ageGroup', 'budgetTag'];
const sleep = ms => new Promise(r => setTimeout(r, ms));

/**
 * 기존에 잘못 들어가 있는 relation 태그 보고.
 * 이 스크립트는 "추가만" 하는 정책이라 자동으로 못 고친다 — 사람이 판단해서 지워야 한다.
 * 실제 사례: 할아버지-생신선물의 relation이 ['아빠']로 들어가 있어 /관계/아빠/ 목록에 섞여 있었다.
 */
function reportSuspects(suspects) {
  if (!suspects.length) return;
  console.log('\n⚠️  기존 relation 태그가 슬러그와 안 맞는 가이드 (자동 수정하지 않음, 사람이 확인 필요):');
  for (const s of suspects) {
    console.log(`   ${s.slug.padEnd(24)} 지금=[${s.wrong.join(',')}]  슬러그상=[${s.shouldBe.join(',')}]`);
  }
}

async function main() {
  const args = process.argv.slice(2);
  const apply = args.includes('--apply');
  const revertIdx = args.indexOf('--revert');

  const notion = new Client({ auth: process.env.NOTION_API_KEY });

  if (revertIdx !== -1) {
    const snapshot = JSON.parse(readFileSync(args[revertIdx + 1], 'utf8'));
    console.log(`되돌리기: ${snapshot.entries.length}개 가이드를 ${snapshot.takenAt} 시점 태그로 복원`);
    for (const e of snapshot.entries) {
      await notion.pages.update({
        page_id: e.id,
        properties: Object.fromEntries(
          FIELDS.map(f => [f, { multi_select: e.before[f].map(name => ({ name })) }]),
        ),
      });
      console.log(`  ↩ ${e.slug}`);
      await sleep(350);
    }
    console.log('복원 완료. python scripts/dump_cache.py 를 실행할 것.');
    return;
  }

  const { guides, products } = JSON.parse(readFileSync(CACHE, 'utf8'));
  const pricesByGuide = new Map();
  for (const p of products) {
    if (!p.price) continue;
    if (!pricesByGuide.has(p.guideId)) pricesByGuide.set(p.guideId, []);
    pricesByGuide.get(p.guideId).push(p.price);
  }

  const targets = [];
  for (const g of guides) {
    const add = proposeFor(g, pricesByGuide.get(g.id) ?? []);
    const count = FIELDS.reduce((n, f) => n + add[f].length, 0);
    if (count > 0) targets.push({ guide: g, add, count });
  }

  // 기존 태그 중 의심스러운 것 보고 — 이 스크립트는 "추가만" 하므로 자동으로 못 고친다.
  // 예: 할아버지-생신선물의 relation이 ['아빠']로 들어가 있어 /관계/아빠/ 목록에 섞여 있다.
  const suspects = [];
  for (const g of guides) {
    if (!RELATION_RULES.some(([re]) => re.test(g.slug))) continue;
    const fromSlug = new Set(RELATION_RULES.filter(([re]) => re.test(g.slug)).map(([, t]) => t));
    const wrong = g.relation.filter(r => !fromSlug.has(r));
    if (wrong.length) suspects.push({ slug: g.slug, wrong, shouldBe: [...fromSlug] });
  }

  const totalTags = targets.reduce((n, t) => n + t.count, 0);
  const wasIsolated = targets.filter(t =>
    FIELDS.every(f => t.guide[f === 'ageGroup' ? 'ageGroup' : f].length === 0));

  console.log(`대상 ${targets.length}개 가이드 / 태그 ${totalTags}개 추가`);
  console.log(`완전 고립이었던 가이드: ${wasIsolated.length}개`);
  console.log('');

  for (const { guide, add } of targets) {
    const parts = FIELDS
      .filter(f => add[f].length)
      .map(f => `${f}+[${add[f].join(',')}]`)
      .join(' ');
    console.log(`  ${guide.slug.padEnd(28)} ${parts}`);
  }

  if (!apply) {
    console.log('\n미리보기입니다. 실제로 반영하려면 --apply 를 붙일 것.');
    reportSuspects(suspects);
    return;
  }

  // 되돌리기용 스냅샷 — 반영 전 상태를 통째로 남긴다
  const snapshotPath = join(ROOT, `tag-backfill-snapshot-${Date.now()}.json`);
  writeFileSync(snapshotPath, JSON.stringify({
    takenAt: new Date().toISOString(),
    entries: targets.map(({ guide }) => ({
      id: guide.id,
      slug: guide.slug,
      before: Object.fromEntries(FIELDS.map(f => [f, guide[f]])),
    })),
  }, null, 2), 'utf8');
  console.log(`\n스냅샷 저장: ${snapshotPath}`);
  console.log('되돌리려면: node --env-file=.env scripts/backfill-tags.mjs --revert <위 파일>\n');

  let ok = 0;
  for (const { guide, add } of targets) {
    const properties = {};
    for (const f of FIELDS) {
      if (!add[f].length) continue;
      properties[f] = {
        multi_select: [...guide[f], ...add[f]].map(name => ({ name })),
      };
    }
    try {
      await notion.pages.update({ page_id: guide.id, properties });
      ok++;
      console.log(`  ✓ ${guide.slug}`);
    } catch (err) {
      console.error(`  ✗ ${guide.slug} — ${err.message}`);
    }
    await sleep(350); // Notion 레이트 리밋(평균 3req/s) 여유
  }

  console.log(`\n반영 ${ok}/${targets.length}`);
  console.log('다음: python scripts/dump_cache.py 로 캐시 갱신 후 빌드할 것.');
}

main().catch(err => { console.error(err); process.exit(1); });
