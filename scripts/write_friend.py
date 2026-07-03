import requests, sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

KEY = get_key()
PID = '367975d6-5268-81f1-9411-f9cd60a46660'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}

# Update intro
intro = "친구 생일선물, 예산은 얼마나 잡을지 뭘 사줘야 센스 있어 보일지 고민되시죠? 네이버 블로그·커뮤니티에서 실제로 언급된 아이템과 가격대를 정리했습니다."
requests.patch(f'https://api.notion.com/v1/pages/{PID}', headers=H, json={
    "properties": {"intro": {"rich_text": [{"text": {"content": intro}}]}}
})
print("Intro updated")

# Delete all blocks
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

B.append(h2("친구 생일선물, 고르기 전에 생각할 3가지"))
B.append(p("친구 생일선물은 연인 선물보다 덜 부담스럽지만, 그래도 '센스 없는 선물'은 피하고 싶습니다. 네이버 블로그와 커뮤니티에서 실제 사람들이 추천한 선물과 후기를 바탕으로 정리했습니다."))

B.append(h3("1. 관계의 친밀도와 예산"))
B.append(p("절친(베프)에게는 3~7만원, 가까운 친구에게는 1~3만원, 직장동료나 가벼운 친구 사이에는 1만원 이하도 부담 없습니다. 네이버 블로그 후기를 보면 비싼 선물보다 '내 취향을 고려해서 골랐구나'라는 느낌이 훨씬 중요하다는 의견이 많았습니다."))

B.append(h3("2. 성별에 따라 선물이 완전히 달라집니다"))
B.append(p("여자친구와 남자친구에게 주는 선물은 당연히 다르고, 같은 여자 친구여도 또래인지, 직장동료인지, 대학 친구인지에 따라 다른 선물이 잘 맞습니다."))

B.append(h3("3. 카카오톡 선물하기를 잘 활용하세요"))
B.append(p("네이버 블로그에서 '친구 생일선물'로 가장 많이 언급된 채널이 카카오톡 선물하기였습니다. 배송 걱정 없고, 받는 사람이 직접 교환할 수 있어서 실패 확률이 낮습니다. 특히 1~3만원대 선물은 카카오톡 선물하기가 가장 무난합니다."))

B.append(h2("여자 친구에게 인기 있는 선물"))
B.append(p("네이버 블로그에서 여자 친구 생일선물로 자주 언급된 아이템들입니다."))

B.append(h3("향초·캔들 세트 — 1~3만원대"))
B.append(p("카카오톡 선물하기에서도 1~2만원대 향초가 인기. 부담 없는 가격에 인테리어 소품으로도 좋고, 받는 사람이 향을 안 좋아해도 인테리어로 두기 좋아서 실패 확률이 낮습니다."))

B.append(h3("립 제품 세트 — 2~4만원대"))
B.append(p("여자 친구끼리는 서로의 메이크업 취향을 어느 정도 알기 때문에 립글로스나 틴트 세트가 자주 언급됩니다. 롬앤, 에뚜드, 어뮤즈 등 중저가 브랜드가 선물용으로 인기입니다."))

B.append(h3("소품·악세서리 — 1~3만원대"))
B.append(p("귀걸이, 반지, 헤어밴드 등 작은 악세서리는 부담 없는 가격에 자주 주고받는 선물입니다. 네이버 블로그에서 '우정링' (친구끼리 맞추는 반지)도 많이 언급됩니다."))

B.append(h2("남자 친구에게 인기 있는 선물"))
B.append(p("남자 친구 선물은 실용성이 가장 중요하다는 후기가 많습니다."))

B.append(h3("스킨케어·세안제 세트 — 2~5만원대"))
B.append(p("남자 친구는 스스로 스킨케어 제품을 잘 사지 않는 경우가 많아서, 세안제나 올인원 로션 세트가 의외로 반응이 좋습니다. 네이버 블로그에서 '남친 피부 관리 선물' 관련 글이 많았습니다."))

B.append(h3("디지털 악세서리 — 2~5만원대"))
B.append(p("보조배터리, 거치대, 케이블 정리 케이스, 무선 충전기 등 실용적인 아이템이 인기. 특히 휴대용 보조배터리(2~3만원대)가 가성비 좋은 선물로 자주 언급됩니다."))

