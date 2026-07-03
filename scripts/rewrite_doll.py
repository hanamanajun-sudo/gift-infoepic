import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

KEY = get_key()
GUIDES_DB = '9603a00b-976b-4791-a129-d5f537e5db06'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}

r = requests.post(f'https://api.notion.com/v1/databases/{GUIDES_DB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'contains': '인형-선물'}},
    'page_size': 5
})
p = r.json()['results'][0]
PID = p['id']
print(f'ID: {PID}')

requests.patch(f'https://api.notion.com/v1/pages/{PID}', headers=H, json={
    'properties': {'intro': {'rich_text': [{'text': {'content': '인형 선물, 아이에게 줄까? 커플 선물? 집들이? 네이버 쇼핑에서 실제 판매 중인 인기 인형과 가격대를 정리했습니다.'}}]}}
})

ids = []
cur = None
while True:
    pp = {'page_size': 100}
    if cur: pp['start_cursor'] = cur
    r2 = requests.get(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, params=pp)
    d = r2.json()
    ids.extend(b['id'] for b in d.get('results', []))
    if not d.get('has_more'): break
    cur = d.get('next_cursor')
for bid in ids: requests.delete(f'https://api.notion.com/v1/blocks/{bid}', headers=H)

def h2(t): return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t): return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t): return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def bp(pts):
    r = []
    for pt in pts:
        if isinstance(pt,tuple): r.append({'type':'text','text':{'content':pt[0]},'annotations':{'bold':True}})
        else: r.append({'type':'text','text':{'content':pt}})
    return {'object':'block','type':'paragraph','paragraph':{'rich_text':r}}

B = []
B.append(h2('인형 선물, 누구에게 주는지에 따라'))
B.append(p('인형은 아기부터 어른까지 누구나 받기 좋은 선물입니다. 네이버 쇼핑에서 확인한 인기 인형 제품과 용도를 정리했습니다.'))

B.append(h3('아기·유아 애착인형'))
B.append(p('커들앤카인드 리틀 컬렉션 핸드메이드 애착인형(129,000원, 리뷰 112)은 출산 선물로 인기입니다. 슈가버니 소프트 수면 토끼인형(19,000원)은 가성비 좋은 애착인형입니다. 테디비 봉제인형은 블로그에서 애착인형으로 많이 추천하고 있습니다.'))

B.append(h3('아이 장난감 인형'))
B.append(p('코코지 오감발달 세트(216,300원, 리뷰 2,544)는 맘카페에서 난리라는 후기가 많습니다. 콩순이 인형은 3살 두돌 여아 선물로 블로그에서 많이 언급됩니다. 에버랜드 레서판다 베이비인형(13,000원, 리뷰 183)은 가볍고 귀여워서 아이 선물로 부담없습니다.'))

B.append(h3('커플·데이트 선물 인형'))
B.append(p('이젠돌스 노블레빗 토끼 인형(18,000원), 스누즐 낮잠인형(25,000원)은 연인이나 친구에게 주기 좋은 사이즈입니다. 티킷테일즈 포근한 토끼인형(25,000원, 리뷰 53)은 데스크테리어로도 활용 가능합니다.'))

B.append(h3('인테리어·집들이 선물'))
B.append(p('에버랜드 캐릭터 인형이나 디자인이 예쁜 스누즐 인형(25,000원)은 집 인테리어 소품으로도 제격입니다. 집들이 선물로 가볍게 들고 가기 좋습니다.'))

B.append(h2('예산별 추천'))
B.append(bp([('1만원 이하',True),' 작은 키링 인형, 에버랜드 미니인형']))
B.append(bp([('1~2만원',True),' 토끼인형, 애착인형(소형), 봉제인형']))
B.append(bp([('2~5만원',True),' 중형 애착인형, 낮잠인형, 테디비']))
B.append(bp([('5만원+',True),' 핸드메이드 애착인형, 코코지, 대형 인형']))

B.append(h2('마치며'))
B.append(p('인형 선물은 받는 사람의 연령대와 취향을 고려하는 게 가장 중요합니다. 아기에게는 안전한 소재의 애착인형을, 연인에게는 귀여운 디자인을 추천합니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.'))

print(f'{len(B)} blocks')
r = requests.patch(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, json={'children': B})
print(f"{'OK' if r.status_code==200 else f'FAIL {r.status_code}'}")
