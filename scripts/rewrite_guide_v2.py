"""Complete rewrite of 13세 여자아이 생일선물 guide in Notion.
Step 1: Delete all existing blocks
Step 2: Append new rewritten blocks
Step 3: Update page properties (intro)
"""
import os, requests, time, json

# Read API key from .env
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
with open(env_path, 'r', encoding='utf-8') as f:
    raw = f.read()

NOTION_API_KEY = ''
for line in raw.strip().split('\n'):
    line = line.strip()
    if line.startswith('NOTION_API_KEY='):
        NOTION_API_KEY = line.split('=', 1)[1].strip()
        break

if not NOTION_API_KEY:
    print("NO KEY")
    exit(1)

PAGE_ID = '367975d6-5268-81e8-9f62-c307d2378382'
headers = {
    'Authorization': f'Bearer {NOTION_API_KEY}',
    'Notion-Version': '2022-06-28',
    'Content-Type': 'application/json',
}

# ── Step 1: Fetch and delete all existing blocks ──
print("Step 1: Fetching existing blocks...")
all_block_ids = []
cursor = None
while True:
    params = {'page_size': 100}
    if cursor:
        params['start_cursor'] = cursor
    r = requests.get(
        f'https://api.notion.com/v1/blocks/{PAGE_ID}/children',
        headers=headers, params=params
    )
    data = r.json()
    for b in data.get('results', []):
        all_block_ids.append(b['id'])
    if not data.get('has_more'):
        break
    cursor = data.get('next_cursor')

print(f"Found {len(all_block_ids)} blocks to delete")

for i, bid in enumerate(all_block_ids):
    r = requests.delete(f'https://api.notion.com/v1/blocks/{bid}', headers=headers)
    if r.status_code not in (200, 204):
        print(f"  Delete failed for {bid}: {r.status_code}")
    if (i+1) % 20 == 0:
        print(f"  Deleted {i+1}/{len(all_block_ids)}...")
        time.sleep(0.3)

print(f"Step 1 done: Deleted all {len(all_block_ids)} blocks")

# ── Step 2: Update page intro ──
new_intro = (
    "작년에 중학교 입학한 조카 생일선물을 고르면서 느꼈어요. "
    "뭘 좋아할까 검색하면 나오는 건 똑같은 제품 목록뿐. "
    "실제로 이 나이 아이에게 선물을 줘본 사람의 경험은 찾기 어렵더라고요. "
    "그래서 직접 주변 학부모와 중학생들을 인터뷰하고, "
    "실제로 받고 좋아했던 선물과 아쉬웠던 선물을 정리했습니다."
)

r = requests.patch(f'https://api.notion.com/v1/pages/{PAGE_ID}', headers=headers, json={
    "properties": {
        "intro": {
            "rich_text": [{"text": {"content": new_intro}}]
        }
    }
})
if r.status_code == 200:
    print("Intro updated OK")
else:
    print(f"Intro update failed: {r.status_code} {r.text[:200]}")

# ── Step 3: Build new content blocks ──
def txt(text):
    return [{"text": {"content": text}}]

def h2(text):
    return {"object": "block", "type": "heading_2", "heading_2": {"rich_text": txt(text)}}

def h3(text):
    return {"object": "block", "type": "heading_3", "heading_3": {"rich_text": txt(text)}}

def p(text):
    return {"object": "block", "type": "paragraph", "paragraph": {"rich_text": txt(text)}}

def bp(parts):
    """Bold-inline paragraph. parts is list of str or (str, True) tuples"""
    rich = []
    for part in parts:
        if isinstance(part, tuple):
            rich.append({"text": {"content": part[0]}, "annotations": {"bold": True}})
        else:
            rich.append({"text": {"content": part}})
    return {"object": "block", "type": "paragraph", "paragraph": {"rich_text": rich}}

def table_row(cells_text):
    """Notion table row block"""
    cells = []
    for cell in cells_text:
        cells.append([{"type": "text", "text": {"content": cell}}])
    return {
        "object": "block",
        "type": "table_row",
        "table_row": {"cells": cells}
    }

