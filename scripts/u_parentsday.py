import requests, sys, os; sys.path.insert(0, 'scripts')
from notion_key import get_key
K=get_key();H={'Authorization':f'Bearer {K}','Notion-Version':'2022-06-28','Content-Type':'application/json'};G='9603a00b-976b-4791-a129-d5f537e5db06'
def h2(t):return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t):return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t):return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}

slug='어버이날-선물'
r=requests.post(f'https://api.notion.com/v1/databases/{G}/query',headers=H,json={'filter':{'property':'slug','rich_text':{'contains':slug}},'page_size':3});pid=r.json()['results'][0]['id']
print(f'{slug}: {pid}')
requests.patch(f'https://api.notion.com/v1/pages/{pid}',headers=H,json={'properties':{'intro':{'rich_text':[{'text':{'content':'어버이날 선물, 건강과 감사를 전하는 아이템을 네이버 쇼핑에서 찾았습니다.'}}]}}})
ids=[];c=None
while True:
    pp={'page_size':100}
    if c:pp['start_cursor']=c
    r2=requests.get(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,params=pp);d=r2.json()
    ids.extend(b['id'] for b in d.get('results',[]))
    if not d.get('has_more'):break
    c=d.get('next_cursor')
for b in ids:requests.delete(f'https://api.notion.com/v1/blocks/{b}',headers=H)
B=[h2('어버이날 선물, 건강과 감사'),p('어버이날은 부모님께 감사하는 마음을 전하는 날입니다. 네이버 쇼핑에서 인기 선물을 정리했습니다.'),h3('건강기능식품'),p('농협안심녹용(60년 전통), 정관장 에브리타임, 랑콤 제니피끄 선물세트 등이 어버이날 1순위 선물입니다. 10~20만원대 프리미엄 제품이 인기입니다.'),h3('안마기'),p('밸롭 종아리 안마기, 목 어깨 안마기 등 부모님의 피로를 풀어주는 아이템이 좋습니다. 5~15만원대입니다.'),h3('꽃·카네이션'),p('나인플라워 전국 꽃배달, 카네이션 꽃바구니는 어버이날의 대표 선물입니다. 직접 전달하면서 안아드리는 게 가장 좋습니다.'),h2('마치며'),p('어버이날 선물은 무엇보다 부모님의 건강을 생각하는 마음이 중요합니다. 직접 만나 뵙고 식사하는 시간을 함께하는 것도 큰 선물입니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]
r3=requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,json={'children':B})
print(f'{"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"}')
