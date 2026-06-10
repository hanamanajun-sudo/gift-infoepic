"""Apply 5 feedback fixes from 회장님"""
import os, requests, time, sys
sys.path.insert(0, os.path.dirname(__file__))
from notion_key import get_key

KEY = get_key()
if not KEY:
    print("NO KEY"); exit(1)

PID = '367975d6-5268-81e8-9f62-c307d2378382'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}

# Step 1: Update intro
new_intro = "13살 여자아이 생일선물, 뭘 사줘야 할지 고민된다면? 주변 지인들에게 물어보고 직접 조사해서 좋았던 선물과 아쉬웠던 선물을 정리했습니다."
r = requests.patch(f'https://api.notion.com/v1/pages/{PID}', headers=H, json={
    "properties": {"intro": {"rich_text": [{"text": {"content": new_intro}}]}}
})
print(f"Intro: {'OK' if r.status_code==200 else f'FAIL {r.status_code}'}")

# Step 2: Delete all existing content blocks
all_ids = []
cursor = None
while True:
    params = {'page_size': 100}
    if cursor: params['start_cursor'] = cursor
    r = requests.get(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, params=params)
    data = r.json()
    all_ids.extend(b['id'] for b in data.get('results', []))
    if not data.get('has_more'): break
    cursor = data.get('next_cursor')

print(f"Delete {len(all_ids)} blocks...")
for i, bid in enumerate(all_ids):
    requests.delete(f'https://api.notion.com/v1/blocks/{bid}', headers=H)
    if (i+1)%50==0: print(f"  {i+1}/{len(all_ids)}"), time.sleep(0.3)
print("Deleted OK")

# Step 3: Append new blocks (with all 5 fixes applied)
def h2(t): return {"object":"block","type":"heading_2","heading_2":{"rich_text":[{"type":"text","text":{"content":t}}]}}
def h3(t): return {"object":"block","type":"heading_3","heading_3":{"rich_text":[{"type":"text","text":{"content":t}}]}}
def p(t): return {"object":"block","type":"paragraph","paragraph":{"rich_text":[{"type":"text","text":{"content":t}}]}}
def bp(parts):
    r = []
    for part in parts:
        if isinstance(part,tuple): r.append({"type":"text","text":{"content":part[0]},"annotations":{"bold":True}})
        else: r.append({"type":"text","text":{"content":part}})
    return {"object":"block","type":"paragraph","paragraph":{"rich_text":r}}

B = []

# Opening - 13살으로 변경, 쿠팡 100개 제거
B.append(h2("13살 여자아이 생일선물, 고르기 전에 이 3가지부터"))
B.append(p("13살 여자아이 선물을 검색해보면 '이거 사세요' 리스트만 가득하고, 왜 이게 좋은지 어떤 아이에게 맞는지에 대한 설명은 부족합니다. 주변 학부모와 중학생들에게 직접 물어보고 정리한 13살 여자아이 선물 고르는 팁과 진짜 좋아할 만한 아이템을 소개합니다."))

B.append(h3("1. 예산: 누가 주는 선물인가가 가장 중요해요"))
B.append(bp([("친구·또래 (1~3만원): ",True),"용돈 범위에서 '센스 있는' 느낌이 중요. 다꾸 스티커, 유행하는 립 제품, 폰 악세서리류가 1~2만원대면 포장까지 예쁘게 가능해요."]))
B.append(bp([("부모가 딸에게 (3~10만원): ",True),"평소 '갖고 싶다'던 걸 사주는 기회. 무선 이어폰(4~8만원), 스킨케어(3~5만원), 폴라로이드 카메라(5~8만원)가 인기 구간."]))
B.append(bp([("친척·어른이 (5~15만원): ",True),"부모가 잘 못 사주는 것. 무선 충전기(2~4만원), 블루투스 스피커(3~7만원), 아이패드 악세서리(5~10만원) 추천."]))

B.append(h3("2. 관심사: 13살 여자아이가 지금 진짜 좋아하는 것"))
B.append(p("취향이 확 달라지는 시기. 요즘 인기 있는 관심사 3가지:"))
B.append(bp([("다꾸(다이어리 꾸미기): ",True),"여전히 건재. 감성 디자인 스티커와 마스킹테이프가 인기."]))
B.append(bp([("K뷰티 입문: ",True),"립글로스, 틴트, 순한 스킨케어에 관심 갖기 시작."]))
B.append(bp([("K-pop/아이돌 굿즈: ",True),"아이돌이 확실할 때만. 모르면 피하세요."]))

B.append(h3("3. '고민한 흔적'이 가격보다 센스"))
B.append(p("2만원짜리도 예쁜 포장+메시지면 감동. 쿠팡 박스 그대로 준 10만원보다 포장 신경 쓴 3만원이 더 반응 좋아요."))

