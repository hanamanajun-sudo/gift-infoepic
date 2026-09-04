import { h2, h3, p, bullet, table } from '../lib.mjs';

export const slug = '화장품-선물-추천';
export const title = '화장품 선물 추천 TOP6 — 나이대에 따라 완전히 다른 걸 찾습니다';
export const description =
  '화장품 선물 추천 TOP6. 20대에게는 색조·트렌디 더마코스메틱이, 부모님 ' +
  '세대에게는 설화수 같은 헤리티지 브랜드가 통합니다. 핸드크림부터 ' +
  '프리미엄 스킨케어까지 예산별·나이대별로 정리했습니다.';
export const occasion = ['생일'];
export const relation = [];
export const ageGroup = [];
export const budgetTag = ['3만원이하', '5만원이하', '10만원이하', '20만원이하'];
export const interests = ['K뷰티'];
export const recipientGender = '여성';
export const priceMin = 17380;
export const priceMax = 114750;

export const intro =
  '화장품 선물 후기를 찾아보면 나이대별로 반응이 확실히 갈립니다. 20대는 ' +
  '"클렌징폼이 순하다", "색조가 예쁘다" 같은 반응이 많고, 부모님 세대에게는 ' +
  '"설화수 자음생크림 진짜 좋아하시더라" 같은 후기가 훨씬 많이 나옵니다. ' +
  '즉 화장품 선물은 브랜드 하나로 통일하기보다 받는 사람의 나이대와 ' +
  '취향에 맞춰 고르는 게 실패 확률을 낮춥니다. 이 글은 가볍게 건네는 ' +
  '핸드크림부터 색조, 대중적인 스킨케어 세트, 부모님 세대가 좋아하는 ' +
  '프리미엄 브랜드까지 예산별로 정리했습니다.';

