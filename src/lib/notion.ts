import { Client } from "@notionhq/client";
import { readFileSync, existsSync } from "fs";
import { join } from "path";
import { fileURLToPath } from "url";

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

// ── 캐시 로더 (Notion API 연결 실패 시 JSON 캐시 사용) ────────────────────
let _cache: { guides: any[]; products: any[] } | null = null;

function loadCache(): { guides: any[]; products: any[] } | null {
  if (_cache) return _cache;
  try {
    // 후보 경로들 (한글/공백 경로 대비 fileURLToPath 사용)
    const candidates: string[] = [];

    // 1) src/lib/ 기준 (import.meta.url)
    try {
      candidates.push(join(fileURLToPath(new URL("..", import.meta.url)), "data", "notion-cache.json"));
    } catch {}

    // 2) process.cwd() 기준
    if (typeof process !== "undefined" && process.cwd) {
      candidates.push(join(process.cwd(), "src", "data", "notion-cache.json"));
    }

    for (const p of candidates) {
      if (existsSync(p)) {
        const raw = readFileSync(p, "utf-8");
        _cache = JSON.parse(raw);
        console.log(`[Notion Cache] 로드 완료: ${_cache.guides.length}개 가이드, ${_cache.products.length}개 상품`);
        return _cache;
      }
    }
  } catch (e) {
    // 조용히 실패
  }
  return null;
}

