import requests, sys, os; sys.path.insert(0, 'scripts')
from notion_key import get_key
K=get_key();H={'Authorization':f'Bearer {K}','Notion-Version':'2022-06-28','Content-Type':'application/json'};G='9603a00b-976b-4791-a129-d5f537e5db06'
def h2(t):return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t):return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t):return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}

for slug,intro,blocks in [
 ('여동생-생일선물','여동생 생일선물, 예쁘고 실용적인 아이템을 골라보세요.',
  [h2('여동생 생일선물'),p('여동생은 가장 가까운 사이지만 오히려 선물 고르기가 어렵습니다. 평소 동생이 좋아하는 걸 떠올려보세요.'),h3('뷰티'),p('립글로스, 틴트, 마스크팩 세트 등 부담 없는 가격의 뷰티 제품이 인기입니다.'),h3('악세서리'),p('귀걸이, 목걸이, 팔찌 등 예쁜 패션 주얼리(1~5만원대)가 좋습니다.'),h3('감성 아이템'),p('무드등, 향초, 인형 등 여동생의 방을 꾸며줄 수 있는 아이템도 좋은 선택입니다.'),h2('마치며'),p('개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]),
 ('남동생-생일선물','남동생 생일선물, 실용적이면서 센스 있는 아이템을 골라보세요.',
  [h2('남동생 생일선물'),p('남동생 선물은 실용적인 게 최고입니다. 평소 동생이 필요로 하는 물건을 생각해보세요.'),h3('전자기기'),p('무선 이어폰, 보조배터리, 게이밍 마우스 등 디지털 기기가 가장 인기입니다.'),h3('패션'),p('속옷 세트, 지갑, 운동화 등 실용 패션 아이템도 좋습니다. 취향을 잘 모르겠다면 속옷이 무난합니다.'),h3('향수'),p('알파무드, 포맨트 등 10~20대 남성 향수도 좋은 선물입니다.'),h2('마치며'),p('개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]),
]:
    r=requests.post(f'https://api.notion.com/v1/databases/{G}/query',headers=H,json={'filter':{'property':'slug','rich_text':{'contains':slug}},'page_size':3})
    pid=r.json()['results'][0]['id'];print(f'{slug}: {pid}')
    requests.patch(f'https://api.notion.com/v1/pages/{pid}',headers=H,json={'properties':{'intro':{'rich_text':[{'text':{'content':intro}}]}}})
    ids=[];c=None
    while True:
        pp={'page_size':100}
        if c:pp['start_cursor']=c
        r2=requests.get(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,params=pp);d=r2.json()
        ids.extend(b['id'] for b in d.get('results',[]))
        if not d.get('has_more'):break
        c=d.get('next_cursor')
    for b in ids:requests.delete(f'https://api.notion.com/v1/blocks/{b}',headers=H)
    r3=requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,json={'children':blocks})
    print(f'  {"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"}')
