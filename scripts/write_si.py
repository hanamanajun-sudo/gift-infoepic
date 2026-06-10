"""Write 시어머니 선물 guide to Notion"""
import requests, sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

KEY = get_key()
PID = '367975d6-5268-81ab-8024-e8adbeddb137'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}

# Update intro
intro = "시어머니 선물, 취향도 모르고 너무 비싸도 눈치 보이죠. 네이버 블로그와 커뮤니티에서 실제 며느리들이 추천한 선물과 경험담을 정리했습니다."
r = requests.patch(f'https://api.notion.com/v1/pages/{PID}', headers=H, json={
    "properties": {"intro": {"rich_text": [{"text": {"content": intro}}]}}
})
print(f"Intro: {'OK' if r.status_code==200 else f'FAIL {r.status_code}'}")

# Delete all existing blocks
ids = []
cur = None
while True:
    params = {'page_size': 100}
    if cur: params['start_cursor'] = cur
    r = requests.get(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, params=params)
    d = r.json()
    ids.extend(b['id'] for b in d.get('results', []))
    if not d.get('has_more'): break
    cur = d.get('next_cursor')
print(f"Delete {len(ids)} blocks...")
for bid in ids:
    requests.delete(f'https://api.notion.com/v1/blocks/{bid}', headers=H)
print("Deleted")

# Build new content
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

B.append(h2("시어머니 선물, 고르기 전에 생각할 3가지"))
B.append(p("시어머니 선물은 엄마 선물보다 고민이 더 큽니다. 취향을 완전히 알기도 어렵고, 가격대도 너무 비싸도 싸도 눈치가 보이거든요. 네이버 블로그와 82쿡·네이트판 등 커뮤니티에서 실제 며느리들이 공유한 경험을 바탕으로 정리했습니다."))

B.append(h3("1. 관계의 거리에 맞는 가격대가 중요합니다"))
B.append(p("시어머니 선물에서 가장 많이 나오는 고민이 '적당한 가격'입니다. 가까운 관계일수록 부담 덜한 실용템(3~7만원)이 잘 맞고, 명절이나 생신처럼 특별한 날에는 조금 더 의미 있는 선물(7~15만원)이 좋습니다. 너무 고가면 오히려 '부담스럽다'는 반응이 많았다는 후기가 많습니다."))
B.append(bp([("평소 선물 (3~7만원): ",True),"건강식품, 간편한 의류, 홈카페 용품 등 일상에서 쓰기 좋은 것"]))
B.append(bp([("생신·명절 선물 (7~15만원): ",True),"한정식 식사권, 고급 스킨케어 세트, 건강검진 패키지 등"]))
B.append(bp([("특별한 기념 선물 (15만원+): ",True),"가족 여행, 금반지, 프리미엄 가전 등 형제들과 함께 준비"]))

B.append(h3("2. 50~60대 여성의 건강·편안함이 최우선"))
B.append(p("네이버 블로그 후기를 보면 시어머니 선물에서 가장 많이 언급되는 키워드가 '발 건강'과 '편안함'입니다. 나이가 들수록 발이 붓고 아프기 때문인데, 이런 실질적인 필요를 채워주는 선물이 만족도가 높습니다."))
B.append(bp([("발 건강: ",True),"워킹화, 기능성 실내화, 발 마사지기 — 네이버 블로그에서 '시어머니 만족도 ★★★★★'로 가장 많이 언급된 카테고리"]))
B.append(bp([("피부 관리: ",True),"고급 한방화장품(설화수·후), 에센스 세트 — 명절 선물 세트로 가장 인기"]))
B.append(bp([("편안한 휴식: ",True),"홈웨어·잠옷 세트, 목 마사지기, 온열 찜질기 — 평소 선물로 반응 좋음"]))

B.append(h3("3. '마음'을 가장 잘 전달하는 방법"))
B.append(p("82쿡 커뮤니티에서 시어머니 선물 후기를 보면, 단순히 비싼 선물보다 '며느리가 신경 써서 골랐구나'라는 느낌이 드는 선물이 훨씬 오래 기억에 남는다고 합니다. 예쁜 쇼핑백에 손편지 한 장이면 어떤 선물이라도 만족도가 올라갑니다."))

B.append(h2("네이버 블로그·쇼핑에서 자주 언급된 선물 아이템"))
B.append(p("다음은 네이버 블로그와 쇼핑에서 '시어머니 선물'로 자주 언급되는 아이템들입니다. 가격은 일반적인 시중 판매가 기준입니다."))

B.append(h3("워킹화 / 기능성 신발 — 7~15만원대"))
B.append(p("네이버 블로그에서 '시어머니 선물 만족도 1위'로 자주 꼽히는 아이템입니다. 나이가 들수록 발 건강이 중요해지는데, 며느리가 편한 신발을 사준 것 자체를 매우 고마워하신다는 후기가 많습니다. 르무통·나르지오 같은 브랜드의 가벼운 워킹화가 10만원 전후로 인기입니다."))
B.append(bp([("참고: ",True),"네이버쇼핑에서 '50대 여성 운동화' 검색 시 7~15만원대 제품 다수"]))