// ── Notion 클라이언트 ─────────────────────────────────────────────────────
function getClient(): Client | null {
  const key =
    (typeof process !== "undefined" && process.env?.NOTION_API_KEY) ||
    import.meta.env?.NOTION_API_KEY;
  if (!key) return null;
  try {
    return new Client({ auth: key });
  } catch {
    return null;
  }
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

// ── 캐시 기반 함수 ────────────────────────────────────────────────────────
function cacheParseGuide(entry: any): GiftGuide {
  return {
    id: entry.id,
    title: entry.title,
    slug: entry.slug,
    description: entry.description,
    recipientAge: entry.recipientAge,
    recipientGender: entry.recipientGender,
    relation: entry.relation,
    occasion: entry.occasion,
    ageGroup: entry.ageGroup,
    budgetTag: entry.budgetTag,
    priceMin: entry.priceMin,
    priceMax: entry.priceMax,
    interests: entry.interests,
    thumbnail: entry.thumbnail,
    intro: entry.intro,
    updatedAt: new Date(entry.updatedAt),
  };
}

// Notion 배경색 주석 → 형광펜 효과 CSS 클래스 (global.css의 mark.hl-* 참고)
const HIGHLIGHT_CLASS: Record<string, string> = {
  yellow_background: "hl-yellow",
  orange_background: "hl-yellow",
  pink_background: "hl-pink",
  red_background: "hl-pink",
  green_background: "hl-green",
  blue_background: "hl-blue",
  purple_background: "hl-blue",
};

// ── 리치텍스트 → HTML ─────────────────────────────────────────────────────
function richTextToHtml(richText: any[]): string {
  return (richText ?? []).map((r: any) => {
    let text = (r.plain_text ?? "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
    if (r.annotations?.bold) text = `<strong>${text}</strong>`;
    if (r.annotations?.italic) text = `<em>${text}</em>`;
    if (r.annotations?.code) text = `<code>${text}</code>`;
    const hlClass = HIGHLIGHT_CLASS[r.annotations?.color];
    if (hlClass) text = `<mark class="${hlClass}">${text}</mark>`;
    if (r.href) text = `<a href="${r.href}" target="_blank" rel="noopener noreferrer">${text}</a>`;
    return text;
  }).join("");
}

function plainText(richText: any[]): string {
  return (richText ?? []).map((r: any) => r.plain_text ?? "").join("");
}

function slugify(text: string): string {
  return text
    .toLowerCase()
    .replace(/\s+/g, "-")
    .replace(/[^\w가-힣-]/g, "")
    .slice(0, 60);
}

function escapeHtml(s: string): string {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

/**
 * "관련 가이드" 섹션 불릿("여자친구 생일선물: 선물보다 편지가 중요한 이유")을
 * 실제 가이드 슬러그로 역해석한다. 콜론 앞부분을 후보 슬러그로 변환해보고,
 * 실패하면 제목 접두 매칭까지 시도한다. 105개 샘플 기준 96% 해석 성공 —
 * 나머지는 병합·미발행 등 콘텐츠 쪽 문제라 링크화하지 않는 게 안전하다
 * (틀린 링크를 보여주느니 텍스트로 두는 게 낫다).
 */
function resolveGuideSlug(head: string, slugSet: Set<string>, guides: { slug: string; title: string }[]): string | null {
  const candidates = [
    head,
    head.replace(/\s*가이드$/, ""),
    head.replace(/^(\d+만원)\s*이하\s*선물만\s*비교하기$/, "$1이하 선물"),
    head.replace(/\s*보기$/, ""),
  ];
  for (const c of candidates) {
    const s = c.trim().replace(/\s+/g, "-");
    if (slugSet.has(s)) return s;
  }
  const m = guides.find((g) => g.title.startsWith(head));
  return m ? m.slug : null;
}

function trackedLink(toSlug: string, label: string, fromSlug: string): string {
  const onclick = `gtag('event','internal_link',{'from':'${fromSlug}','to':'${toSlug}','position':'related-bullet'})`;
  return `<a href="/선물/${toSlug}/" onclick="${onclick}">${label}</a>`;
}

function linkifyRelatedBullet(richText: any[], guides: { slug: string; title: string }[], fromSlug: string): string {
  const text = plainText(richText);
  if (!text.trim()) return richTextToHtml(richText);
  const slugSet = new Set(guides.map((g) => g.slug));

  const colonIdx = text.indexOf(":");
  const head = (colonIdx >= 0 ? text.slice(0, colonIdx) : text).trim();
  const rest = colonIdx >= 0 ? text.slice(colonIdx) : "";

  // "여자친구 생일선물 · 남자친구 생일선물: 연인 사이 기준" 같은 콤보 표기
  if (head.includes("·")) {
    const parts = head.split("·").map((p) => p.trim());
    const resolved = parts.map((p) => resolveGuideSlug(p, slugSet, guides));
    if (resolved.every(Boolean)) {
      const linked = parts.map((p, i) => trackedLink(resolved[i]!, escapeHtml(p), fromSlug)).join(" · ");
      return `${linked}${escapeHtml(rest)}`;
    }
    return richTextToHtml(richText);
  }

  const slug = resolveGuideSlug(head, slugSet, guides);
  if (!slug) return richTextToHtml(richText);
  return `${trackedLink(slug, escapeHtml(head), fromSlug)}${escapeHtml(rest)}`;
}

function cacheBlocksToHtml(blocks: any[], guides: { slug: string; title: string }[] = [], fromSlug = ""): { html: string; headings: Heading[] } {
  let html = "";
  const headings: Heading[] = [];
  let inBulletList = false;
  let inNumberedList = false;
  let inRelatedSection = false;

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
        inRelatedSection = text.startsWith("관련 가이드");
        const id = slugify(text);
        headings.push({ id, text, level: 2 });
        html += `<h2 id="${id}">${richTextToHtml(block.heading_2?.rich_text ?? [])}</h2>\n`;
        break;
      }
      case "heading_3": {
        inRelatedSection = false;
        const text = plainText(block.heading_3?.rich_text ?? []);
        const id = slugify(text);
        headings.push({ id, text, level: 3 });
        html += `<h3 id="${id}">${richTextToHtml(block.heading_3?.rich_text ?? [])}</h3>\n`;
        break;
      }
      case "bulleted_list_item": {
        if (!inBulletList) { html += "<ul>\n"; inBulletList = true; }
        const bulletRt = block.bulleted_list_item?.rich_text ?? [];
        const bulletHtml = inRelatedSection ? linkifyRelatedBullet(bulletRt, guides, fromSlug) : richTextToHtml(bulletRt);
        html += `<li>${bulletHtml}</li>\n`;
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
      case "table": {
        const hasHeader = block.table?.has_column_header;
        const children = block.table?.children ?? [];
        let rowsHtml = "";
        children.forEach((rowBlock: any, i: number) => {
          const cells: any[][] = rowBlock.table_row?.cells ?? [];
          const cellTag = hasHeader && i === 0 ? "th" : "td";
          const cellsHtml = cells.map((cell) => `<${cellTag}>${richTextToHtml(cell)}</${cellTag}>`).join("");
          rowsHtml += `<tr>${cellsHtml}</tr>\n`;
        });
        html += `<table>\n${rowsHtml}</table>\n`;
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

async function blocksToHtml(blocks: any[], notion: Client, guides: { slug: string; title: string }[] = [], fromSlug = ""): Promise<{ html: string; headings: Heading[] }> {
  let html = "";
  const headings: Heading[] = [];
  let inBulletList = false;
  let inNumberedList = false;
  let inRelatedSection = false;

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
        inRelatedSection = text.startsWith("관련 가이드");
        const id = slugify(text);
        headings.push({ id, text, level: 2 });
        html += `<h2 id="${id}">${richTextToHtml(block.heading_2?.rich_text ?? [])}</h2>\n`;
        break;
      }
      case "heading_3": {
        inRelatedSection = false;
        const text = plainText(block.heading_3?.rich_text ?? []);
        const id = slugify(text);
        headings.push({ id, text, level: 3 });
        html += `<h3 id="${id}">${richTextToHtml(block.heading_3?.rich_text ?? [])}</h3>\n`;
        break;
      }
      case "bulleted_list_item": {
        if (!inBulletList) { html += "<ul>\n"; inBulletList = true; }
        const bulletRt = block.bulleted_list_item?.rich_text ?? [];
        const bulletHtml = inRelatedSection ? linkifyRelatedBullet(bulletRt, guides, fromSlug) : richTextToHtml(bulletRt);
        html += `<li>${bulletHtml}</li>\n`;
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
      case "table": {
        const rowsResp = await notion.blocks.children.list({ block_id: block.id });
        const hasHeader = block.table?.has_column_header;
        let rowsHtml = "";
        rowsResp.results.forEach((rowBlock: any, i: number) => {
          const cells: any[][] = rowBlock.table_row?.cells ?? [];
          const cellTag = hasHeader && i === 0 ? "th" : "td";
          const cellsHtml = cells.map((cell) => `<${cellTag}>${richTextToHtml(cell)}</${cellTag}>`).join("");
          rowsHtml += `<tr>${cellsHtml}</tr>\n`;
        });
        html += `<table>\n${rowsHtml}</table>\n`;
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
  if (notion && import.meta.env.NOTION_GUIDES_DB_ID) {
    try {
      const response = await notion.databases.query({
        database_id: import.meta.env.NOTION_GUIDES_DB_ID,
        filter: { property: "published", checkbox: { equals: true } },
        sorts: [{ property: "Title", direction: "ascending" }],
      });
      return response.results
        .filter((p): p is any => p.object === "page")
        .map(parseGuide);
    } catch (e) {
      console.log("[Notion] API 실패, 캐시 사용:", (e as Error).message);
    }
  }

  // Fallback: JSON 캐시
  const cache = loadCache();
  if (cache) {
    return cache.guides.filter((g: any) => true).map(cacheParseGuide);
  }
  return [];
}

export async function getGiftGuideBySlug(slug: string): Promise<GiftGuide | null> {
  const notion = getClient();
  if (notion && import.meta.env.NOTION_GUIDES_DB_ID) {
    try {
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
      if (page && page.object === "page") return parseGuide(page);
    } catch (e) {
      console.log("[Notion] API 실패, 캐시 사용:", (e as Error).message);
    }
  }

  // Fallback
  const cache = loadCache();
  if (cache) {
    const entry = cache.guides.find((g: any) => g.slug === slug);
    if (entry) return cacheParseGuide(entry);
  }
  return null;
}

export async function getGuideContent(pageId: string, allGuides: GiftGuide[] = []): Promise<{ html: string; headings: Heading[] }> {
  const guideRefs = allGuides.map((g) => ({ slug: g.slug, title: g.title }));
  const fromSlug = allGuides.find((g) => g.id === pageId)?.slug ?? "";

  // 1) 캐시에서 블록 찾기
  const cache = loadCache();
  if (cache) {
    const entry = cache.guides.find((g: any) => g.id === pageId);
    if (entry && entry.blocks && entry.blocks.length > 0) {
      return cacheBlocksToHtml(entry.blocks, guideRefs, fromSlug);
    }
  }

  // 2) Notion API (기존 로직)
  const notion = getClient();
  if (!notion) return { html: "", headings: [] };

  let lastError: Error | null = null;
  for (let attempt = 0; attempt < 3; attempt++) {
    try {
      if (attempt > 0) await new Promise((r) => setTimeout(r, 1000 * attempt));
      let allBlocks: any[] = [];
      let cursor: string | undefined = undefined;
      do {
        const response = await notion.blocks.children.list({ block_id: pageId, start_cursor: cursor });
        allBlocks = [...allBlocks, ...response.results];
        cursor = response.next_cursor ?? undefined;
      } while (cursor);
      if (allBlocks.length > 0) return await blocksToHtml(allBlocks, notion, guideRefs, fromSlug);
      if (attempt < 2) continue;
      return { html: "", headings: [] };
    } catch (err) {
      lastError = err instanceof Error ? err : new Error(String(err));
      if (attempt < 2) {
        console.warn(`[Notion] getGuideContent retry ${attempt + 1}: ${lastError.message}`);
        continue;
      }
    }
  }
  console.error(`[Notion] getGuideContent failed: ${lastError?.message}`);
  return { html: "", headings: [] };
}

export async function getProducts(guideId: string): Promise<Product[]> {
  const notion = getClient();
  if (notion && import.meta.env.NOTION_PRODUCTS_DB_ID) {
    try {
      const response = await notion.databases.query({
        database_id: import.meta.env.NOTION_PRODUCTS_DB_ID,
        filter: { property: "giftGuide", relation: { contains: guideId } },
        sorts: [{ property: "rank", direction: "ascending" }],
      });
      return response.results
        .filter((p): p is any => p.object === "page")
        .map(parseProduct);
    } catch (e) {
      console.log("[Notion] Products API 실패, 캐시 사용:", (e as Error).message);
    }
  }

  // Fallback
  const cache = loadCache();
  if (cache) {
    return cache.products
      .filter((p: any) => p.guideId === guideId)
      .map((p: any) => ({
        id: p.id,
        name: p.name,
        price: p.price,
        coupangUrl: p.coupangUrl || "",
        naverUrl: p.naverUrl || "",
        imageUrl: p.imageUrl || "",
        rank: p.rank ?? 99,
        pros: p.pros || "",
      }));
  }
  return [];
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
