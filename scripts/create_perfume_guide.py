import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

K = get_key()
H = {'Authorization': f'Bearer {K}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}
GDB = '9603a00b-976b-4791-a129-d5f537e5db06'

def h2(t): return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t): return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t): return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def plink(pairs):
    rt = []
    for txt, url in pairs:
        if url:
            rt.append({'type':'text','text':{'content':txt,'link':{'url':url}}})
        else:
            rt.append({'type':'text','text':{'content':txt}})
    return {'object':'block','type':'paragraph','paragraph':{'rich_text':rt}}

slug = '향수-처음-고르는-법'
title = '향수 처음 고르는 법 — 선물용 향수, 남자도 쉽게 고르는 방법'
intro = '향수를 선물하고 싶은데 종류도 많고 가격도 천차만별이라 고민이신가요? 향수 종류, 브랜드, 가격대별로 정리했습니다.'

# Check existing
check = requests.post(f'https://api.notion.com/v1/databases/{GDB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'equals': slug}}, 'page_size': 3})
if check.json()['results']:
    print('❌ 슬러그 중복!')
    pid = check.json()['results'][0]['id']
    # Update
    requests.patch(f'https://api.notion.com/v1/pages/{pid}', headers=H, json={
        'properties': {
            'intro': {'rich_text': [{'text': {'content': intro}}]},
            'Title': {'title': [{'text': {'content': title}}]}
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
else:
    print('✅ 신규 생성')
    body = {
        'parent': {'database_id': GDB},
        'properties': {
            'Title': {'title': [{'text': {'content': title}}]},
            'slug': {'rich_text': [{'text': {'content': slug}}]},
            'intro': {'rich_text': [{'text': {'content': intro}}]},
            'published': {'checkbox': True},
        },
        'children': []  # will add below
    }
    r = requests.post('https://api.notion.com/v1/pages', headers=H, json=body)
    pid = r.json()['id'] if r.status_code == 200 else None
    if not pid:
        print(f'❌ 생성 실패: {r.status_code}')
        sys.exit(1)

blocks = [
    h2('향수, 한 번도 사본 적 없는데 괜찮을까요?'),
    p('네, 괜찮습니다. 향수는 생각보다 고르기 어렵지 않아요. 몇 가지 기본 원칙만 알면 누구나 선물용 향수를 고를 수 있습니다.'),

    h2('향수의 종류 — 이 정도만 알면 됩니다'),
    p('향수는 향료 농도에 따라 지속시간과 가격이 달라집니다:'),
    p('• 오드퍼퓸(EDP): 향료 15~20%, 지속 5~8시간. ✅ 선물용으로 가장 추천'),
    p('• 오드뚜왈렛(EDT): 향료 5~15%, 지속 3~5시간. 가벼운 선물용'),
    p('• 오드코롱(EDC): 향료 3~5%, 지속 1~2시간. 여름용이나 스포츠용'),
    p('선물용으로는 EDP(오드퍼퓸)이 가장 무난합니다. 지속력이 길어서 받는 사람이 오래 즐길 수 있어요.'),

    h2('향의 종류 — 어떤 향이 무난할까요?'),
    p('향수를 처음 선물한다면 아래 향이 가장 실패할 확률이 낮습니다:'),
    h3('플로럴 계열 (여성용)'),
    p('장미·라벤더·자스민 등 꽃 향기. 여성 향수의 대표주자로 누구에게나 무난합니다.'),

    h3('시트러스 계열 (공용)'),
    p('레몬·오렌지·자몽 등 상큼한 향. 남녀 모두에게 잘 어울리고 부담이 가장 적습니다.'),

    h3('우디 계열 (남성용)'),
    p('삼나무·백단향 등 나무 향. 남성 향수에서 가장 흔하게 볼 수 있습니다.'),

    h2('선물용 향수, 이 브랜드면 실패 없음'),
    h3('여성에게'),
    p('조말론 잉글리쉬페어앤프리지아(13만원대) — 은은한 프루티 플로럴로 첫 향수 선물 1순위입니다.'),
    p('딥디크 플뢰르 드 뽀(75ml, 15만원대) — 장미 베이스의 우아한 향.'),
    p('랑콤 la vie est belle(10만원대) — 달콤한 플로럴로 20~30대 여성에게 인기.'),

    h3('남성에게'),
    p('알파무드 퍼펙트(79,000원) — 10~20대 남성에게 인기. 가성비 좋은 첫 향수.'),
    p('샤넬 블루 드 샤넬(100ml, 13만원대) — 남성 향수의 정석.'),
    p('디올 소바쥬(100ml, 12만원대) — 시원하면서도 세련된 향.'),

    h3('부담 없이 시작한다면 — 트래블 세트'),
    p('브랜드에서 출시하는 트래블 세트(3~7만원대)는 여러 향을 작은 용량으로 즐길 수 있어서 첫 향수 선물로 가장 안전합니다. 조말론, 바이레도, 알파무드 등에서 출시하고 있습니다.'),

    h2('향수 선물, 이것만 주의하세요'),
    p('① 향수는 개인 취향이 강합니다. 평소 상대방이 사용하는 향이나 좋아하는 향을 참고하세요.'),
    p('② 처음이라면 트래블 세트나 30ml 용량이 부담이 적습니다.'),
    p('③ 면세점보다 네이버 쇼핑이나 쿠팡이 가격이 더 저렴한 경우도 있습니다.'),

    h2('참고하면 좋은 사이트'),
    plink([('• 올리브영', 'https://www.oliveyoung.co.kr'), (' — 향수 판매량 랭킹 확인', None)]),
    plink([('• 화해', 'https://www.hwahae.co.kr'), (' — 성분과 사용자 리뷰', None)]),
    plink([('• 글로우픽', 'https://www.glowpick.com'), (' — 향수 카테고리 리뷰', None)]),

    h2('마치며'),
    p('향수는 고민할수록 어려워지는 선물입니다. 기본 원칙만 지키면 생각보다 쉽습니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.'),
]

r3 = requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children', headers=H, json={'children': blocks})
print(f'{"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"} ({len(blocks)} blocks)')
