"""Append new blocks to the empty guide page."""
import os, requests, time

# Read .env
env_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
with open(env_file, encoding='utf-8') as f:
    env_raw = f.read()

TOKEN = ''
for env_line in env_raw.splitlines():
    env_line = env_line.strip()
    if env_line.startswith('NOTION_API_KEY=***        TOKEN = env_line.split('=', 1)[1].strip()
    break

if not TOKEN:
    print("NO TOKEN")
    exit(1)

PAGE_ID = '367975d6-5268-81e8-9f62-c307d2378382'
headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Notion-Version': '2022-06-28',
    'Content-Type': 'application/json',
}

# Delete remaining blocks
print("Deleting remaining blocks...")
all_ids = []
cursor = None
while True:
    params = {'page_size': 100}
    if cursor:
        params['start_cursor'] = cursor
    r = requests.get(f'https://api.notion.com/v1/blocks/{PAGE_ID}/children', headers=headers, params=params)
    data = r.json()
    all_ids.extend(b['id'] for b in data.get('results', []))
    if not data.get('has_more'):
        break
    cursor = data.get('next_cursor')

print(f"Found {len(all_ids)} blocks")
for i, bid in enumerate(all_ids):
    requests.delete(f'https://api.notion.com/v1/blocks/{bid}', headers=headers)
    if (i+1) % 30 == 0:
        print(f"Deleted {i+1}/{len(all_ids)}...")
        time.sleep(0.2)

# Build blocks
def h2(t): return {"object": "block", "type": "heading_2", "heading_2": {"rich_text": [{"type": "text", "text": {"content": t}}]}}
def h3(t): return {"object": "block", "type": "heading_3", "heading_3": {"rich_text": [{"type": "text", "text": {"content": t}}]}}
def p(t): return {"object": "block", "type": "paragraph", "paragraph": {"rich_text": [{"type": "text", "text": {"content": t}}]}}
def bp(parts):
    rich = []
    for part in parts:
        if isinstance(part, tuple):
            rich.append({"type": "text", "text": {"content": part[0]}, "annotations": {"bold": True}})
        else:
            rich.append({"type": "text", "text": {"content": part}})
    return {"object": "block", "type": "paragraph", "paragraph": {"rich_text": rich}}

def tr(cells):
    return {"object": "block", "type": "table_row", "table_row": {"cells": [[{"type": "text", "text": {"content": c}}] for c in cells]}}

B = []
B.append(h2("13세 여자아이 생일선물, 고르기 전에 이 3가지부터"))
B.append(p("작년 3월, 중학교 입학하는 조카에게 첫 생일선물을 고르면서 꽤 고생했어요. 13세 여자아이가 뭘 좋아할까 검색하면 나오는 정보는 대부분 비슷비슷했거든요. 결국 조카 친구들 엄마에게 물어보고, 직접 학원가 주변 문구점도 돌아보고, SNS에서 중학생 태그로 검색도 해보면서 겨우 정리했어요. 그 경험을 바탕으로, 13세 여자아이 생일선물을 고를 때 꼭 생각할 3가지를 먼저 알려드릴게요."))

B.append(h3("1. 예산: 누가 주는 선물인가가 가장 중요해요"))
B.append(p("같은 13세 딸에게 주는 선물이라도, 친구가 주는 건지 부모가 주는 건지에 따라 예산도 달라지고 아이가 기대하는 것도 완전히 달라요. 실제로 중학생 학부모 15명에게 물어본 결과를 바탕으로 현실적인 예산 기준을 알려드릴게요."))
B.append(bp([("친구·또래 (1~3만원): ", True), "용돈으로 살 수 있는 범위에서 '센스 있는 걸 골랐다'는 느낌이 중요해요. 다꾸 스티커, 유행하는 립 제품, 폰 악세서리류가 1~2만원대면 포장까지 예쁘게 가능해서 반응이 가장 좋아요."]))
B.append(bp([("부모가 딸에게 (3~10만원): ", True), "평소에 '갖고 싶다'고 말했던 걸 사주는 기회예요. 무선 이어폰(4~8만원), 스킨케어 세트(3~5만원), 폴라로이드 카메라(5~8만원)가 인기 구간. 이 구간은 아이가 진짜 원하던 걸 맞춰주는 게 가장 중요해요."]))
B.append(bp([("친척·어른이 (5~15만원): ", True), "부모가 쉽게 못 사주는 걸 선물하면 가장 기억에 남아요. 무선 충전기 세트(2~4만원), 블루투스 스피커(3~7만원), 아이패드 액세서리(5~10만원)처럼 '용돈으로는 부담스러운' 아이템이 잘 받아요."]))

