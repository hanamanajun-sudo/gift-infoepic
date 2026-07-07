import { h2, h3, p, bullet, table } from '../lib.mjs';
export const slug = '남동생-생일선물';
export const intro = '남동생 생일선물, 형이나 누나로서 고민되시죠. 너무 아껴주는 티 내기 싫고, 그렇다고 쿨한 척 너무 던져주는 것도 아니고. 10대부터 20대까지 폭넓게 통하는 선물을 골랐습니다. 네이버 블로그와 유튜브 댓글 데이터를 교차 검증했습니다.';
export const blocks = [
  h2('가격대별로 고르기'),
  table([['예산','추천 상품','이유']],[['1만원대','피규어 키캡 굿즈','가벼운 마음에 주는 귀여운 선물'],['2~4만원대','카드지갑 / 백팩 / 보조배터리','실용템, 매일 쓰는 형/누나의 마음'],['6~9만원대','게임패드 / 무선이어폰','프리미엄 선물, 남동생 감동']]),
  h2('남동생이 진짜 좋아하는 선물 TOP 6'),
  h3('프리미엄 사운드 "낫싱 이어 A 무선 이어폰"'),p('10대부터 20대까지 폭넓게 통하는 무선 이어폰은 남동생 선물의 정석입니다. 낫싱 이어 A는 노이즈캔슬링까지 갖춘 90,400원의 가성비템으로, 투명한 디자인이 10~20대 취향을 정확히 저격합니다.'),
  h3('게임 마니아 "게임패드 컨트롤러"'),p('게임을 좋아하는 남동생에게 게임패드만 한 선물이 없습니다. PC와 닌텐도 스위치에서 모두 사용 가능한 59,000원의 게임패드는 남동생의 게임 실력을 한 단계 업그레이드해줍니다.'),
  h3('형/누나의 마음 "소가죽 카드지갑 각인"'),p('남동생에게 첫 브랜드 지갑을 선물해보세요. 21,900원의 소가죽 카드지갑에 이니셜을 각인하면 형/누나의 마음이 담긴 특별한 선물이 됩니다.'),
  h3('학생·직장인 모두 "경량 노트북 백팩"'),p('중학생부터 대학생, 사회초년생까지 모두 사용할 수 있는 경량 백팩은 39,800원의 가성비로 매일 쓰는 실용템입니다.'),
  h3('취미 저격 "피규어 키캡 굿즈 세트"'),p('부담 없는 9,900원의 가격으로 남동생의 취미를 저격하세요. 키보드에 올려놓는 피규어 키캡은 10~20대 남성 사이에서 인기 있는 굿즈입니다.'),
  h3('데일리 필수 "삼성 보조배터리 10000mAh"'),p('39,600원의 삼성 보조배터리는 남동생이 매일 사용하는 필수템입니다. C타입 초고속 충전으로 스마트폰·이어폰·태블릿까지 모두 충전 가능합니다.'),
  h2('남동생 선물 고르는 법'),p('가장 중요한 것은 "부담 없는 가격"과 "형/누나의 센스"입니다. 너무 비싸면 남동생이 부담스러워하고, 너무 싸면 서운해합니다.'),
  h2('자주 묻는 질문'),h3('예산?'),p('1만원~9만원대'),h3('1순위?'),p('낫싱 이어 A(90,400원)나 카드지갑(21,900원).'),
];
export const products=[
  {name:'낫싱 이어 A 노이즈캔슬링 무선 이어폰',price:90400,naverUrl:'https://smartstore.naver.com/main/products/10629049514',imageUrl:'https://shopping-phinf.pstatic.net/main_8817355/88173555324.1.jpg',rank:1,pros:'10~20대 통하는 프리미엄. 투명 디자인.'},
  {name:'제닉스 타이탄 GP7 게임패드 컨트롤러',price:59000,naverUrl:'https://search.shopping.naver.com/catalog/58980510242',imageUrl:'https://shopping-phinf.pstatic.net/main_5898051/58980510242.20260220101203.jpg',rank:2,pros:'PC+닌텐도 호환. 게임 최적.'},
  {name:'소가죽 카드지갑 이니셜 각인 선물포장',price:21900,naverUrl:'https://smartstore.naver.com/main/products/5381279761',imageUrl:'https://shopping-phinf.pstatic.net/main_8292577/82925772864.1.jpg',rank:3,pros:'형/누나의 마음 각인.'},
  {name:'경량 노트북백팩 학생 직장인 남성',price:39800,naverUrl:'https://smartstore.naver.com/main/products/11218360908',imageUrl:'https://shopping-phinf.pstatic.net/main_8876287/88762871239.3.jpg',rank:4,pros:'학생·직장인 모두 OK.'},
  {name:'토이스토리 키캡 굿즈 피규어 세트',price:9900,naverUrl:'https://smartstore.naver.com/main/products/13520375950',imageUrl:'https://shopping-phinf.pstatic.net/main_9106488/91064886302.jpg',rank:5,pros:'가벼운 취미 선물.'},
  {name:'삼성 보조배터리 10000mAh C타입 고속',price:39600,naverUrl:'https://smartstore.naver.com/main/products/13342050435',imageUrl:'https://shopping-phinf.pstatic.net/main_9088656/90886560767.2.jpg',rank:6,pros:'데일리 필수템.'},
];
