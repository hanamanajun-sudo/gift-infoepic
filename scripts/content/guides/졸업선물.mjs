import { h2, h3, p, bullet, table } from '../lib.mjs';

export const slug = '졸업선물';
export const title = '졸업선물 추천 TOP6 — 학년이 낮을수록 기념품, 높을수록 실용템입니다';
export const description =
  '졸업선물 추천 TOP6. 초등·중학생에게는 각인펜·LED 꽃다발 같은 기념품이, ' +
  '고등학생·대학생에게는 만년필·시계처럼 어른으로 대접받는 실용템이 더 ' +
  '잘 통합니다. 학년별·예산별로 정리했습니다.';
export const occasion = ['졸업'];
export const relation = ['딸', '아들', '조카'];
export const ageGroup = ['초등학생', '중학생', '고등학생', '20대'];
export const budgetTag = ['3만원이하', '5만원이하', '10만원이하'];
export const interests = ['생활', '테크', '패션'];
export const recipientGender = '공통';
export const priceMin = 16900;
export const priceMax = 76050;

export const intro =
  '졸업선물은 학년에 따라 기대하는 게 완전히 다릅니다. 초등·중학생 ' +
  '졸업식에는 각인펜이나 LED 꽃다발처럼 그 순간을 기념하는 선물이 ' +
  '어울리고, 고등학교·대학교 졸업처럼 성인 진입이 걸린 시점에는 시계나 ' +
  '만년필처럼 "이제 어른"이라는 의미가 담긴 실용템이 더 잘 통합니다. ' +
  '이 글은 그 기준으로 학년별·예산별 선물을 정리했습니다.';

export const blocks = [
  h2('가격대별로 고르기'),
  table(
    ['예산', '추천', '이럴 때'],
    [
      ['1만원대', '몽크로스 각인볼펜', '가볍게 기념품을 남기고 싶을 때'],
      ['1만원대', 'LED 장미꽃 영구보존 꽃다발', '졸업식장에서 바로 건넬 선물을 원할 때'],
      ['2만원대', '디지우드 아크릴 이름각인 무드등', '오래 남는 기념품을 원할 때'],
      ['3만원대', '파카 조터 CT 만년필 세트', '대학·취업 앞둔 사람에게 어울리는 선물'],
      ['6만원대', 'IOWODO W40 스마트워치', '실용적인 테크 선물을 원할 때'],
      ['7만원대', '로이드 엘메이트 남성 메탈 시계', '"이제 어른"이라는 의미를 담고 싶을 때'],
    ]
  ),

  h2('졸업선물 추천 TOP6'),

  h3('가볍게 기념품 "몽크로스 각인볼펜"'),
  p(
    '이름이나 문구를 새길 수 있는 고급 볼펜입니다. 초등·중학교 졸업 ' +
    '선물로 부담 없이 고르기 좋습니다. 16,900원.'
  ),

  h3('졸업식장 정석 "LED 장미꽃 영구보존 꽃다발"'),
  p(
    '기프트박스와 카드가 포함돼 있어 졸업식장에서 바로 건네기 좋습니다. ' +
    '시들지 않는 프리저브드 소재입니다. 17,900원.'
  ),

  h3('오래 남는 선물 "디지우드 아크릴 이름각인 무드등"'),
  p(
    '이름이나 문구를 새길 수 있는 주문제작 무드등입니다. 졸업 후에도 ' +
    '방에 두고 볼 수 있는 기념품입니다. 24,800원.'
  ),

  h3('어른 대접 "파카 조터 CT 만년필 세트"'),
  p(
    '국제적으로 검증된 만년필 브랜드입니다. 대학 입학이나 취업을 앞둔 ' +
    '고등·대학 졸업생에게 "이제 어른"이라는 의미를 담아 건네기 좋습니다. ' +
    '39,600원.'
  ),

  h3('실용적인 테크 선물 "IOWODO W40 스마트워치"'),
  p(
    'IP68 방수에 올웨이즈온 디스플레이를 지원합니다. 대학 졸업·취업 ' +
    '준비생에게 실용적인 선물입니다. 69,060원.'
  ),

  h3('격을 더하는 "로이드 엘메이트 남성 메탈 시계"'),
  p(
    '깔끔한 메탈 케이스 디자인으로, 고등학교·대학교 졸업처럼 성인 ' +
    '진입을 축하하는 선물로 어울립니다. 76,050원.'
  ),

  h2('학년이 낮을수록 기념품, 높을수록 실용템입니다'),
  p(
    '졸업선물은 학년에 따라 기대하는 게 다릅니다. 초등학교·중학교 ' +
    '졸업은 그 시절을 기념하는 의미가 크기 때문에 각인펜·LED 꽃다발· ' +
    '무드등처럼 "그날을 기억하는" 선물이 잘 통합니다. 반면 고등학교· ' +
    '대학교 졸업은 곧 성인·사회 진입을 의미하기 때문에 만년필·시계· ' +
    '스마트워치처럼 앞으로도 쓸 수 있는 실용템이 더 잘 통합니다. 받는 ' +
    '사람의 졸업이 "한 시절의 마무리"인지 "새로운 시작"인지를 먼저 ' +
    '생각해 보고 고르세요.'
  ),

  h2('이건 사지 마세요'),
  bullet('학사모 상자 같은 포장 소품만 — 포장은 선물이 아닙니다. 안에 담을 실제 선물을 먼저 정하세요.'),
  bullet('너무 유아틱한 캐릭터 상품 — 고등학생·대학생에게는 부담스러울 수 있습니다.'),
  bullet('시계·만년필처럼 격식 있는 선물을 사이즈·필기감 확인 없이 구매 — 특히 시계는 손목 사이즈를 미리 확인하세요.'),
  bullet('졸업식 당일 급하게 준비 — 각인·주문제작 상품은 제작 기간이 필요합니다. 미리 준비하세요.'),

  h2('자주 묻는 질문'),
  h3('졸업선물, 학년별로 어떻게 다른가요?'),
  p('초등·중학교는 각인펜·꽃다발·무드등 같은 기념품이, 고등학교·대학교는 만년필·시계처럼 어른 대접하는 실용템이 더 잘 통합니다.'),
  h3('예산은 얼마가 적당한가요?'),
  p('1만원대부터 7만원대까지 다양합니다. 조카·친척이라면 가벼운 기념품, 자녀라면 조금 더 예산을 두는 경우가 많습니다.'),
  h3('각인·주문제작 상품은 언제까지 주문해야 하나요?'),
  p('제작 기간이 있으므로 졸업식 최소 1-2주 전에는 주문하는 걸 권합니다.'),

  h2('관련 가이드'),
  bullet('입학선물: 초등학생과 중학생은 완전히 다른 게 필요합니다'),
  bullet('취직축하 선물 가이드'),
  bullet('20만원 이하 선물: 내가 사긴 아깝고 받으면 제일 좋은 것들'),
];

