// 로컬 전용 썸네일 관리 도구. 127.0.0.1에만 바인딩 — 외부에서 접근 불가.
// 실행: npm run thumbnail-admin  ->  http://localhost:4321/ 열기
//
// 여기서 지정한 썸네일은 thumbnailLocked=true로 표시되어
// scripts/sync-thumbnails.mjs(빌드 시 자동 동기화)가 건드리지 않는다.
// "자동으로 되돌리기"를 누르면 잠금이 풀려 다시 1순위 상품 이미지를 따라간다.

import { createServer } from 'http';
import { Client } from '@notionhq/client';
import sharp from 'sharp';
import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const PORT = 4321;

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
  console.error('NOTION_API_KEY / NOTION_GUIDES_DB_ID / NOTION_PRODUCTS_DB_ID가 .env에 필요합니다.');
  process.exit(1);
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
function saveManifest(m) {
  writeFileSync(MANIFEST_PATH, JSON.stringify(m, null, 2), 'utf-8');
}

async function fetchGuideList() {
  const [guides, products] = await Promise.all([
    queryAll(GUIDES_DB, { property: 'published', checkbox: { equals: true } }),
    queryAll(PRODUCTS_DB),
  ]);
  const prodsByGuide = new Map();
  for (const p of products) {
    const rel = p.properties.giftGuide?.relation?.[0]?.id;
    const imageUrl = (p.properties.imageUrl?.rich_text || []).map((t) => t.plain_text).join('');
    if (!rel) continue;
    const rank = p.properties.rank?.number ?? 99;
    const list = prodsByGuide.get(rel) || [];
    list.push({ rank, imageUrl });
    prodsByGuide.set(rel, list);
  }

  return guides
    .map((g) => {
      const title = g.properties.Title?.title?.map((t) => t.plain_text).join('') || '';
      const slug = (g.properties.slug?.rich_text || []).map((t) => t.plain_text).join('');
      const thumbnail = (g.properties.thumbnail?.rich_text || []).map((t) => t.plain_text).join('');
      const locked = g.properties.thumbnailLocked?.checkbox === true;
      const list = (prodsByGuide.get(g.id) || []).filter((p) => p.imageUrl).sort((a, b) => a.rank - b.rank);
      return {
        id: g.id,
        slug,
        title,
        thumbnail,
        locked,
        hasProductImage: list.length > 0,
      };
    })
    .sort((a, b) => a.title.localeCompare(b.title, 'ko'));
}

async function saveThumbnail(guideId, buffer) {
  const resized = await sharp(buffer).resize({ width: 800, withoutEnlargement: true }).jpeg({ quality: 82, mozjpeg: true }).toBuffer();
  if (!existsSync(THUMB_DIR)) mkdirSync(THUMB_DIR, { recursive: true });
  const fname = `${guideId}.jpg`;
  writeFileSync(join(THUMB_DIR, fname), resized);
  const url = `${SITE}/thumbnails/${fname}`;

  await notion.pages.update({
    page_id: guideId,
    properties: {
      thumbnail: { rich_text: [{ text: { content: url } }] },
      thumbnailLocked: { checkbox: true },
    },
  });

  const manifest = loadManifest();
  manifest[guideId] = { sourceType: 'manual', sourceUrl: null };
  saveManifest(manifest);

  return url;
}

async function unlockThumbnail(guideId) {
  await notion.pages.update({
    page_id: guideId,
    properties: { thumbnailLocked: { checkbox: false } },
  });
  const manifest = loadManifest();
  delete manifest[guideId]; // 다음 빌드 시 sync-thumbnails.mjs가 상품 이미지로 다시 채움
  saveManifest(manifest);
}