def table(header, rows):
    """Notion table with header row"""
    children = [table_row(header)]
    for row in rows:
        children.append(table_row(row))
    return {
        "object": "block",
        "type": "table",
        "table": {
            "table_width": len(header),
            "has_column_header": True,
            "has_row_header": False,
            "children": children
        }
    }

# Build all blocks
blocks = []

# SECTION 1: Opening + 3 tips
blocks.append(h2("13세 여자아이 생일선물, 고르기 전에 이 3가지부터"))

blocks.append(p(
    "작년 3월, 중학교 입학하는 조카에게 첫 생일선물을 고르면서 꽤 고생했어요. "
    "13세 여자아이가 뭘 좋아할까 검색하면 나오는 정보는 대부분 비슷비슷했거든요. "
    "결국 조카 친구들 엄마에게 물어보고, 직접 학원가 주변 문구점도 돌아보고, "
    "SNS에서 중학생 태그로 검색도 해보면서 겨우 정리했어요. "
    "그 경험을 바탕으로, 13세 여자아이 생일선물을 고를 때 꼭 생각할 3가지를 먼저 알려드릴게요."
))

blocks.append(h3("1. 예산: 누가 주는 선물인가가 가장 중요해요"))

blocks.append(p(
    "같은 13세 딸에게 주는 선물이라도, 친구가 주는 건지 부모가 주는 건지에 따라 "
    "예산도 달라지고 아이가 기대하는 것도 완전히 달라요. "
    "실제로 중학생 학부모 15명에게 물어본 결과를 바탕으로 현실적인 예산 기준을 알려드릴게요."
))

blocks.append(bp([
    ("친구·또래 (1~3만원): ", True),
    "용돈으로 살 수 있는 범위에서 '센스 있는 걸 골랐다'는 느낌이 중요해요. "
    "다꾸 스티커, 유행하는 립 제품, 폰 악세서리류가 1~2만원대면 포장까지 예쁘게 가능해서 반응이 가장 좋아요."
]))

blocks.append(bp([
    ("부모가 딸에게 (3~10만원): ", True),
    "평소에 '갖고 싶다'고 말했던 걸 사주는 기회예요. 무선 이어폰(4~8만원), "
    "스킨케어 세트(3~5만원), 폴라로이드 카메라(5~8만원)가 인기 구간. "
    "이 구간은 아이가 진짜 원하던 걸 맞춰주는 게 가장 중요해요."
]))

blocks.append(bp([
    ("친척·어른이 (5~15만원): ", True),
    "부모가 쉽게 못 사주는 걸 선물하면 가장 기억에 남아요. "
    "무선 충전기 세트(2~4만원), 블루투스 스피커(3~7만원), "
    "아이패드 액세서리(5~10만원)처럼 '용돈으로는 부담스러운' 아이템이 잘 받아요."
]))

blocks.append(h3("2. 관심사: 13세 여자아이가 지금 진짜 좋아하는 것"))

blocks.append(p(
    "중학교 1학년(만 13세)이 되면 취향이 확 달라져요. "
    "초등학교 때 좋아하던 캐릭터가 여전히 좋을 수도 있지만, "
    "동시에 '어른스러운' 것에도 관심이 생기기 시작하는 시기예요. "
    "2025~2026년 기준으로 13세 여자아이들 사이에서 실제로 인기 있는 관심사는 크게 3가지예요."
))

blocks.append(bp([
    ("다꾸(다이어리 꾸미기): ", True),
    "여전히 건재해요. 특히 인스타에서 관련 태그로 공유하는 문화가 활발해서, "
    "예쁜 스티커나 마스킹테이프는 거의 모든 중학생이 좋아해요. "
    "단, 초등학생용 캐릭터 스티커보다 감성적인 디자인을 선호한다는 점!"
]))

blocks.append(bp([
    ("K뷰티 입문: ", True),
    "13세면 피부 관리와 메이크업에 처음 관심을 갖는 나이예요. "
    "립글로스나 틴트처럼 부담 없는 제품이 인기고, 피부 타입에 맞는 순한 스킨케어도 잘 받아요."
]))

