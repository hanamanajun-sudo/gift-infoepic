import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

K = get_key()
H = {'Authorization': f'Bearer {K}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}
GDB = '9603a00b-976b-4791-a129-d5f537e5db06'

def h2(t): return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t): return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t): return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}

slug = '중학생-남자-생일선물'
r = requests.post(f'https://api.notion.com/v1/databases/{GDB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'contains': slug}}, 'page_size': 3})
pid = r.json()['results'][0]['id']
print(f'{slug}: {pid}')

requests.patch(f'https://api.notion.com/v1/pages/{pid}', headers=H, json={
    'properties': {'intro': {'rich_text': [{'text': {'content': '중학생 남자 생일선물, 운동화부터 가방까지 네이버 블로그와 쇼핑에서 찾은 인기 아이템을 정리했습니다.'}}]}}})

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
  h2('중학생 남자 생일선물, 실용적인 게 최고'),
  p('중학생 남자아이에게 선물하는 건 정말 까다롭습니다. 네이버 블로그 후기를 보면 운동화나 옷은 취향을 많이 타서 실패 확률이 높다고 합니다. 대신 오래 쓸 수 있는 실용적인 물건이나 평소 갖고 싶어했던 아이템이 가장 좋은 반응을 얻습니다.'),
  h3('운동화'),
  p('블로그 후기에서 가장 많이 나온 아이템은 조던 운동화입니다. 네이버 쇼핑에서도 10대 남성 운동화는 꾸준히 인기입니다. 다만 사이즈를 잘 모르면 위험할 수 있어, 평소 신는 신발 사이즈를 확인해두는 게 좋습니다.'),
  h3('백팩'),
  p('중학생은 매일 가방을 메고 다니기 때문에 백팩이 실용적인 선물입니다. 네이버 쇼핑에서 무인양품 발수 백팩(49,900~59,900원, 리뷰 150)이 인기입니다. 디스커버리 데일리 백팩(54,500원)도 가성비가 좋습니다. MLB 백팩(12만9천원)은 좀 더 고급 옵션입니다.'),
  h3('전자기기'),
  p('무선 이어폰(에어팟 또는 갤럭시 버즈), 보조배터리(2만mAh), 게이밍 마우스 등이 중학생 사이에서 인기입니다. 네이버 블로그에서 솔드아웃 상태인 인기템은 미리 재고 확인이 필요합니다.'),
  h2('주의할 점'),
  p('중학생은 취향이 확고해지는 시기라, 평소 아이가 무엇을 좋아하는지 관찰해두는 게 가장 중요합니다. 직접 묻는 게 가장 확실하고, 인기 게임이나 유튜브 콘텐츠를 참고해도 좋습니다.'),
  h2('마치며'),
  p('중학생 남자아이 선물은 비싼 것보다 아이가 진짜 원하는 게 뭔지 아는 게 더 중요합니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.'),
]
r3 = requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children', headers=H, json={'children': B})
print(f'{"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"} ({len(B)} blocks)')
