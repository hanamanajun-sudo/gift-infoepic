import requests, sys, os; sys.path.insert(0, 'scripts')
from notion_key import get_key
K=get_key();H={'Authorization':f'Bearer {K}','Notion-Version':'2022-06-28','Content-Type':'application/json'};G='9603a00b-976b-4791-a129-d5f537e5db06'
def h2(t):return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t):return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t):return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}

slug='화이트데이-선물'
r=requests.post(f'https://api.notion.com/v1/databases/{G}/query',headers=H,json={'filter':{'property':'slug','rich_text':{'contains':slug}},'page_size':3})
pid=r.json()['results'][0]['id'];print(f'{slug}: {pid}')
requests.patch(f'https://api.notion.com/v1/pages/{pid}',headers=H,json={'properties':{'intro':{'rich_text':[{'text':{'content':'화이트데이 선물, 사탕부터 디저트까지 네이버 쇼핑에서 인기 아이템을 정리했습니다.'}}]}}})
ids=[];c=None
while True:
    pp={'page_size':100}
    if c:pp['start_cursor']=c
    r2=requests.get(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,params=pp);d=r2.json()
    ids.extend(b['id'] for b in d.get('results',[]))
    if not d.get('has_more'):break
    c=d.get('next_cursor')
for b in ids:requests.delete(f'https://api.notion.com/v1/blocks/{b}',headers=H)
B=[h2('화이트데이 선물, 사탕 그 이상'),p('화이트데이는 발렌타인데이의 답례 개념. 사탕이 전통이지만 요즘은 다양한 선물이 인기입니다.'),h3('사탕·캔디'),p('피에로구르망 막대사탕(프랑스 명품), 춘식이 하트 캔디 등 예쁜 패키지의 사탕이 인기입니다.'),h3('수제 디저트'),p('카카오브로 수제 디저트 세트, 두바이 초콜렛, 쿠키 세트 등이 인기입니다. 1~3만원대가 부담 없습니다.'),h3('꽃다발'),p('꽃다발은 화이트데이 선물로 항상 좋은 반응을 얻습니다. 전국 꽃배달 서비스를 이용하면 직접 전달하기 부담스러운 경우에도 좋습니다.'),h2('마치며'),p('화이트데이는 받는 사람의 취향을 고려한 선물이 가장 좋습니다. 사탕만으로는 부족하다면 작은 꽃다발이나 디저트를 추가하세요. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]
r3=requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,json={'children':B})
print(f'{"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"}')
