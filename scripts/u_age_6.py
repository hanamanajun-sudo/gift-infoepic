import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

K = get_key()
H = {'Authorization': f'Bearer {K}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}
GDB = '9603a00b-976b-4791-a129-d5f537e5db06'

def h2(t): return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t): return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t): return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}

import time

# 30대 아빠
slug='30대-아빠-생일선물'
r=requests.post(f'https://api.notion.com/v1/databases/{GDB}/query',headers=H,json={'filter':{'property':'slug','rich_text':{'contains':slug}},'page_size':3})
pid=r.json()['results'][0]['id']; print(f'{slug}: {pid}')
requests.patch(f'https://api.notion.com/v1/pages/{pid}',headers=H,json={'properties':{'intro':{'rich_text':[{'text':{'content':'30대 아빠 생일선물, 실용적이면서 감동을 줄 선물을 네이버 쇼핑에서 찾았습니다.'}}]}}})
ids=[];cur=None
while True:
    pp={'page_size':100}
    if cur:pp['start_cursor']=cur
    r2=requests.get(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,params=pp)
    d=r2.json()
    ids.extend(b['id'] for b in d.get('results',[]))
    if not d.get('has_more'):break
    cur=d.get('next_cursor')
for bid in ids:requests.delete(f'https://api.notion.com/v1/blocks/{bid}',headers=H)
B=[h2('30대 아빠 선물, 실용적인 게 최고'),p('30대 아빠는 육아와 직장 생활로 가장 바쁜 시기입니다. 네이버 쇼핑 인기 아이템을 정리했습니다.'),h3('지갑·카드지갑'),p('수제 가죽 카드지갑(48,000원), 그레이그레이 메이트 지갑(47,000원)이 인기입니다. 매일 사용하는 실용적인 선물입니다.'),h3('명함케이스'),p('자개 명함케이스(11,500원, 리뷰 216)는 직장인 아빠에게 좋습니다. 나전칠기 디자인이 고급스럽습니다.'),h3('건강·휴식'),p('목 어깨 안마기(3~5만원대), 건강기능식품도 30대 아빠에게 인기입니다.'),h2('용돈 이벤트'),p('네이버 쇼핑에서 반전 용돈통장(11,900원, 리뷰 958)이 인기입니다. 깜짝 이벤트는 큰 감동을 줍니다.'),h2('마치며'),p('개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]
r3=requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,json={'children':B})
print(f'{"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"}')
time.sleep(1)

# 40대 엄마
slug='40대-엄마-생일선물'
r=requests.post(f'https://api.notion.com/v1/databases/{GDB}/query',headers=H,json={'filter':{'property':'slug','rich_text':{'contains':slug}},'page_size':3})
pid=r.json()['results'][0]['id']; print(f'{slug}: {pid}')
requests.patch(f'https://api.notion.com/v1/pages/{pid}',headers=H,json={'properties':{'intro':{'rich_text':[{'text':{'content':'40대 엄마 생일선물, 건강과 힐링을 생각한 선물을 정리했습니다.'}}]}}})
ids=[];cur=None
while True:
    pp={'page_size':100}
    if cur:pp['start_cursor']=cur
    r2=requests.get(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,params=pp)
    d=r2.json()
    ids.extend(b['id'] for b in d.get('results',[]))
    if not d.get('has_more'):break
    cur=d.get('next_cursor')
for bid in ids:requests.delete(f'https://api.notion.com/v1/blocks/{bid}',headers=H)
B=[h2('40대 엄마 선물, 건강과 힐링'),p('40대 엄마는 가족 돌보느라 자신을 챙길 시간이 부족합니다.'),h3('건강기능식품'),p('홍삼, 침향환, 종합비타민이 인기입니다. 정관장 홍삼 세트(5~10만원대), 종근당 침향환 등이 있습니다.'),h3('힐링 아이템'),p('마사지기, 아로마 디퓨저, 목욕용품 세트 등이 엄마 선물로 인기입니다.'),h3('액세서리'),p('진주 목걸이, 스카프, 실크 손수건 등도 좋은 선물입니다.'),h2('마치며'),p('엄마가 평소 필요하다고 말한 적이 있는지 떠올려보세요. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]
r3=requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,json={'children':B})
print(f'{"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"}')
time.sleep(1)

# 50대 부모님
slug='50대-부모님-생일선물'
r=requests.post(f'https://api.notion.com/v1/databases/{GDB}/query',headers=H,json={'filter':{'property':'slug','rich_text':{'contains':slug}},'page_size':3})
pid=r.json()['results'][0]['id']; print(f'{slug}: {pid}')
requests.patch(f'https://api.notion.com/v1/pages/{pid}',headers=H,json={'properties':{'intro':{'rich_text':[{'text':{'content':'50대 부모님 생일선물, 건강을 먼저 생각하는 선물입니다.'}}]}}})
ids=[];cur=None
while True:
    pp={'page_size':100}
    if cur:pp['start_cursor']=cur
    r2=requests.get(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,params=pp)
    d=r2.json()
    ids.extend(b['id'] for b in d.get('results',[]))
    if not d.get('has_more'):break
    cur=d.get('next_cursor')
for bid in ids:requests.delete(f'https://api.notion.com/v1/blocks/{bid}',headers=H)
B=[h2('50대 부모님 선물, 건강이 최우선'),p('50대는 건강 관리가 중요한 시기입니다.'),h3('건강기능식품'),p('홍삼, 침향환, 녹용, 오메가3, 관절 영양제 등이 대표적입니다. 정관장, 종근당, 녹십자웰빙 브랜드가 네이버 쇼핑에서 인기입니다.'),h3('안마·마사지'),p('목 어깨 안마기(3~10만원대), 발 마사지기, 안마의자까지 예산에 따라 선택 가능합니다.'),h3('의류·패션'),p('편한 운동화, 등산복, 기능성 내의 등 활동적인 부모님께 실용적입니다.'),h2('마치며'),p('부모님의 건강과 생활을 생각한 선물이 가장 기억에 남습니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]
r3=requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,json={'children':B})
print(f'{"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"}')
time.sleep(1)

# 20대 남성
slug='20대-남성-생일선물'
r=requests.post(f'https://api.notion.com/v1/databases/{GDB}/query',headers=H,json={'filter':{'property':'slug','rich_text':{'contains':slug}},'page_size':3})
pid=r.json()['results'][0]['id']; print(f'{slug}: {pid}')
requests.patch(f'https://api.notion.com/v1/pages/{pid}',headers=H,json={'properties':{'intro':{'rich_text':[{'text':{'content':'20대 남성 생일선물, 트렌디하고 실용적인 아이템을 정리했습니다.'}}]}}})
ids=[];cur=None
while True:
    pp={'page_size':100}
    if cur:pp['start_cursor']=cur
    r2=requests.get(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,params=pp)
    d=r2.json()
    ids.extend(b['id'] for b in d.get('results',[]))
    if not d.get('has_more'):break
    cur=d.get('next_cursor')
for bid in ids:requests.delete(f'https://api.notion.com/v1/blocks/{bid}',headers=H)
B=[h2('20대 남성 선물'),p('20대 남성은 패션과 디지털에 관심이 많습니다.'),h3('전자기기'),p('무선 이어폰(에어팟/갤럭시버즈 10~20만원대), 보조배터리, 게이밍 마우스가 인기입니다.'),h3('향수'),p('알파무드, 조말론, 샤넬 블루 등 향수도 좋은 선물입니다.'),h3('패션'),p('스니커즈, 백팩, 지갑 등 실용 패션 아이템도 좋습니다.'),h2('마치며'),p('개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]
r3=requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,json={'children':B})
print(f'{"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"}')
time.sleep(1)

# 30대 엄마
slug='30대-엄마-생일선물'
r=requests.post(f'https://api.notion.com/v1/databases/{GDB}/query',headers=H,json={'filter':{'property':'slug','rich_text':{'contains':slug}},'page_size':3})
pid=r.json()['results'][0]['id']; print(f'{slug}: {pid}')
requests.patch(f'https://api.notion.com/v1/pages/{pid}',headers=H,json={'properties':{'intro':{'rich_text':[{'text':{'content':'30대 엄마 생일선물, 육아로 지친 엄마를 위한 힐링 선물입니다.'}}]}}})
ids=[];cur=None
while True:
    pp={'page_size':100}
    if cur:pp['start_cursor']=cur
    r2=requests.get(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,params=pp)
    d=r2.json()
    ids.extend(b['id'] for b in d.get('results',[]))
    if not d.get('has_more'):break
    cur=d.get('next_cursor')
for bid in ids:requests.delete(f'https://api.notion.com/v1/blocks/{bid}',headers=H)
B=[h2('30대 엄마 선물'),p('30대 엄마는 육아로 가장 바쁜 시기입니다.'),h3('디퓨저·캔들'),p('집에서 편안하게 쉴 수 있는 아로마 디퓨저나 향초가 좋습니다. 플렌느 디퓨저(18,700원) 등이 인기입니다.'),h3('스킨케어'),p('AHC, 라네즈 등 기초 화장품 세트(3~8만원대)가 무난합니다.'),h3('주방가전'),p('에어프라이어, 믹서기 등 간편식 주방가전도 실용적인 선물입니다.'),h2('마치며'),p('개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]
r3=requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,json={'children':B})
print(f'{"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"}')
time.sleep(1)

# 20대 여성
slug='20대-여성-생일선물'
r=requests.post(f'https://api.notion.com/v1/databases/{GDB}/query',headers=H,json={'filter':{'property':'slug','rich_text':{'contains':slug}},'page_size':3})
pid=r.json()['results'][0]['id']; print(f'{slug}: {pid}')
requests.patch(f'https://api.notion.com/v1/pages/{pid}',headers=H,json={'properties':{'intro':{'rich_text':[{'text':{'content':'20대 여성 생일선물, 트렌디하고 예쁜 아이템을 정리했습니다.'}}]}}})
ids=[];cur=None
while True:
    pp={'page_size':100}
    if cur:pp['start_cursor']=cur
    r2=requests.get(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,params=pp)
    d=r2.json()
    ids.extend(b['id'] for b in d.get('results',[]))
    if not d.get('has_more'):break
    cur=d.get('next_cursor')
for bid in ids:requests.delete(f'https://api.notion.com/v1/blocks/{bid}',headers=H)
B=[h2('20대 여성 선물'),p('20대 여성은 뷰티와 패션에 관심이 많습니다.'),h3('향수'),p('조말론, 딥디크 트래블 세트(3~7만원대)가 부담 없는 첫 향수 선물로 좋습니다.'),h3('화장품'),p('립 제품(틴트·립스틱 1~3만원대), 스킨케어 세트가 인기입니다.'),h3('액세서리'),p('귀걸이, 목걸이 등 패션 주얼리(1~5만원대)도 예쁜 선물입니다.'),h2('마치며'),p('개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]
r3=requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,json={'children':B})
print(f'{"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"}')
