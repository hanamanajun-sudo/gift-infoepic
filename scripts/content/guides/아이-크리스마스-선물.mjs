import { h2, h3, p, bullet, bulletMixed, link, table } from '../lib.mjs';

// 2026-11-07 큐레이션 (사용자 승인).
// 근거: 네이버 블로그·유튜브 수집 5개 키워드(src/data/research/*크리스마스*·산타*),
// 일본 HugKum×쇼가쿠칸 설문(저학년 이하 부모 550명, 생일선물 기준),
// 일본 고학년 선물 조사(마이나비·LIMO), 일본 fotowa 숨기는 장소 설문,
// 네이버 데이터랩(2025-10~12): 정점 12/20~23, '산타 선물'은 검색량 미미 → 제목은 '아이 크리스마스 선물'.

export const slug = '아이-크리스마스-선물';
export const title = '아이 크리스마스 선물 추천 TOP6 — 유치원생·초등학생 나이별로 이것만';
export const description =
  '아이 크리스마스 선물 추천 TOP6. 유치원생부터 초등 고학년까지 나이별로, ' +
  '25일 아침 뜯자마자 놀 수 있는 것만 골랐습니다. 산타 선물 들키지 않는 법과 ' +
  '어린이집 산타 행사 선물 기준까지 함께 정리했습니다.';
export const occasion = ['크리스마스'];
export const relation = ['자녀', '아들', '딸', '조카'];
export const ageGroup = ['유아', '4세', '5세', '6세', '7세', '8세', '9세', '초등학생', '10세', '12세'];
export const budgetTag = ['5만원이하', '10만원이하'];
export const recipientGender = '공통';
export const priceMin = 39400;
export const priceMax = 88000;

export const intro =
  '아이 크리스마스 선물은 생일선물과 고르는 기준이 조금 다릅니다. 25일 아침 ' +
  '포장을 뜯자마자 놀 수 있어야 하고, 그날까지 아이 눈에 띄지 않게 숨길 수 ' +
  '있어야 하고, 무엇보다 "크리스마스라서 받은" 특별한 느낌이 있어야 합니다. ' +
  '일본 쇼가쿠칸이 저학년 이하 자녀를 둔 부모 550명에게 물은 설문에서도 아이가 ' +
  '가장 좋아한 선물은 레고·게임기 같은 "특별한 것"이었고, 책·옷·문구처럼 평소에 ' +
  '쓰는 물건은 반응이 약했습니다. 네이버 블로그 실구매 후기와 유튜브 댓글을 ' +
  '교차 확인해 나이대별로 골랐습니다.';