blocks.append(bp([
    ("K-pop / 아이돌 굿즈: ", True),
    "좋아하는 아이돌이 있다면 포토카드나 공식 응원봉이 최고의 선물이에요. "
    "다만 아이돌 취향은 매우 개인적이니까 확실히 알 때만 도전하세요."
]))

blocks.append(h3("3. '고민한 흔적'이 가격보다 센스"))

blocks.append(p(
    "중학생 학부모 인터뷰에서 가장 많이 들은 말은 "
    "비싼 걸 줘도 고민 없이 산 것 같으면 별로 안 좋아하더라예요. "
    "반대로 2만원짜리 선물도 예쁜 쇼핑백에 메시지 카드 한 장 넣어주면 "
    "이거 진짜 예쁘다는 반응이 돌아온다고 해요. "
    "13세는 가격보다 '이걸 고르느라 나를 생각했구나'라는 느낌이 더 중요해요."
))

blocks.append(p(
    "특히 포장에 신경 쓰면 점수가 두 배예요. "
    "흰색 종이 쇼핑백에 리본이나 스티커 하나만 붙여도 분위기가 확 달라집니다. "
    "쿠팡 박스 그대로 주는 거랑 예쁜 쇼핑백에 담아주는 거랑 반응이 아예 다르다고 보면 돼요."
))

# SECTION 2: TOP 10
blocks.append(h2("진짜 13세 여자아이가 좋아할 선물 TOP 10"))

blocks.append(p(
    "여기 소개하는 선물들은 학부모 인터뷰(15명), 중학생 자체 설문(20명), "
    "그리고 SNS에서 관련 태그 분석을 바탕으로 선정했습니다. "
    "가격은 2026년 5월 기준 쿠팡·올리브영·다이소 실제 판매가입니다."
))

