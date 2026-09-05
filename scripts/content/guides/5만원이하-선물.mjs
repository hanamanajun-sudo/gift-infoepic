import { h2, h3, p, bullet, table } from '../lib.mjs';

export const slug = '5만원이하-선물';
export const title = '5만원 이하 선물 추천 TOP6 — 이 가격대부터는 미식 선물이 통합니다';
export const description =
  '5만원 이하 선물 추천 TOP6. 찹쌀떡·치즈·사과즙처럼 미식 선물이 유독 ' +
  '반응 좋은 가격대입니다. 친구·연인·직장동료 모두에게 무난한 선물로 ' +
  '골랐습니다.';
export const occasion = ['생일', '크리스마스', '화이트데이'];
export const relation = ['친구', '남자친구', '여자친구', '직장동료'];
export const ageGroup = ['20대', '30대'];
export const budgetTag = ['5만원이하', '3만원이하', '10만원이하'];
export const interests = ['생활', '패션', 'K뷰티'];
export const recipientGender = '공통';
export const priceMin = 19900;
export const priceMax = 39500;

export const intro =
  '5만원대 선물 후기를 보면 3만원대와 확실히 다른 반응이 나옵니다. ' +
  '"찹쌀떡이 이 가격이라니"라면서도 "진짜 고급지고 맛있다", "선물 ' +
  '다운 선물"이라는 반응이 반복됩니다. 3만원대가 미니어처 세트로 ' +
  '고급스러움을 만드는 구간이라면, 5만원대부터는 실제로 맛있는 ' +
  '미식(간식·디저트) 선물이 제값을 하는 구간입니다. 이 글은 그 ' +
  '기준으로 친구·연인·직장동료 모두에게 무난한 선물을 골랐습니다.';