export const blocks = [
  h2('가격대별로 고르기'),
  table(
    ['예산', '추천', '나이', '이럴 때'],
    [
      ['3만원대', '레고 시티 크리스마스 캘린더 2026', '만 5세~초등 저학년', '12월 1일부터 매일 하나씩 열게 하고 싶을 때'],
      ['4만원대', '우봉고 보드게임', '8세~온 가족', '크리스마스 아침 다 같이 놀고 싶을 때'],
      ['4만원대', '이지드로잉 저온 3D펜', '7~12세', '만들기 좋아하는 아이 (남녀 무관)'],
      ['5만원대', '큐블로 매직큐브 자석블럭 100p', '3~6세', '혼자 오래 집중해서 노는 장난감'],
      ['6만원대', '브리오 스타터 여행기차 세트', '3~5세', '기차·탈것을 좋아하는 아이'],
      ['8만원대', '마리오카트 월드 (스위치2)', '10~12세', '집에 스위치2 본체가 있을 때'],
    ]
  ),

  h2('아이 크리스마스 선물 추천 TOP6 — 나이 순서대로'),

  h3('3~6세, 혼자 오래 노는 "자석블럭"'),
  p(
    '자석블럭은 아이 크리스마스 선물 후기에 해마다 빠지지 않는 장난감입니다. ' +
    '45개월 아이에게 작년 크리스마스 선물로 줬다는 후기, 지오맥·벨베이비 같은 ' +
    '다른 브랜드 사용 후기까지 이어집니다. 다만 1년 사용 후기에서는 "3세는 되어야 ' +
    '제대로 갖고 놀고, 성향에 따라 5세만 되어도 시시해한다"는 이야기도 나와서 ' +
    '3~6세 사이에 주는 게 가장 오래 씁니다. 큐블로는 국내 브랜드이고 로켓배송 ' +
    '상품이라 늦게 사도 비교적 빨리 받을 수 있습니다. 56,600원.'
  ),

  h3('3~5세, 기차를 좋아한다면 "브리오 기차 세트"'),
  p(
    '기차 장난감은 브리오·이케아 릴라보·레일큐브까지 브랜드를 바꿔 가며 아이 ' +
    '크리스마스 선물 후기에 계속 등장합니다. 일본 설문에서도 기차 장난감(프라레일)이 ' +
    '"가장 좋아한 선물" 3위였습니다. 브리오는 원목 트랙이라 오래 쓰고, 나중에 다른 ' +
    '브리오 트랙을 사서 이어 붙일 수 있어 다음 해 선물로도 이어집니다. 스타터 ' +
    '여행기차 세트는 처음 시작하기 좋은 구성입니다. 69,960원.'
  ),

  h3('만 5세~초등 저학년, 12월이 통째로 선물이 되는 "레고 크리스마스 캘린더"'),
  p(
    '24개의 작은 칸을 12월 1일부터 하루에 하나씩 열어 조립하는 캘린더입니다. ' +
    '영화에서 보던 크리스마스 느낌이 나서 아이들이 특히 좋아합니다. 이 가이드를 ' +
    '만든 저희 집 아이도 초등 저학년 때 무척 좋아했습니다. 대신 12월 1일부터 ' +
    '열어야 하니 11월 안에 미리 준비해야 하고, 시즌 한정 상품이라 늦으면 원하는 ' +
    '테마를 못 구할 수 있습니다. 시티판의 권장 연령은 만 5세 이상입니다. 공주·인형 ' +
    '놀이를 좋아하면 프렌즈판(42698), 히어로를 좋아하면 마블판(76340)도 있습니다. ' +
    '39,400원(시티 60510).'
  ),

  h3('7~12세, 만드는 걸 좋아한다면 "저온 3D펜"'),
  p(
    '펜으로 선을 그리면 바로 굳어서 입체가 되는 도구입니다. "크리스마스 선물로 ' +
    '준비했는데 같이 써 보니 엄마까지 빠져들었다", "만들기 좋아하는 딸에게 사 줬다" ' +
    '같은 내돈내산 후기가 아들·딸 가리지 않고 올라옵니다. 후기마다 공통으로 강조하는 ' +
    '건 "저온"입니다. 어린이용은 일반 3D펜보다 훨씬 낮은 온도에서 녹는 필라멘트를 ' +
    '써서 화상 걱정이 적습니다. 이지드로잉은 무선이라 책상에 선이 엉키지 않습니다. ' +
    '49,800원.'
  ),

  h3('8세부터 온 가족, 크리스마스 아침에 같이 펼치는 "우봉고"'),
  p(
    '주어진 판에 조각을 먼저 맞춰 채우는 사람이 이기는 퍼즐 보드게임입니다. ' +
    '크리스마스는 가족이 함께 집에 있는 날이라 "같이 노는 선물"이 빛을 봅니다. ' +
    '형제가 있다면 각자 선물에 보드게임 하나를 공동 선물로 더하면 다툼이 줄어든다는 ' +
    '후기도 있습니다. 글을 읽지 않아도 되는 게임이라 나이 차이가 나는 형제도 함께 ' +
    '할 수 있습니다. 일본의 고학년 선물 조사에도 보드게임이 꾸준히 들어갑니다. ' +
    '44,800원.'
  ),

  h3('10~12세, 스위치2가 있는 집이라면 "마리오카트 월드"'),
  p(
    '일본의 여러 학부모 조사에서 초등 고학년이 받은 크리스마스 선물 1위는 게임기와 ' +
    '게임 소프트였습니다. 마리오카트는 남녀를 가리지 않고, 혼자 해도 가족과 해도 ' +
    '되는 게임이라 크리스마스 연휴에 잘 맞습니다. 다만 닌텐도 스위치2 전용이라 본체가 ' +
    '없는 집에는 맞지 않습니다. 이 상품은 로켓배송이 아니라 판매자 배송이니 12월 ' +
    '20일 이후에 주문한다면 도착 예정일을 꼭 확인하세요. 88,000원.'
  ),

  h2('산타 선물, 아이에게 들키지 않으려면'),
  bullet('택배 상자부터 치우세요 — 상자에 상품명과 사진이 그대로 찍혀 오는 경우가 많습니다. 실제로 상자에 적힌 상품명 때문에 들켰다는 후기가 있습니다. 아이가 보기 전에 상자를 정리해 두세요.'),
  bullet('옷장은 아이도 먼저 뒤집니다 — 일본 설문에서 부모가 선물을 가장 많이 숨기는 곳은 붙박이장·옷장이었는데, 미국 조사에서는 아이들이 가장 먼저 찾아보는 곳도 옷장이었습니다. 여러 곳에 나눠 숨겼다면 어디에 뒀는지 적어 두세요.'),
  bullet('들켰을 때는 — 일본 부모들이 가장 많이 쓴 대답은 "산타 할아버지가 미리 맡겨 두셨대"였습니다.'),
  bullet('늦게 산다면 로켓배송부터 — 크리스마스 선물 검색은 12월 20~23일에 가장 많습니다. 이때 주문한다면 위 추천 중 로켓배송 상품(1~5번)부터 보세요.'),
  bullet('포장은 과하지 않게 — 화려한 포장보다 아이가 직접 뜯는 재미를 살린 포장이 반응이 더 좋았다는 후기가 있습니다.'),

  h2('어린이집·유치원 산타 행사 선물은 기준이 다릅니다'),
  p(
    '12월이 되면 어린이집·유치원에서 "산타 선물을 아이 몰래 보내 달라"는 가정통신문이 ' +
    '옵니다. 산타가 아이들 앞에서 직접 건네주는 선물이라 집에서 주는 선물과 기준이 ' +
    '다릅니다.'
  ),
  bullet('예산은 1만원대가 보통입니다. 다른 아이들과 함께 받는 자리라 너무 비싼 선물은 오히려 부담이 됩니다.'),
  bullet('너무 크거나 무겁지 않은 것으로 고르세요. 산타가 들고 나와서 아이 손에 건네야 합니다.'),
  bullet('이름표를 꼭 붙이세요. 산타 할아버지 편지를 짧게 함께 넣으면 아이들이 더 좋아한다는 후기가 많습니다.'),
  bulletMixed('1만원대 선물은 ', link('1만원 이하 선물 추천', 'https://gift.infoepic.com/선물/1만원이하-선물/'), '에서 고를 수 있습니다.'),

  h2('아이 성향에 따라 참고할 것'),
  p('TOP6에는 넣지 않았지만, 아이 성향에 따라서는 이쪽이 정답일 수 있습니다. 대신 각각 알아둘 점이 있습니다.'),
  bullet('꾸미기 좋아하는 4~9세 — 어린이 화장품·매니큐어: 아이 반응은 좋습니다. 다만 검색되는 후기의 상당수가 협찬 글이라 그대로 믿기 어렵습니다. 물로 씻기거나 떼어내는 수성 제품인지, KC 인증과 성분을 직접 확인하세요.'),
  bullet('폰을 조르는 고학년 — 휴대폰: 아이들이 가장 원하는 선물입니다. 다만 요금제와 사용 시간 규칙은 가족이 정할 일이라, 산타 선물로 깜짝 주기보다 부모가 규칙과 함께 주는 편이 낫습니다.'),
  bullet('공부·영상 겸용 — 태블릿: 인강·숙제용인지 영상용인지 먼저 정하세요. 용도에 따라 10만원대부터 수십만원대까지 가격이 크게 갈립니다.'),
  bullet('아이돌 팬인 고학년 — 아이돌 앨범: 아이에게는 1순위 선물입니다. 다만 최애 멤버와 앨범 버전을 정확히 알아야 하고, 포토카드는 랜덤이라 원하는 멤버가 안 나올 수 있습니다.'),
  bulletMixed('캐릭터를 좋아하는 아이 — 산리오·먼작귀·가나디 굿즈: 유행이 빨리 바뀌고 가품이 많습니다. ', link('가품 위험 안내', 'https://gift.infoepic.com/가품-위험-안내/'), '에서 확인 방법을 보세요.'),
  bulletMixed('구조물·실험을 좋아하는 아이 — 그래비트랙스: 구슬이 레일을 타고 내려가는 장난감으로, 주로 남자아이들 반응이 좋습니다. ', link('10살 남자아이 생일선물', 'https://gift.infoepic.com/선물/10세-남자아이-생일선물/'), '에서 자세히 다뤘습니다.'),
  bulletMixed('사진·꾸미기를 좋아하는 고학년 — 즉석카메라: 찍은 사진이 바로 나와서 좋아하지만 필름값이 계속 듭니다. ', link('12살 여자아이 생일선물', 'https://gift.infoepic.com/선물/12세-여자아이-생일선물/'), '에서 자세히 다뤘습니다.'),

  h2('이건 사지 마세요'),
  bullet('책·학습지·문제집 — 일본 설문에서 아이가 "별로 안 좋아한 선물" 2위가 책·그림책이었고, 학습지도 순위에 올랐습니다. 공부와 연결되는 순간 선물 느낌이 사라집니다. 책을 주고 싶다면 다른 선물 옆에 곁들이세요.'),
  bullet('옷·신발 — 같은 설문에서 3·4위였습니다. 필요해서 사는 물건은 평소에 사 주고, 크리스마스에는 "특별한 것"을 주세요.'),
  bullet('아이가 말한 이름만 듣고 사는 레고·피규어 — "2만 원짜리 레고를 사 달라기에 가 봤더니 20만 원대였다"는 후기처럼, 아이가 말하는 제품과 실제 제품이 다를 수 있습니다. 정확한 제품명을 먼저 확인하세요.'),
  bullet('12월 20일 이후에 주문하는 판매자 배송 상품 — 25일 전에 도착한다는 보장이 없습니다. 이 시기엔 로켓배송 상품을 고르세요.'),

  h2('자주 묻는 질문'),
  h3('아이가 산타에게 뭘 받고 싶은지 어떻게 알아내나요?'),
  p('가장 확실한 방법은 미리 물어보는 것입니다. 일본의 선물 조사에서도 "본인에게 미리 묻는 게 제일 확실하다"는 의견이 가장 많았습니다. 산타에게 편지를 쓰게 하면 자연스럽게 알 수 있고, 11월 안에 받아 두면 레고 캘린더처럼 미리 준비해야 하는 선물도 놓치지 않습니다.'),
  h3('아이 크리스마스 선물 예산은 얼마가 적당한가요?'),
  p('정해진 답은 없습니다. 일본에서는 초등학생 생일선물 예산을 5,000엔 안팎으로 잡는 집이 많다는 조사가 있고, 이 가이드의 추천 상품은 3만원대부터 8만원대까지입니다. 게임기·태블릿처럼 큰 선물은 산타 선물과 따로 생각하는 게 부담이 덜합니다.'),
  h3('형제자매가 있으면 선물을 어떻게 나누나요?'),
  p('각자 선물을 하나씩 주고, 함께 쓰는 보드게임을 공동 선물로 하나 더하는 방법이 있습니다. 실제로 이렇게 하면 다툼이 줄어든다는 후기가 있습니다.'),
  h3('12월 20일이 지났는데 아직 못 샀어요.'),
  p('위 추천 중 1~5번은 로켓배송 상품입니다. 레고 캘린더는 12월 1일부터 여는 상품이지만 늦게 받았다면 25일까지 하루에 몇 칸씩 열어도 아이들은 충분히 즐깁니다.'),

  h2('관련 가이드'),
  bullet('크리스마스 선물: 받는 사람이 정해지지 않았다면'),
  bullet('7-9세 남자아이 생일선물: 초등 저학년 남자아이가 진짜 좋아하는 것'),
  bullet('7-9세 여자아이 생일선물: 초등 저학년 여자아이가 진짜 좋아하는 것'),
  bullet('10세 남자아이 생일선물: 10살 남자아이 추천'),
  bullet('12세 여자아이 생일선물: 12살 여자아이 추천'),
];

