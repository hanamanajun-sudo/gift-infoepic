import requests, sys, os; sys.path.insert(0, 'scripts')
from notion_key import get_key
K=get_key();H={'Authorization':f'Bearer {K}','Notion-Version':'2022-06-28','Content-Type':'application/json'};G='9603a00b-976b-4791-a129-d5f537e5db06'
def h2(t):return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t):return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t):return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}

slug='베프-생일선물'
r=requests.post(f'https://api.notion.com/v1/databases/{G}/query',headers=H,json={'filter':{'property':'slug','rich_text':{'contains':slug}},'page_size':3})
pid=r.json()['results'][0]['id'];print(f'{slug}: {pid}')
requests.patch(f'https://api.notion.com/v1/pages/{pid}',headers=H,json={'properties':{'intro':{'rich_text':[{'text':{'content':'베프 생일선물, 가장 친한 친구에게 특별한 선물을 네이버 쇼핑에서 찾았습니다.'}}]}}})
ids=[];c=None
while True:
    pp={'page_size':100}
    if c:pp['start_cursor']=c
    r2=requests.get(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,params=pp);d=r2.json()
    ids.extend(b['id'] for b in d.get('results',[]))
    if not d.get('has_more'):break
    c=d.get('next_cursor')
for b in ids:requests.delete(f'https://api.notion.com/v1/blocks/{b}',headers=H)
B=[h2('베프 생일선물, 특별한 우정을'),p('베프에게는 평소에는 안 사주는 특별한 선물을 준비해보세요.'),h3('감성·추억 선물'),p('코닥 포토프린터 미니샷3(194,000원, 리뷰 9,999+)는 함께한 추억을 즉석에서 인화할 수 있어 베프 선물로 인기입니다.'),h3('홈카페·리빙'),p('스탠리 텀블러(49,000원), 키크론 무선 키보드(47,500원) 등 실용적이면서 디자인 예쁜 제품이 좋습니다.'),h3('특별한 경험'),p('삼탠바이미 TV(32만원대), 태블릿 등 조금 큰 선물도 베프에게는 가능합니다. 함께 즐길 수 있는 선물이 더 좋습니다.'),h2('마치며'),p('베프는 가장 가까운 친구이니만큼 평소에 친구가 갖고 싶다고 말한 물건을 기억해두는 게 가장 좋습니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]
r3=requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,json={'children':B})
print(f'{"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"}')