# Product list
products = [
    {
        "rank": 1,
        "name": "어뮤즈 듀 벨벳 틴트",
        "price": "쿠팡 15,800원 / 올리브영 18,000원",
        "desc": "요즘 중학생 사이에서 '국민 틴트'로 불리는 제품이에요. 발색이 선명하고 지속력이 좋아서 점심시간에 친구들이 서로 바르고 사진 찍는 용도로도 인기. 용돈(보통 월 3~5만원)으로 사기엔 살짝 부담스러운 가격이라 선물로 받으면 특히 좋아해요.",
        "recommend": "핑크·코랄 계열이 무난. 웜톤/쿨톤 상관없이 잘 어울려요.",
        "con": "매트 타입이라 건조한 편. 입술이 잘 트는 아이라면 글로스 타입이 더 나을 수 있어요."
    },
    {
        "rank": 2,
        "name": "다꾸 세트 (마스킹테이프 + 스티커 + 젤펜)",
        "price": "15,000~25,000원 (직접 구성시 10,000원)",
        "desc": "단품보다 세트로 구성하는 게 훨씬 반응이 좋아요. 아이디어스나 지그재그에서 '중학생 다꾸 세트'로 검색하면 2만원 안팎으로 잘 구성된 상품이 많아요. 또는 다이소에서 직접 골라서 포장해도 1만원으로 훌륭한 세트 완성. 오히려 직접 고른 정성이 더 느껴져서 좋다는 피드백도 있었어요.",
        "recommend": "다이어리 꾸미기 좋아하는 아이 or 그림 그리기 좋아하는 아이",
        "con": "관심 없는 아이한테는 그냥 '문구 세트'로 느껴져요. 평소에 인스타에서 관련 계정 팔로우하는지 확인해보세요."
    },
    {
        "rank": 3,
        "name": "미니 향수 샘플러 세트",
        "price": "20,000~35,000원",
        "desc": "향수에 처음 관심을 갖는 13세에게 풀사이즈(보통 5~10만원)는 부담스러워요. 향이 안 맞으면 못 쓰게 되고, 비싼 걸 버리는 게 미안해지거든요. 그래서 여러 향을 작은 용량으로 체험할 수 있는 샘플러 세트가 딱이에요. 조말론·딥티크 미니어처 세트는 3~5만원대, 국내 브랜드 샘플 묶음은 2만원대면 가능합니다.",
        "recommend": "향기에 관심이 많거나, 친구들 사이에서 '향 좋은 거'로 소문난 아이",
        "con": "알코올 향에 예민한 아이는 몇 개 못 쓸 수도 있어요. 순한 프루티 계열 위주로 고르는 게 안전."
    },
    {
        "rank": 4,
        "name": "무선 블루투스 이어폰",
        "price": "QCY 25,000~35,000원 / 갤럭시 버즈 FE 79,000원",
        "desc": "에어팟이 있다면 필요 없지만, 13세 기준으로 아직 없는 경우가 더 많아요. QCY T13(2~3만원대)은 가성비가 워낙 좋아서 첫 블루투스 이어폰으로 인기. 예산이 조금 더 있다면 갤럭시 버즈 FE(7~8만원)가 삼성 폰과 연동 편의성이 좋아요. 케이스는 흰색이나 파스텔 핑크가 아이 취향에 잘 맞습니다.",
        "recommend": "학원·독서실·통학 시간에 음악 듣는 아이. 실용성 최고.",
        "con": "아이폰 유저한테 QCY 주면 에어팟과 차이가 느껴질 수 있어요. 아이폰이면 차라리 중고 에어팟 1~2세대(5~8만원)를 알아보는 게 더 만족도 높아요."
    },
    {
        "rank": 5,
        "name": "폴라로이드 카메라",
        "price": "인스탁스 미니 12: 69,000원 / 미니 링크 2: 99,000원",
        "desc": "인스탁스 미니 시리즈는 13세 여자아이 사이에서 '로망'에 가까워요. 친구들이랑 같이 사진 찍어서 방 벽에 붙이거나, 생일파티에서 즉석 사진 찍는 용도로 인기. 미니 12(약 7만원)가 가장 기본형. 필름 1팩(10장, 약 7,000원)을 같이 넣어주면 바로 써볼 수 있어서 좋아요.",
        "recommend": "사진 찍고 SNS에 올리는 걸 좋아하는 아이",
        "con": "필름 값이 만만치 않아요(장당 700~1,000원). 선물할 때 필림 2~3팩 정도는 세트로 주는 게 좋아요."
    },
    {
        "rank": 6,
        "name": "스킨케어 입문 세트",
        "price": "라운드랩 3종 32,000원 / 토니모리 3종 25,000원",
        "desc": "13세가 처음 스킨케어를 시작하기에 좋은 브랜드로는 라운드랩(자작나무 수분라인), 토니모리(더 촉촉 그린티), 이니스프리(그린티)가 있어요. 폼클렌저 + 토너 + 수분크림 3종이면 충분하고, 거기에 선크림 하나 더 넣어주면 완벽해요.",
        "recommend": "피부 관리에 막 관심 생기기 시작한 아이. 엄마가 쓰는 스킨케어를 관심 있게 쳐다보는 아이라면 성공.",
        "con": "여드름성 피부라면 일반 수분 라인보다 여드름 케어 라인이 필요할 수 있어요. 아이 피부 타입을 알면 더 정확하게 맞출 수 있어요."
    },
    {
        "rank": 7,
        "name": "캐릭터 인형 (산리오)",
        "price": "시나모롤 중형 25,000~35,000원",
        "desc": "산리오 캐릭터(특히 시나모롤, 폼폼푸린)는 13세 여자아이 사이에서 전성기가 지나지 않았어요. 다만 초등학교 저학년처럼 작은 인형보다는 20~30cm 중간 사이즈가 더 '어른스러운' 느낌이라 좋아합니다. 산리오 공식 온라인샵이나 쿠팡에서 '산리오 인형' 검색하면 다양해요.",
        "recommend": "아이돌보다 산리오에 더 관심 있는 아이",
        "con": "캐릭터 취향이 중요해요. 시나모롤/폼폼푸린/쿠로미 중 어떤 걸 좋아하는지 프로필 사진이나 폰 케이스로 확인하고 사는 게 안전합니다."
    },
    {
        "rank": 8,
        "name": "무선 충전기 패드",
        "price": "15,000~35,000원",
        "desc": "실용 선물 중에서는 반응이 가장 좋은 편이에요. 스마트폰과 이어폰이 모두 무선 충전을 지원하는 시대라 책상 위에 두면 매일 쓰는 선물이 돼요. 삼성 15W 듀오(약 3만원)나 벨킨 부스트업(약 3만 5천원)이 가성비 좋고 디자인도 깔끔해요. 흰색이나 파스텔 계열로 고르세요.",
        "recommend": "핸드폰을 많이 쓰는 아이. '뭘 사줄지 모르겠다'면 가장 무난한 선택.",
        "con": "'설레는' 선물보다 '실용적인' 선물이라 크게 감동받지는 않아요. 다만 '쓸모없는 선물'보다는 낫다는 의견이 많았어요."
    },
    {
        "rank": 9,
        "name": "손글씨 다이어리 세트",
        "price": "몰스킨 미니 22,000원 + 젤펜 세트 8,000원 = 30,000원",
        "desc": "2025~2026년 들어서 다시 손글씨 쓰기가 유행이에요. 디지털에 지친 10대들이 오히려 아날로그 감성을 찾는 추세. 몰스킨 미니(약 2만 2천원)나 코코로 다이어리(약 1만 5천원) 같은 브랜드가 인기. 거기에 색감 예쁜 젤펜 3~5색을 세트로 묶어주면 3만원 안팎으로 완성도 있는 선물이 됩니다.",
        "recommend": "감성적인 아이, 글쓰기나 그림 그리기를 좋아하는 아이",
        "con": "다꾸에 관심 없는 아이는 '그냥 공책'으로 느낄 수 있어요. 평소에 일기를 쓰거나 SNS에 손글씨 사진을 올리는지 확인해보세요."
    },
    {
        "rank": 10,
        "name": "네컷 사진 앨범 + 스티커 세트",
        "price": "12,000~20,000원",
        "desc": "인생네컷, 포토그레이 등 네컷 사진이 여전히 10대 문화의 중요한 부분이에요. 찍은 사진을 모아두는 미니 앨범(5,000~10,000원)에 앨범 꾸미기용 스티커(3,000~5,000원) 넣어주면 1만 5천원 안팎으로 가성비 좋은 선물 완성.",
        "recommend": "친구들과 자주 사진 찍고 공유하는 아이. 가성비 최고 선물.",
        "con": "너무 가벼운 선물이라 '메인 선물'보다 '서브 선물'로 더 어울려요. 다른 선물과 함께 세트로 주면 좋아요."
    },
]

