import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

K = get_key()
H = {'Authorization': f'Bearer {K}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}
GDB = '9603a00b-976b-4791-a129-d5f537e5db06'

def h2(t): return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t): return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t): return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}

# 고등학생 남자
slug = '고등학생-남자-생일선물'
r = requests.post(f'https://api.notion.com/v1/databases/{GDB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'contains': slug}}, 'page_size': 3})
pid = r.json()['results'][0]['id']
print(f'{slug}: {pid}')
requests.patch(f'https://api.notion.com/v1/pages/{pid}', headers=H, json={
    'properties': {'intro': {'rich_text': [{'text': {'content': '고등학생 남자 생일선물, 향수부터 전자기기까지 네이버 블로그와 쇼핑에서 찾은 인기 아이템을 정리했습니다.'}}]}}})
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
  h2('고등학생 남자 생일선물, 이제는 취향을 알 때'),
  p('고등학생 남자아이는 중학생과 달리 자기만의 취향이 확실해지는 시기입니다. 네이버 블로그 후기에서 가장 인기 있는 선물은 향수와 전자기기였습니다.'),
  h3('향수'),
  p('블로그에서 많이 언급된 알파무드 향수는 10대 남자에게 특히 인기입니다. 우디향 베이스에 산뜻하게 스며드는 향으로 남사친 선물로도 추천됩니다. 고등학생부터 20대까지 부담 없이 사용할 수 있는 가격대입니다.'),
  h3('무선 이어폰·전자기기'),
  p('고등학생은 공부할 때나 이동할 때 이어폰을 항상 사용합니다. 에어팟이나 갤럭시 버즈 같은 무선 이어폰이 가장 인기 있는 선물입니다. 무선 충전식 보조배터리(2만원대)도 실용적인 선택입니다.'),
  h3('운동화'),
  p('중학생과 마찬가지로 조던, 나이키 등 인기 운동화 브랜드가 좋습니다. 다만 사이즈와 디자인 취향을 미리 확인해야 합니다.'),
  h2('예산별 추천'),
  p('1~3만원: 향수(알파무드), 보조배터리 / 3~5만원: 무선 이어폰(중국 브랜드), 패션 액세서리 / 5~10만원: 에어팟, 갤럭시 버즈, 운동화 / 10만원+: 프리미엄 운동화, 브랜드 백팩'),
  h2('마치며'),
  p('고등학생 남자는 자신이 좋아하는 분야에 대한 애착이 강합니다. 평소 어떤 브랜드나 아이템에 관심이 있는지 관찰해두면 선물이 훨씬 쉬워집니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.'),
]
r3 = requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children', headers=H, json={'children': B})
print(f'고등남 {"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"} ({len(B)} blocks)')

# 고등학생 여자
slug2 = '고등학생-여자-생일선물'
r4 = requests.post(f'https://api.notion.com/v1/databases/{GDB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'contains': slug2}}, 'page_size': 3})
pid2 = r4.json()['results'][0]['id']
print(f'{slug2}: {pid2}')
requests.patch(f'https://api.notion.com/v1/pages/{pid2}', headers=H, json={
    'properties': {'intro': {'rich_text': [{'text': {'content': '고등학생 여자 생일선물, 뷰티부터 감성 아이템까지 네이버 블로그에서 찾은 인기 선물을 정리했습니다.'}}]}}})
ids2 = []; cur2 = None
while True:
    pp = {'page_size': 100}
    if cur2: pp['start_cursor'] = cur2
    r5 = requests.get(f'https://api.notion.com/v1/blocks/{pid2}/children', headers=H, params=pp)
    d = r5.json()
    ids2.extend(b['id'] for b in d.get('results', []))
    if not d.get('has_more'): break
    cur2 = d.get('next_cursor')
for bid in ids2: requests.delete(f'https://api.notion.com/v1/blocks/{bid}', headers=H)
B2 = [
  h2('고등학생 여자 생일선물, 취향 저격 아이템'),
  p('고등학생 여자아이는 화장품, 향수, 감성 아이템을 좋아합니다. 네이버 블로그에서 인기 있는 선물을 정리했습니다.'),
  h3('향수'),
  p('블로그에서 알파무드 향수가 고등학생 여자에게도 인기입니다. 은은한 플로럴 계열이나 달콤한 과일 계열 향이 선호됩니다. 조말론이나 딥디크는 고급 선물용으로 좋습니다.'),
  h3('화장품·스킨케어'),
  p('립글로스, 틴트, 마스크팩 세트 등이 부담 없는 가격의 선물로 인기입니다. 10대 여자아이에게 인기 있는 브랜드는 어뮤즈, 롬앤, 클리오 등입니다. 가격은 1~3만원대로 부담이 적습니다.'),
  h3('감성 아이템'),
  p('무드등, 향초, 다꾸(다이어리 꾸미기) 세트, 인형 등이 고등학생 여자아이에게 인기입니다. 사진을 찍어 SNS에 올리기 좋은 예쁜 디자인의 제품이 좋은 반응을 얻습니다.'),
  h2('예산별 추천'),
  p('1~3만원: 립 제품, 향수 트래블 세트, 다꾸 세트 / 3~5만원: 무드등, 향초 세트, 마스크팩 / 5~10만원: 향수(정품), 스킨케어 세트 / 10만원+: 프리미엄 향수, 브랜드 화장품'),
  h2('마치며'),
  p('고등학생 여자아이는 SNS 트렌드에 민감하므로, 요즘 또래 사이에서 유행하는 아이템을 참고하는 게 도움이 됩니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.'),
]
r6 = requests.patch(f'https://api.notion.com/v1/blocks/{pid2}/children', headers=H, json={'children': B2})
print(f'고등여 {"OK" if r6.status_code==200 else f"FAIL {r6.status_code}"} ({len(B2)} blocks)')
