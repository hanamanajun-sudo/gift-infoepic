import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

K = get_key()
H = {'Authorization': f'Bearer {K}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}
GDB = '9603a00b-976b-4791-a129-d5f537e5db06'

def h2(t): return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t): return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t): return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}

# 1. 13-15세 여자아이 → 14-15세 여자아이
slug_old = '13-15세-여자아이-생일선물'
slug_new = '14-15세-여자아이-생일선물'
title_new = '14~15세 여자아이 생일선물 추천'
intro_new = '14세 15세 여자아이 생일선물, 중학생 딸을 위한 센스 있는 선물을 소개합니다.'

r = requests.post(f'https://api.notion.com/v1/databases/{GDB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'contains': slug_old}}, 'page_size': 3})
pid = r.json()['results'][0]['id']
print(f'1. {slug_old} → {slug_new}')
requests.patch(f'https://api.notion.com/v1/pages/{pid}', headers=H, json={
    'properties': {
        'slug': {'rich_text': [{'text': {'content': slug_new}}]},
        'intro': {'rich_text': [{'text': {'content': intro_new}}]},
        'Title': {'title': [{'text': {'content': title_new}}]},
    }})
ids=[];c=None
while True:
    pp={'page_size':100}
    if c:pp['start_cursor']=c
    r2=requests.get(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,params=pp);d=r2.json()
    ids.extend(b['id'] for b in d.get('results',[]))
    if not d.get('has_more'):break
    c=d.get('next_cursor')
for b in ids:requests.delete(f'https://api.notion.com/v1/blocks/{b}',headers=H)
B1 = [
    h2('14~15세 여자아이, 중학생 라이프'),
    p('14~15세는 중학생 2~3학년으로 자기 표현 욕구가 강해지고 SNS와 또래 문화에 민감합니다. 14세 생일은 특히 중요한 이정표입니다.'),
    h3('향수'),
    p('알파무드, 조말론 트래블 세트(3~7만원대) 등 첫 향수 선물이 인기입니다. 특히 14세 여자아이는 친구들을 의식하기 시작하는 나이라 브랜드에 민감할 수 있습니다.'),
    h3('뷰티'),
    p('립 제품, 마스크팩, 스킨케어 세트 등이 좋습니다. 롬앤, 어뮤즈 등 10대 인기 브랜드가 14~15세 여자아이에게 가장 좋은 반응을 얻습니다.'),
    h3('감성 아이템'),
    p('무드등, 인스탁스 카메라, 다꾸 세트 등 인스타 감성 아이템이 인기입니다.'),
    h2('예산별'),
    p('1~3만원: 립 제품, 다꾸 세트 / 3~7만원: 향수 트래블 세트 / 7만원+: 무선 이어폰, 인스탁스'),
    h2('마치며'),
    p('14세는 어린이와 청소년의 경계에 있는 특별한 나이입니다. 그 점을 고려한 선물이 가장 좋습니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.'),
]
r3=requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,json={'children':B1})
print(f'  {"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"}')

# 2. 13-15세 남자아이 → 14-15세 남자아이
slug_old2 = '13-15세-남자아이-생일선물'
slug_new2 = '14-15세-남자아이-생일선물'
title_new2 = '14~15세 남자아이 생일선물 추천'
intro_new2 = '14세 15세 남자아이 생일선물, 중학생 아들을 위한 실용적인 선물을 소개합니다.'

