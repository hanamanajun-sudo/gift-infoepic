import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

KEY = get_key()
PID = '367975d6-5268-81f9-9e24-c497072c4118'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}

requests.patch(f'https://api.notion.com/v1/pages/{PID}', headers=H, json={
    "properties": {"intro": {"rich_text": [{"text": {"content": "1만원 이하 선물, 부담 없이 주고받기 좋은 아이템을 찾고 계신가요? 네이버 쇼핑·블로그에서 언급된 아이템을 정리했습니다."}}]}}
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
B.append(h2("1만원 이하 선물, 이럴 때 좋습니다"))
B.append(p("1만원 이하 선물은 '부담스럽지 않은 마음'을 전하기에 가장 좋은 가격대입니다. 부담 없이 주고받을 수 있지만, 센스 있는 선택이 돋보이는 아이템을 네이버 쇼핑·블로그에서 찾아 정리했습니다."))
B.append(h3("이런 상황에 추천"))
B.append(bp([("친구·동료 생일: ",True),"부담 없는 가격으로 '생각하고 있다'는 마음 전하기 좋음"]))
B.append(bp([("스승의날·어버이날: ",True),"작지만 정성이 담긴 선물 + 손편지 조합으로"]))
B.append(bp([("집들이·답례: ",True),"빈손으로 가기 애매할 때 부담 없는 아이템"]))
B.append(bp([("어린이날·크리스마스: ",True),"아이들 단체 선물, 교회·학교 행사 선물로"]))
B.append(bp([("카카오톡 선물하기: ",True),"배송 없이 바로 보낼 수 있는 1만원 이하 아이템 많음"]))

B.append(h2("자주 언급된 1만원 이하 선물"))
B.append(h3("캐릭터 문구 세트 — 3,000~8,000원"))
B.append(p("네이버 쇼핑에서도 리뷰 9,000개 이상인 인기 아이템. 카카오프렌즈 문구세트(약 5,800원), 포켓몬 필통, 산리오 스티커 세트 등이 대표적입니다. 초등학생 아이들에게 특히 좋은 반응입니다."))
B.append(h3("슬라임·액체괴물 — 3,000~9,000원"))
B.append(p("리뷰 6,000개 이상의 인기 아이템. 수제 슬라임은 색상과 향이 다양해서 아이들이 좋아합니다. 단, 어린아이에게 줄 때는 삼키지 않도록 주의가 필요합니다."))
B.append(h3("텀블러·물병 — 5,000~10,000원"))
B.append(p("요즘 누구나 하나씩 가지고 다니는 실용 아이템. 1만원 이하에서도 괜찮은 디자인의 텀블러를 찾을 수 있습니다. 카카오프렌즈, 산리오 캐릭터 텀블러가 특히 인기입니다."))
B.append(h3("간식 선물 — 5,000~10,000원"))
B.append(p("수제 약과, 마카롱 세트, 초콜릿 등 1만원 이하 간식 선물도 많습니다. 네이버 쇼핑에서 '선물용 간식' 검색 시 5,000원~1만원대 제품이 다양합니다."))
B.append(h3("소형 보조배터리 — 8,000~10,000원"))
B.append(p("5,000mAh 정도의 소형 보조배터리는 1만원 이하로 구매 가능합니다. 휴대성이 좋아 실용적인 선물로 인기."))
B.append(h3("향초·캔들 — 5,000~10,000원"))
B.append(p("카카오톡 선물하기에서도 1만원 이하 향초가 인기. 부담 없는 가격에 인테리어 소품으로도 좋고, 받는 사람이 향을 안 좋아해도 두고 보기 좋아서 실패 확률이 낮습니다."))

B.append(h2("1만원 이하 선물 고를 때 팁"))
B.append(p("1만원 이하 선물은 가격이 낮은 만큼 '포장'이 더 중요해집니다. 예쁜 쇼핑백이나 손편지 한 장만 있어도 5,000원짜리 선물이 2만원짜리처럼 느껴집니다. 카카오톡 선물하기를 이용하면 선물 포장이 자동으로 되어 있어 편리합니다."))

B.append(h2("이런 선물은 피하는 게 좋습니다"))
B.append(bp([("품질이 의심스러운 초저가 전자제품: ",True),"1만원 이하 블루투스 이어폰 등은 품질과 안전성이 의심됩니다."]))
B.append(bp([("유통기한 임박한 식품: ",True),"간식 선물은 신선도가 생명입니다. 유통기한 반드시 확인하세요."]))

B.append(h2("마치며"))
B.append(p("1만원 이하 선물은 가격이 낮다고 해서 '센스'까지 낮은 건 아닙니다. 받는 사람의 취향을 고려한 작은 선물 하나가 때로는 고가의 선물보다 더 오래 기억에 남습니다."))
B.append(p("여기 정리한 정보는 네이버 블로그·쇼핑에서 언급된 아이템 기준입니다. 개별 가격은 쿠팡·네이버쇼핑에서 확인하세요."))

print(f'{len(B)} blocks')
r = requests.patch(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, json={"children": B})
print(f"{'OK' if r.status_code==200 else f'FAIL {r.status_code}'}")