export const blocks = [
  h2('가격대별로 고르기'),
  table(
    ['예산', '추천', '이럴 때'],
    [
      ['1만원대후반', '피터래빗 웨이퍼 틴케이스', '선생님·부모님께 드리는 간식 선물'],
      ['2만원대', '더마쉐어 고체향수 멀티스틱 3개', '가볍게 뷰티 선물을 원할 때'],
      ['2만원대', '서울파머스 NFC 사과주스', '건강한 음료 선물을 원할 때'],
      ['3만원대', '그래인스쿠키 칸타빌레 틴케이스', '디저트 선물을 원할 때'],
      ['3만원대', '치즈 선물세트 LIGHT (와인 안주)', '집들이·홈파티용 선물을 원할 때'],
      ['3만원대후반', '모찌이야기 과일모찌 12구', '"선물다운 선물"을 원할 때'],
    ]
  ),

  h2('5만원 이하 선물 추천 TOP6'),

  h3('선생님·부모님께 "피터래빗 웨이퍼 4종 틴케이스"'),
  p(
    '고급 과자 틴케이스로, 선생님·부모님 선물세트로 명시된 구성입니다. ' +
    '19,900원.'
  ),

  h3('가볍게 뷰티 선물 "더마쉐어 고체향수 멀티스틱 3개"'),
  p(
    '비건 고체향수로, 향수보다 부담 없이 휴대하며 쓸 수 있습니다. ' +
    '22,400원.'
  ),

  h3('건강한 음료 선물 "서울파머스 NFC 국산 사과주스"'),
  p(
    '국산 사과를 착즙한 NFC 주스입니다. 건강을 챙기는 선물로 무난 ' +
    '합니다. 24,290원.'
  ),

  h3('디저트 선물이라면 "그래인스쿠키 칸타빌레 틴케이스"'),
  p(
    '32개입 쿠키에 쇼핑백까지 포함돼 있어 따로 포장할 필요가 없습니다. ' +
    '30,000원.'
  ),

  h3('집들이·홈파티용 "치즈 선물세트 LIGHT (와인 안주)"'),
  p(
    '와인 안주로도 쓸 수 있는 치즈 구성입니다. 집들이·생일·홈파티 ' +
    '선물로 두루 어울립니다. 32,000원.'
  ),

  h3('"선물다운 선물" "모찌이야기 과일모찌 12구"'),
  p(
    '100% 국산 찹쌀로 만든 과일모찌입니다. "이 가격에 이 정도라니"라는 ' +
    '반응이 반복적으로 나오는 카테고리입니다. 39,500원.'
  ),

  h2('이 가격대부터는 미식 선물이 통합니다'),
  p(
    '1만~3만원대에서는 미니어처 세트나 소모품이 안전한 선택이었다면, ' +
    '5만원대부터는 실제로 맛있는 음식 선물이 존재감을 발휘하기 ' +
    '시작합니다. 찹쌀떡·치즈·사과주스 같은 미식 선물 후기에서 ' +
    '"고급지다", "선물다운 선물"이라는 반응이 반복되는 이유입니다. ' +
    '저가형 간식과 달리 이 가격대의 미식 선물은 실제로 맛과 구성에서 ' +
    '차이가 나기 때문에, 받는 사람이 가격을 짐작하기 어려운 만족감을 ' +
    '줍니다. 뷰티·생활용품으로 무난하게 가고 싶다면 고체향수나 ' +
    '쿠키·틴케이스 구성도 여전히 안전한 선택지입니다.'
  ),

  h2('이건 사지 마세요'),
  bullet('유통기한이 짧게 남은 신선식품 — 찹쌀떡·치즈처럼 냉장·냉동 보관이 필요한 식품은 배송·유통기한을 꼭 확인하세요.'),
  bullet('알레르기 여부를 모르는 유제품·견과류 포함 식품 — 치즈·쿠키류는 미리 확인하는 게 안전합니다.'),
  bullet('향에 민감한 사람에게 향이 강한 고체향수 — 무향·저자극 라인이 무난합니다.'),
  bullet('포장 없이 낱개로만 구성된 식품 — 이 가격대는 포장까지가 선물의 일부입니다.'),

  h2('자주 묻는 질문'),
  h3('5만원대 선물, 3만원대와 뭐가 다른가요?'),
  p('3만원대는 미니어처 세트로 고급스러움을 만드는 구간이고, 5만원대부터는 실제로 맛있는 미식 선물이 제값을 하는 구간입니다.'),
  h3('친구·연인·직장동료 선물을 다르게 골라야 하나요?'),
  p('사과주스·치즈·쿠키류는 관계 구분 없이 무난합니다. 연인에게는 고체향수 같은 뷰티 아이템이 좀 더 자연스럽습니다.'),
  h3('예산을 더 쓸 수 있다면요?'),
  p('10만원 이하 선물 가이드에서 더 다양한 선택지를 볼 수 있습니다.'),

  h2('관련 가이드'),
  bullet('3만원 이하 선물만 비교하기'),
  bullet('10만원 이하 선물만 비교하기'),
  bullet('친구 생일선물: 성별을 모른다면 무난함이 먼저입니다'),
];

