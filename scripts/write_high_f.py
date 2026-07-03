import requests, sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

KEY = get_key()
PID = '367975d6-5268-810c-919f-d9f1e36101f8'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}

intro = "고등학생 여자 생일선물, 뭘 사줘야 좋아할지 모르겠다면? 네이버 블로그·쇼핑에서 실제 언급된 아이템을 정리했습니다."
requests.patch(f'https://api.notion.com/v1/pages/{PID}', headers=H, json={
    "properties": {"intro": {"rich_text": [{"text": {"content": intro}}]}}
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

B.append(h2("고등학생 여자 생일선물, 고르기 전에 생각할 3가지"))
B.append(p("고등학생 여자아이는 중학생 때와 취향이 확 달라집니다. '귀여운' 것보다 '예쁜' 것을 더 선호하고, 자신만의 스타일이 생기기 시작하는 시기예요. 네이버 블로그와 쇼핑에서 실제로 언급된 아이템을 기준으로 정리했습니다."))

B.append(h3("1. '중학생 같은' 선물은 피하는 게 좋습니다"))
B.append(p("캐릭터 인형이나 지나치게 아동용 디자인의 문구류는 고등학생 여자아이에게 '유치하다'는 반응을 받을 수 있습니다. 대신 감성적인 디자인, 미니멀한 스타일의 제품이 더 잘 맞습니다. 네이버 블로그 후기에서도 '고등학생 여자 선물은 너무 아동용 같으면 안 된다'는 의견이 많았습니다."))

B.append(h3("2. 예산은 주는 사람에 따라"))
B.append(bp([("친구·또래 (1~3만원): ",True),"카톡 기프티콘, 문구 세트, 립 제품, 손편지"]))
B.append(bp([("부모 (3~8만원): ",True),"지갑, 스킨케어 세트, 무선 이어폰, 향수"]))
B.append(bp([("친척 (5~15만원): ",True),"브랜드 지갑, 헤드폰, 미니백 — 오래 쓸 수 있는 것"]))

B.append(h3("3. 이 나이에는 '나만의 스타일'이 중요합니다"))
B.append(p("고등학생이 되면 친구들과 다르게 보이고 싶은 욕구가 강해집니다. 그래서 '다들 갖고 있는' 뻔한 선물보다는 '나만의 취향을 고려한' 선물에 더 감동합니다."))

B.append(h2("고등학생 여자 선물로 자주 언급된 아이템"))

B.append(h3("지갑·카드지갑 — 2~5만원대"))
B.append(p("네이버 쇼핑에서 '고등학생 여자 지갑'이 관련 검색어로 많이 나옵니다. 교통카드, 학생증, 용돈을 넣을 반지갑이나 카드지갑이 실용적입니다. 10대 여성용 감성 디자인 브랜드(마땡킴, 에스콰이아, 헤지스) 제품이 인기입니다."))

B.append(h3("립 제품 세트 — 1~3만원대"))
B.append(p("13살 때보다 메이크업에 더 관심이 많아지는 나이입니다. 립글로스, 틴트, 립밤 세트가 부담 없는 가격에 인기. 롬앤, 에뚜드, 어뮤즈 등 중저가 브랜드 제품이 잘 맞습니다."))

B.append(h3("문구·다이어리 세트 — 1~3만원대"))
B.append(p("고등학생이 되어도 다꾸(다이어리 꾸미기) 문화는 이어집니다. 다만 초등학생용 캐릭터 문구보다 감성적인 디자인의 다이어리와 젤펜 세트가 더 잘 맞습니다. 리훈 메모지, 낼나 펜슬 파우치 같은 제품이 네이버 쇼핑에서 인기입니다."))

B.append(h3("향수 — 3~7만원대"))
B.append(p("여고생도 향수에 관심이 많습니다. 풀사이즈보다는 여러 향을 시도해볼 수 있는 샘플러 세트가 안전합니다. 프루티·플로럴 계열이 10대 여성에게 가장 인기 있는 향입니다."))

B.append(h3("무선 이어폰 — 3~8만원대"))
B.append(p("등하교, 학원 이동, 공부할 때까지 매일 쓰는 필수템. QCY(2~4만원)부터 갤럭시 버즈 FE(7~8만원), 에어팟(중고 5~8만원)까지 예산에 따라 선택 가능합니다."))

B.append(h3("스킨케어 세트 — 3~5만원대"))
B.append(p("여드름 관리, 피부 톤 등 외모에 관심이 많아지는 시기입니다. 순한 성분의 클렌징 폼, 토너, 수분크림 세트가 기본. 라운드랩, 이니스프리, 토니모리 브랜드가 자주 언급됩니다."))

B.append(h2("예산별 추천"))
B.append(bp([("~3만원",True)," 립 제품, 문구·다이어리 세트, 카톡 기프티콘, 향수 샘플러"]))
B.append(bp([("3~7만원",True)," 지갑, 스킨케어 세트, 무선 이어폰(QCY), 향수"]))
B.append(bp([("7~10만원",True)," 갤럭시 버즈FE, 브랜드 지갑, 헤드폰"]))
B.append(bp([("10만원+",True)," 미니백, 에어팟, 브랜드 향수 — 부모·친척 한정"]))

B.append(h2("이런 선물은 피하는 게 좋습니다"))
B.append(bp([("아동용 캐릭터 상품: ",True),"고등학생에게는 유치하게 느껴질 수 있습니다. 같은 문구라도 감성적인 디자인을 선택하세요."]))
B.append(bp([("사이즈 모르는 옷·신발: ",True),"성인 여성 사이즈에 가까워져서 더 위험합니다. 취향도 모르면서 사는 건 비추천."]))
B.append(bp([("공부 관련 선물(참고서): ",True),"수능 준비로 스트레스 많은 나이에 공부 관련 선물은 부담만 줍니다."]))

B.append(h2("생일 메시지 예시"))
B.append(bp([("친구에게: ",True),"생일 축하해! 요즘 유행한다고 해서 골랐어 ㅎㅎ 마음에 들면 좋겠다~"]))
B.append(bp([("부모가 딸에게: ",True),"생일 축하한다. 이제 고등학생이라 많이 컸구나. 앞으로도 건강하고 행복하게 지내길!"]) )
B.append(bp([("이모·삼촌이 조카에게: ",True),"생일 축하한다! 많이 컸구나~ 공부도 재미도 놓치지 말고, 화이팅!"]))
B.append(bp([("남자친구가 여자친구에게: ",True),"생일 축하해! 네가 좋아할 것 같아서 준비했어. 항상 고맙고 사랑해 ❤️"]))

B.append(h2("마치며"))
B.append(p("고등학생 여자 선물의 핵심은 '캐릭터 상품은 피하고, 감성적인 디자인을 선택하라'입니다. 초등학교 때 좋아하던 것과 고등학교 때 좋아하는 것이 확연히 다르다는 점을 기억하세요."))
B.append(p("여기 정리한 정보는 네이버 블로그·쇼핑에서 언급된 아이템과 가격대를 기준으로 했습니다. 개별 가격은 쿠팡·네이버쇼핑에서 직접 확인하세요."))

print(f'{len(B)} blocks')
r = requests.patch(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, json={"children": B})
print(f"{'OK' if r.status_code==200 else f'FAIL {r.status_code}'}")
