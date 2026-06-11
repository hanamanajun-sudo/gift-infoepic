import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

K = get_key()
H = {'Authorization': f'Bearer {K}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}
GDB = '9603a00b-976b-4791-a129-d5f537e5db06'

def h2(t): return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t): return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t): return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}

slug = '할아버지-생일선물'
r = requests.post(f'https://api.notion.com/v1/databases/{GDB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'contains': slug}}, 'page_size': 3})
pid = r.json()['results'][0]['id']
print(f'{slug}: {pid}')

requests.patch(f'https://api.notion.com/v1/pages/{pid}', headers=H, json={
    'properties': {'intro': {'rich_text': [{'text': {'content': '할아버지 생일선물, 건강과 전통 간식까지 네이버 쇼핑에서 인기 있는 아이템을 정리했습니다.'}}]}}})

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
  h2('할아버지 생일선물, 건강과 정성을 담아서'),
  p('할아버지 선물은 건강을 생각하는 마음이 가장 잘 전달됩니다. 네이버 쇼핑에서 인기 있는 할아버지 선물을 정리했습니다.'),
  h3('건강기능식품'),
  p('산양삼(49,800원, 리뷰 9,999+)이 할아버지 선물로 가장 인기입니다. 한국임업진흥원 인증 제품이 신뢰도가 높습니다. 쏘팔메토(29,900원)나 비아노스(28,900원, 리뷰 4,955) 같은 전립선 건강 제품도 나이 드신 남성분께 좋은 선물입니다.'),
  h3('꿀·전통 식품'),
  p('벌집꿀(33,900원, 리뷰 9,999+)은 건강에도 좋고 맛도 있어 인기입니다. 해태 연양갱(11,800원, 리뷰 928)은 부드러워서 치약이 약한 할아버지도 드시기 좋습니다.'),
  h3('실용 아이템'),
  p('따뜻한 목도리, 클래식 모자, 편한 실내화 등이 네이버 쇼핑 할아버지 선물 카테고리에서 인기입니다.'),
  h2('예산별 추천'),
  p('1~2만원: 연양갱, 전통 간식 세트 / 2~5만원: 벌꿀, 건강 음료, 목도리 / 5~10만원: 산양삼, 전립선 건강식품 / 10만원+: 프리미엄 홍삼 세트'),
  h2('마치며'),
  p('할아버지 선물은 무엇보다 건강과 관련된 실용적인 아이템이 가장 좋은 반응을 얻습니다. 직접 전해드리면서 안부 인사를 꼭 전하세요. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.'),
]
r3 = requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children', headers=H, json={'children': B})
print(f'{"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"} ({len(B)} blocks)')
