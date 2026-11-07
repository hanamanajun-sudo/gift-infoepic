import { h2, h3, p, bullet, bulletMixed, link, table } from '../lib.mjs';

// 2026-11-07 받는 사람별 허브로 재작성 (사용자 승인).
// 이전 버전(계절 소품 6개: 스노우볼·트리·편지지·캔들·어글리 스웨터·꽃다발)은 28일 조회 1회.
// 근거: 네이버 블로그·유튜브 수집 5개 키워드(src/data/research/ 여자친구·남자친구·부모님-크리스마스-선물-후기,
// 크리스마스-선물교환-3만원-후기, 마니또-선물-직장-크리스마스),
// 네이버 데이터랩(2025-10~12): '크리스마스 선물' 일반어가 다른 키워드의 10배 이상, 정점 12/20~23.
// 엄마 상품은 아빠 면도기(89,770원)와 가격을 맞춰 달라는 사용자 요청으로 발마사지기(88,120원) 선정.

export const slug = '크리스마스-선물';
export const title = '크리스마스 선물 추천 TOP8 — 여자친구·남자친구·부모님·선물교환, 받는 사람별로';
export const description =
  '크리스마스 선물 추천 TOP8. 여자친구·남자친구·엄마·아빠·선물교환(마니또)·아이까지 ' +
  '받는 사람별로 1~2개씩만 골랐습니다. 주문 마감 시기와 선물교환 예산 기준도 함께 정리했습니다.';
export const occasion = ['크리스마스'];
export const relation = ['여자친구', '남자친구', '엄마', '아빠', '친구'];
export const ageGroup = [];
export const budgetTag = ['3만원이하', '5만원이하', '10만원이하'];
export const interests = ['생활'];
export const recipientGender = '공통';
export const priceMin = 22500;
export const priceMax = 89770;

export const intro =
  '크리스마스 선물은 "무엇을 줄까"보다 "누구에게 줄까"에서 이미 반은 정해집니다. ' +
  '연인에게는 겨울 내내 쓰는 것, 부모님께는 서랍에 들어가지 않고 실제로 쓰시는 것, ' +
  '선물교환·마니또에서는 예산 상한을 지키면서도 크리스마스 기분이 나는 것이 기준입니다. ' +
  '네이버 블로그 실구매 후기 100건과 유튜브 댓글을 받는 사람별로 나눠 확인하고, ' +
  '받는 사람마다 1~2개씩 TOP8로 추렸습니다. 아이 선물은 나이별로 따로 정리한 가이드가 있습니다.';

