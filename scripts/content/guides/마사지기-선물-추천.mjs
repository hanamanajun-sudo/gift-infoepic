import { h2, h3, p, bullet, table } from '../lib.mjs';

export const slug = '마사지기-선물-추천';
export const title = '마사지기 선물 고르는 법 — 안마의자 대신 이 정도가 부담 없습니다';
export const description =
  '마사지기 선물 고르는 법. 목·어깨·다리·손·두피 중 어디가 안 좋으신지에 ' +
  '따라 골라야 할 기기가 완전히 다릅니다. 안마의자는 부담스러운 예산대에서 ' +
  '실제로 쓸 만한 부위별 마사지기를 정리했습니다.';
export const occasion = ['생일', '어버이날'];
export const relation = ['엄마', '아빠', '부모님', '할머니', '할아버지'];
export const ageGroup = ['40대', '50대'];
export const budgetTag = ['3만원이하', '5만원이하', '10만원이하'];
export const interests = ['건강'];
export const recipientGender = '공통';
export const priceMin = 27900;
export const priceMax = 89900;

export const intro =
  '마사지기 선물을 검색하면 안마의자·안마매트처럼 300만원대 제품부터 ' +
  '나옵니다. 실제 후기를 보면 안마의자가 "선물로 들여놓으려고 일주일을 ' +
  '싸웠지만 결국 가장 사랑받는 선물이 됐다"는 이야기도 있을 만큼 만족도는 ' +
  '높습니다. 다만 그 정도 예산을 쓰기 어렵다면, 부위별로 나온 소형 ' +
  '마사지기 중에서 골라도 충분히 좋은 선물이 됩니다. 이 글은 목·어깨· ' +
  '다리·손·두피 중 어디가 불편하신지에 따라 다른 기기를 추천하고, 종아리 ' +
  '마사지기처럼 잘못 쓰면 오히려 안 좋은 경우도 함께 정리했습니다.';

