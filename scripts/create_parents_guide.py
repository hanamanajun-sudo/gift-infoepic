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
        if url:
            rt.append({'type':'text','text':{'content':txt,'link':{'url':url}}})
        else:
            rt.append({'type':'text','text':{'content':txt}})
    return {'object':'block','type':'paragraph','paragraph':{'rich_text':rt}}

slug = '부모님-선물-고르는-법'
title = '부모님 선물 고르는 법 — 엄마 아빠에게 감동을 주는 선물'
intro = '매년 부모님 선물 고민, 이제 끝내세요. 엄마와 아빠에게 딱 맞는 선물 고르는 방법을 정리했습니다.'

check = requests.post(f'https://api.notion.com/v1/databases/{GDB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'equals': slug}}, 'page_size': 3})

if check.json()['results']:
    print('❌ 슬러그 중복!')
    pid = check.json()['results'][0]['id']
    requests.patch(f'https://api.notion.com/v1/pages/{pid}', headers=H, json={
        'properties': {'intro': {'rich_text': [{'text': {'content': intro}}]}, 'Title': {'title': [{'text': {'content': title}}]}}})
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
    body = {
        'parent': {'database_id': GDB},
        'properties': {
            'Title': {'title': [{'text': {'content': title}}]},
            'slug': {'rich_text': [{'text': {'content': slug}}]},
            'intro': {'rich_text': [{'text': {'content': intro}}]},
            'published': {'checkbox': True},
        },
        'children': []
    }
    r = requests.post('https://api.notion.com/v1/pages', headers=H, json=body)
    pid = r.json()['id'] if r.status_code == 200 else None
    if not pid:
        print(f'❌ 생성 실패: {r.status_code}'); sys.exit(1)
    print('✅ 신규 생성')

blocks = [
    h2('부모님 선물, 왜 항상 어려울까요?'),
    p('부모님은 항상 "뭐 필요 없다"고 말씀하십니다. 하지만 그 말을 그대로 믿으면 안 됩니다. 부모님도 선물을 받으면 기뻐하십니다. 다만 본인이 필요하다고 생각하지 않거나, 자식에게 부담을 주기 싫어서 그렇게 말씀하시는 것뿐입니다.'),

    h2('엄마 선물, 이렇게 접근하세요'),
    h3('먼저 알아야 할 것'),
    p('엄마는 가족을 위해 자신을 희생하는 경우가 많습니다. 평소 엄마가 "하나 사고 싶다"고 말한 적이 있는 물건이나, 갖고 싶지만 본인이 사기엔 아까워하는 물건을 떠올려보세요.'),

    h3('추천 아이템'),
    p('• 건강기능식품: 정관장 에브리타임, 침향환 — 엄마 건강을 생각하는 마음이 전해집니다.'),
    p('• 편한 신발: 르무통 운동화 — 가볍고 발이 편해서 엄마 선물 1순위입니다.'),
    p('• 스킨케어: 설화수, AHC — 평소 좋아하는 브랜드가 있다면 그걸로 준비하세요.'),
    p('• 디저트: 떡케이크나 꽃다발 — 이벤트성 선물은 언제나 환영입니다.'),

    h2('아빠 선물, 이렇게 접근하세요'),
    h3('먼저 알아야 할 것'),
    p('아빠는 대부분 필요한 게 있어도 본인이 직접 삽니다. 그래서 아빠 선물은 "필요한데 귀찮아서 안 사고 있는 것"을 찾는 게 핵심입니다.'),

    h3('추천 아이템'),
    p('• 건강기능식품: 정관장 홍삼정, 산양삼 — 아빠 건강을 생각한 선물 1순위.'),
    p('• 실용 아이템: 지갑, 벨트, 명함케이스 — 낡은 지갑을 새 지갑으로 바꿔드리는 것만으로도 감동입니다.'),
    p('• 취미용품: 낚시용품, 등산용품, 정원용품 — 아빠 취미와 연결되면 성공입니다.'),

    h2('예산별 추천'),
    p('3~5만원: 건강 음료 세트, 스카프, 장갑'),
    p('5~10만원: 정관장 스틱, 편한 운동화, 마사지기'),
    p('10~20만원: 프리미엄 홍삼 세트, 한우 세트, 설화수'),
    p('20만원+: 안마의자(렌탈/구매), 부모님 해외여행'),

    h2('부모님 선물, 이것만 주의하세요'),
    p('① 비싼 것보다 정성이 중요합니다. 직접 전달하고 식사하는 시간을 함께하는 게 가장 좋은 선물입니다.'),
    p('② 부모님 건강 상태를 고려하세요. 당뇨가 있으신데 달콤한 간식 선물은 피해야 합니다.'),
    p('③ "매년 같은 선물"은 피하세요. 작년에 드렸던 선물과 다른 걸 준비하는 게 좋습니다.'),

    h2('관련 가이드'),
    plink([('• 엄마 생일선물 추천', 'https://gift.infoepic.com/%EC%84%A0%EB%AC%BC/%EC%97%84%EB%A7%88-%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC/')]),
    plink([('• 아빠 생일선물 추천', 'https://gift.infoepic.com/%EC%84%A0%EB%AC%BC/%EC%95%84%EB%B9%A0-%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC/')]),
    plink([('• 50대 부모님 생일선물', 'https://gift.infoepic.com/%EC%84%A0%EB%AC%BC/50%EB%8C%80-%EB%B6%80%EB%AA%A8%EB%8B%98-%EC%83%9D%EC%9D%BC%EC%84%A0%EB%AC%BC/')]),

    h2('마치며'),
    p('부모님 선물은 돈으로 환산할 수 없는 가치가 있습니다. 직접 안아드리는 것만으로도 큰 선물이 됩니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.'),
]

r3 = requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children', headers=H, json={'children': blocks})
print(f'{"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"} ({len(blocks)} blocks)')