B.append(h2("성별 무관, 누구에게나 무난한 선물"))
B.append(p("성별을 크게 타지 않으면서 센스 있는 선물로 평가받는 아이템들입니다."))

B.append(h3("카카오톡 기프티콘 — 1~5만원"))
B.append(p("가장 무난한 선택이지만, '그냥 기프티콘?'이라는 반응이 있을 수 있습니다. 커피 기프티콘보다는 배달음식 기프티콘(치킨, 피자, 떡볶이)이 더 정성이 느껴진다는 의견이 많았습니다."))

B.append(h3("다꾸·문구 세트 — 1~3만원대"))
B.append(p("여자 친구에게 특히 인기. 예쁜 다이어리 + 젤펜 세트, 스티커 북 등은 가격 대비 만족도가 높습니다."))

B.append(h3("홈카페 용품 — 2~5만원대"))
B.append(p("요즘 유행하는 홈카페 아이템. 텀블러, 머그컵 세트, 드립 커피 도구 등은 친구가 평소 커피를 즐겨 마시면 좋은 선택입니다."))

B.append(h2("예산별 추천"))
B.append(bp([("~1만원",True)," 카톡 기프티콘(치킨·피자·커피), 네컷 앨범, 간단한 악세서리"]))
B.append(bp([("1~3만원",True)," 향초·캔들, 다꾸 세트, 립 제품, 우정 반지, 보조배터리"]))
B.append(bp([("3~7만원",True)," 스킨케어 세트, 무선 충전기, 홈카페 세트, 인스탁스 필름 세트"]))
B.append(bp([("7만원+",True)," 헤드폰, 향수(취향 알 때만), 패션 아이템 — 절친 한정"]))

B.append(h2("이런 선물은 피하는 게 좋습니다"))
B.append(bp([("너무 개인적인 취향 선물(향수·옷): ",True),"친구의 취향을 모르면 특히 위험합니다. 옷은 사이즈가 맞아도 스타일이 안 맞으면 안 입게 됩니다."]))
B.append(bp([("실용성 0% 장식품: ",True),"인형, 피규어 등은 그 친구가 해당 캐릭터/아이템의 팬이 아니라면 집에서 먼지만 쌓입니다."]))
B.append(bp([("'필요해서' 산 느낌의 선물: ",True),"생색나는 선물보다 '네가 좋아할 것 같아서'라는 마음이 느껴지는 선물이 훨씬 반응이 좋습니다."]))

B.append(h2("친구에게 쓰는 생일 메시지 예시"))
B.append(p("선물만큼 메시지도 중요합니다. 친구 관계에 맞게 골라 쓰세요."))
B.append(bp([("절친에게: ",True),"생일 축하해! 내년에도 같이 보자. 이거 네가 좋아할 것 같아서 골랐어ㅎㅎ"]))
B.append(bp([("가까운 친구에게: ",True),"생일 축하해! 항상 고마워. 작은 거지만 맘에 들면 좋겠다~"]))
B.append(bp([("직장동료에게: ",True),"생일 축하드려요! 앞으로도 잘 부탁드립니다. 커피 한 잔 하세요 :)"]))
B.append(bp([("오랜만에 연락하는 친구에게: ",True),"오랜만이야! 생일 축하해. 소식 들었어. 다음에 한번 보자~"]))

B.append(h2("마치며"))
B.append(p("친구 생일선물에서 가장 중요한 건 '이 친구를 생각해서 골랐다'는 마음입니다. 비싼 선물보다 '아, 이 친구가 나를 알고 있구나'라는 느낌을 주는 게 훨씬 오래 기억에 남습니다."))
B.append(p("여기 정리한 정보는 네이버 블로그·쇼핑과 커뮤니티(네이트판·인스티즈)에서 언급된 아이템과 가격대를 기준으로 했습니다. 개별 상품의 가격은 쿠팡·네이버쇼핑·카카오톡 선물하기에서 직접 확인하세요."))

total = len(B)
print(f'{total} blocks')
r = requests.patch(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, json={"children": B})
print(f"{'OK' if r.status_code==200 else f'FAIL {r.status_code}'}")
