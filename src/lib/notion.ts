import { Client } from "@notionhq/client";

export interface GiftGuide {
  id: string;
  title: string;
  slug: string;
  description: string;
  recipientAge: number | null;
  recipientGender: string;
  relation: string[];
  occasion: string[];
  ageGroup: string[];
  budgetTag: string[];
  priceMin: number | null;
  priceMax: number | null;
  interests: string[];
  thumbnail: string;
  intro: string;
  updatedAt: Date;
}

export interface Product {
  id: string;
  name: string;
  price: number | null;
  coupangUrl: string;
  naverUrl: string;
  imageUrl: string;
  rank: number;
  pros: string;
}

export interface Heading {
  id: string;
  text: string;
  level: 2 | 3;
}

// ── 샘플 데이터 (Notion 미연결 시 개발용) ──────────────────────────────
const SAMPLE_GUIDES: GiftGuide[] = [
  {
    id: "sample-1",
    title: "13세 여자아이 생일선물 추천 TOP10",
    slug: "13세-여자아이-생일선물",
    description: "중학교 1학년 딸에게 완벽한 선물을 찾고 있다면? 실제 구매자 후기와 함께하는 13세 여아 생일선물 추천 TOP10",
    recipientAge: 13,
    recipientGender: "여아",
    relation: ["딸", "조카", "친구"],
    occasion: ["생일"],
    ageGroup: ["13세", "중학생", "초등학생"],
    budgetTag: ["5만원이하", "10만원이하"],
    priceMin: 15000,
    priceMax: 80000,
    interests: ["K뷰티", "패션", "문구"],
    thumbnail: "",
    intro: "중학교에 입학하거나 막 졸업한 13살 딸에게 어떤 선물을 줘야 할지 막막하다면, 이 글이 도움이 될 거예요. 또래 아이들이 실제로 받고 좋아했던 선물만 골랐습니다.",
    updatedAt: new Date("2026-05-01"),
  },
  {
    id: "sample-2",
    title: "7세 남자아이 어린이날 선물 추천",
    slug: "7세-남자아이-어린이날선물",
    description: "어린이날 7살 아들 선물, 뭘 사줄지 모르겠다면? 레고부터 과학 키트까지 7세 남아 인기 선물 추천",
    recipientAge: 7,
    recipientGender: "남아",
    relation: ["아들", "조카"],
    occasion: ["어린이날", "생일"],
    ageGroup: ["7세", "초등학생"],
    budgetTag: ["3만원이하", "5만원이하"],
    priceMin: 20000,
    priceMax: 50000,
    interests: ["장난감", "레고", "과학"],
    thumbnail: "",
    intro: "7살 남자아이는 뛰어다니고 만들고 탐험하는 걸 좋아해요. 그 에너지를 제대로 살려줄 선물을 골라야 진짜 좋아합니다.",
    updatedAt: new Date("2026-04-20"),
  },
  {
    id: "sample-3",
    title: "남자친구 생일선물 추천 — 20대 남성",
    slug: "남자친구-생일선물",
    description: "남자친구 생일선물 고민 끝! 20대 남성이 실제로 원하는 선물 추천. 3만원~20만원대까지",
    recipientAge: null,
    recipientGender: "남성",
    relation: ["남자친구"],
    occasion: ["생일"],
    ageGroup: ["20대"],
    budgetTag: ["3만원이하", "5만원이하", "10만원이하", "20만원이하"],
    priceMin: 30000,
    priceMax: 200000,
    interests: ["패션", "테크", "게임"],
    thumbnail: "",
    intro: "남자친구 선물은 항상 어렵습니다. 마음에 드는 거 사줬다고 생각했는데 반응이 미지근하면 속상하잖아요. 실제로 남성들이 선물 받고 기뻤던 것들만 추려봤어요.",
    updatedAt: new Date("2026-05-10"),
  },
  {
    id: "sample-4",
    title: "여자친구 생일선물 추천 — 20대 여성",
    slug: "여자친구-생일선물",
    description: "여자친구 생일선물 아이디어! 20대 여성이 받고 감동한 선물 추천. 예산별 추천 포함",
    recipientAge: null,
    recipientGender: "여성",
    relation: ["여자친구"],
    occasion: ["생일"],
    ageGroup: ["20대"],
    budgetTag: ["5만원이하", "10만원이하", "20만원이하"],
    priceMin: 30000,
    priceMax: 200000,
    interests: ["K뷰티", "패션", "향기"],
    thumbnail: "",
    intro: "여자친구 선물, 매년 고민이죠. '또 향수야?' 소리 듣기 싫다면 이 글을 읽어보세요. 2026년 기준 실제 반응 좋은 선물만 모았습니다.",
    updatedAt: new Date("2026-05-12"),
  },
  {
    id: "sample-5",
    title: "30대 엄마 생일선물 추천 TOP8",
    slug: "30대-엄마-생일선물",
    description: "어린 자녀를 키우는 30대 엄마에게 드리는 선물. 실용적이면서도 특별한 30대 엄마 생일선물 추천",
    recipientAge: 35,
    recipientGender: "여성",
    relation: ["엄마"],
    occasion: ["생일", "어버이날"],
    ageGroup: ["30대"],
    budgetTag: ["5만원이하", "10만원이하"],
    priceMin: 30000,
    priceMax: 100000,
    interests: ["뷰티", "건강", "생활"],
    thumbnail: "",
    intro: "30대 엄마는 자신을 위한 시간이 부족해요. 그래서 선물도 '나를 위한 것'이어야 진심으로 기뻐합니다. 쓸모 있으면서도 마음이 담긴 선물을 골랐어요.",
    updatedAt: new Date("2026-04-28"),
  },
  {
    id: "sample-6",
    title: "크리스마스 선물 추천 — 연령별 완벽 가이드",
    slug: "크리스마스-선물-추천",
    description: "2026년 크리스마스 선물 추천. 아이부터 어른까지, 예산별 크리스마스 선물 아이디어 총정리",
    recipientAge: null,
    recipientGender: "공통",
    relation: [],
    occasion: ["크리스마스"],
    ageGroup: [],
    budgetTag: ["3만원이하", "5만원이하", "10만원이하"],
    priceMin: 10000,
    priceMax: 100000,
    interests: [],
    thumbnail: "",
    intro: "크리스마스 선물은 11월부터 준비하면 여유롭게 골를 수 있어요. 배송 기간까지 고려하면 12월 15일 이전에 주문하는 걸 추천드립니다.",
    updatedAt: new Date("2026-05-05"),
  },
  {
    id: "sample-7",
    title: "초등학생 생일선물 추천 — 8~12세",
    slug: "초등학생-생일선물",
    description: "초등학생 생일선물 뭐가 좋을까? 8세~12세 아이들이 실제로 받고 좋아한 선물 추천",
    recipientAge: null,
    recipientGender: "공통",
    relation: ["딸", "아들", "조카"],
    occasion: ["생일", "어린이날"],
    ageGroup: ["초등학생", "8세", "9세", "10세", "11세", "12세"],
    budgetTag: ["3만원이하", "5만원이하"],
    priceMin: 15000,
    priceMax: 50000,
    interests: ["장난감", "문구", "보드게임", "도서"],
    thumbnail: "",
    intro: "초등학생 선물은 나이에 따라 취향이 확연히 달라요. 저학년(8~9세)과 고학년(10~12세)이 원하는 게 달라서, 나이에 맞는 선물을 골라야 합니다.",
    updatedAt: new Date("2026-04-15"),
  },
  {
    id: "sample-8",
    title: "졸업선물 추천 — 초등·중학·고등·대학",
    slug: "졸업선물-추천",
    description: "2026년 졸업선물 추천. 초등, 중학, 고등, 대학 졸업 각각 상황에 맞는 선물 아이디어",
    recipientAge: null,
    recipientGender: "공통",
    relation: ["딸", "아들", "조카", "친구"],
    occasion: ["졸업"],
    ageGroup: ["초등학생", "중학생", "고등학생", "20대"],
    budgetTag: ["3만원이하", "5만원이하", "10만원이하"],
    priceMin: 20000,
    priceMax: 100000,
    interests: ["패션", "테크", "문구"],
    thumbnail: "",
    intro: "졸업선물은 '다음 단계'를 위한 선물이에요. 초등 졸업이냐, 대학 졸업이냐에 따라 완전히 다른 선물이 필요합니다.",
    updatedAt: new Date("2026-03-10"),
  },
];