export const blocks = [
  h2('가격대별로 고르기'),
  table(
    ['예산', '추천', '이럴 때'],
    [
      ['1만원대', '메디플라워 보니타가든 6종 핸드크림세트', '가볍게 건네는 선물을 원할 때'],
      ['3만원대', '헤라 센슈얼 틴티드 샤인 스틱', '20대·색조 선호하는 사람에게'],
      ['3만원대', 'AHC 블랙 캐비어 유스 리츄얼 케어 5종 세트', '무난한 스킨케어 세트를 원할 때'],
      ['5만원대', '닥터지 레드 블레미쉬 시카 토너+로션 2종 세트', '트러블·민감성 피부에게'],
      ['7만원대', 'AHC 바이탈 골든 콜라겐 유스 토탈 케어 5종 세트', '탄력·안티에이징 케어를 원할 때'],
      ['11만원대', '설화수 자음 2종 세트', '부모님·어른 세대에게'],
    ]
  ),

  h2('화장품 선물 추천 TOP6'),

  h3('가볍게 건네는 "메디플라워 보니타가든 6종 핸드크림세트"'),
  p(
    '쇼핑백까지 포함돼 따로 포장할 필요가 없습니다. 향이 여러 종류라 ' +
    '받는 사람의 취향을 몰라도 무난하게 고를 수 있습니다. 17,380원.'
  ),

  h3('20대에게 잘 통하는 "헤라 센슈얼 틴티드 샤인 스틱"'),
  p(
    '리뷰에서 반복적으로 언급되는 헤라 센슈얼 라인의 틴트형 립 제품 ' +
    '입니다. 촉촉하게 발려 입술이 건조한 계절에도 무난합니다. 31,320원.'
  ),

  h3('대중적인 스킨케어 세트 "AHC 블랙 캐비어 유스 리츄얼 케어 5종"'),
  p(
    '올리브영·면세점에서도 꾸준히 팔리는 스테디셀러 브랜드입니다. ' +
    '토너부터 크림까지 5종이 세트로 구성돼 있어 선물 완결성이 좋습니다. ' +
    '37,500원.'
  ),

  h3('트러블 피부에게 "닥터지 레드 블레미쉬 시카 토너+로션 2종"'),
  p(
    '시카 성분 중심의 진정 케어 라인으로, 피부 타입을 정확히 모를 때 ' +
    '자극이 적어 무난한 선택입니다. 56,000원.'
  ),

  h3('탄력 케어를 원한다면 "AHC 바이탈 골든 콜라겐 유스 토탈 케어 5종"'),
  p(
    '콜라겐 성분 중심으로, 탄력·안티에이징에 관심 있는 30대 이상에게 ' +
    '어울리는 구성입니다. 72,500원.'
  ),

  h3('부모님 세대 프리미엄 "설화수 자음 2종 세트"'),
  p(
    '"부모님께 설화수 사드린다"는 후기가 반복적으로 나올 만큼 명절·생신 ' +
    '선물로 검증된 브랜드입니다. 자음생크림 계열의 한방 스킨케어 2종 ' +
    '세트입니다. 114,750원.'
  ),

  h2('나이대에 따라 완전히 다른 걸 찾습니다'),
  p(
    '화장품 선물 후기를 나이대별로 나눠 보면 패턴이 뚜렷합니다. 20대 ' +
    '수신자에게는 색조 제품이나 트렌디한 더마코스메틱 브랜드 후기가 ' +
    '많고, "클렌징폼이 순하다", "발색이 예쁘다"처럼 즉각적인 만족을 ' +
    '언급합니다. 반면 부모님 세대에게는 설화수처럼 오래 검증된 헤리티지 ' +
    '브랜드 후기가 압도적으로 많고, "아껴서 바닥까지 긁어 쓴다"는 식의 ' +
    '반응이 나옵니다. 받는 사람의 나이대를 먼저 정하고, 그에 맞는 결의 ' +
    '브랜드를 고르는 게 가장 실패 확률이 낮은 접근입니다.'
  ),

  h2('이건 사지 마세요'),
  bullet('피부 타입을 모르는데 고기능성(안티에이징·미백) 제품 — 트러블이 날 수 있습니다. 핸드크림처럼 무난한 것부터 시작하세요.'),
  bullet('향이 강한 제품 — 향에 민감한 사람이 의외로 많습니다.'),
  bullet('마켓플레이스의 초고가 해외 럭셔리 브랜드(라메르·라프레리 등) — 가품 위험이 있고 정가 자체도 매우 높습니다. 국내 프리미엄 라인이 더 안전한 대안입니다.'),
  bullet('유통기한이 임박한 특가 상품 — 화장품은 구매 전 유통기한을 꼭 확인하세요.'),

  h2('자주 묻는 질문'),
  h3('화장품 선물, 나이대별로 뭐가 다른가요?'),
  p('20대는 색조·트렌디 더마코스메틱, 부모님 세대는 설화수 같은 헤리티지 브랜드 반응이 뚜렷하게 좋습니다.'),
  h3('피부 타입을 모르면 뭘 사야 하나요?'),
  p('핸드크림이나 시카 계열처럼 자극이 적은 제품이 무난합니다. 고기능성 제품은 피부에 안 맞을 위험이 있습니다.'),
  h3('부모님께 드릴 화장품은 뭐가 좋나요?'),
  p('설화수처럼 오래 검증된 국내 헤리티지 브랜드가 후기에서 가장 자주 언급됩니다.'),

  h2('관련 가이드'),
  bullet('40대 엄마 생일선물: 후기에 반복된 그 브랜드들'),
  bullet('여자친구 생일선물: 선물보다 편지가 중요한 이유'),
  bullet('20대 여성 생일선물: 친구·동료 기준'),
];

