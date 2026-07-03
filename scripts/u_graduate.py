import requests, sys, os; sys.path.insert(0, 'scripts')
from notion_key import get_key
K=get_key();H={'Authorization':f'Bearer {K}','Notion-Version':'2022-06-28','Content-Type':'application/json'};G='9603a00b-976b-4791-a129-d5f537e5db06'
def h2(t):return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t):return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t):return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}

slug='졸업선물'
r=requests.post(f'https://api.notion.com/v1/databases/{G}/query',headers=H,json={'filter':{'property':'slug','rich_text':{'contains':slug}},'page_size':3});pid=r.json()['results'][0]['id']
print(f'{slug}: {pid}')
requests.patch(f'https://api.notion.com/v1/pages/{pid}',headers=H,json={'properties':{'intro':{'rich_text':[{'text':{'content':'졸업선물, 새로운 시작을 응원하는 의미 있는 선물을 소개합니다.'}}]}}})
ids=[];c=None
while True:
    pp={'page_size':100}
    if c:pp['start_cursor']=c
    r2=requests.get(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,params=pp);d=r2.json()
    ids.extend(b['id'] for b in d.get('results',[]))
    if not d.get('has_more'):break
    c=d.get('next_cursor')
for b in ids:requests.delete(f'https://api.notion.com/v1/blocks/{b}',headers=H)
B=[h2('졸업선물, 새로운 시작을 응원하며'),p('졸업은 한 시즌의 마무리이자 새로운 시작입니다. 응원의 마음을 담은 선물이 좋습니다.'),h3('초등학교 졸업'),p('워터맨 만년필(54,000원), 라미 만년필 등 의미 있는 필기구가 인기입니다. 새 학교에서 쓸 백팩도 좋은 선택입니다.'),h3('중·고등학교 졸업'),p('워터맨 까렌 디럭스(696,000원) 같은 프리미엄 만년필, 향수(알파무드, 조말론) 등이 인기입니다.'),h3('대학교 졸업'),p('시계, 면도기, 향수, 노트북 등 사회생활에 필요한 실용적인 선물이 좋습니다. 비나다 논알콜 와인(축하 분위기용)도 인기입니다.'),h2('마치며'),p('졸업선물은 물건 자체보다 응원과 축하의 메시지가 중요합니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]
r3=requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,json={'children':B})
print(f'{"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"}')
