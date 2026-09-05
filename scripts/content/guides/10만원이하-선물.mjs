import { h2, h3, p, bullet, table } from '../lib.mjs';

export const slug = '10만원이하-선물';
export const title = '10만원 이하 선물 추천 TOP6 — "스몰럭셔리"라는 말에 속지 마세요';
export const description =
  '10만원 이하 선물 추천 TOP6. "10만원대 명품"이라는 콘텐츠 중에는 실제로 ' +
  '17만~19만원대인 경우가 많습니다. 이 글은 실제로 10만원 이하인 상품만 ' +
  '골랐습니다.';
export const occasion = ['생일', '어버이날', '크리스마스'];
export const relation = ['친구', '엄마', '아빠', '남자친구', '여자친구'];
export const ageGroup = ['20대', '30대', '40대'];
export const budgetTag = ['10만원이하', '20만원이하'];
export const interests = ['생활', '건강', '테크'];
export const recipientGender = '공통';
export const priceMin = 11970;
export const priceMax = 66700;

export const intro =
  '"10만원대 스몰럭셔리 선물"이라는 콘텐츠를 찾아보면 막상 "19만원짜리를 ' +
  '10만원대라고 하지 말자", "톰포드가 10만원대? 10ml짜리잖아요", "5만원 ' +
  '넘어가면 더 이상 스몰이 아니다" 같은 반박 댓글이 자주 달립니다. 가격을 ' +
  '실제보다 낮춰 부르는 경우가 많다는 뜻입니다. 이 글은 그런 함정 없이, ' +
  '실제로 10만원 이하인 상품만 골랐습니다.';

export const blocks = [
  h2('가격대별로 고르기'),
  table(
    ['예산', '추천', '이럴 때'],
    [
      ['1만원대', '뭉클 니치향수 미니어처 3종', '여러 향을 한 번에 선물하고 싶을 때'],
      ['1만원대', '로즐린 아로마틱 핸드워시 2개', '바디케어 선물을 원할 때'],
      ['2만원대', 'LG 프리미엄 퍼퓸컬렉션', '생활용품 선물을 원할 때'],
      ['2만원대', '헤트라스 프리미엄 대용량 디퓨저 3개', '인테리어 향 소품을 원할 때'],
      ['4만원대', '프리미엄 위스키 스톤 세트', '홈바 취미가 있는 분께'],
      ['6만원대', '블라우풍트 노이즈캔슬링 이어폰', '실용적인 테크 선물을 원할 때'],
    ]
  ),

  h2('10만원 이하 선물 추천 TOP6'),

  h3('여러 향을 한 번에 "뭉클 니치향수 미니어처 3종"'),
  p(
    '5ml 미니어처 3개 구성으로, 니치 향수를 부담 없이 접해볼 수 ' +
    '있습니다. 11,970원.'
  ),

  h3('바디케어 선물 "로즐린 아로마틱 핸드워시 히노키 2개"'),
  p(
    '히노키 향의 아로마틱 핸드워시 2개 구성입니다. 19,900원.'
  ),

  h3('생활용품 선물 "LG 프리미엄 퍼퓸컬렉션 샴푸바디 세트"'),
  p(
    '샴푸·바디워시가 함께 구성된 프리미엄 라인입니다. 25,230원.'
  ),

  h3('인테리어 향 소품 "헤트라스 프리미엄 대용량 디퓨저 3개"'),
  p(
    '500ml 대용량 디퓨저 3개 구성으로 오래 쓸 수 있습니다. 25,800원.'
  ),

  h3('홈바 취미가 있다면 "프리미엄 위스키 스톤 트위스트 세트"'),
  p(
    '녹지 않는 위스키 스톤 세트입니다. 홈바를 즐기는 분께 어울립니다. ' +
    '47,700원.'
  ),

  h3('실용적인 테크 선물 "블라우풍트 노이즈캔슬링 오픈형 이어폰"'),
  p(
    '오픈형 귀걸이형 디자인에 노이즈캔슬링·37시간 재생을 지원합니다. ' +
    '66,700원.'
  ),

  h2('"스몰럭셔리"라는 말에 속지 마세요'),
  p(
    '10만원대 선물을 검색하면 "스몰럭셔리", "가성비 명품"이라는 표현이 ' +
    '자주 등장합니다. 다만 실제 댓글을 보면 이런 콘텐츠에 대한 지적이 ' +
    '반복적으로 나옵니다 — 실제 가격은 17만~19만원대인데 "10만원대"라고 ' +
    '부르거나, 10ml짜리 미니 향수를 "선물용"이라고 소개하는 식입니다. ' +
    '받는 사람이 나중에 정가를 검색해보고 실망할 수 있는 구조입니다. ' +
    '이 글에 실은 가격은 전부 확인 시점 기준 실제 판매가이며, 최고가 ' +
    '상품도 66,700원입니다.'
  ),

  h2('이건 사지 마세요'),
  bullet('"명품"이라는 이름만 붙은 마켓플레이스 초저가 상품 — 정가와 지나치게 차이 나면 가품 위험을 의심하세요.'),
  bullet('가격표만 보고 용량을 확인하지 않은 향수·화장품 — 미니 사이즈인지 정품 사이즈인지 꼭 확인하세요.'),
  bullet('노이즈캔슬링 이어폰을 사이즈·착용감 확인 없이 구매 — 귀 모양에 따라 착용감 차이가 큽니다.'),
  bullet('술을 온라인으로 직접 구매 — 위스키 스톤 같은 관련 용품으로 대신하세요.'),

  h2('자주 묻는 질문'),
  h3('10만원대 "스몰럭셔리" 선물, 믿고 사도 되나요?'),
  p('가격 표기를 실제 판매가와 대조해보세요. 정가보다 지나치게 저렴하면 미니 사이즈이거나 가품 위험이 있는 경우가 많습니다.'),
  h3('친구·연인·부모님 선물을 다르게 골라야 하나요?'),
  p('디퓨저·핸드워시·생활용품은 관계 구분 없이 무난합니다. 위스키 스톤은 홈바 취미가 있는 사람에게, 이어폰은 실용적인 선물을 원할 때 어울립니다.'),
  h3('예산을 더 쓸 수 있다면요?'),
  p('20만원 이하 선물 가이드에서 더 다양한 선택지를 볼 수 있습니다.'),

  h2('관련 가이드'),
  bullet('5만원 이하 선물만 비교하기'),
  bullet('20만원 이하 선물: 내가 사긴 아깝고 받으면 제일 좋은 것들'),
  bullet('가방 선물 추천: 진짜 명품백 대신 이걸 고르는 이유'),
];

