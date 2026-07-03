import { pushGuide } from './lib.mjs';

// 사용법: node --env-file=.env scripts/content/push.mjs 13세-여자아이-생일선물
const slug = process.argv[2];
if (!slug) {
  console.error('가이드 슬러그를 넘겨주세요. 예: node --env-file=.env scripts/content/push.mjs 13세-여자아이-생일선물');
  process.exit(1);
}

const config = await import(`./guides/${slug}.mjs`);
await pushGuide(config);
