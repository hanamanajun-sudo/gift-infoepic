import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

KEY = get_key()
GUIDES_DB = '9603a00b-976b-4791-a129-d5f537e5db06'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}

r = requests.post(f'https://api.notion.com/v1/databases/{GUIDES_DB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'contains': '할아버지-생신'}},
    'page_size': 5
})
p = r.json()['results'][0]
PID = p['id']
print(f'ID: {PID}')

intro = '할아버지 생신선물, 뭘 드려야 좋아하실지 고민되시죠? 네이버 쇼핑에서 인기 있는 할아버지 선물 아이템과 가격대를 정리했습니다.'
requests.patch(f'https://api.notion.com/v1/pages/{PID}', headers=H, json={
    'properties': {'intro': {'rich_text': [{'text': {'content': intro}}]}}
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
B.append(h2('할아버지 생신선물, 고르기 전에 생각할 3가지'))
B.append(p('할아버지 선물은 건강과 편안함에 초점을 맞추는 게 가장 좋습니다. 네이버 쇼핑에서 할아버지 선물로 인기 있는 카테고리는 영양제, 전통 간식, 편한 옷, 벌꿀 등입니다.'))
B.append(h3('1. 건강을 생각한 선물이 1순위'))
B.append(p('나이가 들수록 건강에 대한 관심이 커집니다. 쏘팔메토(전립선 건강), 산양삼, 종합비타민 등 건강기능식품이 할아버지 선물로 가장 인기입니다. 네이버 쇼핑에서도 리뷰 수천 개 이상의 인기 제품이 많습니다.'))
B.append(h3('2. 간단히 즐길 수 있는 간식 선물'))
B.append(p('연양갱, 벌꿀, 전통 한과처럼 부담 없이 드실 수 있는 간식 선물도 인기입니다. 해태 연양갱(20개 11,800원)이나 벌집꿀(33,000~50,000원)이 가격 부담 없이 드리기 좋습니다.'))
B.append(h3('3. 예산'))
B.append(bp([('손주·친지 (1~5만원): ',True),'연양갱 세트, 벌꿀, 전통 간식, 따뜻한 양말·목도리']))
B.append(bp([('자녀 (5~10만원): ',True),'건강기능식품(쏘팔메토, 산양삼), 편한 운동화, 내복·잠옷']))
B.append(bp([('특별한 날 (10만원+): ',True),'건강검진 패키지, 안마의자(소형), 가족 여행(식사)']))

B.append(h2('자주 언급된 선물 아이템'))
B.append(h3('건강기능식품 — 3~10만원대'))
B.append(p('쏘팔메토(전립선 건강, 약 3만원), 산양삼 세트(5만원대), 오메가3, 종합비타민 순으로 인기입니다. 네이버 쇼핑에서 리뷰 5,000~10,000개 이상인 제품들이 많아 신뢰할 수 있습니다.'))
B.append(h3('전통 간식·벌꿀 — 1~5만원대'))
B.append(p('해태 연양갱 20개(11,800원), 벌집꿀(33,000~50,000원), 수제 한과 세트(2~3만원) 등이 부담 없는 가격에 드리기 좋습니다. 드시기도 편하고 건강에도 좋아서 인기입니다.'))
B.append(h3('편한 의류 — 3~10만원대'))
B.append(p('경량 패딩 조끼, 편한 바지, 내복 세트, 따뜻한 실내화 등이 인기. 사이즈를 정확히 알아야 하고, 색상은 무난한 네이비·그레이·블랙 계열이 안전합니다.'))
B.append(h3('목도리·장갑 — 1~3만원대'))
B.append(p('겨울철 할아버지 선물로 부담 없이 드리기 좋습니다. 캐시미어 혼방 목도리나 가죽 장갑이 인기. 색상은 블랙이나 브라운 계열이 무난합니다.'))
B.append(h3('디지털 악세서리 — 3~7만원대'))
B.append(p('요즘 할아버지들도 스마트폰을 많이 사용합니다. 대형 버튼 폰 케이스, 블루투스 스피커, 간단한 무선 이어폰도 실용적인 선물로 인기입니다.'))

B.append(h2('예산별 추천'))
B.append(bp([('~3만원',True),' 연양갱 세트, 벌꿀, 목도리·장갑, 따뜻한 양말']))
B.append(bp([('3~7만원',True),' 건강기능식품, 전통 한과 세트, 편한 실내화']))
B.append(bp([('7~10만원',True),' 산양삼, 경량 패딩 조끼, 건강검진(기본)']))
B.append(bp([('10만원+',True),' 안마의자(소형), 종합 건강검진, 가족 외식']))

B.append(h2('이런 선물은 피하는 게 좋습니다'))
B.append(bp([('조작이 복잡한 전자기기: ',True),'스마트 기기는 사용법이 어려우면 오히려 부담이 됩니다. 간단한 조작의 제품을 선택하세요.']))
B.append(bp([('너무 개인적인 취향(향수·스타일): ',True),'할아버지 취향을 모르면 실패 확률이 높습니다. 무난하고 실용적인 게 최고입니다.']))

B.append(h2('생신 메시지 예시'))
B.append(bp([('자녀가: ',True),'아버지, 생신 축하드려요. 항상 건강하시고 오래오래 함께해 주세요.']))
B.append(bp([('손주가: ',True),'할아버지 생신 축하해요! 항상 건강하시고, 다음에 뵐 때까지 건강하세요!']))

B.append(h2('마치며'))
B.append(p('할아버지 선물의 핵심은 건강과 편안함입니다. 화려한 것보다 실용적이고 오래 쓸 수 있는 선물이 가장 좋은 반응을 얻습니다. 개별 제품의 가격은 쿠팡·네이버쇼핑에서 확인하세요.'))

print(f'{len(B)} blocks')
r = requests.patch(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, json={'children': B})
print(f"{'OK' if r.status_code==200 else f'FAIL {r.status_code}'}")
