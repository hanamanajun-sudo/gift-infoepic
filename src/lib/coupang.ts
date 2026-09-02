import { createHmac } from 'crypto';
import { readFileSync, writeFileSync } from 'fs';
import { fileURLToPath } from 'url';
import { join, dirname } from 'path';

export interface CoupangProduct {
  productId: number;
  productName: string;
  productPrice: number;
  productImage: string;
  productUrl: string;
  isRocket: boolean;
  categoryName: string;
}

interface CacheEntry {
  fetchedAt: string;
  products: CoupangProduct[];
}

const CACHE_TTL_DAYS = 7;
const CACHE_PATH = join(dirname(fileURLToPath(import.meta.url)), '../data/coupang-cache.json');

// 빌드 중 API 호출을 직렬화해 분당 50회 제한을 넘지 않도록 함
let callQueue: Promise<void> = Promise.resolve();

function enqueueApiCall<T>(fn: () => Promise<T>): Promise<T> {
  let resolve!: (v: T) => void;
  let reject!: (e: unknown) => void;
  const result = new Promise<T>((res, rej) => { resolve = res; reject = rej; });

  callQueue = callQueue.then(async () => {
    try { resolve(await fn()); } catch (e) { reject(e); }
    await new Promise(r => setTimeout(r, 1500)); // 1.5초 간격 = 분당 40회
  });

  return result;
}

function loadCache(): Record<string, CacheEntry> {
  try {
    return JSON.parse(readFileSync(CACHE_PATH, 'utf-8'));
  } catch {
    return {};
  }
}

function saveCache(cache: Record<string, CacheEntry>) {
  try {
    writeFileSync(CACHE_PATH, JSON.stringify(cache, null, 2), 'utf-8');
  } catch (err) {
    console.warn('[Coupang cache] write failed:', err);
  }
}

function isFresh(entry: CacheEntry): boolean {
  const age = Date.now() - new Date(entry.fetchedAt).getTime();
  return age < CACHE_TTL_DAYS * 24 * 60 * 60 * 1000;
}

function buildAuthHeader(method: string, path: string, query: string): string {
  // import.meta.env는 Astro 빌드 안에서만 존재한다. 상품 리서치용 CLI 스크립트에서도
  // 같은 함수를 쓰려면 process.env 폴백이 필요하다.
  const accessKey = import.meta.env?.COUPANG_ACCESS_KEY ?? process.env.COUPANG_ACCESS_KEY;
  const secretKey = import.meta.env?.COUPANG_SECRET_KEY ?? process.env.COUPANG_SECRET_KEY;

  // 쿠팡 API: 2자리 연도 형식 YYMMDDTHHmmssZ
  const now = new Date();
  const pad = (n: number) => String(n).padStart(2, '0');
  const datetime =
    String(now.getUTCFullYear()).slice(-2) +
    pad(now.getUTCMonth() + 1) +
    pad(now.getUTCDate()) +
    'T' +
    pad(now.getUTCHours()) +
    pad(now.getUTCMinutes()) +
    pad(now.getUTCSeconds()) +
    'Z';

  // 메시지: datetime + method + path + queryString (개행 없음)
  const message = datetime + method + path + query;
  const signature = createHmac('sha256', secretKey).update(message).digest('hex');

  return `CEA algorithm=HmacSHA256, access-key=${accessKey}, signed-date=${datetime}, signature=${signature}`;
}

/**
 * 상품검색 API가 돌려주는 productUrl은 그 검색 요청에 서명된 임시 링크다.
 * 실측: 같은 상품을 몇 분 간격으로 두 번 검색하면 requestid·token이 매번 바뀐다.
 * 이 링크를 Notion에 저장해 며칠 뒤 방문자가 누르면 "요청하신 페이지의 사용권한이
 * 없습니다"로 막힌다 — 2026-09-03 추석 가이드 발행 직후 실제로 겪은 사고.
 *
 * 저장·게시용으로 오래 남는 링크가 필요하면 반드시 이 함수로 별도 변환해야 한다.
 * (공식 Deeplink API. 상품검색과 완전히 다른 엔드포인트.)
 */