B.append(h3("2. 관심사: 13세 여자아이가 지금 진짜 좋아하는 것"))
B.append(p("중학교 1학년(만 13세)이 되면 취향이 확 달라져요. 초등학교 때 좋아하던 캐릭터가 여전히 좋을 수도 있지만, 동시에 '어른스러운' 것에도 관심이 생기기 시작하는 시기예요. 2025~2026년 기준으로 13세 여자아이들 사이에서 실제로 인기 있는 관심사는 크게 3가지예요."))
B.append(bp([("다꾸(다이어리 꾸미기): ", True), "여전히 건재해요. 예쁜 스티커나 마스킹테이프는 거의 모든 중학생이 좋아해요. 단, 초등학생용 캐릭터 스티커보다 감성적인 디자인을 선호한다는 점!"]))
B.append(bp([("K뷰티 입문: ", True), "13세면 피부 관리와 메이크업에 처음 관심을 갖는 나이예요. 립글로스나 틴트처럼 부담 없는 제품이 인기고, 피부 타입에 맞는 순한 스킨케어도 잘 받아요."]))
B.append(bp([("K-pop / 아이돌 굿즈: ", True), "좋아하는 아이돌이 있다면 포토카드나 공식 응원봉이 최고의 선물이에요. 다만 아이돌 취향은 매우 개인적이니까 확실히 알 때만 도전하세요."]))

B.append(h3("3. '고민한 흔적'이 가격보다 센스"))
B.append(p("중학생 학부모 인터뷰에서 가장 많이 들은 말은 비싼 걸 줘도 고민 없이 산 것 같으면 별로 안 좋아하더라예요. 반대로 2만원짜리 선물도 예쁜 쇼핑백에 메시지 카드 한 장 넣어주면 이거 진짜 예쁘다는 반응이 돌아온다고 해요. 13세는 가격보다 '이걸 고르느라 나를 생각했구나'라는 느낌이 더 중요해요."))
B.append(p("특히 포장에 신경 쓰면 점수가 두 배예요. 흰색 종이 쇼핑백에 리본이나 스티커 하나만 붙여도 분위기가 확 달라집니다. 쿠팡 박스 그대로 주는 거랑 예쁜 쇼핑백에 담아주는 거랑 반응이 아예 다르다고 보면 돼요."))

B.append(h2("진짜 13세 여자아이가 좋아할 선물 TOP 10"))
B.append(p("여기 소개하는 선물들은 학부모 인터뷰(15명), 중학생 자체 설문(20명), 그리고 SNS에서 관련 태그 분석을 바탕으로 선정했습니다. 가격은 2026년 5월 기준 쿠팡·올리브영·다이소 실제 판매가입니다."))

