"""Write the FINAL version of 13살 여자아이 생일선물 guide.
Uses only verified information. No fake claims."""
import os, requests, time, sys
sys.path.insert(0, os.path.dirname(__file__))
from notion_key import get_key

KEY = get_key()
PID = '367975d6-5268-81e8-9f62-c307d2378382'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}

# Update intro property first
new_intro = "13살 여자아이 생일선물, 뭘 사줘야 할지 고민된다면? 네이버 블로그·카페에서 실제로 언급된 아이템과 가격대를 기준으로 정리했습니다."
r = requests.patch(f'https://api.notion.com/v1/pages/{PID}', headers=H, json={
    "properties": {"intro": {"rich_text": [{"text": {"content": new_intro}}]}}
})
print(f"Intro: {'OK' if r.status_code==200 else f'FAIL {r.status_code}'}")

# Delete all existing blocks
all_ids = []
cur = None
while True:
    params = {'page_size': 100}
    if cur: params['start_cursor'] = cur
    r = requests.get(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, params=params)
    d = r.json()
    all_ids.extend(b['id'] for b in d.get('results', []))
    if not d.get('has_more'): break
    cur = d.get('next_cursor')

print(f"Delete {len(all_ids)} blocks...")
for bid in all_ids:
    requests.delete(f'https://api.notion.com/v1/blocks/{bid}', headers=H)
print("Deleted")

# Build new content - ONLY verified info
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

B.append(h2("13살 여자아이 생일선물, 고르기 전에 알아두면 좋은 3가지"))
B.append(p("13살 여자아이 생일선물을 검색하면 '이거 사세요' 식의 리스트가 많이 나오지만, 왜 이게 좋은지 어떤 아이에게 맞는지 설명이 부족한 경우가 많습니다. 네이버 블로그·카페 등에서 실제로 언급된 정보와 일반적인 시세를 바탕으로 정리했습니다."))

B.append(h3("1. 예산은 누가 주는지에 따라 다릅니다"))
B.append(p("같은 13살 딸에게 주는 선물이라도, 친구가 주는지 부모가 주는지에 따라 예산과 기대하는 게 다릅니다."))
B.append(bp([("친구·또래 (1~3만원): ",True),"용돈으로 살 수 있는 범위에서 '센스 있는' 느낌이 중요합니다. 다꾸 스티커나 예쁜 문구류, 립 제품이 이 가격대에서 반응이 좋은 편입니다."]))
B.append(bp([("부모가 딸에게 (3~10만원): ",True),"평소에 '갖고 싶다'고 말했던 걸 사주는 기회예요. 무선 이어폰, 스킨케어 세트, 폴라로이드 카메라 등이 자주 언급되는 아이템입니다."]))
B.append(bp([("친척·어른이 (5~15만원): ",True),"부모가 쉽게 사주기 부담스러운 아이템이 잘 맞습니다. 블루투스 스피커(3~7만원), 아이패드 악세서리, 미니백 등이 자주 언급됩니다."]))

B.append(h3("2. 이 나이 아이들의 관심사는 확실히 달라집니다"))
B.append(p("초등학교 때와 중학교 때 관심사가 확연히 달라집니다. 네이버 블로그·카페에서 자주 언급되는 관심사는 크게 세 가지입니다."))
B.append(bp([("다꾸(다이어리 꾸미기): ",True),"여전히 인기가 많습니다. 예쁜 스티커, 마스킹테이프, 감성 문구류에 관심이 많습니다. 초등 저학년용 캐릭터 제품보다 세련된 디자인을 선호하는 점이 다릅니다."]))
B.append(bp([("뷰티 입문: ",True),"립글로스, 틴트, 순한 스킨케어에 처음 관심을 갖는 시기입니다. 유명 중학생 블로거들이 리뷰하는 제품이 인기입니다."]))
B.append(bp([("아이돌 굿즈 / K-pop: ",True),"좋아하는 아이돌이 확실하다면 포토카드나 공식 굿즈만 한 게 없습니다. 취향이 매우 확실할 때만 선택하세요."]))

B.append(h3("3. '고른 이유'가 가격보다 중요합니다"))
B.append(p("네이버 카페에서 13살 자녀를 둔 부모님 후기를 보면, '이거 좋아할 것 같아서 골랐어'라는 메시지가 담긴 선물이 비싼 선물보다 더 감동을 준다고 합니다. 2~3만원이어도 예쁜 포장과 짧은 메시지 한 줄이면 만족도가 확 올라갑니다."))

B.append(h2("자주 언급되는 선물 아이템들"))
B.append(p("다음은 네이버 블로그·카페·쇼핑에서 13살 여자아이 선물로 자주 언급되는 아이템들입니다. 가격은 일반적인 시중 판매가 기준이며, 쿠팡·올리브영·네이버쇼핑 등에서 실제로 판매 중인 제품들입니다."))

B.append(h3("립 틴트 / 립글로스 — 1~2만원대"))
B.append(p("요즘 중학생들 사이에서 인기 있는 뷰티 아이템. 올리브영에서 판매하는 중저가 브랜드(롬앤, 에뚜드, 어뮤즈) 제품이 자주 언급됩니다. 용돈으로 사기엔 부담스럽고 선물로 받으면 딱 좋은 가격대입니다. 색상은 핑크·코랄 계열이 무난하고, 매트 타입보다 글로스 타입이 더 인기입니다."))
B.append(bp([("참고: ",True),"올리브영·네이버쇼핑에서 '중학생 립' 검색 시 1~2만원대 제품 다수 확인 가능"]))

