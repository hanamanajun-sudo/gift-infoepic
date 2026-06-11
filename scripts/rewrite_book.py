import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

KEY = get_key()
GUIDES_DB = '9603a00b-976b-4791-a129-d5f537e5db06'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}

r = requests.post(f'https://api.notion.com/v1/databases/{GUIDES_DB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'contains': '책-선물'}},
    'page_size': 5
})
p = r.json()['results'][0]
PID = p['id']
print(f'ID: {PID}')

requests.patch(f'https://api.notion.com/v1/pages/{PID}', headers=H, json={
    'properties': {'intro': {'rich_text': [{'text': {'content': '책 선물, 받는 사람이 좋아할 만한 책을 고르는 게 쉽지 않죠. 네이버 블로그에서 추천하는 인기 책 선물과 북액세서리를 정리했습니다.'}}]}}
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
B.append(h2('책 선물, 받는 사람별 추천'))
B.append(p('책 선물은 받는 사람의 상황과 취향을 고려하는 게 중요합니다. 네이버 블로그에서 자주 언급되는 책 선물을 정리했습니다.'))

B.append(h3('임산부·신생아 선물'))
B.append(p('출산을 앞둔 지인에게는 육아책이 정말 유용한 선물입니다. 네이버 블로그에서 많이 추천하는 책은 임신출산육아대백과, 똑게육아, 베이비위스퍼, 삐뽀삐뽀119소아과입니다. 특히 똑게육아는 수면 교육으로 유명하고, 삐뽀삐뽀119는 응급상황 대처법이 잘 정리되어 있어 초보 엄마들에게 인기입니다.'))

B.append(h3('친구·지인 선물'))
B.append(p('카카오톡 선물하기로 책을 보내는 것도 인기입니다. 민음사 세계문학전집(위대한 개츠비 등)은 첫 문장만 보고 골라서 보내는 재미가 있습니다. 타이탄의 도구들은 자기계발에 관심 있는 친구에게 좋습니다. 책갈피나 형광펜이 함께 오는 구성도 있어 포장 걱정이 없습니다.'))

B.append(h3('부모님·어른 선물'))
B.append(p('가정의 달이나 어버이날에는 인문학·에세이 책이 좋습니다. 네이버 블로그에서 5월 가정의 달 선물로 책을 추천하는 글이 많이 올라옵니다. 베스트셀러 에세이나 인문학 책이 무난합니다.'))

B.append(h2('함께 주면 좋은 북액세서리'))
B.append(bp([('책갈피',True),' 힐링쉴드 북마크(2,900원, 리뷰 618), 이태리 가죽 각인 책갈피(9,900원, 리뷰 5,074)']))
B.append(bp([('북커버',True),' 업사이클 북파우치(26,000원) — 책 좋아하는 사람에게 특별한 선물']))
B.append(bp([('문구 세트',True),' 책+투명메모지+형광펜 세트로 보내는 카톡선물하기']))
B.append(h2('마치며'))
B.append(p('책 선물은 단순히 책만 주는 게 아니라 생각을 선물하는 거라고 생각합니다. 받는 사람의 관심사에 맞춰 고르면 훨씬 의미 있는 선물이 됩니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.'))

print(f'{len(B)} blocks')
r = requests.patch(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, json={'children': B})
print(f"{'OK' if r.status_code==200 else f'FAIL {r.status_code}'}")