export const products = [
  {
    rank: 1,
    name: '큐블로 매직큐브 자석블럭 100p MC100C',
    price: 56600,
    pros: '3~6세. 크리스마스 선물 후기가 해마다 반복되는 장난감. 국내 브랜드, 로켓배송.',
    imageUrl: 'https://ads-partners.coupang.com/image1/WXngsTtlxqdEcpA2WRdKnBvPMBV84tAcSQEhgsUG-S8w2jWiRBF22gRQ8kbfyo1QcP6mo4d9vtDMp2iZUx6391vn0R7mVcz1w9ekzf5ktunOzNItWswiV0p5cbFqbkyT0yQOFt7gRm-QzOfCHAQ4AB9xpHc5rA7FU_99Zox55PaQtZM_bEN9_3xRvcsHhz1flHmENNqU8oZbSfuap456cLBMRzs3ngKmrR-T24DoKglT35fzT7ZFuPsx0gQv9sl-Eba7hZLcghPbzoCN0yBzeEz_Cy6Zs8-r6KJs-1f8gVo866rifFI3lN_-Ni-JOjnaInP25mzln8jCEEjNL24jdSIwbKkxYaHUDUI-mdDgFbyK7vlxjR65pPCLEyTPAnrtUbIlmB5NfB1opeQLU8-B_-lkemB2HSAk9WgY9mcmDo2yAG8d6D9c9ETxEIxogXz3S1oIm-rsqY3ZcC1A7C7flRyf642iI66YuSNbFz4VGQ2c1rjyhH6XxA8ATaEWp75kvYgvSUGMiOE=',
    coupangUrl: 'https://link.coupang.com/a/itUZNvQsW4',
    naverUrl: null,
  },
  {
    rank: 2,
    name: '브리오 스타터 여행기차 세트 36079',
    price: 69960,
    pros: '3~5세. 원목 트랙이라 오래 쓰고 다른 브리오 트랙과 이어 확장 가능. 로켓배송.',
    imageUrl: 'https://ads-partners.coupang.com/image1/OAF_8JqyKui9fog1OB99l0Cb2VBR5FI5TBPwiA6XZ70ND8LcGqfLStCQxKHW966ftJ_qMrQb3F9OBU1HjkC8ERSWNq-IPSaoGYkzbI1h1VBzzIh6wXty3oCbmPg1vN81bMvJy7PDu7u2ll-WdjXn0F9FZJqkwwLsYTKA0Feq0wVtT9WIeEdQvdtZvZx_6pmxbkkVLNdtfq9I9IhzcW7hkn0spwLvPF6jmCl4JYzEPdW3VkBuHnwiWNCTumh0hvHziy6vF8ddbsP4KPCdv8yfUo02DW7vP5HSgcmw-jweogGK28lG5YsvhWVdPZBNwCMm2wCjDbb-Sgt0kXu7foMBbRwmrqSH-IfQavSVR83MlXRk0GDcRwAC6_yAtf0E7vFYFhs-xGP4P4b3oTTGfrWyYMSaQke2DdRJ7jqRDNlgwFGEtgIiQ34yepoARFlYqcI3inSkw0ZTQtapVp7Ht5QRyapDLH4PEOImRtcu3qFUtM-1K0nFuj-TwTDzUEUpNynsJ7III8BTmVgT5OZMns2e',
    coupangUrl: 'https://link.coupang.com/a/itUZNCwudg',
    naverUrl: null,
  },
  {
    rank: 3,
    name: '레고 시티 크리스마스 캘린더 2026 60510',
    price: 39400,
    pros: '만 5세 이상. 12월 1일부터 24일간 매일 한 칸씩. 11월 안에 준비해야 함. 로켓배송.',
    imageUrl: 'https://ads-partners.coupang.com/image1/sRct5RI_NW57GQ2NscLZEmd1wu0UPxnJxaENbzrwtZFlFJRO_p_H7KxILFFULr3ualYwhwtwS4MndA2nRRK7-qeKgtENZwwon8C0C2oUJwDzSiapK6NTiL41SdBaH5Ed84g-EZfOEpfHZ2aPpFiBnzrYb6tU5JjgyLwY1j7zk2J83qSWGOFuKIGreTMdXTotGup7kH74wI6I00Gzt3HUt3Wdpok0m0iZVmq1B7oGFPOh0lNO4b4N65dVVTFG8YlE9WpgJ2DflIOtexXev0iojJ0dWm2dwM7rV0O-vKSjwWolHPNNTILwEriZIhOlwEGqUt240cK-xMWHjn5aY8SROU73116lOPRXpQR_xZu5QXYdNIb_3glSh30XlV8v30dkFoS_tn3pTQNykZS9W6iR2A-yMbu3JGJHM8q3V6q7_uSlb7x8wZwAVpcg99jis6XKC-30DiYjsL-D7Kc1WQvp83O8_9HM9HSu3UzIdJIRpLkm0nblu3aeBL3l7jY_RhGi_Bh-NhEnPFNneCK4TfZ8n5M=',
    coupangUrl: 'https://link.coupang.com/a/itUZNGUO1A',
    naverUrl: null,
  },
  {
    rank: 4,
    name: '이지드로잉 어린이 저온 무선 3D펜',
    price: 49800,
    pros: '7~12세, 남녀 무관. 저온 필라멘트라 화상 걱정이 적고 무선. 로켓배송.',
    imageUrl: 'https://ads-partners.coupang.com/image1/zYsTiwy_JNClPBsTzZOIuDv0UXBRq75U4uwGLuXGgPj7Kohp_Y9EJ_wO7nlMw-u-lRB4YhPHNyzHxDQQvKZJJnzdQSsWLLjSwO06ZqPYdA8Mh_7U6HWC6yBPPFWJMbOZVRKqvASFUjVQSqGRjL3o6G2gLh0k41enq6j3S7CTVcdV7NrNa2eUeRvAE7WID9PCp3df9TDR2HR9JtcZycQfb2yemxyMmnUnUrD8g-0sAkR2I_jqJ1fOfQySo_oWEdepIQjZlcbBMXA86bKNdQ-ofo0Zdf_Az9FCFAt__HbkloeRdfs5bEsOG8zya2ogqh0T9tQkSHELNphEDcY8o0YPzphmgrwbGqhwgs7ze4MVX6GxgKrayx5aKYYobWNumoFIU3bjExvCCGzWetGseR7VLZTCX2ipoIP3p_v8qQNj3CIaIz5Lc04-sfXmgsbXTPFheJj7-a2GVdoLEEsPm7k8TTsI4S6j-ZKHKHpNw0LO2PaExSKT3kzl4T8aB49y-fViZyv1_Pa1ehVctpNzmNaLmxsKuD4HaRidv7NaOkYXcKGF',
    coupangUrl: 'https://link.coupang.com/a/itUZNLj3fg',
    naverUrl: null,
  },
  {
    rank: 5,
    name: '코리아보드게임즈 우봉고 보드게임',
    price: 44800,
    pros: '8세~온 가족. 글을 읽지 않아도 되는 퍼즐 게임이라 형제 공동 선물로 좋음. 로켓배송.',
    imageUrl: 'https://ads-partners.coupang.com/image1/U1vAL4qdvVJRifcBU9ChKBFBdJJiYlJufBbWMxDmWwddqV0Xs-TwGUDw0fo8uo1UGEbALA4H-jfcwsoj6AHj31WLhzUI48snsE3fqSXaJU9V8jIYgHDTHihsLRbTrDkQDJ1xFGFgZVgzvExIDNdCR1i3H8IOeAaWuB2yWums600Xqp5GY4M9Unsg6piF8tAu_16zbrnaq1WUzGMaHxEh_JK8JDB1-o1gYIYjEJ7-ZeOcFAaEuabs9YFdi8rPD8LlGoVy222gn8LMte6GVIUNRfhCmrql8oJyB77HGmb9Xm1LADb_p3rekVIwQXOIsMk3YzM19vKvE3usRjXFDnafXmzZHpuX31gvBAWJV7aAk1DSaldBvFTsyp_60VfwvSZl9Euve1OttLpgYHtxw98Vu6Kjq0wZ2kMZysvroNaOCFEti0wg6Vuw0pxmII0DuoQQTYuGT_pL-WPCLyH5MmyNKlUzLn66nRr3sXGhOqQ8KTQmHkQ-yfZ6u1PmQUsXJhB4aSiA8sd-vosYVr-P',
    coupangUrl: 'https://link.coupang.com/a/itUZNQGiAu',
    naverUrl: null,
  },
  {
    rank: 6,
    name: '닌텐도 스위치2 마리오 카트 월드 한글판 게임 칩',
    price: 88000,
    pros: '10~12세. 스위치2 본체가 있는 집만. 판매자 배송이라 12월 20일 이후엔 도착일 확인.',
    imageUrl: 'https://ads-partners.coupang.com/image1/tRsNGmMIBnunjDiGtYXJN5K4vuk0NhIs1rtwZvHxUmcfFO22PaoR1isP-ky3M04pPsRFAzovCVi_S4XG7-DxlW6EAX5rJXH3IRXb_3in-2kRTGQLGdDwcQz1kjEl2K_XHXelkYKwPqbW05dv-G_peZvcFordHT1MbqWOa3Aq4H2vPxHBWcLH5ID98dfIjlgCB0BEkU14qH2QPDzgT63F9vGtzUlQ_haPryHwqgiBnR0x4nCgPwluXDUiqFLeSeeSkEx0D7xna808Ff0RRr6rNEBd2908dXqdKePFYF09eBsBA1cL_YxRpZDTvuhrpwgS_95uO3U8TxdDdzUai4e7kZ2-OQk_oyKt_4CxYTRO_nObiYxCFQFtz8Hb0eE3TsAEaEnuBxeYGXizV2DgvfChdPB7eXNtXwgSBm_aKD8dXuCbaHqxNUTnvc2Jg4m-x3sOJ8DuI5mq_Ce4D9hgmr-RjAfR0nDV1oy4ZsUNIjcqt1EEi6WVZJM6aInT1yjVBWIcM7hKnAZCKKRUJayJwKcVonxEaGbmTeB-j6NWvg2XtQ==',
    coupangUrl: 'https://link.coupang.com/a/itU0H4Qw0a',
    naverUrl: null,
  },
];
