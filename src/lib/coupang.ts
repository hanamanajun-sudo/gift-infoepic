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
  const accessKey = import.meta.env.COUPANG_ACCESS_KEY;
  const secretKey = import.meta.env.COUPANG_SECRET_KEY;

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

export async function searchCoupangProducts(keyword: string, limit = 8): Promise<CoupangProduct[]> {
  const accessKey = import.meta.env.COUPANG_ACCESS_KEY;
  const secretKey = import.meta.env.COUPANG_SECRET_KEY;

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