const SAMPLE_PRODUCTS: Record<string, Product[]> = {
  "sample-1": [
    { id: "p1-1", name: "어뮤즈 립글로우 발라지는 틴트", price: 18000, coupangUrl: "#", naverUrl: "#", imageUrl: "", rank: 1, pros: "중학생 사이에서 유행 중인 뷰티 제품. 색이 예쁘고 용돈으로 사기엔 부담스러워서 선물로 딱 좋아요." },
    { id: "p1-2", name: "다꾸 스티커 세트 + 마스킹테이프", price: 22000, coupangUrl: "#", naverUrl: "#", imageUrl: "", rank: 2, pros: "다이어리 꾸미기를 좋아하는 13세 여아라면 100% 좋아합니다. SNS에서 유행하는 다꾸 아이템 모음." },
    { id: "p1-3", name: "펜텔 컬러 브러쉬 사인펜 세트", price: 28000, coupangUrl: "#", naverUrl: "#", imageUrl: "", rank: 3, pros: "미술이나 그림 그리기를 좋아하는 아이에게 추천. 색 발색이 좋고 오래 씁니다." },
  ],
  "sample-3": [
    { id: "p3-1", name: "르라보 산탈 33 샘플 세트", price: 35000, coupangUrl: "#", naverUrl: "#", imageUrl: "", rank: 1, pros: "향수에 관심 있는 20대 남성에게 좋습니다. 풀사이즈 전에 향을 확인해볼 수 있는 샘플러." },
    { id: "p3-2", name: "무선 충전 보조배터리 20000mAh", price: 45000, coupangUrl: "#", naverUrl: "#", imageUrl: "", rank: 2, pros: "실용적이면서도 매일 쓰는 제품. 용량이 크고 아이폰/갤럭시 모두 지원해서 불편함이 없어요." },
  ],
};