r = requests.post(f'https://api.notion.com/v1/databases/{GDB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'contains': slug_old2}}, 'page_size': 3})
pid2 = r.json()['results'][0]['id']
print(f'2. {slug_old2} → {slug_new2}')
requests.patch(f'https://api.notion.com/v1/pages/{pid2}', headers=H, json={
    'properties': {
        'slug': {'rich_text': [{'text': {'content': slug_new2}}]},
        'intro': {'rich_text': [{'text': {'content': intro_new2}}]},
        'Title': {'title': [{'text': {'content': title_new2}}]},
    }})
ids2=[];c2=None
while True:
    pp={'page_size':100}
    if c2:pp['start_cursor']=c2
    r2=requests.get(f'https://api.notion.com/v1/blocks/{pid2}/children',headers=H,params=pp);d2=r2.json()
    ids2.extend(b['id'] for b in d2.get('results',[]))
    if not d2.get('has_more'):break
    c2=d2.get('next_cursor')
for b in ids2:requests.delete(f'https://api.notion.com/v1/blocks/{b}',headers=H)
B2 = [
    h2('14~15세 남자아이, 중학생 라이프'),
    p('14~15세 남아는 중학생으로 외모와 자기 관리에 관심이 생기기 시작합니다. 14세 생일부터는 선물의 수준이 달라져야 합니다.'),
    h3('전자기기'),
    p('무선 이어폰(에어팟/갤럭시버즈), 보조배터리, 게이밍 마우스 등이 가장 인기입니다.'),
    h3('향수'),
    p('알파무드, 포맨트 등 10대 남성 향수가 인기입니다. 자기 관리에 관심이 생기는 나이에 좋은 선물입니다.'),
    h3('운동화'),
    p('조던, 나이키 등 인기 운동화 브랜드가 좋습니다. 14~15세는 브랜드에 민감해지는 시기이니 취향 확인이 필수입니다.'),
    h2('예산별'),
    p('1~3만원: 향수, 보조배터리 / 3~5만원: 게이밍 마우스 / 5~10만원: 무선 이어폰 / 10만원+: 운동화'),
    h2('마치며'),
    p('개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.'),
]
r3=requests.patch(f'https://api.notion.com/v1/blocks/{pid2}/children',headers=H,json={'children':B2})
print(f'  {"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"}')

# 3. 16-19세 남자아이 → 17-19세 남자아이
slug_old3 = '16-19세-남자아이-생일선물'
slug_new3 = '17-19세-남자아이-생일선물'
title_new3 = '17~19세 남자아이 생일선물 추천'
intro_new3 = '17세 18세 19세 남자아이 생일선물, 고등학생부터 성인 직전까지 실용적인 선물을 소개합니다.'

r = requests.post(f'https://api.notion.com/v1/databases/{GDB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'contains': slug_old3}}, 'page_size': 3})
pid3 = r.json()['results'][0]['id']
print(f'3. {slug_old3} → {slug_new3}')
requests.patch(f'https://api.notion.com/v1/pages/{pid3}', headers=H, json={
    'properties': {
        'slug': {'rich_text': [{'text': {'content': slug_new3}}]},
        'intro': {'rich_text': [{'text': {'content': intro_new3}}]},
        'Title': {'title': [{'text': {'content': title_new3}}]},
    }})
ids3=[];c3=None
while True:
    pp={'page_size':100}
    if c3:pp['start_cursor']=c3
    r2=requests.get(f'https://api.notion.com/v1/blocks/{pid3}/children',headers=H,params=pp);d3=r2.json()
    ids3.extend(b['id'] for b in d3.get('results',[]))
    if not d3.get('has_more'):break
    c3=d3.get('next_cursor')
for b in ids3:requests.delete(f'https://api.notion.com/v1/blocks/{b}',headers=H)
B3 = [
    h2('17~19세 남자아이, 취향이 확실한 나이'),
    p('17~19세는 고등학생에서 성인이 되는 중요한 시기입니다. 자신의 취향이 확실하고 브랜드에도 민감합니다.'),
    h3('향수'),
    p('알파무드, 샤넬 블루, 디올 소바쥬 등 브랜드 향수가 가장 인기 있는 선물입니다.'),
    h3('전자기기'),
    p('무선 이어폰, 스마트워치, 게이밍 기어(키보드, 마우스, 헤드셋) 등이 인기입니다.'),
    h3('패션'),
    p('운동화, 백팩, 지갑, 시계 등 브랜드 패션 아이템이 좋습니다. 18세 성인 이후에는 면도기나 향수도 좋습니다.'),
    h2('예산별'),
    p('3~5만원: 향수, 게이밍 마우스 / 5~10만원: 무선 이어폰 / 10~20만원: 운동화, 스마트워치'),
    h2('마치며'),
    p('17~19세는 성인으로 가는 길목입니다. 선물에도 어른스러운 느낌을 주는 게 좋습니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.'),
]
r3=requests.patch(f'https://api.notion.com/v1/blocks/{pid3}/children',headers=H,json={'children':B3})
print(f'  {"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"}')

print('\n✅ 3개 그룹 수정 완료')
