import { pushGuide } from './lib.mjs';
import { readFileSync } from 'fs';

// .env 직접 파싱 (Node --env-file 호환성 이슈 대응)
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

// 사용법: node scripts/content/push.mjs 13세-여자아이-생일선물
const slug = process.argv[2];
if (!slug) {
  console.error('가이드 슬러그를 넘겨주세요. 예: node scripts/content/push.mjs 13세-여자아이-생일선물');
  process.exit(1);
}

const config = await import(`./guides/${slug}.mjs`);
await pushGuide(config);