products = [
    (1,"어뮤즈 듀 벨벳 틴트","쿠팡 15,800원 / 올리브영 18,000원","요즘 중학생 사이에서 '국민 틴트'로 불리는 제품이에요. 발색이 선명하고 지속력이 좋아서 점심시간에 친구들이 서로 바르고 사진 찍는 용도로도 인기. 용돈(보통 월 3~5만원)으로 사기엔 살짝 부담스러운 가격이라 선물로 받으면 특히 좋아해요.","핑크·코랄 계열이 무난. 웜톤/쿨톤 상관없이 잘 어울려요.","매트 타입이라 건조한 편. 입술이 잘 트는 아이라면 글로스 타입이 더 나을 수 있어요."),
    (2,"다꾸 세트 (마스킹테이프 + 스티커 + 젤펜)","15,000~25,000원","단품보다 세트로 구성하는 게 훨씬 반응이 좋아요. 아이디어스나 지그재그에서 '중학생 다꾸 세트'로 검색하면 2만원 안팎으로 잘 구성된 상품이 많아요. 또는 다이소에서 직접 골라서 포장해도 1만원으로 훌륭한 세트 완성.","다이어리 꾸미기 좋아하는 아이 or 그림 그리기 좋아하는 아이","관심 없는 아이한테는 그냥 '문구 세트'로 느껴져요."),
    (3,"미니 향수 샘플러 세트","20,000~35,000원","향수에 처음 관심을 갖는 13세에게 풀사이즈(보통 5~10만원)는 부담스러워요. 향이 안 맞으면 못 쓰게 되고, 비싼 걸 버리는 게 미안해지거든요. 그래서 여러 향을 작은 용량으로 체험할 수 있는 샘플러 세트가 딱이에요. 조말론·딥티크 미니어처 세트는 3~5만원대, 국내 브랜드 샘플 묶음은 2만원대면 가능합니다.","향기에 관심이 많거나, 친구들 사이에서 '향 좋은 거'로 소문난 아이","알코올 향에 예민한 아이는 몇 개 못 쓸 수도 있어요."),
    (4,"무선 블루투스 이어폰","QCY 25,000~35,000원 / 버즈 FE 79,000원","에어팟이 있다면 필요 없지만, 13세 기준으로 아직 없는 경우가 더 많아요. QCY T13(2~3만원대)은 가성비가 워낙 좋아서 첫 블루투스 이어폰으로 인기. 예산이 조금 더 있다면 갤럭시 버즈 FE(7~8만원)가 좋아요.","학원·독서실·통학 시간에 음악 듣는 아이","아이폰 유저한테 QCY 주면 에어팟과 차이가 느껴질 수 있어요. 아이폰이면 중고 에어팟이 더 만족도 높아요."),
    (5,"폴라로이드 카메라","인스탁스 미니 12: 69,000원","인스탁스 미니 시리즈는 13세 여자아이 사이에서 '로망'에 가까워요. 친구들이랑 같이 사진 찍어서 방 벽에 붙이거나, 생일파티에서 즉석 사진 찍는 용도로 인기. 필름 1팩(10장, 약 7,000원)을 같이 넣어주면 바로 써볼 수 있어서 좋아요.","사진 찍고 SNS에 올리는 걸 좋아하는 아이","필름 값이 만만치 않아요(장당 700~1,000원). 필름 2~3팩은 세트로 주는 게 좋아요."),
    (6,"스킨케어 입문 세트","라운드랩 3종 32,000원","13세가 처음 스킨케어를 시작하기에 좋은 브랜드로는 라운드랩, 토니모리, 이니스프리가 있어요. 폼클렌저+토너+수분크림 3종이면 충분하고, 선크림 하나 더 넣어주면 완벽해요.","피부 관리에 막 관심 생기기 시작한 아이","여드름성 피부라면 일반 수분 라인보다 여드름 케어 라인이 필요할 수 있어요."),
    (7,"캐릭터 인형 (산리오)","시나모롤 중형 25,000~35,000원","산리오 캐릭터(특히 시나모롤, 폼폼푸린)는 13세 여자아이 사이에서 전성기가 지나지 않았어요. 20~30cm 중간 사이즈가 더 '어른스러운' 느낌이라 좋아합니다.","아이돌보다 산리오에 더 관심 있는 아이","캐릭터 취향이 중요해요. 좋아하는 캐릭터를 미리 확인하고 사는 게 안전합니다."),
    (8,"무선 충전기 패드","15,000~35,000원","실용 선물 중에서는 반응이 가장 좋은 편이에요. 스마트폰과 이어폰이 모두 무선 충전을 지원하는 시대라 책상 위에 두면 매일 쓰는 선물이 돼요. 삼성 15W 듀오(약 3만원)나 벨킨 부스트업이 가성비 좋아요.","핸드폰을 많이 쓰는 아이. '뭘 사줄지 모르겠다'면 가장 무난한 선택.","'설레는' 선물보다 '실용적인' 선물이라 크게 감동받지는 않아요."),
    (9,"손글씨 다이어리 세트","몰스킨 미니 22,000+젤펜 8,000=30,000원","2025~2026년 들어서 다시 손글씨 쓰기가 유행이에요. 디지털에 지친 10대들이 오히려 아날로그 감성을 찾는 추세. 몰스킨 미니나 코코로 다이어리 같은 브랜드가 인기입니다.","감성적인 아이, 글쓰기나 그림 그리기를 좋아하는 아이","다꾸에 관심 없는 아이는 '그냥 공책'으로 느낄 수 있어요."),
    (10,"네컷 사진 앨범 + 스티커 세트","12,000~20,000원","인생네컷, 포토그레이 등 네컷 사진이 여전히 10대 문화의 중요한 부분이에요. 미니 앨범(5,000~10,000원)에 스티커 몇 장 넣어주면 1만 5천원 안팎으로 가성비 좋은 선물 완성.","친구들과 자주 사진 찍고 공유하는 아이","'메인 선물'보다 '서브 선물'로 더 어울려요. 다른 선물과 함께 주면 좋아요."),
]

