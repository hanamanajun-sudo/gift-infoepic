import requests, sys, os; sys.path.insert(0, 'scripts')
from notion_key import get_key
K=get_key();H={'Authorization':f'Bearer {K}','Notion-Version':'2022-06-28','Content-Type':'application/json'};G='9603a00b-976b-4791-a129-d5f537e5db06'
def h2(t):return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t):return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t):return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}

slug='결혼축하-선물'
r=requests.post(f'https://api.notion.com/v1/databases/{G}/query',headers=H,json={'filter':{'property':'slug','rich_text':{'contains':slug}},'page_size':3});pid=r.json()['results'][0]['id']
print(f'{slug}: {pid}')
requests.patch(f'https://api.notion.com/v1/pages/{pid}',headers=H,json={'properties':{'intro':{'rich_text':[{'text':{'content':'결혼축하 선물, 예산과 관계에 따라 골라보세요. 네이버 쇼핑에서 인기 아이템을 정리했습니다.'}}]}}})
ids=[];c=None
while True:
    pp={'page_size':100}
    if c:pp['start_cursor']=c
    r2=requests.get(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,params=pp);d=r2.json()
    ids.extend(b['id'] for b in d.get('results',[]))
    if not d.get('has_more'):break
    c=d.get('next_cursor')
for b in ids:requests.delete(f'https://api.notion.com/v1/blocks/{b}',headers=H)
B=[h2('결혼축하 선물, 예산과 관계에 따라'),p('결혼식 참석 시 축하 선물 고민. 친한 정도와 예산에 따라 선택하세요.'),h3('가전·생활용품(5~10만원)'),p('디퓨저+주얼리스틱 세트(21,800원), 에리쏭 디퓨저, 전통 살림용품 등이 인기입니다. 신혼부부에게 실용적인 아이템이 좋습니다.'),h3('현금(10만원+)'),p('가장 무난한 결혼축하 선물은 현금입니다. 친한 정도에 따라 5~30만원까지 다양합니다. 축하 메시지를 꼭 함께 전하세요.'),h3('토퍼·이벤트용품'),p('한글토퍼(11,900원)는 결혼식장에서 사진 촬영용으로 인기입니다. 재미있는 문구의 토퍼를 준비하면 분위기를 살릴 수 있습니다.'),h2('마치며'),p('결혼축하 선물은 축하하는 마음이 가장 중요합니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]
r3=requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,json={'children':B})
print(f'{"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"}')
