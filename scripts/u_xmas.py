import requests, sys, os; sys.path.insert(0, 'scripts')
from notion_key import get_key
K=get_key();H={'Authorization':f'Bearer {K}','Notion-Version':'2022-06-28','Content-Type':'application/json'};G='9603a00b-976b-4791-a129-d5f537e5db06'
def h2(t):return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t):return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t):return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}

slug='크리스마스-선물'
r=requests.post(f'https://api.notion.com/v1/databases/{G}/query',headers=H,json={'filter':{'property':'slug','rich_text':{'contains':slug}},'page_size':3});pid=r.json()['results'][0]['id']
print(f'{slug}: {pid}')
requests.patch(f'https://api.notion.com/v1/pages/{pid}',headers=H,json={'properties':{'intro':{'rich_text':[{'text':{'content':'크리스마스 선물, 연인부터 가족까지 네이버 쇼핑에서 인기 아이템을 정리했습니다.'}}]}}})
ids=[];c=None
while True:
    pp={'page_size':100}
    if c:pp['start_cursor']=c
    r2=requests.get(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,params=pp);d=r2.json()
    ids.extend(b['id'] for b in d.get('results',[]))
    if not d.get('has_more'):break
    c=d.get('next_cursor')
for b in ids:requests.delete(f'https://api.notion.com/v1/blocks/{b}',headers=H)
B=[h2('크리스마스 선물, 누구에게 주는지에 따라'),p('크리스마스는 연인, 가족, 친구 모두에게 선물을 준비하는 시즌입니다.'),h3('연인에게'),p('브라운 전기면도기(남성), 디올 향수(여성), 지거스 우드편지(감성) 등이 인기입니다. 달리아 에스테틱 같은 경험 선물도 특별합니다.'),h3('부모님에게'),p('정관장 건강식품(10~20만원대), 목도리, 실내복 등 따뜻한 선물이 좋습니다.'),h3('친구에게'),p('스탠리 텀블러, 캔들 세트, 오설록 티 선물세트 등 2~5만원대 실용 선물이 인기입니다.'),h2('마치며'),p('크리스마스는 서로의 마음을 확인하는 날입니다. 정성 담긴 선물을 준비하세요. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]
r3=requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,json={'children':B})
print(f'{"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"}')
