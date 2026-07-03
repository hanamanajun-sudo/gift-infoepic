"""Notion에 10세-남자아이-생일선물 가이드 반영"""
import os, json, urllib.request, re, unicodedata

project = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Read .env
with open(os.path.join(project, '.env')) as f:
    for line in f:
        line = line.strip()
        if '=' in line and not line.startswith('#'):
            k, v = line.split('=', 1)
            os.environ[k.strip()] = v.strip().strip('"')

KEY = os.environ['NOTION_API_KEY']
GUIDES_DB_ID = os.environ['NOTION_GUIDES_DB_ID']
PRODUCTS_DB_ID = os.environ['NOTION_PRODUCTS_DB_ID']

HEADERS = {
    'Authorization': f'Bearer {KEY}',
    'Notion-Version': '2022-06-28',
    'Content-Type': 'application/json'
}

def notion(method, path, body=None):
    url = f'https://api.notion.com/v1/{path}'
    data = json.dumps(body, ensure_ascii=False).encode('utf-8') if body else None
    req = urllib.request.Request(url, data=data, headers=HEADERS, method=method)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())

# Find the guide
print("=== 가이드 검색 ===")
result = notion('POST', f'databases/{GUIDES_DB_ID}/query', {
    'filter': {'property': 'slug', 'rich_text': {'equals': '10세-남자아이-생일선물'}}
})
guide = result['results'][0]
guide_id = guide['id']
print(f"가이드 ID: {guide_id}")
title = guide['properties']['Title']['title'][0]['plain_text']
print(f"타이틀: {title}")

# Update intro
intro_text = (
    '10세 남자아이는 초등 3~4학년으로, 활동적인 놀이와 만들기를 좋아하면서도 '
    '게임·전자기기에 관심이 생기기 시작하는 과도기예요. '
    '장난감을 점점 안 갖고 노는 것 같지만, 막상 받으면 하루 종일 가지고 노는 나이이기도 합니다. '
    '네이버 블로그 실제 후기와 유튜브 댓글, 일본 커뮤니티 사례를 교차 검증해서 '
    '이 나이 아이들이 진짜 좋아했던 선물만 골랐습니다.'
)
nfc_intro = unicodedata.normalize('NFC', intro_text)
notion('PATCH', f'pages/{guide_id}', {
    'properties': {
        'intro': {
            'rich_text': [{'type': 'text', 'text': {'content': nfc_intro}}]
        }
    }
})
print("intro 갱신 완료")

# Delete existing blocks
existing = notion('GET', f'blocks/{guide_id}/children')
for block in existing['results']:
    notion('DELETE', f'blocks/{block["id"]}')
print(f"기존 블록 {len(existing['results'])}개 삭제 완료")

# Build new blocks
def rt(text):
    return [{'type': 'text', 'text': {'content': unicodedata.normalize('NFC', text)}}]

def h2(text):
    return {'object': 'block', 'type': 'heading_2', 'heading_2': {'rich_text': rt(text)}}

def h3(text):
    return {'object': 'block', 'type': 'heading_3', 'heading_3': {'rich_text': rt(text)}}

def p(text):
    return {'object': 'block', 'type': 'paragraph', 'paragraph': {'rich_text': rt(text)}}

def bullet(text):
    return {'object': 'block', 'type': 'bulleted_list_item', 'bulleted_list_item': {'rich_text': rt(text)}}

def table(header, rows):
    def to_row(cells):
        return {'object': 'block', 'type': 'table_row', 'table_row': {'cells': [[{
            'type': 'text', 'text': {'content': unicodedata.normalize('NFC', c)}
        }] for c in cells]}}
    return {
        'object': 'block', 'type': 'table', 'table': {
            'table_width': len(header),
            'has_column_header': True,
            'has_row_header': False,
            'children': [to_row(header)] + [to_row(r) for r in rows]
        }
    }

