import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

KEY = get_key()
GUIDES_DB = '9603a00b-976b-4791-a129-d5f537e5db06'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}

r = requests.post(f'https://api.notion.com/v1/databases/{GUIDES_DB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'contains': '쿠션-선물'}},
    'page_size': 5
})
p = r.json()['results'][0]
PID = p['id']
print(f'ID: {PID}')

requests.patch(f'https://api.notion.com/v1/pages/{PID}', headers=H, json={
    'properties': {'intro': {'rich_text': [{'text': {'content': '쿠션 선물, 소파 인테리어용? 바디필로우? 등받이? 네이버 쇼핑에서 실제 판매 중인 인기 쿠션 제품과 가격대를 정리했습니다.'}}]}}
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
B.append(h2('쿠션 선물, 용도별로 고르는 법'))
B.append(p('쿠션은 종류가 다양해서 같은 이름으로 불러도 실제 제품은 완전히 다릅니다. 네이버 쇼핑에서 판매 중인 쿠션 제품들을 용도별로 나눠 정리했습니다.'))

B.append(h3('소파 인테리어 쿠션'))
B.append(p('소파나 침대에 올려두는 인테리어용 쿠션입니다. 네이버 쇼핑 검색 결과 쥬앤크홈(16,900원), 조브라운 북유럽 스타일(23,000~26,000원), 플리스 쿠션커버(23,400원) 등이 판매 중입니다. 커버만 따로 판매하는 제품이 많아서 선물할 때는 속통이 포함된 제품인지 확인해야 합니다.'))

B.append(h3('바디필로우 (롱쿠션)'))
B.append(p('잠잘 때 안고 자는 긴 베개 형태의 쿠션입니다. 네이버 쇼핑에서 슬로우룸 알러지케어 바디필로우(24,700원) 등이 판매 중입니다. 옆으로 누워 자는 사람에게 특히 좋은 선물입니다.'))

B.append(h3('캐릭터 쿠션'))
B.append(p('모찌모찌 시바견 얼굴 쿠션(15,900원), 데데리트 동물 쿠션 인형(7,700원) 등이 인기입니다. 귀여운 디자인이라 아이들 선물이나 집들이 선물로 좋습니다.'))

B.append(h3('등받이 허리 쿠션'))
B.append(p('의자에 앉아 오래 일하는 사람에게 실용적인 선물입니다. 메모리폼 소재가 인기고, 네이버 쇼핑에서 허리 쿠션 검색 시 1~3만원대 제품이 다양합니다. 의자에 앉아 일하는 직장인이나 수험생에게 추천합니다.'))

B.append(h2('예산별 추천'))
B.append(bp([('~1만원',True),' 캐릭터 쿠션(소형), 동물 인형 쿠션']))
B.append(bp([('1~3만원',True),' 인테리어 쿠션, 등받이 쿠션, 쿠션 커버']))
B.append(bp([('3~5만원',True),' 바디필로우, 대형 인테리어 쿠션 세트']))
B.append(bp([('5만원+',True),' 기능성 쿠션(목/허리), 고급 소재 쿠션']))

B.append(h2('마치며'))
B.append(p('쿠션 선물은 받는 사람이 어떤 용도로 사용할지를 먼저 생각하는 게 중요합니다. 인테리어용인지, 수면용인지, 허리 건강용인지에 따라 선택이 달라집니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.'))

print(f'{len(B)} blocks')
r = requests.patch(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, json={'children': B})
print(f"{'OK' if r.status_code==200 else f'FAIL {r.status_code}'}")
