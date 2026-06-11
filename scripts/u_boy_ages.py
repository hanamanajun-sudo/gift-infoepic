import requests, sys, os; sys.path.insert(0, 'scripts')
from notion_key import get_key
K=get_key();H={'Authorization':f'Bearer {K}','Notion-Version':'2022-06-28','Content-Type':'application/json'};G='9603a00b-976b-4791-a129-d5f537e5db06'
def h2(t):return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t):return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t):return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}

for slug,intro,blocks in [
 ('10세-남자아이-생일선물','10세 남자아이 생일선물, 레고와 장난감이 인기입니다.',
  [h2('10세 남자아이 선물'),p('10세는 초등 3~4학년으로 만들기와 활동적인 놀이를 좋아하는 시기입니다.'),h3('레고'),p('레고 닌자고(104,900원), 레고 스피드챔피언(61,500원), 레고 테크닉 부가티(59,700원) 등 레고 시리즈가 가장 인기입니다.'),h3('RC카·미니카'),p('마이리틀타이거 미니카(19,900원), RC카 등 활동적인 장난감이 좋습니다.'),h3('보드게임'),p('루미큐브, 젠가 등 가족과 함께 즐기는 보드게임도 좋은 선택입니다.'),h2('마치며'),p('개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]),
 ('12세-남자아이-생일선물','12세 남자아이 생일선물, 게임과 전자기기가 인기입니다.',
  [h2('12세 남자아이 선물'),p('12세는 초등 고학년으로 게임과 디지털 기기에 관심이 많아집니다.'),h3('닌텐도 게임'),p('포켓몬 ZA(54,800원, 리뷰 2,542), 마인크래프트 등 닌텐도 스위치 게임 타이틀이 인기입니다.'),h3('전자기기'),p('무선 이어폰, 보조배터리, 게이밍 마우스 등이 실용적인 선물입니다.'),h3('레고·블록'),p('레고 테크닉, 레고 마인크래프트 시리즈 등 만들기 좋아하는 아이에게 좋습니다.'),h2('마치며'),p('개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]),
 ('13세-남자아이-생일선물','13세 남자아이 생일선물, 중학생 첫 선물 고민.',
  [h2('13세 남자아이 선물'),p('13세는 중학생으로 접어드는 시기입니다. 이전과 취향이 확 바뀔 수 있어 조심해야 합니다.'),h3('전자기기'),p('무선 이어폰(에어팟/갤럭시버즈 10~20만원대), 보조배터리, 게이밍 마우스 등이 가장 인기입니다.'),h3('운동화'),p('조던, 나이키 등 인기 운동화 브랜드가 좋습니다. 사이즈 확인이 필수입니다.'),h3('향수'),p('알파무드, 포맨트 등 10대 남성을 위한 향수가 인기입니다.'),h2('마치며'),p('개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]),
 ('16세-남자아이-생일선물','16세 남자아이 생일선물, 고등학생 선물 고민.',
  [h2('16세 남자아이 선물'),p('16세는 고등학생으로 자기만의 취향이 확실한 시기입니다.'),h3('향수'),p('알파무드, 샤넬 블루, 조말론 등 향수가 가장 인기 있는 선물입니다.'),h3('전자기기'),p('무선 이어폰, 스마트워치, 게이밍 기어 등이 좋습니다.'),h3('패션'),p('운동화, 백팩, 지갑 등 실용 패션 아이템도 좋습니다. 브랜드에 민감할 수 있어 취향 확인이 필요합니다.'),h2('마치며'),p('개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]),
 ('13세-여자아이-생일선물','13세 여자아이 생일선물, 중학생 첫 생일.',
  [h2('13세 여자아이 선물'),p('13세는 중학생으로 접어드는 중요한 시기입니다. 뷰티와 감성 아이템이 인기입니다.'),h3('향수'),p('알파무드, 조말론 트래블 세트(3~7만원대) 등 첫 향수 선물이 인기입니다.'),h3('화장품'),p('립글로스, 틴트, 마스크팩 등 가벼운 뷰티 제품이 좋습니다. 롬앤, 어뮤즈 등 10대 브랜드가 인기입니다.'),h3('캐릭터 굿즈'),p('산리오(시나모롤) 인형이나 문구, 다꾸 세트 등이 아직도 인기입니다.'),h2('마치며'),p('개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]),
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
