import requests, sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

KEY = get_key()
PID = '367975d6-5268-81ef-a5ce-f2abf6c038f7'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}

intro = "고등학생 남자 생일선물, 뭘 사줘야 할지 고민이세요? 네이버 블로그에서 실제 언급된 아이템과 가격대를 정리했습니다."
requests.patch(f'https://api.notion.com/v1/pages/{PID}', headers=H, json={
    "properties": {"intro": {"rich_text": [{"text": {"content": intro}}]}}
})
print("Intro updated")

ids = []
cur = None
while True:
    p = {'page_size': 100}
    if cur: p['start_cursor'] = cur
    r = requests.get(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, params=p)
    d = r.json()
    ids.extend(b['id'] for b in d.get('results', []))
    if not d.get('has_more'): break
    cur = d.get('next_cursor')
print(f'Delete {len(ids)} blocks')
for bid in ids:
    requests.delete(f'https://api.notion.com/v1/blocks/{bid}', headers=H)
print('Deleted')

def h2(t): return {"object":"block","type":"heading_2","heading_2":{"rich_text":[{"type":"text","text":{"content":t}}]}}
def h3(t): return {"object":"block","type":"heading_3","heading_3":{"rich_text":[{"type":"text","text":{"content":t}}]}}
def p(t): return {"object":"block","type":"paragraph","paragraph":{"rich_text":[{"type":"text","text":{"content":t}}]}}
def bp(pts):
    r = []
    for pt in pts:
        if isinstance(pt,tuple): r.append({"type":"text","text":{"content":pt[0]},"annotations":{"bold":True}})
        else: r.append({"type":"text","text":{"content":pt}})
    return {"object":"block","type":"paragraph","paragraph":{"rich_text":r}}

B = []

B.append(h2("고등학생 남자 생일선물, 고르기 전에 생각할 3가지"))
B.append(p("고등학생 남자아이는 어린이와 어른의 중간이라 선물 고르기가 애매합니다. 게임 좋아하는 아이, 향수에 관심 생긴 아이, 운동하는 아이까지 취향이 다양해서 더 고민되죠. 네이버 블로그에서 실제 언급된 아이템을 기준으로 정리했습니다."))

B.append(h3("1. 고등학생이 된 남자아이의 취향 변화"))
B.append(p("고등학생이 되면 초등학생 때처럼 장난감이나 단순한 문구류보다 '실제로 쓰는 것'을 더 선호합니다. 특히 10대 후반으로 갈수록 향수, 지갑, 헤드폰처럼 '어른스러운' 아이템에 관심이 생깁니다. 네이버 블로그 후기에서 '고등학생 남자 선물은 향수가 가장 무난했다'는 의견이 많았습니다."))

B.append(h3("2. 예산은 주는 사람에 따라"))
B.append(bp([("친구·또래 (1~3만원): ",True),"편의점 기프티콘, 게임 아이템, 향수 샘플러 등 부담 없는 선물"]))
B.append(bp([("부모 (3~10만원): ",True),"무선 이어폰, 향수 풀사이즈, 지갑, 게이밍 마우스 등 실용템"]))
B.append(bp([("친척 (5~15만원): ",True),"헤드폰, 스마트워치, 브랜드 지갑 등 오래 쓸 수 있는 것"]))

B.append(h3("3. 이 나이 아이들은 '어른스러운' 선물을 원합니다"))
B.append(p("고등학생 남자는 '학생 티 나는 선물'보다 '어른이 된 느낌'이 드는 선물을 더 좋아하는 경향이 있습니다. 지나치게 아동용 같은 디자인보다는 심플하고 정제된 디자인의 제품이 반응이 좋았습니다."))

B.append(h2("고등학생 남자 선물로 자주 언급된 아이템"))

B.append(h3("향수 — 2~8만원대"))
B.append(p("네이버 블로그에서 '고등학생 남자 생일선물'로 가장 많이 언급된 아이템입니다. 특히 알파무드 같은 중저가 브랜드 향수가 2~5만원대로 인기. 우디향, 시트러스 계열이 무난하고, 10대 남성에게 무겁지 않은 향이 잘 맞는다는 후기가 많았습니다."))
B.append(bp([("참고: ",True),"네이버에서 '10대 남자 향수 추천' 검색 시 2~5만원대 제품 다수"]))

