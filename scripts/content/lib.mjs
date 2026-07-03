import { Client } from '@notionhq/client';

export const notion = new Client({ auth: process.env.NOTION_API_KEY });
export const GUIDES_DB_ID = process.env.NOTION_GUIDES_DB_ID;
export const PRODUCTS_DB_ID = process.env.NOTION_PRODUCTS_DB_ID;

export const rt = (text, opts = {}) => [{ type: 'text', text: { content: text }, annotations: opts }];
export const h2 = (text) => ({ object: 'block', type: 'heading_2', heading_2: { rich_text: rt(text) } });
export const h3 = (text) => ({ object: 'block', type: 'heading_3', heading_3: { rich_text: rt(text) } });
export const p = (text) => ({ object: 'block', type: 'paragraph', paragraph: { rich_text: rt(text) } });
export const bullet = (text) => ({ object: 'block', type: 'bulleted_list_item', bulleted_list_item: { rich_text: rt(text) } });

export function table(headerRow, rows) {
  const toRow = (cells) => ({
    object: 'block',
    type: 'table_row',
    table_row: { cells: cells.map((c) => rt(c)) },
  });
  return {
    object: 'block',
    type: 'table',
    table: {
      table_width: headerRow.length,
      has_column_header: true,
      has_row_header: false,
      children: [toRow(headerRow), ...rows.map(toRow)],
    },
  };
}

async function findGuideId(slug) {
  const search = await notion.databases.query({
    database_id: GUIDES_DB_ID,
    filter: { property: 'slug', rich_text: { equals: slug } },
  });
  const guide = search.results[0];
  if (!guide) throw new Error(`슬러그 "${slug}"를 가진 가이드를 찾지 못했습니다.`);
  return guide.id;
}

// config: { slug, intro, blocks, products: [{ name, price, naverUrl, coupangUrl?, imageUrl, rank, pros }] }
export async function pushGuide(config) {
  const guideId = await findGuideId(config.slug);
  console.log(`[${config.slug}] 가이드 페이지: ${guideId}`);

  if (config.intro) {
    await notion.pages.update({ page_id: guideId, properties: { intro: { rich_text: rt(config.intro) } } });
    console.log(`[${config.slug}] intro 갱신 완료`);
  }

  const existing = await notion.blocks.children.list({ block_id: guideId });
  for (const block of existing.results) {
    await notion.blocks.delete({ block_id: block.id });
  }
  console.log(`[${config.slug}] 기존 블록 ${existing.results.length}개 삭제 완료`);

  await notion.blocks.children.append({ block_id: guideId, children: config.blocks });
  console.log(`[${config.slug}] 새 블록 ${config.blocks.length}개 추가 완료`);

  if (config.products && config.products.length > 0) {
    const existingProducts = await notion.databases.query({
      database_id: PRODUCTS_DB_ID,
      filter: { property: 'giftGuide', relation: { contains: guideId } },
    });
    for (const page of existingProducts.results) {
      await notion.pages.update({ page_id: page.id, archived: true });
    }
    if (existingProducts.results.length > 0) {
      console.log(`[${config.slug}] 기존 연결 상품 ${existingProducts.results.length}개 아카이브 완료`);
    }

    for (const product of config.products) {
      await notion.pages.create({
        parent: { database_id: PRODUCTS_DB_ID },
        properties: {
          Title: { title: [{ text: { content: product.name } }] },
          giftGuide: { relation: [{ id: guideId }] },
          price: { number: product.price },
          naverUrl: { url: product.naverUrl },
          ...(product.coupangUrl ? { coupangUrl: { url: product.coupangUrl } } : {}),
          imageUrl: { rich_text: [{ text: { content: product.imageUrl } }] },
          rank: { number: product.rank },
          pros: { rich_text: [{ text: { content: product.pros } }] },
        },
      });
      console.log(`[${config.slug}] 상품 생성: ${product.name}`);
    }
  }

  console.log(`[${config.slug}] 완료\n`);
}
