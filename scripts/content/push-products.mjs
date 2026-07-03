import { Client } from '@notionhq/client';

const notion = new Client({ auth: process.env.NOTION_API_KEY });
const GUIDES_DB_ID = process.env.NOTION_GUIDES_DB_ID;
const PRODUCTS_DB_ID = process.env.NOTION_PRODUCTS_DB_ID;

const SLUG = '12세-여자아이-생일선물';

const PRODUCTS = [
  {
    name: '레고 프렌즈 하트레이크 시티 아파트와 상점 42670',
    price: 159900,
    naverUrl: 'https://search.shopping.naver.com/catalog/59557782476',
    imageUrl: 'https://shopping-phinf.pstatic.net/main_5955778/59557782476.20260406093425.jpg',
    rank: 1,
    pros: '독립된 블로그 3곳에서 반복 언급된 스테디셀러. 고급 브릭 조립으로 몰입감이 높고, 완성 후에도 갖고 놀 수 있어 만족도가 오래갑니다.',
  },
  {
    name: '봉봉프렌즈 어린이 화장품 봉봉 메이크업박스 5종세트',
    price: 47560,
    naverUrl: 'https://search.shopping.naver.com/catalog/51652538619',
    imageUrl: 'https://shopping-phinf.pstatic.net/main_5165253/51652538619.20250102121122.jpg',
    rank: 2,
    pros: '꾸미기·화장에 관심이 생기기 시작하는 시기 심리와 정확히 맞아떨어지는 아이템. 키즈 전용 순한 성분이라 부모도 안심할 수 있습니다.',
  },
  {
    name: '다름인터내셔널 디알고 고양이귀 키즈 블루투스 스터디 헤드셋',
    price: 31150,
    naverUrl: 'https://search.shopping.naver.com/catalog/54067898167',
    imageUrl: 'https://shopping-phinf.pstatic.net/main_5406789/54067898167.20250411161909.jpg',
    rank: 3,
    pros: '"4세부터 12세까지 오래 쓸 수 있다"는 실사용 후기가 확인된 제품. 학습·인강용으로도 매일 쓸 수 있어 실용성이 높습니다.',
  },
  {
    name: '우정 예술 공예 팔찌 문자열 메이커 키트',
    price: 27300,
    naverUrl: 'https://smartstore.naver.com/main/products/13421887303',
    imageUrl: 'https://shopping-phinf.pstatic.net/main_9096639/90966397639.jpg',
    rank: 4,
    pros: '같은 카테고리 제품 실사용 후기에서 "대만족" 반응이 확인됐습니다. 완성한 팔찌를 직접 착용할 수 있어 성취감이 큽니다.',
  },
  {
    name: '디알고 어린이이어셋 청력보호 블루투스 골전도 키즈 이어폰',
    price: 19800,
    naverUrl: 'https://smartstore.naver.com/main/products/12247815836',
    imageUrl: 'https://shopping-phinf.pstatic.net/main_8979232/89792326552.jpg',
    rank: 5,
    pros: '위시리스트형 유튜브 댓글에서 최다 언급된 카테고리. 일반 이어폰 대신 골전도를 채택해 초등학생 안전성을 우선했습니다.',
  },
];

async function main() {
  const search = await notion.databases.query({
    database_id: GUIDES_DB_ID,
    filter: { property: 'slug', rich_text: { equals: SLUG } },
  });

  const guide = search.results[0];
  if (!guide) {
    console.error(`슬러그 "${SLUG}"를 가진 가이드를 찾지 못했습니다.`);
    process.exit(1);
  }

  console.log(`가이드 페이지: ${guide.id}`);

  // 기존 연결된 상품 삭제(재실행 대비)
  const existingProducts = await notion.databases.query({
    database_id: PRODUCTS_DB_ID,
    filter: { property: 'giftGuide', relation: { contains: guide.id } },
  });
  for (const page of existingProducts.results) {
    await notion.pages.update({ page_id: page.id, archived: true });
  }
  if (existingProducts.results.length > 0) {
    console.log(`기존 연결 상품 ${existingProducts.results.length}개 아카이브 완료`);
  }

  for (const product of PRODUCTS) {
    await notion.pages.create({
      parent: { database_id: PRODUCTS_DB_ID },
      properties: {
        Title: { title: [{ text: { content: product.name } }] },
        giftGuide: { relation: [{ id: guide.id }] },
        price: { number: product.price },
        naverUrl: { url: product.naverUrl },
        imageUrl: { rich_text: [{ text: { content: product.imageUrl } }] },
        rank: { number: product.rank },
        pros: { rich_text: [{ text: { content: product.pros } }] },
      },
    });
    console.log(`생성 완료: ${product.name}`);
  }

  console.log('\n완료: 상품 5건 입력');
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