export const blocks = [
  h2('부위부터 정하세요'),
  p(
    '마사지기는 부위마다 구조가 다릅니다. 목·어깨는 두드리는 방식이 ' +
    '많고, 다리는 공기압으로 조이는 방식, 손은 손가락 마디까지 눌러주는 ' +
    '방식, 두피는 괄사나 지압 방식이 일반적입니다. 평소 "여기가 뻐근하다"고 ' +
    '자주 말씀하시는 부위를 먼저 떠올려 보세요.'
  ),

  h2('가격대별로 고르기'),
  table(
    ['예산', '추천', '이럴 때'],
    [
      ['2만원대', 'Rotima 목 어깨 마사지기', '목·어깨가 자주 뻐근하실 때'],
      ['2만원대', '한일의료기 거북손 종아리 마사지기', '다리 피로가 심하실 때'],
      ['3만원대', '릴렉스조이 미니미 손 마사지기', '손목·손가락이 안 좋으실 때'],
      ['3만원대', '모두이룸 세라믹 두피괄사', '두피·측두근 마사지를 원하실 때'],
      ['8만원대', 'METAVIZ 흡입식 바디 마사지기', '두드리는 방식이 안 맞으실 때'],
    ]
  ),

  h2('마사지기 선물 고르는 법 TOP5'),

  h3('목·어깨가 뻐근하시다면 "Rotima 목 어깨 마사지기"'),
  p(
    '무선·온열 기능이 있는 선물용 안마기입니다. 저소음이라 거실에서 ' +
    '써도 부담이 적습니다. 27,900원.'
  ),

  h3('다리 피로가 심하시다면 "한일의료기 거북손 종아리 마사지기"'),
  p(
    '공기압으로 조이는 방식이며 강도·온도 조절이 됩니다. 다만 사용법을 ' +
    '지켜야 하는 카테고리입니다 — 아래 "이렇게 쓰면 안 좋습니다" 참고. ' +
    '29,000원.'
  ),

  h3('손목·손가락이 안 좋으시다면 "릴렉스조이 미니미 손 마사지기"'),
  p(
    '손 전체를 감싸는 무선·온열 방식입니다. 뜨개질·설거지 등으로 손을 ' +
    '많이 쓰시는 분께 어울립니다. 35,900원.'
  ),

  h3('두피가 뻐근하시다면 "모두이룸 세라믹 두피괄사"'),
  p(
    '두피와 측두근을 함께 마사지하는 세라믹 소재 괄사입니다. 전자식이 ' +
    '아니라 어디서든 손쉽게 쓸 수 있습니다. 37,800원.'
  ),

  h3('두드리는 방식이 안 맞으시다면 "METAVIZ 흡입식 바디 마사지기"'),
  p(
    '두드리는 방식 대신 흡입으로 뭉친 부위를 풀어주는 방식입니다. ' +
    '두드리는 마사지기가 시원하지 않다고 느끼셨던 분께 대안이 됩니다. ' +
    '89,900원.'
  ),

  h2('안마의자 대신 이 정도가 부담 없습니다'),
  p(
    '안마의자·안마매트는 실제로 선물 만족도가 높은 카테고리입니다. ' +
    '다만 300만원대부터 시작하는 가격, 거실을 차지하는 크기, 렌탈이냐 ' +
    '일시불이냐를 정해야 하는 번거로움까지 감안하면 선뜻 결정하기 ' +
    '어렵습니다. 이 글에서 다루는 부위별 소형 마사지기는 그 정도 감동은 ' +
    '아니지만, 3만~9만원대로 실제 불편한 부위를 짚어서 드릴 수 있다는 ' +
    '점에서 훨씬 부담 없는 선택지입니다. 예산에 여유가 있고 거실에 ' +
    '둘 공간이 있다면 안마의자도 고려할 만하지만, 그렇지 않다면 이 ' +
    '가격대에서 부위를 좁혀 고르는 쪽이 실패 확률이 낮습니다.'
  ),

  h2('종아리 마사지기, 이렇게 쓰면 오히려 안 좋습니다'),
  p(
    '종아리·허벅지처럼 공기압으로 조이는 마사지기는 압박 강도를 세게 ' +
    '쓰면 오히려 붓기나 통증이 심해질 수 있다는 우려가 실제로 자주 ' +
    '제기됩니다. 강한 압박이 근육을 풀어주기보다 자극을 줄 수 있기 ' +
    '때문입니다. 정맥류가 있거나 다리가 잘 붓는 분이라면 약한 강도로 ' +
    '짧게 쓰는 게 안전하고, 평소 다리 쪽에 지병이 있으시다면 선물하기 ' +
    '전에 병원에서 사용 가능 여부를 확인해 보시길 권합니다. 목·어깨· ' +
    '손 마사지기는 상대적으로 이런 우려가 적은 편입니다.'
  ),

  h2('이건 사지 마세요'),
  bullet('SNS 광고에서 자주 보이는 제품만 보고 결제 — 광고 노출이 많다고 실제 후기가 좋은 건 아닙니다. 장기 사용 후기를 따로 확인하세요.'),
  bullet('A/S 정책을 확인하지 않은 저가 제품 — 마사지기는 고장이 잦은 전자기기입니다. 구매 전 A/S 기간과 방법을 확인하세요.'),
  bullet('부위를 정하지 않고 "전신 마사지기"부터 구매 — 실제로 불편한 부위 하나에 확실한 기기가 만족도가 더 높습니다.'),
  bullet('정맥류·순환기 질환이 있는 분께 강한 압박형 다리 마사지기 — 미리 사용 가능 여부를 확인하세요.'),

  h2('자주 묻는 질문'),
  h3('마사지기 선물, 어떻게 골라야 하나요?'),
  p('평소 "여기가 뻐근하다"고 자주 말씀하시는 부위부터 확인하세요. 부위를 좁혀서 고르는 게 만족도가 높습니다.'),
  h3('안마의자를 선물하고 싶은데 예산이 부담스럽다면요?'),
  p('이 글에서 다루는 3만~9만원대 부위별 마사지기가 대안이 됩니다. 안마의자만큼은 아니어도 실제로 불편한 부위를 짚어드릴 수 있습니다.'),
  h3('다리 마사지기는 정말 위험한가요?'),
  p('평소 다리가 잘 붓거나 정맥류가 있는 분이라면 강한 압박을 피하고 약한 강도로 짧게 쓰는 게 안전합니다. 걱정되면 병원에서 먼저 확인해 보세요.'),

  h2('관련 가이드'),
  bullet('50대 부모님 생일선물: 절대 자기 돈으로는 안 사는 것들'),
  bullet('할아버지 생일선물: "효도의 완성은 돈"이라지만'),
  bullet('40대 엄마 생일선물: 후기에 반복된 그 브랜드들'),
];

