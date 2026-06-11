import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

KEY = get_key()
GUIDES_DB = '9603a00b-976b-4791-a129-d5f537e5db06'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}

r = requests.post(f'https://api.notion.com/v1/databases/{GUIDES_DB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'contains': '남동생-선물'}},
    'page_size': 5
})
p = r.json()['results'][0]
PID = p['id']
print(f'ID: {PID}')

requests.patch(f'https://api.notion.com/v1/pages/{PID}', headers=H, json={
    'properties': {'intro': {'rich_text': [{'text': {'content': '남동생 선물, 나이와 취향에 따라 골라보세요. 네이버 블로그에서 인기 있는 남동생 선물 아이템을 정리했습니다.'}}]}}
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

B = []
B.append(h2('남동생 선물, 실용적인 게 최고'))
B.append(h3('패션·액세서리'))
B.append(p('블로그에서 남동생 선물로 라쉬반 프리미엄 속옷(듀얼글로우 3종)이 추천되고 있습니다. 특히 평소 속옷 착용감에 민감한 남동생도 편하게 입는다는 후기가 많습니다. 실용적인 선물을 고민한다면 속옷 세트나 넥타이, 지갑 같은 패션 아이템이 좋습니다.'))
B.append(h3('전자기기·디지털'))
B.append(p('남동생 나이에 따라 무선 이어폰, 보조배터리(1~3만원대), 게이밍 마우스 등이 인기입니다. 네이버 쇼핑에서 남동생 선물로 무선 충전식 제품도 많이 보입니다.'))
B.append(h3('특별한 날 선물'))
B.append(p('상견례 때 만나는 동생들 선물로는 원앙 떡케이크나 답례 선물 세트가 블로그에서 추천되고 있습니다. 가벼운 선물이라도 정성이 느껴지는 게 중요합니다.'))
B.append(h2('나이별 추천'))
B.append(p('초등학생 남동생: 장난감, 보드게임, 과학키트'))
B.append(p('중·고등학생 남동생: 무선 이어폰, 보조배터리, 운동화'))
B.append(p('20대 이상 남동생: 속옷 세트, 지갑, 향수, 전자기기'))
B.append(h2('마치며'))
B.append(p('남동생 선물은 비싼 것보다 실용적이고 마음에 쏙 드는 게 가장 좋습니다. 평소 동생이 좋아하는 걸 관찰해두었다가 그에 맞춰 고르면 성공입니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.'))

print(f'{len(B)} blocks')
r = requests.patch(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, json={'children': B})
print(f"{'OK' if r.status_code==200 else f'FAIL {r.status_code}'}")
