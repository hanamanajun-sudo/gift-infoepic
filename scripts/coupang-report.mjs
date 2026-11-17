/**
 * 쿠팡 파트너스 리포트 API 조회 (읽기 전용).
 *
 * 목적: GA4 product_click 대비 쿠팡 집계 격차 조사(2026-11 트래킹 실험)를 수동 리포트 화면
 * 없이 날짜별·subId(trackingCode)별로 대조한다. 링크를 호출하지 않으므로 클릭이 생기지 않는다.
 *
 * 사용법:
 *   node --env-file=.env scripts/coupang-report.mjs clicks 20261113 20261117
 *   node --env-file=.env scripts/coupang-report.mjs clicks 20261113 20261117 --raw   # 응답 원문 일부 출력
 *   (종류: clicks | orders | cancels | commission)
 *
 * 주의 (비공식 문서 기준 — 공식 문서는 접근 불가여서 응답 형태를 실측으로 확인한다):
 *  - 기간 최대 30일, 데이터는 매일 15:00 KST 갱신, 날짜 형식 yyyyMMdd
 *  - 호출이 잦으면 계정이 정지될 수 있다는 경고가 있어 페이지 1회씩만 호출한다(자동 반복 없음).
 *  - 키는 출력하지 않는다.
 */
import { createHmac } from 'node:crypto';

const [kind = 'clicks', startDate, endDate, ...flags] = process.argv.slice(2);
const RAW = flags.includes('--raw');
const KINDS = ['clicks', 'orders', 'cancels', 'commission'];
if (!KINDS.includes(kind) || !/^\d{8}$/.test(startDate ?? '') || !/^\d{8}$/.test(endDate ?? '')) {
  console.error('usage: node --env-file=.env scripts/coupang-report.mjs <clicks|orders|cancels|commission> <yyyyMMdd> <yyyyMMdd> [--raw]');
  process.exit(1);
}
const { COUPANG_ACCESS_KEY: accessKey, COUPANG_SECRET_KEY: secretKey } = process.env;
if (!accessKey || !secretKey) { console.error('COUPANG_ACCESS_KEY/SECRET_KEY 없음 (--env-file=.env 확인)'); process.exit(1); }

const path = `/v2/providers/affiliate_open_api/apis/openapi/v1/reports/${kind}`;
const query = `startDate=${startDate}&endDate=${endDate}&page=0`;

const pad = n => String(n).padStart(2, '0');
const now = new Date();
const datetime = String(now.getUTCFullYear()).slice(-2) + pad(now.getUTCMonth() + 1) + pad(now.getUTCDate())
  + 'T' + pad(now.getUTCHours()) + pad(now.getUTCMinutes()) + pad(now.getUTCSeconds()) + 'Z';
const signature = createHmac('sha256', secretKey).update(datetime + 'GET' + path + query).digest('hex');
const auth = `CEA algorithm=HmacSHA256, access-key=${accessKey}, signed-date=${datetime}, signature=${signature}`;

const res = await fetch(`https://api-gateway.coupang.com${path}?${query}`, { headers: { Authorization: auth } });
const text = await res.text();
console.log(`HTTP ${res.status} ${kind} ${startDate}~${endDate}`);
let json;
try { json = JSON.parse(text); } catch { console.log(text.slice(0, 500)); process.exit(res.ok ? 0 : 1); }

console.log('rCode:', json.rCode, '| rMessage:', json.rMessage);
const rows = Array.isArray(json.data) ? json.data : [];
console.log('rows:', rows.length, rows.length ? `| fields: ${Object.keys(rows[0]).join(', ')}` : '');
if (RAW) for (const r of rows.slice(0, 50)) console.log(JSON.stringify(r));

// 날짜 × subId(trackingCode) 합계. 필드명은 실측 후 맞춘다(없으면 있는 숫자 필드를 전부 합산).
if (rows.length) {
  const groupKey = r => `${r.date ?? r.regDate ?? '?'} | ${r.trackingCode ?? r.subId ?? r.subParam ?? '(없음)'}`;
  const sums = new Map();
  for (const r of rows) {
    const g = sums.get(groupKey(r)) ?? {};
    for (const [k, v] of Object.entries(r)) if (typeof v === 'number') g[k] = (g[k] ?? 0) + v;
    sums.set(groupKey(r), g);
  }
  for (const [k, v] of [...sums].sort()) console.log(k, JSON.stringify(v));
}