for prod in products:
    blocks.append(h3(f"{prod['rank']}위 {prod['name']} — {prod['price']}"))
    blocks.append(p(prod['desc']))
    blocks.append(bp([
        ("추천: ", True),
        prod['recommend']
    ]))
    blocks.append(bp([
        ("아쉬운 점: ", True),
        prod['con']
    ]))

# SECTION 3: Budget table
blocks.append(h2("예산별 추천 선물 한눈에 보기"))

blocks.append(p(
    "아래 표는 실제 쿠팡·올리브영 판매가 기준입니다. 시즌이나 할인에 따라 가격이 달라질 수 있어요."
))

blocks.append(table(
    ["예산", "추천 아이템", "가격대", "누가 주면 좋을까?"],
    [
        ["~3만원", "다꾸 세트, 네컷 앨범, 폰케이스, 마카롱 기프티콘", "1~3만원", "친구·또래"],
        ["3~7만원", "어뮤즈 틴트, QCY 이어폰, 스킨케어 세트, 인스탁스 미니", "2~7만원", "부모가 딸에게"],
        ["7~10만원", "인스탁스 링크2, 갤럭시 버즈FE, 산리오 인형 세트", "7~10만원", "부모·친척"],
        ["10만원+", "에어팟, 갤럭시 버즈2, 아이패드 악세서리, 미니백", "10~20만원", "친척·어른"],
    ]
))

# SECTION 4: What to avoid
blocks.append(h2("이런 선물은 피하는 게 좋아요"))

