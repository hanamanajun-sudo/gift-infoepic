import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

K = get_key()
H = {'Authorization': f'Bearer {K}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}
GDB = '9603a00b-976b-4791-a129-d5f537e5db06'

def h2(t): return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t): return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t): return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}

slug = '스승의날-선물'
r = requests.post(f'https://api.notion.com/v1/databases/{GDB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'contains': slug}}, 'page_size': 3})
pid = r.json()['results'][0]['id']
print(f'{slug}: {pid}')
requests.patch(f'https://api.notion.com/v1/pages/{pid}', headers=H, json={
    'properties': {'intro': {'rich_text': [{'text': {'content': '스승의날 선물, 부담 없이 마음을 전할 수 있는 아이템을 네이버 쇼핑에서 찾았습니다.'}}]}}})
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
B=[h2('스승의날 선물, 부담 없이 마음을'),p('스승의날은 감사하는 마음을 전하는 날입니다. 네이버 쇼핑에서 인기 있는 스승의날 선물을 정리했습니다.'),h3('건강식품'),p('농협홍삼 스틱 선물세트(32,800원, 리뷰 9,999+)가 가장 인기입니다. 한방에 챙겨 먹기 편해서 선생님 선물로 좋습니다.'),h3('차·티 세트'),p('오설록 티 베리에이션 선물세트(20,000원, 리뷰 9,999+)는 가성비 좋은 스승의날 선물입니다. 6가지 맛을 즐길 수 있습니다.'),h3('견과류 세트'),p('산과들에 하루견과(32,900원), HBAF 바프(17,900원) 등 견과류 선물세트도 부담 없는 가격의 인기 선물입니다.'),h3('카네이션·꽃'),p('카네이션 꽃다발은 스승의날의 대표 선물입니다. 네이버 쇼핑에서 전국 꽃배달 서비스를 이용할 수 있습니다.'),h2('예산별'),p('1만원 이하: 카네이션, 손편지 / 1~3만원: 오설록 티, 견과류, 핸드크림 / 3~5만원: 홍삼 스틱, 스탠리 텀블러 / 5만원+: 프리미엄 건강식품'),h2('마치며'),p('스승의날 선물은 비싼 것보다 정성이 담긴 편지나 인사말이 가장 큰 감동을 줍니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]
r3=requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children', headers=H, json={'children': B})
print(f'{"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"} ({len(B)} blocks)')
