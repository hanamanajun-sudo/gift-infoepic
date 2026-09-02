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

/**
 * 설정 파일이 내보낸 속성만 골라 Notion 형식으로 바꾼다.
 * 내보내지 않은 속성은 아예 넣지 않아서 기존 값이 지워지지 않게 한다
 * (재큐레이션할 때 손으로 넣어둔 값을 규칙이 덮으면 안 되기 때문).
 */
function buildProperties(config) {
  const props = {};
  if (config.title) props.Title = { title: [{ text: { content: config.title } }] };
  if (config.description) props.description = { rich_text: [{ text: { content: config.description } }] };
  if (config.intro) props.intro = { rich_text: [{ text: { content: config.intro } }] };
  for (const key of ['occasion', 'relation', 'ageGroup', 'budgetTag', 'interests']) {
    if (config[key]) props[key] = { multi_select: config[key].map(name => ({ name })) };
  }
  if (config.priceMin != null) props.priceMin = { number: config.priceMin };
  if (config.priceMax != null) props.priceMax = { number: config.priceMax };
  if (config.recipientGender) props.recipientGender = { select: { name: config.recipientGender } };
  return props;
}

const existing = await notion.databases.query({
  database_id: GUIDES_DB_ID,
  filter: { property: 'slug', rich_text: { equals: slug } },
});

if (existing.results.length === 0) {
  const page = await notion.pages.create({
    parent: { database_id: GUIDES_DB_ID },
    properties: {
      ...buildProperties(config),
      slug: { rich_text: [{ text: { content: slug } }] },
      published: { checkbox: true },
    },
  });
  console.log(`[${slug}] 신규 가이드 페이지 생성: ${page.id}`);
} else {
  const pageId = existing.results[0].id;
  await notion.pages.update({ page_id: pageId, properties: buildProperties(config) });
  console.log(`[${slug}] 기존 가이드 속성 갱신 (${pageId})`);
}

await pushGuide(config);
