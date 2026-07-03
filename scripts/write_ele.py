import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

KEY = get_key()
PID = '367975d6-5268-8172-ad56-cb0d5c22890a'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}

requests.patch(f'https://api.notion.com/v1/pages/{PID}', headers=H, json={
    "properties": {"intro": {"rich_text": [{"text": {"content": "초등학생 저학년(7~9세) 생일·어린이날 선물, 뭘 사줘야 좋아할까요? 네이버 블로그·쇼핑에서 실제 언급된 아이템을 정리했습니다."}}]}}
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
B.append(h2("초등학생 저학년 선물, 고르기 전에 생각할 3가지"))
B.append(p("초등학교 1~3학년(7~9세) 아이들은 아직 장난감을 좋아하지만, 학습에 대한 관심도 생기기 시작하는 시기입니다. 이 나이에 맞는 선물을 고르는 기준을 네이버 블로그와 쇼핑 정보를 바탕으로 정리했습니다."))
B.append(h3("1. '재미'와 '학습'의 균형"))
B.append(p("이 나이 아이들은 순수하게 재미있는 것도 좋아하지만, 부모님은 학습에 도움되는 것을 원합니다. 네이버 블로그에서 인기 있는 선물은 '재미있으면서도 두뇌 발달에 좋은' 아이템, 즉 보드게임, 과학 실험 키트, 블록 장난감 등입니다."))
B.append(h3("2. 캐릭터의 힘을 무시하지 마세요"))
B.append(p("초등 저학년은 포켓몬, 카카오프렌즈, 산리오 캐릭터의 영향력이 절대적입니다. 같은 문구 세트라도 캐릭터가 있으면 반응이 완전히 다릅니다."))
B.append(h3("3. 예산"))
B.append(bp([("친구·또래 (1~2만원): ",True),"캐릭터 문구 세트, 슬라임, 간식 선물"]))
B.append(bp([("부모 (3~7만원): ",True),"보드게임, 과학 키트, 블록 장난감, 키즈 카메라"]))
B.append(bp([("친척 (5~10만원): ",True),"닌텐도 스위치 게임, RC카, 자전거 악세서리"]))

B.append(h2("자주 언급된 선물 아이템"))
B.append(h3("보드게임 — 2~4만원대"))
B.append(p("네이버 쇼핑에서 '초등학생 선물' 카테고리에 자주 등장하는 아이템. 꼬치의달인 (약 3만원), 루미큐브 (약 3.5만원), 할리갈리 등이 가족과 함께 즐기기 좋습니다."))
B.append(h3("캐릭터 문구 세트 — 5,000~15,000원"))
B.append(p("카카오프렌즈 문구세트(약 5,800원), 포켓몬 필통 세트, 산리오 스티커 북 등 부담 없는 가격에 캐릭터가 들어간 문구 세트가 인기입니다."))
B.append(h3("슬라임·액체괴물 — 3,000~10,000원"))
B.append(p("요즘 초등학생 사이에서 슬라임은 꾸준한 인기 아이템입니다. 수제 슬라임(6,000~10,000원)이 네이버 쇼핑 리뷰 6,000개 이상으로 인기. 다만 옷이나 가구에 묻지 않도록 주의해야 합니다."))
B.append(h3("과학 실험 키트 — 1~3만원대"))
B.append(p("집에서 간단히 실험할 수 있는 과학 키트가 학습 효과와 재미를 모두 잡은 선물로 인기. 결정 성장 키트, 화산 폭발 실험, 태양광 자동차 등 종류가 다양합니다."))
B.append(h3("블록 장난감(레고) — 2~10만원대"))
B.append(p("레고는 초등 저학년 아이들에게 언제나 옳은 선택입니다. 레고 시티, 레고 프렌즈, 레고 마인크래프트 시리즈가 인기. 가격대가 다양해서 예산에 맞춰 고를 수 있습니다."))
B.append(h3("키즈 카메라 — 3~5만원대"))
B.append(p("아이 전용 즉석 카메라나 디지털 카메라가 인기. 인스탁스 미니 시리즈(7만원)가 대표적이지만, 전용 키즈 카메라 제품은 3~4만원대로 더 부담 없습니다."))

B.append(h2("예산별 추천"))
B.append(bp([("~2만원",True)," 캐릭터 문구 세트, 슬라임, 색연필·크레파스 세트, 간식 선물"]))
B.append(bp([("2~5만원",True)," 보드게임, 과학 키트, 블록(소형), 키즈 카메라"]))
B.append(bp([("5~10만원",True)," 레고(중형), 보드게임(대형), 닌텐도 스위치 게임팩, RC카"]))
B.append(bp([("10만원+",True)," 닌텐도 스위치, 자전거, 드론 — 부모님 한정"]))

B.append(h2("이런 선물은 피하는 게 좋습니다"))
B.append(bp([("너무 어려운 학습 교구: ",True),"아이가 따라오기 어려우면 금방 싫증냅니다. '재미'가 없는 선물은 오래 가지 않아요."]))
B.append(bp([("작은 부품이 많은 장난감(3세 미만 기준): ",True),"안전상 주의. 삼킴 위험이 있는 작은 부품은 피하는 게 좋습니다."]))
B.append(bp([("아이 취향을 모르는 옷: ",True),"초등 저학년도 자신이 좋아하는 캐릭터나 색깔이 있습니다. 모르면 실패 확률이 높습니다."]))

B.append(h2("생일 메시지 예시"))
B.append(bp([("친구에게: ",True),"생일 축하해! 이거 재밌어 보여서 샀어. 같이 놀자!"]))
B.append(bp([("부모가 아이에게: ",True),"생일 축하해! 우리 ○○이가 7살이 됐구나. 항상 건강하고 행복하자. 사랑해!"]))
B.append(bp([("이모·삼촌이 조카에게: ",True),"생일 축하한다! 요즘 이게 인기래. 잘 놀다가 공부도 열심히 해~"]))

B.append(h2("마치며"))
B.append(p("초등학생 저학년 선물의 핵심은 '재미 + 학습'의 균형과 캐릭터 활용입니다. 아이가 좋아하는 캐릭터가 무엇인지 먼저 확인하고, 그에 맞춰 고르면 실패 확률이 크게 줄어듭니다."))
B.append(p("여기 정리한 정보는 네이버 블로그·쇼핑에서 언급된 아이템과 가격대 기준입니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요."))

print(f'{len(B)} blocks')
r = requests.patch(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, json={"children": B})
print(f"{'OK' if r.status_code==200 else f'FAIL {r.status_code}'}")
