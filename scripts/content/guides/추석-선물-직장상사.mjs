import { h2, h3, p, bullet, table } from '../lib.mjs';

export const slug = '추석-선물-직장상사';
export const title = '추석 선물 거래처·직장상사 추천 — 청탁금지법부터 확인하세요';
export const description =
  '추석 선물 거래처·직장상사 추천 TOP6. 공직자인지 아닌지에 따라 금액 기준이 완전히 다릅니다. ' +
  '청탁금지법 상한액부터 대량 발송용, 격식 있는 자리까지 예산별로 정리했습니다.';
export const occasion = ['추석'];
export const relation = ['직장상사', '직장동료'];
export const budgetTag = ['3만원이하', '5만원이하', '10만원이하', '20만원이하', '20만원이상'];
export const priceMin = 25900;
export const priceMax = 208900;

export const intro =
  '거래처나 직장상사께 드리는 추석 선물은 부모님 선물과 고민의 결이 다릅니다. ' +
  '"얼마짜리를 드려야 하나"보다 먼저 막히는 지점이 있습니다 — ' +
  '상대가 공무원이면 법으로 정해진 금액 상한이 있고, 아니면 그런 제한 자체가 없습니다. ' +
  '이걸 헷갈려서 "명절 선물 5만원인가 30만원인가"를 검색하는 사람이 많았습니다. ' +
  '네이버 블로그·유튜브 댓글을 모아보니 실제로 "회사가 선물을 아예 주고받지 말자고 한다"는 글까지 있었습니다. ' +
  '금액 기준을 먼저 정리하고, 대량 발송용부터 격식 있는 자리까지 예산별로 상품을 골랐습니다.';

