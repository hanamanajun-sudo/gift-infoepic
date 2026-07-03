import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

K = get_key()
H = {'Authorization': f'Bearer {K}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}
GDB = '9603a00b-976b-4791-a129-d5f537e5db06'

def h2(t): return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t): return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t): return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}

slug = '친구-생일선물'
r = requests.post(f'https://api.notion.com/v1/databases/{GDB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'contains': slug}}, 'page_size': 3})
pid = r.json()['results'][0]['id']
print(f'{slug}: {pid}')
requests.patch(f'https://api.notion.com/v1/pages/{pid}', headers=H, json={
    'properties': {'intro': {'rich_text': [{'text': {'content': '친구 생일선물, 성별과 취향에 따라 골라보세요. 네이버 쇼핑에서 인기 있는 친구 선물을 정리했습니다.'}}]}}})
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
B=[h2('친구 생일선물, 성별과 취향에 따라'),p('친구 선물은 가장 가까운 사이인 만큼 취향을 잘 아는 게 중요합니다. 네이버 쇼핑에서 인기 친구 선물을 정리했습니다.'),h3('남자 친구'),p('알파무드 향수(3만원대)가 남자 친구 선물로 인기입니다. 무선 이어폰, 게이밍 마우스, 보조배터리 등 전자기기도 실용적입니다.'),h3('여자 친구'),p('디올 뷰티 립글로우, 향수, 스킨케어 세트 등이 인기입니다. 퍼스널컬러 진단 같은 경험 선물도 특별합니다.'),h3('감성 선물'),p('자작나무에 추억을 새기는 나무 편지, 커플 각인 아이템 등 특별한 메시지를 담은 선물이 인기입니다.'),h3('가성비 선물'),p('스탠리 텀블러(49,000원), 오설록 티 세트(20,000원) 등 부담 없는 가격의 선물도 좋습니다.'),h2('마치며'),p('친구는 가장 가까운 사이니 평소에 친구가 필요로 하거나 갖고 싶어했던 걸 기억해보는 게 가장 좋은 선물입니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]
r3=requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children', headers=H, json={'children': B})
print(f'{"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"} ({len(B)} blocks)')
