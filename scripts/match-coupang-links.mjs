/**
 * 쿠팡 링크가 없는 상품(네이버 링크만 있는 것)에 쿠팡 링크를 붙인다.
 *
 * 배경: 155개 상품이 naverUrl만 갖고 있어 수수료가 0원이다. 그중 9개 가이드가
 * 전체 트래픽의 24%를 차지한다. 쿠팡 계정 승인(2026-09-03)이 나기 전에는
 * 고쳐도 의미가 없었지만 이제는 바로 수익으로 이어진다.
 *
 * 이건 재큐레이션이 아니라 **매칭**이다. 상품은 이미 사람이 골라놓은 것이고,
 * 같은 물건을 쿠팡에서 찾아 링크만 붙인다. 그래서 "레고 마인크래프트 무기고 21252"처럼
 * 모델명이 있는 건 기계가 확신을 갖고 매칭할 수 있고, 애매한 것만 사람이 본다.
 *
 * 사용법:
 *   node --env-file=.env scripts/match-coupang-links.mjs                # 전체 미리보기
 *   node --env-file=.env scripts/match-coupang-links.mjs --guide <슬러그>  # 한 가이드만
 *   node --env-file=.env scripts/match-coupang-links.mjs --apply        # 확신 건만 반영
 *
 * --apply는 confidence가 'high'인 것만 반영한다. 'review'는 표로 출력만 하고
 * 건드리지 않는다 — 사람이 보고 판단할 몫이다.
 */

import { Client } from '@notionhq/client';
import { readFileSync, writeFileSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { searchCoupangProducts, createDeeplinks } from '../src/lib/coupang.ts';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const CACHE = join(ROOT, 'src/data/notion-cache.json');
const sleep = ms => new Promise(r => setTimeout(r, ms));

/** 검색어로 쓸 만하게 상품명을 줄인다. 쿠팡 검색은 긴 문장에 약하다. */
function toQuery(name) {
  return name
    .replace(/\[[^\]]*\]/g, ' ')       // [단독증정] 같은 판촉 괄호 제거
    .replace(/\([^)]*\)/g, ' ')
    .replace(/[,/+]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim()
    .split(' ')
    .slice(0, 6)                        // 앞쪽 6토큰이면 대개 브랜드+제품명
    .join(' ');
}

const norm = s => s.toLowerCase().replace(/[^0-9a-z가-힣]/g, '');

/** 모델 코드로 볼 만한 토큰(숫자 4자리 이상, 또는 영문+숫자 조합) */
function modelCodes(name) {
  return (name.match(/\b(?=\w*\d)[A-Za-z]*\d{3,}[A-Za-z]*\b/g) ?? [])
    .map(s => s.toLowerCase())
    .filter(s => !/^\d{4}$/.test(s) || Number(s) < 1900 || Number(s) > 2100); // 연도 제외
}

function scoreMatch(product, cand) {
  const a = norm(product.name);
  const b = norm(cand.productName);

  const codes = modelCodes(product.name);
  const codeHit = codes.length > 0 && codes.some(c => norm(cand.productName).includes(norm(c)));

  const tokenize = s => [...new Set(s.replace(/[\[\](),/+]/g, ' ').split(/\s+/).filter(t => t.length >= 2))];

  // 원본 토큰이 후보에 얼마나 들어있나
  const aTokens = tokenize(product.name);
  const overlap = aTokens.length ? aTokens.filter(t => b.includes(norm(t))).length / aTokens.length : 0;

  // 후보 토큰이 원본으로 설명되나 — 이게 낮으면 후보 쪽에 딴 게 붙어 있다는 뜻이다.
  // "코리아보드게임즈 할리갈리"를 찾는데 "코리아보드게임즈 미키와 친구들 할리갈리"가
  // 걸리면 원본 토큰은 100% 겹치지만(overlap=1.0) 실제로는 다른 에디션이다.
  const bTokens = tokenize(cand.productName);
  const reverse = bTokens.length ? bTokens.filter(t => a.includes(norm(t))).length / bTokens.length : 0;

  // 가격 근접도 (같은 상품이면 대개 ±35% 안)
  const ratio = product.price && cand.productPrice
    ? Math.min(product.price, cand.productPrice) / Math.max(product.price, cand.productPrice)
    : 0;

  // 에디션·구성 차이를 나타내는 말이 후보에만 붙어 있으면 다른 SKU로 본다.
  // 상품명이 짧으면 토큰 비율만으로는 못 걸러진다 — "코리아보드게임즈 할리갈리"와
  // "코리아보드게임즈 할리갈리 디럭스"는 reverse가 0.67이라 통과해버린다.
  const VARIANT = /디럭스|딜럭스|스페셜|에디션|리미티드|한정|프리미엄|플러스|미니|대형|특대|확장|리뉴얼|콜라보|기획|증정|[0-9]+개입|[0-9]+세트/;
  const variantOnlyInCand = VARIANT.test(cand.productName) && !VARIANT.test(product.name);

  let confidence = 'none';
  if (variantOnlyInCand) confidence = overlap >= 0.45 ? 'review' : 'none';
  else if (codeHit && ratio >= 0.55 && reverse >= 0.5) confidence = 'high';
  else if (codeHit) confidence = 'review';
  else if (overlap >= 0.6 && ratio >= 0.7 && reverse >= 0.65) confidence = 'high';
  else if (overlap >= 0.45 && ratio >= 0.55) confidence = 'review';
  else if (overlap >= 0.3) confidence = 'review';

  return { confidence, overlap, reverse, ratio, codeHit, variantOnlyInCand };
}