# TOP 10 - all descriptions rewritten more naturally
B.append(h2("진짜 13살 여자아이가 좋아할 선물 TOP 10"))
prods = [
    (1,"어뮤즈 듀 벨벳 틴트","쿠팡 15,800원/올리브영 18,000원","중학생 사이에서 '국민 틴트'로 불려요. 발색 선명하고 지속력 좋음. 용돈으로 사기엔 부담스러워서 선물 반응이 특히 좋아요.","핑크·코랄 계열 무난","매트 타입이라 건조할 수 있어요"),
    (2,"다꾸 세트(스티커+테이프+펜)","15,000~25,000원","단품보다 세트로 묶어주는 게 반응 두 배. 아이디어스·지그재그에 '중학생 다꾸 세트' 검색하면 2만원 안팎. 다이소 직접 구성도 1만원 가능","다이어리 꾸미기 좋아하는 아이","관심 없으면 '그냥 문구'로 느껴져요"),
    (3,"미니 향수 샘플러 세트","20,000~35,000원","풀사이즈는 취향 모르면 위험. 조말론·딥티크 미니어처(3~5만)나 국내 샘플 묶음(2만)이 딱. 예쁜 파우치에 담아주면 더 특별해요.","향기에 관심 많은 아이","알코올 향 예민하면 몇 개 못 쓸 수도"),
    (4,"무선 블루투스 이어폰","QCY 25,000~35,000 / 버즈FE 79,000원","QCY T13 가성비 최고. 갤럭시 버즈FE는 삼성폰 연동 좋음. 케이스 흰색·파스텔 핑크 추천.","학원·통학 길에 음악 듣는 아이","아이폰 유저는 중고 에어팟이 더 나을 수 있어요"),
    (5,"폴라로이드 카메라","인스탁스 미니12 69,000원","13살 여아 '로망' 아이템. 친구들이랑 찍어서 방 벽에 붙이는 용도로 인기. 필름 1팩(7,000원) 꼭 같이 주세요.","사진 찍고 공유하는 아이","필름값 장당 700~1,000원 추가 비용"),
    (6,"스킨케어 입문 세트","라운드랩 3종 32,000원","폼클렌저+토너+수분크림 기본. 라운드랩·토니모리·이니스프리 추천. 선크림 하나 더 넣어주면 완벽해요.","피부 관리 막 시작한 아이","여드름성은 일반 수분라인보다 케어 제품 필요"),
    (7,"산리오 캐릭터 인형","25,000~35,000원","시나모롤·폼폼푸린·쿠로미 여전히 인기. 20~30cm 중간 사이즈가 딱 좋아요.","산리오 좋아하는 아이","좋아하는 캐릭터 미리 확인 필수"),
    (8,"무선 충전기 패드","15,000~35,000원","매일 쓰는 실용템. 삼성 15W 듀오(3만)·벨킨 부스트업 추천. 흰색이 방 인테리어랑 잘 맞아요.","뭘 사줄지 모르겠다면 가장 무난","감동보다 실용성 위주"),
    (9,"손글씨 다이어리 세트","몰스킨 미니 22,000+젤펜 8,000=30,000원","아날로그 감성 열풍. 몰스킨·코코로 브랜드 인기. 예쁜 젤펜 3~5색 묶어주세요.","글쓰기·그림 좋아하는 감성적인 아이","관심 없으면 '그냥 공책' 느낌"),
    (10,"네컷 앨범+스티커 세트","12,000~20,000원","인생네컷 사진 모으는 미니 앨범+꾸미기 스티커. 1.5만원이면 가성비 최고 선물 완성.","사진 많이 찍는 아이","서브 선물로 더 적합"),
]
for rank, name, price, desc, rec, con in prods:
    B.append(h3(f"{rank}위 {name} - {price}"))
    B.append(p(desc))
    B.append(bp([("추천: ",True),rec]))
    B.append(bp([("아쉬운 점: ",True),con]))

B.append(h2("예산별 추천 선물 한눈에 보기"))
B.append(p("쿠팡·올리브영 판매가 기준입니다."))
B.append(bp([("~3만원 (친구·또래): ",True),"다꾸 세트, 네컷 앨범, 폰케이스, 마카롱 기프티콘"]))
B.append(bp([("3~7만원 (부모가 딸에게): ",True),"어뮤즈 틴트, QCY 이어폰, 스킨케어 세트, 인스탁스 미니"]))
B.append(bp([("7~10만원 (부모·친척): ",True),"인스탁스 링크2, 갤럭시 버즈FE, 산리오 인형 세트"]))
B.append(bp([("10만원+ (친척·어른): ",True),"에어팟, 아이패드 악세서리, 미니백"]))

B.append(h2("이런 선물은 피하는 게 좋아요"))
B.append(bp([("공부 관련 선물(참고서·문제집): ",True),"중학생한테 '공부=스트레스'예요. 문제집 선물은 최악."]))
B.append(bp([("취향 모르는 향수 풀사이즈: ",True),"향 안 맞으면 못 써요. 샘플러로 대신하세요."]))
B.append(bp([("어른스러운 실용 선물(텀블러·우산): ",True),"'써야 하는 것'보다 '갖고 싶은 것'을 선물하세요."]))

B.append(h2("관계별 생일 메시지 예시"))
B.append(p("선물+메시지 조합이 감동을 더해줍니다."))
B.append(bp([("친구에게: ",True),"생일 축하해! 이거 네가 좋아할 것 같아서 골랐어ㅎㅎ 마음에 들면 좋겠다~"]))
B.append(bp([("부모가 딸에게: ",True),"우리 딸 생일 축하해! 중학교 들어가고 많이 컸다. 앞으로도 건강하고 행복하게 지내자. 사랑해!"]))
B.append(bp([("이모·삼촌이 조카에게: ",True),"생일 축하한다! 많이 컸구나~ 이거 네가 좋아할 것 같아서 골랐어. 잘 써👍"]))

B.append(h2("마치며"))
B.append(p("13살 여자아이 선물에서 가장 중요한 건 '고민의 흔적'이에요. 비싼 것보다 '내가 좋아할 만한 걸 골랐구나'라는 느낌을 주는 게 훨씬 중요합니다. 평소에 아이가 무엇에 관심 있는지 관찰하는 게 최고의 선물 준비예요."))

total = len(B)
print(f"Blocks: {total}")
r = requests.patch(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, json={"children":B})
print(f"Append: {'OK' if r.status_code==200 else f'FAIL {r.status_code}'}")
if r.status_code!=200: print(r.text[:500])
