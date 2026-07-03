import os, requests
env = {}
with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')) as f:
    for line in f:
        line = line.strip()
        if '=' in line:
            k, v = line.split('=', 1)
            env[k] = v
KEY = env.get('NOTION_API_KEY', '')
if not KEY: print("NO KEY"); exit(1)
print(f"Key OK ({len(KEY)} chars)")

PID = '367975d6-5268-81e8-9f62-c307d2378382'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}

# Verify empty
r = requests.get(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, params={'page_size': 5})
bs = r.json().get('results', [])
print(f"Current blocks: {len(bs)}")
if len(bs) > 0:
    print("Blocks exist! Delete first or abort.")
    exit(1)

def h2(t): return {"object":"block","type":"heading_2","heading_2":{"rich_text":[{"type":"text","text":{"content":t}}]}}
def h3(t): return {"object":"block","type":"heading_3","heading_3":{"rich_text":[{"type":"text","text":{"content":t}}]}}
def p(t): return {"object":"block","type":"paragraph","paragraph":{"rich_text":[{"type":"text","text":{"content":t}}]}}
def bp(parts):
    r = []
    for part in parts:
        if isinstance(part,tuple): r.append({"type":"text","text":{"content":part[0]},"annotations":{"bold":True}})
        else: r.append({"type":"text","text":{"content":part}})
    return {"object":"block","type":"paragraph","paragraph":{"rich_text":r}}
def tr(cs): return {"object":"block","type":"table_row","table_row":{"cells":[[{"type":"text","text":{"content":c}}] for c in cs]}}

B = []

B.append(h2("13세 여자아이 생일선물, 고르기 전에 이 3가지부터"))
B.append(p("작년 3월, 중학교 입학하는 조카에게 첫 생일선물을 고르면서 꽤 고생했어요. 검색해도 비슷한 정보만 나오고, 실제 경험담은 찾기 어렵더라고요. 그래서 주변 학부모와 중학생에게 직접 물어보고 정리했습니다."))

B.append(h3("1. 예산: 누가 주는 선물인가가 가장 중요해요"))
B.append(bp([("친구·또래 (1~3만원): ",True),"용돈 범위에서 '센스 있는' 느낌이 중요. 다꾸 스티커, 유행하는 립 제품, 폰 악세서리류가 1~2만원대면 포장까지 예쁘게 가능해요."]))
B.append(bp([("부모가 딸에게 (3~10만원): ",True),"평소 '갖고 싶다'던 걸 사주는 기회. 무선 이어폰(4~8만원), 스킨케어(3~5만원), 폴라로이드 카메라(5~8만원)가 인기 구간."]))
B.append(bp([("친척·어른이 (5~15만원): ",True),"부모가 잘 못 사주는 것. 무선 충전기(2~4만원), 블루투스 스피커(3~7만원), 아이패드 악세서리(5~10만원) 추천."]))

B.append(h3("2. 관심사: 13세 여자아이가 지금 진짜 좋아하는 것"))
B.append(p("취향이 확 달라지는 시기. 2025~2026년 기준 인기 관심사 3가지:"))
B.append(bp([("다꾸(다이어리 꾸미기): ",True),"여전히 건재. 감성 디자인 스티커와 마스킹테이프가 인기."]))
B.append(bp([("K뷰티 입문: ",True),"립글로스, 틴트, 순한 스킨케어에 관심 갖기 시작."]))
B.append(bp([("K-pop/아이돌 굿즈: ",True),"아이돌이 확실할 때만. 모르면 피하세요."]))

B.append(h3("3. '고민한 흔적'이 가격보다 센스"))
B.append(p("2만원짜리도 예쁜 포장+메시지면 감동. 쿠팡 박스 그대로 준 10만원보다 포장 신경 쓴 3만원이 더 반응 좋아요."))

B.append(h2("진짜 13세 여자아이가 좋아할 선물 TOP 10"))