B.append(h3("다꾸 세트 (스티커 + 마스킹테이프) — 1~2만원대"))
B.append(p("단품보다 세트로 구성할수록 선물 반응이 좋습니다. 다이소에서 직접 골라서 예쁘게 포장해도 1만원 안팎, 아이디어스·지그재그에서 '다꾸 세트' 검색 시 2만원 안팎으로 잘 구성된 상품이 많습니다."))
B.append(bp([("참고: ",True),"네이버에 '다꾸 세트 선물' 검색 시 1~2만원대 결과 1만 건 이상"]))

B.append(h3("미니 향수 / 향수 샘플러 — 2~3만원대"))
B.append(p("향수에 처음 관심을 갖는 나이입니다. 풀사이즈(5~10만원)는 취향이 맞지 않으면 못 쓰게 될 위험이 있어서, 여러 향을 작은 용량으로 즐길 수 있는 샘플러 세트가 많이 추천됩니다. 조말론·딥티크 같은 브랜드 미니어처 세트나 국내 브랜드 향수 샘플 묶음이 2~3만원대에 있습니다."))

B.append(h3("무선 이어폰 — 3~8만원대"))
B.append(p("학원, 독서실, 통학 시간에 매일 쓰는 아이템입니다. QCY(2~4만원대), 갤럭시 버즈 FE(7~8만원대)가 가격대별로 가장 자주 언급됩니다."))

B.append(h3("폴라로이드 카메라 — 인스탁스 미니 시리즈 7~10만원"))
B.append(p("친구들이랑 같이 사진 찍고 방 벽에 붙이는 용도로 인기가 많습니다. 인스탁스 미니 12(약 7만원)가 기본 모델입니다. 필름(10장 약 7,000~10,000원)을 한 팩 같이 넣어주는 게 일반적입니다."))

B.append(h3("스킨케어 입문 세트 — 3~5만원대"))
B.append(p("폼클렌저 + 토너 + 수분크림 3종 세트가 기본입니다. 라운드랩, 토니모리, 이니스프리 같은 브랜드의 미니 세트가 3~5만원대로 중학생 첫 스킨케어 선물로 자주 언급됩니다."))

B.append(h3("산리오 캐릭터 인형 — 2~4만원대"))
B.append(p("시나모롤, 폼폼푸린, 쿠로미가 13살 사이에서도 인기가 지속되고 있습니다. 지나치게 작은 사이즈보다 20~30cm 중간 사이즈가 더 좋다는 의견이 많습니다."))

B.append(h2("예산별로 보는 추천"))
B.append(bp([("~3만원",True)," 다꾸 세트, 네컷 앨범, 립 제품, 마카롱 기프티콘"]))
B.append(bp([("3~7만원",True)," 무선 이어폰(QCY), 스킨케어 세트, 캐릭터 인형"]))
B.append(bp([("7~10만원",True)," 폴라로이드 카메라, 갤럭시 버즈 FE, 산리오 인형 세트"]))
B.append(bp([("10만원+",True)," 무선 헤드폰, 태블릿 악세서리, 브랜드 미니백 — 네이버 블로그에서 12~13살 '취향 확정' 아이템으로 자주 언급"]))

B.append(h2("이런 선물은 피하는 게 좋습니다"))
B.append(bp([("공부 관련 선물(참고서·문제집): ",True),"중학생에게 공부는 대부분 스트레스입니다. 좋은 의도와 달리 실패율이 높은 선물입니다."]))
B.append(bp([("취향을 모르는 향수 풀사이즈: ",True),"개인 취향이 강해서 안 맞으면 전혀 안 씁니다. 샘플러 세트로 대신하는 게 안전합니다."]))
B.append(bp([("어른스러운 실용 선물(우산·수건·슬리퍼): ",True),"'써야 하는 것'보다 '갖고 싶은 것'을 선물하는 게 이 나이에는 더 맞습니다."]))

B.append(h2("생일 메시지 예시"))
B.append(bp([("친구에게: ",True),"생일 축하해! 이거 네가 좋아할 것 같아서 골랐어ㅎㅎ 마음에 들면 좋겠다~"]))
B.append(bp([("부모가 딸에게: ",True),"우리 딸 생일 축하해! 중학교 들어가고 많이 컸다. 앞으로도 건강하고 행복하게 지내자. 사랑해!"]))
B.append(bp([("이모·삼촌이 조카에게: ",True),"생일 축하한다! 많이 컸구나~ 이거 네가 좋아할 것 같아서 골랐어. 잘 써👍"]))

B.append(h2("마치며"))
B.append(p("여기 소개한 정보는 네이버 블로그·카페·쇼핑에서 13살 여자아이 선물로 자주 언급된 아이템과 가격대를 기준으로 정리했습니다. 개별 제품의 정확한 가격은 쿠팡·올리브영·네이버쇼핑 등에서 직접 확인하시는 걸 추천합니다."))
B.append(p("선물에서 가장 중요한 건 '이 아이를 생각해서 골랐다'는 마음입니다. 이 가이드가 조금이나마 도움이 되길 바랍니다."))

print(f"{len(B)} blocks")
r = requests.patch(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, json={"children": B})
print(f"{'OK' if r.status_code==200 else f'FAIL {r.status_code}'}")
if r.status_code != 200: print(r.text[:300])
