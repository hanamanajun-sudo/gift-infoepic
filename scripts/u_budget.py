import requests, sys, os; sys.path.insert(0, 'scripts')
from notion_key import get_key
K=get_key();H={'Authorization':f'Bearer {K}','Notion-Version':'2022-06-28','Content-Type':'application/json'};G='9603a00b-976b-4791-a129-d5f537e5db06'
def h2(t):return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t):return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t):return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}

for slug,intro,blocks in [
 ('1만원이하-선물','1만원 이하 선물, 부담 없이 마음을 전할 수 있는 아이템을 소개합니다.',
  [h2('1만원 이하 선물'),p('1만원 이하로도 센스 있는 선물이 가능합니다. 부담 없이 주고받기 좋습니다.'),h3('핸드크림'),p('향 좋은 핸드크림은 3~8천원대로 가성비 좋은 선물입니다. 여러 개 사서 여럿에게 나눠줘도 좋습니다.'),h3('문구류'),p('카카오프렌즈 문구세트(5,800원), 예쁜 볼펜, 스티커 등이 인기입니다.'),h3('간식·사탕'),p('해태 연양갱(11,800원/20개), 개별 포장 초콜릿 등 부담 없는 간식 선물도 좋습니다.'),h2('마치며'),p('개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]),
 ('3만원이하-선물','3만원 이하 선물, 가성비 좋은 실용 아이템을 소개합니다.',
  [h2('3만원 이하 선물'),p('3만원 이하는 부담스럽지 않으면서도 괜찮은 선물을 고를 수 있는 예산입니다.'),h3('향초·캔들'),p('소이캔들, 미니 디퓨저 등 1~3만원대 감성 아이템이 인기입니다.'),h3('머그컵·텀블러'),p('코렐 머그(10,900원), 락앤락 텀블러(21,400원) 등 실용적입니다.'),h3('보드게임'),p('루미큐브(35,200원)는 3만원대를 살짝 넘지만 가성비 최고의 선물입니다.'),h2('마치며'),p('개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]),
 ('5만원이하-선물','5만원 이하 선물, 실용적이면서도 품질 좋은 아이템을 소개합니다.',
  [h2('5만원 이하 선물'),p('5만원은 선물 예산으로 가장 무난한 구간입니다.'),h3('향수 트래블 세트'),p('조말론, 딥디크 등 트래블 세트(3~7만원대)가 첫 향수 선물로 좋습니다.'),h3('액세서리'),p('패션 귀걸이, 목걸이, 팔찌 등 3~5만원대 주얼리가 인기입니다.'),h3('스킨케어 세트'),p('AHC, 미샤 등 기초 화장품 세트(3~5만원대)가 무난합니다.'),h2('마치며'),p('개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]),
 ('10만원이하-선물','10만원 이하 선물, 중간 예산의 품격 있는 선물을 소개합니다.',
  [h2('10만원 이하 선물'),p('10만원 이하는 조금 더 신경 쓴 선물을 할 수 있는 예산입니다.'),h3('향수'),p('알파무드, 조말론 30ml(7~10만원대) 등 인기 향수가 가능합니다.'),h3('전자기기'),p('무선 이어폰(중국 브랜드 3~5만원), 보조배터리, 스마트워치(5~10만원) 등이 있습니다.'),h3('패션'),p('가방, 지갑, 스카프 등 패션 아이템(5~10만원대)이 좋습니다.'),h2('마치며'),p('개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]),
 ('20만원이하-선물','20만원 이하 선물, 프리미엄 선물의 시작 가격대입니다.',
  [h2('20만원 이하 선물'),p('10~20만원은 선물로 가장 애매하면서도 중요한 구간입니다. 오래 쓸 수 있는 제품이 좋습니다.'),h3('전자기기'),p('에어팟, 갤럭시 버즈(10~20만원대)가 가장 인기입니다. 무선 이어폰은 누구나 좋아합니다.'),h3('건강식품'),p('정관장 에브리타임(12만원대), 산양삼(49,800원) 등 프리미엄 건강식품이 가능합니다.'),h3('주얼리'),p('14K 귀걸이, 목걸이 등 가벼운 금액의 주얼리(10~20만원대)도 좋은 선택입니다.'),h2('마치며'),p('개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]),
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
