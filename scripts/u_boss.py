import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

K = get_key()
H = {'Authorization': f'Bearer {K}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}
GDB = '9603a00b-976b-4791-a129-d5f537e5db06'

def h2(t): return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t): return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t): return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}

slug = '직장상사-선물'
r = requests.post(f'https://api.notion.com/v1/databases/{GDB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'contains': slug}}, 'page_size': 3})
pid = r.json()['results'][0]['id']
print(f'{slug}: {pid}')
requests.patch(f'https://api.notion.com/v1/pages/{pid}', headers=H, json={
    'properties': {'intro': {'rich_text': [{'text': {'content': '직장상사 선물, 부담 없으면서도 품격 있는 아이템을 네이버 쇼핑과 커뮤니티에서 찾았습니다.'}}]}}})
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
B=[h2('직장상사 선물, 상황별로'),p('직장상사 선물은 관계와 상황에 따라 선택이 다릅니다. 네이버 커뮤니티에서 실제 추천된 선물을 정리했습니다.'),h3('50대 이상 상사'),p('네이버 카페에서 50대 남성 상사 선물로 건강식품(알부민, 정관장)이 많이 추천됩니다. 10~20만원대 프리미엄 건강식품이 무난합니다.'),h3('30~40대 상사'),p('고급 펜(유니 제트스트림 프라임 28,000원), 가죽 펜케이스(58,000원) 등 사무용품이 실용적입니다. 부담스럽지 않은 가격대라 연말이나 명절 선물로 좋습니다.'),h3('집들이 선물'),p('신혼 상사 집들이에는 수건세트(5~6장), 와인, 디퓨저 세트 등이 무난합니다. 인테리어 스타일을 모르면 식기류는 피하는 게 좋다는 의견이 많습니다.'),h2('주의할 점'),p('직장상사 선물은 너무 고가이면 부담스러울 수 있습니다. 개인적인 취향이 강한 아이템(향수, 옷)보다 실용적인 건강식품이나 사무용품이 안전합니다.'),h2('마치며'),p('개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]
r3=requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children', headers=H, json={'children': B})
print(f'{"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"} ({len(B)} blocks)')