export const blocks = [
  h2('받는 사람별로 바로 고르기'),
  table(
    ['받는 사람', '고르는 기준', '추천', '가격'],
    [
      ['여자친구', '겨울 내내 쓰는 것, 취향 실패가 적은 것', '캐시미어 머플러 · 록시땅 핸드크림 세트', '3만~7만원대'],
      ['남자친구', '실용적인데 선물다운 것', '캐시미어 머플러 · 닥스 가죽장갑', '5만~7만원대'],
      ['엄마', '서랍에 들어가지 않고 매일 쓰시는 것', '공기압 온열 발마사지기', '8만원대'],
      ['아빠', '매일 쓰고 오래 쓰는 것', '브라운 시리즈5 전기면도기', '8만원대'],
      ['선물교환·마니또', '예산 상한 안에서 크리스마스 기분', '하리보 어드벤트 캘린더 · 오르골 워터볼', '2만원대'],
      ['아이', '25일 아침 바로 놀 수 있는 것', '레고 크리스마스 캘린더', '3만원대'],
    ]
  ),
  bulletMixed(
    '아이 선물은 ',
    link('아이 크리스마스 선물 추천', 'https://gift.infoepic.com/선물/아이-크리스마스-선물/'),
    '에서 유치원생부터 초등 고학년까지 나이별 6개를 볼 수 있습니다.'
  ),

  h2('크리스마스 선물 추천 TOP8 — 받는 사람별로'),

  h3('[연인] 겨울 내내 목에 두르는 "캐시미어 100% 머플러"'),
  p(
    '여자친구·남자친구 크리스마스 선물 후기를 나눠 봤을 때 양쪽 모두에 자주 나온 ' +
    '품목이 머플러였습니다. 코치·버버리 같은 명품 머플러 후기가 많지만 20만원을 ' +
    '넘기기 쉬워서, 캐시미어 100%이면서 10만원 안쪽인 제품으로 골랐습니다. ' +
    '남녀공용 디자인이라 여자친구·남자친구 누구에게 줘도 되고, 선물박스가 포함돼 ' +
    '따로 포장할 필요가 없습니다. 색은 상대가 평소 입는 코트 색에 맞추면 실패가 ' +
    '적습니다. 79,000원, 로켓배송.'
  ),

  h3('[여자친구] 취향을 몰라도 실패가 적은 "록시땅 핸드크림 기프트팩"'),
  p(
    '립스틱·향수는 여자친구 크리스마스 선물로 자주 추천되지만 색과 향이 취향을 ' +
    '크게 탑니다. 화장품을 잘 모른다면 핸드크림이 안전합니다. 록시땅 시어버터 ' +
    '핸드크림은 향보다 보습으로 알려진 제품이라 겨울에 건조한 손에 매일 바르기 ' +
    '좋고, 선물포장과 쇼핑백이 함께 와서 그대로 건네면 됩니다. 머플러에 곁들여도 ' +
    '부담스럽지 않은 가격입니다. 31,800원.'
  ),

  h3('[남자친구] 실용적인데 선물다운 "닥스 천연 가죽장갑"'),
  p(
    '남자친구 선물 후기에는 지갑·향수·시계가 많지만, 지갑은 이미 쓰던 게 있기 ' +
    '쉽고 향수는 취향을 탑니다. 장갑은 겨울에 없으면 바로 아쉬운 물건인데 정작 ' +
    '본인은 좋은 걸 잘 사지 않는다는 점에서 크리스마스 선물로 잘 맞습니다. 닥스 ' +
    '천연 가죽장갑은 선물포장과 쇼핑백이 함께 오고 로켓배송입니다. 손이 큰 ' +
    '편이라면 사이즈를 고를 수 있는지 상세 페이지에서 먼저 확인하세요. 59,000원.'
  ),

  h3('[엄마] 저녁마다 쓰시는 "공기압 온열 발마사지기"'),
  p(
    '부모님 선물 후기에서 가장 많이 나온 말은 "결국 서랍에 들어갔다"였고, 반대로 ' +
    '계속 쓰신다는 선물에는 안마·찜질 용품이 많았습니다. 이 발마사지기는 공기압 ' +
    '마사지와 온열 찜질을 함께 해 줘서, 겨울 저녁 TV를 보실 때 발을 넣어 두기만 ' +
    '하면 됩니다. 중소 브랜드 제품이라 AS 보장 내용을 상세 페이지에서 확인하고 ' +
    '사는 것을 권합니다. 아빠 면도기와 가격대를 맞춰 두 분께 함께 드리기 좋습니다. ' +
    '88,120원, 로켓배송.'
  ),

  h3('[아빠] 매일 아침 쓰시는 "브라운 시리즈5 전기면도기"'),
  p(
    '남편·아빠 크리스마스 선물 후기에서 전기면도기는 "1년 넘게 잘 쓰고 있다"는 ' +
    '말이 반복되는 품목입니다. 브라운은 상위 시리즈로 갈수록 수십만원대로 ' +
    '올라가는데, 시리즈5는 8만원대라 엄마 선물과 예산을 맞추기 좋습니다. 이미 ' +
    '쓰시는 면도기가 있다면 언제 산 건지 먼저 확인해 보세요. 89,770원, 로켓배송.'
  ),

  h3('[선물교환·마니또] 12월이 통째로 선물이 되는 "하리보 어드벤트 캘린더"'),
  p(
    '직장 마니또와 친구 선물교환 후기에서는 2만~3만원 상한이 가장 흔했고, 그 ' +
    '안에서 크리스마스 기분을 가장 확실하게 내는 선물이 어드벤트 캘린더입니다. ' +
    '12월 1일부터 하루에 한 칸씩 열어 젤리를 꺼내는 달력이라, 받는 사람이 누구든 ' +
    '부담 없이 즐깁니다. 판매자 배송 상품이라 12월 1일 전에 받으려면 11월 안에 ' +
    '주문하고, 식품이니 유통기한도 확인하세요. 25,580원.'
  ),

  h3('[선물교환·마니또] 시즌이 지나도 남는 "오르골 워터볼 무드등"'),
  p(
    '3만원 안쪽 선물교환에서는 "예쁜 쓰레기"가 되지 않는 게 관건입니다. 오르골 ' +
    '워터볼은 흔들면 눈이 내리고 오르골 음악이 나오는 크리스마스 소품이면서 ' +
    '무드등으로도 쓸 수 있어서, 크리스마스가 지나도 책상이나 침대 옆에 남습니다. ' +
    '성별과 나이를 가리지 않아 누가 받을지 모르는 랜덤 선물교환에 특히 무난합니다. ' +
    '22,500원, 로켓배송.'
  ),

  h3('[아이] 12월 1일부터 매일 여는 "레고 크리스마스 캘린더"'),
  p(
    '아이 선물은 나이에 따라 정답이 크게 달라서 따로 가이드를 만들었습니다. 그중 ' +
    '유치원생부터 초등 저학년까지 가장 넓게 통하는 하나를 꼽으면 레고 크리스마스 ' +
    '캘린더입니다. 저희 아이도 초등 저학년 때 정말 좋아했습니다. 영화에서 보던 ' +
    '크리스마스 느낌이 나서 아이들이 특히 좋아하는데, 12월 1일부터 여는 상품이라 ' +
    '미리 준비해야 합니다. 39,400원(시티 60510), 로켓배송.'
  ),

  h2('주문은 언제까지 해야 하나요'),
  bullet('올해 크리스마스는 금요일입니다. 12월 셋째 주부터 택배가 몰리고 주말이 끼어, 판매자 배송 상품은 25일 전 도착을 장담하기 어렵습니다.'),
  bullet('판매자 배송 상품(록시땅 핸드크림, 하리보 캘린더)은 12월 둘째 주까지 주문하는 것이 안전합니다.'),
  bullet('12월 20일이 지났다면 로켓배송 상품(머플러·가죽장갑·발마사지기·면도기·오르골 워터볼·레고 캘린더)에서 고르세요.'),
  bullet('어드벤트 캘린더는 12월 1일부터 여는 상품이라 11월 안에 받아야 제 역할을 합니다.'),

  h2('같이 주면 좋은 것'),
  p(
    '어떤 선물이든 짧은 카드 한 장을 더하면 인상이 달라집니다. 크리스마스는 유독 ' +
    '손편지 문화가 남아 있는 날이라, 1만원 안쪽의 크리스마스 편지지 하나로도 ' +
    '충분합니다. 부모님 선물 후기에서는 용돈과 함께 실제로 쓰시는 물건 하나를 ' +
    '드리는 조합이 자주 나왔습니다.'
  ),

  h2('이건 사지 마세요'),
  bullet('사이즈가 딱 맞아야 하는 옷 — 스웨터·패딩은 사이즈와 취향을 모두 맞춰야 해서 교환이 잦습니다. 입는 걸 주고 싶다면 머플러·장갑처럼 사이즈 부담이 적은 것으로 고르세요.'),
  bullet('선물교환에서 상한을 넘기는 선물 — 혼자 비싼 선물을 가져오면 받는 사람보다 다른 참가자들이 불편해집니다. 정해진 예산을 지키는 게 예의입니다.'),
  bullet('크리스마스가 지나면 쓸 데가 없는 장식 — 반짝이 장식이나 일회용 소품은 1월이면 버려집니다. 시즌 소품을 주려면 무드등처럼 평소에도 쓰는 것으로 고르세요.'),

  h2('자주 묻는 질문'),
  h3('연인 크리스마스 선물 예산은 얼마가 적당한가요?'),
  p('정해진 답은 없습니다. 이 가이드의 연인 추천은 3만원대부터 7만원대까지입니다. 사귄 지 얼마 안 됐다면 미리 예산을 맞춰 두면 서로 부담이 줄어듭니다.'),
  h3('부모님께도 크리스마스 선물을 드려야 하나요?'),
  p('꼭 그렇지는 않지만, 한 해 고마웠다는 인사를 겸해 드리기 좋은 때입니다. 엄마·아빠 선물을 같은 가격대로 맞추면 두 분께 함께 드리기 편합니다.'),
  h3('마니또·선물교환은 얼마짜리가 적당한가요?'),
  p('직장·친구 모임 후기에서는 2만~3만원 상한이 가장 흔했습니다. 정해진 상한이 있다면 그 안에서 고르고, 없다면 3만원 이하로 맞추는 것이 무난합니다.'),
  h3('12월 20일이 지났는데 아직 못 샀어요.'),
  p('위 추천 중 머플러·가죽장갑·발마사지기·면도기·오르골 워터볼·레고 캘린더는 로켓배송 상품입니다. 결제 전에 도착 예정일을 꼭 확인하세요.'),

  h2('관련 가이드'),
  bullet('아이 크리스마스 선물: 유치원생·초등학생 나이별 TOP6'),
  bullet('여자친구 생일선물: 연인 선물을 더 넓게 보고 싶다면'),
  bullet('남자친구 생일선물: 연인 선물을 더 넓게 보고 싶다면'),
  bullet('엄마 생일선물: 엄마 선물 더 보기'),
  bullet('아빠 생일선물: 아빠 선물 더 보기'),
  bullet('마사지기 선물 추천: 부모님 안마기를 더 비교하려면'),
  bullet('3만원이하 선물: 선물교환 예산에 맞춰 고르기'),
];

