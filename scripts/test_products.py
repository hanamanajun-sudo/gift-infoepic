import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

K = get_key()
H = {'Authorization': f'Bearer {K}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}
GDB = '9603a00b-976b-4791-a129-d5f537e5db06'
PDB = '3595b6af-2ff8-44aa-bb2f-9a75d9e0c487'

# 1. Find the guide "13세 여자아이 생일선물"
r = requests.post(f'https://api.notion.com/v1/databases/{GDB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'contains': '13세-여자아이'}}, 'page_size': 3})
guides = r.json()['results']
if not guides:
    print('Guide not found!')
    sys.exit(1)
guide = guides[0]
guide_id = guide['id']
guide_title = guide['properties']['Title']['title'][0]['text']['content']
print(f'Guide: {guide_title} ({guide_id})')

# 2. Check existing products for this guide
r2 = requests.post(f'https://api.notion.com/v1/databases/{PDB}/query', headers=H, json={
    'filter': {'property': 'giftGuide', 'relation': {'contains': guide_id}}, 'page_size': 10})
existing = r2.json()['results']
print(f'Existing products: {len(existing)}')

# 3. Create a test product
products = [
    {
        'Title': {'title': [{'text': {'content': '어뮤즈 립글로우 발라지는 틴트 3호'}}]},
        'price': {'number': 18000},
        'coupangUrl': {'url': 'https://www.coupang.com/vp/products/123456'},
        'naverUrl': {'url': 'https://search.shopping.naver.com/catalog/123456'},
        'imageUrl': {'rich_text': [{'text': {'content': ''}}]},
        'pros': {'rich_text': [{'text': {'content': '13살 여자아이에게 인기 있는 뷰티 제품. 색이 예쁘고 용돈으로 사기엔 부담스러워서 선물로 딱이에요.'}}]},
        'rank': {'number': 1},
        'giftGuide': {'relation': [{'id': guide_id}]},
    },
    {
        'Title': {'title': [{'text': {'content': '다꾸 스티커 세트 + 마스킹테이프 50pcs'}}]},
        'price': {'number': 22000},
        'coupangUrl': {'url': 'https://www.coupang.com/vp/products/789012'},
        'pros': {'rich_text': [{'text': {'content': '다이어리 꾸미기를 좋아하는 13세 여아라면 100% 좋아합니다. SNS에서 유행하는 다꾸 아이템 모음.'}}]},
        'rank': {'number': 2},
        'giftGuide': {'relation': [{'id': guide_id}]},
    },
    {
        'Title': {'title': [{'text': {'content': '시나모롤 귀여운 봉제인형 25cm'}}]},
        'price': {'number': 15900},
        'naverUrl': {'url': 'https://search.shopping.naver.com/catalog/789013'},
        'pros': {'rich_text': [{'text': {'content': '산리오 캐릭터 시나모롤 인형. 10~13세 여아가 가장 좋아하는 선물 중 하나입니다.'}}]},
        'rank': {'number': 3},
        'giftGuide': {'relation': [{'id': guide_id}]},
    },
]

for p in products:
    body = {
        'parent': {'database_id': PDB},
        'properties': p
    }
    r3 = requests.post('https://api.notion.com/v1/pages', headers=H, json=body)
    if r3.status_code == 200:
        print(f'  ✅ {p["Title"]["title"][0]["text"]["content"]}')
    else:
        print(f'  ❌ {r3.status_code}: {r3.text[:100]}')

print('DONE')