export const products = [
  {
    rank: 1,
    name: '몽크로스 각인볼펜 선물용 고급 볼펜',
    price: 16900,
    pros: '이름·문구 각인 가능. 초등·중학교 졸업선물로 부담 없음.',
    imageUrl: 'https://ads-partners.coupang.com/image1/MfqycpGHX4NhLG5HMaRkn3hJsyZBM1-e1mlCARRzHy7Nu7IB2J2crf7y3lgvtmQdSixMvz4oz9P5KvWsS_K4L78sKiPVi8FjHAYvdMTic5E7psq3Tnq_CgKEHcSPx0sQw2TOxc8zR3vrzMHCfya650kMZkYcu7csyJysGqTTtCWLW30iri7gB_Ta1kp82RMGm4cNvpsdqmyhwjJ03VXaCSTVWVTa465h7RT4fZXmSBURcDkWZCiomtRpXoP9fV55doyx1ZcH62UAWUylP-4BUiG1iU_YLHGn-A9dlppfVETBSx3TDa1OUmive2TnEasYlvlwL_f5UM7EJad9mONAFKe3yMbdNqbK85vZThC9_XiacItRCcN0sXlpf1ZiGyhp3RpUzCLxVg-YfPSj3RqvN_VsiYuELPU9sbfnqGy-DmdRRQ8JcuF4A2500u9Dirg_QHUllr2jwgqrJYYJb6dGGUVkW0CZtHGSdOaRgG6y3zU3QqIzb234tq4Jz4ws4HTM5P1go8UzdGwUP86T7n7WgTLZmegCeKE=',
    coupangUrl: 'https://link.coupang.com/a/gMAkvcmSBM',
    naverUrl: null,
  },
  {
    rank: 2,
    name: 'LED 장미꽃 18송이 영구보존 꽃다발 선물세트 기프트박스',
    price: 17900,
    pros: '기프트박스+카드 포함. 시들지 않는 프리저브드 소재.',
    imageUrl: 'https://ads-partners.coupang.com/image1/VIQYT2XA6lgnH5SZVEjA2RtZHznJtrbNWfitubTcCVHmtBnkYnVzwRh-9ql1frnNAWM1C_X45Sdvm2gdtQT0XRWgeMw_JTsL4eqQBuosW7yzx_T5yTwmtxbNqiiVRI68EzsPb8EMv1giDiBKs6wTy7UGFN60hYizjDRqhW0DYVeHcx5szBXO18m2cZGVNJRAH39hLfBN5mpioz-hot2XnPqLoysU3DS_G5EQNBJGwjXyYGchIq0aTorMKwRFSKfBS8BOmAYFGTuVHcjfneVditcu8Bxtg5kx_sI9BGZgbg9eGLlz6w66Xgv40XGoxk6OdVw_xc3QncctQrWinEuaTY1nUpVR73vWcN51Fei0OxnobuzfSkNRCIUQwdpd_2iRuWcPZKIoZEt8frUzKUbdk9CV76mwVROcI-CPCDkjpvfdgoUeB2z8-ELIb__pIThvBDr8s9uy0wWVg12rfup78i7Uuzbgzm3C8fRl-_u7Kae8AGOZ6SiTVXuUyk1G7qaefLdtGsbL9KYvF0kgPODjIcK1-tUMTfuABpSM2n_EBTJJFds=',
    coupangUrl: 'https://link.coupang.com/a/gMAkvib8BU',
    naverUrl: null,
  },
  {
    rank: 3,
    name: '[디지우드] 주문제작 "커스텀문구" 아크릴 달 LED무드등, 이름각인',
    price: 24800,
    pros: '주문제작 이름각인. 졸업 후에도 방에 두고 볼 수 있는 기념품.',
    imageUrl: 'https://ads-partners.coupang.com/image1/bdmTemOo9bThG3jbbd0PZOBYfWzfB7OfqCHCTAJ9ud0VUhpa2mbJQ4lEb6pgLqpXtQlnq9qwGQUe_LnDPNm9Dwr3-KtL_UU3Jh_E1JiryF7Fva7sf_Jt7dfc99G2d3k0PoO414CTnNss1mLgUjQuZFBcWdQQlYz5y9ppBSV0K9wozNZvr3yfDpt1dsno5UR5z878woG29AqIV61IfTpgf9NAMsjQDNAXsUKLtDJD7mgHx61uMW36up9QWq8evDiaj2s_WV4yfQnO4TVj92SiGh2gA-ZDOOT8U_jsxDVWsRufWrZ-J23ykAbEAGATh0t_XHp2nCHIjujMAqGDW1qRgpbXn0Q5BJ4BCktNtpP7Qi75fVe_sT5ljg5sj7FzUqfIEDrL-FnzxQLDBSaHF4hvFtk768H3Hlv3xDRkXJnwmprrKH6UC92WMqF2MLL-ywneS7olkQ-CgZ_Um_8x6G3mpifIk6xxFM81Fym-x23slptzvrnyUXuQvROrZSkJWPdHIJu7NdOxFXu7TP8In-jGY95Ua79AoXFlcU6lfw6UOp7n',
    coupangUrl: 'https://link.coupang.com/a/gMAkvnzt9g',
    naverUrl: null,
  },
  {
    rank: 4,
    name: '파카 조터 CT 만년필 + 카트리지 기프트세트',
    price: 39600,
    pros: '국제적으로 검증된 만년필 브랜드. 대학·취업 앞둔 졸업생에게 어울림.',
    imageUrl: 'https://ads-partners.coupang.com/image1/mfWlF_f59BGe7RS1mXBXuz4QFJSJSz400D7hw9B1e2Khvo64CtLLjtXavBRuBiqDDN6etpYbHvKArr9C98Dt5rrYKtpd1AYAweOgmIPHBf4S080P6Ngxt0caEbQFFmqezGSJWkLmtQz0J2T3inUXjvNWao4UA879jgtyEg3RkV-gZM02sE066Jeg_xnEVnG9iNI8a4Y4VW_1uwSitozH3WUFq26ah8sk74KPuT0IkkPO_QjYV0KYJVvPtEFycyKk8AaJuOcdpU6zDFzXrdHG5LiOZOtzpTEpbpS3XmkrkcXQVQuJ6WfftSwfCqsaK-lnrIbzU0y18dSGAaaNhkynmidmIn1kx-skVFsoCUmmdwX-VxbFmjWdWOc7jj7gZZGyaXzRrV70uE_kcbRCewTqRRTYkC7jyYl4uq8CYy7adAkRaZVbOlDbA0M3I6d6QrifpvFMiDJqqUR1litqKKsKIKJ2QxMaTGvIx7ETymvQbxhZBu8lzWaI1Efj8gJLJXFTg4cvErj3s6-2pd8K3ukoECuVoniu0Fh8QWGZy3xZXfAK-A==',
    coupangUrl: 'https://link.coupang.com/a/gMAkvtfx4S',
    naverUrl: null,
  },
  {
    rank: 5,
    name: 'IOWODO W40 스마트워치',
    price: 69060,
    pros: 'IP68 방수, 올웨이즈온 디스플레이. 취업·대학 준비생에게 실용적.',
    imageUrl: 'https://ads-partners.coupang.com/image1/11D3bFI6VFwscYsU1-4bb3fKUSQVErU9YBYzonMWBGPW1Z6EqolO7BJAp8JiWuIxmvA2lKoTKAgLcVEaheM4LUlkXHNrbonPuZ9Hv5qmPGEhTzPPW_vKZ4VFft_rmw75H4DY6a5kgiN7XISz535OOAWsxebYxL1QTV9LKluNPw3mGwoZ4DfAA02RyMZw04ZHJ06_gf_G00CeslIvixWT7PCp3pRhC2Ws7PG9IvcH8zgqlFN_-lO5-tkX3IuTsMBYRzS7Dlq9WzjTYMCTT4VfqTcYyHaH5GWujsmYfT7Gw9v0ZIkvjfCY7x0FqJYeMCTXXd8STXwwJLg9VVYVXJ_Ki3pXKLBHbUuWzkjE4S7QP2vePNGpKCG3TMNd-K5hLwUyUCnpggHbvVp2cgbjTlSWbhHk8trKDD2AjYbluF354a5RS1F1nXC4VD9j0nnnMe6jt9Bzf2qnb7HUEIKkGZmFI3eJjD04UCGu1HAfGuAokMfXDIsPmi1mXGxkfmViBI0fAJ1lDGNId8cU_ExrLuNs8NbqQArraIZX',
    coupangUrl: 'https://link.coupang.com/a/gMAkvxncey',
    naverUrl: null,
  },
  {
    rank: 6,
    name: '로이드 엘메이트 블랙 실버 남성 메탈 시계',
    price: 76050,
    pros: '깔끔한 메탈 케이스. 고등·대학 졸업처럼 성인 진입을 축하하는 선물.',
    imageUrl: 'https://ads-partners.coupang.com/image1/5kpGn57FJ7Ibx-1L5pbEockG5QqtdHMWTQ10hiy_t1zkW9Hozy1Gf2nU-QCMUHds4IEHWkOOvTowIr3KYUUTeK3v4RA_lh2FL6jVICm4SIJVT-PYi0haOf7BCwFI1K2Lc9G4Dca9YVbr-WA1DtJ18B1ow12S_pBsvzFbwVqsDxM5lrstW4tmzV20jjI7H1G4pNYUV5RBrAJeVDgiADyTCEs4y5qJTuXrUOFSbrMCRIMf9vlSOQRx0PIaevkBaZyX-kEWkjwFkwfZHKSSuZk_6zPlmgASlkrSQtGunp1Gzh9u2pOe-2JTL2Xkndua_P237S-WybW6so-ddQfS_DUifPtHm_b0EqWwnr5Wn225LIsTHIFkeRy-rOJEShWT0QqcGfMJWvz63H2jwlpCdKClgeF0v15UDBwKiEcQ5NULAUyhKmMW8DBBEiPyiyBj8F-4n7Z3mXuArTo44qsNnQhO3JdejNFcUphISe3Ov9YaTxYtghVk5vVFh_J2yvv8TPnbvO6EJz_PU4zeJz3C871LCSlWoDcatLX4EYVTXB_rRhYcbA==',
    coupangUrl: 'https://link.coupang.com/a/gMAkvDt3mK',
    naverUrl: null,
  },
];
