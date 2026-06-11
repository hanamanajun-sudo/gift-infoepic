import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

K = get_key()
H = {'Authorization': f'Bearer {K}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}
GDB = '9603a00b-976b-4791-a129-d5f537e5db06'

def h2(t): return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t): return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t): return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}

rels = [
    ('아빠-생일선물', '아빠 생일선물, 건강과 편안함을 생각한 선물을 네이버 쇼핑에서 찾았습니다.',
     [h2('아빠 생일선물, 건강과 편안함'),p('아빠는 대부분 필요한 게 있어도 본인이 사는 편이라 선물 고르기가 어렵습니다. 네이버 쇼핑에서 아빠 선물로 인기 있는 아이템입니다.'),h3('건강기능식품'),p('정관장 에브리타임(12만원대), 산양삼(49,800원) 등 건강기능식품이 아빠 선물 1순위입니다. 매일 챙겨 드실 수 있는 스틱형 제품이 인기입니다.'),h3('편안한 아이템'),p('목 어깨 안마기, 발 마사지기, 편한 실내화 등 피로를 풀어주는 아이템이 좋습니다. 매트리스(센스맘)도 아빠 선물로 인기입니다.'),h3('꽃·떡케이크'),p('나인플라워 꽃배달, 엠케이크 떡케이크 등 이벤트성 선물도 좋습니다. 직접 전달하는 자리에서 깜짝 이벤트를 하면 큰 감동을 줍니다.'),h2('마치며'),p('아빠 선물은 평소에 아빠가 불편해하거나 필요하다고 말한 적이 있는 걸 떠올려보는 게 가장 좋습니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]),
    ('엄마-생일선물', '엄마 생일선물, 건강과 힐링을 생각한 선물을 네이버 쇼핑에서 찾았습니다.',
     [h2('엄마 생일선물'),p('엄마는 가족을 위해 자신을 희생하는 경우가 많습니다. 평소 엄마가 필요하다고 말한 적이 있는 선물이 가장 좋습니다.'),h3('건강기능식품'),p('정관장 에브리타임, 침향환, 종합비타민 등 건강식품이 엄마 선물로 인기입니다. 선물세트 포장이 되어 있어 따로 포장할 필요가 없습니다.'),h3('힐링 아이템'),p('디퓨저, 캔들, 마사지기 등 엄마의 피로를 풀어주는 아이템이 좋습니다. 스킨케어 세트(설화수, AHC)도 인기입니다.'),h3('꽃·케이크'),p('꽃다발이나 떡케이크는 엄마에게 가장 큰 감동을 주는 선물입니다. 직접 전하는 자리에서 함께 드리면 더 좋습니다.'),h2('마치며'),p('엄마 선물은 물건보다 마음이 중요합니다. 직접 안아드리는 것만으로도 큰 선물이 됩니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]),
    ('여자친구-생일선물', '여자친구 생일선물, 센스 있는 선택을 네이버 쇼핑에서 찾았습니다.',
     [h2('여자친구 선물'),p('여자친구 선물은 평소 그녀가 좋아하는 브랜드나 아이템을 떠올려보는 게 가장 중요합니다.'),h3('향수'),p('조말론, 딥디크, 알파무드 등 인기 향수가 좋습니다. 트래블 세트는 부담 없이 여러 향을 시도해볼 수 있습니다.'),h3('액세서리'),p('귀걸이, 목걸이, 팔찌 등 패션 주얼리(1~10만원대)가 인기입니다. 평소 스타일을 고려해야 합니다.'),h3('화장품'),p('디올 립글로우, 설화수 기초 세트 등 그녀가 좋아하는 브랜드의 제품이 가장 좋습니다.'),h2('마치며'),p('여자친구 선물은 가격보다 그녀의 취향을 얼마나 잘 알고 있느냐가 중요합니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]),
    ('남자친구-생일선물', '남자친구 생일선물, 실용적이면서 센스 있는 아이템을 네이버 쇼핑에서 찾았습니다.',
     [h2('남자친구 선물'),p('남자친구 선물은 평소 그가 좋아하는 취미나 관심사를 기준으로 고르는 게 좋습니다.'),h3('전자기기'),p('무선 이어폰, 게이밍 마우스, 보조배터리 등 디지털 기기가 가장 인기입니다.'),h3('향수'),p('알파무드, 샤넬 블루, 디올 소바쥬 등 향수는 남자친구 선물로 정석입니다.'),h3('패션'),p('스니커즈, 지갑, 백팩, 시계 등 실용 패션 아이템도 좋습니다.'),h2('마치며'),p('남자친구가 평소에 갖고 싶다고 말한 적이 있는 걸 기억해보세요. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]),
]

for slug, intro, blocks in rels:
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
