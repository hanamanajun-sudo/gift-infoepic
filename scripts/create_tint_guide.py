import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

K = get_key()
H = {'Authorization': f'Bearer {K}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}
GDB = '9603a00b-976b-4791-a129-d5f537e5db06'

def h2(t): return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def h3(t): return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
def p(t): return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}

slug = '틴트-처음-고르는-법'
title = '틴트 처음 고르는 법 — 남자도 쉽게! 선물용 틴트 추천'

intro = '선물로 틴트를 사고 싶은데 종류가 너무 많아서 고민이신가요? 컬러, 브랜드, 가격대별로 정리했습니다.'

blocks = [
    h2('틴트랑 립스틱이 뭐가 달라요?'),
    p('틴트와 립스틱, 둘 다 입술에 바르는 제품이지만 느낌이 완전히 다릅니다.'),
    p('립스틱은 선명하고 매트한 발색이 오래 가는 반면, 틴트는 입술에 착색되어 물이나 음식을 먹어도 쉽게 지워지지 않습니다. 틴트는 바르면 처음엔 물처럼 발리다가 시간이 지날수록 입술에 스며들어 자연스러운 혈색을 만들어줍니다.'),
    p('선물용으로는 틴트가 더 안전합니다. 컵에 묻어날 일이 적고, 자연스러워서 누가 받아도 부담이 없어요.'),

    h2('여자친구에게 틴트 사줄 때 꼭 알아야 할 3가지'),
    h3('① 컬러 — 무난한 게 최고'),
    p('선물용 틴트를 고를 때 가장 중요한 건 색상입니다. 취향을 모른다면 누구에게나 잘 어울리는 로즈 계열이나 코랄 계열이 무난합니다. 너무 진한 레드나 브라운 계열은 피하는 게 좋아요.'),
    p('네이버 쇼핑에서 "틴트 BEST"를 검색해보면 상위 랭킹 제품들이 공통적으로 로즈나 코랄 계열이라는 걸 알 수 있습니다.'),

    h3('② 브랜드 — 10~20대 여성 인기 브랜드'),
    p('틴트는 값비싼 브랜드보다 10~20대 여성 사이에서 인기 있는 브랜드가 선물 성공률이 높습니다. 대표적으로 롬앤, 어뮤즈, 에뛰드, 삐아, 페리페라가 있습니다. 네이버 쇼핑과 SNS에서 가장 많이 언급되는 브랜드입니다.'),

    h3('③ 가격대 — 부담 없이 1~3만원'),
    p('틴트의 적정 선물 가격은 1~3만원입니다. 부담스럽지 않으면서도 퀄리티가 좋은 제품이 많습니다. 2만원 전후 제품이 가장 인기입니다.'),

    h2('선물용 틴트, 이것만 골라도 실패 없음'),
    h3('1위. 어뮤즈 립글로우 발라지는 틴트'),
    p('13세부터 20대까지 폭넓게 인기 있는 제품입니다. 발색이 예쁘고 지속력이 좋아서 첫 틴트 선물로 가장 추천합니다.'),

    h3('2위. 롬앤 블러벨벳 틴트'),
    p('벨벳처럼 부드러운 발림성이 특징입니다. SNS에서 가장 많이 보이는 틴트 중 하나로, 10대 여자아이에게 특히 인기가 많습니다.'),

    h3('3위. 에뛰드 글로우 픽싱 틴트'),
    p('촉촉한 글로우 타입이라 건조한 입술에도 부담 없이 바를 수 있습니다. 은은한 광택이 있어 첫 틴트 선물로 인기입니다.'),

    h2('포장도 반입니다'),
    p('틴트 선물의 성공 비결 중 하나는 포장입니다. 쇼핑백에 담거나, 리본으로 묶거나, 귀여운 스티커를 붙이는 것만으로도 받는 사람의 만족도가 확 올라갑니다. 브랜드마다 선물 포장 서비스를 제공하는 경우도 있으니 구매 전 확인해보세요.'),

    h2('마치며'),
    p('틴트는 가격 부담이 적고 실용적이라 선물용으로 안성맞춤입니다. 처음이라면 위에 소개한 제품 중 하나를 골라보세요. 실패할 확률이 훨씬 줄어듭니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.'),
]

# Check if slug already exists
check = requests.post(f'https://api.notion.com/v1/databases/{GDB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'equals': slug}}, 'page_size': 3})
if check.json()['results']:
    print('슬러그 중복!')
    pid = check.json()['results'][0]['id']
    print(f'기존 페이지 업데이트: {pid}')
else:
    body = {
        'parent': {'database_id': GDB},
        'properties': {
            'Title': {'title': [{'text': {'content': title}}]},
            'slug': {'rich_text': [{'text': {'content': slug}}]},
            'intro': {'rich_text': [{'text': {'content': intro}}]},
            'published': {'checkbox': True},
        },
        'children': blocks
    }
    r = requests.post('https://api.notion.com/v1/pages', headers=H, json=body)
    if r.status_code == 200:
        print(f'✅ 생성 완료!')
    else:
        print(f'❌ 실패: {r.status_code} {r.text[:200]}')
