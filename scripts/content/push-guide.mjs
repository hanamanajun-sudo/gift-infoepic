import { Client } from '@notionhq/client';

const notion = new Client({ auth: process.env.NOTION_API_KEY });
const GUIDES_DB_ID = process.env.NOTION_GUIDES_DB_ID;

const SLUG = '12세-여자아이-생일선물';

const NEW_INTRO =
  '12세 여자아이는 초등학교 마지막 해를 보내며 취향이 뚜렷해지는 시기예요. ' +
  '친구들 사이 유행에 민감해지고 꾸미기·화장에 관심이 생기기 시작하지만, 아직 어린이다운 즐거움도 함께 갖고 있어요. ' +
  '실제 블로그 후기, 유튜브 댓글, 일본 커뮤니티 사례를 교차 검증해서 이 시기 아이들이 진짜 반응했던 선물만 골랐습니다.';

// ── 리치텍스트 헬퍼 ──────────────────────────────────────────────────────
const rt = (text, opts = {}) => [{ type: 'text', text: { content: text }, annotations: opts }];

const h2 = (text) => ({ object: 'block', type: 'heading_2', heading_2: { rich_text: rt(text) } });
const h3 = (text) => ({ object: 'block', type: 'heading_3', heading_3: { rich_text: rt(text) } });
const p = (text) => ({ object: 'block', type: 'paragraph', paragraph: { rich_text: rt(text) } });
const bullet = (text) => ({ object: 'block', type: 'bulleted_list_item', bulleted_list_item: { rich_text: rt(text) } });

function table(headerRow, rows) {
  const toRow = (cells) => ({
    object: 'block',
    type: 'table_row',
    table_row: { cells: cells.map((c) => rt(c)) },
  });
  return {
    object: 'block',
    type: 'table',
    table: {
      table_width: headerRow.length,
      has_column_header: true,
      has_row_header: false,
      children: [toRow(headerRow), ...rows.map(toRow)],
    },
  };
}

const BLOCKS = [
  h2('가격대별로 고르기'),
  table(
    ['예산', '추천 상품', '이유'],
    [
      ['2만원대', '골전도 키즈 이어폰', '부담 없이 줄 수 있는 실용템. 조카나 친척 아이에게도 무난'],
      ['3만원대', '고양이귀 블루투스 헤드셋 / 팔찌메이커 키트', '취향 갈림이 적고, 친구 선물로도 좋음'],
      ['5만원대', '키즈 메이크업박스 세트', '꾸미기에 관심 생긴 아이에게 특별한 느낌을 주는 선물'],
      ['15만원대', '레고 프렌즈 세트', '생일처럼 특별한 날, 오래 갖고 노는 고관여 선물'],
    ]
  ),
  h2('12세 여자아이 선물 고르는 법'),
  p('이 나이대는 취향이 아이마다 크게 갈리기 시작해요. 무작정 유행템을 고르기보다, 아이가 평소 뭘 좋아하는지 떠올려보고 아래 세 유형 중 가까운 쪽을 골라보세요.'),
  h3('꾸미기·화장에 관심 많은 아이라면'),
  p('키즈 메이크업박스나 액세서리 쪽이 좋습니다. 다만 실제 화장품보다 순한 성분의 키즈 전용 제품인지 꼭 확인하세요.'),
  h3('만들기·조립을 좋아하는 아이라면'),
  p('레고 프렌즈처럼 브릭 조립 난이도가 있는 세트나 팔찌메이커 같은 DIY 키트가 몰입도가 높습니다. 완성 후 실제로 쓰거나 착용할 수 있다는 점도 만족도를 높입니다.'),
  h3('아직은 실용템이 편한 아이라면'),
  p('무선이어폰이나 헤드셋처럼 학교·학원에서 매일 쓰는 물건을 선물하면 실패 확률이 낮습니다. 12세는 전자기기를 처음 갖기 시작하는 나이라 반응이 좋은 편이에요.'),
  h2('이건 사지 마세요'),
  bullet('여러 명이 겹쳐 줄 만한 소모품(핸드크림, 향수류)은 피하세요 — 이미 비슷한 걸 여러 개 받아서 쌓여 있을 확률이 높습니다.'),
  bullet('색상 호불호가 갈리는 코스메틱(립글로스, 틴트 등)은 무난한 색이나 투명 제품을 고르세요.'),
  bullet('"귀엽지만 어려 보이는" 유아틱한 캐릭터 디자인은 조심하세요. 12세는 어린이 취급받는 걸 싫어하는 나이라 오히려 실망할 수 있습니다.'),
  h2('자주 묻는 질문'),
  h3('12세 여자아이 생일선물 예산은 얼마가 적당한가요?'),
  p('2만원~6만원대가 무난하고, 특별한 날이면 10만원대 이상도 괜찮습니다. 매번 고가 선물을 하면 다음 해에 부담이 될 수 있어 적당한 선을 지키는 게 좋습니다.'),
  h3('취향을 잘 모르는 조카·친척 아이에게는 뭐가 좋을까요?'),
  p('호불호가 갈리는 캐릭터·색상 제품보다는 무선이어폰이나 문화상품권처럼 실용적이고 무난한 선택이 안전합니다.'),
  h3('형제자매가 있는 집이면 어떻게 하나요?'),
  p('팔찌메이커나 레고 같은 조립·DIY 키트는 형제 간 다툼 소지가 있으니, 1인용으로 명확히 구분되는 선물을 고르는 게 좋습니다.'),
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

  console.log(`가이드 페이지 발견: ${guide.id}`);

  // intro 갱신
  await notion.pages.update({
    page_id: guide.id,
    properties: {
      intro: { rich_text: rt(NEW_INTRO) },
    },
  });
  console.log('intro 갱신 완료');

  // 기존 본문 블록 삭제
  const existing = await notion.blocks.children.list({ block_id: guide.id });
  for (const block of existing.results) {
    await notion.blocks.delete({ block_id: block.id });
  }
  console.log(`기존 블록 ${existing.results.length}개 삭제 완료`);

  // 새 본문 추가 (100개 제한 고려 — 지금은 20개 내외라 한 번에 전송)
  await notion.blocks.children.append({ block_id: guide.id, children: BLOCKS });
  console.log(`새 블록 ${BLOCKS.length}개 추가 완료`);

  console.log('\n완료:', guide.id);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
