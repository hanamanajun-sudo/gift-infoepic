import rss from '@astrojs/rss';
import { getGiftGuides } from '../lib/notion';

export async function GET(context) {
  const guides = await getGiftGuides();
  const sorted = guides.sort((a, b) => b.updatedAt.getTime() - a.updatedAt.getTime());

  return rss({
    title: '선물추천 가이드 — 나이·관계·예산으로 찾는 선물',
    description: '나이, 관계, 예산으로 찾는 완벽한 선물 가이드. 생일선물부터 크리스마스 선물까지.',
    site: context.site,
    items: sorted.map(guide => ({
      title: guide.title,
      description: guide.description || guide.intro,
      pubDate: guide.updatedAt,
      link: `/선물/${guide.slug}/`,
    })),
    customData: '<language>ko-KR</language>',
  });
}