B.append(h3("고급 한방화장품 세트 — 10~20만원대"))
B.append(p("명절이나 생신 선물로 가장 전통적인 선택입니다. 설화수 자음 2종 기획세트(네이버 기준 약 15만원)가 대표적이고, 후(Who) 공진향 세트, 이니스프리 한방 라인도 자주 언급됩니다. 평소에 아끼던 브랜드가 있다면 더 좋고, 모르겠다면 설화수가 무난합니다."))

B.append(h3("간편한 홈웨어·잠옷 세트 — 3~6만원대"))
B.append(p("평소 선물로 부담 없이 드리기 좋습니다. 82쿡에서도 '시어머니가 편하게 입을 수 있는 홈웨어'가 선물 추천으로 자주 나옵니다. 실크나 면 100% 소재가 인기고, 색상은 차분한 톤이 무난합니다."))

B.append(h3("목·어깨 마사지기 — 4~8만원대"))
B.append(p("평소 '어깨가 아프다'거나 '목이 뻐근하다'는 말씀을 자주 하시는 시어머니께 추천합니다. 온열 기능이 있는 제품이 만족도가 높고, 너무 크지 않은 목 베개형이 실용적입니다."))

B.append(h3("건강기능식품 — 5~15만원대"))
B.append(p("홍삼(정관장), 종합비타민, 오메가3, 관절 건강 제품 순으로 인기입니다. 다만 '또 건강식품?'이라는 반응이 있을 수 있어서, 선물만 단독으로 주기보다 식사권이나 다른 선물과 함께 준비하는 게 더 좋다는 의견이 많았습니다."))

B.append(h3("외식·카페 상품권 — 3~10만원"))
B.append(p("요즘은 '경험 선물'의 가치가 높게 평가됩니다. 호텔 뷔페 이용권, 한정식 식사권 등이 특히 인기. '며느리와 단둘이 외식하는 날'을 만드는 것 자체가 큰 선물이 된다는 후기가 많습니다."))

B.append(h2("예산별 추천"))
B.append(bp([("~5만원",True),"홈웨어 세트, 목 마사지기, 건강기능식품(정관장 에브리데이)" ]))
B.append(bp([("5~10만원",True),"워킹화, 스킨케어 세트, 외식 상품권, 발 마사지기"]))
B.append(bp([("10~20만원",True),"설화수·후 기획세트, 건강검진 패키지, 한정식 식사권, 명품 패션 소품"]))
B.append(bp([("20만원+",True),"가족 여행, 프리미엄 가전(안마의자·공기청정기), 금반지 — 형제들과 분담"]))

B.append(h2("이런 선물은 피하는 게 좋습니다"))
B.append(bp([("너무 개인적인 취향의 선물(향수·옷): ",True),"사이즈·취향을 모르면 실패 확률이 높습니다. 특히 옷은 사이즈가 맞아도 스타일이 맞지 않으면 안 입게 됩니다."]))
B.append(bp([("주방용품·살림살이: ",True),"시어머니 입장에서 '며느리가 나보고 살림하라는 뜻?'으로 오해할 수 있다는 후기가 커뮤니티에서 자주 언급됩니다."]))
B.append(bp([("너무 고가의 선물: ",True),"되려 며느리에게 '부담된다'고 말씀하시는 경우가 많습니다. 형제들과 함께 준비하거나, 특별한 날로 의미를 더하는 게 좋습니다."]))

B.append(h2("생일·명절 메시지 예시"))
B.append(p("선물과 함께 짧은 메시지를 쓰면 감동이 두 배입니다."))
B.append(bp([("생신 선물과 함께: ",True),"어머니 생신 축하드려요. 평소에 need하실 것 같아서 준비했어요. 마음에 드시면 좋겠습니다."]))
B.append(bp([("명절 선물과 함께: ",True),"어머니, 그동안 건강하셨어요? 추석 잘 보내세요. 작은 선물 준비했는데 편하게 사용하세요."]))
B.append(bp([("특별한 날: ",True),"어머니, 그동안 감사했습니다. 저희가 마음을 모아 준비했어요. 앞으로도 건강하세요!"]))

B.append(h2("마치며"))
B.append(p("시어머니 선물은 며느리 입장에서 '너무하면 안 되는데, 너무 안 해도 안 되는' 애매한 고민이 많은 주제입니다. 여기 정리한 정보는 네이버 블로그·쇼핑과 82쿡·네이트판 커뮤니티에서 실제 며느리들이 공유한 후기와 경험을 바탕으로 했습니다."))
B.append(p("개별 상품의 정확한 가격과 재고는 쿠팡·네이버쇼핑·올리브영에서 직접 확인하시는 게 좋습니다. 이 가이드가 시어머니 선물 고민에 조금이라도 도움이 되길 바랍니다."))

total = len(B)
print(f"{total} blocks")
r = requests.patch(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, json={"children": B})
print(f"{'OK' if r.status_code==200 else f'FAIL {r.status_code}'}")
