import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

KEY = get_key()
GUIDES_DB = '9603a00b-976b-4791-a129-d5f537e5db06'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}

r = requests.post(f'https://api.notion.com/v1/databases/{GUIDES_DB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'contains': '헤드폰-선물'}},
    'page_size': 5
})
p = r.json()['results'][0]
PID = p['id']
print(f'ID: {PID}')

requests.patch(f'https://api.notion.com/v1/pages/{PID}', headers=H, json={
    'properties': {'intro': {'rich_text': [{'text': {'content': '헤드폰 선물, 어떤 제품이 좋을까요? 네이버 쇼핑에서 실제 판매 중인 인기 헤드폰과 가격대를 정리했습니다.'}}]}}
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
B.append(h2('헤드폰 선물, 종류별로 살펴보기'))
B.append(p('헤드폰은 사용 목적과 예산에 따라 선택이 갈립니다. 네이버 쇼핑에서 확인한 인기 헤드폰 제품들을 정리했습니다.'))

B.append(h3('프리미엄 블루투스 헤드폰'))
B.append(p('젠하이저 엑센텀 블루투스 무선 헤드폰(171,000원)이 네이버 쇼핑에서 리뷰 755개로 가장 인기입니다. 음질과 브랜드 모두 만족도가 높습니다. 블랙/화이트 두 가지 색상이 있습니다.'))

B.append(h3('가성비 노이즈캔슬링 헤드폰'))
B.append(p('브리츠 ANC1000XL4(79,900원, 리뷰 154)와 에이투 플레이5(59,900원, 리뷰 284)가 가성비가 좋습니다. 두 제품 모두 ANC(노이즈캔슬링)를 지원하고 블루투스 5.3을 탑재했습니다. 가격 부담이 적으면서도 기능이 충실해서 선물용으로 좋습니다.'))

B.append(h3('모니터링 헤드폰'))
B.append(p('슈어 SRH840A(245,000원)와 SRH440A(163,000원)는 음악 작업용 모니터링 헤드폰입니다. 음질에 진심인 사람에게 좋은 선물입니다. 리뷰 평점도 4.9로 매우 높습니다.'))

B.append(h3('어린이·학습용 헤드폰'))
B.append(p('마이퍼스트 BCL 어학용 골전도 헤드셋(69,000원, 리뷰 213)은 아이들 선물로 적합합니다. 골전도 방식이라 귀가 편하고 어학 학습에 활용하기 좋습니다.'))

B.append(h2('예산별 추천'))
B.append(bp([('5~8만원',True),' 브리츠 ANC, 에이투 플레이5 (가성비 좋음)']))
B.append(bp([('8~15만원',True),' 중급 블루투스 헤드폰, 게이밍 헤드셋']))
B.append(bp([('15~20만원',True),' 젠하이저 엑센텀, 음질 좋은 무선 헤드폰']))
B.append(bp([('20만원+',True),' 슈어 SRH840A, 소니 WH-1000XM, 프리미엄급']))

B.append(h2('마치며'))
B.append(p('헤드폰 선물은 받는 사람이 어디에 사용할지를 먼저 생각하는 게 중요합니다. 음악 감상용, 업무용, 학습용에 따라 선택이 완전히 달라집니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.'))

print(f'{len(B)} blocks')
r = requests.patch(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, json={'children': B})
print(f"{'OK' if r.status_code==200 else f'FAIL {r.status_code}'}")
