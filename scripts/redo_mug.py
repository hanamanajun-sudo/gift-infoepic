import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

KEY = get_key()
GUIDES_DB = '9603a00b-976b-4791-a129-d5f537e5db06'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}

r = requests.post(f'https://api.notion.com/v1/databases/{GUIDES_DB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'contains': '머그컵-선물'}},
    'page_size': 5
})
p = r.json()['results'][0]
PID = p['id']
print(f'ID: {PID}')

requests.patch(f'https://api.notion.com/v1/pages/{PID}', headers=H, json={
    'properties': {'intro': {'rich_text': [{'text': {'content': '머그컵 선물, 부담스럽지 않은 가격에 실용적이면서도 디자인이 예쁜 걸 고르려면? 네이버 쇼핑에서 찾은 인기 머그컵을 정리했습니다.'}}]}}
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
B.append(h2('머그컵 선물, 종류별로 살펴보기'))
B.append(p('머그컵은 선물로 부담없으면서도 매일 사용하게 되는 실용 아이템입니다. 네이버 쇼핑 검색 결과 인기 있는 머그컵을 정리했습니다.'))

B.append(h3('캐릭터 머그컵'))
B.append(p('코렐의 시나모롤, 쿠로미 캐릭터 머그컵이 네이버 쇼핑에서 인기입니다. 1개 10,900원, 2개 세트 19,620원이며 리뷰가 316개로 구매 피드백이 많습니다. 산리오 캐릭터를 좋아하는 친구나 아이에게 좋은 선물입니다.'))

B.append(h3('감성 디자인 머그컵'))
B.append(p('네이버 쇼핑에서 감성 머그컵으로 검색하면 수제 도자기 머그, 레터링 머그, 북유럽 감성 디자인 제품이 다양하게 나옵니다. 가격은 보통 5,000~15,000원 선입니다. 집들이 선물이나 신혼부부에게 인기입니다.'))

B.append(h3('네이밍/각인 머그컵'))
B.append(p('이름이나 문구를 각인할 수 있는 맞춤 머그컵도 선물로 인기입니다. 개인화된 선물을 원하는 사람에게 추천합니다. 결혼식 답례품이나 단체 선물로도 많이 찾습니다.'))

B.append(h2('예산별 추천'))
B.append(bp([('~5,000원',True),' 일반 무지 머그컵, 이니셜 각인']))
B.append(bp([('5,000~1만원',True),' 캐릭터 머그 1P, 수제 도자기 머그']))
B.append(bp([('1~2만원',True),' 캐릭터 머그 2P 세트, 감성 디자인 세트']))
B.append(bp([('2만원+',True),' 명품 브랜드 머그(스타벅스), 세라믹 세트']))

B.append(h2('마치며'))
B.append(p('머그컵은 가격 부담이 적고 매일 사용하는 실용적인 선물입니다. 선물할 사람의 취향을 고려해서 디자인이나 캐릭터를 고르면 더 좋아할 거예요. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.'))

print(f'{len(B)} blocks')
r = requests.patch(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, json={'children': B})
print(f"{'OK' if r.status_code==200 else f'FAIL {r.status_code}'}")
