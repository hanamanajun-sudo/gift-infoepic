import { h2, h3, p, bullet, table } from '../lib.mjs';

export const slug = '1만원이하-선물';
export const title = '1만원 이하 선물 추천 TOP6 — 가격보다 커 보이는 게 먼저입니다';
export const description =
  '1만원 이하 선물 추천 TOP6. 친구·직장동료·선생님께 부담 없이 드릴 수 ' +
  '있는, 가격보다 반응이 큰 선물로 골랐습니다. 전부 1만원 이하입니다.';
export const occasion = ['생일', '스승의날'];
export const relation = ['친구', '직장동료', '선생님'];
export const ageGroup = ['20대', '30대'];
export const budgetTag = ['1만원이하', '3만원이하', '5만원이하'];
export const interests = ['생활', '향기', 'K뷰티'];
export const recipientGender = '공통';
export const priceMin = 1880;
export const priceMax = 9490;

export const intro =
  '1만원 이하 선물은 "가격보다 반응이 커 보이는가"가 관건입니다. 직장 ' +
  '동료 선물 후기를 보면 "가격대비 받을 때 와 하는 맛이 있어야 하는데, ' +
  '나중에 알고 보니 비싼 거였네 하는 제품은 별로"라는 반응이 자주 ' +
  '나옵니다. 반대로 스타벅스 기프티콘을 계속 돌려막다가 다른 방향으로 ' +
  '바꿔서 반응이 좋았다는 후기도 있었습니다. 이 글은 친구·직장동료· ' +
  '선생님께 부담 없이 드릴 수 있으면서, 가격 대비 만족도가 높은 선물로 ' +
  '골랐습니다.';

export const blocks = [
  h2('가격대별로 고르기'),
  table(
    ['예산', '추천', '이럴 때'],
    [
      ['1천원대', '미니 수첩 볼펜 메모지 세트', '선생님·동료께 가볍게 드릴 때'],
      ['6천원대', '호두과자 20개입', '직장 탕비실에서 나눠 먹기 좋을 때'],
      ['6천원대', '바세린 립 테라피', '친구에게 부담 없이 드릴 때'],
      ['8천원대', '투데이넛 2주플랜 견과류', '건강 챙기는 분께 드릴 때'],
      ['9천원대', '씨솔트 벨기에 초콜릿', '무난한 디저트가 필요할 때'],
      ['7천원대', '에인디 미니 디퓨저', '조금 더 격 있는 선물을 원할 때'],
    ]
  ),

  h2('1만원 이하 선물 추천 TOP6'),

  h3('선생님·동료께 가볍게 "미니 수첩 볼펜 메모지 세트"'),
  p(
    '스프링 수첩과 볼펜, 포스트잇이 함께 구성돼 있습니다. 부담 없이 ' +
    '드릴 수 있는 문구 선물입니다. 1,880원.'
  ),

  h3('탕비실에서 나눠 먹기 좋은 "호두과자 20개입"'),
  p(
    '당일생산·무방부제로 만든 호두과자입니다. 팥앙금·누텔라·고구마· ' +
    '앙버터 네 가지 맛이 섞여 있어 여럿이 나눠 먹기 좋습니다. 6,000원.'
  ),

  h3('친구에게 부담 없이 "바세린 립 테라피 컬러 앤 케어"'),
  p(
    '색조와 케어를 함께 챙기는 틴티드 립밤입니다. 가볍게 건네기 좋은 ' +
    '뷰티 아이템입니다. 6,200원.'
  ),

  h3('건강 챙기는 분께 "투데이넛 2주플랜 견과류"'),
  p(
    '소포장 14회분으로 구성돼 있어 매일 챙겨 먹기 좋습니다. 건강을 ' +
    '신경 쓰는 친구·동료에게 어울립니다. 8,390원.'
  ),

  h3('무난한 디저트 "씨솔트 벨기에 초콜릿"'),
  p(
    '카라멜과 씨솔트가 더해진 벨기에 초콜릿입니다. 30개입이라 여럿이 ' +
    '나눠 먹기도 좋습니다. 9,490원.'
  ),

  h3('조금 더 격 있게 "에인디 시그니처 미니 디퓨저"'),
  p(
    '선물 패키지로 포장돼 있어 따로 포장할 필요가 없습니다. 이 ' +
    '가격대에서는 드문 인테리어 소품 카테고리입니다. 7,000원.'
  ),

  h2('가격보다 커 보이는 게 먼저입니다'),
  p(
    '1만원 이하 선물은 예산 자체가 낮다 보니 "성의 없어 보이지 않을까"가 ' +
    '가장 큰 고민입니다. 실제 후기를 보면 답은 명확합니다 — 가격이 ' +
    '아니라 받는 사람이 실제로 쓸 수 있는지, 그리고 "이게 이 가격이라고?" ' +
    '싶은 만족감이 있는지가 관건입니다. 반대로 겉보기엔 그럴듯해도 ' +
    '나중에 알고 보니 저렴했던 티가 나는 선물은 반응이 약했습니다. ' +
    '이 가격대에서는 소모품(과자·초콜릿·립밤)처럼 실패 확률이 낮은 ' +
    '카테고리가 안전하고, 조금 욕심을 낸다면 미니 디퓨저처럼 이 ' +
    '가격대에서는 흔치 않은 카테고리로 차별화하는 것도 방법입니다.'
  ),

  h2('이건 사지 마세요'),
  bullet('스타벅스 기프티콘 반복 — 편하지만 "돌려막기"처럼 느껴질 수 있습니다. 가끔은 실물 선물로 바꿔보세요.'),
  bullet('유통기한이 임박한 식품 — 선물용 식품은 유통기한을 꼭 확인하세요.'),
  bullet('너무 저렴한 티가 나는 포장 — 이 가격대일수록 포장이 인상을 좌우합니다.'),
  bullet('알레르기·다이어트 여부를 모르는 식품류 선물 — 간단히 확인 후 고르세요.'),

  h2('자주 묻는 질문'),
  h3('1만원 이하 선물, 뭐가 제일 무난한가요?'),
  p('과자·초콜릿 같은 소모품이 실패 확률이 가장 낮습니다. 조금 더 특별하게 하고 싶다면 미니 디퓨저 같은 소품도 이 가격대에서는 차별화됩니다.'),
  h3('직장동료·선생님·친구 선물을 다르게 골라야 하나요?'),
  p('문구·차·소모품류는 관계 구분 없이 무난합니다. 다만 친구에게는 립밤 같은 뷰티템이, 선생님·동료에게는 나눠 먹을 수 있는 간식류가 좀 더 안전합니다.'),
  h3('예산을 조금 더 쓸 수 있다면요?'),
  p('3만원 이하, 5만원 이하 선물 가이드에서 더 다양한 선택지를 볼 수 있습니다.'),

  h2('관련 가이드'),
  bullet('3만원 이하 선물만 비교하기'),
  bullet('스승의날 선물 가이드'),
  bullet('직장동료 선물 가이드'),
];