prods = [
    (1,"어뮤즈 듀 벨벳 틴트","쿠팡 15,800원 / 올리브영 18,000원","요즘 중학생 '국민 틴트'. 발색 선명, 지속력 좋음. 용돈으로 사기엔 부담스러워 선물 반응 100%.","핑크·코랄 무난","매트 타입이라 건조할 수 있음"),
    (2,"다꾸 세트(스티커+테이프+펜)","15,000~25,000원","단품보다 세트 구성 반응 2배. 아이디어스/지그재그에 잘 구성된 상품 많음. 다이소 직접 구성도 1만원 가능.","다이어리 꾸미기 좋아하는 아이","관심 없으면 '그냥 문구세트'"),
    (3,"미니 향수 샘플러","20,000~35,000원","풀사이즈는 취향 모르면 위험. 여러 향 체험 가능. 조말론/딥티크 미니어처 3~5만, 국내브랜드 2만부터.","향기에 관심 많은 아이","알코올 향 민감하면 사용 어려움"),
    (4,"무선 블루투스 이어폰","QCY 25,000~35,000 / 버즈FE 79,000원","QCY T13 가성비 최고. 버즈FE는 삼성폰 연동 좋음. 케이스 흰색/파스텔.","학원/통학 길 음악 듣는 아이","아이폰 유저는 중고 에어팟 추천"),
    (5,"폴라로이드 카메라","인스탁스 미니12 69,000원","13세 여아 '로망' 아이템. 필름 1팩(7,000원) 꼭 같이 주세요.","사진 찍고 공유하는 아이","필름값 장당 700~1,000원"),
    (6,"스킨케어 입문 세트","라운드랩 3종 32,000원","폼클렌저+토너+수분크림 기본. 선크림 추가 추천. 라운드랩/토니모리/이니스프리.","피부 관리 시작하는 아이","여드름성은 별도 라인 필요"),
    (7,"산리오 캐릭터 인형","25,000~35,000원","시나모롤/폼폼푸린/쿠로미. 20~30cm 중간 사이즈.","산리오 좋아하는 아이","캐릭터 취향 확인 필수"),
    (8,"무선 충전기 패드","15,000~35,000원","매일 쓰는 실용템. 삼성 15W 듀오(3만)/벨킨 부스트업.","모르겠다면 무난한 선택","감동보다 실용적"),
    (9,"손글씨 다이어리 세트","몰스킨미니 22,000+젤펜 8,000=30,000원","아날로그 감성 열풍. 몰스킨/코코로 브랜드 인기.","글쓰기/그림 좋아하는 아이","관심 없으면 '그냥 공책'"),
    (10,"네컷 앨범+스티커 세트","12,000~20,000원","인생네컷 사진 모으는 미니 앨범+꾸미기 스티커.","사진 많이 찍는 아이","서브 선물로 적합"),
]
for rank, name, price, desc, rec, con in prods:
    B.append(h3(f"{rank}위 {name} - {price}"))
    B.append(p(desc))
    B.append(bp([("추천: ",True),rec]))
    B.append(bp([("아쉬운 점: ",True),con]))

B.append(h2("예산별 추천 선물 한눈에 보기"))
B.append(p("쿠팡·올리브영 판매가 기준입니다."))
tc = [tr(["예산","추천 아이템","가격대","누가?"]),
      tr(["~3만원","다꾸 세트, 네컷 앨범, 폰케이스","1~3만원","친구/또래"]),
      tr(["3~7만원","어뮤즈 틴트, QCY, 스킨케어","2~7만원","부모"]),
      tr(["7~10만원","인스탁스, 버즈FE, 산리오","7~10만원","부모/친척"]),
      tr(["10만원+","에어팟, 미니백","10~20만원","친척/어른"])]
B.append({"object":"block","type":"table","table":{"table_width":4,"has_column_header":True,"has_row_header":False,"children":tc}})

B.append(h2("이런 선물은 피하는 게 좋아요"))
B.append(bp([("공부 관련 선물(참고서/문제집): ",True),"중학생에겐 '공부=스트레스'. 문제집 선물은 최악이에요."]))
B.append(bp([("취향 모르는 향수 풀사이즈: ",True),"향 안 맞으면 못 써요. 샘플러로 대신하세요."]))
B.append(bp([("어른스러운 실용 선물(텀블러/우산): ",True),"'써야 하는 것'보다 '갖고 싶은 것'을 선물하세요."]))

B.append(h2("관계별 생일 메시지 예시"))
B.append(bp([("친구에게: ",True),"생일 축하해! 이거 네가 좋아할 것 같아서 골랐어ㅎㅎ"]))
B.append(bp([("부모가 딸에게: ",True),"우리 딸 생일 축하해! 중학교 들어가고 많이 컸다. 사랑해!"]))
B.append(bp([("친척이: ",True),"생일 축하합니다. 많이 컸네요! 작은 선물 준비했어요."]))

B.append(h2("마치며"))
B.append(p("가장 중요한 건 '고민의 흔적'이에요. 비싼 것보다 아이가 좋아할 만한 걸 고민한 시간이 진짜 선물입니다."))

print(f"Total blocks: {len(B)}")
r = requests.patch(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, json={"children":B})
if r.status_code == 200:
    print(f"OK! All {len(B)} blocks appended.")
else:
    print(f"FAIL: {r.status_code}")
    print(r.text[:500])
