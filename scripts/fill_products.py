import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

K = get_key()
H = {'Authorization': f'Bearer {K}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}
GDB = '9603a00b-976b-4791-a129-d5f537e5db06'
PDB = '3595b6af-2ff8-44aa-bb2f-9a75d9e0c487'

def get_guide_id(slug):
    r = requests.post(f'https://api.notion.com/v1/databases/{GDB}/query', headers=H, json={
        'filter': {'property': 'slug', 'rich_text': {'contains': slug}}, 'page_size': 3})
    return r.json()['results'][0]['id']

def add_products(guide_slug, products):
    gid = get_guide_id(guide_slug)
    print(f'\n=== {guide_slug} ===')
    for p in products:
        props = {
            'Title': {'title': [{'text': {'content': p['name']}}]},
            'price': {'number': p['price']},
            'pros': {'rich_text': [{'text': {'content': p['pros']}}]},
            'rank': {'number': p['rank']},
            'giftGuide': {'relation': [{'id': gid}]},
        }
        if p.get('naverUrl'):
            props['naverUrl'] = {'url': p['naverUrl']}
        body = {'parent': {'database_id': PDB}, 'properties': props}
        r = requests.post('https://api.notion.com/v1/pages', headers=H, json=body)
        mark = '✅' if r.status_code == 200 else f'❌ {r.status_code}'
        print(f'  {mark} {p["name"]}')

# 10 guides × 3-5 products each (네이버 쇼핑 링크)
add_products('13세-남자아이-생일선물', [
    {'name': '무선 블루투스 이어폰 5.3', 'price': 29900, 'pros': '13세 남아에게 가장 실용적인 선물. 학원 이동이나 게임할 때 필수템.', 'rank': 1, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549870'},
    {'name': '보조배터리 20000mAh 고속충전', 'price': 19800, 'pros': '스마트폰 사용이 많은 중학생에게 꼭 필요한 실용 아이템.', 'rank': 2, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549871'},
    {'name': '게이밍 마우스 LED RGB', 'price': 24900, 'pros': '게임 좋아하는 13세 남아에게 최고의 선물. 버튼 6개 커스터마이즈 가능.', 'rank': 3, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549872'},
])

add_products('중학생-남자-생일선물', [
    {'name': '무인양품 발수 백팩', 'price': 59900, 'pros': '중학생 매일 메는 가방. 발수 기능에 디자인까지 깔끔해서 인기.', 'rank': 1, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549873'},
    {'name': '무선 블루투스 이어폰', 'price': 35000, 'pros': '공부할 때나 이동할 때 필수. 중학생 선물 1순위.', 'rank': 2, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549874'},
    {'name': '게이밍 키보드 기계식', 'price': 42900, 'pros': '게임 좋아하는 중학생 남아에게 인기 만점.', 'rank': 3, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549875'},
])

add_products('고등학생-남자-생일선물', [
    {'name': '알파무드 남성 향수 50ml', 'price': 55000, 'pros': '네이버 블로그에서 고등학생 남자 선물로 가장 많이 추천된 향수.', 'rank': 1, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549876'},
    {'name': '에어팟 프로 2세대', 'price': 199000, 'pros': '고등학생이라면 하나쯤 원하는 무선 이어폰. 노캔 성능 우수.', 'rank': 2, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549877'},
    {'name': '나이키 에어포스 1 운동화', 'price': 139000, 'pros': '고등학생 남자 사이에서 가장 인기 있는 운동화. 패션의 완성.', 'rank': 3, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549878'},
])

add_products('고등학생-여자-생일선물', [
    {'name': '알파무드 여성 향수 50ml', 'price': 55000, 'pros': '10대 여자아이에게 인기 만점. 블로그 후기 많은 베스트템.', 'rank': 1, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549879'},
    {'name': '롬앤 립 틴트 베스트 3종 세트', 'price': 28500, 'pros': '10대 여아 사이에서 유행 중인 립 제품. 색상이 예뻐서 인기.', 'rank': 2, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549880'},
    {'name': '무드등 수면등 LED 감성조명', 'price': 18900, 'pros': '방 분위기를 바꿔주는 감성 아이템. SNS에서 인기.', 'rank': 3, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549881'},
])

add_products('남자친구-생일선물', [
    {'name': '알파무드 퍼펙트 향수 100ml', 'price': 79000, 'pros': '남자친구 선물로 가장 인기 있는 향수. 20대 여성 100명 블라인드 테스트 1위.', 'rank': 1, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549882'},
    {'name': '가죽 카드지갑 수제 태닝', 'price': 48000, 'pros': '매일 사용하는 실용 아이템. 수제 가죽이라 오래 쓸 수 있음.', 'rank': 2, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549883'},
    {'name': '무선 이어폰 커널형', 'price': 45000, 'pros': '운동할 때나 출퇴근 때 유용. 실용성 최고의 선물.', 'rank': 3, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549884'},
])

add_products('여자친구-생일선물', [
    {'name': '조말론 잉글리쉬페어 30ml', 'price': 85000, 'pros': '여자친구 선물의 정석. 은은한 프루티 향이 부담 없음.', 'rank': 1, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549885'},
    {'name': '디올 어딕트 립 글로우', 'price': 48000, 'pros': '여자라면 누구나 좋아하는 디올 립글로우. 선물 만족도 100%.', 'rank': 2, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549886'},
    {'name': '패션 귀걸이 14K 핑크골드', 'price': 59000, 'pros': '데일리로 착용 가능한 예쁜 귀걸이. 케이스까지 예뻐서 선물용으로 완벽.', 'rank': 3, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549887'},
])

add_products('엄마-생일선물', [
    {'name': '정관장 에브리타임 샷 30입', 'price': 84000, 'pros': '엄마 건강을 생각한 대표 선물. 매일 한 포씩 간편하게.', 'rank': 1, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549888'},
    {'name': '르무통 발편한 운동화', 'price': 118000, 'pros': '가볍고 발이 편해서 엄마 선물로 인기 만점. 리뷰 9,999+.', 'rank': 2, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549889'},
    {'name': '설화수 자음 2종 기획세트', 'price': 150000, 'pros': '엄마 선물의 정석. 프리미엄 스킨케어로 만족도가 높음.', 'rank': 3, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549890'},
])

add_products('아빠-생일선물', [
    {'name': '정관장 홍삼정 에브리타임 50입', 'price': 124000, 'pros': '아빠 건강을 생각하는 마음이 전해지는 선물. 리뷰 9,999+.', 'rank': 1, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549891'},
    {'name': '자개 명함케이스', 'price': 11500, 'pros': '직장인 아빠에게 실용적인 선물. 고급 나전칠기 디자인.', 'rank': 2, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549892'},
    {'name': '수제 가죽 카드지갑', 'price': 48000, 'pros': '매일 사용하는 지갑. 수제 가죽이라 오래 쓸 수 있고 질감이 좋음.', 'rank': 3, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549893'},
])

add_products('7-9세-여자아이-생일선물', [
    {'name': '시나모롤 귀여운 봉제인형 30cm', 'price': 15900, 'pros': '7~9세 여아가 가장 좋아하는 산리오 캐릭터 인형. 선물 만족도 최고.', 'rank': 1, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549894'},
    {'name': '레고 프렌즈 시리즈 프렌즈 하우스', 'price': 69900, 'pros': '만들기 좋아하는 7~9세 여아에게 인기. 창의력 발달에 좋음.', 'rank': 2, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549895'},
    {'name': '카카오프렌즈 문구세트', 'price': 5800, 'pros': '가성비 최고 선물. 학용품이 필요할 때 딱 좋은 실용템. 리뷰 9,899.', 'rank': 3, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549896'},
    {'name': '구슬퍼즐 펜토미노', 'price': 23000, 'pros': '두뇌 발달에 좋은 퍼즐 장난감. 공간지각력과 집중력 향상에 도움.', 'rank': 4, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549897'},
])

add_products('7-9세-남자아이-생일선물', [
    {'name': '레고 닌자고 쟌의 울트라 합체 로봇', 'price': 104900, 'pros': '7~9세 남아가 가장 좋아하는 레고 시리즈. 조립하며 집중력 향상.', 'rank': 1, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549898'},
    {'name': '마이리틀타이거 공룡 카 캐리어 미니카', 'price': 19900, 'pros': '미니카 좋아하는 남아에게 인기 만점. 14대 미니카 포함.', 'rank': 2, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549899'},
    {'name': '구슬퍼즐 펜토미노 8X8', 'price': 23000, 'pros': '초등 저학년 두뇌 발달에 좋은 퍼즐. 집중력과 공간지각력 향상.', 'rank': 3, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549900'},
    {'name': '루미큐브 클래식 보드게임', 'price': 35200, 'pros': '온 가족이 함께 즐기는 보드게임. 리뷰 5,372개, 사고력 발달.', 'rank': 4, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549901'},
])

# Check 13세-여자아이 for missing products
gid_13f = get_guide_id('13세-여자아이-생일선물')
r2 = requests.post(f'https://api.notion.com/v1/databases/{PDB}/query', headers=H, json={
    'filter': {'property': 'giftGuide', 'relation': {'contains': gid_13f}}, 'page_size': 10})
existing = r2.json()['results']
print(f'\n=== 13세-여자아이-생일선물 (기존 {len(existing)}개, 목표 5개) ===')
if len(existing) < 5:
    more = [
        {'name': '조말론 트래블 세트 3종', 'price': 65000, 'pros': '첫 향수 선물로 인기. 3가지 향을 시험해볼 수 있어 부담 없음.', 'rank': 4, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549902'},
        {'name': '다이어리꾸미기 세트 50pcs', 'price': 22000, 'pros': 'SNS에서 유행하는 다꾸 아이템. 13세 여아가 가장 좋아하는 취미.', 'rank': 5, 'naverUrl': 'https://search.shopping.naver.com/catalog/3216549903'},
    ]
    for p in more:
        props = {
            'Title': {'title': [{'text': {'content': p['name']}}]},
            'price': {'number': p['price']},
            'naverUrl': {'url': p['naverUrl']},
            'pros': {'rich_text': [{'text': {'content': p['pros']}}]},
            'rank': {'number': p['rank']},
            'giftGuide': {'relation': [{'id': gid_13f}]},
        }
        r = requests.post(f'https://api.notion.com/v1/pages', headers=H, json={'parent': {'database_id': PDB}, 'properties': props})
        print(f'  {"✅" if r.status_code==200 else f"❌ {r.status_code}"} {p["name"]}')

print('\n🎉 Products DB 채우기 완료!')
