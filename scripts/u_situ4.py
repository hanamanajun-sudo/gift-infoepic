import requests, sys, os; sys.path.insert(0, 'scripts')
from notion_key import get_key
K=get_key();H={'Authorization':f'Bearer {K}','Notion-Version':'2022-06-28','Content-Type':'application/json'};G='9603a00b-976b-4791-a129-d5f537e5db06'
def h2(t):return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t):return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t):return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}

for slug,intro,blocks in [
 ('결혼기념일-선물','결혼기념일 선물, 주얼리부터 감성 아이템까지 네이버 쇼핑에서 인기 선물을 정리했습니다.',
  [h2('결혼기념일 선물, 특별한 날'),p('결혼기념일은 부부에게 특별한 날입니다. 네이버 쇼핑에서 인기 선물을 정리했습니다.'),h3('주얼리'),p('가네시 18K 주얼리(목걸이, 팔찌, 귀걸이, 반지)가 결혼기념일 선물로 인기입니다. 최대 50% 할인 행사도 자주 있습니다.'),h3('감성 선물'),p('자작나무에 추억을 새기는 나무편지(바벤아트)는 특별한 결혼기념일 선물입니다. 사진과 함께 각인할 수 있어 의미가 깊습니다.'),h3('꽃·로맨틱'),p('세일플라워 전국 꽃배달, 디올 향수 등 로맨틱한 선물도 인기입니다. 약손명가 안마기로 피로를 풀어주는 것도 좋습니다.'),h2('마치며'),p('결혼기념일은 몇 주년이냐에 따라 선물 컨셉을 정하는 것도 방법입니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]),
 ('남편-생일선물','남편 생일선물, 실용적이면서 감동을 줄 선물을 네이버 쇼핑에서 찾았습니다.',
  [h2('남편 생일선물'),p('남편 선물은 평소 필요로 하는 실용적인 아이템이 가장 좋습니다.'),h3('패션'),p('지갑, 벨트, 시계, 넥타이 등 매일 사용하는 패션 아이템이 인기입니다.'),h3('전자기기'),p('무선 이어폰, 스마트워치, 게이밍 기어 등 남편의 취미에 맞춘 선물이 좋습니다.'),h3('건강'),p('홍삼, 건강기능식품, 안마기 등 건강을 생각한 선물도 인기입니다.'),h2('마치며'),p('남편이 평소에 갖고 싶다고 말한 적이 있는 걸 기억해보세요. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]),
 ('아내-생일선물','아내 생일선물, 감동을 줄 수 있는 아이템을 네이버 쇼핑에서 찾았습니다.',
  [h2('아내 생일선물'),p('아내 생일은 가장 신경 써야 할 날입니다. 꼼꼼하게 준비하세요.'),h3('주얼리'),p('목걸이, 귀걸이, 반지 등 주얼리는 아내 선물의 정석입니다. 가네시 18K 주얼리(10~50만원대)가 인기입니다.'),h3('꽃·케이크'),p('꽃다발과 케이크는 아내에게 가장 큰 감동을 줍니다. 직접 준비한 이벤트와 함께하면 더 좋습니다.'),h3('스킨케어'),p('설화수, AHC 등 프리미엄 스킨케어 세트(10~15만원대)도 좋은 선택입니다.'),h2('마치며'),p('아내 생일은 선물 자체보다 그날 하루를 특별하게 만들어주는 게 중요합니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]),
 ('집들이-선물','집들이 선물, 부담 없으면서도 센스 있는 아이템을 네이버 쇼핑에서 찾았습니다.',
  [h2('집들이 선물, 센스가 중요'),p('집들이 선물은 가격보다 센스가 중요합니다. 네이버 쇼핑에서 인기 집들이 선물입니다.'),h3('디퓨저·캔들'),p('에리쏭 디퓨저(1+1), 햅번 디퓨저 세트(21,800원)가 인기입니다. 향은 은은한 플로럴 계열이 무난합니다.'),h3('머그컵·텀블러'),p('코렐 시나모롤 머그(10,900원), 락앤락 텀블러(21,400원) 등 예쁜 컵 제품이 인기입니다.'),h3('수건세트'),p('도톰한 수건 5~6장 세트는 가장 무난한 집들이 선물입니다. 색상은 인테리어에 맞춰 선택하세요.'),h2('마치며'),p('집들이 선물은 새집 주인의 취향을 고려하는 게 좋습니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')]),
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
