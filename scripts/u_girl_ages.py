import requests, sys, os; sys.path.insert(0, 'scripts')
from notion_key import get_key
K=get_key();H={'Authorization':f'Bearer {K}','Notion-Version':'2022-06-28','Content-Type':'application/json'};G='9603a00b-976b-4791-a129-d5f537e5db06'
def h2(t):return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t):return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t):return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}

for slug,intro,blocks in [
 ('8세-여자아이-생일선물','8세 여자아이 생일선물, 레고와 캐릭터 아이템이 인기입니다.',
  [h2('8세 여자아이 선물'),p('8세는 초등 1~2학년으로 캐릭터와 만들기 놀이를 좋아하는 시기입니다.'),h3('레고'),p('레고 프렌즈 시리즈, 레고 클래식 브릭박스(59,990원) 등 만들기 장난감이 인기입니다. 마이리틀타이거 블록(24,900원)도 가성비 좋은 선택입니다.'),h3('캐릭터 인형'),p('산리오(시나모롤·쿠로미), 포켓몬 등 캐릭터 인형이 8세 여아에게 인기입니다.'),h3('문구·미술'),p('카카오프렌즈 문구세트, 색연필 세트, 스티커 북 등 창의력을 키워주는 선물이 좋습니다.'),h2('마치며'),p('개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]),
 ('10세-여자아이-생일선물','10세 여자아이 생일선물, 취향이 생기기 시작하는 나이입니다.',
  [h2('10세 여자아이 선물'),p('10세는 초등 3~4학년으로 본격적인 취향이 생기는 시기입니다.'),h3('레고·블록'),p('레고 프렌즈, 레고 크리에이터 등 만들기 좋아하는 아이에게 레고 시리즈가 인기입니다.'),h3('캐릭터·인형'),p('시나모롤·쿠로미 인형, 포켓몬 인형, 산리오 굿즈 등이 좋습니다. 다꾸(다이어리꾸미기) 세트도 인기입니다.'),h3('보드게임'),p('루미큐브(35,200원), 할리갈리 등 가족과 함께 즐길 수 있는 보드게임이 좋습니다.'),h2('마치며'),p('개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]),
 ('12세-여자아이-생일선물','12세 여자아이 생일선물, 중학생 입학 전 예비 청소년 선물입니다.',
  [h2('12세 여자아이 선물'),p('12세는 초등 고학년으로 또래 문화에 관심이 많아지는 시기입니다.'),h3('뷰티'),p('립글로스, 틴트, 네일 스티커 등 가벼운 뷰티 제품이 인기입니다. 롬앤, 어뮤즈 등 10대 브랜드가 좋습니다.'),h3('캐릭터 굿즈'),p('산리오, 포켓몬 등 캐릭터 문구나 소품이 인기입니다. 다꾸(다이어리꾸미기) 재료도 좋습니다.'),h3('전자기기'),p('무선 이어폰, 보조배터리, 무드등 등이 실용적인 선물입니다.'),h2('마치며'),p('개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]),
 ('15세-여자아이-생일선물','15세 여자아이 생일선물, 고등학생 선물 고민 해결.',
  [h2('15세 여자아이 선물'),p('15세는 고등학생으로 또래 문화와 SNS 트렌드에 민감합니다.'),h3('향수'),p('조말론 트래블 세트(3~7만원대), 알파무드, 딥디크 플뢰르 드 뽀 등이 인기입니다.'),h3('화장품'),p('립 제품, 마스크팩, 스킨케어 세트 등이 좋습니다. 디올 립글로우, 롬앤 틴트 등이 인기입니다.'),h3('패션 액세서리'),p('귀걸이, 목걸이, 팔찌 등 패션 주얼리(1~5만원대)가 인기입니다.'),h2('마치며'),p('개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]),
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
