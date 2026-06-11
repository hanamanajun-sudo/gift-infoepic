import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

KEY = get_key()
GUIDES_DB = '9603a00b-976b-4791-a129-d5f537e5db06'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}

r = requests.post(f'https://api.notion.com/v1/databases/{GUIDES_DB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'contains': '할머니-생신'}},
    'page_size': 5
})
p = r.json()['results'][0]
PID = p['id']
print(f'ID: {PID}')

intro = '할머니 생신선물, 뭘 드려야 좋아하실지 고민이세요? 네이버 쇼핑·블로그에서 인기 있는 할머니 선물 아이템을 정리했습니다.'
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
B.append(h2('할머니 생신선물, 고르기 전에 생각할 3가지'))
B.append(p('할머니 선물은 편안함과 건강, 그리고 특별한 날이라는 느낌을 주는 것이 중요합니다. 네이버 쇼핑에서 인기 있는 할머니 선물 카테고리는 건강식품, 스킨케어, 편안한 의류, 전통 간식 등입니다.'))
B.append(h3('1. 건강과 편안함이 최우선'))
B.append(p('나이가 들수록 건강과 편안함에 대한 관심이 커집니다. 건강기능식품(홍삼, 비타민), 편안한 실내화, 가벼운 목도리 등이 실용적인 선물로 인기입니다.'))
B.append(h3('2. 평소에는 안 사는 특별한 것을'))
B.append(p('할머니는 평소에 자신을 위한 소비를 아끼는 경우가 많습니다. 평소에는 안 사는 좋은 크림, 한과 선물 세트, 따뜻한 목도리 등이 특별한 날 선물로 잘 맞습니다.'))
B.append(h3('3. 예산'))
B.append(bp([('손주·친지 (1~5만원): ',True),'연양갱 세트, 따뜻한 목도리, 핸드크림 세트']))
B.append(bp([('자녀 (5~10만원): ',True),'홍삼 세트, 편한 실내화, 스킨케어 세트']))
B.append(bp([('특별한 날 (10만원+): ',True),'건강검진, 가족 외식, 안마의자(소형)']))

B.append(h2('자주 언급된 선물 아이템'))
B.append(h3('건강기능식품 — 3~10만원대'))
B.append(p('정관장 홍삼 세트, 종합비타민, 오메가3, 관절 건강 제품이 인기입니다. 네이버 쇼핑 리뷰 수천 개 이상의 인기 제품이 많습니다.'))
B.append(h3('스킨케어·핸드크림 세트 — 2~5만원대'))
B.append(p('할머니도 피부 관리를 좋아합니다. 설화수, 이니스프리 등 한방화장품이나 고급 핸드크림 세트가 인기. 평소에는 안 사는 좋은 제품을 선물하면 좋아하십니다.'))
B.append(h3('편안한 실내화·슬리퍼 — 2~5만원대'))
B.append(p('집에서 신는 실내화는 할머니께서 매일 사용하는 실용적인 선물입니다. 발이 편한 기능성 슬리퍼나 푹신한 실내화가 인기입니다.'))
B.append(h3('전통 간식·한과 — 2~5만원대'))
B.append(p('수제 한과 세트, 연양갱, 벌꿀 등이 부담 없는 가격에 드리기 좋습니다. 예쁜 포장이 된 선물 세트를 고르면 더 좋아하십니다.'))
B.append(h3('따뜻한 목도리·숄 — 3~7만원대'))
B.append(p('겨울철에 특히 잘 어울리는 선물. 캐시미어 혼방 목도리나 가벼운 숄이 인기입니다. 색상은 베이지, 브라운, 와인 등 차분한 계열이 무난합니다.'))

B.append(h2('예산별 추천'))
B.append(bp([('~3만원',True),' 연양갱 세트, 핸드크림 세트, 따뜻한 양말']))
B.append(bp([('3~7만원',True),' 홍삼 세트(소형), 편한 실내화, 목도리']))
B.append(bp([('7~10만원',True),' 스킨케어 세트, 건강검진(기본), 전통 한과 선물 세트']))
B.append(bp([('10만원+',True),' 안마의자(소형), 종합 건강검진, 가족 외식']))

B.append(h2('이런 선물은 피하는 게 좋습니다'))
B.append(bp([('조작이 복잡한 전자기기: ',True),'사용법이 어려우면 오히려 부담이 됩니다. 간단한 제품을 선택하세요.']))
B.append(bp([('너무 젊은 스타일의 옷·악세서리: ',True),'할머니 연령대에 맞는 디자인을 고르는 게 중요합니다.']))

B.append(h2('생신 메시지 예시'))
B.append(bp([('자녀가: ',True),'어머니, 생신 축하드려요. 항상 건강하시고 오래오래 곁에 계셔 주세요.']))
B.append(bp([('손주가: ',True),'할머니 생신 축하해요! 항상 건강하시고, 다음에 뵐게요!']))

B.append(h2('마치며'))
B.append(p('할머니 선물의 핵심은 평소에는 안 사는 특별한 것을 드리는 것입니다. 실용적이면서도 특별한 날이라는 느낌이 드는 선물이 가장 좋은 반응을 얻습니다.'))
B.append(p('개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.'))

print(f'{len(B)} blocks')
r = requests.patch(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, json={'children': B})
print(f"{'OK' if r.status_code==200 else f'FAIL {r.status_code}'}")
