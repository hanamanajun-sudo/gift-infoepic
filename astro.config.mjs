import { readFileSync } from 'node:fs';
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import tailwindcss from '@tailwindcss/vite';

function rehypeLazyImages() {
  function walk(node) {
    if (node.type === 'element' && node.tagName === 'img') {
      node.properties = node.properties || {};
      if (!node.properties.loading) node.properties.loading = 'lazy';
      if (!node.properties.decoding) node.properties.decoding = 'async';
    }
    if (node.children) node.children.forEach(walk);
  }
  return (tree) => walk(tree);
}

// ── sitemap lastmod ──
//
// ⚠️ 현재 꺼져 있다. 켜지 말 것 — 아래 조건이 충족되기 전까지는 가짜 신선도 신호가 된다.
//
// 이유: Notion의 updatedAt이 실제 콘텐츠 변경 이력을 반영하지 않는다.
// 2026-08-19 썸네일 동기화 스크립트가 전 가이드의 Notion 페이지를 일괄 수정해서
// 102개 중 98개가 2026-08-19, 4개가 2026-08-20으로 뭉쳐 있다.
// 이대로 내보내면 sitemap 165개 URL 중 142개가 같은 날짜가 되는데,
// 이런 획일적 lastmod는 구글이 신뢰하지 않거나 사이트 전체에서 무시한다.
//
// 켜도 되는 시점: 가이드를 개별적으로 재작성·큐레이션하기 시작해서
// updatedAt이 페이지마다 실제로 갈라진 뒤. (STRATEGY-2026-09.md의 Tier 0·3 진행 후)
// 판정 기준: `node -e "const c=require('./src/data/notion-cache.json');
//   console.log(new Set(c.guides.map(g=>g.updatedAt.slice(0,10))).size)"` 가
// 최소 10 이상이면 의미 있는 분포로 본다.
const EMIT_LASTMOD = false;

function buildLastmodMap() {
  const { guides } = JSON.parse(readFileSync('./src/data/notion-cache.json', 'utf8'));
  const map = new Map();

  const latest = (key, iso) => {
    const prev = map.get(key);
    if (!prev || iso > prev) map.set(key, iso);
  };

  for (const g of guides) {
    const iso = new Date(g.updatedAt).toISOString();
    map.set(`/선물/${g.slug}/`, iso);

    latest('/', iso);
    for (const v of g.ageGroup) { latest(`/나이/${v}/`, iso); latest('/나이/', iso); }
    for (const v of g.occasion) { latest(`/상황/${v}/`, iso); latest('/상황/', iso); }
    for (const v of g.relation) { latest(`/관계/${v}/`, iso); latest('/관계/', iso); }
    for (const v of g.budgetTag) { latest(`/예산/${v}/`, iso); latest('/예산/', iso); }
  }

  // 키를 sitemap이 내보내는 형태(퍼센트 인코딩)로 맞춰 둔다
  return new Map([...map].map(([path, iso]) => [encodeURI(path), iso]));
}

const lastmodByPath = EMIT_LASTMOD ? buildLastmodMap() : new Map();

export default defineConfig({
  site: 'https://gift.infoepic.com',
  integrations: [
    sitemap({
      filter: (page) => !page.includes('/search'),
      serialize(item) {
        const path = new URL(item.url).pathname;
        const lastmod = lastmodByPath.get(path) ?? lastmodByPath.get(`${path}/`);
        if (lastmod) item.lastmod = lastmod;
        return item;
      },
    }),
  ],
  markdown: {
    rehypePlugins: [rehypeLazyImages],
  },
  output: 'static',
  trailingSlash: 'ignore',
  vite: {
    plugins: [tailwindcss()],
  },
});
