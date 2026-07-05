"""P5: 아들-생일선물 Notion 신규 페이지 생성"""
import os, json, urllib.request, unicodedata
project = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(project, '.env')) as f:
    for line in f:
        l = line.strip()
        if '=' in l and not l.startswith('#'):
            k, v = l.split('=', 1)
            os.environ[k.strip()] = v.strip().strip('"')
KEY = os.environ['NOTION_API_KEY']
GID = os.environ['NOTION_GUIDES_DB_ID']
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}
def n(method, path, body=None):
    url = f'https://api.notion.com/v1/{path}'
    d = json.dumps(body, ensure_ascii=False).encode() if body else None
    req = urllib.request.Request(url, data=d, headers=H, method=method)
    with urllib.request.urlopen(req) as resp: return json.loads(resp.read())
def rt(t): return [{'type': 'text', 'text': {'content': unicodedata.normalize('NFC', t)}}]
def h2(t): return {'object': 'block', 'type': 'heading_2', 'heading_2': {'rich_text': rt(t)}}
def h3(t): return {'object': 'block', 'type': 'heading_3', 'heading_3': {'rich_text': rt(t)}}
def p(t): return {'object': 'block', 'type': 'paragraph', 'paragraph': {'rich_text': rt(t)}}
def b(t): return {'object': 'block', 'type': 'bulleted_list_item', 'bulleted_list_item': {'rich_text': rt(t)}}

# Create new page in GiftGuides DB
page = n('POST', 'pages', {
    'parent': {'database_id': GID},
    'properties': {
        'Title': {'title': [{'type': 'text', 'text': {'content': '아들 생일선물 추천 TOP10 — 나이별 총정리 (2026년)'}}]},
        'slug': {'rich_text': [{'type': 'text', 'text': {'content': '아들-생일선물'}}]},
        'published': {'checkbox': True},
        'description': {'rich_text': [{'type': 'text', 'text': {'content': '아들 생일선물, 나이별로 무엇을 줘야 할까? 0세부터 고등학생까지 연령대별 추천 선물을 한 페이지에서 확인하세요.'}}]},
        'intro': {'rich_text': [{'type': 'text', 'text': {'content': '아들 생일선물 고민, 나이마다 천차만별입니다. 유아기에는 안전한 장난감을, 초등 저학년에는 만들기·캐릭터를, 고학년에는 실용템을, 중고등학생에게는 취향을 존중하는 선물이 필요합니다. 이 페이지에서는 아들 나이대별로 가장 좋은 반응을 보였던 선물을 연령별로 정리했습니다.'}}]},
        'occasion': {'multi_select': [{'name': '생일'}]},
        'relation': {'multi_select': [{'name': '아들'}, {'name': '조카'}]},
        'recipientGender': {'select': {'name': '남아'}},
        'interests': {'multi_select': [{'name': '장난감'}, {'name': '레고'}, {'name': '게임'}, {'name': '스포츠'}, {'name': '실용'}]},
    }
})
gid = page['id']
print(f'✅ 아들-생일선물 페이지 생성됨 (ID: {gid})')

# Blocks: 연령대별 점프링크 허브
blocks = [
    h2('아들 나이별 선물 한눈에 보기'),
    p('아래에서 아들의 나이 또는 학년에 맞는 선물 가이드로 바로 이동할 수 있습니다. 각 가이드는 블로그 후기, 유튜브 댓글, 일본 커뮤니티 데이터를 교차 검증해서 엄선했습니다.'),
    h3('👶 유아기 (0~3세)'),
    p('0~3세 아기에게는 안전하고 감각을 자극하는 선물이 가장 중요합니다. 단순한 소리·빛 장난감보다 촉감 놀이, 원목 블록, 그림책 등이 발달에 도움이 됩니다.'),
    p('👉 추천 가이드: /선물/0-3세-아기-선물/, /선물/4-6세-유아-선물/'),
    h3('🧒 미취학·초등 저학년 (4~6세, 7~9세)'),
    p('4~6세는 공룡·자동차·캐릭터에 폭발적 관심을 보이는 시기입니다. 7~9세는 초등학교에 막 입학하여 친구 관계가 생기고, 포켓몬카드·레고·야구글러브 등 본격적인 취미가 시작됩니다.'),
    p('👉 추천 가이드: /선물/4-6세-유아-선물/, /선물/7-9세-남자아이-생일선물/'),
    h3('📚 초등 고학년 (10~12세)'),
    p('10~12세는 초등학교 3~6학년으로, 장난감에서 점차 실용템으로 관심이 옮겨가는 시기입니다. 레고·드론·시계·지갑 등 "어른스러운" 선물에 반응하기 시작합니다. 12살은 GSC(Google Search Console)에서 아들 선물 키워드 중 가장 높은 검색량을 기록했습니다.'),
    p('👉 추천 가이드: /선물/10세-남자아이-생일선물/, /선물/12세-남자아이-생일선물/, /선물/13세-남자아이-생일선물/'),
    h3('🎒 중학생 (13~16세)'),
    p('중학생 아들은 더 이상 "아이 취급" 받는 걸 싫어합니다. 선물도 실용적이면서도 센스 있는 아이템이 필요합니다. 무선 이어폰, 스마트워치, 향수, 문화상품권 등이 인기입니다.'),
    p('👉 추천 가이드: /선물/13세-남자아이-생일선물/, /선물/중학생-남자-생일선물/, /선물/16세-남자아이-생일선물/'),
    h3('🎓 고등학생 (17~19세)'),
    p('고등학생 아들은 본인이 원하는 게 뭔지 가장 잘 압니다. 직접 묻는 것도 방법이지만, 무난한 선택으로는 무선 이어폰이나 향수, 브랜드 악세사리 등이 있습니다.'),
    p('👉 추천 가이드: /선물/고등학생-남자-생일선물/, /선물/17-19세-남자아이-생일선물/'),
    h2('아들 생일선물, 이것만 알면 실패 없다'),
    p('아들 선물의 핵심은 "나이에 맞는 선물"과 "아이의 취향 존중"입니다. 아래 팁을 참고하세요:'),
    b('5세 이하: 안전성 최우선. 작은 부품 삼킴 위험 없는 완구를 고르세요.'),
    b('6~9세: 아이가 좋아하는 캐릭터나 취미(공룡·포켓몬·레고)를 먼저 관찰하세요.'),
    b('10~12세: 장난감과 실용템의 중간. 시계·지갑·드론처럼 "어른스러운" 선물이 통합니다.'),
    b('13세 이상: 직접 묻는 게 가장 빠릅니다. 부모님 취향보다 아이의 취향을 우선하세요.'),
    p('더 자세한 내용은 각 연령별 가이드 페이지를 참고하세요.'),
]

n('PATCH', f'blocks/{gid}/children', {'children': blocks})
print(f'✅ 본문 블록 {len(blocks)}개 추가 완료')
print('P5: 아들-생일선물 Notion 생성 + 블록 작성 완료')