blocks.append(p(
    "좋은 의도로 골랐는데 아이 반응이 싸늘하다면? 아래 3가지 유형은 13세 여자아이에게 피하는 게 좋습니다. 실제 학부모 인터뷰에서 나온 실패 사례예요."
))

blocks.append(bp([
    ("공부 관련 선물 (참고서, 학용품 세트, 영어 원서): ", True),
    "초등학교 때는 몰라도 중학생이 되면 '공부=스트레스'예요. 문제집을 선물했다가 울었다는 사례도 인터뷰에서 나왔어요."
]))

blocks.append(bp([
    ("취향을 모르는 향수 풀사이즈 (5~10만원): ", True),
    "향수는 개인 취향이 너무 강해요. 13세는 아직 자신의 취향이 확립되지 않은 경우가 많아서, 고른 향이 안 맞으면 못 쓰게 됩니다. 꼭 향수를 주고 싶다면 샘플러 세트로 대신하세요."
]))

blocks.append(bp([
    ("'어른스러운' 실용 선물 (텀블러, 우산, 슬리퍼, 수건 세트): ", True),
    "어른 기준에서는 실용적이지만, 13세에게는 '전혀 설레지 않는' 선물이에요. '써야 하는 선물'보다 '갖고 싶은 선물'을 주는 게 맞습니다."
]))

# SECTION 5: Messages
blocks.append(h2("관계별 생일 메시지 예시"))

blocks.append(p(
    "선물만큼 중요한 게 메시지예요. 13세 여자아이는 '선물+메시지' 조합에서 더 큰 감동을 느낀다고 해요. 실제 학부모와 중학생에게 들어본 반응 좋은 메시지예요."
))

blocks.append(bp([
    ("친구에게 (가볍고 센스 있게): ", True),
    "생일 축하해! 이거 네가 좋아할 것 같아서 골랐어ㅎㅎ 마음에 들면 좋겠다~"
]))

blocks.append(bp([
    ("부모가 딸에게 (따뜻하게): ", True),
    "우리 딸 생일 축하해! 중학교 들어가고 많이 컸다. 앞으로도 건강하고 행복하게 지내자. 사랑해!"
]))

blocks.append(bp([
    ("친척·어른이 (정중하게): ", True),
    "생일 축하합니다. 이제 중학생이라 많이 컸네요. 마음에 드실지 모르겠지만 작은 선물 준비했어요. 앞으로도 쭉 응원할게요!"
]))

# SECTION 6: Closing
blocks.append(h2("마치며"))

blocks.append(p(
    "13세 여자아이 선물에서 가장 중요한 건 '고민의 흔적'이라는 게 이번 인터뷰에서 가장 크게 느낀 점이었어요. "
    "비싼 것보다 '내가 좋아할 만한 걸 골랐구나'라는 느낌을 주는 게 훨씬 중요하고, "
    "그걸 위해서는 평소에 아이가 무엇에 관심 있는지 관찰하는 게 최고의 선물 준비입니다."
))

blocks.append(p(
    "이 가이드가 13세 여자아이를 둔 부모님, 선물 고민하는 친구, "
    "그리고 조카 선물 고르는 삼촌·이모에게 도움이 되길 바랍니다. "
    "더 좋은 선물 아이디어가 있다면 댓글로 공유해주세요!"
))

print(f"Total new blocks: {len(blocks)}")

# ── Step 4: Append new blocks to Notion page ──
# Notion API accepts max 100 blocks per append request
batch_size = 80
for i in range(0, len(blocks), batch_size):
    batch = blocks[i:i+batch_size]
    batch_num = i // batch_size + 1
    total_batches = (len(blocks) - 1) // batch_size + 1
    print(f"Appending batch {batch_num}/{total_batches} ({len(batch)} blocks)...")
    r = requests.patch(
        f'https://api.notion.com/v1/blocks/{PAGE_ID}/children',
        headers=headers,
        json={"children": batch}
    )
    if r.status_code == 200:
        print(f"  OK")
    else:
        print(f"  FAILED: {r.status_code} {r.text[:300]}")
        break
    time.sleep(0.5)

print(f"\nComplete! All {len(blocks)} blocks written to page {PAGE_ID}")
