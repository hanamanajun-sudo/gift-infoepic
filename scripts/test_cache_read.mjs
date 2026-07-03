// 캐시 기반 getGiftGuides 테스트
import { readFileSync, existsSync } from 'fs';

const path = new URL('../src/data/notion-cache.json', import.meta.url);
console.log('Path:', path.pathname);
console.log('Exists:', existsSync(path));

if (existsSync(path)) {
  const raw = readFileSync(path, 'utf-8');
  const cache = JSON.parse(raw);
  console.log('Guides:', cache.guides.length);
  console.log('Products:', cache.products.length);
  console.log('\nGuide slugs (first 5):');
  cache.guides.slice(0, 5).forEach(g => console.log(`  ${g.slug}`));
  console.log('\nGuide slugs (last 5):');
  cache.guides.slice(-5).forEach(g => console.log(`  ${g.slug}`));
  console.log('\nFirst guide keys:', Object.keys(cache.guides[0]).join(', '));
}