const HTML = `<!doctype html>
<html lang="ko"><head><meta charset="utf-8">
<title>썸네일 관리자</title>
<style>
  :root { color-scheme: light; }
  body { font-family: -apple-system, "Pretendard", sans-serif; max-width: 900px; margin: 0 auto; padding: 24px 16px 80px; background: #faf9fc; color: #1f1b2e; }
  h1 { font-size: 1.4rem; margin-bottom: 4px; }
  .hint { color: #6b6478; font-size: 0.85rem; margin-bottom: 20px; }
  .search { width: 100%; padding: 10px 14px; border: 1px solid #ddd7e8; border-radius: 10px; font-size: 0.95rem; margin-bottom: 16px; box-sizing: border-box; }
  .card { display: flex; gap: 14px; align-items: center; background: #fff; border: 1px solid #ece7f5; border-radius: 12px; padding: 12px; margin-bottom: 10px; }
  .card img { width: 96px; height: 54px; object-fit: cover; border-radius: 8px; background: #eee; flex-shrink: 0; }
  .card .noimg { width: 96px; height: 54px; border-radius: 8px; background: #ece7f5; flex-shrink: 0; display:flex; align-items:center; justify-content:center; font-size:0.7rem; color:#8a80a3; }
  .info { flex: 1; min-width: 0; }
  .title { font-weight: 600; font-size: 0.92rem; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .slug { color: #9088a3; font-size: 0.78rem; }
  .badge { display: inline-block; font-size: 0.7rem; padding: 1px 7px; border-radius: 999px; margin-left: 6px; }
  .badge.locked { background: #fde8e8; color: #c0392b; }
  .badge.auto { background: #e8f3ea; color: #2a7a3d; }
  .actions { display: flex; gap: 6px; flex-shrink: 0; }
  button, .filebtn { border: 1px solid #ddd7e8; background: #fff; border-radius: 8px; padding: 7px 12px; font-size: 0.8rem; cursor: pointer; color: #443d59; }
  button:hover, .filebtn:hover { background: #f3effa; }
  button.unlock { color: #2a7a3d; }
  input[type=file] { display: none; }
  .status { font-size: 0.75rem; color: #6b6478; margin-top: 4px; }
</style></head>
<body>
  <h1>썸네일 관리자</h1>
  <p class="hint">로컬 전용 도구입니다. 파일을 선택하거나 이미지 URL을 붙여넣으면 바로 Notion에 반영되고, 이후 빌드 자동 동기화 대상에서 제외됩니다("자동으로 되돌리기"로 해제 가능).</p>
  <input class="search" id="search" placeholder="가이드 제목/슬러그 검색...">
  <div id="list">불러오는 중...</div>

<script>
let guides = [];

async function load() {
  const res = await fetch('/api/guides');
  guides = await res.json();
  render();
}

function esc(s) {
  const d = document.createElement('div');
  d.textContent = s ?? '';
  return d.innerHTML;
}

function render() {
  const q = document.getElementById('search').value.trim().toLowerCase();
  const filtered = guides.filter(g => !q || g.title.toLowerCase().includes(q) || g.slug.toLowerCase().includes(q));
  const list = document.getElementById('list');
  list.innerHTML = filtered.map(g => \`
    <div class="card" data-id="\${esc(g.id)}">
      \${g.thumbnail ? \`<img src="\${esc(g.thumbnail)}?t=\${Date.now()}" alt="">\` : '<div class="noimg">없음</div>'}
      <div class="info">
        <div class="title">\${esc(g.title)}\${g.locked ? '<span class="badge locked">수동 고정</span>' : '<span class="badge auto">자동</span>'}</div>
        <div class="slug">\${esc(g.slug)}</div>
        <div class="status" data-status></div>
      </div>
      <div class="actions">
        <label class="filebtn">파일 선택<input type="file" accept="image/*" onchange="uploadFile('\${esc(g.id)}', this)"></label>
        <button onclick="promptUrl('\${esc(g.id)}')">URL 붙여넣기</button>
        \${g.locked ? \`<button class="unlock" onclick="unlock('\${esc(g.id)}')">자동으로 되돌리기</button>\` : ''}
      </div>
    </div>
  \`).join('');
}

function setStatus(id, text) {
  const el = document.querySelector(\`.card[data-id="\${id}"] [data-status]\`);
  if (el) el.textContent = text;
}

async function uploadFile(id, input) {
  const file = input.files[0];
  if (!file) return;
  setStatus(id, '업로드 중...');
  const reader = new FileReader();
  reader.onload = async () => {
    const res = await fetch('/api/thumbnail', {
      method: 'POST', headers: {'Content-Type':'application/json'},
      body: JSON.stringify({ guideId: id, imageDataUrl: reader.result })
    });
    if (res.ok) { setStatus(id, '완료'); await load(); } else { setStatus(id, '실패: ' + await res.text()); }
  };
  reader.readAsDataURL(file);
}

async function promptUrl(id) {
  const url = prompt('이미지 URL을 붙여넣으세요');
  if (!url) return;
  setStatus(id, '가져오는 중...');
  const res = await fetch('/api/thumbnail-url', {
    method: 'POST', headers: {'Content-Type':'application/json'},
    body: JSON.stringify({ guideId: id, url })
  });
  if (res.ok) { setStatus(id, '완료'); await load(); } else { setStatus(id, '실패: ' + await res.text()); }
}

async function unlock(id) {
  await fetch('/api/unlock', { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify({ guideId: id }) });
  await load();
}

document.getElementById('search').addEventListener('input', render);
load();
</script>
</body></html>`;

function send(res, status, body, headers = {}) {
  res.writeHead(status, { 'Content-Type': 'text/plain; charset=utf-8', ...headers });
  res.end(body);
}

const server = createServer(async (req, res) => {
  try {
    if (req.method === 'GET' && req.url === '/') {
      res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
      res.end(HTML);
      return;
    }
    if (req.method === 'GET' && req.url === '/api/guides') {
      const list = await fetchGuideList();
      res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
      res.end(JSON.stringify(list));
      return;
    }
    if (req.method === 'POST' && (req.url === '/api/thumbnail' || req.url === '/api/thumbnail-url' || req.url === '/api/unlock')) {
      let body = '';
      for await (const chunk of req) body += chunk;
      const data = JSON.parse(body || '{}');

      if (req.url === '/api/unlock') {
        await unlockThumbnail(data.guideId);
        return send(res, 200, 'ok');
      }

      let buffer;
      if (req.url === '/api/thumbnail') {
        const match = /^data:.*?;base64,(.*)$/.exec(data.imageDataUrl || '');
        if (!match) return send(res, 400, '잘못된 이미지 데이터');
        buffer = Buffer.from(match[1], 'base64');
      } else {
        const r = await fetch(data.url, { headers: { 'User-Agent': 'Mozilla/5.0' } });
        if (!r.ok) return send(res, 400, `이미지 URL 요청 실패 (HTTP ${r.status})`);
        buffer = Buffer.from(await r.arrayBuffer());
      }

      const url = await saveThumbnail(data.guideId, buffer);
      return send(res, 200, url);
    }
    send(res, 404, 'not found');
  } catch (e) {
    console.error(e);
    send(res, 500, String(e.message || e));
  }
});

server.listen(PORT, '127.0.0.1', () => {
  console.log(`썸네일 관리자: http://localhost:${PORT}/  (Ctrl+C로 종료)`);
});
