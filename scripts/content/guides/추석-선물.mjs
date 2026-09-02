import { h2, h3, p, bullet, table } from '../lib.mjs';

export const slug = '추석-선물';

export const intro =
  '추석 선물은 "무엇을 살까"보다 "얼마짜리를 드려야 실례가 아닐까"에서 더 오래 막힙니다. ' +
  '네이버 블로그와 유튜브 댓글에서 추석 선물 이야기를 모아보니 가장 많이 언급된 건 현금과 상품권이었고, ' +
  '실물 선물 중에서는 홍삼·한우·과일 순이었습니다. ' +
  '여기에 한국의 추석과 성격이 거의 같은 일본의 명절 선물 관습(お歳暮) 조사를 교차 확인했습니다. ' +
  '받아서 기뻤던 선물 1위가 육류·햄, 2위 해산물, 3위 과일이었고, ' +
  '"내 돈으로는 안 사는 고급 식품"을 원한다는 응답이 47.5%로 가장 높았습니다. ' +
  '이 두 자료를 바탕으로 1만원대부터 9만원대까지, 관계별로 나눠서 정리했습니다.';

export const blocks = [
  h2('가격대별로 고르기'),
  table(
    ['예산', '추천 상품', '어떤 관계에 맞나'],
    [
      ['1만원대', '견과 선물세트 4종', '직장 동료·이웃, 여러 명에게 돌려야 할 때'],
      ['2만원대', '꿀 유자차 세트 / 스팸 햄 세트', '어르신, 자취하는 형제, 실용성을 보는 집'],
      ['3만원대', '홍삼 선물세트 / 사과·배 혼합세트', '부모님·시부모님 기본 구간'],
      ['5만원대', '영광굴비 선물세트', '처가·시가 첫 명절, 예의를 갖춰야 하는 자리'],
      ['9만원대', '한우 1++ 구이용 선물세트', '직장 상사·거래처, 부모님께 크게 드릴 때'],
    ]
  ),

  h2('추석 선물 추천 TOP 7'),

  h3('부모님 선물의 기본값 "한삼인 홍삼 대보 선물세트 2호"'),
  p(
    '수집한 블로그·유튜브 댓글에서 현금과 상품권 다음으로 많이 언급된 품목이 홍삼이었습니다. ' +
    '33,900원이고 쇼핑백이 포함돼 있어 따로 포장할 필요가 없습니다. 로켓배송이라 명절 직전에 주문해도 도착 날짜를 맞추기 쉽습니다. ' +
    '이럴 때 맞습니다: 부모님이나 시부모님께 무난하게 드리고 싶고, 예산을 3만원 안팎으로 잡았을 때. ' +
    '다만 건강기능식품은 이미 드시는 제품이 있을 수 있어, 복용 중인 것이 있는지 한 번 확인하는 편이 낫습니다.'
  ),

  h3('실패 확률이 가장 낮은 선택 "프리미엄 사과배혼합 과일선물세트"'),
  p(
    '일본 お歳暮 조사에서 과일·농산물이 "받아서 기뻤던 선물" 3위였고, 한국 추석에서는 사과와 배가 차례상 품목과 겹쳐 쓰임이 더 분명합니다. ' +
    '33,900원. 이럴 때 맞습니다: 상대의 취향을 잘 모르거나, 여러 집에 같은 선물을 돌려야 할 때. ' +
    '신선식품이라 수령 날짜를 먼저 정해야 하고, 명절 직전에는 배송이 몰리므로 여유를 두고 주문하세요.'
  ),

  h3('두고두고 쓰는 실용 선물 "스팸 8호 햄 통조림 세트"'),
  p(
    '일본 조사에서 "받아서 기뻤던 선물" 1위가 육류·햄이었습니다. 한국에서도 통조림 햄 세트는 명절 선물의 오래된 기본값입니다. ' +
    '27,890원에 쇼핑백이 포함되고 로켓배송이 됩니다. 유통기한이 길어 바로 쓰지 않아도 부담이 없다는 점이 이 선물의 핵심입니다. ' +
    '이럴 때 맞습니다: 자취하는 형제, 이웃, 실용성을 중시하는 집.'
  ),

  h3('2만원 아래에서 격식을 갖추는 "다반사 4종 견과 선물세트 골드 1호"'),
  p(
    '16,400원, 710g 4종 구성이고 로켓배송입니다. ' +
    '이럴 때 맞습니다: 직장 동료나 이웃처럼 여러 명에게 같은 선물을 돌려야 해서 1인당 예산이 2만원 아래일 때. ' +
    '견과는 보관이 쉽고 호불호가 적어 여러 명에게 나눠 드리기에 적합합니다. 다만 견과 알레르기가 있는 집에는 피하세요.'
  ),

  h3('부담을 덜어주는 선택 "꽃샘 꿀 유자차 모과차 명절선물세트"'),
  p(
    '22,800원. 이럴 때 맞습니다: 어르신께 드려야 하는데 건강식품은 이미 여러 곳에서 받으실 것 같고, ' +
    '그렇다고 빈손으로 가기는 어려운 자리. ' +
    '차는 상대가 바로 소비하지 않아도 부담이 없고, 냉장 보관이나 조리가 필요 없다는 점이 장점입니다.'
  ),

  h3('격식이 필요한 자리 "명가 영광굴비 선물세트 10미"'),
  p(
    '59,900원. 일본 조사에서 해산물이 2위였고, 한국 명절에서 굴비는 격식을 갖춘 선물로 오래 통용돼 왔습니다. ' +
    '이럴 때 맞습니다: 처가나 시가에서 맞는 첫 명절이거나, 거래처에 예의를 갖춰야 할 때. ' +
    '냉장·냉동 보관이 필요하므로 상대가 받을 수 있는 날짜를 반드시 먼저 확인하세요. 빈집에 도착하면 선물이 상합니다.'
  ),

  h3('예산이 넉넉할 때 "투뿔 1++ 특수부위 한우선물세트 구이용 1kg"'),
  p(
    '92,300원. 일본 조사에서 "내 돈으로는 안 사는 고급 식품"을 받고 싶다는 응답이 47.5%로 가장 높았는데, ' +
    '한우 선물세트가 정확히 그 자리에 있는 품목입니다. ' +
    '이럴 때 맞습니다: 직장 상사나 거래처처럼 5만~10만원대가 관례인 관계이거나, 부모님께 특별히 크게 드리고 싶을 때. ' +
    '냉장 배송이라 수령 날짜 확인이 필요합니다.'
  ),

  p('이 목록은 관계별 예산 구간(1만원대~9만원대)과 보관·배송 조건을 기준으로 정리했습니다.'),
  bullet('마지막 상품 정보 확인일: 2026-09-03'),
  bullet('확인한 정보: 상품명·가격·구성·배송 유형'),
  bullet('제외 기준: 상대의 취향을 알아야 고를 수 있는 품목(주류·화장품), 보관 조건이 까다로운 품목'),
  bullet('제휴 고지: 일부 링크를 통해 구매하면 수수료를 받을 수 있으나, 수수료는 추천 순서에 영향을 주지 않습니다.'),

  h2('얼마짜리를 드려야 실례가 아닐까'),

  h3('부모님·시부모님은 3만원 안팎이 기준입니다'),
  p(
    '일본의 같은 관습에서 부모·시부모에게 보내는 명절 선물의 기준 금액은 3,000엔 안팎으로, 한국 돈으로 3만원 정도입니다. ' +
    '평소 자주 뵙지 못하거나 특별히 신세를 진 해에는 5,000엔(약 5만원)까지 올리는 것이 일반적이라고 정리돼 있습니다. ' +
    '한국의 추석도 구조가 같아서, 3만원대 홍삼·과일 세트가 가장 두껍게 팔리는 구간입니다.'
  ),

  h3('직장 상사·거래처는 5만~10만원이 관례입니다'),
  p(
    '상사에게 보내는 경우는 일반 기준보다 높은 5,000~10,000엔(약 5만~10만원)으로 잡습니다. ' +
    '다만 회사에 따라 직원 간 선물을 금지하는 곳이 있으므로, 보내기 전에 사내 규정을 확인하라는 조언이 함께 붙습니다. ' +
    '한국에서도 공직자나 특정 업종은 청탁금지법상 금액 제한이 있으니, 상대의 직군을 먼저 확인하세요.'
  ),

  h3('비싸다고 좋은 게 아닙니다'),
  p(
    '이 부분이 가장 자주 틀리는 지점입니다. 여러 자료가 공통적으로 "지나치게 비싼 선물은 상대에게 부담을 지워 오히려 실례가 된다"고 못 박습니다. ' +
    '받는 사람이 답례를 걱정하게 만드는 순간, 선물의 목적이 어긋납니다. ' +
    '관계에 맞는 구간 안에서 고르는 것이, 같은 예산으로 한 단계 위 등급을 사는 것보다 낫습니다.'
  ),

  h2('현금과 상품권은 어떤가요'),
  p(
    '솔직히 말하면, 이번에 모은 자료에서 가장 많이 언급된 건 현금과 상품권이었습니다. ' +
    '실물 선물보다 압도적으로 많았습니다. 받는 쪽에서 필요한 데 쓸 수 있으니 당연한 결과입니다.'
  ),
  p(
    '그럼에도 실물 선물을 고르는 이유는 대개 "성의가 없어 보일까 봐"입니다. ' +
    '이럴 때 쓰는 방법이 하나 있습니다. 부모님께는 현금을 드리되 2만원대 실물 선물을 하나 얹는 것입니다. ' +
    '금액의 실질은 현금이 가져가고, 명절에 빈손으로 가지 않았다는 형식은 실물이 채웁니다. ' +
    '반대로 거래처나 상사처럼 현금이 곤란한 관계에서는 실물이 유일한 선택지가 됩니다.'
  ),

  h2('이건 사지 마세요'),
  bullet('상대의 취향을 모르는 상태의 주류·화장품은 피하세요 — 술은 못 마시는 경우가 있고, 화장품은 피부 타입을 알아야 고를 수 있습니다.'),
  bullet('받을 사람이 집에 없는 날짜로 신선식품을 보내지 마세요 — 굴비·한우·과일은 배송 당일 수령이 전제입니다. 명절 연휴에 걸치면 상합니다.'),
  bullet('건강기능식품을 중복으로 드리지 마세요 — 홍삼·비타민은 이미 여러 곳에서 받으시는 경우가 많습니다. 복용 중인 제품이 있는지 먼저 확인하세요.'),

  h2('자주 묻는 질문'),

  h3('추석 선물은 언제 보내야 하나요?'),
  p(
    '연휴 시작 1~2주 전에 도착하도록 잡는 것이 무난합니다. 신선식품은 특히 그렇습니다. ' +
    '연휴에 임박하면 배송이 몰려 날짜를 맞추기 어렵고, 상대도 집을 비우는 경우가 많습니다. ' +
    '로켓배송 상품은 상대적으로 여유가 있지만, 명절 성수기에는 평소보다 하루 이틀 더 걸린다고 보는 편이 안전합니다.'
  ),

  h3('시부모님과 친정 부모님께 같은 금액을 드려야 하나요?'),
  p(
    '일반적으로는 같은 수준으로 맞추는 쪽이 뒷말이 없습니다. 품목까지 똑같을 필요는 없고, 예산 구간만 맞추면 됩니다. ' +
    '한쪽이 건강식품을 이미 많이 드신다면 그쪽만 과일이나 굴비로 바꾸는 식으로 조정하세요.'
  ),

  h3('거래처 선물은 얼마가 적당한가요?'),
  p(
    '5만~10만원 구간이 일반적입니다. 다만 상대가 공직자이거나 청탁금지법 적용 대상 업종이면 금액 제한이 따로 있으므로, ' +
    '보내기 전에 상대 회사의 수령 규정을 확인하는 것이 안전합니다. 확인이 어렵다면 보내지 않는 편이 낫습니다.'
  ),

  h3('선물세트 대신 직접 고른 물건을 보내도 되나요?'),
  p(
    '가까운 사이라면 괜찮습니다. 다만 격식이 필요한 관계에서는 명절 포장이 된 선물세트가 무난합니다. ' +
    '포장 자체가 "명절 인사"라는 형식을 대신 전달하기 때문입니다. ' +
    '쇼핑백이 포함된 상품인지 확인해두면 따로 준비하는 수고를 덜 수 있습니다.'
  ),

  h2('관련 가이드'),
  bullet('설날 선물: 같은 명절 선물이지만 시기와 품목이 조금 다릅니다'),
  bullet('부모님 선물 고르는 법: 명절이 아닌 때의 기준'),
  bullet('5만원 이하 선물만 비교하기'),
  bullet('10만원 이하 선물만 비교하기'),
];

