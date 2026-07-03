import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

K = get_key()
H = {'Authorization': f'Bearer {K}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}
GDB = '9603a00b-976b-4791-a129-d5f537e5db06'

def h2(t): return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t): return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t): return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}

slug = '직장동료-선물'
r = requests.post(f'https://api.notion.com/v1/databases/{GDB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'contains': slug}}, 'page_size': 3})
pid = r.json()['results'][0]['id']
print(f'{slug}: {pid}')
requests.patch(f'https://api.notion.com/v1/pages/{pid}', headers=H, json={
    'properties': {'intro': {'rich_text': [{'text': {'content': '직장동료 선물, 부담 없이 실용적인 아이템을 네이버 쇼핑에서 찾았습니다.'}}]}}})
ids = []; cur = None
while True:
    pp = {'page_size': 100}
    if cur: pp['start_cursor'] = cur
    r2 = requests.get(f'https://api.notion.com/v1/blocks/{pid}/children', headers=H, params=pp)
    d = r2.json()
    ids.extend(b['id'] for b in d.get('results', []))
    if not d.get('has_more'): break
    cur = d.get('next_cursor')
for bid in ids: requests.delete(f'https://api.notion.com/v1/blocks/{bid}', headers=H)
B=[h2('직장동료 선물, 부담 없이 실용적으로'),p('직장동료 선물은 부담스럽지 않으면서도 실용적인 아이템이 가장 좋습니다.'),h3('텀블러·머그컵'),p('락앤락 메트로 텀블러(21,400원, 리뷰 7,334)가 가성비 좋은 직장동료 선물입니다. 코렐 시나모롤 머그(10,900원)도 인기입니다.'),h3('사무용품'),p('유니 제트스트림 볼펜, 다이어리, 업무용 가방 등 매일 사용하는 사무용품이 실용적입니다.'),h3('디저트·간식'),p('오설록 티 세트, 견과류, 초콜릿 등 부담 없는 간식 선물도 좋습니다. 공용으로 즐길 수 있는 간식은 회사에서 인기입니다.'),h2('마치며'),p('직장동료 선물은 가격보다 마음이 중요합니다. 부담 없는 가격대에서 정성을 선택하세요. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]
r3=requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children', headers=H, json={'children': B})
print(f'{"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"} ({len(B)} blocks)')
