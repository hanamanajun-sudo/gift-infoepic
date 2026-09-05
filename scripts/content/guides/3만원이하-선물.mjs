import { h2, h3, p, bullet, table } from '../lib.mjs';

export const slug = '3만원이하-선물';
export const title = '3만원 이하 선물 추천 TOP6 — 받으면 명품 받은 기분이 나는 것들';
export const description =
  '3만원 이하 선물 추천 TOP6. 향수·스킨케어·티세트처럼 실제 가격보다 ' +
  '고급스럽게 느껴지는 미니어처·세트 구성 위주로 골랐습니다. 친구· ' +
  '직장동료·선생님 모두에게 무난합니다.';
export const occasion = ['생일', '스승의날', '크리스마스'];
export const relation = ['친구', '직장동료', '선생님'];
export const ageGroup = ['20대', '30대', '고등학생'];
export const budgetTag = ['3만원이하', '5만원이하', '10만원이하'];
export const interests = ['생활', 'K뷰티', '향기'];
export const recipientGender = '공통';
export const priceMin = 9900;
export const priceMax = 25900;

export const intro =
  '3만원대 선물 후기를 보면 "적당한 가격에 명품 받은 기분이 들어서 ' +
  '선물하는 사람이나 받는 사람이나 둘 다 기분 좋다"는 반응이 자주 ' +
  '나옵니다. 이 가격대의 핵심은 실제 가격보다 고급스럽게 느껴지는 ' +
  '구성을 찾는 겁니다. 향수·스킨케어처럼 미니어처 여러 개를 세트로 ' +
  '주는 상품이 대표적입니다. 이 글은 그런 기준으로 친구·직장동료· ' +
  '선생님 모두에게 무난한 선물을 골랐습니다.';

