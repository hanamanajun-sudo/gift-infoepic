import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

K=get_key();H={'Authorization':f'Bearer {K}','Notion-Version':'2022-06-28','Content-Type':'application/json'};GDB='9603a00b-976b-4791-a129-d5f537e5db06'
def h2(t):return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t):return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t):return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}

slug='발렌타인데이-선물'
r=requests.post(f'https://api.notion.com/v1/databases/{GDB}/query',headers=H,json={'filter':{'property':'slug','rich_text':{'contains':slug}},'page_size':3});pid=r.json()['results'][0]['id']
print(f'{slug}: {pid}')
requests.patch(f'https://api.notion.com/v1/pages/{pid}',headers=H,json={'properties':{'intro':{'rich_text':[{'text':{'content':'발렌타인데이 선물, 초콜릿부터 향수까지 네이버 쇼핑에서 인기 아이템을 정리했습니다.'}}]}}})
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
B=[h2('발렌타인데이 선물, 초콜릿이 기본'),p('발렌타인데이는 초콜릿이 기본! 하지만 요즘은 초콜릿 외에도 다양한 선물이 인기입니다.'),h3('초콜릿'),p('고급 수제 초콜릿, 파베 초콜릿이 발렌타인데이의 대표 선물입니다. 카카오브로 같은 수제 디저트 전문 브랜드가 네이버 쇼핑에서 인기입니다.'),h3('향수'),p('여자가 남자에게 주는 날이라 향수도 인기입니다. 알파무드, 조말론 등이 발렌타인데이 선물로 많이 찾습니다.'),h3('패션 액세서리'),p('목걸이, 귀걸이, 반지 등 주얼리도 발렌타인데이의 대표 선물입니다. 3~10만원대 제품이 인기입니다.'),h2('마치며'),p('발렌타인데이는 혼자만의 이벤트가 아니라 서로의 마음을 확인하는 날입니다. 정성이 담긴 선물을 준비하세요. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]
r3=requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,json={'children':B})
print(f'{"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"} ({len(B)} blocks)')
