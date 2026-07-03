import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

K = get_key()
H = {'Authorization': f'Bearer {K}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}
GDB = '9603a00b-976b-4791-a129-d5f537e5db06'

def h2(t): return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t): return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t): return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}

slug = '할머니-생일선물'
r = requests.post(f'https://api.notion.com/v1/databases/{GDB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'contains': slug}}, 'page_size': 3})
pid = r.json()['results'][0]['id']
print(f'{slug}: {pid}')

requests.patch(f'https://api.notion.com/v1/pages/{pid}', headers=H, json={
    'properties': {'intro': {'rich_text': [{'text': {'content': '할머니 생일선물, 건강과 편안함을 생각한 선물을 네이버 쇼핑과 블로그에서 찾았습니다.'}}]}}})

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

B = [
  h2('할머니 생일선물, 건강과 편안함을 생각해서'),
  p('할머니 선물은 무엇보다 건강과 편안함을 생각하는 게 가장 중요합니다. 네이버 블로그에서도 건강식품과 실용적인 생활 아이템이 많이 추천됩니다.'),
  h3('건강기능식품'),
  p('네이버 쇼핑에서 정관장 에브리타임 샷(124,000원, 리뷰 9,999+)이 할머니 선물로 가장 인기입니다. 휴대가 간편해서 매일 챙겨 드시기 좋습니다. 홍삼, 침향환, 종합비타민 등도 좋은 선택입니다.'),
  h3('실용 생활 아이템'),
  p('블로그에서 할머니 선물로 틈틈 TMTM 초경량 지팡이(2만원대)가 추천되었습니다. 가벼워서 들고 다니기 편하고 디자인도 예뻐서 할머니 선물로 인기입니다. 편한 운동화, 가벼운 스카프, 목도리도 좋습니다.'),
  h3('전통 간식·한과'),
  p('네이버 쇼핑에서 할머니 선물 카테고리에 한과, 전통 간식 세트가 있습니다. 부담 없는 가격(1~3만원대)에 정성이 느껴지는 선물입니다.'),
  h2('예산별 추천'),
  p('1~3만원: 한과 세트, 스카프, 장갑 / 3~5만원: 지팡이, 편한 운동화 / 5~10만원: 건강 기능식품, 마사지기 / 10만원+: 정관장 프리미엄 세트'),
  h2('마치며'),
  p('할머니 선물은 비싼 것보다 할머니가 실제로 필요로 하는 것, 사용하시는 게 가장 좋습니다. 평소에 할머니가 불편해하시는 점을 떠올려보세요. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.'),
]
r3 = requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children', headers=H, json={'children': B})
print(f'{"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"} ({len(B)} blocks)')