export const products = [
  {
    rank: 1,
    name: '뭉클 샹스 오 땅드르 니치향수 미니어처 3개',
    price: 11970,
    pros: '5ml 미니어처 3개 구성. 니치 향수를 부담 없이 접해볼 수 있음.',
    imageUrl: 'https://ads-partners.coupang.com/image1/Fcb34_pgnc-ox_8vFf4KQJNT9CZdF7olqFNa_P1GbK3ob5AQ7C7nkrN2YdFmaF52qdIV13D20gAY4zzvfGe7aClx7YAJqpLCFNqDbrNNUGO8JivN7YOqaC4ROWf33BY_fAL3iCRF7lVMGUVavP6YPQhWzRiNC3hosss-ulipJhA_WU3oGVYJEupqaPKYdv7xhWpsefmQhExOzr-Zvl20MvZ3L5UnKOCFNAXioo47jfUwH3Mijrzp0eRMfamXs_V7VsG1ShGp36p4IP-pzQMyfnWqOAjcictlK2cQXDWd5Nci5ag1Ci_1qLUnVvfosnt-LU-KktDxbnUVNFPbCV3Rv2lO4CJPgmIm6kpb3j_2PUNttfD_y2jNOQYomvOvHOSx_31L2pBtwvyQYpOaLTmdySzVVOQtrKmpjmHDeb6xm56-PW7RcJJO6A_EHmbcObVx2d-t4WST29VEDv80VODRQPem23B255-9Ufs4lA32Dr8swOzJ2lGvBPsa_V8T-7rELd3KegjwqKLhl7uXFPFvNg==',
    coupangUrl: 'https://link.coupang.com/a/gNYatmmmWW',
    naverUrl: null,
  },
  {
    rank: 2,
    name: '로즐린 아로마틱 핸드워시 히노키 500ml 2개',
    price: 19900,
    pros: '히노키 향 아로마틱 핸드워시 2개 구성.',
    imageUrl: 'https://ads-partners.coupang.com/image1/rjAwa2kYziScQZaIrjLzy2uYH5mAZUHsusYp4yqjDf6hMkxt8s90GTHeSd7rpt_DOUvDT7SP4gwbQCCqftruvpBA7dVL9XrJn4LFi7iykFN1yHjKmxwEmyIkrGX4GwaI17uc1dZC1Ch8OW6Ul7XAhbcuLtD82QxAcFtRiiqJ1EPtxpS_bU6Lx6MdA7Tph1x-nw6T2dVAz6w-3bKYLFukSnHY687G_J0TS31lXSblG4XXLKaw0NNHAb0ro4i2oSN6bjr4JhevczsxFxet43r8Xl2hxpwrFAHAv3WyZA-8w7XAAq_CQ4nVxcXAwr4l5Ksq0Sl5MHcF1IrEd3r4-PeQJtSRl6wdPy5j7JY0bIwt2jK6nPNqHV_KxySkeh1QldpjzBk9vkCyK_fUYYpwa7yBD23WkiWuULWB3aS-1ztt6VVxDbzGOZamEf6bZVTO2r6V5_QBcCVO0cM_aLbvw9BimJyesA-iVjZXGuIWbepA5Xs_uZSUoctmVJOumWSw17K8zQ==',
    coupangUrl: 'https://link.coupang.com/a/gNYatrhmjQ',
    naverUrl: null,
  },
  {
    rank: 3,
    name: 'LG생활건강 생활의품격 프리미엄 퍼퓸컬렉션 샴푸바디 세트',
    price: 25230,
    pros: '샴푸+바디워시 프리미엄 라인 구성.',
    imageUrl: 'https://ads-partners.coupang.com/image1/P0lVnemt4kpYpFyhPyMOd8_PC8w4qBE5MYzm5eYEotZ5M8fs3zZJ8lmHAMBt6b0zT7xUb5gE9xvCQlesIKOWJzf8IsMbrILGybyWVnG8yX13l24cU0zbdQMlikGdknmN11DBFyTOLHpnbHH9V6TGJ-KpLjL3jVG2IzXD2NPwGhoaoFwOuQ63JTJ4HkG8P6WYBW746PYbENCYPw-q1hdhNi5u9HIKK_m9qxBk8ptpR8NEpdpkwITFR-ypUeufsA-n_L6MG5y_LYVSMBo0l5EixB6maFRF1OciESNIBQSmXzqhtuqarzCzLd_qGUQqZi90HuQqyXanN42lIzB5FWKyGcN4WFgmfvzo62uhGOWOc6COGr2Z-jUp-07_IMBgxaHZL9bh3prfsdg04JQ9eTSfZAKK7XCYsKDWaxB2bpFk9DCVuLoARry5fzRws_NdWvp3KdN47w0r-QB6LnMBaI8XDoeHHUjN_h8WgkmFcLiq9AlVPRyzT_c6D_Vjp_85InY9vJwbX5G1uu0vWw5EaBX4EShcP7-iNx34ChY6Tj3KLkaPLH6I',
    coupangUrl: 'https://link.coupang.com/a/gNYatwnhnM',
    naverUrl: null,
  },
  {
    rank: 4,
    name: '헤트라스 프리미엄 대용량 디퓨저 데이지 500ml 3개',
    price: 25800,
    pros: '500ml 대용량 3개 구성. 오래 쓸 수 있는 인테리어 향 소품.',
    imageUrl: 'https://ads-partners.coupang.com/image1/YkWZk_l6F-7H2FC1YnxM0uDyxIuMFn1hqAez3zWyjzOl-HkVbhG6ztROONph-GXJyc6Lf9-sCCxqgjvnuUseuEL3cAw5RzODpZ2qIj1xZ8cWuJcoCZSlXpogKRCS-yObYtkmyRW5sOIiHSPLV2lMWWJ7Ygf_Py-Z4gVX_eG-qFg_0_YlzSO0c_4z1R3hqOOEYZymJxcoLs5ZAnjmdgnITC-rbbQQLyM1xmEyox2mNQhEXUGB2xO7CYs1bBHWH61r4aZyQ0EhXxAwAPSRD1FCJyevPbqVzcfv7Hk5pGafYhCpI_kniZAurAQ132yn4GEYdOIX2Yys7gahvD3FL8fEPcpyTrn4otTXjSpqDQA7vf67vtFAPdhIiZrfoyGzRxxB30y65eLxJJXQE0uSy_W30qZleCtaHAEEwO9vQ0iZ6EXKfZeswEq5KRgxFEH0ySnxXVAdzc-YpdEOUXNNQ4PSwBar55hkyjPGwrMq6KLQ_BW5B7i4-GHnzKgDIBC5aQa0p_URFa4Wkwzc',
    coupangUrl: 'https://link.coupang.com/a/gNYatBcxVc',
    naverUrl: null,
  },
  {
    rank: 5,
    name: '프리미엄 위스키 스톤 트위스트 A 세트',
    price: 47700,
    pros: '녹지 않는 위스키 스톤. 홈바 취미 있는 분께 어울림.',
    imageUrl: 'https://ads-partners.coupang.com/image1/XMIYDhXOn9nsPgxzXCow9A7r0iGWAf_M_V53AHQzRrfoKwds94DKxEbRx4aCHI7jNwA1Cxh37457ya6z8lA3c61VkDL0HjAa7s_dA96TcJUaMqq0gDZVp92N0fxOhj5fAeUDF475Yys2CXoTX2jGpCkB7hPlDemkX0sMxHa224l6kBO50UmM7qsuAmQAogU1NMEjPkL9ha1bsdNry3jsN-0hgIeTl7UxwZb04bBCY-lNzgUtbhtlKEeqZCup-vQnwSoVrGSthMydv-JJIKf-2IeTtYPXiXJwEDFGGh1wCBvEsZ4PY2DdCeaYAGyUzEzkEai1620_dQpmj-4cnlaWzyOhAQXwvdxVsQniW4m3iP-3nDTRsQ3jicibrxoX7MZoAg0pAAQO98NhPaWjepNxmgzaJpr3QtSURJTPlz-mxb8EjUPRs5ardnGI52xdbuzLb0VMEphNqO-cMIKjGqjhkR4Q0q4C8VRDUG5VMGbKVhw6uYFKBHfZl7Tn8PIlHq_BEVJdZcav184cNazriynTI5JC6Rd3k9cCmmNbKJofPQ==',
    coupangUrl: 'https://link.coupang.com/a/gNYatHmGzI',
    naverUrl: null,
  },
  {
    rank: 6,
    name: '블라우풍트 노이즈캔슬링 오픈 귀걸이형 블루투스 이어폰',
    price: 66700,
    pros: '오픈형 귀걸이 디자인. 노이즈캔슬링, 최대 37시간 재생.',
    imageUrl: 'https://ads-partners.coupang.com/image1/cpIqazQ_Tsp5KfWLcomNlzPj8_JsEg9jLtJb3z2VVxpw_rnU7QR00rl1-Z_HCCLmEfVz9PmYwBg1VFWVl0P8_EtCqx-S8LZKM9MFsIZ6vvNrBxXpBQBs9w-R2WTPiswLkcKD2_uKRpyIvtES9FZefZecHLxftoynlkuPDTIf1rtL2Tr9yP0le-OPSkLTaCVqdp3B_KB5Lmwx3v-_WgIm70B5VGoZdhLLXfpgwCyGkNQj23e0GRdEzCakEHoMjNAt511HgzJMcrnC7JygrbNzEw1ozDFzmH3Qycr0DRZNRN6Gf-its-a4LgFajfQUsXoBzMdKV4_awmud-gPuQk3zN7hIMApkrfJcl0nj5peuIsNZ67dUcL_NTXQGVr6sNGX0DtPD-krb8jzuIrWLzgfgzrnxr2VHUkVdGrkmfZIIGdpd5eop4VND92GaL0ZufIE5U-siRvhuwQfGe-UlszuWK7MhuDPq4Y-GtoHPtk3a8GTiIBq5WG3aJGB47GcVD8OGx683gm5ff5HI_6k1YSKbEYa_JtAXHOgNOTmjEtawsWk0pw==',
    coupangUrl: 'https://link.coupang.com/a/gNYatO7Ffg',
    naverUrl: null,
  },
];
