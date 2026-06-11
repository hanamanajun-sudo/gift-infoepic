import requests, sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

KEY = get_key()
GUIDES_DB = '9603a00b-976b-4791-a129-d5f537e5db06'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}

r = requests.post(f'https://api.notion.com/v1/databases/{GUIDES_DB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'contains': '게임기-선물'}},
    'page_size': 5
})
p = r.json()['results'][0]
PID = p['id']
print(f'ID: {PID}')

requests.patch(f'https://api.notion.com/v1/pages/{PID}', headers=H, json={
    'properties': {'intro': {'rich_text': [{'text': {'content': '게임기 선물, 닌텐도 스위치? PS5? Xbox? 예산과 연령별로 추천하는 게임기와 게임 타이틀을 정리했습니다.'}}]}}
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
print(f'Deleted {len(ids)}')

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
B.append(h2('게임기 선물, 고르기 전에 알아야 할 3가지'))
B.append(p('게임기는 닌텐도 스위치, PS5, Xbox, PC(Steam Deck) 등 종류가 다양해서 처음 고르는 사람은 헷갈리기 쉽습니다. 네이버 쇼핑에서 판매 중인 제품 정보와 실제 사용자 후기를 바탕으로 정리했습니다.'))
B.append(h3('1. 받는 사람이 좋아하는 게임 장르가 가장 중요'))
B.append(p('마리오·젤다·포켓몬 좋아하면 닌텐도 스위치, 갓오브워·라스트오브어스·스파이더맨 좋아하면 PS5, 포르자·헤일로·게임패스 좋아하면 Xbox가 정답입니다.'))
B.append(h3('2. 예산을 본체+게임+악세서리까지 고려'))
B.append(p('본체 외에도 게임 타이틀(개당 3~7만원), 추가 컨트롤러(5~10만원), 온라인 이용권(연 3~5만원)이 추가로 필요합니다. 총 예산을 본체 가격의 1.5배 정도로 잡는 게 현실적입니다.'))
B.append(h3('3. 휴대성 vs 성능'))
B.append(p('이동이 잦다면 닌텐도 스위치(휴대+거치 겸용), 집에서 4K 고화질로 즐기고 싶다면 PS5/Xbox, PC 게임을 휴대하고 싶다면 Steam Deck을 고려하세요.'))
B.append(h2('게임기별 추천'))
B.append(h3('닌텐도 스위치 OLED — 약 45만원'))
B.append(p('가장 대중적인 게임기. 남녀노소 누구나 즐길 수 있는 게임(마리오, 젤다, 동물의 숲, 포켓몬)이 많아 선물용으로 1순위입니다. OLED 모델이 가장 인기고, 라이트 모델(약 25만원, TV 연결 불가)도 있습니다.'))
B.append(h3('PS5 — 약 60~80만원'))
B.append(p('고사양 독점 게임을 즐기고 싶다면 PS5. 디스크 드라이브 있는 모델과 디지털 에디션이 있으며 약 10만원 차이입니다. 게임 타이틀 1개(7만원)와 추가 컨트롤러(듀얼센스 약 8만원)를 함께 추천.'))
B.append(h3('Xbox Series S — 약 40만원 / Series X — 약 70만원'))
B.append(p('게임패스(월 1만원대)로 수백 가지 게임을 즐길 수 있는 게 최대 장점. 가성비와 휴대성을 원하면 S, 4K 고성능을 원하면 X를 선택하세요.'))
B.append(h3('Steam Deck — 약 60만원'))
B.append(p('PC 게임을 휴대용 기기로 즐기고 싶다면 Steam Deck. 이미 PC 게임 라이브러리가 많은 사람에게 특히 좋은 선물입니다.'))
B.append(h2('게임 악세서리 및 타이틀'))
B.append(h3('추가 컨트롤러 — 5~10만원'))
B.append(p('2인용 게임을 즐긴다면 추가 컨트롤러가 필요합니다. 듀얼센스(PS5, 약 8만원), 프로 컨트롤러(스위치, 약 7만원)가 인기.'))
B.append(h3('게임 타이틀 — 3~7만원'))
B.append(p('게임기가 이미 있다면 게임 타이틀만 선물하는 것도 좋습니다. 마인크래프트(디지털 코드, 3만원), 포켓몬 ZA(5~6만원), 젤다의 전설(7만원) 등이 인기입니다.'))
B.append(h3('레이싱휠 — 10~20만원'))
B.append(p('레이싱 게임을 즐기는 사람에게 전용 컨트롤러는 최고의 선물. 트러스트마스터 T98(약 17만원)이 입문용으로 인기입니다.'))
B.append(h2('예산별 추천'))
B.append(bp([('~10만원',True),' 게임 타이틀, 추가 컨트롤러, 게임패스 이용권']))
B.append(bp([('10~30만원',True),' 닌텐도 스위치 라이트(중고), 레이싱휠']))
B.append(bp([('30~50만원',True),' 닌텐도 스위치 OLED, Xbox Series S']))
B.append(bp([('50만원+',True),' PS5, Xbox Series X, Steam Deck']))
B.append(h2('이런 선물은 피하는 게 좋습니다'))
B.append(bp([('본체만 있고 게임이 없는 경우: ',True),'게임기는 본체만으로는 아무것도 할 수 없습니다. 게임 타이틀 1~2개는 꼭 함께 선물하세요.']))
B.append(bp([('취향 모르는 게임 타이틀: ',True),'받는 사람이 좋아하는 장르와 싫어하는 장르를 미리 확인하는 게 중요합니다.']))
B.append(h2('마치며'))
B.append(p('게임기 선물은 가격이 부담스럽지만, 받는 사람이 몇 년 동안 사용한다는 점에서 가성비가 좋은 선물입니다. 네이버 쇼핑과 쿠팡에서 정기적으로 할인하니 알뜰하게 구매하세요.'))
B.append(p('개별 가격은 쿠팡·네이버쇼핑에서 직접 확인하세요.'))

print(f'{len(B)} blocks')
r = requests.patch(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, json={'children': B})
if r.status_code == 200:
    print('OK')
else:
    print(f'FAIL: {r.status_code} {r.text[:200]}')
