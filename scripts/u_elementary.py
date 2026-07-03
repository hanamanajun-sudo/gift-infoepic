import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

K = get_key()
H = {'Authorization': f'Bearer {K}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}
GDB = '9603a00b-976b-4791-a129-d5f537e5db06'

def h2(t): return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t): return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t): return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}

jobs = [
    ('초등학생-저학년-선물', '초등학생 저학년 선물, 뭘 사줘야 아이가 좋아할까? 네이버 쇼핑에서 인기 있는 아이템을 정리했습니다.',
     [h2('초등학생 저학년 선물, 장난감과 교구 사이'),p('초등 1~3학년은 아직 장난감을 좋아하지만 학습 능력도 키우기 시작하는 시기입니다. 네이버 쇼핑에서 인기 아이템을 정리했습니다.'),
      h3('보드게임'),p('루미큐브 클래식(35,200원, 리뷰 5,372)과 꼬치의달인(29,900원, 리뷰 9,999+)이 가장 인기입니다. 온 가족이 함께 즐길 수 있고 두뇌 발달에도 좋아 선물용으로 인기가 많습니다.'),
      h3('슬라임·촉감놀이'),p('띵이슬라임 수제 슬라임(6,900원, 리뷰 6,034)은 스트레스 해소와 촉감 놀이에 좋습니다. 아이들이 정말 좋아하지만 옷에 묻지 않도록 주의해야 합니다.'),
      h3('문구세트'),p('카카오프렌즈 문구세트(5,800원, 리뷰 9,899)는 가성비 최고의 선물입니다. 연필, 지우개, 공책 등 실용적인 구성이라 학부모님도 좋아합니다.'),
      h3('닌텐도 게임'),p('포켓몬 ZA(54,800원, 리뷰 2,542)는 닌텐도 스위치가 있는 아이에게 인기입니다. 다만 게임기는 별도로 있어야 해서 사전 확인이 필요합니다.'),
      h3('자전거'),p('로얄키즈 클래식 어린이자전거 16인치(224,000원, 리뷰 1,075)는 활동적인 아이에게 좋은 선물입니다. 99% 조립 배송으로 부모님 수고가 적습니다.'),
      h2('예산별'),p('1만원 이하: 슬라임, 문구세트 / 1~3만원: 보드게임(소형), 캐릭터 인형 / 3~5만원: 보드게임(대형), 과학키트 / 5만원+: 닌텐도 게임, 자전거, 로봇 장난감'),
      h2('마치며'),p('초등 저학년은 아직 취향이 명확하지 않아서 보드게임이나 문구세트처럼 여러 명이 함께 즐길 수 있는 선물이 무난합니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]),
    ('7세-여자아이-생일선물', '7세 여자아이 생일선물, 예쁘고 재미있는 걸 고르려면? 네이버 쇼핑에서 인기 아이템을 정리했습니다.',
     [h2('7세 여자아이 선물'),p('7세는 초등학교 입학 전후로 새로운 취미가 생기는 시기입니다.'),
      h3('캐릭터 인형·소품'),p('산리오(시나모롤·쿠로미)나 포켓몬 캐릭터 인형이 인기입니다. 네이버 쇼핑에서 1~3만원대.'),
      h3('보드게임·놀이'),p('루미큐브 주니어, 젠가 등 가족이 함께 할 수 있는 보드게임이 좋습니다.'),
      h3('문구·미술세트'),p('카카오프렌즈 문구세트, 색연필 세트, 스티커 북 등이 부담 없는 선물로 좋습니다.'),
      h2('예산별'),p('1만원 이하: 스티커북, 문구세트 / 1~3만원: 캐릭터 인형, 색연필 세트 / 3~5만원: 보드게임, 과학놀이키트'),
      h2('마치며'),p('7세 여아는 아직 취향이 다양한 편이라 예쁘고 귀여운 디자인의 제품이 무난합니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]),
    ('7세-남자아이-생일선물', '7세 남자아이 생일선물, 활동적이고 재미있는 걸 고르려면? 네이버 쇼핑에서 인기 아이템을 정리했습니다.',
     [h2('7세 남자아이 선물'),p('7세 남아는 활동적인 놀이를 좋아하는 시기입니다.'),
      h3('RC카·미니카'),p('네이버 쇼핑에서 RC카(1~3만원대)와 미니카 세트가 인기입니다.'),
      h3('보드게임'),p('루미큐브, 할리갈리 등 간단한 규칙의 보드게임이 좋습니다.'),
      h3('과학키트·블록'),p('레고(3~5만원대)나 간단한 과학 실험 키트가 창의력 발달에 좋습니다.'),
      h2('예산별'),p('1만원 이하: 미니카, 문구세트 / 1~3만원: RC카, 블록 / 3~5만원: 레고, 보드게임 / 5만원+: 닌텐도 게임'),
      h2('마치며'),p('7세 남아는 활동적인 장난감이 가장 좋은 반응을 보입니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]),
]

for slug, intro, blocks in jobs:
    r = requests.post(f'https://api.notion.com/v1/databases/{GDB}/query', headers=H, json={
        'filter': {'property': 'slug', 'rich_text': {'contains': slug}}, 'page_size': 3})
    pid = r.json()['results'][0]['id']
    print(f'{slug}: {pid}')
    requests.patch(f'https://api.notion.com/v1/pages/{pid}', headers=H, json={
        'properties': {'intro': {'rich_text': [{'text': {'content': intro}}]}}})
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
    r3 = requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children', headers=H, json={'children': blocks})
    print(f'  {"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"}')
