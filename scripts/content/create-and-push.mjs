/**
 * 새 가이드 생성 + 발행 (일회성 헬퍼).
 *
 * push.mjs는 findGuideId()가 기존 Notion 페이지를 찾는 걸 전제로 한다
 * (없으면 에러를 던진다). 완전히 새로운 가이드를 만들 때는 먼저 페이지 자체를
 * 필요한 속성(Title·slug·description·occasion·relation·budgetTag·priceMin/Max·
 * published)까지 채워서 생성한 다음, 같은 push.mjs 로직(블록·상품 채우기)을 태운다.
 *
 * 사용법: node --env-file=.env scripts/content/create-and-push.mjs <슬러그>
 * guides/<슬러그>.mjs 가 slug 외에 title·description·occasion·relation·
 * budgetTag·priceMin·priceMax 를 함께 export 해야 한다.
 */

import { notion, GUIDES_DB_ID, pushGuide } from './lib.mjs';
import { readFileSync } from 'fs';

const envContent = readFileSync(new URL('../../.env', import.meta.url), 'utf-8');
for (const line of envContent.split('\n')) {
  const t = line.trim();
  if (t && !t.startsWith('#') && t.includes('=')) {
    const i = t.indexOf('=');
    const k = t.slice(0, i).trim();
    let v = t.slice(i + 1).trim();
    if (v.startsWith('"') && v.endsWith('"')) v = v.slice(1, -1);
    if (!process.env[k]) process.env[k] = v;
  }
}

const slug = process.argv[2];
if (!slug) {
  console.error('가이드 슬러그를 넘겨주세요. 예: node scripts/content/create-and-push.mjs 추석-선물-직장상사');
  process.exit(1);
}

const config = await import(`./guides/${slug}.mjs`);

const existing = await notion.databases.query({
  database_id: GUIDES_DB_ID,
  filter: { property: 'slug', rich_text: { equals: slug } },
});

if (existing.results.length === 0) {
  const page = await notion.pages.create({
    parent: { database_id: GUIDES_DB_ID },
    properties: {
      Title: { title: [{ text: { content: config.title } }] },
      slug: { rich_text: [{ text: { content: slug } }] },
      description: { rich_text: [{ text: { content: config.description } }] },
      intro: { rich_text: [{ text: { content: config.intro } }] },
      occasion: { multi_select: (config.occasion ?? []).map(name => ({ name })) },
      relation: { multi_select: (config.relation ?? []).map(name => ({ name })) },
      ageGroup: { multi_select: (config.ageGroup ?? []).map(name => ({ name })) },
      budgetTag: { multi_select: (config.budgetTag ?? []).map(name => ({ name })) },
      ...(config.priceMin != null ? { priceMin: { number: config.priceMin } } : {}),
      ...(config.priceMax != null ? { priceMax: { number: config.priceMax } } : {}),
      ...(config.recipientGender ? { recipientGender: { select: { name: config.recipientGender } } } : {}),
      published: { checkbox: true },
    },
  });
  console.log(`[${slug}] 신규 가이드 페이지 생성: ${page.id}`);
} else {
  console.log(`[${slug}] 이미 존재하는 가이드 (${existing.results[0].id}) — 속성은 건드리지 않고 콘텐츠만 갱신합니다.`);
}

await pushGuide(config);