export const blocks = [
  h2('가격대별로 고르기'),
  table(
    ['예산', '추천', '이럴 때'],
    [
      ['9천원대', '오르덴 향수 디스커버리 세트 5종', '여러 향을 한 번에 선물하고 싶을 때'],
      ['1만원대', '자황수 보음 미니어쳐 여행용 5종', '스킨케어 선물을 원할 때'],
      ['2만원대', '헤트라스 퍼퓸 버블 핸드워시 5종', '바디케어 선물을 원할 때'],
      ['2만원대', '오설록 티 베리에이션 세트', '어른께 드리는 차 선물을 원할 때'],
      ['2만원대', '자주가게 식물성 멜라토닌', '수면 부족한 분께 건강을 챙겨드릴 때'],
      ['2만원대', '소이캔들 플라워 캔들워머 세트', '인테리어 소품을 원할 때'],
    ]
  ),

  h2('3만원 이하 선물 추천 TOP6'),

  h3('여러 향을 한 번에 "오르덴 향수 디스커버리 세트 5종"'),
  p(
    '미니 트래블 사이즈 5종이 세트로 구성돼 있어 취향을 몰라도 무난 ' +
    '하게 고를 수 있습니다. 9,900원.'
  ),

  h3('스킨케어 선물이라면 "자황수 보음 미니어쳐 여행용 5종"'),
  p(
    '여행용으로도 쓸 수 있는 미니어처 구성입니다. 실제 가격보다 ' +
    '알차 보이는 세트 구성이 장점입니다. 14,900원.'
  ),

  h3('바디케어 선물 "헤트라스 퍼퓸 버블 핸드워시 5종 세트"'),
  p(
    '고보습 산양유 성분에 향까지 신경 쓴 핸드워시 세트입니다. 5종 ' +
    '구성이라 선물 느낌이 확실합니다. 21,800원.'
  ),

  h3('어른께 드리는 차 선물 "오설록 티 베리에이션 세트"'),
  p(
    '인지도 있는 티 브랜드로, 선생님이나 어른께 드리는 선물로도 ' +
    '무난합니다. 25,500원.'
  ),

  h3('건강을 챙겨드리고 싶다면 "자주가게 식물성 멜라토닌"'),
  p(
    '식약청 인증·HACCP 마크가 있는 수면 영양제입니다. "커피 쿠폰만 ' +
    '보내다가 건강 챙기는 선물로 바꿨더니 반응이 좋았다"는 후기가 ' +
    '반복적으로 나오는 카테고리입니다. 25,600원.'
  ),

  h3('인테리어 소품이라면 "소이캔들 플라워 캔들워머 세트"'),
  p(
    '캔들워머와 소이캔들이 함께 구성돼 있어 화기 부담 없이 향을 ' +
    '즐길 수 있습니다. 밝기 조절도 됩니다. 25,900원.'
  ),

  h2('받으면 명품 받은 기분이 나는 것들'),
  p(
    '3만원이라는 예산은 애매합니다. 너무 저렴하면 성의 없어 보이고, ' +
    '무리해서 비싼 걸 고르기도 부담스럽습니다. 실제 후기를 보면 이 ' +
    '가격대에서 반응이 좋은 선물에는 공통점이 있습니다 — 향수나 ' +
    '스킨케어처럼 미니어처 여러 개를 세트로 구성해서, 실제 가격보다 ' +
    '알차고 고급스럽게 느껴지는 상품입니다. 낱개로 사면 이 가격에 ' +
    '살 수 없는 브랜드를 미니 사이즈로 여러 개 받는 느낌이라, 받는 ' +
    '사람도 "이 가격에 이 정도라고?" 하는 반응이 나옵니다. 이 원리를 ' +
    '기억해두면 3만원 예산 안에서도 실패 확률을 크게 줄일 수 있습니다.'
  ),

  h2('이건 사지 마세요'),
  bullet('향이나 성분을 미리 확인하지 않은 바디케어 제품 — 향에 민감하거나 특정 성분에 예민한 사람도 있습니다.'),
  bullet('유통기한이 짧게 남은 식품·건강기능식품 — 구매 전 꼭 확인하세요.'),
  bullet('낱개 구성보다 저렴해 보이는 무성의한 조합 — 세트 구성 자체가 선물력을 좌우합니다.'),
  bullet('건강기능식품을 이미 챙겨 먹고 있는 사람에게 중복 선물 — 미리 확인하고 겹치지 않는 걸로 고르세요.'),

  h2('자주 묻는 질문'),
  h3('3만원대 선물, 뭐가 제일 반응이 좋나요?'),
  p('향수·스킨케어처럼 미니어처 여러 개를 세트로 구성한 상품이 실제 가격보다 알차 보여서 반응이 좋습니다.'),
  h3('친구·직장동료·선생님 선물을 다르게 골라야 하나요?'),
  p('스킨케어·바디케어·차는 관계 구분 없이 무난합니다. 다만 선생님·어른께는 차·건강 관련 선물이, 친구에게는 향수·뷰티 세트가 좀 더 자연스럽습니다.'),
  h3('예산을 더 쓸 수 있다면요?'),
  p('5만원 이하, 10만원 이하 선물 가이드에서 더 다양한 선택지를 볼 수 있습니다.'),

  h2('관련 가이드'),
  bullet('1만원 이하 선물만 비교하기'),
  bullet('5만원 이하 선물만 비교하기'),
  bullet('캔들 선물 추천: 촛불이냐 워머냐, 그게 먼저입니다'),
];