export const products = [
  {
    rank: 1,
    name: '한삼인 홍삼 대보 선물세트 2호 + 쇼핑백',
    price: 33900,
    pros: '수집한 여론에서 실물 선물 중 가장 많이 언급된 품목. 쇼핑백 포함이라 별도 포장이 필요 없고 로켓배송으로 날짜 맞추기 쉽습니다.',
    imageUrl: 'https://ads-partners.coupang.com/image1/T4E3jp87yWtW88B1T0Sh46dYeyWtWPqdrKyOksU1c_HyNsvB7qEpb0vyVXi7YN7GndMUlMjPbhlCiJZLcE0xprHw3pqfMwgVIsQqHpWN7GaoW4m92zkdaK7Rzth85fWS9XEgHcQBYpIOQxSLKMMsoE0dQpj0Ul7Ssp0P-JHLva1jbvSyT-fLfP9o7AAo2d837aSeHFUZShe7eWM1nmWkrKTfVXFgLDqAO3kjUP8p2XQ5sODoL8JE409amJfhQ3s9NxvFvajk8Y68rRsxUlZcxiXJniR83YyEx8F3dFdZ-uVgTi_BsXW6zNi2u_CaP0DH5_S25Mkz-_V4I-DstFvB6NTO1QcH72H1yZ2R0R8n40Qtg0wcVY2ZRKAoncMDEbaXq2eKDrROULP4sg5XOfdTr6EMQbzC9PYA_UR8AMQldEu33rnyWhUF0zWcGWkMCLdUiLkqiKHKg3anB0b29fua2IP7k9cmyNKvpsNtmS97cDYFjY98cDNk0l2z0i68H1pR9cRm33SzFvQo391KsA==',
    coupangUrl: 'https://link.coupang.com/re/AFFSDP?lptag=AF2072433&pageKey=6320091400&itemId=13167459817&vendorItemId=80426151399&traceid=V0-153-28465165eaf7bd27&requestid=20260903001821620019617705&token=31850C%7CGM&pt=0&slot=7',
    naverUrl: null,
  },
  {
    rank: 2,
    name: '[감사를 전하는] 프리미엄 사과배혼합 과일선물세트',
    price: 33900,
    pros: '취향을 몰라도 실패하지 않는 구성. 여러 집에 같은 선물을 돌려야 할 때 무난합니다. 신선식품이라 수령 날짜만 미리 정하세요.',
    imageUrl: 'https://ads-partners.coupang.com/image1/klJ3Mpk8jetpz_Nukqz4SV41c7YBxqpd9Cho_51v58U3usuZuRLs6iUGDRGSGIV7NGTx2MwnBClp8PsGf31qUSNyGhg7DRJRCYFfhjW2flpyEJXuL0bqVQKPeeYr58tYc3GGkT6HxmkqnGphVKr5HXDP6WbGVSfrx68dzknRsb5C2re1lVdMHu62lsonx-ZjYgkaM5UfKaGP1soapEyggpk07Qihl2QuP0TMm_bDu3VDkKjj_BtLE2er3pCF34b8-TFbxOVY_JYqmHg5oxgSpAjGSmhiltZZps3YddLgIx6z4Qvto-GWdtCo6d75jctXZ4_vfEJXuuv_7G3UpCTPqYBUoQbEUBkVO2abaI4AO1t1UmhiYhHtfZwgvu7eG-2Of5bYjBr0R0HAa6Jtn3P2UOuh7UoueIMh-g8_yMUHnPWRH3cu7xyenGvlHUx5guurfekquaV5Ki52M75y8pYmqRDRY_Jq4gI9GQfyZppd7-LnrIAqCRvP5JiBpfQnhEIACssoPd_k6gJHkkTDXBbzlY9h5r2HOCZr34--jIXxVWyx_HSVFK7VUQ==',
    coupangUrl: 'https://link.coupang.com/re/AFFSDP?lptag=AF2072433&pageKey=9707809949&itemId=29043979478&vendorItemId=95971001079&traceid=V0-153-b881edad4360fb25&requestid=20260903001823266152404509&token=31850C%7CMIXED&pt=0&slot=6',
    naverUrl: null,
  },
  {
    rank: 3,
    name: '스팸 8호 햄 통조림 세트 + 쇼핑백, 1세트',
    price: 27890,
    pros: '유통기한이 길어 바로 쓰지 않아도 부담이 없습니다. 쇼핑백 포함, 로켓배송. 자취하는 형제나 이웃에게 적합합니다.',
    imageUrl: 'https://ads-partners.coupang.com/image1/G9Gq53GcpZwrQuaqG7vvcOsIMM3tMQxK64MpwXCU3aFgF3vQAJ24-tASFluJMr4kz_CyrXyFoHFoQLbiDBmuAZCj4zHligCn3dBA1DReCglv4X57NW_XEsiTB2XAAtEIY8soA7ahCnTpF2OQf3lJiE-9kE1Xn6oGBi6JV2DpQrevTcUHLsceKxMFUxJTJHdlyjP-Q99CPR0zbKHOP-Eg_log0MJZezmXBvtxM1tmRAhG9HfT7gNARLExD7apBBhIEdpw98oSirdO7dorY6K9mpvzzxh4rwjx8nIJ-A0dXFCTBadZ4AzxKZrYTKa8h3XImm-kqzk63DXY1tWdGI3qrkWQXMuvq93xl6LTMkENRmnwhr3fVtauoH-nctnE2_KlPJLFJ4b0opTx1f7XeoHJbzs4HkzWKnaVz9ZiZZRXfb6mlAyrLijELbB47s7kvQS31cw5CRN2VLlHNdftyRZIEIq49aR21UGoing0NsJVdoKC1BTU-GjU4Nfc97I_RQQdRaTphXdYAslroU8=',
    coupangUrl: 'https://link.coupang.com/re/AFFSDP?lptag=AF2072433&pageKey=2171131275&itemId=21340320525&vendorItemId=95699496368&traceid=V0-153-ceea590e51f1f22b&clickBeacon=8cc83720-a6e1-11f1-b0c3-54d8c2e24f23%7E3&requestid=20260903001828408303176037&token=31850C%7CMIXED&pt=1&slot=1',
    naverUrl: null,
  },
  {
    rank: 4,
    name: '다반사 4종 견과 선물세트 골드 1호 710g, 1세트',
    price: 16400,
    pros: '2만원 아래에서 명절 포장을 갖출 수 있는 구성. 보관이 쉽고 호불호가 적어 여러 명에게 나눠 드리기 좋습니다.',
    imageUrl: 'https://ads-partners.coupang.com/image1/upALOvpJzsK0nSy4ukvpwEe7JimqffAZyMkEO-iMnhF65usFCUd_MroI4_lMZsRJRSKKWDdmndroTc0O0Hy0TR-8DAy3akl1ieXWifDRLSDAzHdq-FM4UMDcw0kr1zfdDBl3C-vDkH4MpwOXj80vLa6y1rw_zKGoEuVea6fMGhIRxDeq7xmsejAV47CqHRd4fyrHj2KhGOkoCDaa9sb1pAFqR7IHbzIRbQ0UROBCk3SHZThk7V6j5ae4lcjOgBwkqq3_JqGrhQ6mdJuFmiHT9HUCaRVsk7xXlhGpYefCfVyYJbLO30vyNCMLVlXm2oqcfs5R96IZiEwRtT50H4IkjYi2jwY9yP1HuqePMB5kOd02NlIfOF_fIDyXFnfPztCsAwdLU_KN7wUQYX2EYP7yxx-wtLtsHw-_IcHK5gz8nk-H5LIdBFQsFXseedPpeIKYJlFpudW0BN89EDjs1tcB6MaQfuaR-JJJL7dMie4Tl0Kmd9bWBgXKsBA4wEIxZORlMT62o4eJE4Ll4QnCcNm99CMAmfqn-5RCGZGtt5z36KcCw8IsbQ==',
    coupangUrl: 'https://link.coupang.com/re/AFFSDP?lptag=AF2072433&pageKey=7826376778&itemId=21272824673&vendorItemId=79580504534&traceid=V0-153-fb3536d7d8a660c3&clickBeacon=8bc93db0-a6e1-11f1-9913-732a0abf4fec%7E3&requestid=20260903001826746155964864&token=31850C%7CMIXED&pt=1&slot=1',
    naverUrl: null,
  },
  {
    rank: 5,
    name: '꽃샘 꿀 유자차 모과차 명절선물세트',
    price: 22800,
    pros: '건강식품이 겹칠까 걱정될 때의 대안. 바로 소비하지 않아도 부담이 없고 냉장 보관이나 조리가 필요 없습니다.',
    imageUrl: 'https://ads-partners.coupang.com/image1/WP4rTdVS-DRvP7bXWFBkp65Kvrch1Gw7oDoNeyBqeKCrlK4cesTBrarVG7p2uSHFTqfmnx_xzbDv5bXd1wQGyxjiWR_R48ep6g1XmKDcIAt7k1XkZJ8cT1Vr_ibYIne8bMwNkGoUb4QbzJzQBGolrDS_rBh2Ty-X8nV1hNuxnAnL6iAi0-xGSJ-x8diaxd5qkTZoetC3YWiA20fADApjVH1n1vxsZoGdghtoJ8BzlTCFRX6YTj1wY_Gkkjx_fryfNwUo2oRFu7U02MCJmYohnPa3XAsltKzxCnDJJYN_ArepAoyonUeXIF4_xYFJ7qOfRPFRSWMgmYOgQBFNGOvLNhrM9Ss36yZrhcRdBUSOX5nIjAeAAWnXOhZfceUtRAkXuAoASKR9C9JNImzycO9dP1JTzYkrCMSrfj-tMhATmUD7SOc9ZFdX4OStz6g0nOLVhk-8bCjPb5U2learjLjIWPGahigQQs6kXTWVJ2V_GsLsLR0-0PfqcQO91VyGARBCilzwbE-rstqzl2v2qT0E7in5E8_mNp57p-1xHZxhpoK-TofJWCY=',
    coupangUrl: 'https://link.coupang.com/re/AFFSDP?lptag=AF2072433&pageKey=9706059093&itemId=29037706130&vendorItemId=95964978247&traceid=V0-153-07cdad3032ca621a&requestid=20260903001830178112618726&token=31850C%7CMIXED&pt=0&slot=6',
    naverUrl: null,
  },
  {
    rank: 6,
    name: '명가 영광굴비 선물세트 10미 - 설 추석 명절선물세트, 거래처선물',
    price: 59900,
    pros: '격식이 필요한 자리에 오래 통용돼 온 품목. 냉장·냉동 보관이라 상대가 받을 수 있는 날짜를 먼저 확인해야 합니다.',
    imageUrl: 'https://ads-partners.coupang.com/image1/klO1Z9KnjeVF9hxZkghEues3GmSbHZkr1EUEj3C_kBPrRadVCiulN0NbQ4fUhfhQQzga9Bun8qJluYNH6wus3jipgtJnQVY_n-d2aWadACWHz6QOTrf5t7oGe1yL_da1byDrhQJLhFll-ugh-agSdC7jgWUC29R8du1kBeNeHd1qHVQ_PZiicLCx6Mnam35rOjsnizSdnrNLA9g6Ov1Ez-1lqGH2CYfWnLSoGN8AZlCI6KEZV93WPKkFb_MvNY5MTy-tCjBKAkR7BySHa1xKZgdAgIbQctiyKtiP1d__I_Qwd_8VlF4jjuUlvtZY5MFxdMZBWEcqAcTygMouE9o_FN_W-tO5YacMlzKnSwyFx2qL1W3wO19SpmaeDdPJ9-DWOgQxDmPV8eIgTPd5hxPQ7AcDjoEwTjkQBKeIZs0fZ5925aFtLSE4Ej3OfDKx7-GJs4vhqCVl-vU9hDtdzk-dNhDRVVU7kKltRAC13eeOGBPnZpm0_b2GRTo60n2Ux6l7XhkprQYTsZPO0xQZJfcKNaaLaRBpzkYzOXwLlREFeCA1jqVpFHQL5w==',
    coupangUrl: 'https://link.coupang.com/re/AFFSDP?lptag=AF2072433&pageKey=9344497585&itemId=27715592190&vendorItemId=94677048531&traceid=V0-153-32371eb403046dba&requestid=20260903001825070116401127&token=31850C%7CMIXED&pt=0&slot=5',
    naverUrl: null,
  },
  {
    rank: 7,
    name: '투뿔 1++ 특수부위 한우선물세트 구이용 1kg',
    price: 92300,
    pros: '"내 돈으로는 안 사는 고급 식품"에 정확히 해당하는 품목. 상사·거래처처럼 5만~10만원대가 관례인 관계에 맞습니다.',
    imageUrl: 'https://ads-partners.coupang.com/image1/B-4o_n6FbMOr5IzaB6iqiX4t5ZZV7XurQjAWO2mO0J8PfUHIqpHQeQp4oZT4EtX-n3utjGGwwpzj6mhwdgLrSTIEqnI_lJc-HKQGw1KIheNXnuFj5z9s9OuAo14Eyg20qEo5dF27BDrVTidNgyq2S__yKHuzWa4ZjdEIqrAwwow5eQ-08kjhhehztzL0_kaR3wEsmR_FpZlL0RW3uxOBo5qfkqtvD0o9LsPyfJaV6mC82uiyStBFsCRHh3XfUNY_uQ1CGxLRA42h-WFY0Fpf_uv6TI3F6xPdGqhtcfqxER9fVnJVZ4tnwU9r2O0lJ6vBFxFsrW9NlFxWj7Bjn_7fFR9Jh2tCPFLjFbBIEzo4bUGpFVdkZc9FJodkFACFitpErfsMW5KST25M_-nji-_VCjb6Mzz6rgr5H_a6OMx5Xmnti5DybMWBz94UrTYrcPc-hYLHmPINRTohlVbTsZ5GM1O6udnFxbemXfNIrB9LvFVR5R_UJpJYrjKWTNZXEM6wKMAqKlGEDltS9KtDNDhU7U6vjtkrhhQNayKYJSmLz3j5Tux4vJI=',
    coupangUrl: 'https://link.coupang.com/re/AFFSDP?lptag=AF2072433&pageKey=9030867126&itemId=26489389779&vendorItemId=93471007313&traceid=V0-153-779d68169f005ca0&requestid=20260903001819982304099061&token=31850C%7CMIXED&pt=0&slot=7',
    naverUrl: null,
  },
];
