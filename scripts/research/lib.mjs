// 리서치 수집 공용 유틸 — Astro 빌드와 무관한 독립 스크립트에서만 사용

export function stripHtml(str) {
  return str
    .replace(/<[^>]+>/g, '')
    .replace(/&quot;/g, '"')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&#39;/g, "'")
    .trim();
}

export function slugify(keyword) {
  return keyword.trim().replace(/\s+/g, '-');
}

export async function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}