export const blocks = [
  h2('가격대별로 고르기'),
  table(
    ['예산', '추천 상품', '어떤 자리에 맞나'],
    [
      ['3만원 이하', '홍삼 스틱 / 한과 세트', '여러 곳에 나눠 보낼 때, 공직자에게도 항상 안전한 금액'],
      ['4~5만원대', '참치 세트 / 견과 세트', '가장 무난한 기본값 — 청탁금지법 일반 선물 상한(5만원)과도 맞음'],
      ['7~10만원대', '굴비 세트', '예의를 확실히 갖춰야 하는 거래처'],
      ['20만원대', '한우 세트', '가장 격식 있는 자리 — 공직자 명절 상한(30만원) 이내'],
    ]
  ),

  h2('추석 선물 추천 TOP6'),

  h3('여러 곳에 나눠도 부담 없는 "개성상인 녹용 홍삼 스틱"'),
  p(
    '27,900원, 쇼핑백 포함, 로켓배송. 청탁금지법상 공직자에게 드리는 일반 선물의 상한선(5만원)에도 여유 있게 들어가는 금액이라, ' +
    '상대가 공무원인지 아닌지 확인이 어려운 상황에서도 가장 안전합니다. ' +
    '이럴 때 맞습니다: 여러 거래처·부서에 같은 선물을 두루 돌려야 할 때.'
  ),

  h3('정갈한 인상을 주는 "수담한과 고급지함 2호"'),
  p(
    '25,900원, 2단 구성 1.2kg, 로켓배송. 홍삼과 달리 건강기능식품이 아니라서 이미 여러 곳에서 홍삼을 받은 상대에게도 부담이 없습니다. ' +
    '한과라는 품목 자체가 격식 있는 명절 인사로 오래 쓰여왔습니다. ' +
    '이럴 때 맞습니다: 홍삼·견과가 겹칠 것 같은 자리, 정갈한 인상을 주고 싶을 때.'
  ),

  h3('대량 발송에 최적화된 "동원스페셜 참치세트 10호"'),
  p(
    '48,550원. 상품명 자체가 "회사직원·거래처 대량 답례품"으로 나올 만큼, 여러 곳에 동시에 보내는 용도로 많이 쓰입니다. ' +
    '유통기한이 길어 받는 쪽에서도 부담 없이 보관할 수 있습니다. ' +
    '이럴 때 맞습니다: 거래처 여러 곳에 같은 시기에 발송해야 해서 단가와 배송 편의를 함께 고려해야 할 때.'
  ),

  h3('무난한 중간 격식 "추석선물 견과류 선물세트 2호"'),
  p(
    '71,460원. 상품 설명에 "어르신·거래처 대량주문"이 명시돼 있을 만큼 이 용도로 검증된 구성입니다. ' +
    '보관이 쉽고 호불호가 적어 상대의 취향을 모를 때도 무난합니다. ' +
    '이럴 때 맞습니다: 홍삼·한과보다는 한 단계 격식을 올리고 싶지만 굴비·한우까지는 부담스러울 때.'
  ),

  h3('예의를 확실히 갖추는 "명품 오가 특대 굴비 세트 10미"'),
  p(
    '97,000원, 100% 국산. 한국 명절에서 굴비는 격식을 갖춘 선물로 오래 통용돼 왔고, 이 가격대에서는 거래처 선물의 대표 격입니다. ' +
    '냉장 보관이 필요하므로 상대 회사가 명절 연휴 동안 비어 있지는 않은지, 받을 수 있는 날짜를 먼저 확인하세요. ' +
    '이럴 때 맞습니다: 첫 거래를 튼 신규 거래처, 확실히 예의를 갖춰야 하는 자리.'
  ),

  h3('가장 격식 있는 자리에 "농협안심한우 1++등급 신선구이 세트"'),
  p(
    '208,900원, 냉장 프리미엄. 공직자에게 드리는 경우라도 명절 기간 한정 농축수산물 상한선(30만원) 안에 여유 있게 들어갑니다. ' +
    '1++ 등급이라 가격만큼의 격식이 분명하게 드러납니다. ' +
    '이럴 때 맞습니다: 핵심 거래처, 여러 해 관계를 이어온 상사·파트너처럼 확실히 예산을 들여야 하는 자리. 냉장 배송이라 수령 날짜 확인이 필수입니다.'
  ),

  p('이 목록은 대량 발송 적합성, 청탁금지법 상한선과의 관계, 배송·보관 조건을 기준으로 정리했습니다.'),
  bullet('마지막 상품 정보 확인일: 2026-09-03'),
  bullet('확인한 정보: 상품명·가격·구성·배송 유형'),
  bullet('제외 기준: 상대의 개인 취향을 알아야 하는 품목(주류·향수), 보관 조건이 까다로운데 대량 발송이 어려운 품목'),
  bullet('제휴 고지: 일부 링크를 통해 구매하면 수수료를 받을 수 있으나, 수수료는 추천 순서에 영향을 주지 않습니다.'),

  h2('상대가 공무원인가요? 여기서 갈립니다'),

  h3('공직자·공공기관 관계자라면'),
  p(
    '청탁금지법(김영란법)이 적용됩니다. 원활한 직무 수행이나 사교·의례 목적의 선물은 평소 5만원까지, ' +
    '농축수산물·농축수산가공품은 15만원까지 허용됩니다. ' +
    '명절 기간에는 농축수산물에 한해 이 금액이 두 배로 올라 30만원까지 가능합니다 — 위 목록의 한우 세트가 여기 해당합니다. ' +
    '가공식품(참치·견과·한과 등)은 명절이라고 상한이 올라가지 않으니 5만원 기준을 그대로 적용하세요. ' +
    '적용 대상은 국가·지방공무원, 공직유관단체·공공기관 임직원, 학교·학교법인 관계자, 언론사 임직원과 그 배우자입니다.'
  ),

  h3('일반 회사원·거래처 담당자라면'),
  p(
    '청탁금지법은 공직자가 받는 선물에만 적용됩니다. 받는 사람이 공무원이 아닌 일반 민간기업 직원이라면 ' +
    '법적인 금액 제한 자체가 없습니다. 다만 법이 없다고 기준이 없는 건 아닙니다 — 회사 자체 규정(청렴 서약, 접대비 규정)이나 ' +
    '업계 관례를 따르는 경우가 많고, 실제로는 5만원에서 10만원 사이가 가장 흔한 구간입니다. ' +
    '거래처 담당자가 바뀐 지 얼마 안 됐거나 첫 거래라면, 상대 회사의 선물 수령 정책을 먼저 확인하는 것이 안전합니다.'
  ),

  h2('회사가 아예 선물을 금지했다면'),
  p(
    '최근 들어 임직원 간 또는 거래처와의 선물 수수 자체를 사규로 금지하는 회사가 늘고 있습니다. ' +
    '이런 경우 개인적으로 선물을 준비해서 보내면 오히려 상대를 곤란하게 만들 수 있습니다. ' +
    '금지 여부가 확실하지 않다면 무리하게 개인 명의로 보내기보다, 명절 인사 카드나 메일로 대체하거나 ' +
    '회사 총무팀·컴플라이언스 부서를 통해 회사 명의로 통일해서 진행하는 쪽이 안전합니다. ' +
    '거래처가 큰 조직일수록 이 확인 절차 자체가 실례가 되지 않으니, 애매하면 먼저 물어보세요.'
  ),

  h2('이건 피하세요'),
  bullet('개인 취향이 갈리는 주류·향수는 피하세요 — 회사 내 반입이 금지된 품목일 수 있고, 술을 못 마시는 경우도 많습니다.'),
  bullet('신선식품(굴비·한우)을 보낼 땐 수령 가능 날짜를 반드시 먼저 확인하세요 — 회사가 명절 연휴 동안 비어 있으면 상합니다.'),
  bullet('거래처에는 현금성 상품권을 피하는 게 안전합니다 — 개인 지인과 달리 대가성으로 오해받을 소지가 더 큽니다.'),

  h2('자주 묻는 질문'),

  h3('거래처 선물, 회사 대표 명의로 보내야 하나요 개인 명의로 보내야 하나요?'),
  p(
    '업무상 관계로 만난 거래처라면 회사 명의(부서명 포함)로 보내는 것이 일반적입니다. ' +
    '개인적으로 친분이 두터워진 경우가 아니라면 회사 명의 쪽이 오해의 소지가 적습니다.'
  ),

  h3('여러 거래처에 다르게 보내도 되나요, 같은 걸 보내야 하나요?'),
  p(
    '거래 규모나 관계의 깊이에 따라 예산을 다르게 잡는 것이 자연스럽습니다. ' +
    '다만 같은 급의 거래처끼리는 비슷한 수준으로 맞추는 것이 뒷말이 없습니다.'
  ),

  h3('청탁금지법을 넘는 선물을 보내면 받는 사람도 처벌받나요?'),
  p(
    '네, 청탁금지법은 주는 사람과 받는 사람 모두를 규율합니다. 상한선을 넘는 선물인 걸 알면서 받았다면 ' +
    '받는 쪽도 제재 대상이 될 수 있습니다. 상대가 공직자라면 금액 확인을 보내는 쪽에서 미리 해두는 것이 서로에게 안전합니다.'
  ),

  h3('추석 선물, 언제까지 보내야 하나요?'),
  p(
    '연휴 시작 1~2주 전 도착을 목표로 하는 것이 무난합니다. 신선식품은 특히 그렇습니다. ' +
    '연휴 직전에는 배송이 몰리고, 회사도 연휴 동안 자리를 비우는 경우가 많습니다.'
  ),

  h2('관련 가이드'),
  bullet('추석 선물 추천: 부모님·가족 대상 전체 가이드'),
  bullet('설날 선물: 같은 명절이지만 시기가 다릅니다'),
  bullet('10만원 이하 선물만 비교하기'),
  bullet('20만원 이하 선물만 비교하기'),
];