// ── Notion 클라이언트 ─────────────────────────────────────────────────────
function getClient(): Client | null {
  if (!import.meta.env.NOTION_API_KEY) return null;
  return new Client({ auth: import.meta.env.NOTION_API_KEY });
}

// ── 타입 헬퍼 ─────────────────────────────────────────────────────────────
function getTitle(prop: any): string {
  return prop?.title?.[0]?.plain_text ?? "";
}
function getText(prop: any): string {
  return prop?.rich_text?.map((r: any) => r.plain_text).join("") ?? "";
}
function getNumber(prop: any): number | null {
  return prop?.number ?? null;
}
function getSelect(prop: any): string {
  return prop?.select?.name ?? "";
}
function getMultiSelect(prop: any): string[] {
  return prop?.multi_select?.map((s: any) => s.name) ?? [];
}
function getUrl(prop: any): string {
  return prop?.url ?? "";
}

function parseGuide(page: any): GiftGuide {
  const p = page.properties;
  return {
    id: page.id,
    title: getTitle(p.Title),
    slug: getText(p.slug),
    description: getText(p.description),
    recipientAge: getNumber(p.recipientAge),
    recipientGender: getSelect(p.recipientGender),
    relation: getMultiSelect(p.relation),
    occasion: getMultiSelect(p.occasion),
    ageGroup: getMultiSelect(p.ageGroup),
    budgetTag: getMultiSelect(p.budgetTag),
    priceMin: getNumber(p.priceMin),
    priceMax: getNumber(p.priceMax),
    interests: getMultiSelect(p.interests),
    thumbnail: getText(p.thumbnail),
    intro: getText(p.intro),
    updatedAt: new Date(page.last_edited_time),
  };
}

