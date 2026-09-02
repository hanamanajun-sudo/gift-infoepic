import type { GiftGuide } from './notion';

/**
 * 연관 가이드 선정.
 *
 * 예전에는 단일 점수(상황3·관계2·나이2·예산1) 상위 3개를 본문 맨 아래에만 붙였다.
 * 뽑히는 게 죄다 "같은 상황"으로 쏠려서, 방문자의 다음 질문
 * ("우리 애는 한 살 더 많은데", "이 예산 말고 더 싼 건")에 답하지 못했다.
 * 그래서 축을 4개로 나누고 축마다 최대 2개씩 뽑는다.
 *
 * 설계 원칙 — **틀린 걸 보여주느니 적게 보여준다.**
 * 아내 생일선물 페이지에 13세 남자아이 가이드가 붙는 종류의 사고는
 * 카드 몇 개 늘리는 이득보다 손해가 훨씬 크다. 그래서 아래 두 가드를 전 축에 건다:
 *   1) 성별이 반대면 무조건 제외
 *   2) 생애 단계(영유아/아동/청소년/청년/중장년)가 다르면 무조건 제외 (아이템 축 제외)
 *
 * 태그가 비어 있는 가이드는 걸러낼 근거가 없어 후보가 거의 안 나온다.
 * 그건 버그가 아니라 분류 태그 백필(STRATEGY-2026-09.md Tier 1-1)이 선행돼야 한다는 신호다.
 */

export type RelatedAxis = 'age' | 'occasion' | 'audience' | 'item';

export interface RelatedGroup {
  axis: RelatedAxis;
  label: string;
  guides: GiftGuide[];
}

const AXIS_LABEL: Record<RelatedAxis, string> = {
  age: '비슷한 나이대는 이렇게',
  occasion: '같은 자리, 다른 사람에게',
  audience: '같은 사람에게, 다른 선택지',
  item: '품목으로 좁혀서 고르기',
};

/**
 * 성별 표기가 두 갈래로 섞여 있다 — 여성/남성 34개, 여아/남아 10개, 공통 50개, 빈값 8개.
 * 이걸 정규화하지 않으면 "고등학생 여자"(여성)와 "16세 남자아이"(남아)가
 * 서로 반대라는 걸 알아채지 못한다. 실제로 그 사고가 났었다.
 */
function genderOf(guide: GiftGuide): 'f' | 'm' | null {
  const g = guide.recipientGender ?? '';
  if (g.includes('여')) return 'f';
  if (g.includes('남')) return 'm';
  return null; // 공통·빈값 — 어느 쪽과도 충돌하지 않는다
}

/**
 * 나이 사다리. 표기가 제각각(2세 / 초등학생 / 30대)이라 숫자 축 하나로 눌러야
 * "인접"을 계산할 수 있다. 학년·연대는 그 구간의 대표 나이로 잡는다.
 */
const AGE_ANCHOR: Record<string, number> = {
  영아: 1, 유아: 4, 초등학생: 9, 중학생: 14, 고등학생: 17,
  '20대': 25, '30대': 35, '40대': 45, '50대': 55, '60대': 65, '70대': 75,
};

function ageOf(guide: GiftGuide): number | null {
  if (guide.recipientAge != null) return guide.recipientAge;
  for (const tag of guide.ageGroup) {
    const years = tag.match(/^(\d+)세$/);
    if (years) return Number(years[1]);
  }
  for (const tag of guide.ageGroup) {
    if (AGE_ANCHOR[tag] != null) return AGE_ANCHOR[tag];
  }
  return null;
}

type Stage = 'baby' | 'child' | 'teen' | 'young' | 'mature';

function stageOf(guide: GiftGuide): Stage | null {
  const age = ageOf(guide);
  if (age == null) return null;
  if (age <= 6) return 'baby';
  if (age <= 12) return 'child';
  if (age <= 19) return 'teen';
  if (age <= 39) return 'young';
  return 'mature';
}

/**
 * '생일'은 102개 중 60개가 달고 있어서 사실상 신호가 없다.
 * 이걸 "같은 상황"으로 치면 아무 가이드나 매칭된다.
 */
const GENERIC_OCCASIONS = new Set(['생일']);

/**
 * 행사 계열. 사이트에 하나뿐인 상황(추석·환갑·퇴직…)은 "같은 상황" 축에서 짝이 안 나온다.
 * 그렇다고 아무거나 붙이면 안 되니, 사람이 납득할 묶음만 손으로 적어둔다.
 * 추석을 보는 사람은 설날도 본다. 취직 축하를 찾는 사람에겐 승진·퇴직이 같은 계열이다.
 */
