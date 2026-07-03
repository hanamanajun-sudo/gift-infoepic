import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

KEY = get_key()
GUIDES_DB = '9603a00b-976b-4791-a129-d5f537e5db06'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}

r = requests.post(f'https://api.notion.com/v1/databases/{GUIDES_DB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'contains': '설날-선물'}},
    'page_size': 5
})
p = r.json()['results'][0]
PID = p['id']
print(f'ID: {PID}')

requests.patch(f'https://api.notion.com/v1/pages/{PID}', headers=H, json={
    'properties': {'intro': {'rich_text': [{'text': {'content': '설날 선물, 뭘 준비해야 할지 고민되시죠? 네이버 쇼핑에서 판매 중인 인기 설날 선물 세트와 가격대를 정리했습니다.'}}]}}
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
B.append(h2('설날 선물, 이렇게 고르세요'))
B.append(p('설날은 부모님, 친척, 지인에게 감사 인사를 전하는 명절입니다. 네이버 쇼핑에서 설날 선물로 인기 있는 제품들은 주로 건강기능식품과 전통 선물 세트입니다.'))
B.append(h3('건강기능식품이 가장 인기'))
B.append(p('네이버 검색 결과 설날 선물로 가장 많이 언급되는 카테고리는 건강기능식품입니다. 녹십자웰빙 어삼 양태반(발효인삼), 정관장 홍삼 세트 등이 대표적입니다. 건강을 챙겨드리는 의미가 있어 부모님 선물로 특히 좋습니다.'))
B.append(h3('벌꿀 선물세트'))
B.append(p('예밀담 꿀 선물세트처럼 벌꿀은 설날 선물로 꾸준히 인기입니다. 건강에도 좋고 보관이 쉬워서 부담 없이 드리기 좋습니다. 무료 메시지 카드와 보자기 포장 서비스가 있는 제품도 있습니다.'))
B.append(h3('가격대별 추천'))
B.append(bp([('3~5만원',True),' 벌꿀 선물세트, 건강 음료, 과일 세트']))
B.append(bp([('5~10만원',True),' 홍삼 세트(소), 건강기능식품, 스팸 선물세트']))
B.append(bp([('10~20만원',True),' 프리미엄 홍삼, 한우 세트, 굴비 세트']))
B.append(h2('주의할 점'))
B.append(p('설날 선물은 명절 2~3주 전부터 네이버쇼핑과 쿠팡에서 예약 판매를 시작합니다. 원하는 제품을 받으려면 미리 주문하는 게 좋습니다. 선물 세트는 포장 상태를 꼭 확인하세요.'))
B.append(h2('마치며'))
B.append(p('설날 선물은 해마다 새로운 트렌드가 나오지만, 건강식품과 전통 선물 세트가 가장 무난합니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.'))

print(f'{len(B)} blocks')
r = requests.patch(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, json={'children': B})
print(f"{'OK' if r.status_code==200 else f'FAIL {r.status_code}'}")
