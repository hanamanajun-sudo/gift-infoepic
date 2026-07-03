import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

KEY = get_key()
GUIDES_DB = '9603a00b-976b-4791-a129-d5f537e5db06'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}

r = requests.post(f'https://api.notion.com/v1/databases/{GUIDES_DB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'contains': '화장품-선물'}},
    'page_size': 5
})
p = r.json()['results'][0]
PID = p['id']
print(f'ID: {PID}')

requests.patch(f'https://api.notion.com/v1/pages/{PID}', headers=H, json={
    'properties': {'intro': {'rich_text': [{'text': {'content': '화장품 선물, 어떤 브랜드가 좋을지 고민되시죠? 네이버 쇼핑에서 인기 있는 화장품 선물세트와 브랜드를 정리했습니다.'}}]}}
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
B.append(h2('화장품 선물, 브랜드별로 고르기'))
B.append(p('화장품은 선물용으로 가장 인기 있는 카테고리 중 하나입니다. 네이버 쇼핑에서 확인한 화장품 선물 브랜드와 특징을 정리했습니다.'))

B.append(h3('명품 브랜드'))
B.append(p('랑콤 제니피끄 선물세트가 네이버 쇼핑에서 인기입니다. 제니듀오세트, 제니세럼세트, 제니아이크림 등 다양한 구성으로 나와 있습니다. 가격대는 5~15만원 선입니다. 받는 사람이 나이가 있는 경우 명품 브랜드가 무난합니다.'))

B.append(h3('대중 브랜드'))
B.append(p('AHC는 스킨케어 라인이 잘 알려져 있고, 네이버 쇼핑에서 할인 행사가 자주 있습니다. 아모레퍼시픽 계열(설화수, 헤라, 라네즈)은 선물세트 구성이 다양하고 품질이 검증된 브랜드입니다. 가격대는 3~10만원입니다.'))

B.append(h3('자연주의 브랜드'))
B.append(p('네이처리퍼블릭 등 자연주의 화장품도 인기입니다. 피부가 예민한 사람에게 선물하기 좋고, 가격도 부담스럽지 않은 편입니다.'))

B.append(h2('받는 사람별 추천'))
B.append(bp([('10대·20대 초반',True),' 네이처리퍼블릭, 이니스프리, 토니모리']))
B.append(bp([('20대 후반·30대',True),' AHC, 라네즈, 미샤']))
B.append(bp([('40대+',True),' 설화수, 헤라, 랑콤, 술']))
B.append(h2('마치며'))
B.append(p('화장품 선물은 받는 사람의 나이와 피부 타입을 고려하는 게 가장 중요합니다. 선물세트는 정품 구성 그대로 포장되어 있어 따로 감쌀 필요가 없어 편리합니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.'))

print(f'{len(B)} blocks')
r = requests.patch(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, json={'children': B})
print(f"{'OK' if r.status_code==200 else f'FAIL {r.status_code}'}")
