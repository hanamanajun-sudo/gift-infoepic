import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

K = get_key()
H = {'Authorization': f'Bearer {K}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}
GDB = '9603a00b-976b-4791-a129-d5f537e5db06'

def h2(t): return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t): return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t): return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}

slug = '시어머니-선물'
r = requests.post(f'https://api.notion.com/v1/databases/{GDB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'contains': slug}}, 'page_size': 3})
pid = r.json()['results'][0]['id']
print(f'{slug}: {pid}')
requests.patch(f'https://api.notion.com/v1/pages/{pid}', headers=H, json={
    'properties': {'intro': {'rich_text': [{'text': {'content': '시어머니 선물, 발편한 신발부터 명품 스킨케어까지 네이버 쇼핑에서 인기 아이템을 정리했습니다.'}}]}}})
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
B=[h2('시어머니 선물, 센스 있는 선택'),p('시어머니 선물은 첫인상이 중요합니다. 네이버 쇼핑에서 인기 있는 시어머니 선물을 정리했습니다.'),h3('발편한 운동화'),p('르무통 메리노울 운동화(118,000원, 리뷰 9,999+)가 시어머니 선물로 가장 인기입니다. 가볍고 발이 편해서 나이 드신 분들이 좋아합니다. 허시파피 소가죽 샌들(54,000원)도 계절에 맞는 좋은 선택입니다.'),h3('스킨케어 세트'),p('설화수 자음 2종 기획세트(150,000원, 리뷰 9,999+)는 시어머니 선물의 정석입니다. 프리미엄 브랜드라 격식 있는 선물로 좋습니다.'),h3('가방'),p('브랜든 세이프 크로스바디백(55,900원, 리뷰 4,836)은 도난방지 기능이 있어 여행이나 외출 시 유용합니다.'),h2('예산별'),p('3~5만원: 스카프, 손수건 세트 / 5~10만원: 편한 신발, 가방 / 10~15만원: 르무통 운동화 / 15만원+: 설화수, 프리미엄 스킨케어'),h2('마치며'),p('시어머니 선물은 정성과 센스가 중요합니다. 선물과 함께 따뜻한 인사말을 꼭 전하세요. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]
r3=requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children', headers=H, json={'children': B})
print(f'{"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"} ({len(B)} blocks)')