async function main() {
  const args = process.argv.slice(2);
  const apply = args.includes('--apply');
  const guideIdx = args.indexOf('--guide');
  const onlyGuide = guideIdx !== -1 ? args[guideIdx + 1] : null;

  const notion = new Client({ auth: process.env.NOTION_API_KEY });
  const { guides, products } = JSON.parse(readFileSync(CACHE, 'utf8'));
  const guideSlug = new Map(guides.map(g => [g.id, g.slug]));

  let targets = products
    .filter(p => !p.coupangUrl && p.naverUrl)
    .map(p => ({ ...p, guide: guideSlug.get(p.guideId) ?? '(연결없음)' }))
    .filter(p => p.guide !== '(연결없음)');

  if (onlyGuide) targets = targets.filter(p => p.guide === onlyGuide);

  console.log(`대상 ${targets.length}개 상품 / ${new Set(targets.map(t => t.guide)).size}개 가이드\n`);

  const results = [];
  for (const [i, product] of targets.entries()) {
    const query = toQuery(product.name);
    let cands = [];
    try {
      cands = await searchCoupangProducts(query, 8);
    } catch (err) {
      console.error(`  검색 실패: ${product.name.slice(0, 30)} — ${err.message}`);
    }

    const scored = cands
      .map(c => ({ cand: c, ...scoreMatch(product, c) }))
      .sort((a, b) => (b.confidence === 'high') - (a.confidence === 'high') || b.overlap - a.overlap);

    const best = scored[0];
    results.push({ product, query, best: best ?? null });

    const tag = !best || best.confidence === 'none' ? '✗ 없음'
      : best.confidence === 'high' ? '✓ 확신'
      : '? 확인필요';
    console.log(`[${String(i + 1).padStart(3)}/${targets.length}] ${tag}  [${product.guide}] ${product.name.slice(0, 32)}`);
    if (best && best.confidence !== 'none') {
      console.log(`        → ${best.cand.productPrice.toLocaleString()}원 (원가 ${product.price?.toLocaleString()}원) ${best.cand.productName.slice(0, 48)}`);
    }
  }

  const high = results.filter(r => r.best?.confidence === 'high');
  const review = results.filter(r => r.best?.confidence === 'review');
  const none = results.filter(r => !r.best || r.best.confidence === 'none');

  console.log(`\n확신 ${high.length} / 확인필요 ${review.length} / 매칭없음 ${none.length}`);

  const reportPath = join(ROOT, `coupang-match-report-${Date.now()}.json`);
  writeFileSync(reportPath, JSON.stringify(
    results.map(r => ({
      guide: r.product.guide,
      productId: r.product.id,
      원본: { name: r.product.name, price: r.product.price },
      검색어: r.query,
      confidence: r.best?.confidence ?? 'none',
      후보: r.best?.cand ? { name: r.best.cand.productName, price: r.best.cand.productPrice, url: r.best.cand.productUrl } : null,
      지표: r.best ? { overlap: +r.best.overlap.toFixed(2), reverse: +r.best.reverse.toFixed(2), priceRatio: +r.best.ratio.toFixed(2), codeHit: r.best.codeHit } : null,
    })), null, 2), 'utf8');
  console.log(`리포트: ${reportPath}`);

  if (!apply) {
    console.log('\n미리보기입니다. 확신 건만 반영하려면 --apply 를 붙일 것.');
    return;
  }

  // 확신 건만 영구 딥링크로 변환해 반영
  const plains = high.map(r => {
    const u = new URL(r.best.cand.productUrl);
    return `https://www.coupang.com/vp/products/${u.searchParams.get('pageKey')}?itemId=${u.searchParams.get('itemId')}&vendorItemId=${u.searchParams.get('vendorItemId')}`;
  });

  const linkMap = {};
  for (let i = 0; i < plains.length; i += 20) {
    Object.assign(linkMap, await createDeeplinks(plains.slice(i, i + 20), 'link-match-20260903'));
  }

  let ok = 0;
  for (const [i, r] of high.entries()) {
    const shorten = linkMap[plains[i]];
    if (!shorten) { console.error(`  ✗ 변환 실패: ${r.product.name.slice(0, 30)}`); continue; }
    await notion.pages.update({ page_id: r.product.id, properties: { coupangUrl: { url: shorten } } });
    console.log(`  ✓ [${r.product.guide}] ${r.product.name.slice(0, 30)} → ${shorten}`);
    ok++;
    await sleep(350);
  }
  console.log(`\n반영 ${ok}/${high.length}. 다음: python scripts/dump_cache.py`);
}

main().catch(err => { console.error(err); process.exit(1); });