const OCCASION_FAMILIES: string[][] = [
  ['추석', '설날'],
  ['결혼축하', '결혼기념일'],
  ['취직축하', '승진축하', '퇴직'],
  ['백일', '돌잔치', '출산'],
  ['입학', '졸업', '스승의날'],
  ['발렌타인', '화이트데이', '크리스마스'],
  ['어버이날', '환갑'],
];

function familyOf(occasions: string[]): string[] {
  const family = OCCASION_FAMILIES.find(f => occasions.some(o => f.includes(o)));
  return family ?? [];
}

/** 아이템 가이드(지갑·향수·텀블러…)는 슬러그 형태로 구분된다. */
function isItemGuide(guide: GiftGuide): boolean {
  return /-선물-추천$/.test(guide.slug) || /-고르는-법$/.test(guide.slug);
}

const overlaps = (a: string[], b: string[]) => a.some(v => b.includes(v));

export function getRelatedGroups(
  guide: GiftGuide,
  allGuides: GiftGuide[],
  perAxis = 2,
): RelatedGroup[] {
  const myGender = genderOf(guide);
  const myStage = stageOf(guide);
  const myAge = ageOf(guide);

  // 성별 가드 — 양쪽이 다 알려져 있고 다르면 제외
  const genderOk = (g: GiftGuide) => {
    const other = genderOf(g);
    return myGender == null || other == null || myGender === other;
  };
  // 생애 단계 가드 — 양쪽이 다 알려져 있고 다르면 제외
  const stageOk = (g: GiftGuide) => {
    const other = stageOf(g);
    return myStage == null || other == null || myStage === other;
  };

  const pool = allGuides.filter(g => g.slug !== guide.slug && genderOk(g));

  // 나이·예산 축의 오염원 차단.
  // "12세 남자아이 생일선물"과 "스승의날 선물"은 대상 나이가 비슷하다는 이유로 붙었었는데,
  // 방문자가 찾는 맥락이 전혀 다르다. 후보가 현재 가이드에 없는 고유 상황
  // (스승의날·집들이·어린이날 …)을 달고 있으면 나이·예산 축에서 뺀다.
  // 규칙은 대칭이어야 한다. 한쪽만 검사하면 "집들이 선물" 페이지에
  // (고유 상황이 없는) "16세 남자아이 생일선물"이 나이가 비슷하다는 이유로 붙는다.
  const myDistinct = guide.occasion.filter(o => !GENERIC_OCCASIONS.has(o));
  const sameOccasionProfile = (g: GiftGuide) => {
    const theirs = g.occasion.filter(o => !GENERIC_OCCASIONS.has(o));
    return myDistinct.length === 0 ? theirs.length === 0 : overlaps(theirs, myDistinct);
  };

  const used = new Set<string>();
  const take = (candidates: GiftGuide[]) => {
    const picked: GiftGuide[] = [];
    for (const g of candidates) {
      if (used.has(g.slug)) continue;
      picked.push(g);
      used.add(g.slug);
      if (picked.length >= perAxis) break;
    }
    return picked;
  };

  // ── 축 1. 인접 나이 ──
  // 같은 나이(Δ0)는 제외한다. 같은 나이 페이지는 카니발라이제이션 정리 대상이지 추천 대상이 아니다.
  // 허용 폭은 아이일수록 좁게 — 12세와 16세는 완전히 다른 선물이지만 35세와 39세는 사실상 같다.
  const byAge = myAge == null ? [] : pool
    .filter(g => !isItemGuide(g))
    .filter(sameOccasionProfile)
    .map(g => ({ g, age: ageOf(g) }))
    .filter((x): x is { g: GiftGuide; age: number } => x.age != null)
    .map(({ g, age }) => ({ g, delta: Math.abs(age - myAge) }))
    .filter(({ delta }) => delta > 0 && delta <= (myAge < 20 ? 3 : 12))
    .sort((a, b) => a.delta - b.delta)
    .map(({ g }) => g);

  // ── 축 2. 같은 상황(단, 범용 태그 제외), 다른 대상 ──
  const myOccasions = guide.occasion.filter(o => !GENERIC_OCCASIONS.has(o));
  const direct = myOccasions.length === 0 ? [] : pool
    .filter(g => overlaps(g.occasion.filter(o => !GENERIC_OCCASIONS.has(o)), myOccasions))
    .filter(g => !overlaps(g.relation, guide.relation));

  // 직접 매칭이 없으면(사이트에 그 행사 페이지가 하나뿐이면) 같은 계열로 넓힌다
  const family = familyOf(myOccasions).filter(o => !myOccasions.includes(o));
  const byOccasion = (direct.length ? direct : pool.filter(g => overlaps(g.occasion, family)))
    .sort((a, b) => b.updatedAt.getTime() - a.updatedAt.getTime());

  // ── 축 3. 같은 대상, 다른 선택지 ──
  //
  // 원래 "같은 대상 · 다른 예산"이었는데 실제 데이터에서 후보가 0개로 수렴했다.
  // 예산 밴드는 누적이라(2만원 상품은 3만·5만·10만원 밴드에 전부 해당) 겹치는 게 정상이고,
  // "예산이 겹치지 않는 같은 대상 가이드"는 사실상 존재하지 않는다.
  //
  // 그래서 조건을 "같은 대상"으로 넓히고, 정렬로 다양성을 만든다 —
  // 예산 구성이 많이 다른 것을 앞에 세워서 결과적으로 "다른 가격대"가 먼저 보이게 한다.
  const budgetDistance = (g: GiftGuide) =>
    g.budgetTag.filter(b => !guide.budgetTag.includes(b)).length +
    guide.budgetTag.filter(b => !g.budgetTag.includes(b)).length;

  const byAudience = pool
    .filter(stageOk)
    .filter(sameOccasionProfile)
    .filter(g => overlaps(g.relation, guide.relation) || overlaps(g.ageGroup, guide.ageGroup))
    .sort((a, b) => budgetDistance(b) - budgetDistance(a) || b.updatedAt.getTime() - a.updatedAt.getTime());

  // ── 축 4. 아이템 가이드 ──
  // 아이템은 대상 무관하게 성립하므로 생애 단계 가드를 걸지 않는다.
  // 다만 관심사가 겹치는 것을 앞세워서, 아무 관련 없는 품목이 1순위로 오지 않게 한다.
  // 관심사가 겹치는 것만. 예전엔 interests가 비면 전부 통과시켰는데,
  // 그 결과 67개 페이지에 똑같은 카드 두 장(커플·어린이 고르는 법)이 붙었다.
  // 아무 데나 붙는 추천은 없느니만 못하다.
  // 관심사가 겹치는 아이템 가이드를 먼저 본다.
  // 관심사 태그가 없는 가이드가 절반이라(50/102) 그때는 예산대가 비슷한 아이템을 형제로 친다 —
  // 3만원짜리 텀블러를 보는 사람에게 30만원짜리 게임기를 들이밀지 않기 위해서다.
  // (예전엔 관심사가 비면 전부 통과시켜서 67개 페이지에 똑같은 카드 두 장이 붙었다.)
  const budgetOverlap = (g: GiftGuide) =>
    g.budgetTag.filter(b => guide.budgetTag.includes(b)).length;

  const itemPool = pool.filter(g => isItemGuide(g) && g.slug !== guide.slug);
  const byItem = guide.interests.length > 0
    ? itemPool
        .filter(g => overlaps(g.interests, guide.interests))
        .sort((a, b) => budgetOverlap(b) - budgetOverlap(a))
    : itemPool
        .filter(g => budgetOverlap(g) > 0)
        .sort((a, b) => budgetOverlap(b) - budgetOverlap(a) || a.slug.localeCompare(b.slug));

  return (
    [
      ['age', byAge],
      ['occasion', byOccasion],
      ['audience', byAudience],
      ['item', byItem],
    ] as [RelatedAxis, GiftGuide[]][]
  )
    .map(([axis, candidates]) => ({ axis, label: AXIS_LABEL[axis], guides: take(candidates) }))
    .filter(group => group.guides.length > 0);
}

/**
 * 본문 중간(상품 사이)에 끼울 카드 하나.
 * 끝까지 스크롤하지 않는 방문자가 대다수라 맨 아래 목록만으로는 닿지 않는다.
 * 나이 축을 우선하는 이유: "우리 애는 한 살 더 많은데"가 이 사이트에서 가장 흔한 이탈 사유다.
 * 아이템 축은 여기서 제외한다 — 상품을 읽는 중에 품목 가이드를 들이미는 건 흐름을 끊는다.
 */
export function getInlineSuggestion(
  groups: RelatedGroup[],
): { guide: GiftGuide; label: string } | null {
  for (const axis of ['age', 'audience', 'occasion'] as RelatedAxis[]) {
    const group = groups.find(g => g.axis === axis);
    if (group?.guides.length) return { guide: group.guides[0], label: group.label };
  }
  return null;
}