export const products = [
  {
    rank: 1,
    name: '오르덴 향수 오드퍼퓸 디스커버리 세트 5종 미니 트래블키트',
    price: 9900,
    pros: '미니 트래블 사이즈 5종 세트. 취향 몰라도 무난하게 선택 가능.',
    imageUrl: 'https://ads-partners.coupang.com/image1/GhdDX43JRqIR7TlkGkzqqrx0k4V7Uh8n6DnjFjCEqOpf2u2cabXbl_9dPCqUxoXkxHuQvP9gHWqFSBdghAqCeU2bC1Tyn_6_LkoZD5CgX1ggM2Df3fY0XIIauvHbGG4eJToVGW6FF0ACK9HVyz9p_dzPiA0AbZ89bmtoV4FVB_P_yhPoqBFj7gXqB_fqJbLl4sG77BSc_pUmEQsKF2DPGP01JIO_lMUw1iB2kUMYpIjhLVVQSE0kauofhGw7nEauDJBzeOGa3Qy75Lntkk_achXgD6LoQD4520VBtKeHHAZJpIf_qFSahifa0MySGB36uKcAuCjZkrYzFki_aCYOhVsgpKzCEl6QdLosNL_G3WBEXo9gm5LvaMvKaNmjEjDfM79KckakI9ltGcoiZQFk1AcVPZNoOrUGPDbnllHfw-sxvRBmGA16yjjj0BAbNJqALsgT_xh6DeBA8ePBEPkeGviUt-tQQS8DYH3uDFVFqzz_S3JBNdnumP1Wx-gdrrmJk-NPhcPfOxURqtxGXQHFJcUO0KWbZseLDfJqewRbkLOMh8E=',
    coupangUrl: 'https://link.coupang.com/a/gNXxeDRvoq',
    naverUrl: null,
  },
  {
    rank: 2,
    name: '자황수 보음 미니어쳐 여행용 5종 세트',
    price: 14900,
    pros: '여행용으로도 활용 가능한 스킨케어 미니어처 5종.',
    imageUrl: 'https://ads-partners.coupang.com/image1/3ivKljKDG3HDbYaR3nri5vIfdbQIDqDaJ_kpg44ktPigQi17i9g9k6VMdTwu6Z584ikxXdqmMdsqC2jh6LFIIxTtlhBf0XQX5LwtG9QktvFtMtkJEtl065HyQ0CMp6pjoBf2TS-Skac6EuOutS0ug2Qvr8Vs12PySz512V3S90O6ySFOpxYb-UEX97UwueW_DLNtYFSH5CvZy7ENQnXyeOmGvFeMF6zDszICRTusZhWMmzuqwPV6wR_xnHSVgu-0iLLrpK8Pg7pnSomof4XYdP0W18xkUDfqKMVfpQ0AS4z9QzQCYijCMnWtlrcyvriC3Tr-Km2bluJntzbPwtFfZVcwoRL01FHg7pDZd8l7TPYJ8VhdY0jQYfd7f_NEtjAQG11qFlLQF43KB6bdUnK8WqBrg5y8NTR0mEHIjp-nh558FP9TrMHxRSxPkzLWBpMy93J7LHzfIEMs8zzfumGj0D6s72xkZqIl-TyMWnfM2p-X607e0Ye09FwKWr6Q45pvR1xZr0OXZCWouwj8L-DbyIzL7QLYqhPuHw==',
    coupangUrl: 'https://link.coupang.com/a/gNXxeIoZ88',
    naverUrl: null,
  },
  {
    rank: 3,
    name: '헤트라스 퍼퓸 버블 고보습 산양유 핸드워시 5종 세트',
    price: 21800,
    pros: '고보습 산양유 성분+향까지 신경 쓴 핸드워시 5종.',
    imageUrl: 'https://ads-partners.coupang.com/image1/sbitJu4yRVec2VqrseU6SMrddOeUUQYul5E375pagok1vJdniYl6h276UwUECTUZtHcEm0IdYP7cA5mS-dN2V0qXwD9Sojex5v2nn-YNGXKzGfSSp9sHZe_Lz1PNbufv92W7fqZtJo-3sw-9mse6hYqQxn65noaW4A-FZWL_RgYTCMsjwhogGQwpq-1SYuU-Ig2PU4af7YXHbnPZRtya-Tj7oFV1FHy2_6Xu3VN9dHWCpsZ-lMoP0vuO0Hc3FfzzhyS0gMfDvXDZR1lCLTAXLZErslzKGCf69NSCHhqV_Uo3JRpINqz1S-ncHGvjQw80--y4hCfzqbO4pSnQUmDYLKwjspAY8EAVl5b38149EHpZvxLOPM7JzDwTlDztCK6-HXakfOWGOscy34deysS1mPgYCYHrsRjC3FBkKqf8wHFhHlivitKVjFz1-jxibqxfzFRz4eGypF9s6CLZVgkd_4E96sEbeYNoezjNlayXM7E1T461YV9p_AQaxEu9vePK9LrNqKwDxA==',
    coupangUrl: 'https://link.coupang.com/a/gNXxeOhCZU',
    naverUrl: null,
  },
  {
    rank: 4,
    name: '오설록 티 베리에이션 오 티백 차 세트',
    price: 25500,
    pros: '인지도 있는 티 브랜드. 선생님·어른께 드리는 선물로 무난.',
    imageUrl: 'https://ads-partners.coupang.com/image1/6axtSTlO8Cybv2CX6ZXvp5C-0SAlSDGH7A2i08vQfK6VH6ZC2zV5hLpvuPdVX0MC5MKCjOI-Qc8plDelVP-0cTeZ3enKaJ1-c2DkuxViYN-VyObJ8on9J_3y4Z3LfjbazdpxSyD_DwKTJXYOV52SwZb54m6bFX1KQgQWXkd30ubWEtwCORel6CpHbbYD5sbcYHG44-9tXQEzafhOU6DI4yxag6n1iEjUg8gKx8vOIM1V-pscClSuP6tyDbjMv6P5SQjEiaG9nb1SzaQQ_9ne72M1Oz1zahLR1-47cAbgliQx_JJkmaRjvtA37rRvql0GN0cLhP3AhHodr89uYDB2T53JjJWvZDTkdB1gLGCcKe9rI-qLkboW7TBIotVEt0OY9LSG7bi56Ldl-NWotdzyx7i8VZYyh06i1S82NAIHbX3LPPOTmlkeiWBExVuieT5WwYjSN5PEmq2f7PagUqZqss3o3sIIz9p2o_a2VNmiHPWTitBqNUhjG5xGPs3Cy-44ZeGvsT5d2ZNcZJ7Zumc9CXfIRw==',
    coupangUrl: 'https://link.coupang.com/a/gNXxeSU1eK',
    naverUrl: null,
  },
  {
    rank: 5,
    name: '자주가게 식물성 멜라토닌 1일 2mg 함유 멜라 테아닌 나잇',
    price: 25600,
    pros: '식약청인증·HACCP. "건강 챙기는 선물로 바꿨더니 반응 좋았다"는 후기 다수.',
    imageUrl: 'https://ads-partners.coupang.com/image1/FLOgPst9ea71pWE8FJbBon5NrbswNV0WyJ4nWUvxV6QX3nWEL125aGon1F4pg_t59EiMclIEMz7CtEWIoop9kXunMUniCNrhDVh2aK-7nsjmV7OBVe7pYULPlmZctU5cx4TG8zJLg_yiGf2SvD__PReN6MlkUT6EEbUMpzaDqrDuNsOuMN_BE7cbYYL-Xle84DXK5-qZTpJVBJENkZRFArAR6dsknK2gnDMXQHDK55q5ieWvR2z6cSMmOlXhI6rTqrwVChelc-05978s0oNXiop48lydFpabXCHeriNyL0xYc8N4och4pHqtJuYmoFJUXh-pRsoZeus8PNruoRRJLuo5aACgG2sQxVKBJUHRWCLRj9vqn79GwWOYD2pzvAryWOmJPWgQ25uf_4iRg3pK4XRqa1uVRhliGhgfcqkkPHJbyrXY_713bJNXHoMWuQ89f4Q-uT-ECOXNnhovPuKdTkywWtphc-laEAB1WB0NeUbMCeyG9uYq9Z8Avb_I7retAUgia-UAy8O_fF86qMt1m95cIYU7qpQcKw==',
    coupangUrl: 'https://link.coupang.com/a/gNXxeYRJGS',
    naverUrl: null,
  },
  {
    rank: 6,
    name: '소이캔들 스몰자 90g 플라워 캔들워머 세트',
    price: 25900,
    pros: '캔들워머+소이캔들 세트. 밝기 조절 가능, 화기 부담 없음.',
    imageUrl: 'https://ads-partners.coupang.com/image1/UEf0HEMEka6lTjkmUOLfUQS8t70p2li9-aQQA5R0NLOb2Eves6PhSZIwxrWCm8oFjZ8JtkmRjZ9U9aAi9u0nG6rL15cfs70c277SgSrcB7tTRH19oRnSGc7bVJfYFVhVaNxQBbk0EMAgxBQIqLKc9ck1cHz_iyzj1ZafSWRkl_V3iJIVhqpmdxvQs5euxqI8rO96-UfC6ywpWLj5dX-Ft5GqV-dEdiDBHOPwPJ2tcBXjE3rO-cvdAd1Zg9lS27KbERTJHwiPF-xQMkM8JQDVARYbE7sY1wZs09Iz7UrwjqIz2mNwrDEbuy6n9pMKvxfhkM9ukonIb6IgoQq5LiBbdgAdK99XeJ1DGNl-X_VFkh3mJJRctfY9rNTnF4C_HGGgHgoEG8xQtR2-ZD5avoz-zEI4zLbZKWZXv4BGm5IlzZ36ydSR6JXoXI50DvukcAIKDRh6tg3bRAYmAJz0tGp8kpr7iqRia6y5DTLchLxJqhiqhNt3swZVCjxYH7eiNPEBajAOOwj-VsWkFXOgz-2jahhyQESafWbd',
    coupangUrl: 'https://link.coupang.com/a/gNXxe5jyNM',
    naverUrl: null,
  },
];