export const products = [
  {
    rank: 1,
    name: '개성상인 녹용 홍삼 스틱 + 쇼핑백',
    price: 27900,
    pros: '청탁금지법 일반 선물 상한(5만원)에 여유 있게 들어가 상대가 공무원인지 몰라도 안전합니다. 쇼핑백 포함, 로켓배송.',
    imageUrl: 'https://ads-partners.coupang.com/image1/UlVtzeoCSqS8VKbqUjmPl5GyjrA8SZkHZu1FWfOjVeKZ7MzwKAsR4W8Ya6g7T8uvJXumB-5lS0HgmTN6gKv9lcuMxe9joItMIFpkSbm4Pb-x48a508CgmfMVKWLzC7HC1yWeg6YZyQDO7aGgZEYqUtRGYjza9KXy9SvZ_b_8WqhtW8KWs5CdcL8U7ni60u8nUZMJKBSnhhdy5O9fgPXHxvmOGTQH7aNr6DL6JpqXFMMk8n7pwtPoWo6-5c_bTxXeYxzOfKMhYHQhJNcvbN-yfsYQrtH-aBp9whQ6a70xWXBGa0zaE1V3Me5nArmXiIkli9xpjFJXaWJ0SSiyDBVSLYWKiikXwXS7tgI9ZdKLOaqdmFO3g_oBHiUkXrORUyBkHXuEMDzSgdfj90JMpYh8qFgYWkN4UT4A7LnnAcCIjJE_JUQqT25mSOpSKKa-2e6ekQKCkrtVOqbP3v8dNXo3MTHr0BrzZvF19_FW2FVvJMyWjvsnj5fLshIGY-w93x3dAy9UsuCNG8jiZQJhqUK5tFowkq0=',
    coupangUrl: 'https://link.coupang.com/a/gIW8WlEkeG',
    naverUrl: null,
  },
  {
    rank: 2,
    name: '수담한과 고급지함 2호 수 2단구성 한과 선물 세트, 1세트, 1.2kg',
    price: 25900,
    pros: '건강기능식품이 아니라 홍삼과 겹치지 않습니다. 한과라는 품목 자체가 격식 있는 명절 인사로 오래 쓰여왔습니다. 로켓배송.',
    imageUrl: 'https://ads-partners.coupang.com/image1/TPCzcK34rUI7iMAWTIk-jq0bjEurcdOBdl8Y5SXQT7wV_HxjfxGgUeRUncw2lh4noa9x_hgLRM1FqoAoZ6xTVPOOqVoq5QKrhJkp3lsuAoa8pKoZhfKrGQQbuhT1-n7n_2ORGfRimUXFgqsmL8UMOHRZ_BhX3-ZdaB_AXORIC-XY_YWL6xFQH6Bqf6LRE1XdSX5cugN7SIDGWnUbzuj9Ry2TaK06RPPuMzwg8tDP-3EbeCfXbRW4WbR94N63mUppm0WhIstX0VlDodgqQYAsTCcVcieCVDV0o0fzXZu-9yLZLMEvOoJaXxn0FENFbNDlpbDuJ4NiVy4ndLQRbvuohCIPR3Vt-s0ZeKIYZSkmxkMxLPik0rJpLarNED3yftrjm5tBLmYGdZv1Gu6dmgdFd0iOO-I-PPlKl3XPsXzwaHBPzbG1rmI1dSJNUGpXSQDJ_pqHeZw0Zw90-FuFmSpeCZkHW2dvrEq075OVp0bZv9prh5lE1yAHXje9vJzWZuc-6oS_FV6_FWqTZNNvFPfNzmfKpZkxxWRg',
    coupangUrl: 'https://link.coupang.com/a/gIXays8Zsy',
    naverUrl: null,
  },
  {
    rank: 3,
    name: '참치선물세트 동원스페셜10호 캔 명절선물 추석 설날 회사직원 선생님 대량 답례품 거래처',
    price: 48550,
    pros: '거래처 대량 답례품 용도로 검증된 구성입니다. 유통기한이 길어 받는 쪽도 부담 없이 보관합니다.',
    imageUrl: 'https://ads-partners.coupang.com/image1/jV6qh2r21GDd08pAjTpXlt29YPPZ2RRT-J3Aq3t9g9Ldwttqc8BFvbCTcPetEGbxR8QDAlbLtUXmk4UKxaAaM_aag8PL_EfCWT-rkKMN9XK0f5C88MAxE-O8MN7m6nW4ZLhWK0XAScznjzVu2BxcKh-cGbxZMbN-CEZx0r1bpIy9r1aPENy_GQurir49FRMXRoIyffopdiUP0bnj1F8Yi1wJg6--8kEa3F9KmF0VbmY45hZZ8AhuHlOlcedILDRCPErps8gkPwKypRNxi0I0HBlT8TzbKHXWqwLNIgPu2f-RdJc2HoQ0YynQ2er-1iUPAMiIEbUniz7nckCjHSKk-nlReEowBAZLVSBzZfEVjPuHive0BjcWqhn3IYYoZIZDrfZaiFi9XnvbJZMlm7VaiULtGvRx-yNN8P8LxdLLsQXCDMMWc7AaBOYKdpzgzIcfHjEzlQhu9jU15W2k9GUrNla9T-rERtQWJJbM0rxn2pyjCwjHvT7PHofcP5dEAtGCH5dDZ2m-vNWTBsuYNzjszkVmPTKG3XN_wCDs_iSyC0XRiGg=',
    coupangUrl: 'https://link.coupang.com/a/gIW8WslAdw',
    naverUrl: null,
  },
  {
    rank: 4,
    name: '추석선물 견과류 선물세트 2호 넛츠 견과 추석 설날 명절 답례품 단체 어르신 거래처 대량주문',
    price: 71460,
    pros: '어르신·거래처 대량주문 용도로 명시된 구성입니다. 보관이 쉽고 호불호가 적습니다.',
    imageUrl: 'https://ads-partners.coupang.com/image1/Rr91ci-sLRlD3ZHLRkoC5OmRxtHLu6KsRbhsqPq5SPJO6_0dzGGg4qJbVIu6P8YvIdSG95zwpn5wBxoHIkxVGw5apYRWgdwRydj7l__lQc-A1LfJ_70cr7NAS_HbZQKBHz9yQt8eyuDLs3AYxkpDh_sxwKuZcd5mnbHXigc887wH40wO30IPzUIOhIAmt3HpDhjJPYTp79UKTbJs2W-ylnbJGRisuUCz44GvuG5klr-qry9Mf80lDozRRGmCQoYc_wf00TwgTfJRtd3OJrv1M_EzoJDelpx-kzS_l3aTK8w3if262eQ0olwLzbVFOn1SaBCHrv9csE_JqAuHEcOJR1Ma3mEUBnBcKSQgEypgRal3CFBVhWzgAr0Efa8JnR2ReuEwE0jLbUFWU7RgoyekqQmzV_O-yTX9Nhybuy_Tc8P04y56tpEtQcLsmWNplB2WYfw52lQomuy5QkH84VFs5FeXYW2c3IoLPRUoeP71KEtRNO_ohtJ538GspzSyz3MqecZqOQ38zYPGq7WhZOGa_O5SksHQvIvf9jHTg3fCdwqV63GM',
    coupangUrl: 'https://link.coupang.com/a/gIW8WyUo0G',
    naverUrl: null,
  },
  {
    rank: 5,
    name: '100% 국산 참굴비 영광 법성포 명품 오가 특대 굴비 세트 10미, 1세트',
    price: 97000,
    pros: '한국 명절에서 격식을 갖춘 선물로 오래 통용돼 온 품목입니다. 냉장 보관이 필요해 수령 날짜 확인이 필요합니다.',
    imageUrl: 'https://ads-partners.coupang.com/image1/1uL94pRheBQEAX-l1jeQMGrDsMnyeQkKOuTuK_Mhkx1nDCVRp01y14nW_7umWJwNvuD0P11nMLPxdHH__9IhW31-ww5epIE9d5dNQjnwo2CJFjHVneZgH4uUATYjwCey1rNQQl2ueAQUi3ZV2jXPg4tq1HJPzi66xYIM6wTg4OmGMvyClJs_g3r4poUmta5I2DVbag4IEfzE7O9KWWakBcsCAGXsu1lO7zvK3lnwrkURsFhZMMzQyDrJjvr2A3sxWYQ5S6v3Ma0vkjN_U-HXaaT6bqOjuQpuO1pQnEDAtRgZPuxt58sorJXU2J13W9wXRGZdbdZkzZWy9YN0WUZ3PVEKAdq84nXsbFS1sfTENw1miGnJVg75RRdWhUPS_r1BQd1zJP_a6J7q8FGZu7pOXDd3yCy7WQs4hSWOh8AcbJuzQiy1XDh9Bbeedo_nLl953vnQkUU3FQAdXznYRRNpojS3_7ntVLAq_Tmd5bfQcAnZKBqKLhY7kWhf8JSGXwCy8_iBjPnPJ6MoICGQ9qS6BnNyH9vr0D_vYw==',
    coupangUrl: 'https://link.coupang.com/a/gIW8WDCc56',
    naverUrl: null,
  },
  {
    rank: 6,
    name: '농협안심한우 1++등급 신선구이 한우 선물 세트 냉장 프리미엄, 1세트',
    price: 208900,
    pros: '공직자 명절 한정 상한(30만원) 이내입니다. 1++ 등급이라 가격만큼의 격식이 분명합니다. 냉장 배송, 수령 날짜 확인 필수.',
    imageUrl: 'https://ads-partners.coupang.com/image1/a8sMwlXn_2wa-JgUa6Db5K6ArVqHOKRmHb4RabEdfGLU_ifFmOapdTXOXtS0ROTldHIjtWJUCK1iAFX49MK3glvvFZpuMYBSR_5el5IznN2lGPr0hf4o3-yBT4luZwC7FX0QDaYLxSmhb6lFvN09N2k0cvtS_oY5Vjw9WUGFxbqgn1ZLE0kj8xH6sjtnhXeYHaYFIqjDaSBvfsXPXAI3wq2owfqwsWAFM-IkYDxIhmVJQUMC4nLYuO-rMCBpmQeutbHMxmmY9cf8x40-RHKTuTkxQW7aGwrUQeQu8Ope9PasvnWUxmjiI2N6i08ylnjI5DOG3MDAW7PJ3MEZizZ67Hpklh7-7QAfwGP8l6NwrUN3pYTLt8NobDAQFBs-s4cVGD8Ue9Flt8TYwCbgJvLFMFrJx2Em5QxhtM5cwWFqbXbxkifuaNia9L8Jq5dP5vLXMkaA0nECBbLr5RX18yD7zXMuSPX3CAW59DSQ2lZzM4uhqyMNK1-HAradvDDYy6EKBo8c9ks8J1e7eRYASJlI3M6N',
    coupangUrl: 'https://link.coupang.com/a/gIW8WH4DvM',
    naverUrl: null,
  },
];