export const products = [
  {
    rank: 1,
    name: 'Rotima 목 어깨 마사지기 무선 온열 강력 저소음 선물용 안마기',
    price: 27900,
    pros: '무선·온열·저소음. "선물용"으로 명시된 목어깨 마사지기.',
    imageUrl: 'https://ads-partners.coupang.com/image1/lC9jGPhODZ8ZmeEflMffmQ_ErdG3dGSkYJq54suOdmYE9mxZzVc_w8JkOoZBpSe5T5j07weLsF8nZTnkp3dtp-ANMiXsI3BI7d16iGIhraisDhwA1Tt28wSLkEuwCOFfTwitERW56J60FyjgY3qsJaT1zRADLbv5vCEgrb84injymK-xe5CBerj41OteUWrwsOCmNtSu1ruqRzn6GX6B5PGaF5cD_wL5GR-W3JV1ICOLBnUBzq-jXrNmnFyqHXu0ExyR-fu_SNMWjlu7auj_uayyHZw6vrlwAt2HgWXGZVZFH-JSSPhjPHv6qmUgTe3o_Nl0LcAsny9kg9tfAlGI0dTEdIdHI0tu6Bt6aoQo8EiPGmQAbtOR0ORVnEbN--r1qXviqZi4XKYC7uuKPAoMVnZkmI0_7cEc_x4qJAlr0JqzPRQGAU5H2ahbLjaaghJbmmiI2eEdDZSMbSi0n2kT_r-OjGthFuEqUVSZt1yUwCwocDCwOHanmr70GQHPp4FeyIFUYtEbEAVyYs3WMw-Lvnva1-F36pnt_YpxCe5rBS-GWw==',
    coupangUrl: 'https://link.coupang.com/a/gND0fFGaQe',
    naverUrl: null,
  },
  {
    rank: 2,
    name: '한일의료기 거북손 공기압 온열 종아리 마사지기',
    price: 29000,
    pros: '강도·온도 조절 가능. 의료기 브랜드. 사용법 준수가 중요한 카테고리.',
    imageUrl: 'https://ads-partners.coupang.com/image1/stB_8g0XTg1YJSmqspvrPEVzMTQzL4O5fhMLnM5GsFrfSPYPYKF9t38jEZ2coeuIdjOn02NyN2fiVyQ8ZfsAari758N57SGFHnCKVeqLX0Sc3znq86ciTNJl6DnSpUc6l_EUTUi0ly4clJn4txrWK6yngApOraPqByRtdiwFlnHL-Ml8oyG-bhM55GJwal1BazXP4v5jZt0h6ixrvkjcguqYDsA1wf7J4WB8RTw8LDkBJZXZkEwTskR-pXPUI8Sj_Sw6R10UQ0mS-bD3tzx7cFZjp2Lfp33L_Bp0kxbdy8GKJ60LV0ykvWTaFxlsaWxzwoRVpMJtfVZMsU9PNO1azcTOw_jy-GfF1apicwVBDS8zMr2bCCfuHoMDHnx563Lu_5RXZe48K3vWZEexS0ydqRvtfkr2Lnsmu2C8n1YGE_6CLumVsWAb_dB-u_Rb27tmjb3oGtmb30-dEaWAdCY6mSnIC9XhmZrRC410bNKlBPuohNzPTo07ET82dcCGWRBrwwpJXxON0YzzsEYUL7b4wH2HsMOdMdYv',
    coupangUrl: 'https://link.coupang.com/a/gND0fKWeAe',
    naverUrl: null,
  },
  {
    rank: 3,
    name: '릴렉스조이 미니미 무선 온열 손 마사지기',
    price: 35900,
    pros: '손 전체 감싸는 무선·온열 방식. 손을 많이 쓰는 분께 적합.',
    imageUrl: 'https://ads-partners.coupang.com/image1/FBCrUMYYq51n7UzxFEEavZ7XLo0VFL-M3NfKFaTjudcMWpLsCqiqGd5TFqdFeP6L03ryv-2oDdni4jWnTRRPh3z9hIERD1_Zedkscl6fEb5Hc4ivb5wJNqLKRmTLbfTEO4VKIbqLroN3yyjVy783FuVmUKALfywoPInSBBf9xR9VWsXl7Mxi-qaOcZVNTExw-t2ehfnnmeRI4BZfW6qQygPM3qnJJYKETkHgigpfcVd-vkU5ldDWuJczOAgGvMKzB8qkG92Q4P0b4Wxh4gKr5PVZrfi7RqTkb_HLAs4FEFWIsIs1V1gd7JRxNxbAFWp1yjA48UQJCJdV81FwGvhCOXPLi5RbJzdK5QAIDYTMPy-sjWb0KH96m_R8qVP-n7ekjRt4DpRdpJ9ARz8w-tL3rDv5XQQIJAmPy43_GTJcRff97i37G3lFeuu_u9HumIrbjpWXQt-X8zrMhhENi0LmxMSM0Ww3s-Q3vSkq6_tFvffDuPoCcL1G2tMyPz1pKPHOa1PMG7ecv-gNJ6tpU1C3wLqyYLjo_vQiRgI3IK2sjWq3CA==',
    coupangUrl: 'https://link.coupang.com/a/gND0fPKnRs',
    naverUrl: null,
  },
  {
    rank: 4,
    name: '모두이룸 두피괄사 측두근 바디괄사 프리미엄 세라믹괄사',
    price: 37800,
    pros: '두피+측두근 동시 마사지. 세라믹 소재, 전자식 아니라 어디서든 사용.',
    imageUrl: 'https://ads-partners.coupang.com/image1/KbM0dWGYqrxwz0c0KcrUShAzufXZvm1cp4dB9jOfyMowvGsLsvrXPBCyA259GKgxBT4Ncot_LKeY6ZHszIPByDtjrHFnGKXEVNK1_VyiEfzHTwYbC-jJzaNgNK2VumS61jwfmEp0y31v1SR2_iu_teIpPnZb0Nli5XTMFZCi6BV3cWBxTFRcAvt0hFVBpSqSxxpprNkgOoO1CPR940K_jyNl_rzzFzBtlNrK8TaIYaexDExdGMniVsdIlfNj3D3Qek3EF8CxxqJrNcHcYH3y3lcb375090-v3NBnyrx_fpKiYrcHTHRxjZ5pF-GELGSs3F4DpitlwpDMpoWph9WvK1Fv9f3hIb5FeP9CDJw6ijhBiAaMTOnRtktN60zS3HXbvakqnBpDlXYHyPZ2JshFzjCMHACpBCh1x1TEXa4_zD2s57xp1IKiBchEITkWC9o7iGFTBpcavdi--b2AHt9zEY4AieqSTrhKnNaFoGBlJ9Fg9WFhBSCGBcdxGS0p0UUfIDPvHUEnHLNmAoZn0v7rpE3r3FhkxnQ=',
    coupangUrl: 'https://link.coupang.com/a/gND0fU8QE0',
    naverUrl: null,
  },
  {
    rank: 5,
    name: 'METAVIZ 진동 흡입 EMS 바디 마사지기',
    price: 89900,
    pros: '두드리는 방식이 아닌 흡입 방식. 근막·뭉친 부위 집중 관리.',
    imageUrl: 'https://ads-partners.coupang.com/image1/DVpJiY_m7BXcEfiHDfOwTOIs7FAj6d1BQItEW735dbdk1aajZPm_bZk3dhV-V3ub-mAmNYmkYuWnqQPUg4iahe8OL7lyVwF7ZjQo4q93KlflARA2OCu2YIVS3Ay9ldCu7Thj48XjN6d3DZv69B6_JcAmnYhAadublHYwy-rqrVBXqm8fpU7aPlW4t2BjVUkNIyCJOsxEirLimUJgjRF0Ga78L-QtCojvqVPQ4JwMzogJnEKYA6IKbHvi9avw5JwofuSSMIYQnO8XOLyUwSONAfc1f8RLYC9GNZqRPjqm3cwi4JO2NUxsB9DZ3xw1Kuh8T64SZ3oOqbWwdkGiKMJtno_6Ldj1U5EIElglv4mTPj2UmrKnn0AXWM9F6_1aNTEF7H-tsfHiSPYyAKwPujryn_12tCNMjMKqPg4S7HXrzXOGMkQ173316gN6c7g0DQaNX5i3A5C9OuxjG3UdXd7eHeRuzQnmcEgwqquaC0ed4CQHvIjyPKRH_LjjFxT67sHkfs4SlMKxPWfe5iDSKPoctLj5R08ACr0=',
    coupangUrl: 'https://link.coupang.com/a/gND0f0oTkW',
    naverUrl: null,
  },
];
