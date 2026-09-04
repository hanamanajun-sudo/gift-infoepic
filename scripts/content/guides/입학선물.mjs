import { h2, h3, p, bullet, table } from '../lib.mjs';

export const slug = '입학선물';
export const title = '입학선물 추천 TOP6 — 초등학생과 중학생은 완전히 다른 게 필요합니다';
export const description =
  '입학선물 추천 TOP6. 초등학생에게는 필통·독서대 같은 실용템이, ' +
  '중학생에게는 운동화처럼 자기 표현이 강한 아이템이 더 잘 통합니다. ' +
  '학년별·예산별로 정리했습니다.';
export const occasion = ['입학'];
export const relation = ['딸', '아들', '조카'];
export const ageGroup = ['초등학생', '중학생', '7세', '13세'];
export const budgetTag = ['3만원이하', '5만원이하', '10만원이하', '20만원이하'];
export const interests = ['도서', '문구', '생활', '패션'];
export const recipientGender = '공통';
export const priceMin = 10900;
export const priceMax = 129000;

export const intro =
  '입학선물 후기를 초등학생과 중학생으로 나눠 보면 원하는 게 완전히 ' +
  '다릅니다. 초등학생, 특히 저학년에게는 필통·독서대·연필깎이처럼 매일 ' +
  '쓰는 실용템이 반응이 좋고, 중학생에게는 운동화나 가방처럼 취향과 ' +
  '자기 표현이 담긴 아이템이 더 잘 통합니다. 이 글은 그 기준으로 ' +
  '학년별·예산별 선물을 정리했습니다.';

export const blocks = [
  h2('가격대별로 고르기'),
  table(
    ['예산', '추천', '이럴 때'],
    [
      ['1만원대', 'BDYP 대용량 필통', '가볍게 학용품 선물을 원할 때'],
      ['2만원대', '슈펜키즈 슈베어 베이직 백팩', '가방을 새로 마련해야 할 때'],
      ['2만원대', '아크릴팩토리 투명 독서대', '책상 위 실용템을 원할 때'],
      ['3만원대', '카시오 방수 어린이 손목시계', '시간 관리 습관을 들이고 싶을 때'],
      ['3만원대', '프로살림 오토베어 자동 연필깎이', '문구 실용템 중 가장 반응 좋은 아이템'],
      ['12만원대', '나이키 에어포스 1\'07 운동화', '중학생에게 취향을 존중한 선물을 원할 때'],
    ]
  ),

  h2('입학선물 추천 TOP6'),

  h3('가볍게 챙기는 "BDYP 대용량 필통"'),
  p(
    '패브릭 소재로 가볍고 수납이 넉넉합니다. 저학년 입학선물로 부담 ' +
    '없이 고르기 좋습니다. 10,900원.'
  ),

  h3('새 학기 필수템 "슈펜키즈 슈베어 베이직 백팩"'),
  p(
    '슈펜 키즈 라인의 기본형 책가방입니다. 무난한 디자인이라 학년 ' +
    '구분 없이 쓸 수 있습니다. 23,570원.'
  ),

  h3('책상 위 실용템 "아크릴팩토리 투명 독서대"'),
  p(
    '높이·각도 조절이 되는 아크릴 독서대입니다. 학습 습관을 잡아주는 ' +
    '실용적인 입학선물로 후기에서 자주 언급됩니다. 29,500원.'
  ),

  h3('시간 관리 습관 "카시오 방수 어린이 손목시계"'),
  p(
    '방수 기능이 있는 디지털 시계로, 등하교·학원 시간 관리를 스스로 ' +
    '익히기 시작하는 시기에 어울립니다. 33,900원.'
  ),

  h3('문구 실용템 1위 "프로살림 오토베어 자동 연필깎이"'),
  p(
    '심 굵기 조절이 되는 자동 연필깎이입니다. 입학선물 후기에서 ' +
    '반복적으로 언급되는 실용템입니다. 36,890원.'
  ),

  h3('중학생에게 취향 존중 "나이키 에어포스 1\'07 운동화"'),
  p(
    '중학교 입학선물로 자주 언급되는 스테디셀러 스니커즈입니다. ' +
    '사이즈를 미리 확인하고 구매하세요. 129,000원.'
  ),

  h2('초등학생과 중학생은 완전히 다른 게 필요합니다'),
  p(
    '입학선물 후기를 학년별로 나눠 보면 뚜렷한 차이가 보입니다. ' +
    '초등학생, 특히 저학년에게는 필통·독서대·연필깎이 같은 문구 ' +
    '실용템이 "매일 쓴다"는 이유로 반응이 좋습니다. 반면 중학생에게는 ' +
    '실용성보다 취향이 우선입니다. 이 시기엔 브랜드나 디자인에 대한 ' +
    '자기 기준이 생기기 시작하기 때문에, 운동화나 가방처럼 스스로 ' +
    '고르고 싶어 하는 카테고리를 선물하면 만족도가 높습니다. 받는 ' +
    '아이의 학년을 먼저 확인하고, 그에 맞는 결의 선물을 고르는 게 ' +
    '중요합니다.'
  ),

  h2('이건 사지 마세요'),
  bullet('사이즈를 모르는 신발·가방 — 미리 사이즈를 확인하지 않으면 반품 부담이 큽니다.'),
  bullet('이미 학교 준비물 목록에 있는 학용품과 겹치는 구매 — 학교에서 지정한 준비물을 먼저 확인하세요.'),
  bullet('중학생에게 너무 유아틱한 디자인 — 캐릭터가 강한 제품은 저학년까지만 무난합니다.'),
  bullet('인증 없는 저가 전자시계 — 방수·내구성이 확인되지 않은 제품은 금방 고장 날 수 있습니다.'),

  h2('자주 묻는 질문'),
  h3('입학선물, 학년별로 어떻게 다른가요?'),
  p('저학년은 필통·독서대·연필깎이 같은 실용템이, 중학생은 운동화·가방처럼 취향이 반영된 아이템이 더 잘 통합니다.'),
  h3('예산은 얼마가 적당한가요?'),
  p('1만원대부터 12만원대까지 다양합니다. 조카·친척이라면 가벼운 실용템, 자녀라면 조금 더 예산을 두는 경우가 많습니다.'),
  h3('아이 취향을 모르면 뭘 사야 하나요?'),
  p('필통·독서대·연필깎이처럼 취향을 크게 타지 않는 실용템이 무난합니다.'),

  h2('관련 가이드'),
  bullet('7-9세 남자아이 생일선물 가이드'),
  bullet('7-9세 여자아이 생일선물 가이드'),
  bullet('중학생 남자 생일선물: 가방을 "꾸미는" 나이입니다'),
];

