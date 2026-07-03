import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

KEY = get_key()
GUIDES_DB = '9603a00b-976b-4791-a129-d5f537e5db06'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}

r = requests.post(f'https://api.notion.com/v1/databases/{GUIDES_DB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'contains': '장인어른-선물'}},
    'page_size': 5
})
p = r.json()['results'][0]
PID = p['id']
print(f'ID: {PID}')

requests.patch(f'https://api.notion.com/v1/pages/{PID}', headers=H, json={
    'properties': {'intro': {'rich_text': [{'text': {'content': '장인어른 선물, 뭘 드려야 할지 고민되시죠? 네이버 쇼핑에서 인기 있는 장인어른 선물 아이템과 가격대를 정리했습니다.'}}]}}
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
B.append(h2('장인어른 선물, 건강을 생각하세요'))
B.append(p('장인어른 선물은 네이버 쇼핑에서 확인한 결과 건강기능식품이 가장 인기입니다. 효도 선물의 기본은 건강입니다.'))

B.append(h3('건강기능식품'))
B.append(p('종근당 침향환은 프리미엄 건강기능식품으로 누적판매 300만환을 기록했습니다. 녹십자웰빙 어삼은 발효인삼과 호주산 양태반이 함유되어 있어 기력 보충에 좋습니다. 가격대는 5~15만원입니다. 농협안심녹용의 녹용 진액(60년 전통)도 장인어른 선물로 인기입니다.'))

B.append(h3('홍삼·발효인삼'))
B.append(p('김정환홍삼, 정관장 홍삼 세트는 장인어른 선물의 대표 아이템입니다. 면역력 강화와 피로회복에 좋아 나이 드신 분들께 인기가 많습니다. 가격대는 3~20만원까지 다양합니다.'))

B.append(h2('예산별 추천'))
B.append(bp([('3~5만원',True),' 홍삼 세트(소), 건강 음료, 전통주 세트']))
B.append(bp([('5~10만원',True),' 침향환, 발효인삼, 녹용 진액']))
B.append(bp([('10~20만원',True),' 프리미엄 홍삼, 종합 건강식품 세트']))
B.append(bp([('20만원+',True),' 안마의자(할인 시), 프리미엄 건강 세트']))

B.append(h2('마치며'))
B.append(p('장인어른 선물은 건강을 생각하는 마음이 가장 잘 전달됩니다. 선물과 함께 따뜻한 인사말을 전하는 것도 잊지 마세요. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.'))

print(f'{len(B)} blocks')
r = requests.patch(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, json={'children': B})
print(f"{'OK' if r.status_code==200 else f'FAIL {r.status_code}'}")
