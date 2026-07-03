import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

KEY = get_key()
PID = '367975d6-5268-81ae-97e9-c0510536458c'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}

requests.patch(f'https://api.notion.com/v1/pages/{PID}', headers=H, json={
    "properties": {"intro": {"rich_text": [{"text": {"content": "중학생 남자 생일선물, 고민되시죠? 네이버 블로그·쇼핑에서 실제로 언급된 아이템과 가격대를 정리했습니다."}}]}}
})
print("Intro done")

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
for bid in ids: requests.delete(f'https://api.notion.com/v1/blocks/{bid}', headers=H)
print(f'Deleted {len(ids)}')

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
B.append(h2("중학생 남자 생일선물, 고르기 전에 생각할 3가지"))
B.append(p("중학생 남자아이는 초등학생과 고등학생의 중간이라 선물 고르기가 특히 애매합니다. 아직 어린 취향이 남아있으면서도 '어른스러운' 것에 관심이 생기기 시작하는 시기예요. 네이버 블로그에서 언급된 아이템을 기준으로 정리했습니다."))
B.append(h3("1. 아직은 '장난감'과 '실용템'의 중간"))
B.append(p("초등학생처럼 장난감만 좋아하지도 않고, 고등학생처럼 완전히 실용적인 것만 원하지도 않습니다. '재미있으면서도 쓸모 있는' 아이템이 중학생 남자 선물로 가장 잘 맞습니다. 보드게임, 무선 이어폰, 조명, 운동용품 등이 대표적입니다."))
B.append(h3("2. 예산은 부담 없게"))
B.append(bp([("친구·또래 (1~2만원): ",True),"편의점 기프티콘, 문구 세트, 게임 아이템"]))
B.append(bp([("부모 (3~7만원): ",True),"무선 이어폰, 운동화, 보드게임, 가방"]))
B.append(bp([("친척 (5~10만원): ",True),"헤드폰, 스마트워치, 브랜드 운동화"]))
B.append(h3("3. '갖고 노는' 것보다 '쓰는' 것을"))
B.append(p("중학생이 되면 친구 관계, 취미, 외모에 신경 쓰기 시작합니다. 그래서 '방에 전시해두는' 선물보다 '실제로 매일 쓰는' 선물이 더 만족도가 높습니다."))

B.append(h2("자주 언급된 선물 아이템"))
B.append(h3("무선 이어폰 — 2~5만원대"))
B.append(p("학원, 통학 길, 게임할 때까지 중학생도 무선 이어폰은 필수템입니다. QCY(2~3만원)가 가장 무난하고, 아이폰 유저는 중고 에어팟도 좋은 선택입니다."))
B.append(h3("보드게임 — 2~5만원대"))
B.append(p("친구들과 함께 즐길 수 있는 보드게임은 중학생 남자아이에게 '재미+실용'을 모두 만족시키는 선물입니다. 할리갈리, 젠가, 루미큐브 등이 인기. 친구들 초대해서 같이 놀 수 있는 아이템이라 반응이 좋습니다."))
B.append(h3("무선 충전식 LED 조명 — 1~3만원대"))
B.append(p("책상에서 공부할 때나 방 분위기를 바꿀 때 쓸 수 있는 무선 조명. 네이버 쇼핑에서 5,000원~2만원대로 다양합니다. 터치 방식, 타이머 기능이 있는 제품이 인기입니다."))
B.append(h3("운동화 — 5~10만원대"))
B.append(p("중학생 남자아이는 활동량이 많아서 운동화를 자주 신습니다. 아식스, 뉴발란스, 나이키 등 브랜드 운동화가 부모님 선물로 인기. 다만 발 사이즈를 정확히 알아야 합니다."))
B.append(h3("스킨케어 기본 세트 — 2~4만원대"))
B.append(p("사춘기 시절이라 피부 관리에 관심이 생기기 시작하지만, 스스로 제품을 사지는 않는 경우가 많습니다. 클렌징 폼 + 올인원 로션 정도의 가벼운 세트면 부담 없이 시작할 수 있습니다."))

B.append(h2("예산별 추천"))
B.append(bp([("~2만원",True)," LED 조명, 문구 세트, 보드게임(소형), 기프티콘"]))
B.append(bp([("2~5만원",True)," 무선 이어폰(QCY), 보드게임, 스킨케어 세트, 가방"]))
B.append(bp([("5~10만원",True)," 운동화, 헤드폰, 스마트워치(저가형)"]))
B.append(bp([("10만원+",True)," 브랜드 운동화, 태블릿 악세서리 — 부모·친척 한정"]))

B.append(h2("이런 선물은 피하는 게 좋습니다"))
B.append(bp([("초등학생용 장난감: ",True),"중학생이 갖기에는 유치해 보입니다. 레고나 프라모델처럼 만들기 취미가 있는 경우는 예외."]))
B.append(bp([("공부 관련 선물: ",True),"중학교는 초등보다 학업 스트레스가 커지는 시기. 참고서나 문제집은 최악의 선물입니다."]))
B.append(bp([("사이즈 모르는 옷·신발: ",True),"성장기라 사이즈가 빠르게 변합니다. 특히 신발은 반 사이즈 차이가 큽니다."]))

B.append(h2("생일 메시지 예시"))
B.append(bp([("친구에게: ",True),"생일 축하해! 이거 재밌어 보여서 골랐어 ㅎㅎ 다음에 같이 하자~"]))
B.append(bp([("부모가 아들에게: ",True),"생일 축하한다! 중학생이라 많이 컸구나. 맘에 들었으면 좋겠다."]))
B.append(bp([("이모·삼촌이 조카에게: ",True),"생일 축하한다! 요즘 중학생들이 좋아하는 거라는데 맘에 들었으면 좋겠다~"]))

B.append(h2("마치며"))
B.append(p("중학생 남자 선물은 '재미'와 '실용'의 균형이 가장 중요합니다. 아이의 취미와 관심사를 먼저 파악하고, 그에 맞는 아이템을 고르는 게 가장 좋은 방법입니다."))
B.append(p("여기 정리한 정보는 네이버 블로그·쇼핑에서 언급된 아이템과 가격대 기준입니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요."))

print(f'{len(B)} blocks')
r = requests.patch(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, json={"children": B})
print(f"{'OK' if r.status_code==200 else f'FAIL {r.status_code}'}")