B.append(h3("무선 이어폰·헤드폰 — 3~10만원대"))
B.append(p("등하교 길, 학원, 공부할 때까지 매일 쓰는 필수 아이템. QCY(2~4만원)부터 갤럭시 버즈 FE(7~8만원)까지 예산에 따라 선택. 헤드폰은 게임용·음악감상용으로도 인기가 많습니다."))

B.append(h3("지갑·카드지갑 — 2~5만원대"))
B.append(p("고등학생이 되면 교통카드, 학생증, 용돈을 넣을 지갑이 필요해집니다. 마땡킴·헤지스 같은 브랜드의 심플한 카드지갑이 블로그에서 자주 언급되었습니다. 블랙이나 네이비 계열이 무난합니다."))

B.append(h3("게이밍 마우스·키보드 — 3~10만원대"))
B.append(p("게임을 좋아하는 고등학생 남자라면 가장 확실한 선택. 로지텍 G 시리즈 마우스, 기계식 키보드(적축·청축)가 인기입니다. 다만 평소 게임을 하는지 확인 후 고르는 게 좋습니다."))

B.append(h3("스킨케어 세트 — 2~5만원대"))
B.append(p("여드름 관리에 신경 쓰기 시작하는 나이라 클렌징 폼, 토너, 올인원 로션 세트가 잘 맞습니다. 네이버 블로그에서 '남자 고등학생 피부 관리 선물' 관련 글이 많았습니다."))

B.append(h2("예산별 추천"))
B.append(bp([("~3만원",True)," 향수 샘플러, 게임 기프티콘, 편의점 기프티콘, 카드지갑"]))
B.append(bp([("3~7만원",True)," 무선 이어폰(QCY), 향수(알파무드), 게이밍 마우스, 스킨케어 세트"]))
B.append(bp([("7~10만원",True)," 갤럭시 버즈FE, 헤드폰, 브랜드 지갑, 기계식 키보드"]))
B.append(bp([("10만원+",True)," 스마트워치, 무선 헤드폰, 브랜드 향수 — 부모·친척 한정"]))

B.append(h2("이런 선물은 피하는 게 좋습니다"))
B.append(bp([("'초등학생 같은' 장난감·캐릭터 상품: ",True),"고등학생은 '어른 취급' 받고 싶어하는 나이입니다. 지나치게 어려 보이는 선물은 반응이 좋지 않습니다."]))
B.append(bp([("사이즈 모르는 옷·신발: ",True),"성장기라 사이즈가 빠르게 변합니다. 모르면 실패 확률이 높습니다."]))
B.append(bp([("공부 관련 선물(참고서·문제집): ",True),"좋은 의도와 달리 부담만 줍니다. 대신 '공부할 때 쓰는 것' (헤드폰, 독서등)은 괜찮습니다."]))

B.append(h2("생일 메시지 예시"))
B.append(bp([("친구에게: ",True),"생일 축하해! 이거 써보고 괜찮아서 골랐어 ㅎㅎ 잘 쓰면 돼~"]))
B.append(bp([("부모가 아들에게: ",True),"생일 축하한다. 고등학생 됐으니까 이제 어른스러운 것도 써 봐라. 맘에 들었으면 좋겠다."]))
B.append(bp([("이모·삼촌이 조카에게: ",True),"생일 축하한다! 고등학생이라 많이 컸구나. 공부도 운동도 화이팅!"]))
B.append(bp([("여자친구가 남자친구에게: ",True),"생일 축하해! 네가 좋아할 것 같아서 골랐어. 앞으로도 잘 부탁해 ㅎㅎ"]))

B.append(h2("마치며"))
B.append(p("고등학생 남자 선물의 핵심은 '어른스러우면서도 실용적인' 아이템을 고르는 것입니다. 같은 돈을 써도 '학생 티 나는' 선물보다는 '처음 가져보는' 어른스러운 선물이 훨씬 오래 기억에 남습니다."))
B.append(p("여기 정리한 정보는 네이버 블로그에서 실제로 언급된 아이템과 가격대를 기준으로 했습니다. 개별 상품의 가격은 쿠팡·네이버쇼핑에서 확인하세요."))

total = len(B)
print(f'{total} blocks')
r = requests.patch(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, json={"children": B})
print(f"{'OK' if r.status_code==200 else f'FAIL {r.status_code}'}")