function parseProduct(page: any): Product {
  const p = page.properties;
  return {
    id: page.id,
    name: getTitle(p.Title),
    price: getNumber(p.price),
    coupangUrl: getUrl(p.coupangUrl),
    naverUrl: getUrl(p.naverUrl),
    imageUrl: getText(p.imageUrl),
    rank: getNumber(p.rank) ?? 99,
    pros: getText(p.pros),
  };
}

// ── 리치텍스트 → HTML ─────────────────────────────────────────────────────
function richTextToHtml(richText: any[]): string {
  return (richText ?? []).map((r) => {
    let text = (r.plain_text ?? "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
    if (r.annotations?.bold) text = `<strong>${text}</strong>`;
    if (r.annotations?.italic) text = `<em>${text}</em>`;
    if (r.annotations?.code) text = `<code>${text}</code>`;
    if (r.href) text = `<a href="${r.href}" target="_blank" rel="noopener noreferrer">${text}</a>`;
    return text;
  }).join("");
}

function plainText(richText: any[]): string {
  return (richText ?? []).map((r) => r.plain_text ?? "").join("");
}

function slugify(text: string): string {
  return text
    .toLowerCase()
    .replace(/\s+/g, "-")
    .replace(/[^\w가-힣-]/g, "")
    .slice(0, 60);
}

function blocksToHtml(blocks: any[]): { html: string; headings: Heading[] } {
  let html = "";
  const headings: Heading[] = [];
  let inBulletList = false;
  let inNumberedList = false;

  for (const block of blocks) {
    if (inBulletList && block.type !== "bulleted_list_item") {
      html += "</ul>\n";
      inBulletList = false;
    }
    if (inNumberedList && block.type !== "numbered_list_item") {
      html += "</ol>\n";
      inNumberedList = false;
    }

    switch (block.type) {
      case "paragraph": {
        const text = richTextToHtml(block.paragraph?.rich_text ?? []);
        if (text.trim()) html += `<p>${text}</p>\n`;
        break;
      }
      case "heading_2": {
        const text = plainText(block.heading_2?.rich_text ?? []);
        const id = slugify(text);
        headings.push({ id, text, level: 2 });
        html += `<h2 id="${id}">${richTextToHtml(block.heading_2?.rich_text ?? [])}</h2>\n`;
        break;
      }
      case "heading_3": {
        const text = plainText(block.heading_3?.rich_text ?? []);
        const id = slugify(text);
        headings.push({ id, text, level: 3 });
        html += `<h3 id="${id}">${richTextToHtml(block.heading_3?.rich_text ?? [])}</h3>\n`;
        break;
      }
      case "bulleted_list_item": {
        if (!inBulletList) { html += "<ul>\n"; inBulletList = true; }
        html += `<li>${richTextToHtml(block.bulleted_list_item?.rich_text ?? [])}</li>\n`;
        break;
      }
      case "numbered_list_item": {
        if (!inNumberedList) { html += "<ol>\n"; inNumberedList = true; }
        html += `<li>${richTextToHtml(block.numbered_list_item?.rich_text ?? [])}</li>\n`;
        break;
      }
      case "image": {
        const url = block.image?.type === "external"
          ? block.image.external?.url ?? ""
          : block.image?.file?.url ?? "";
        const caption = plainText(block.image?.caption ?? []);
        html += `<figure><img src="${url}" alt="${caption}" loading="lazy" decoding="async">${caption ? `<figcaption>${caption}</figcaption>` : ""}</figure>\n`;
        break;
      }
      case "divider":
        html += "<hr>\n";
        break;
      case "quote":
        html += `<blockquote>${richTextToHtml(block.quote?.rich_text ?? [])}</blockquote>\n`;
        break;
      case "callout":
        html += `<blockquote>${richTextToHtml(block.callout?.rich_text ?? [])}</blockquote>\n`;
        break;
    }
  }

  if (inBulletList) html += "</ul>\n";
  if (inNumberedList) html += "</ol>\n";

  return { html, headings };
}

// ── 공개 API ──────────────────────────────────────────────────────────────
export async function getGiftGuides(): Promise<GiftGuide[]> {
  const notion = getClient();
  if (!notion || !import.meta.env.NOTION_GUIDES_DB_ID) return SAMPLE_GUIDES;

  const response = await notion.databases.query({
    database_id: import.meta.env.NOTION_GUIDES_DB_ID,
    filter: { property: "published", checkbox: { equals: true } },
    sorts: [{ property: "Title", direction: "ascending" }],
  });

  return response.results
    .filter((p): p is any => p.object === "page")
    .map(parseGuide);
}

export async function getGiftGuideBySlug(slug: string): Promise<GiftGuide | null> {
  const notion = getClient();
  if (!notion || !import.meta.env.NOTION_GUIDES_DB_ID) {
    return SAMPLE_GUIDES.find((g) => g.slug === slug) ?? null;
  }

  const response = await notion.databases.query({
    database_id: import.meta.env.NOTION_GUIDES_DB_ID,
    filter: {
      and: [
        { property: "slug", rich_text: { equals: slug } },
        { property: "published", checkbox: { equals: true } },
      ],
    },
  });

  const page = response.results[0];
  if (!page || page.object !== "page") return null;
  return parseGuide(page);
}

export async function getGuideContent(pageId: string): Promise<{ html: string; headings: Heading[] }> {
  const notion = getClient();
  if (!notion) {
    return {
      html: "<p>Notion API 키를 설정하면 이 자리에 본문이 표시됩니다.</p>",
      headings: [],
    };
  }

  // Retry up to 3 times with exponential backoff for rate limit resilience
  let lastError: Error | null = null;
  for (let attempt = 0; attempt < 3; attempt++) {
    try {
      if (attempt > 0) {
        await new Promise(r => setTimeout(r, 1000 * attempt));
      }
      const response = await notion.blocks.children.list({ block_id: pageId });
      if (response.results && response.results.length > 0) {
        return blocksToHtml(response.results);
      }
      // Empty results: may need pagination or just empty page
      // Try pagination if has_more
      let allBlocks = [...response.results];
      let cursor = response.next_cursor;
      while (cursor) {
        const next = await notion.blocks.children.list({
          block_id: pageId,
          start_cursor: cursor,
        });
        allBlocks = [...allBlocks, ...next.results];
        cursor = next.next_cursor;
      }
      if (allBlocks.length > 0) {
        return blocksToHtml(allBlocks);
      }
      // If still empty and not the last attempt, retry
      if (attempt < 2) continue;
      return { html: "", headings: [] };
    } catch (err) {
      lastError = err instanceof Error ? err : new Error(String(err));
      if (attempt < 2) {
        console.warn(`[Notion] getGuideContent retry ${attempt + 1} for ${pageId.slice(0, 12)}: ${lastError.message}`);
        continue;
      }
    }
  }
  console.error(`[Notion] getGuideContent failed for ${pageId.slice(0, 12)}: ${lastError?.message}`);
  return { html: "", headings: [] };
}

export async function getProducts(guideId: string): Promise<Product[]> {
  const notion = getClient();
  if (!notion || !import.meta.env.NOTION_PRODUCTS_DB_ID) {
    return SAMPLE_PRODUCTS[guideId] ?? [];
  }

  const response = await notion.databases.query({
    database_id: import.meta.env.NOTION_PRODUCTS_DB_ID,
    filter: { property: "giftGuide", relation: { contains: guideId } },
    sorts: [{ property: "rank", direction: "ascending" }],
  });

  return response.results
    .filter((p): p is any => p.object === "page")
    .map(parseProduct);
}

// ── 가격 포맷 ─────────────────────────────────────────────────────────────
export function formatPrice(price: number | null): string {
  if (!price) return "";
  if (price >= 10000) {
    const man = price / 10000;
    return man % 1 === 0 ? `${man}만원` : `${man.toFixed(1)}만원`;
  }
  return `${price.toLocaleString()}원`;
}

export function formatPriceRange(min: number | null, max: number | null): string {
  if (!min && !max) return "";
  if (!min) return `~${formatPrice(max)}`;
  if (!max) return `${formatPrice(min)}~`;
  return `${formatPrice(min)} ~ ${formatPrice(max)}`;
}