blocks = [
    h2('가격대별로 고르기'),
    table(
        ['예산', '추천 상품', '이유'],
        [
            ['1만원대', '할리갈리 보드게임', '가족과 함께 즐기기 좋고, 친구 생일선물로도 무난'],
            ['2~3만원대', '레고 스피드챔피언 F1 / 너프건', '조립과 액션놀이 모두 커버, 10세 취향 저격'],
            ['4~5만원대', '3D펜 세트 / RC카', '만들기 좋아하는 아이·활동적인 아이 각각 맞춤'],
            ['8~10만원대', '메탈카드봇W 그랑블루레온', '특별한 날 선물, 캐릭터 좋아하는 아이에게'],
        ]
    ),
    h2('10세 남자아이가 진짜 좋아하는 선물 TOP 6'),
    h3('조립하고 전시하는 재미 "레고 스피드챔피언 F1"'),
    p(
        '레고 스피드챔피언 F1 더 무비 APXGP 팀 레이스카(77252)는 268개 피스, 10세 이상 권장으로 '
        '초등 3~4학년 조립 난이도에 딱 맞습니다. '
        '네이버 블로그에서 "아들이 레고를 조립하고 F1 자동차 전시하며 좋아했다"는 후기가 여러 건 확인됐습니다. '
        '완성 후에도 자동차 모형으로 갖고 놀 수 있어 만족도가 오래갑니다.'
    ),
    h3('실내에서 신나게 "너프건 탄피배출"'),
    p(
        '탄피가 실제처럼 배출되는 너프건은 초등 남아 사이에서 "갖고 싶은 선물 1위"로 반복 언급되는 카테고리입니다. '
        '블로그 후기에서 "어린이날 선물로 줬는데 형제가 서로 뺏아가며 논다"는 반응이 다수였고, '
        '과녁까지 함께 있으면 형제·친구와 대전 놀이로 발전할 수 있습니다. '
        '(단, 안전을 위해 총구가 형광색인 제품이나 고무탄 방식인지 확인하세요.)'
    ),
    h3('두뇌 자극 STEM 장난감 "그래비트랙스 코어 스타터"'),
    p(
        '그래비트랙스는 구슬의 움직임을 직접 설계하는 STEM 교구로, '
        '네이버 블로그와 유튜브에서 초등학생 선물로 꾸준히 추천되는 제품입니다. '
        '"7세 8세 아이가 선물로 받고 대만족했다"는 후기가 있고, '
        '혼자서도 좋아하지만 아빠와 함께 조립하기에도 좋습니다. '
        '(다만 80,160원으로 약간 높은 편이니, 만들기를 특히 좋아하는 아이라면 고려하세요.)'
    ),
    h3('창의력 발산 "3D펜 세트"'),
    p(
        '초등교사 유튜브 채널에서 실제 추천한 아이템으로, '
        '댓글에서 "전자노트랑 3D펜 사달라는 아이들 많다"는 반응이 확인됐습니다. '
        '저온 타입 필라멘트를 쓰는 제품을 고르면 화상 위험이 적고, '
        '입체 도안이 포함된 세트를 고르면 처음 시작하는 아이도 부담 없이 만들 수 있습니다. '
        '다만 평소 만들기나 그림 그리기를 좋아하는 아이에게 특히 잘 맞습니다.'
    ),
    h3('밖에서 신나게 "RC카"'),
    p(
        '"초등 3학년 남아 선물 = RC카"라는 전용 블로그 글이 있을 정도로, '
        '이 나이 남아에게 RC카는 정석 중 정석입니다. '
        '야외에서 활동적으로 놀 수 있고, 핸들 조종을 배우는 과정 자체가 재미요소입니다. '
        '실내에서도 즐길 수 있는 미니 RC카부터 야외용 대형 RC카까지 취향에 따라 고를 수 있습니다.'
    ),
    h3('캐릭터 빠진 아이에게 "메탈카드봇W 그랑블루레온"'),
    p(
        '메탈카드봇 시리즈는 현재 초등 남아 사이에서 레고 다음으로 인기 높은 변신로봇 완구입니다. '
        '실제 블로그에서 "초3 아들 생일선물로 사전예약해서 배송받았다"는 후기가 확인됐습니다. '
        '다크에디션은 기본판보다 디테일이 좋아 아이들이 더 좋아하는 편이나, '
        '가격이 10만원대라 특별한 날 선물에 적합합니다.'
    ),
    h2('10세 남자아이 선물 고르는 법'),
    p(
        '10세(초등 3~4학년)는 장난감을 점점 안 갖고 노는 것처럼 보이지만, '
        '사실은 갖고 노는 방식이 달라지는 시기입니다. '
        '단순한 역할놀이 장난감보다 조립·완성·전시·대전처럼 목표가 있는 놀이를 선호합니다. '
        '아이의 평소 성향을 떠올리며 아래 세 유형 중 가까운 쪽을 골라보세요.'
    ),
    h3('만들기·조립을 좋아하는 아이라면'),
    p(
        '레고 스피드챔피언이나 3D펜이 최선입니다. '
        '완성 후 결과물이 남아서 전시할 수 있다는 점이 포인트입니다. '
        '레고는 시리즈가 많아 취향(자동차·우주·마인크래프트 등)에 따라 골라줄 수 있습니다.'
    ),
    h3('액션·운동을 좋아하는 아이라면'),
    p(
        '너프건이나 RC카가 잘 맞습니다. '
        '너프건은 형제·친구와 함께할 수 있고, RC카는 야외 활동까지 연결됩니다. '
        '다만 너프건을 고를 때는 안전성(고무탄 or 흡착탄)을 먼저 확인하세요.'
    ),
    h3('게임·디지털에 관심이 많은 아이라면'),
    p(
        '그래비트랙스 같은 STEM 교구가 좋은 대안입니다. '
        '게임만큼 몰입할 수 있으면서도 두뇌를 자극하는 활동입니다. '
        '이미 게임기를 갖고 있다면 보드게임(할리갈리)으로 가족과 함께하는 시간을 만들어주는 것도 방법입니다.'
    ),
    h2('이건 사지 마세요'),
    bullet(
        '색칠공부·유아용 캐릭터 장난감 — 10세는 "자기는 이제 어린이가 아니다"라고 생각하는 나이라, '
        '유치한 디자인은 오히려 실망할 수 있습니다.'
    ),
    bullet(
        '값싼 문구 세트나 학용품 — 블로그 댓글에서 "초등학생한테 학용품 선물하면 실망한다"는 의견이 다수였습니다. '
        '실용적이긴 하지만 선물로는 재미가 부족합니다.'
    ),
    bullet(
        '여러 명이 겹쳐 줄 수 있는 흔한 장난감(뻥튀기볼, LED 장난감 등) — '
        '이미 비슷한 걸 갖고 있거나, 생일 선물이 겹쳐서 실망할 가능성이 높습니다.'
    ),
    h2('자주 묻는 질문'),
    h3('10세 남자아이 생일선물 예산은 얼마가 적당한가요?'),
    p(
        '네이버 블로그 데이터 기준, 2만원~5만원대가 가장 무난한 범위입니다. '
        '특별한 날(생일, 크리스마스)이면 10만원까지도 괜찮지만, '
        '매번 고가 선물을 하면 다음 해 부담이 될 수 있으니 적당한 선을 지키는 게 좋습니다.'
    ),
    h3('취향을 잘 모르는 조카·친척 아이에게는 뭐가 좋을까요?'),
    p(
        '할리갈리 보드게임이나 레고 스피드챔피언처럼 호불호가 적은 제품이 안전합니다. '
        '너프건이나 메탈카드봇은 이미 갖고 있을 가능성이 있어 조금 더 리스크가 있습니다.'
    ),
    h3('형제자매가 있으면 어떻게 골라야 하나요?'),
    p(
        '레고나 3D펜처럼 1인용 콘텐츠는 형제 간 다툼이 생길 수 있습니다. '
        '할리갈리·그래비트랙스처럼 여럿이 함께할 수 있는 선물이 오히려 더 좋은 선택입니다.'
    ),
]

