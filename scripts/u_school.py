import requests, sys, os; sys.path.insert(0, 'scripts')
from notion_key import get_key
K=get_key();H={'Authorization':f'Bearer {K}','Notion-Version':'2022-06-28','Content-Type':'application/json'};G='9603a00b-976b-4791-a129-d5f537e5db06'
def h2(t):return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t):return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t):return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}

slug='입학선물'
r=requests.post(f'https://api.notion.com/v1/databases/{G}/query',headers=H,json={'filter':{'property':'slug','rich_text':{'contains':slug}},'page_size':3})
pid=r.json()['results'][0]['id'];print(f'{slug}: {pid}')
requests.patch(f'https://api.notion.com/v1/pages/{pid}',headers=H,json={'properties':{'intro':{'rich_text':[{'text':{'content':'입학선물, 초등학교부터 대학교까지 학령별로 네이버 쇼핑에서 인기 아이템을 정리했습니다.'}}]}}})
ids=[];c=None
while True:
    pp={'page_size':100}
    if c:pp['start_cursor']=c
    r2=requests.get(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,params=pp);d=r2.json()
    ids.extend(b['id'] for b in d.get('results',[]))
    if not d.get('has_more'):break
    c=d.get('next_cursor')
for b in ids:requests.delete(f'https://api.notion.com/v1/blocks/{b}',headers=H)
B=[h2('입학선물, 학령별로'),p('입학은 새로운 시작을 응원하는 의미 있는 순간입니다. 학령별로 추천 선물이 다릅니다.'),h3('초등학교 입학'),p('스테들러 문구세트(50,000원), 올포홈 젤리빈 필통(24,900원) 등 학용품이 인기입니다. 책가방이나 필기도구는 부모님이 이미 준비했을 가능성이 높아 피하는 게 좋습니다.'),h3('중·고등학교 입학'),p('라미 만년필(29만원대), 나무 각인 볼펜(58,000원) 등 고급 필기구가 의미 있는 입학선물입니다. 백팩이나 실용 가방도 좋은 선택입니다.'),h3('대학교 입학'),p('노트북 가방, 무선 이어폰, 향수 등이 인기입니다. 용돈도 가장 무난한 입학선물 중 하나입니다.'),h2('마치며'),p('입학선물은 새로운 시작을 응원하는 메시지를 꼭 함께 전하세요. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]
r3=requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,json={'children':B})
print(f'{"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"}')
