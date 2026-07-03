import requests, sys, os; sys.path.insert(0, 'scripts')
from notion_key import get_key
K=get_key();H={'Authorization':f'Bearer {K}','Notion-Version':'2022-06-28','Content-Type':'application/json'};G='9603a00b-976b-4791-a129-d5f537e5db06'
def h2(t):return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t):return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t):return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}

slug='조카-생일선물'
r=requests.post(f'https://api.notion.com/v1/databases/{G}/query',headers=H,json={'filter':{'property':'slug','rich_text':{'contains':slug}},'page_size':3});pid=r.json()['results'][0]['id']
print(f'{slug}: {pid}')
requests.patch(f'https://api.notion.com/v1/pages/{pid}',headers=H,json={'properties':{'intro':{'rich_text':[{'text':{'content':'조카 생일선물, 나이에 따라 골라주세요. 네이버 쇼핑 인기 장난감을 정리했습니다.'}}]}}})
ids=[];c=None
while True:
    pp={'page_size':100}
    if c:pp['start_cursor']=c
    r2=requests.get(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,params=pp);d=r2.json()
    ids.extend(b['id'] for b in d.get('results',[]))
    if not d.get('has_more'):break
    c=d.get('next_cursor')
for b in ids:requests.delete(f'https://api.notion.com/v1/blocks/{b}',headers=H)
B=[h2('조카 생일선물, 나이별 추천'),p('조카 선물은 나이에 따라 취향이 완전히 달라집니다. 네이버 쇼핑에서 인기 아이템을 정리했습니다.'),h3('유아(3~5세)'),p('타요 소방센터(76,900원), 마이리틀타이거 미니카(19,900원), 타요 신호등 놀이(51,900원) 등 캐릭터 장난감이 인기입니다.'),h3('초등 저학년(6~8세)'),p('레고 닌자고 로봇(104,900원), 레고 시티 기차(153,900원) 등 레고 시리즈가 최고 인기입니다. 보드게임도 좋습니다.'),h3('초등 고학년(9~13세)'),p('무선 이어폰, 닌텐도 게임, 캐릭터 문구세트, 과학키트 등 학습과 놀이를 겸한 선물이 좋습니다.'),h2('주의할 점'),p('조카 선물은 부모님(형제자매)에게 미리 어떤 장난감을 좋아하는지 물어보는 게 가장 안전합니다. 중복 선물을 피할 수 있습니다.'),h2('마치며'),p('조카 선물은 이모·삼촌의 정성이 느껴지는 특별한 선물이 좋습니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]
r3=requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,json={'children':B})
print(f'{"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"}')