notion('PATCH', f'blocks/{guide_id}/children', {'children': blocks})
print(f"새 블록 {len(blocks)}개 추가 완료")

# Archive old products
existing_products = notion('POST', f'databases/{PRODUCTS_DB_ID}/query', {
    'filter': {'property': 'giftGuide', 'relation': {'contains': guide_id}}
})
for page in existing_products['results']:
    notion('PATCH', f'pages/{page["id"]}', {'archived': True})
if existing_products['results']:
    print(f"기존 연결 상품 {len(existing_products['results'])}개 아카이브 완료")

# Create new products
products = [
    {
        'name': '레고 스피드챔피언 F1 더 무비 APXGP 팀 레이스카 77252',
        'price': 34320,
        'naverUrl': 'https://search.shopping.naver.com/catalog/59458293362',
        'imageUrl': 'https://shopping-phinf.pstatic.net/main_5945829/59458293362.20260330165954.jpg',
        'rank': 1,
        'pros': '네이버 블로그 5곳 이상에서 반복 언급된 스테디셀러. 조립·전시·놀이 3박자.',
    },
    {
        'name': '너프건 스나이퍼 저격총 장난감 탄창식',
        'price': 25420,
        'naverUrl': 'https://search.shopping.naver.com/catalog/59629279713',
        'imageUrl': 'https://shopping-phinf.pstatic.net/main_5962927/59629279713.20260626071358.jpg',
        'rank': 2,
        'pros': '블로그 후기에서 "갖고 싶은 선물 1위"로 반복 언급된 카테고리.',
    },
    {
        'name': '코리아보드게임즈 할리갈리',
        'price': 14870,
        'naverUrl': 'https://search.shopping.naver.com/catalog/5591547578',
        'imageUrl': 'https://shopping-phinf.pstatic.net/main_5591547/5591547578.20210420091459.jpg',
        'rank': 3,
        'pros': '가족과 함께 즐기기 좋은 정통 보드게임. 1만원대 부담 없는 가격.',
    },
    {
        'name': '뉴 이지드로잉 저온 무선 어린이 3D펜 리필 필라멘트 세트',
        'price': 49800,
        'naverUrl': 'https://smartstore.naver.com/main/products/13447346795',
        'imageUrl': 'https://shopping-phinf.pstatic.net/main_9099185/90991857147.jpg',
        'rank': 4,
        'pros': '초등교사 유튜브 채널에서 실제 추천한 아이템. 저온 타입 안전.',
    },
    {
        'name': '람보르기니 슈퍼베네노 레드 문열림 어린이 RC카',
        'price': 38900,
        'naverUrl': 'https://smartstore.naver.com/main/products/5107701989',
        'imageUrl': 'https://shopping-phinf.pstatic.net/main_8265222/82652224035.2.jpg',
        'rank': 5,
        'pros': '"초등 3학년 남아 선물 = RC카"라는 전용 블로그 글이 있을 만큼 정석 선물.',
    },
    {
        'name': '메탈카드봇 그랑블루레온 다크에디션',
        'price': 108620,
        'naverUrl': 'https://search.shopping.naver.com/catalog/60531818999',
        'imageUrl': 'https://shopping-phinf.pstatic.net/main_6053181/60531818999.20260626070520.jpg',
        'rank': 6,
        'pros': '실구매 블로그 후기 "초3 아들이 엄청 좋아했다" 확인됨.',
    },
]

for prod in products:
    notion('POST', 'pages', {
        'parent': {'database_id': PRODUCTS_DB_ID},
        'properties': {
            'Title': {'title': [{'type': 'text', 'text': {'content': unicodedata.normalize('NFC', prod['name'])}}]},
            'giftGuide': {'relation': [{'id': guide_id}]},
            'price': {'number': prod['price']},
            'naverUrl': {'url': prod['naverUrl']},
            'imageUrl': {'rich_text': [{'type': 'text', 'text': {'content': prod['imageUrl']}}]},
            'rank': {'number': prod['rank']},
            'pros': {'rich_text': [{'type': 'text', 'text': {'content': unicodedata.normalize('NFC', prod['pros'])}}]},
        }
    })
    print(f"  상품 생성: {prod['name']}")

print("\n✅ 10세-남자아이-생일선물 큐레이션 완료!")
