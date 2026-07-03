import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

K = get_key()
H = {'Authorization': f'Bearer {K}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}
GDB = '9603a00b-976b-4791-a129-d5f537e5db06'

def h2(t): return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t): return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t): return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def plink(pairs):
    rt = []
    for txt, url in pairs:
        if url: rt.append({'type':'text','text':{'content':txt,'link':{'url':url}}})
        else: rt.append({'type':'text','text':{'content':txt}})
    return {'object':'block','type':'paragraph','paragraph':{'rich_text':rt}}

def create_or_update(slug, title, intro, blocks):
    check = requests.post(f'https://api.notion.com/v1/databases/{GDB}/query', headers=H, json={
        'filter': {'property': 'slug', 'rich_text': {'equals': slug}}, 'page_size': 3})
    if check.json()['results']:
        pid = check.json()['results'][0]['id']
        print(f'{slug}: 업데이트')
        requests.patch(f'https://api.notion.com/v1/pages/{pid}', headers=H, json={
            'properties': {'intro': {'rich_text': [{'text':{'content':intro}}]}, 'Title':{'title':[{'text':{'content':title}}]}}})
        ids=[];c=None
        while True:
            pp={'page_size':100}
            if c:pp['start_cursor']=c
            r2=requests.get(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,params=pp);d=r2.json()
            ids.extend(b['id'] for b in d.get('results',[]))
            if not d.get('has_more'):break
            c=d.get('next_cursor')
        for b in ids:requests.delete(f'https://api.notion.com/v1/blocks/{b}',headers=H)
    else:
        body = {'parent':{'database_id':GDB},'properties':{'Title':{'title':[{'text':{'content':title}}]},'slug':{'rich_text':[{'text':{'content':slug}}]},'intro':{'rich_text':[{'text':{'content':intro}}]},'published':{'checkbox':True}},'children':[]}
        r = requests.post('https://api.notion.com/v1/pages',headers=H,json=body)
        pid = r.json().get('id')
        if not pid: print(f'❌ {slug} 생성실패'); return
        print(f'{slug}: ✅ 신규')
    r3 = requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,json={'children':blocks})
    print(f'  {"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"} ({len(blocks)}블록)')

# 1. 어린이 선물 고르는 법
create_or_update('어린이-선물-고르는-법',
    '어린이 선물 고르는 법 — 나이별 안전하고 좋은 선물',
    '아이에게 선물할 때 안전한지, 나이에 맞는지 고민되시죠? 나이별 발달 단계에 맞는 선물 고르는 법을 정리했습니다.',
    [h2('어린이 선물, 안전이 첫 번째'),
     p('아이에게 주는 선물은 안전이 가장 중요합니다. KC 인증 마크가 있는 제품인지, 사용 연령에 맞는 제품인지 꼭 확인하세요.'),
     h2('0~3세: 감각 발달을 돕는 선물'),
     p('이 시기는 오감 발달이 가장 활발한 때입니다. 딸랑이, 치발기, 헝겊책, 모빌 등 촉감과 청각을 자극하는 장난감이 좋습니다.'),
     p('주의: 작은 부품이 없는 제품, BPA-free 소재 제품을 선택하세요.'),
     h2('4~6세: 상상력과 창의력을 키우는 선물'),
     p('역할놀이, 만들기, 블록 등 상상력을 자극하는 장난감이 좋습니다. 레고 듀플로, 소꿉놀이 세트, 타요 장난감 등이 인기입니다.'),
     p('이 시기에는 혼자 노는 시간도 길어지므로 안전하게 가지고 놀 수 있는 제품이 좋습니다.'),
     h2('7~9세: 배움과 놀이의 균형'),
     p('초등 저학년 시기로 학습과 놀이를 겸한 선물이 좋습니다. 구슬퍼즐 펜토미노(23,000원)는 공간지각력과 집중력을 키워주는 두뇌 발달 장난감입니다.'),
     p('레고, 과학키트, 보드게임 등도 좋습니다. 루미큐브(35,200원)는 가족이 함께 즐기면서 사고력을 키울 수 있습니다.'),
     h2('10~12세: 취향이 생기는 시기'),
     p('또래 문화에 관심이 많아지는 나이입니다. 닌텐도 게임, 무선 이어폰, 캐릭터 굿즈 등이 인기입니다.'),
     p('아직 어린이이지만 취향이 확실해지므로 아이가 평소 좋아하는 것을 관찰해두는 게 좋습니다.'),
     h2('참고하면 좋은 가이드'),
     plink([('• 7~9세 여자아이 선물', 'https://gift.infoepic.com/%EC%84%A0%EB%AC%BC/7-9%EC%84%B8-%EC%97%AC%EC%9E%90%EC%95%84%EC%9D%B4-%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC/')]),
     plink([('• 7~9세 남자아이 선물', 'https://gift.infoepic.com/%EC%84%A0%EB%AC%BC/7-9%EC%84%B8-%EB%82%A8%EC%9E%90%EC%95%84%EC%9D%B4-%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC/')]),
     plink([('• 0~3세 아기 선물', 'https://gift.infoepic.com/%EC%84%A0%EB%AC%BC/0-3%EC%84%B8-%EC%95%84%EA%B8%B0-%EC%84%A0%EB%AC%BC/')]),
     h2('마치며'),
     p('아이 선물은 안전과 발달 단계를 고려하는 게 가장 중요합니다. 비싼 장난감보다 아이에게 맞는 장난감이 최고입니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')])

