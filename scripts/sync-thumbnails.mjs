// 가이드 썸네일을 1순위 상품 이미지와 자동 동기화한다.
// - thumbnailLocked 체크된 가이드는 건드리지 않음(관리자가 수동으로 고정)
// - 상품 이미지가 없는 가이드는 기존 값(Unsplash 등 대체 이미지)을 그대로 둠
// - 1순위 상품의 이미지 URL이 매니페스트와 다르면(=상품이 바뀌었으면) 새로 받아서 교체
// npm run build 안에서 astro build보다 먼저 실행된다.

import { Client } from '@notionhq/client';
import sharp from 'sharp';
import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');

// .env가 있으면 읽어서 채운다(이미 설정된 값은 덮어쓰지 않음 — CI의 실제 시크릿이 우선).
const envPath = join(ROOT, '.env');
if (existsSync(envPath)) {
  for (const line of readFileSync(envPath, 'utf-8').split('\n')) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) continue;
    const eq = trimmed.indexOf('=');
    if (eq === -1) continue;
    const key = trimmed.slice(0, eq).trim();
    const val = trimmed.slice(eq + 1).trim().replace(/^["']|["']$/g, '');
    if (!(key in process.env)) process.env[key] = val;
  }
}

const NOTION_API_KEY = process.env.NOTION_API_KEY;
const GUIDES_DB = process.env.NOTION_GUIDES_DB_ID;
const PRODUCTS_DB = process.env.NOTION_PRODUCTS_DB_ID;
const SITE = 'https://gift.infoepic.com';
const THUMB_DIR = join(ROOT, 'public', 'thumbnails');
const MANIFEST_PATH = join(ROOT, 'src', 'data', 'thumbnail-manifest.json');

if (!NOTION_API_KEY || !GUIDES_DB || !PRODUCTS_DB) {
  console.log('[thumbnail-sync] Notion 환경변수 없음 — 건너뜀');
  process.exit(0);
}

const notion = new Client({ auth: NOTION_API_KEY });

async function queryAll(database_id, filter) {
  let results = [];
  let cursor;
  do {
    const res = await notion.databases.query({
      database_id,
      ...(filter ? { filter } : {}),
      ...(cursor ? { start_cursor: cursor } : {}),
      page_size: 100,
    });
    results = results.concat(res.results);
    cursor = res.has_more ? res.next_cursor : undefined;
  } while (cursor);
  return results;
}

function loadManifest() {
  try {
    return JSON.parse(readFileSync(MANIFEST_PATH, 'utf-8'));
  } catch {
    return {};
  }
}

async function main() {
  if (!existsSync(THUMB_DIR)) mkdirSync(THUMB_DIR, { recursive: true });
  const manifest = loadManifest();

  const [guides, products] = await Promise.all([
    queryAll(GUIDES_DB, { property: 'published', checkbox: { equals: true } }),
    queryAll(PRODUCTS_DB),
  ]);

  const prodsByGuide = new Map();
  for (const p of products) {
    const rel = p.properties.giftGuide?.relation?.[0]?.id;
    const imageUrl = (p.properties.imageUrl?.rich_text || []).map((t) => t.plain_text).join('');
    if (!rel || !imageUrl) continue;
    const rank = p.properties.rank?.number ?? 99;
    const list = prodsByGuide.get(rel) || [];
    list.push({ rank, imageUrl });
    prodsByGuide.set(rel, list);
  }

  let checked = 0;
  let changed = 0;
  let failed = 0;

  for (const g of guides) {
    const gid = g.id;
    const locked = g.properties.thumbnailLocked?.checkbox === true;
    if (locked) continue;

    const list = prodsByGuide.get(gid);
    if (!list || list.length === 0) continue; // 상품 이미지 없음 — 기존 썸네일(있다면 Unsplash 등) 유지

    list.sort((a, b) => a.rank - b.rank);
    const desiredUrl = list[0].imageUrl;
    checked++;

    const current = manifest[gid];
    if (current && current.sourceType === 'product' && current.sourceUrl === desiredUrl) {
      continue; // 1순위 상품 이미지가 그대로 — 변경 없음
    }

    try {
      const res = await fetch(desiredUrl, { headers: { 'User-Agent': 'Mozilla/5.0' } });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const buf = Buffer.from(await res.arrayBuffer());
      const resized = await sharp(buf)
        .resize({ width: 800, withoutEnlargement: true })
        .jpeg({ quality: 80, mozjpeg: true })
        .toBuffer();
      const fname = `${gid}.jpg`;
      writeFileSync(join(THUMB_DIR, fname), resized);

      manifest[gid] = { sourceType: 'product', sourceUrl: desiredUrl };
      changed++;

      try {
        await notion.pages.update({
          page_id: gid,
          properties: {
            thumbnail: { rich_text: [{ text: { content: `${SITE}/thumbnails/${fname}` } }] },
          },
        });
      } catch (e) {
        console.warn(`[thumbnail-sync] Notion thumbnail 필드 갱신 실패 (${gid}): ${e.message}`);
      }
    } catch (e) {
      failed++;
      console.warn(`[thumbnail-sync] 이미지 다운로드 실패 (${gid}): ${e.message}`);
    }
  }

  writeFileSync(MANIFEST_PATH, JSON.stringify(manifest, null, 2), 'utf-8');
  console.log(`[thumbnail-sync] 확인 ${checked}건, 갱신 ${changed}건, 실패 ${failed}건`);
}

main().catch((e) => {
  console.error('[thumbnail-sync] 오류:', e);
  process.exit(0); // 썸네일 동기화 실패로 전체 배포가 막히지 않도록 함
});