export const products = [
  {
    rank: 1,
    name: '메디플라워 보니타가든 6종 핸드크림세트+쇼핑백',
    price: 17380,
    pros: '쇼핑백 포함으로 따로 포장 불필요. 여러 향 구성으로 취향 몰라도 무난.',
    imageUrl: 'https://ads-partners.coupang.com/image1/gz01EpMbEf5on12lg4v9FittMx3D5j6yFk1rfoep-hfcYd-ZfOGjdwD8lywzcqi5hrWEcin0HcJeqLzkQg7rtO1JyuPW282SR0A7-x0d038famRs-CIlooqtYc4nlvRvlAGJrFCqjcLHg6M2z_JcYCED2agA_1Qd9GwHkgAu-5M6u_jGuAIEcLTeTVXGG1nLZ_h7JpgG-qzal2XME1RK6LtguW4BgH1rPVIRw1P07pCGUOLcNFfUILq84-jk2nXz-E8TiG1XLTyQetD93nJTxOzItLnnkUYJSNHL_0AYnfVbfuxIDqSESHjbasx2DoBOIStrnlBoEhYxhAuBhjsGXssB8aFs4gDKDZ3paY773We-pmpzHbxE64r4f_wA6BS8XGW6wcx2fvZZVWJLjc9dmpwFNesb7DIgvjFY5ayJ4SyO81wK8qjJkbj0Mxik0XPcvs1BxOxOk0iwQkfPNshAruk1H3mWNe7t676QQBMlugOX25-duaYDFIjoUa1ZYai1QzGeKw0uKDV1ajdXUtPFFrM=',
    coupangUrl: 'https://link.coupang.com/a/gMoCnEi3aK',
    naverUrl: null,
  },
  {
    rank: 2,
    name: '헤라 센슈얼 틴티드 샤인 스틱',
    price: 31320,
    pros: '촉촉하게 발리는 틴트형 립 제품. 헤라 센슈얼 라인 리뷰 다수.',
    imageUrl: 'https://ads-partners.coupang.com/image1/Gpg1DHkfpNfJDabnGhuH10NHBMAEJeJ7drEaUzKM5Im1HXqO-hsLdNvLebYCtUS504Sbw4MUyHdtlEQZaVwJdLQ3k-GChMP64iNQHkHBFgxkRRIfJ7O0k7IPfnDsEQsfBdhGqswENhOmPH_0LbAuTGVQYQlsA1b-s-kc8an9USnMSc44WOepp3-5qksMweQ1JSPyRIX07y9UOHDdCeZFV-bZIWq3KrJPy4kjYGZ43s_s49eLJeq9EF2r6DKozBCyOXCpnWHrjGvTeOQcZhwOchdgltiotWjXfQvIpw5BIQLMddYMSkQcH4eP4lSy1FPlfhgsmIAjgeUc9ra5Im-K3utGho2EszG5aF6ewr7jX6rTXR0goETHa9AqFn9Xx1gQtcooftJFc3gw3VYPinNpz3ccXLQbPEcDlX49XQgAB6zgAiCKvcsH4QSa7X1IWxcDxtQQ5DDTzVkg8LqWEFIpgJ2PgCYxSmhiNQwrM_vtvdtPspRgJNgasDgIhfKvc8Vhh_ZUgDg6uSybx0Fv-19Naz4Urw==',
    coupangUrl: 'https://link.coupang.com/a/gMoCnJgtQO',
    naverUrl: null,
  },
  {
    rank: 3,
    name: 'AHC 블랙 캐비어 유스 리츄얼 케어 5종 세트',
    price: 37500,
    pros: '올리브영·면세점 스테디셀러. 토너~크림 5종 구성으로 선물 완결성 좋음.',
    imageUrl: 'https://ads-partners.coupang.com/image1/C8RZxyW5KOAWc4yiC6q2F5UZcknrEzzi_SARWIVN_D5UFy305ugg6UXKxFkMz2lv_G2yoOoTV5EzD2zGLavi6bXTLQ2KAaXihe5bgyTiR6enkchalyrkRN2aR-AmBNGoBUCOWL-I2R7B7OewmPqznkvo1OP1RUg0ZnulTCyfPavKEiYLAoJY1IGxjruWCbj92SpuIv59km3-fArMNyJLbNvnPHlYdzt1_PysH3fiEeUmiRj92P79tDyY0VlDcjnKiA8-esKBk9anQy2dpIFe9B_FXqXX66px-SZevR7JGldrUn8ekW5giZ43WdpmcMavjGNztT-x5OpMBo7bstHXsYu15uF2CqlgVGEiHOkzkLPH7nxzrUT0XSgsRhhXSm7qvl3LNqpeMEFzbgGJBTDwZWwc1MkcOhcsfVlYkjltIQa8ZbrLqLE6tu-x3aRhbWiJbhBch9hMTNOOSA3ES6f5UaOLhqecy3SYjUi4CFy7MzoFImAIegmVzpIuiXpYKAvWJUP1N8Nvxg==',
    coupangUrl: 'https://link.coupang.com/a/gMoCnN5Koe',
    naverUrl: null,
  },
  {
    rank: 4,
    name: '닥터지 레드 블레미쉬 시카 토너 200ml + 로션 150ml 2종 세트',
    price: 56000,
    pros: '시카 성분 진정 케어. 자극 적어 피부 타입 몰라도 무난한 선택.',
    imageUrl: 'https://ads-partners.coupang.com/image1/6M4l_FBJ7YwxvgJc6A6sLXFkmhXa62kf5Hpsa91Dhd3oV45-dTrPshwdE3fsHWlgNdhnm52aZX2PVvcgTge7_MfKvE1iMJz0LqjU1TPn2tBQt0Rz9ZJnsQyXsm-b9BmYsNBvJBCNLpOpM7n24wjZzA_YsDGK0TOLYFRGAjzJuGP_7aTQooIKa4nB85FCzKJJzDIRI8IXJMTrUbtg-ORmvbNYDSTBn5laD3kw_Dupp4YTRb0aZVpfQT8UPUoVKsBOKoLWh95nJjXvh3IzonNR5JlcNXsaIZJq6VsmAfpFcWLK4e7MsXReLE-4X9mTUk2MWDumOD-Fx-gVQhzlDgDoeSHn08sc8L_tGbyF-gjzkbMavBXzfEd2sWvgr_WaB5Yw8w25pGktXFIA31UNtw2-Ei1ejI4_MlDSqscPJZAoCBjM6fLGCTNjOAIBnv_Fd0wRh1NltNikBLp_c5KYN_koXTSrBh5fo6IzWzXM3K8TTCB_KOKc-_l04Qvkavye52UOHoCbY4WiuQ==',
    coupangUrl: 'https://link.coupang.com/a/gMoCnTenOm',
    naverUrl: null,
  },
  {
    rank: 5,
    name: 'AHC 바이탈 골든 콜라겐 유스 토탈 케어 5종 세트',
    price: 72500,
    pros: '콜라겐 성분 중심 탄력 케어. 30대 이상 안티에이징 관심층에 적합.',
    imageUrl: 'https://ads-partners.coupang.com/image1/8IYSUxubIMGlY-c78JQU0M3apC9vCDWz3lg9iXRT3wPMgtfdpKdcrUPS-tU2z3nUNqgBaQQwhq2SWcoJiCSDnWWnbqAyXHvt8XiSmLDwBrUPU7NvSQEVahsDb5lt1TrXOCJk2p_gFK-WmyikTzWau4Y-OpEHYTAnUAJGRMZ6AOaoHo3F25VcE-m3XF3SJA4lDqsmCz3GU8_bQl7RVtdIpSthT1FSFk4sSAcrH4OtGKfhEWALoRM8V1Y9SL4Kqi6Q4Jy4lZvb1zS9dec4kv8WUhuUqZdW1UhAIHbGBd8qBM5QLaH8WPdTF_ZffPlzqHKbp-Nl_WKhEDdEPMBV7-Raf2cju9UxdfnUUJS9lLgh-KZJ7YnQm9NpVLbzmgyofIv2hCSIPVhZdUgepKxjd8xqjUnaDb3zjakB74hMFZBt-51QuAs5sQz2nx2cZjN_nemiLCT9sDZwGDp-Ag6DVBBTfGHF_AW2tYK0lnb-StuyAygA81stdg0gkM6MUYTBtKdzQe_m79lEiQ==',
    coupangUrl: 'https://link.coupang.com/a/gMoCnYszpk',
    naverUrl: null,
  },
  {
    rank: 6,
    name: '설화수 자음 2종 세트',
    price: 114750,
    pros: '부모님·어른 세대 선물로 반복 검증된 헤리티지 한방 스킨케어 세트.',
    imageUrl: 'https://ads-partners.coupang.com/image1/iDQBLsdjv15rgQa9iN4Cpkm84NSqmqeG-coBycBMsplLjkun-3VKC1CfGGcB9uDa1aYwWg4QXwIsNi_6nyEBKDf_n9s2c9Mor2vj0RZYfRAoawWz_nvlHaSMmk3FZU33B2v2mVHWX3w7z6RHRFME41SPab6qHxJfuWbc8oxjb5HbJuqmMQ1_35VlQ-690X8rSI73Eaoh6hJHHmXVNeRFGjWhSwjbd_OGm3fmLr_nLl007QRpG5xUfd5bUsWFV3k-vnyE3mCkUftWj_MfVHuWp3HnLupTsi4VAHABvKwSSkAJ6sdJ_gVxPJO5Xa8rtYQw0DjQc0_538XqSj0uAoTVT2dev9FWO6AE9NP9KK9IAoL58uo2EzI1b35CHsbsPND6ehXf4Gk78CnY-oSOx8hM4N8oovvctkS4A8BO7e3dvLJ2_iea8FPJNEkMmnI2cJSQiCmcSrZy1tonak1NwhrnVPmzqKPLF-Zks9QUSvJh0UUCdLxqQl-hctXYz4zOMQYHnDabZjwl21wYyFp1qsP7sII=',
    coupangUrl: 'https://link.coupang.com/a/gMoCn4yoBE',
    naverUrl: null,
  },
];