export const products = [
  {
    rank: 1,
    name: 'BDYP 가벼운 대용량 필통 패브릭 펜 파우치',
    price: 10900,
    pros: '패브릭 소재로 가볍고 수납 넉넉. 저학년 입학선물로 부담 없음.',
    imageUrl: 'https://ads-partners.coupang.com/image1/9_KY6KAIJHpNKfbz99kaE4KhjPBkj9cdTQ4_YHJ61vl7n5bfi5tdhgdIEay1nKMa67D_Nlj5DVIP2abJr7gGMQgmoCa-bmvakCq_pkC-ZoE4YW4cY3E2lmnAxSIjb8dDAxRXBgEJBhpVx5_k6283h3Lp7SDKYzNtkqWnsv2Tk9mjoNiGuRHYwgk9UKv2AG0X7KuK_sYDz3_OqcBsRpCiJ9vcnMY97uCUAlK5Oa87IVxQ2rNN0tRrWer_jI8AqVTXRLM59PZ0QxhQqLZUvIp5fnKMK-FKxmQpb2SgZS7RO9qIAhuQglRj4YSnzr-fAmvkZaextePpFzccY2BQ8QJXnSfTP1757I3t8io3glyYpwao-J2y6u55r1GJuANlLqYiwEv4-FP284Pz8OGFdJRIeyCOeljB6UxhXhP5m1OZoSeRLuHrWlCUTK7Yz1slLcaLpaBOV_PxLKSq2ZME9Hv7oaIu5jIScCXzGbiCW0IuFzdzprPVsW2uQOPdSPaUHwiERLs2o66O-c1-oJsmlZKhB9uwxAapyTU=',
    coupangUrl: 'https://link.coupang.com/a/gMzSOOE91M',
    naverUrl: null,
  },
  {
    rank: 2,
    name: '슈펜키즈 슈베어 베이직 백팩',
    price: 23570,
    pros: '슈펜 키즈 라인 기본형 책가방. 학년 구분 없이 무난한 디자인.',
    imageUrl: 'https://ads-partners.coupang.com/image1/FTJDGKJdvYqqjUNcFdWCtExSwW5dcDFvbOlbyUmCuAIZ5KKkTTwwg8MLS5faTIXCQdWodcQsWOUUzqucMWWQC6hH8khndcijOGGW3U9-B1H4tu8YLRvA63v4IDkya8aiu2hSa1F2TTSJe2AIAbGpodE_UWd-okIOkcGxjmwTBRSviC-msMNRo0BoARI2LdGI4eq3O5alDK9a_ZH8tZbA88joOYTMkTkV_qxPYyxOTLU_q7DoYWUs9aPsR8CsIHAo0Y9Gt5o9lrrxli29PtcWJnUe6sMwMmbp1NQg3f2Y-35MxL_ZAHnQBi2vhXdSZzKP2x5mblq_hcHH-N1QsyttanqqlgOr33Qzp3cPAjchQKab8COtIbksTClgZzao13pPV3pMkaKhQNibRB6S_BKbDCOmuzKD5Oesaj5zrWzv6YVwvbveU1olAzN9lS6xubotrvb939s1qdqrTRSEKL6i71YonbtcH2K8WGys2D0Puz9HYItgIM3NN-BXVAVE16Ie_bTYim_2mHfv0zuQfth8HnoBjg==',
    coupangUrl: 'https://link.coupang.com/a/gMzSOT3CPl',
    naverUrl: null,
  },
  {
    rank: 3,
    name: '아크릴팩토리 아크릴 독서대 필기대 책거치대 책받침대 북스탠드',
    price: 29500,
    pros: '높이·각도 조절 가능. 학습 습관 형성에 도움되는 실용 선물.',
    imageUrl: 'https://ads-partners.coupang.com/image1/YpsipoCT-nElqIieYpjAz4GAWXLutpjbzK8FoypPVJvNjczGLyZacdqlnJFB5EuRakU2iK5YbbsWn2vRZz4GrXlqdkeaGEWqXSszWtTIUELpl4YutM3wXL2JqoqR7yuzF-cGrfiLCab5xR_2SFa_B0-HL5SCZ0pxXjZJpcRu7bIXqYG1kQ8sT0vdRJbQ-GEV8Ha-v32GaN2Jz3Q9320Gkv5sN96q1JynqtYWaiUDZeOpnw0hiayjoNMnkcEkaFYfar6PTaxmbal9kLCfuw5bHo94YoLvh-s9plfORSiBXiRcT7rhwGGI3Pg9xQQRpn4YUDJuYEH99MfXf6UA1GRsh1aVzu15W3u0Pb-A20Fx5LxMZH_ACiV5DdoLUuKC1fcVZGTAskJwWO-QgNilt0v2ma2XbRdVEZJDrWuRAuw-C0ADyN9cKSjG-kSFyXoDjbKqKJL31hRpsC2IvubO8nC4a9XvnEVsBr2V4AnfvEXR2yhSARhusUO4ruoSe3aTE8sv1PwRqtWdkhuugwHiAvoIoOf0X2Aapr0=',
    coupangUrl: 'https://link.coupang.com/a/gMzSOZjFvg',
    naverUrl: null,
  },
  {
    rank: 4,
    name: '카시오 디지털 전자 방수 초등학생 어린이 우레탄 손목시계',
    price: 33900,
    pros: '방수 디지털 시계. 등하교·학원 시간 관리 습관 형성에 어울림.',
    imageUrl: 'https://ads-partners.coupang.com/image1/oRr-fW50xIxid5yUoebxumEUicex6itPSRej5xSSg_2EiRUxAFCsSA_X485QPKvBzfjGzgMPUEhRb8tz-TZVt57VoLPj3klm95YhKuxePpV-3e3eeFqybJ8Be0saoGlyxNDNpKM3PpfmJCWtHLj6nkwQAhXK3rX5GkiF6yGj82GlaKRbAXF0MezyTif5uU_SApoG1wxkeFIAdfooIUETv7zjpVzoZaLY4wW9aiY9vUcGo1eRbL5g2tEsbjjit-xWd3lRbx615AaiHGZU6RB2JzXZLDn5iKb0zX8Y6EYSZfXQ2zP46NZOd-17QBAQd9qM9Dvsk97iZNNYCu7orUiHelx-qipFrTjU_IiIPPzmF15njyfh9ZWMIJTPQKL60MVdSx860lDJgayNGQ-KZ7xTrPQkmb0zWd0kLN9W-w2qUENjMAkMCq8IjxzT-k3_5wERC91SHkWoEeKIW9_lYwCwP8QZGC0eiHoFKngjStESXxVR-0uGtFjpi1-mg24chlIEfZbJmOfCI9GRIQwo5j4wt8mFewiKYk0=',
    coupangUrl: 'https://link.coupang.com/a/gMzSO47Tzw',
    naverUrl: null,
  },
  {
    rank: 5,
    name: '프로살림 오토베어 자동 연필깎이',
    price: 36890,
    pros: '심 굵기 조절 가능. 입학선물 후기에 반복적으로 언급되는 실용템.',
    imageUrl: 'https://ads-partners.coupang.com/image1/60D3-VKyHF_bcleq6yyKvRH4OvxWnPgf1dWLOfmWHHs2L1uoP5UY1uFEDU6lHhNQsKQC4Jcs5ZvfGe-6De4Yl3sZBpXqP5UGHjhzqQuLvHazWNN1SW6qtOuAngT6HHY_wrbhy3KTJ0XoiK-h9cqYDmMonbrrG764wofUbt0AEGecIB1sfEDpIzgALsRasJAeFiN-4pEKKEgmlSuo2WwgBD9ojmQcYYcPIwVsltGXmYMaNJ5w6dTfA-2O_bngWwLUEhC55siyfsxyCDBJFYCg9imD69iZR32kn60vm01Tw0D73rdAUbczHKEiMElzDG-S6vDMHQPxJG0dzCxl3dt6Nv0LE1G8nuxDrLwU-YTvx-b2s6iCyMwX_3CSv7OirZ_URa-skXBXSlIBI3nAIkpB1Bnx3C5pfJ_1jHA4UjU-Vdv0u1VeCqfp5pBdEcJDzHX6gX3YimGDcVLBZX8i6mk71bFNN-00AXOBspu_BEKL8UHYDU9Vuq5oHgMF_uXef3YXxzdakKGNqJF6qlb5WWvGa8zLd2Y29lFmZl-NTyCDWf0nIA==',
    coupangUrl: 'https://link.coupang.com/a/gMzSPaeLe0',
    naverUrl: null,
  },
  {
    rank: 6,
    name: '나이키 남성용 에어포스 1\'07 운동화',
    price: 129000,
    pros: '중학교 입학선물로 자주 언급되는 스테디셀러 스니커즈.',
    imageUrl: 'https://ads-partners.coupang.com/image1/eYr7M4Fde1PeD4iseetjFYxrVNIUIw8sedusVctfsRtA5Zoyqxns7jD4Mql3tflshFHB8HGDrxdqI-TApo6drW6FtLPm4AqbsHSzEMJuvtqRHt_E3jd0-Qhe85tpj-pgjVtmzp8i1Z4KcSkbvCxDc43mMxuB39jYrUmyuQ5bI-cp5rUx4hpPWPxxsxD0jyqe7a8D89ZM7PE5DIrpqgEILbEb77u1RUUb_7pMhsnQcSeV21GW-bWhPOue-TLMmJm9Xo5DeX7iA57-f3c0d6saEegoxuBAAF_XKYLiszaMt1dM_9YS42tmjRFUKxOqKnU40GbXI35hAQM-8jzuY5d_03rlP5i6KDlgiB_fYtO2vBeG90-36umx4MVdORuy_sXawTPlnkFD4cu-v1qkwNGfiWHLAqio5lv9qFV7jbBAILJsdE5CjuoOt0wHY1AxT4P7OENJXFiggNNC39XzZDxwyg9ek97iLvLLTRbUkyyUgbbwoEL2WSeL3L2mcTIh-bffhUCooirem7kQaTU_vxLmBS0Z',
    coupangUrl: 'https://link.coupang.com/a/gMzSPeVBEO',
    naverUrl: null,
  },
];
