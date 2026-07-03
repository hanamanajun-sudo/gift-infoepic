import { writeFileSync, mkdirSync, existsSync } from 'fs';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';
import { searchNaverBlog } from './naver-blog.mjs';
import { collectYoutubeOpinions } from './youtube.mjs';
import { slugify } from './lib.mjs';

// 사용법: node --env-file=.env scripts/research/collect.mjs "12세 여아 선물" "초등 고학년 여자 생일선물 후기"
const keywords = process.argv.slice(2);

if (keywords.length === 0) {
  console.error('키워드를 하나 이상 넘겨주세요. 예: node --env-file=.env scripts/research/collect.mjs "12세 여아 선물"');
  process.exit(1);
}

const OUT_DIR = join(dirname(fileURLToPath(import.meta.url)), '../../src/data/research');
if (!existsSync(OUT_DIR)) mkdirSync(OUT_DIR, { recursive: true });

for (const keyword of keywords) {
  console.log(`\n[수집 중] ${keyword}`);

  const [naverBlog, youtube] = await Promise.all([
    searchNaverBlog(keyword),
    collectYoutubeOpinions(keyword),
  ]);

  const out = {
    keyword,
    collectedAt: new Date().toISOString(),
    naverBlog,
    youtube,
  };

  const outPath = join(OUT_DIR, `${slugify(keyword)}.json`);
  writeFileSync(outPath, JSON.stringify(out, null, 2), 'utf-8');

  const commentCount = youtube.reduce((sum, v) => sum + v.comments.length, 0);
  console.log(`  네이버 블로그 ${naverBlog.length}건, 유튜브 영상 ${youtube.length}개(댓글 ${commentCount}건) 저장 → ${outPath}`);
}