# 2. 커플 선물 고르는 법
create_or_update('커플-선물-고르는-법',
    '커플 선물 고르는 법 — 남자친구 여자친구 선물 총정리',
    '커플 선물, 항상 고민되시죠? 성별과 관계 기간에 따른 선물 고르는 법을 정리했습니다.',
    [h2('커플 선물, 왜 항상 어려울까요?'),
     p('연인에게 주는 선물은 친구나 가족과 달리 "감동"이 필요합니다. 너무 실용적이면 재미없고, 너무 비싸면 부담스럽습니다. 중요한 건 상대방의 취향을 얼마나 알고 있느냐입니다.'),
     h2('여자친구 선물 공식'),
     h3('1~3만원: 감성 아이템'),
     p('캔들, 디퓨저, 립 제품, 예쁜 머그컵 등 부담 없는 가격으로 센스를 보여줄 수 있는 아이템입니다.'),
     h3('3~7만원: 향수 트래블 세트'),
     p('조말론, 딥디크 트래블 세트가 가장 인기입니다. 여러 향을 시험해볼 수 있어 첫 향수 선물로 좋습니다.'),
     h3('7~15만원: 향수 정품, 스킨케어'),
     p('조말론, 디올 향수(7~13만원대), 설화수 스킨케어 세트 등이 좋습니다.'),
     h3('15만원+: 주얼리, 명품 액세서리'),
     p('14K 귀걸이, 목걸이, 반지 등 가치 있는 주얼리는 특별한 날에 어울립니다.'),
     h2('남자친구 선물 공식'),
     h3('1~3만원: 향수, 액세서리'),
     p('알파무드 향수(3만원대), 게이밍 마우스, 보조배터리 등이 부담 없는 가격입니다.'),
     h3('3~10만원: 전자기기, 패션'),
     p('무선 이어폰(중국브랜드 3~5만원), 게이밍 키보드, 운동화 등이 인기입니다.'),
     h3('10~20만원: 명품 향수, 시계'),
     p('샤넬 블루, 디올 소바쥬 향수(12~13만원대), 갤럭시 워치 등이 좋습니다.'),
     h2('커플 선물, 이것만 주의하세요'),
     p('① 너무 비싼 선물은 상대방에게 부담이 됩니다. 처음엔 가벼운 선물로 시작하세요.'),
     p('② "평소에 갖고 싶다고 말한 것"을 기억했다가 선물하면 가장 큰 감동을 줍니다.'),
     p('③ 발렌타인데이, 화이트데이, 크리스마스 같은 기념일에는 더 신경 써서 준비하세요.'),
     h2('참고하면 좋은 가이드'),
     plink([('• 남자친구 생일선물', 'https://gift.infoepic.com/%EC%84%A0%EB%AC%BC/%EB%82%A8%EC%9E%90%EC%B9%9C%EA%B5%AC-%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC/')]),
     plink([('• 여자친구 생일선물', 'https://gift.infoepic.com/%EC%84%A0%EB%AC%BC/%EC%97%AC%EC%9E%90%EC%B9%9C%EA%B5%AC-%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC/')]),
     plink([('• 발렌타인데이 선물', 'https://gift.infoepic.com/%EC%84%A0%EB%AC%BC/%EB%B0%9C%EB%A0%8C%ED%83%80%EC%9D%B8%EB%8D%B0%EC%9D%B4-%EC%84%A0%EB%AC%BC/')]),
     h2('마치며'),
     p('커플 선물은 가격보다 상대방을 얼마나 이해하고 있는지가 중요합니다. 오래 함께할수록 더 특별한 선물이 가능합니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.')])

print('\n🎉 2페이지 생성 완료!')