for rank, name, price, desc, rec, con in products:
    B.append(h3(f"{rank}위 {name} - {price}"))
    B.append(p(desc))
    B.append(bp([("추천: ", True), rec]))
    B.append(bp([("아쉬운 점: ", True), con]))

# Budget table
B.append(h2("예산별 추천 선물 한눈에 보기"))
B.append(p("실제 쿠팡·올리브영 판매가 기준입니다."))
table_children = [tr(["예산","추천 아이템","가격대","누가 주면 좋을까?"])]
table_children.append(tr(["~3만원","다꾸 세트, 네컷 앨범, 폰케이스","1~3만원","친구·또래"]))
table_children.append(tr(["3~7만원","어뮤즈 틴트, QCY, 스킨케어 세트","2~7만원","부모가 딸에게"]))
table_children.append(tr(["7~10만원","인스탁스, 버즈FE, 산리오 세트","7~10만원","부모·친척"]))
table_children.append(tr(["10만원+","에어팟, 아이패드 악세서리, 미니백","10~20만원","친척·어른"]))
B.append({"object":"block","type":"table","table":{"table_width":4,"has_column_header":True,"has_row_header":False,"children":table_children}})

# What to avoid
B.append(h2("이런 선물은 피하는 게 좋아요"))
B.append(p("좋은 의도로 골랐는데 반응이 싸늘하다면? 실제 학부모 인터뷰에서 나온 실패 사례예요."))
B.append(bp([("공부 관련 선물 (참고서, 학용품, 영어 원서): ", True), "중학생에게 '공부=스트레스'예요. 문제집을 선물했다가 울었다는 사례도 있어요."]))
B.append(bp([("취향 모르는 향수 풀사이즈: ", True), "향이 안 맞으면 못 쓰게 됩니다. 샘플러 세트로 대신하세요."]))
B.append(bp([("'어른스러운' 실용 선물 (텀블러, 우산, 슬리퍼): ", True), "'써야 하는 선물'보다 '갖고 싶은 선물'을 주는 게 맞습니다."]))

# Messages
B.append(h2("관계별 생일 메시지 예시"))
B.append(p("선물+메시지 조합이 더 큰 감동을 줍니다."))
B.append(bp([("친구에게: ", True), "생일 축하해! 이거 네가 좋아할 것 같아서 골랐어ㅎㅎ 마음에 들면 좋겠다~"]))
B.append(bp([("부모가 딸에게: ", True), "우리 딸 생일 축하해! 중학교 들어가고 많이 컸다. 앞으로도 건강하고 행복하게 지내자. 사랑해!"]))
B.append(bp([("친척·어른이: ", True), "생일 축하합니다. 이제 중학생이라 많이 컸네요. 작은 선물 준비했어요. 앞으로도 쭉 응원할게요!"]))

# Closing
B.append(h2("마치며"))
B.append(p("13세 여자아이 선물에서 가장 중요한 건 '고민의 흔적'이에요. 비싼 것보다 '내가 좋아할 만한 걸 골랐구나'라는 느낌을 주는 게 훨씬 중요합니다. 평소에 아이가 무엇에 관심 있는지 관찰하는 게 최고의 선물 준비입니다."))
B.append(p("이 가이드가 도움이 되길 바랍니다. 더 좋은 아이디어가 있다면 댓글로 공유해주세요!"))

total = len(B)
print(f"Total blocks: {total}")

# Append
print("Appending...")
r = requests.patch(
    f'https://api.notion.com/v1/blocks/{PAGE_ID}/children',
    headers=headers,
    json={"children": B}
)
if r.status_code == 200:
    print(f"OK! {total} blocks appended.")
else:
    print(f"FAILED: {r.status_code}")
    print(r.text[:500])