export const products = [
  {
    rank: 1,
    name: '코어하임 캐시미어 100 머플러 남녀공용 (선물박스 포함)',
    price: 79000,
    pros: '여자친구·남자친구 공용. 캐시미어 100%에 10만원 안쪽, 선물박스 포함. 로켓배송.',
    imageUrl: 'https://ads-partners.coupang.com/image1/WSqE6RcVL21LaMglWerJCinHENtcmjKiVMMAwmlOCNBz4VLKQO9LGpYgAuspD78TDt3MelrW7wU1fbYzX_l1X1eivlqT93QyJkx75arJcdLrRJLTwFRc3g4Ucigt_FYhDIi6_fGAHec4LLNnIdjiN8HBu_3vo9twnGfhYmh9ezOu1cqUATbgQee2ECt6xhQBUsi5K5JPB5XbRkNrCh8NmoFiQfpdj6TIsDJChPKt8aHef-XrbRsKEsgqoI0nmK6BcHWwIVy0Ztj1kRg2aQC9C29JQ6BMXenaCIvX3q6dQvFmy7E29rSX4MTRR2wNYJ8Kg7B6b1IpZGZgoGQ4yT92DYc0mOCZNzqk8b8AoJZwRYhSaxpjsd5p-4gmqO90_Y0XD4NvRnc54xrogTXUAHY_Iezmi8Cw53Tyc3_yh44ntGmNLYyJRq10o0gOSxRiqR0rHZ93oJZl_CDSiNaZvoVI819GKaZWUS6-QOtakiJWuoOaNYLVfkT4g1PDPjMI47PB92PX5uxrkWAvEdie3OQRFr0zDKFTCUpIXiRwy5K0Bg0YdezH6VvmWxZytfuZYJPv_D22Mvh-UkVrQOyjma-LVk7kJWAcJxC7YP0l',
    coupangUrl: 'https://link.coupang.com/a/iuhA3uX0r6',
    naverUrl: null,
  },
  {
    rank: 2,
    name: '록시땅 시어버터 핸드크림 GIFT PACK 세트 (선물포장+쇼핑백)',
    price: 31800,
    pros: '여자친구. 색·향 취향을 덜 타는 핸드크림. 선물포장 포함. 판매자 배송이라 미리 주문.',
    imageUrl: 'https://ads-partners.coupang.com/image1/VUuWRAyyafh1mFs-VaONJC3UPbiWItNW3of-TwhCEKIUm90AilL3kxew2G7T8NlYf64j0U7xC5QBwc5p7fqVnSEitTUp2zEJQubItJyxE-bIjqIlrAaqJLJeuPmuKc8XzXG9zf8UGWUEzLiYpnhZlFourTjgv-VJRkMYt-1ZfESDlpFeouOiy6mnTkRN4pz1fvN15ErAHl-054aMuuWsn3ngdsWCGDr9gIDpwZhXg3Gf4iJ0t4u8BD5qv_N7S8orcFAOFOgMlMruPBlKFDd5pphPJcTqhWu1cYcJwVgeGkTkvYXLHmulHnGsUaeseiHVLk-v8wq9PcLR9b-O47aC24F7Xy5AWdIeDXrH1_ES0UZ8YS5G3sem-tX_Hi125At5OR-eECYx3xkokL_kXNck3N8MuEI8bM_1Q_HEjtEMiiDq5I2gZgE6EhT3YdjEoEdF3v-Tzm_OzQnudRysqhqk1RvlPu8GUdkVMpsSIw5KiqgbaEG4JBzs21UYfww7tlT1V3YNhAdxCcrssN2DRqKQGC1upIlGeM4AQkoTJtoJbmlG0rh12l1IQj8G0T5X',
    coupangUrl: 'https://link.coupang.com/a/iuhAgbS0Qu',
    naverUrl: null,
  },
  {
    rank: 3,
    name: '닥스 남성 천연 가죽장갑 (선물포장+쇼핑백)',
    price: 59000,
    pros: '남자친구. 겨울 실용템인데 본인은 잘 안 사는 물건. 선물포장 포함. 로켓배송.',
    imageUrl: 'https://ads-partners.coupang.com/image1/0gkK0PnWCPESaOQg0tH-s5EExVpISxkBuRoCpwN7BV4I1dbO68a8hGX_hya3yfIt1CRtXEXadzRBdrZkoBp1OH5CH34e0dxfRMrh1yKc7Ib6myAHSgIVDmQGx3vt6mLEUTYnXP2SwrKVH7yn8pTQNLL1tXEXl0ExdJ-oBHX6a-mQe6sVbs-15_Z9_ZZrcFXC-o8BDvEpwQL1NKm4jJxLP9N2o_M1s3HgMZXnciu5Haa885i7pc5Wp86Sb82lrCymYCybpTXyqwTVUTkFgudGlg4_x8qH2NRDaWQkv-kThinxSEZglWActEitFKB_nZLLDApLbk2s-iQWrkScD3wLxZy6SM6jwBI6qTVOYY6JQktJ8-ghT_dMAYho0vqyKpS8N65ku0_r2RGzb4yvrhxgrdSslURPhVjs5Fik-B986NBLJxUrZo-Iafu4nxHdm7VxbAVtAGzABrHyEup3uBjEgq-zhk5nUqmVWCnB4a6rleW0V2aO3ZgfyXApDtqEjV3TcVoO_slIuRJBJg28G-Ge7qjeeJ1RCe7qBxJqh3AxCQAi_UjB',
    coupangUrl: 'https://link.coupang.com/a/iuhAghIeIu',
    naverUrl: null,
  },
  {
    rank: 4,
    name: '힐링 발마사지기 공기압 온열 찜질 SH-22F',
    price: 88120,
    pros: '엄마. 공기압+온열 찜질. 아빠 면도기와 같은 가격대. 중소 브랜드라 AS 조건 확인. 로켓배송.',
    imageUrl: 'https://ads-partners.coupang.com/image1/6cu9zwJK3jzpi_PZ6RYQT_RCu78WOtJUwtOSR0M2_WoO8TeMbRiGPRufKPjFBYNIsYMnIpbjcCLqUiG-eUr7dv4k6YvRvTWhYgj6r80M-AaQd8xecuRDfdanKFEPLv5HsXeLjWye4GF7lYUGOwnkSeEM4SOEB0LAVX6Nqbnv6DovCfy0Hea2-O5IqZCaZghF284T2fsgcOvz3yxDvSVH01vaFKrmPycHjumlaUxp4fGzdJf3DVRqQdrOgkfk-aijusJIo0Qoe_ymfPYihGmfLAK8-q8YzBmkxgQa_PvuO4vERHLk8aqB2opRrxqS9ZB5Y0pws7kzZv2wWJy7lXfKZxqJU23zyxVHrZKMeu0LvK3DuVrghNMmlxHnvhp382AtBZpeV2BUaDPjYA8h9Xh_Tlwm283JbLg1vLr8dOCLYfaPbfQ7wVa2P09Ii1ewHBpesCWUnAZCZkl3EQ1WgQjTRQPlEUljCdfdW1jN3kBguW2tPm7lEqEWhNjf0i8gGykTbgD47LuqpdqndFf852eNneoM5xPbLSKsQE3GxI1pNg==',
    coupangUrl: 'https://link.coupang.com/a/iuhA3zFG44',
    naverUrl: null,
  },
  {
    rank: 5,
    name: '브라운 시리즈5 전기면도기',
    price: 89770,
    pros: '아빠. 매일 아침 쓰는 물건. 상위 시리즈보다 부담 적은 8만원대. 로켓배송.',
    imageUrl: 'https://ads-partners.coupang.com/image1/zlM-8IbWS6P07kmJzmCM0i9HHBdvpYbEpattuxDT87Cj4oMoPlq0oHJCJetX_jTk8ACsy7htc_b1uK0XKd2UftCIMnbSRUWbAc2LwTtL4Lt_xytCfjB6YmHDuF3CYkwafexU3-rTjelKNVC1os3dCnJXcmVZyC8Syrc4Gn28U0SsUc7Moc7QvMIGpUWOt_sMFAgmo9Z3DkFAPnrrIbuDFBPvRiJa-HnWA6z7sy6CD6UcRt59fDKpTKHKLVM758nI52Ef767-ZgZAR3f4PGYRRcSj6QU4cV5tAmv5h2d-r-OpfK6hpbmFevwQxbf4dtDxEe6DcExM0qRwFvE3GeDAVR46DOXDGSObtMRNO8kTTFq-JwXOuO-tRyMuqSCGqHh_Pl8laO0WiKBoUuWR0Rata3kVYvhkJnYStQgq2mWJpIrKmHqKXqfzgTKY9FM9aL_Jo7_IM3XL4I5VB4YSUzvr6vITY1t5NyeJqVAvyVonLLvYHKkDBagSzd1ij1zBWugV6Ua7TG11Pm0hrueLoSGLyxODHSM=',
    coupangUrl: 'https://link.coupang.com/a/iuhAgm4t3I',
    naverUrl: null,
  },
  {
    rank: 6,
    name: '하리보 크리스마스 어드벤트 캘린더',
    price: 25580,
    pros: '선물교환·마니또. 12월 1일부터 매일 한 칸씩. 11월 안에 주문, 유통기한 확인.',
    imageUrl: 'https://ads-partners.coupang.com/image1/WisUwS2bUFBCaH0TWur-hQqdLKLbwENOBP2dfRvZm_guYyQKeXfvORLCKqDHtzX6QP2iopV8Jo5xrHf1dfTKbvC8OL1zMF-BaeM4mt4mI6-oAS_cQWU2pW0U-MJiOATxYvQW3-9XmQhmtQQf9tEeVfZcBmEdsT6GMTGOMi3YJXpuA-KcHyLt7oZmo2oa5NVqzAkkEalbwiHp6Im-Y1amwkmHFqGzrR4NWg6P8ytDqP3YSFD9cD50gTa_UzqcPj-HugwqD-3p25YI-7SAAb1t1KiYK6L1Cfgh8Fp_zLXdmKrQ_mBE7-TmY2K1XIdGBtcuYFvaFacuD2afMWHqRzHFxlEy8Tmg3yWjavERsg6OAThhyhHKfdhG97e-9S8eaocJ2aijbqmxskrbWEtz1Hq6C_IE2-41C5VydLi6yptNokbujfZDGuA_fY2zAo9AWijsFZO8K829StY9DAizrrPTg-h_lndrhrkpha-EkGlqTnmePwJ-HQWu9-5sZnbq1AXhQIH80MyOwaEI7gSpC4oo9I8z2XZKciuUTf8bnllfLgIK3g==',
    coupangUrl: 'https://link.coupang.com/a/iuhAguT8yO',
    naverUrl: null,
  },
  {
    rank: 7,
    name: '홀리해요 크리스마스 육각형 워터 오르골 무드등 스노우볼',
    price: 22500,
    pros: '선물교환·마니또. 성별·나이 무관, 시즌 후에도 무드등으로 사용. 로켓배송.',
    imageUrl: 'https://ads-partners.coupang.com/image1/Ce3wmEaGqw7pNPW9CaD0B2zb9BhqQYWuTjH-YIuAQgGpVLb7G9S53ozqngl3mUx0Td7Z1o9wFfv5Lk9CPIsdY9RtlVPdVd4t-9edOU1O06g-y2bO_BHsiJ3Md9Vk-iNYtpbqMENbzGFUBiaEowCtwKkMpx-1fIckjSqGVP70ctRWZsbB9_Sgj4XhE8HPpWN60z0oCca4RFJgh9EIR1HUV34BPbns7-H3loVKvvsOgqrZUs2vneAMXmWfsCUhCu3_jsCj0Q6bmzwLTMDvNqd0XoF34zK2pv4JDluGApWiHwLryEj8bz5k-vF8mrwSf64NyyKmExDPMVdYGOO_UklNA0E0krLtKbq8WsuSA8FvxX9pDG_BdUQC6Us74nXq6pU5VZDsmVuL9HAApr6_DD4VJIQqyXMdXCITKm6pHiHwk6k5CxpEJPvUrTNkxmIXjna6OqBPTk8zX2khEc4t0AoFOv8tM-S-P1t_ttV3lQOYRNb5UOvEyRqUtYqvrNBOTjozbqRf7SgsPJS9cat-Tl97BVSczxeXkwNU2pBK1QfgSynrhGM5sdBU8gpLaHXB770R6R4O9XqC',
    coupangUrl: 'https://link.coupang.com/a/iuhAgAQQ0W',
    naverUrl: null,
  },
  {
    rank: 8,
    name: '레고 시티 크리스마스 캘린더 2026 60510',
    price: 39400,
    pros: '아이(만 5세~초등 저학년). 12월 1일부터 24일간 매일 한 칸씩. 11월 안에 준비. 로켓배송.',
    imageUrl: 'https://ads-partners.coupang.com/image1/sRct5RI_NW57GQ2NscLZEmd1wu0UPxnJxaENbzrwtZFlFJRO_p_H7KxILFFULr3ualYwhwtwS4MndA2nRRK7-qeKgtENZwwon8C0C2oUJwDzSiapK6NTiL41SdBaH5Ed84g-EZfOEpfHZ2aPpFiBnzrYb6tU5JjgyLwY1j7zk2J83qSWGOFuKIGreTMdXTotGup7kH74wI6I00Gzt3HUt3Wdpok0m0iZVmq1B7oGFPOh0lNO4b4N65dVVTFG8YlE9WpgJ2DflIOtexXev0iojJ0dWm2dwM7rV0O-vKSjwWolHPNNTILwEriZIhOlwEGqUt240cK-xMWHjn5aY8SROU73116lOPRXpQR_xZu5QXYdNIb_3glSh30XlV8v30dkFoS_tn3pTQNykZS9W6iR2A-yMbu3JGJHM8q3V6q7_uSlb7x8wZwAVpcg99jis6XKC-30DiYjsL-D7Kc1WQvp83O8_9HM9HSu3UzIdJIRpLkm0nblu3aeBL3l7jY_RhGi_Bh-NhEnPFNneCK4TfZ8n5M=',
    coupangUrl: 'https://link.coupang.com/a/itUZNGUO1A',
    naverUrl: null,
  },
];