export const products = [
  {
    rank: 1,
    name: '미니 수첩 볼펜 메모지 세트 스프링 포스트잇 노트',
    price: 1880,
    pros: '수첩+볼펜+포스트잇 구성. 선생님·동료께 부담 없이.',
    imageUrl: 'https://ads-partners.coupang.com/image1/eI31IZqT1uKIQ2R8eCMx57B70f6989rpsybYFo6D7SqKFzWXwfcYg1J_ojBa94wDXRNRtiphJ_UWi8iNXsgUvAZuhWYwm2HO_Zl6xvj1-wr_4XcLVmLed7Yl_Cd0UdgKMIzUKJ7b2av7wLX0yw-hV84bo_dlNRTu8u9X6RTWOS4OYHW6tkUIcA_dhbi-07olY5Pz5x9E4nH4pGRvRCdbQQbhY1MPbpI_xVFFp0cWvadkHhCxBEWoN7f6gjkclkuNkXsyeWplkkUp1qX66kG8hX-L6-oEwSrMFlfUjWhpiBDxrbehXS7LM79xhE2xp5DVMWSiylKcFcXtz9ptDgYi_mbQ0qn5ubFNGwYEz60Yg5vBNeylpCxblOuIWwOd4Re_p4W73shMjhlb7cPKElwbk_Q-1QHRfTiJnrRUYlRsS_LvEY6rIKigD5rqq7c6s7KMus8avqZdpFgfSvBbnO0KJ_JQIi4efSSeaXz0njtO_9R7qda4NAWv-Cxgoq3AJiroSOiVl6ds9-_iZVCFAfWyLHCK8gqcGZp1UCQysbGFGNE_nQS_',
    coupangUrl: 'https://link.coupang.com/a/gNXbPjbss0',
    naverUrl: null,
  },
  {
    rank: 2,
    name: '호두가 팥앙금 누텔라 고구마 앙버터 호두과자 20개입',
    price: 6000,
    pros: '당일생산·무방부제. 네 가지 맛 구성으로 여럿이 나눠 먹기 좋음.',
    imageUrl: 'https://ads-partners.coupang.com/image1/Gm_qESrMuqSm6ZDcGiuPyoETQ-A4p4-A4UKWGPgDLduJfqpfsQVHiEAB7n_UzjdxoT1mReX4BEq3PIhVtZNUvVWngZypVIFUfzJypLWCzQMSUORsmX4rfw0BCmqmAnc-gfwPoHWuzFYPNYn5a6sl33h-30U492x1PDewv7QPQaQ0LSFD9IJUPuSIkVFf87meDQvEO3M2huUDn051CDK4k_8emocTqgrnA9l-k2H3M3ulcoA8BofRk0GAKx6OibZJ8TQ7BI8HmkS3J8X0z_6Nd4lgozXBh5qOpCHcYjWMgt6ENcmXom9Xh1Jnt9hcKWY1VnztQZkcEsbuLEGvEpYAny_FZd3rG1ypoy1ny4Yg5eYJWxN7fMGhMRpT9adeYKSL6kHANGYej_RoCI8URp8vId2QCbpM6NVpjh99_We0ZFsII7JnpNtbUxtXujSAsXZtoMEnMpkoNpG1QsDqqWsnZJVSAc3UF7pXfVbcG_j8PGYLRDCv5FExI6HseJtCwC4A-ROp4LKmgfOpbPAMDKGJHMgm39W5KjE=',
    coupangUrl: 'https://link.coupang.com/a/gNXbPn6rPU',
    naverUrl: null,
  },
  {
    rank: 3,
    name: '바세린 립 테라피 컬러 앤 케어, 키씽 레드',
    price: 6200,
    pros: '색조+케어 겸용 틴티드 립밤. 친구에게 가볍게 건네기 좋음.',
    imageUrl: 'https://ads-partners.coupang.com/image1/y_SI_wEuS3myJn4_ywXQiu5PbffhdnFYYw9MMm9RILVD55MIqbesD-Vwm413By6GrhKCXhokPNYu3Qtm_ZyiMKJZ3FgrSUWobPynwlPXnkmh-TvYgvF96YIf_EQQUYaYX6ScGhd6Bb-Hp9i1CoZay3Lj5D8vuYbjUzS-HOZZnD22S2TiAYHOhHrfzCX8XGyB_Onzr8-BAMk2Wrexlgn4YVjJwzD7zRSaJPuInaxJpSRL3x0i-cEpXhfppdWacVB9AE9krDbBubIFa5OOWL-KncFxMCaFC3Tm7dqmJcxzdD3Kjgg0KadSf_C1W_jc9r7MTnTvwQrm49DsdVqfHiCpfRkzhqnpbTFTPNaimRoHamv8mFZwaqbgsiHqEgGg3JH46SV3gwMClk0xye43vw_L2XMoPeux3RfECe4LRvEEQtrG-DrVnPNK6dtWT82UQUx15tAJIA6SIzcJhpvXySTXPoh3IcFIWdgVDiaFRTyU4hI0MFZ9_LIBlthXQdO1wn0sxLaMB5_j3iqH',
    coupangUrl: 'https://link.coupang.com/a/gNXbPvs9Wm',
    naverUrl: null,
  },
  {
    rank: 4,
    name: '투데이넛 2주플랜 클래식 14p',
    price: 8390,
    pros: '소포장 14회분. 건강 챙기는 친구·동료에게 어울림.',
    imageUrl: 'https://ads-partners.coupang.com/image1/bhGhmsUoVt8KBR9nbstFBujM81mMvaBHHwNGQjdRnYNYNZaAErkwbeTTedApghCEg08KVb00bI6YhlDDGXUeAgMnMMk1ysPW93AaSQB2YnenaPcDt81Raj6z5p8-iochkb3k3Ri-82Tv9kP8d5lvZqv0ZGPaYvKlKbVINpvF2HoDclINl9GHd7z-pvAo5lfzrcL_Y5YoTVENUd1FAAGTTyk87D6gHfjGWe-P6rSddXWpvt9rViKcL3MpTqMwS-VqsfAZ0gLCBJbt2rUQ-PmBabFAOdBDXVgzzzFXJpwbgV7nI7OQbNgwQE5duap7OUiXdSJKVwgf0FCZ3cQDUWRdO46MBUOHQO8N9B6MK_lsIKGff2V93S_Kiw26wyvfTEmljErDGBL5o-A1WnZAeQ28pnzNjzm4Tp-IgGRmYPCz3swkBQsnnidr3tRpvJDTJqh52PigE38fAQGPsp-3L9e0ml83TVLuaGsykxy_tYnHYYQYTok2eAF8mOD3nf7STsuM9r7I1d2rnn8=',
    coupangUrl: 'https://link.coupang.com/a/gNXbPAMAw0',
    naverUrl: null,
  },
  {
    rank: 5,
    name: '씨솔트 밀크 초코 위드 카라멜 벨기에 초콜릿, 30개',
    price: 9490,
    pros: '카라멜+씨솔트 벨기에 초콜릿. 30개입으로 나눠 먹기 좋음.',
    imageUrl: 'https://ads-partners.coupang.com/image1/l1Q9w29af7pr_Sr7l3C2FvKH3jQ1dHwDTkFWG-K2djNNTDDPlO4KmkDAa8xNdECxkJ5RKny0zNT0kFU1mgDxqiGaaCHubRnkm4f5WFyT-E-JnCqxN_UYZC6bvduYi4UupCQhWZ7hCNF0_4EqEikACv4pI7Das9bzqBCpPtL5Y6YOcfjufo28epxIBFkqkc8-Zsh50pzPdVjTq5PjXpnwJF3PN0EnRPn9N0N551iUnbS6rc1MRIIW-fSsLoyK_CXaLJ8w-ao_vJ1UPi0ctrpKSPeG2FgqzlzU01o2CXJSQWzoPVXSgJE8uShah7bREuITmH9G4BD7soxPmR0eP6jKFpULQdsYyAza1b3DQ9gnqPAil-i6h0Qy9g_GQONLi4tcF8HH7rmfKYvR_jbGxXle7dV76MvGLlLeGX2yx8qfEuOFMGn279Yfe_LGOZgw9s8ZSWPPyxWQSa2wvTvjRNYxFW_bYVozE1NrYIcjS8O2b0RtRbqh1YT9qSO-50eGfT2Nff28uKbtCPXx6fzj0mLLeTsmWP85kBGBew==',
    coupangUrl: 'https://link.coupang.com/a/gNXcQZzLMq',
    naverUrl: null,
  },
  {
    rank: 6,
    name: '에인디 시그니처 디퓨저 (플라워 미니 디퓨저) 선물패키지',
    price: 7000,
    pros: '선물 패키지 포함. 이 가격대에서 드문 인테리어 소품.',
    imageUrl: 'https://ads-partners.coupang.com/image1/PqNFLrpbMQZ1m5VAPuE_0P-qb2TIo__Kv1fcDatAwDdpbhLWPgc8z8oTTu4WpINVLQ8SWdQ4UuZcKUqaKwfZloGrT3iR5FDXD1yTRPUG27XB08IRc8MQWWoC23KTUf0zqPCIC_NORL9ocIhNtvLODvOpoCZhKZL3sVi2EstL0yFHbH_oB5fRIq6zOvKrCTSYStCQYML4EVP8iEYC_r_yP4GpiHCOe08-3UFi2SzbRlWwou1Sqzgrxuox1DJK9ucEkBiVgC_3hQSpIhBQgEjHmNEbGS6evbwMpSCWbxs2K2M28VMxE26j3Fl_ehv9gnvYq4dKqSsGs85onDpbCKkDWJnFxMyc-Ao7tcKTcq3Z5cdusxWnK3YdxIzi3CSq3_2wzrDm86cWPmvdX5yFUoo6Vqc1l0DXeVVQHfmoxwQtYqoeW8REVXz1AbLkHR0WToyzSfRTnx9J900OfS9ject6Pj_WAPs1M2l6xfp6P2uReH_sxpLN6Bvi-z8WotGfl05PjQ0gTKXrrez0BlcJMCH3zOTyRcFyelAX',
    coupangUrl: 'https://link.coupang.com/a/gNXaZ9pE16',
    naverUrl: null,
  },
];
