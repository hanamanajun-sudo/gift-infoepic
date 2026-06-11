import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

KEY = get_key()
GUIDES_DB = '9603a00b-976b-4791-a129-d5f537e5db06'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}

r = requests.post(f'https://api.notion.com/v1/databases/{GUIDES_DB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'contains': '여동생-선물'}},
    'page_size': 5
})
p = r.json()['results'][0]
PID = p['id']
print(f'ID: {PID}')

requests.patch(f'https://api.notion.com/v1/pages/{PID}', headers=H, json={
    'properties': {'intro': {'rich_text': [{'text': {'content': '여동생 선물, 예쁘면서도 실용적인 걸 고르려면? 네이버 쇼핑과 블로그에서 추천하는 여동생 선물을 정리했습니다.'}}]}}
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
B.append(h2('여동생 선물, 이런 건 어때요'))
B.append(h3('주얼리'))
B.append(p('여동생 선물로 가장 인기 있는 건 주얼리입니다. 뮤젬 같은 브랜드에서 다이아 세팅 주얼리가 20만원대부터 있습니다. 전제품 고급포장 무료 서비스가 있어 선물용으로 부담이 적습니다.'))
B.append(h3('무드등·홈데코'))
B.append(p('쿠팡에서 무선 충전식 무드등이 9,900원부터 판매 중입니다. 은은한 불빛이 방 분위기를 살려주고 실용적이어서 여동생 선물로 인기입니다.'))
B.append(h3('꽃다발'))
B.append(p('나인플라워 같은 꽃배달 서비스를 이용하면 전국 당일 배송이 가능합니다. 특별한 날 여동생에게 꽃다발을 보내는 것도 좋은 방법입니다.'))
B.append(h2('나이별 추천'))
B.append(p('초등학생 여동생: 인형, 문구세트, 캐릭터 굿즈'))
B.append(p('중·고등학생 여동생: 무드등, 향초, 텀블러, 파우치'))
B.append(p('20대 이상 여동생: 주얼리, 향수, 스킨케어 세트, 꽃다발'))
B.append(h2('마치며'))
B.append(p('여동생 선물은 예쁜 디자인과 실용성을 모두 갖춘 제품이 가장 좋은 반응을 얻습니다. 평소 동생이 좋아하는 스타일을 기억해두세요. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.'))

print(f'{len(B)} blocks')
r = requests.patch(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, json={'children': B})
print(f"{'OK' if r.status_code==200 else f'FAIL {r.status_code}'}")
