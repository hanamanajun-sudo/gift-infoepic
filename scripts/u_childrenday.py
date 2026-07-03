import requests, sys, os; sys.path.insert(0, 'scripts')
from notion_key import get_key
K=get_key();H={'Authorization':f'Bearer {K}','Notion-Version':'2022-06-28','Content-Type':'application/json'};G='9603a00b-976b-4791-a129-d5f537e5db06'
def h2(t):return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t):return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t):return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}

slug='어린이날-선물'
r=requests.post(f'https://api.notion.com/v1/databases/{G}/query',headers=H,json={'filter':{'property':'slug','rich_text':{'contains':slug}},'page_size':3});pid=r.json()['results'][0]['id']
print(f'{slug}: {pid}')
requests.patch(f'https://api.notion.com/v1/pages/{pid}',headers=H,json={'properties':{'intro':{'rich_text':[{'text':{'content':'어린이날 선물, 나이와 취향에 따라 골라보세요. 네이버 쇼핑에서 인기 아이템을 정리했습니다.'}}]}}})
ids=[];c=None
while True:
    pp={'page_size':100}
    if c:pp['start_cursor']=c
    r2=requests.get(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,params=pp);d=r2.json()
    ids.extend(b['id'] for b in d.get('results',[]))
    if not d.get('has_more'):break
    c=d.get('next_cursor')
for b in ids:requests.delete(f'https://api.notion.com/v1/blocks/{b}',headers=H)
B=[h2('어린이날 선물, 나이별로'),p('어린이날은 아이들에게 가장 신나는 날입니다. 나이에 따라 좋아하는 선물이 다릅니다.'),h3('유아(3~7세)'),p('Swap 자전거 구독(성장맞춤 교체), 블록 장난감, 캐릭터 인형이 인기입니다.'),h3('초등 저학년(8~10세)'),p('보드게임(루미큐브 35,200원), 문구세트, 과학키트, RC카 등이 좋습니다.'),h3('초등 고학년(11~13세)'),p('닌텐도 게임, 무선 이어폰, 캐릭터 굿즈, 스마트워치 등이 인기입니다.'),h2('마치며'),p('어린이날 선물은 아이가 평소에 갖고 싶어했던 걸 관찰해두었다가 준비하는 게 가장 좋습니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]
r3=requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,json={'children':B})
print(f'{"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"}')