export const products = [
  {
    rank: 1,
    name: '피터래빗 웨이퍼 4종 틴케이스 고급 과자 선생님 부모님 선물세트',
    price: 19900,
    pros: '틴케이스 구성. "선생님 부모님 선물세트"로 명시됨.',
    imageUrl: 'https://ads-partners.coupang.com/image1/d6xLtYN35q76ZUiEdwlv77iWbA3XDRA5uG1iE_TFmw4MH5Oe09M5Bk70QMp6H-l5-VR57-OU55wESF_-Eb--bjzy3Pn954rq8gI0-AZqmFKby784xlOabkKceTlNrJ4ULbtM4bBNebsx1kz_Xz8oKIxVXNPuGsnLoclS_AJq8Ryl0oVQuDZi7zUdmq-ST31w-_LyiE-yO3V8eJiwqEg9Og6UHCpTHTAWhpGKnxke737CxvrGpMmagbZO2MVHekGCUb7voDi6EZ55xk-12sS5Kpg3m27CaM7P_CTCMss6yh6q2mxht7rd6ba9Xmkkg6m10E9y0z56OkhX-IsbtKVx6FXJ0Mcy02BLnSBVfds-WvTxiCghRV9mJbhllPMtwII4fEniDExf2-RCDX20Xm_u7hEtdOw845E0ZG9P9wxt9guw6oAJXN2JMtVwHzF6K3DN_ZwvbyFFVwDVu9OgexOd_pd3l0eQvwHJwSV__Bg19GpIePbdTY-3FLDfsEHcuSIPj-0OvIH0HA-b-ExzVcsl2iYycYY8HabMiXg=',
    coupangUrl: 'https://link.coupang.com/a/gNXPOWYclE',
    naverUrl: null,
  },
  {
    rank: 2,
    name: '더마쉐어 비건 퍼퓸 밤 카모 브라운 고체향수 멀티스틱 3개',
    price: 22400,
    pros: '비건 고체향수. 향수보다 부담 없이 휴대 가능.',
    imageUrl: 'https://ads-partners.coupang.com/image1/iqsj6-OGnAyuXkb3ipr7nEVG5p_Zc_SQGPeUgmfajan69qCVFmnKpRTDISoHVIF-xvFNTFN4HDkpqFBSLymoqYd9UpO46bT95-mcIS8OrB1CpTommmt2uAVnzaCQQw2flmrXf3q54TjINfHyiu94h0ty6sQrIuJsWGpVPDEMCN5kEwbLN__537fqTi7gxa18Viu8aURImmISzRJq3OrE5UYzupj1Iw3XzuNYHXz5Gy3baXwUexqoFWQz0qDHp85oBCJUcYT4DXWJ9NTD4xS7H7RsJhnwwt7QXRl5CRre4yWfgjIzP53mpgWSRFXQZCsdMdOUow_djYSqeJvkN42VK-n6I9RTeLuDbLGBL2pzWHyEmYVW7rvqu7HBRO40cPf8DCnm8CeXMBDo0Xuze15hjCI2ujEae4ryFmUhaMZOGqNhzRFOkD9A-Liqa1dKwfMuRu2oJhCzATrUcvLxhzNXX7gnE7eqKOSguXu9kPQYAs-jR92XtFOa_rIak8xszoqEP-3TjXuahOMfi3iiZBb8Df0SkhSUjUM=',
    coupangUrl: 'https://link.coupang.com/a/gNXPO2snYG',
    naverUrl: null,
  },
  {
    rank: 3,
    name: '서울파머스 NFC 국산 사과주스',
    price: 24290,
    pros: '국산 사과 착즙 NFC 주스. 건강 챙기는 선물로 무난.',
    imageUrl: 'https://ads-partners.coupang.com/image1/uAaON_0j_5vjUfKsuOfcLF6erquBLKwRaK59juqfdSeFv4hdRBXxDiwqSN3hWZrNRoUwr7nVB-URtfQgsxq-tngisr1m-IukCmpUMl-GYUEagLdfUqigsJJhYbc2tKUnFjUeFkw-owqRSFcNsNKhz14ss_-A-TOK9Mj5FK5CxZzEL_SAl_BmE6y8b5WulqWEheG33Ei4JYqvfddJKpaRuA3rxbEL2ALbYq8sAKZRqOH1u-A4g3_QE3_yI73ZQzXefjDET0kw0M5BSN6tcaX-k2S_7pRSYGp4GQD74VrhOF8UK1gJuH36fZYdyaL7AvUo26ra4CAxjMWjTJWUZirzSlgXtVn0LOTklUKf9AfHk8W-mzYZ-9o1o6t77TKFRXBYzQ8B3FXl_OZ5KdHBmstgqWIFJ6A2u474xt0Jsp9M4dO8sqWhAb9SJ4br2mo3JtvbPR8ADU2lcLakDOC6WquTpCr6M0UJEZGJel-2cYqWw925g9_2CB4VBcmzd2l4B5rBsmzOk82oJNuByNgXgIBYL2FbVw1_T6Z8umOhPK139Dwscb4=',
    coupangUrl: 'https://link.coupang.com/a/gNXPO7PZu0',
    naverUrl: null,
  },
  {
    rank: 4,
    name: '그래인스쿠키 칸타빌레 틴케이스 쿠키 32p + 쇼핑백 세트',
    price: 30000,
    pros: '32개입 쿠키+쇼핑백 포함. 따로 포장 불필요.',
    imageUrl: 'https://ads-partners.coupang.com/image1/G_oVysgq_mCfDzZxG74WWLU-le59j8rMkBks8JRHLuqLwW0E_PzONURzsyQXSuWbr8558DFTJXnOGQiME-yXttx4mC-4eE1iX9NX4kc7ZHQxjZhUeLHpE0u1OyD_FR2wAEs4ieZVviy-jtWtz0aPaRsi7p-mNPB7qZU7vyCYhr1g3Gh4b3TZk6uvV2i1hNQhWAxbGSuErVbxyZKd-m4_q7DgN9uBYqTgen8xATao1U5BG-j4suveX7Tz5gZhsbVcFJ9VcRaXm3Gsu8_p2Fdf6xuuL5uDSK4Z4TvRDrou_AlrjkjX6WmL3fhVug2IshDEa7r7Ml7bVlpA91o3WsyP4SUTZyvYPTuzBXtVz44qKYqsL5DMItq14I_UhMhGH_Y_2xAXNy5gxztXYCrqoAOG1a0VhJkjH3oGhGRWpvtcja4ZDqIPTw8fqtkpxLkfyOEjxzi5VECNFF2sOjv7_RVS_mOdX567W9MXJW0eCAFN2ezSZOReoQ7Tfz9EsweMlrDxXJA13xQRtenPkXOrklJ1_cCI6g==',
    coupangUrl: 'https://link.coupang.com/a/gNXPPcE5nM',
    naverUrl: null,
  },
  {
    rank: 5,
    name: '치즈 선물세트 LIGHT (와인 안주)',
    price: 32000,
    pros: '와인 안주로도 활용. 집들이·홈파티 선물로 무난.',
    imageUrl: 'https://ads-partners.coupang.com/image1/KvpDdW2dS3tcYJ-dKt2-EhJc4KlLMa9D_p4XClzVv8R7NhFD8IZvIXOua5Mwl1Q9s-SxvlgAUN000futok7xiXvm9FWDus2xKR7N2MjTV8OnytcWVhYMFT7nyPRcgajlvszK4ZMn7k19_kzflmcdv4hyngyAA6AEfFbNEBZfW0bTAxSdCsLZOf52OL3gx3yZBJIk9fRmJF2GfttGFSXL-jnsH6rJlqPhMG7zIVrQEHwE7MTShet8QNHSOGIGgEj1HZ5zHo0B7kmAAhiTghbzbSLjvsn7W4uBDO36uY6XbTyIrRWa_Z3HvUof6pSArz8bdqovUdqP2mWOqybSaZ1qpQv_oD8JIykSs14LJrS3NeXmGOTcxIxr2pkV6yr6xSOu9Fait7_8_MU2tDQMzJz_LzdxHufHgT5mvQNeIbahISCrzrMjEHmpWTqyIaHi63IlGnE9Huijw5y7Do3i0aIG50LKeseDMk2EvBP8z7wCeaZW8-LD6HXNhIWgW-6fDtBSfiNiUaJj5XzPcotNl4AVFy1L9ZFFO7Zh9wxwZiRUehb6po8=',
    coupangUrl: 'https://link.coupang.com/a/gNXPPixIey',
    naverUrl: null,
  },
  {
    rank: 6,
    name: '모찌이야기 과일모찌 세트 12구 (100% 국산찹쌀)',
    price: 39500,
    pros: '100% 국산 찹쌀. "이 가격에 이 정도라니" 반응 반복.',
    imageUrl: 'https://ads-partners.coupang.com/image1/QZBDZwpQD2GNNzj7QejZMGCHIgZKyyyf_ccf020KHiRrHRdX1udB0-26XXA-BuFInjnhcAIVC0-i2EHu6V_I8SX1-U4tFHhpaZWBkJ-fOr8d4gx3KqyKoq9It2tZFZ6xf62JLG-fctt65fDFVagn-3vxFLk1lgwfQKfnOBRdbF009jzMhlQhkDWvnUW4GCj-g2afomBpC-Av4urt0BjeWvvOFaVL0OQ4zV-JyBTzOR5v2RYk8fP36EzPBOkUxZTfg_5roQclHWl_P0entRhBMSS7XZQUAZH2TbzQwPE7YsRDi_2_Pyewoj1AB80iIb8uLRdCJidDe63x1gbC_ovtg1z6sMxDiECjug6v4RuD8UHF1WIr1tOvvNmpjHlHRLim_wZiEWWxMU13ceiTpb7mOe2Msurk0XZKrPak7_xehEHMtIzpPB5MHd0ZXPGwhN2BpXct5MmDc0mRh2pePer0_s0-gK_mRb63Tqu-yu-9otDzWgKTvZ4iHK18XS3c9KKvYM_AWMPngrUggg8FvP54LG2sPznSo8JDuA==',
    coupangUrl: 'https://link.coupang.com/a/gNXQT7aBoG',
    naverUrl: null,
  },
];
