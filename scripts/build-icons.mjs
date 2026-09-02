/**
 * Tabler 아이콘 서브셋 생성기 → src/styles/icons.css
 *
 * 왜 있나: Tabler 웹폰트를 CDN에서 통째로 받으면 CSS 250KB + woff2 829KB가
 * 렌더링 차단 경로에 걸린다. 실제로 쓰는 아이콘은 28개뿐이라, 그것만
 * CSS mask용 data URI로 인라인하면 13KB로 끝난다.
 *
 * 사용법:
 *   node scripts/build-icons.mjs
 *
 * 아이콘을 추가/제거하려면 아래 ICONS 배열만 고치면 된다.
 * 마크업은 그대로 `<i class="ti ti-star"></i>` 를 쓴다 (웹폰트 시절과 동일).
 * `filled:` 접두사가 붙으면 @tabler/icons 의 filled 세트에서 받아온다.
 *
 * 실제로 쓰이는 아이콘 목록을 다시 뽑으려면:
 *   grep -rhoE "ti ti-[a-z0-9-]+" src/ | sort -u
 */

import { writeFile } from 'node:fs/promises';

const VERSION = '3.34.0';

const ICONS = [
  'alert-triangle', 'arrow-right', 'calendar', 'calendar-event', 'cash-banknote',
  'check', 'chevron-right', 'clock', 'external-link', 'filter-search',
  'gift', 'gift-off', 'heart', 'list', 'menu-2', 'mood-empty', 'package',
  'school', 'search', 'share', 'shopping-bag', 'shopping-cart',
  'star', 'table', 'users', 'wallet', 'x',
  // GiftCard·허브 인덱스에서 동적으로 조합되는 아이콘들.
  // class 문자열을 변수로 만들어 넣기 때문에 'ti ti-' 검색으로는 안 잡힌다.
  // 전수 확인은: grep -rhoE '\bti-[a-z0-9-]+' src/ --include=*.astro | sort -u
  'baby-carriage', 'backpack', 'book', 'briefcase', 'building', 'christmas-tree',
  'coffee', 'confetti', 'friends', 'heart-handshake', 'user', 'man', 'woman',
  'mood-kid', 'mood-smile-beam',
  'filled:star',   // → .ti-star-filled
];

/** SVG 원문을 data URI 안에 안전하게 넣을 수 있는 형태로 압축·이스케이프 */
function toDataUri(svg) {
  const cleaned = svg
    .replace(/\r?\n\s*/g, ' ')
    .replace(/\s+/g, ' ')
    .replace(/ class="[^"]*"/g, '')
    .replace(/currentColor/g, '#000')   // mask는 알파만 쓰므로 색은 검정 고정
    .replace(/"/g, "'")
    .trim();

  const escaped = cleaned
    .replace(/%/g, '%25')
    .replace(/#/g, '%23')
    .replace(/</g, '%3C')
    .replace(/>/g, '%3E')
    .replace(/\{/g, '%7B')
    .replace(/\}/g, '%7D');

  return `url("data:image/svg+xml,${escaped}")`;
}

async function fetchIcon(entry) {
  const filled = entry.startsWith('filled:');
  const name = filled ? entry.slice('filled:'.length) : entry;
  const set = filled ? 'filled' : 'outline';
  const className = filled ? `${name}-filled` : name;

  const url = `https://cdn.jsdelivr.net/npm/@tabler/icons@${VERSION}/icons/${set}/${name}.svg`;
  const res = await fetch(url);
  if (!res.ok) throw new Error(`${set}/${name} → HTTP ${res.status}`);

  return { className, dataUri: toDataUri(await res.text()) };
}

const header = `/* Tabler Icons 서브셋 — 실제 사용 중인 ${ICONS.length}개만 CSS mask로 인라인.
 * 원본: @tabler/icons ${VERSION} (MIT License)
 * 자동 생성 파일 — 직접 고치지 말고 \`node scripts/build-icons.mjs\` 를 다시 돌릴 것.
 *
 * 교체 전에는 jsdelivr에서 CSS 250KB + woff2 829KB를 렌더링 차단 경로로 받고 있었다.
 */

.ti {
  display: inline-block;
  width: 1em;
  height: 1em;
  flex-shrink: 0;
  vertical-align: -0.125em;
  background-color: currentColor;
  -webkit-mask: var(--ti-i) no-repeat center / contain;
          mask: var(--ti-i) no-repeat center / contain;
}
`;

const icons = await Promise.all(ICONS.map(fetchIcon));
icons.sort((a, b) => a.className.localeCompare(b.className));

const css = header + '\n' + icons
  .map(({ className, dataUri }) => `.ti-${className} { --ti-i: ${dataUri}; }`)
  .join('\n') + '\n';

await writeFile('src/styles/icons.css', css, 'utf8');
console.log(`✓ src/styles/icons.css — 아이콘 ${icons.length}개 / ${(css.length / 1024).toFixed(1)} KB`);
