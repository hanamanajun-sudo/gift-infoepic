/**
 * 분류 태그 정정 — 명시적으로 적어둔 항목만 바꾼다.
 *
 * `backfill-tags.mjs`는 "추가만" 하는 정책이라 잘못 들어간 값을 못 고친다.
 * 이 스크립트는 반대로 **지정한 필드를 통째로 교체**하므로, 규칙 추론을 쓰지 않고
 * 아래 표에 손으로 적은 것만 건드린다. 왜 바꾸는지도 같이 적는다.
 *
 * 사용법:
 *   node --env-file=.env scripts/fix-tags.mjs            # 미리보기
 *   node --env-file=.env scripts/fix-tags.mjs --apply    # 반영 + 되돌리기 스냅샷
 *   node --env-file=.env scripts/fix-tags.mjs --revert <스냅샷파일>
 *
 * 반영 뒤 `python scripts/dump_cache.py` 필수.
 */

import { Client } from '@notionhq/client';
import { readFileSync, writeFileSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const CACHE = join(ROOT, 'src/data/notion-cache.json');

/**
 * 2026-09-03 정정분.
 * 전부 백필 이전부터 있던 오류다 — 규칙이 만든 게 아니라 사람이 손으로 잘못 넣은 값이다.
 */
const FIXES = [
  {
    slug: '딸-생일선물',
    relation: ['딸'],
    why: '조카가 붙어 있어 /관계/조카/ 목록에 섞였다. 조카-생일선물은 별도로 있다.',
  },
  {
    slug: '아들-생일선물',
    relation: ['아들'],
    why: '위와 같음.',
  },
  {
    slug: '여동생-생일선물',
    relation: ['여동생'],
    why: '딸이 붙어 있었다. 여동생과 딸은 다른 대상이고 각각 페이지가 있다.',
  },
  {
    slug: '남동생-생일선물',
    relation: ['남동생'],
    why: '아들이 붙어 있었다.',
  },
  {
    slug: '할아버지-생신선물',
    relation: ['할아버지'],
    ageGroup: ['60대', '70대'],
    why: 'relation이 아빠로 들어가 /관계/아빠/에 섞였고, ageGroup이 50대라 40대 남성 페이지와 "인접 나이"로 묶였다.',
  },
  {
    slug: '할머니-생신선물',
    relation: ['할머니'],
    ageGroup: ['60대', '70대'],
    why: 'relation이 엄마로, ageGroup이 50대로 들어가 있었다.',
  },
  {
    slug: '12세-남자아이-생일선물',
    occasion: ['생일'],
    why: '졸업 태그 때문에 11·13세 가이드와의 연결이 끊기고 대신 졸업선물이 "비슷한 나이"로 붙었다. 초등 졸업은 졸업선물 페이지가 담당한다.',
  },
  {
    slug: '12세-여자아이-생일선물',
    occasion: ['생일'],
    why: '위와 같음.',
  },
];

const FIELDS = ['occasion', 'relation', 'ageGroup', 'budgetTag'];
const sleep = ms => new Promise(r => setTimeout(r, ms));

async function main() {
  const args = process.argv.slice(2);
  const apply = args.includes('--apply');
  const revertIdx = args.indexOf('--revert');
  const notion = new Client({ auth: process.env.NOTION_API_KEY });

  if (revertIdx !== -1) {
    const snapshot = JSON.parse(readFileSync(args[revertIdx + 1], 'utf8'));
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

  const { guides } = JSON.parse(readFileSync(CACHE, 'utf8'));
  const targets = [];

  for (const fix of FIXES) {
    const guide = guides.find(g => g.slug === fix.slug);
    if (!guide) { console.error(`✗ 가이드를 못 찾음: ${fix.slug}`); continue; }

    const changes = FIELDS
      .filter(f => fix[f] && JSON.stringify(fix[f]) !== JSON.stringify(guide[f]))
      .map(f => ({ field: f, before: guide[f], after: fix[f] }));

    if (!changes.length) { console.log(`  = ${fix.slug} (이미 정정됨)`); continue; }
    targets.push({ guide, fix, changes });
  }

  for (const { guide, fix, changes } of targets) {
    console.log(`\n${guide.slug}`);
    for (const c of changes) console.log(`   ${c.field}: [${c.before.join(',')}] → [${c.after.join(',')}]`);
    console.log(`   ↳ ${fix.why}`);
  }

  if (!targets.length) { console.log('\n바꿀 것이 없습니다.'); return; }
  if (!apply) { console.log('\n미리보기입니다. 반영하려면 --apply 를 붙일 것.'); return; }

  const snapshotPath = join(ROOT, `tag-fix-snapshot-${Date.now()}.json`);
  writeFileSync(snapshotPath, JSON.stringify({
    takenAt: new Date().toISOString(),
    entries: targets.map(({ guide }) => ({
      id: guide.id,
      slug: guide.slug,
      before: Object.fromEntries(FIELDS.map(f => [f, guide[f]])),
    })),
  }, null, 2), 'utf8');
  console.log(`\n스냅샷: ${snapshotPath}`);

  let ok = 0;
  for (const { guide, changes } of targets) {
    const properties = Object.fromEntries(
      changes.map(c => [c.field, { multi_select: c.after.map(name => ({ name })) }]),
    );
    try {
      await notion.pages.update({ page_id: guide.id, properties });
      ok++;
      console.log(`  ✓ ${guide.slug}`);
    } catch (err) {
      console.error(`  ✗ ${guide.slug} — ${err.message}`);
    }
    await sleep(350);
  }
  console.log(`\n반영 ${ok}/${targets.length}. 다음: python scripts/dump_cache.py`);
}

main().catch(err => { console.error(err); process.exit(1); });
