import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

KEY = get_key()
GUIDES_DB = '9603a00b-976b-4791-a129-d5f537e5db06'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}

r = requests.post(f'https://api.notion.com/v1/databases/{GUIDES_DB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'contains': '추석-선물'}},
    'page_size': 5
})
p = r.json()['results'][0]
PID = p['id']
print(f'ID: {PID}')

requests.patch(f'https://api.notion.com/v1/pages/{PID}', headers=H, json={
    'properties': {'intro': {'rich_text': [{'text': {'content': '추석 선물, 부모님·친척·지인에게 뭘 드려야 할지 고민되시죠? 네이버 쇼핑에서 인기 있는 추석 선물 세트와 트렌드를 정리했습니다.'}}]}}
})

ids = []
cur = None
while True:
    pp = {'page_size': 100}
    if cur: pp['start_cursor'] = cur
    r2 = requests.get(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, params=pp)
    d = r2.json()
    ids.extend(b['id'] for b in d.get('results', []))
    if not d.get('has_more'): break
    cur = d.get('next_cursor')
for bid in ids: requests.delete(f'https://api.notion.com/v1/blocks/{bid}', headers=H)

def h2(t): return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t): return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t): return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def bp(pts):
    r = []
    for pt in pts:
        if isinstance(pt,tuple): r.append({'type':'text','text':{'content':pt[0]},'annotations':{'bold':True}})
        else: r.append({'type':'text','text':{'content':pt}})
    return {'object':'block','type':'paragraph','paragraph':{'rich_text':r}}

B = []
B.append(h2('추석 선물, 부모님께는 건강을'))
B.append(p('추석은 한 해의 수확을 감사하는 명절인 만큼, 부모님이나 어른들께 건강을 챙겨드리는 의미의 선물이 가장 인기입니다. 네이버 쇼핑에서 확인한 추석 선물 트렌드를 정리했습니다.'))

B.append(h3('건강기능식품 세트'))
B.append(p('홍삼, 발효인삼, 녹용, 침향 등 건강기능식품이 추석 선물의 대표주자입니다. 네이버 쇼핑 검색 결과 녹십자웰빙, 정관장 등 브랜드 제품이 많이 보입니다. 가격대는 3~10만원이 주류이고, 선물세트 포장이 되어 있어 따로 포장할 필요가 없습니다.'))

B.append(h3('전통차·꿀 선물세트'))
B.append(p('혜민당 같은 브랜드의 전통한방차, 벌꿀 선물세트도 추석 선물로 인기입니다. 16년 전통의 차 브랜드 제품부터 프리미엄 꿀 선물세트까지 다양합니다. 부담 없는 가격대(2~5만원)라 선배나 지인에게도 좋습니다.'))

B.append(h3('화장품 선물세트'))
B.append(p('네이처리퍼블릭 등 브랜드의 화장품 선물세트도 추석 시즌에 많이 찾습니다. 평소에 비해 할인 행사를 많이 하기 때문에 명절을 노려 구매하는 사람이 많습니다.'))

B.append(h2('예산별 추천'))
B.append(bp([('3~5만원',True),' 전통차 세트, 벌꿀 세트, 스팸 선물세트']))
B.append(bp([('5~10만원',True),' 홍삼 세트(소), 건강 음료, 화장품 세트']))
B.append(bp([('10~20만원',True),' 프리미엄 홍삼, 한우 세트, 굴비, 과일 세트']))
B.append(bp([('20만원+',True),' 안마의자, 건강식품 프리미엄 세트']))

B.append(h2('추석 선물 고를 때 팁'))
B.append(p('추석 선물은 명절 3~4주 전부터 예약 판매가 시작됩니다. 늦어도 2주 전에는 주문해야 원하는 상품을 받을 수 있습니다. 선물 세트의 유통기한도 꼭 확인하세요.'))

B.append(h2('마치며'))
B.append(p('추석은 온 가족이 모이는 날, 건강을 생각하는 선물이 가장 오래 기억에 남습니다. 개별 제품 가격은 쿠팡·네이버쇼핑에서 확인하세요.'))

print(f'{len(B)} blocks')
r = requests.patch(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, json={'children': B})
print(f"{'OK' if r.status_code==200 else f'FAIL {r.status_code}'}")
