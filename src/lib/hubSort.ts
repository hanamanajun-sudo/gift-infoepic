import type { GiftGuide } from './notion';

export type HubAxis = 'ageGroup' | 'relation' | 'occasion' | 'budgetTag';

/**
 * 허브(나이·관계·상황·예산) 페이지의 가이드 정렬.
 *
 * 기존에는 제목 가나다순이라 "40대" 허브의 첫 카드가 "10만원 이하 선물"이었다.
 * 방문자가 허브 이름과 직접 맞는 가이드를 먼저 보도록 다음 순서로 올린다.
 *   1) 제목이 허브 이름으로 시작하는 가이드 ("40대 남성 생일선물" → 40대 허브 최상단)
 *   2) 그 축의 태그가 적게 붙은 가이드 — 태그가 적을수록 그 허브 전용에 가깝다
 *   3) 기존 순서(제목 가나다순) 유지
 */
export function sortHubGuides(guides: GiftGuide[], axis: HubAxis, label: string): GiftGuide[] {
  const startsWith = labelMatchers(label);
  const rank = (g: GiftGuide) => {
    const title = g.title.replace(/\s+/g, '');
    const slug = decodeURIComponent(g.slug);
    return {
      lead: startsWith.some(re => re.test(title) || re.test(slug)) ? 0 : 1,
      tags: g[axis].length,
    };
  };
  return guides
    .map((g, i) => ({ g, i, r: rank(g) }))
    .sort((a, b) => a.r.lead - b.r.lead || a.r.tags - b.r.tags || a.i - b.i)
    .map(x => x.g);
}

// 허브 라벨이 제목·슬러그에 등장하는 표기 (예: 7세 → 7살, 3만원이하 → "3만원 이하"의 공백 제거본)
function labelMatchers(label: string): RegExp[] {
  const forms = new Set<string>([label]);
  if (/^\d+세$/.test(label)) forms.add(label.replace('세', '살'));
  return [...forms].map(f => new RegExp('^' + escapeRegExp(f)));
}

function escapeRegExp(s: string): string {
  return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}
