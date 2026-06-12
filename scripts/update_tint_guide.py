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
r = requests.post(f'https://api.notion.com/v1/databases/{GDB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'equals': slug}}, 'page_size': 3})
pid = r.json()['results'][0]['id']
print(f'{slug}: {pid}')

# Update intro
requests.patch(f'https://api.notion.com/v1/pages/{pid}', headers=H, json={
    'properties': {'intro': {'rich_text': [{'text': {'content': '틴트를 선물하고 싶은데 종류가 너무 많아서 고민이신가요? 피부톤, 제형, 브랜드별로 선물용 틴트 고르는 법을 정리했습니다.'}}]}}
})

# Wipe existing blocks
ids = []; cur = None
while True:
    pp = {'page_size': 100}
    if cur: pp['start_cursor'] = cur
    r2 = requests.get(f'https://api.notion.com/v1/blocks/{pid}/children', headers=H, params=pp)
    d = r2.json()
    ids.extend(b['id'] for b in d.get('results', []))
    if not d.get('has_more'): break
    cur = d.get('next_cursor')
for bid in ids: requests.delete(f'https://api.notion.com/v1/blocks/{bid}', headers=H)

B = [
    h2('틴트랑 립스틱이 뭐가 달라요?'),
    p('틴트와 립스틱, 둘 다 입술에 바르는 제품이지만 느낌이 완전히 다릅니다. 립스틱은 선명한 발색이 특징이고, 틴트는 입술에 착색되어 물이나 음식을 먹어도 쉽게 지워지지 않습니다. 선물용으로는 틴트가 더 안전합니다. 컵에 묻어날 일이 적고 자연스러워서 누가 받아도 부담이 없어요.'),

    h2('고르기 전, 이것부터 확인'),
    h3('피부톤 확인하기 (웜톤 vs 쿨톤)'),
    p('틴트를 고를 때 가장 중요한 건 받는 사람의 피부톤입니다. 간단한 확인법: 손목 안쪽 정맥 색이 푸르거나 자주색이면 쿨톤, 초록빛이면 웜톤입니다.'),
    p('쿨톤에게는 핑크, 베리, 푸시아 계열이 잘 어울립니다.'),
    p('웜톤에게는 코랄, 피치, 벽돌, 오렌지 계열이 잘 어울립니다.'),
    p('피부톤을 모른다면 코랄이나 로즈 계열이 가장 무난합니다.'),

    h3('틴트 제형의 차이'),
    p('틴트는 제형에 따라 느낌이 확실히 달라집니다:'),
    p('• 글로시/젤 틴트: 촉촉한 광택, 지속력은 보통. 첫 틴트 선물에 좋습니다.'),
    p('• 벨벳/블러 틴트: 보송한 느낌, 지속력이 좋음. 입술 주름을 부드럽게 잡아줍니다.'),
    p('• 워터 틴트: 가장 가볍고 자연스럽지만 지속력이 짧습니다.'),
    p('• 틴트 밤: 보습력이 강해서 건조한 입술에 좋습니다.'),

    h2('선물용 틴트, 이것만 골라도 실패 없음'),
    h3('1위. 어뮤즈 젤 핏 틴트 3호 누드 핑크'),
    p('어뮤즈는 비건 인증 브랜드로 10~20대 여성에게 인기가 많습니다. 3호 누드 핑크는 데일리로 사용하기 좋은 무난한 핑크 베이스 컬러로 첫 틴트 선물에 가장 추천합니다. 젤처럼 얇고 쫀쫀하게 발리면서 유리알 같은 광택이 특징입니다.'),

    h3('2위. 롬앤 쥬시 래스팅 틴트'),
    p('가성비의 대명사입니다. 인기 색상은 02 누키다미아, 03 베어 그레이프 등이 있습니다. 네이버 쇼핑과 SNS에서 가장 많이 보이는 틴트 중 하나입니다.'),

    h3('3위. 페리페라 잉크 무드 글로이 틴트'),
    p('쿨톤에게 잘 어울리는 05 어쩔체리가 특히 인기입니다. 발색이 선명하고 지속력이 좋아 선물용으로 인기입니다.'),

    h2('참고하면 좋은 사이트'),
    p('올리브영: 국내 최대 뷰티숍으로 실제 판매량 기반 베스트 랭킹이 가장 현실적인 지표입니다.'),
    p('화해: 성분 분석과 사용자 리뷰 데이터가 풍부합니다.'),
    p('글로우픽: 사용자 리뷰 기반 랭킹이 유용합니다.'),

    h2('포장도 반입니다'),
    p('틴트 선물의 성공 비결 중 하나는 포장입니다. 쇼핑백에 담거나 리본으로 묶는 것만으로도 받는 사람의 만족도가 확 올라갑니다.'),

    h2('마치며'),
    p('틴트는 가격 부담이 적고 실용적이라 선물용으로 안성맞춤입니다. 피부톤과 제형만 고려하면 실패 확률이 훨씬 줄어듭니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요.'),
]

r3 = requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children', headers=H, json={'children': B})
print(f'{"OK" if r3.status_code==200 else f"FAIL {r3.status_code}"} ({len(B)} blocks)')
