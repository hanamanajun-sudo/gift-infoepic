/**
 * 만료되는 쿠팡 링크 일괄 교체.
 *
 * 근본 원인 (2026-09-03 발견): `searchCoupangProducts()`가 돌려주는 productUrl은
 * 그 검색 요청 하나에 서명된 임시 링크다. 실측 — 같은 상품을 몇 분 간격으로
 * 두 번 검색하면 requestid·token이 매번 바뀐다. 이 링크를 Notion에 저장해두면
 * 며칠 뒤 방문자가 눌렀을 때 "요청하신 페이지의 사용권한이 없습니다"로 막힌다.
 * 추석-선물 발행 당일 실제로 겪었다.
 *
 * 저장·게시용 영구 링크는 별도의 Deeplink API(POST .../v1/deeplink)를 호출해서
 * 평문 상품 URL(coupang.com/vp/products/{id}?itemId=&vendorItemId=)을
 * `https://link.coupang.com/a/xxxxxxxxxx` 형태로 변환해야 한다.
 *
 * 이 스크립트는 Notion Products DB 전체에서 `token=` 파라미터가 붙은
 * (=검색 API가 직접 돌려준, 만료 위험이 있는) coupangUrl을 찾아 영구 링크로 교체한다.
 * "이미 /a/ 형태인 것", "token 없는 구형 링크"(수동으로 만든 것으로 보임)는 건드리지 않는다.
 *
 * 사용법:
 *   node --env-file=.env scripts/fix-coupang-links.mjs            # 미리보기
 *   node --env-file=.env scripts/fix-coupang-links.mjs --apply    # 실제 반영 + 로그 저장
 *
 * 반영 뒤 `python scripts/dump_cache.py` 필수.
 */

import { Client } from '@notionhq/client';
import { readFileSync, writeFileSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createDeeplinks } from '../src/lib/coupang.ts';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const CACHE = join(ROOT, 'src/data/notion-cache.json');
const CHUNK = 20; // Deeplink API 1회 호출당 최대 URL 수 (실측: 21개부터 400 에러)
const sleep = ms => new Promise(r => setTimeout(r, ms));

function toPlainUrl(coupangUrl) {
  const u = new URL(coupangUrl);
  const itemId = u.searchParams.get('itemId');
  const vendorItemId = u.searchParams.get('vendorItemId');
  const productId = u.searchParams.get('pageKey');
  if (!itemId || !vendorItemId || !productId) return null;
  return `https://www.coupang.com/vp/products/${productId}?itemId=${itemId}&vendorItemId=${vendorItemId}`;
}

async function main() {
  const apply = process.argv.includes('--apply');
  const notion = new Client({ auth: process.env.NOTION_API_KEY });

  const { guides, products } = JSON.parse(readFileSync(CACHE, 'utf8'));
  const guideSlug = new Map(guides.map(g => [g.id, g.slug]));

  const targets = products
    .filter(p => p.coupangUrl && p.coupangUrl.includes('/re/AFFSDP') && p.coupangUrl.includes('token='))
    .map(p => ({ id: p.id, name: p.name, guide: guideSlug.get(p.guideId) ?? p.guideId, oldUrl: p.coupangUrl, plainUrl: toPlainUrl(p.coupangUrl) }))
    .filter(t => t.plainUrl);

  const skipped = products.filter(p => p.coupangUrl && p.coupangUrl.includes('/re/AFFSDP') && p.coupangUrl.includes('token=')).length - targets.length;

  console.log(`대상: ${targets.length}개 링크 (파싱 실패로 건너뜀: ${skipped}개)`);
  console.log(`영향받는 가이드: ${new Set(targets.map(t => t.guide)).size}개`);
  console.log(`청크 수: ${Math.ceil(targets.length / CHUNK)} (1청크당 최대 ${CHUNK}개)\n`);

  if (!apply) {
    console.log('미리보기입니다. 첫 5개 샘플:');
    for (const t of targets.slice(0, 5)) console.log(`  [${t.guide}] ${t.name.slice(0, 30)} → ${t.plainUrl}`);
    console.log('\n반영하려면 --apply 를 붙일 것.');
    return;
  }

  const log = { startedAt: new Date().toISOString(), fixed: [], failed: [] };

  for (let i = 0; i < targets.length; i += CHUNK) {
    const chunk = targets.slice(i, i + CHUNK);
    console.log(`\n[청크 ${Math.floor(i / CHUNK) + 1}/${Math.ceil(targets.length / CHUNK)}] ${chunk.length}개 변환 중...`);

    const map = await createDeeplinks(chunk.map(t => t.plainUrl), 'sitewide-fix-20260903');

    for (const t of chunk) {
      const shorten = map[t.plainUrl];
      if (!shorten) {
        console.error(`  ✗ 변환 실패: [${t.guide}] ${t.name.slice(0, 30)}`);
        log.failed.push(t);
        continue;
      }
      try {
        await notion.pages.update({ page_id: t.id, properties: { coupangUrl: { url: shorten } } });
        console.log(`  ✓ [${t.guide}] ${t.name.slice(0, 30)} → ${shorten}`);
        log.fixed.push({ ...t, newUrl: shorten });
      } catch (err) {
        console.error(`  ✗ Notion 갱신 실패: [${t.guide}] ${t.name.slice(0, 30)} — ${err.message}`);
        log.failed.push({ ...t, error: err.message });
      }
      await sleep(350);
    }
  }

  const logPath = join(ROOT, `coupang-link-fix-log-${Date.now()}.json`);
  writeFileSync(logPath, JSON.stringify(log, null, 2), 'utf8');

  console.log(`\n완료: ${log.fixed.length}/${targets.length} 성공, ${log.failed.length}개 실패`);
  console.log(`로그: ${logPath}`);
  console.log('\n다음: python scripts/dump_cache.py');
}

main().catch(err => { console.error(err); process.exit(1); });