export async function createDeeplinks(coupangUrls: string[], subId = ''): Promise<Record<string, string>> {
  const accessKey = import.meta.env?.COUPANG_ACCESS_KEY ?? process.env.COUPANG_ACCESS_KEY;
  const secretKey = import.meta.env?.COUPANG_SECRET_KEY ?? process.env.COUPANG_SECRET_KEY;
  if (!accessKey || !secretKey || coupangUrls.length === 0) return {};

  const method = 'POST';
  const path = '/v2/providers/affiliate_open_api/apis/openapi/v1/deeplink';

  return enqueueApiCall(async () => {
    try {
      const res = await fetch(`https://api-gateway.coupang.com${path}`, {
        method,
        headers: {
          Authorization: buildAuthHeader(method, path, ''),
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ coupangUrls, subId }),
      });

      if (!res.ok) {
        console.warn(`[Coupang Deeplink] ${res.status} ${res.statusText}`);
        return {};
      }

      const data = await res.json() as any;
      if (data.rCode !== '0') {
        console.warn(`[Coupang Deeplink] rCode: ${data.rCode} ${data.rMessage}`);
        return {};
      }

      const map: Record<string, string> = {};
      for (const item of data.data ?? []) map[item.originalUrl] = item.shortenUrl;
      return map;
    } catch (err) {
      console.warn('[Coupang Deeplink] fetch error:', err);
      return {};
    }
  });
}

/** productUrl(임시 서명 링크)에서 itemId·vendorItemId를 뽑아 평문 상품 URL을 만든다. */
export function toPlainProductUrl(product: CoupangProduct): string | null {
  try {
    const u = new URL(product.productUrl);
    const itemId = u.searchParams.get('itemId');
    const vendorItemId = u.searchParams.get('vendorItemId');
    if (!itemId || !vendorItemId) return null;
    return `https://www.coupang.com/vp/products/${product.productId}?itemId=${itemId}&vendorItemId=${vendorItemId}`;
  } catch {
    return null;
  }
}

export async function searchCoupangProducts(keyword: string, limit = 8): Promise<CoupangProduct[]> {
  // import.meta.env는 Astro 빌드 안에서만 존재한다. 상품 리서치용 CLI 스크립트에서도
  // 같은 함수를 쓰려면 process.env 폴백이 필요하다.
  const accessKey = import.meta.env?.COUPANG_ACCESS_KEY ?? process.env.COUPANG_ACCESS_KEY;
  const secretKey = import.meta.env?.COUPANG_SECRET_KEY ?? process.env.COUPANG_SECRET_KEY;

  if (!accessKey || !secretKey) return [];

  const cache = loadCache();

  if (cache[keyword] && isFresh(cache[keyword])) {
    return cache[keyword].products;
  }

  const method = 'GET';
  const path = '/v2/providers/affiliate_open_api/apis/openapi/products/search';
  const query = `keyword=${encodeURIComponent(keyword)}&limit=${limit}`;

  return enqueueApiCall(async () => {
    // 큐 안에서 캐시를 다시 확인 (앞선 호출이 같은 키워드를 채웠을 수 있음)
    const fresh = loadCache();
    if (fresh[keyword] && isFresh(fresh[keyword])) return fresh[keyword].products;

    try {
      const res = await fetch(`https://api-gateway.coupang.com${path}?${query}`, {
        headers: {
          Authorization: buildAuthHeader(method, path, query),
          'Content-Type': 'application/json;charset=UTF-8',
        },
      });

      if (!res.ok) {
        console.warn(`[Coupang API] ${res.status} ${res.statusText} — keyword: ${keyword}`);
        return [];
      }

      const data = await res.json() as any;
      if (data.rCode !== '0') {
        console.warn(`[Coupang API] rCode: ${data.rCode} ${data.rMessage}`);
        return [];
      }

      const products: CoupangProduct[] = data.data?.productData ?? [];
      const updated = loadCache();
      updated[keyword] = { fetchedAt: new Date().toISOString(), products };
      saveCache(updated);
      return products;
    } catch (err) {
      console.warn('[Coupang API] fetch error:', err);
      return [];
    }
  });
}
