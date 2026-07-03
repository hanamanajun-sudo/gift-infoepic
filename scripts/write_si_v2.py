"""Finish 시어머니 guide - delete remaining 3, append all"""
import requests, sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

KEY = get_key()
PID = '367975d6-5268-81ab-8024-e8adbeddb137'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}

# Delete remaining 3
r = requests.get(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, params={'page_size': 10})
for b in r.json().get('results', []):
    requests.delete(f'https://api.notion.com/v1/blocks/{b["id"]}', headers=H)
    time.sleep(0.1)
print("Remaining blocks deleted")

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
B.append(p("시어머니 선물은 엄마 선물보다 고민이 더 큽니다. 취향을 완전히 알기도 어렵고, 가격대도 너무 비싸도 싸도 눈치가 보이거든요. 네이버 블로그와 커뮤니티(82쿡·네이트판)에서 실제 며느리들이 공유한 경험을 바탕으로 정리했습니다."))
B.append(h3("1. 관계의 거리에 맞는 가격대가 중요합니다"))
B.append(p("시어머니 선물에서 가장 많이 나오는 고민이 '적당한 가격'입니다. 너무 고가면 오히려 '부담스럽다'는 반응이 많았다는 후기가 많습니다."))
B.append(bp([("평소 선물 (3~7만원): ",True),"건강식품, 간편한 의류, 홈카페 용품 등 일상에서 쓰기 좋은 것"]))
B.append(bp([("생신·명절 선물 (7~15만원): ",True),"한정식 식사권, 고급 스킨케어 세트, 건강검진 패키지 등"]))
B.append(bp([("특별한 기념 (15만원+): ",True),"가족 여행, 금반지, 프리미엄 가전 — 형제들과 함께 준비"]))
B.append(h3("2. 50~60대 여성의 건강·편안함이 최우선"))
B.append(p("네이버 블로그에서 시어머니 선물로 가장 많이 언급되는 키워드는 '발 건강'과 '편안함'입니다. 실질적인 필요를 채워주는 선물이 만족도가 높았습니다."))
B.append(bp([("발 건강: ",True),"워킹화, 기능성 실내화, 발 마사지기 — '시어머니 만족도 1위' 카테고리"]))
B.append(bp([("피부 관리: ",True),"고급 한방화장품(설화수·후), 에센스 세트 — 명절 선물로 인기"]))
B.append(bp([("편안한 휴식: ",True),"홈웨어·잠옷, 목 마사지기, 온열 찜질기 — 평소 선물로 좋음"]))
B.append(h3("3. '신경 쓴 흔적'이 비싼 선물보다 낫습니다"))
B.append(p("커뮤니티 후기를 보면, 시어머니는 비싼 선물보다 '며느리가 나를 생각해서 골랐구나'라는 느낌을 가장 감동적으로 받아들인다고 합니다. 비싼 쇼핑백보다 짧은 손편지 한 장이 더 오래 기억에 남습니다."))

B.append(h2("네이버 블로그·쇼핑에서 자주 언급된 선물 아이템"))
B.append(p("네이버 블로그와 쇼핑에서 '시어머니 선물'로 자주 언급되는 아이템들입니다. 가격은 일반적인 시중 판매가 기준입니다."))
B.append(h3("워킹화/기능성 신발 — 7~15만원대"))
B.append(p("네이버 블로그에서 시어머니 선물 만족도 1위. 나이가 들수록 발 건강이 중요해져서 워킹화 선물의 만족도가 매우 높습니다. 르무통·나르지오 등 가벼운 워킹화 브랜드가 자주 언급됩니다."))
B.append(h3("고급 한방화장품 세트 — 10~20만원대"))
B.append(p("명절·생신 선물의 전통적 1순위. 설화수 자음 2종 기획세트(약 15만원), 후(Who) 공진향 세트가 인기입니다. 취향을 모르겠다면 설화수가 가장 무난합니다."))
B.append(h3("홈웨어·잠옷 세트 — 3~6만원대"))
B.append(p("평소 선물로 부담 없이 드리기 좋습니다. 실크나 면 100% 소재가 인기고 색상은 차분한 계열이 무난합니다."))
B.append(h3("목·어깨 마사지기 — 4~8만원대"))
B.append(p("\"어깨가 아프다\"는 말씀을 자주 하시는 시어머니께 추천. 온열 기능이 있는 목 베개형이 실용적입니다."))
B.append(h3("건강기능식품 — 5~15만원대"))
B.append(p("홍삼(정관장), 종합비타민, 오메가3 순으로 인기. 단독 선물보다 식사권이나 다른 선물과 함께 준비하는 게 더 좋다는 의견이 많았습니다."))
B.append(h3("외식·카페 상품권 — 3~10만원"))
B.append(p("'경험 선물'의 가치가 높습니다. 호텔 뷔페, 한정식 식사권이 특히 인기. 며느리와의 외식 자체가 큰 선물이 된다는 후기가 많습니다."))

B.append(h2("예산별 추천"))
B.append(bp([("~5만원",True)," 홈웨어 세트, 목 마사지기, 건강기능식품"]))
B.append(bp([("5~10만원",True)," 워킹화, 스킨케어 세트, 외식 상품권"]))
B.append(bp([("10~20만원",True)," 설화수 기획세트, 건강검진, 한정식 식사권"]))
B.append(bp([("20만원+",True)," 가족 여행, 안마의자, 금반지 — 형제들과 분담"]))

B.append(h2("이런 선물은 피하는 게 좋습니다"))
B.append(bp([("향수·옷(사이즈·취향): ",True),"실패 확률이 높습니다. 특히 옷은 사이즈 맞아도 스타일이 안 맞으면 안 입게 됩니다."]))
B.append(bp([("주방용품·살림살이: ",True),"커뮤니티에서 '며느리가 나 보고 살림하라는 뜻?'으로 오해할 수 있다는 후기가 자주 나옵니다."]))
B.append(bp([("너무 고가의 선물: ",True),"오히려 며느리에게 '부담된다'는 말씀을 하시는 경우가 많습니다."]))

B.append(h2("생일·명절 메시지 예시"))
B.append(p("선물과 함께 짧은 메시지를 쓰면 감동이 두 배입니다."))
B.append(bp([("생신: ",True),"어머니, 생신 축하드려요. 평소에 need하실 것 같아서 준비했어요. 마음에 드시면 좋겠습니다."]))
B.append(bp([("명절: ",True),"어머니, 그동안 건강하셨어요? 추석 잘 보내세요. 작은 선물 준비했는데 편하게 사용하세요."]))
B.append(bp([("특별한 날: ",True),"어머니, 그동안 감사했습니다. 저희가 마음을 모아 준비했어요. 앞으로도 건강하세요!"]))

B.append(h2("마치며"))
B.append(p("여기 정리한 정보는 네이버 블로그·쇼핑과 82쿡·네이트판 커뮤니티에서 실제 며느리들이 공유한 후기와 경험을 바탕으로 했습니다. 개별 상품의 정확한 가격은 쿠팡·네이버쇼핑에서 직접 확인하세요."))
B.append(p("시어머니 선물, 가장 중요한 건 '생각하는 마음'입니다. 이 가이드가 고민에 조금이라도 도움이 되길 바랍니다."))

print(f"{len(B)} blocks")
r = requests.patch(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, json={"children": B})
print(f"{'OK' if r.status_code==200 else f'FAIL {r.status_code}'}")
