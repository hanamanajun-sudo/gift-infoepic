import requests, sys, os; sys.path.insert(0, 'scripts')
from notion_key import get_key
K=get_key();H={'Authorization':f'Bearer {K}','Notion-Version':'2022-06-28','Content-Type':'application/json'};G='9603a00b-976b-4791-a129-d5f537e5db06'
def h2(t):return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t):return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t):return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}

slug='선생님-감사선물'
r=requests.post(f'https://api.notion.com/v1/databases/{G}/query',headers=H,json={'filter':{'property':'slug','rich_text':{'contains':slug}},'page_size':3})
pid=r.json()['results'][0]['id'];print(f'{slug}: {pid}')
requests.patch(f'https://api.notion.com/v1/pages/{pid}',headers=H,json={'properties':{'intro':{'rich_text':[{'text':{'content':'선생님 감사선물, 부담 없는 가격으로 마음을 전하는 아이템을 소개합니다.'}}]}}})
ids=[];c=None
while True:
    pp={'page_size':100}
    if c:pp['start_cursor']=c
    r2=requests.get(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,params=pp);d=r2.json()
    ids.extend(b['id'] for b in d.get('results',[]))
    if not d.get('has_more'):break
    c=d.get('next_cursor')
for b in ids:requests.delete(f'https://api.notion.com/v1/blocks/{b}',headers=H)
B=[h2('선생님 감사선물'),p('선생님께 감사하는 마음을 전하는 선물은 가격보다 정성이 중요합니다.'),h3('오설록 티 세트'),p('오설록 티 베리에이션(20,000원)은 가성비 좋은 선생님 선물입니다. 6가지 맛을 즐길 수 있습니다.'),h3('핸드크림·향초'),p('부담 없는 가격의 핸드크림이나 캔들도 선생님께 좋은 선물입니다. 5천원~1만원대로 준비할 수 있습니다.'),h3('편지·카드'),p('선생님께는 물건보다 진심이 담긴 편지가 가장 큰 감동을 줍니다. 작은 선물에 편지를 꼭 함께 전하세요.'),h2('마치며'),p('개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]
r3=requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,json={'children':B})
print(f'{"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"}')
