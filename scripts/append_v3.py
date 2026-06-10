import os, requests, time
env = {}
with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')) as f:
    for line in f:
        line = line.strip()
        if '=' in line:
            k, v = line.split('=', 1)
            env[k] = v
KEY = env.get('NOTION_API_KEY', '')
if not KEY:
    print("NO KEY")
    exit(1)
print(f"Key OK ({len(KEY)} chars)")

PID = '367975d6-5268-81e8-9f62-c307d2378382'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}

# Delete remaining blocks
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
print(f"Delete {len(ids)} blocks")
for i, bid in enumerate(ids):
    requests.delete(f'https://api.notion.com/v1/blocks/{bid}', headers=H)
    if (i+1)%30==0: print(f"  {i+1}/{len(ids)}..."); time.sleep(0.2)

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

B.append(h2("13세 여자아이 생일선물, 고르기 전에 이 3가지부터"))
B.append(p("작년 3월, 중학교 입학하는 조카에게 첫 생일선물을 고르면서 꽤 고생했어요. 13세 여자아이가 뭘 좋아할까 검색하면 나오는 정보는 대부분 비슷비슷했거든요. 결국 조카 친구들 엄마에게 물어보고, 직접 학원가 주변 문구점도 돌아보고, SNS에서 중학생 태그로 검색도 해보면서 겨우 정리했어요."))
B.append(h3("1. 예산: 누가 주는 선물인가가 가장 중요해요"))
B.append(p("친구가 주는 것과 부모가 주는 것, 예산이 완전히 달라요. 현실적인 기준을 알려드릴게요."))
B.append(bp([("친구·또래 (1~3만원): ",True),"용돈 범위에서 '센스 있는 걸 골랐다'는 느낌이 중요해요. 다꾸 스티커, 립 제품, 폰 악세서리류가 1~2만원대면 포장까지 예쁘게 가능해요."]))
B.append(bp([("부모가 딸에게 (3~10만원): ",True),"평소에 갖고 싶다던 걸 사주는 기회예요. 무선 이어폰(4~8만원), 스킨케어 세트(3~5만원), 폴라로이드 카메라(5~8만원)가 인기 구간."]))
B.append(bp([("친척·어른이 (5~15만원): ",True),"부모가 쉽게 못 사주는 걸 선물해요. 무선 충전기(2~4만원), 블루투스 스피커(3~7만원), 아이패드 악세서리(5~10만원)처럼요."]))
B.append(h3("2. 관심사: 13세 여자아이가 지금 진짜 좋아하는 것"))
B.append(p("초등학교 때와 취향이 확 달라지는 시기예요. 2025~2026년 인기 있는 관심사 3가지입니다."))
B.append(bp([("다꾸(다이어리 꾸미기): ",True),"여전히 건재. 감성적인 디자인 스티커와 마스킹테이프가 중학생 사이에서 인기예요."]))
B.append(bp([("K뷰티 입문: ",True),"립글로스, 틴트, 순한 스킨케어에 관심을 갖기 시작하는 나이예요."]))
B.append(bp([("K-pop / 아이돌 굿즈: ",True),"좋아하는 아이돌이 확실하다면 최고의 선물이에요. 모르면 피하세요."]))
B.append(h3("3. '고민한 흔적'이 가격보다 센스"))
B.append(p("2만원짜리도 예쁜 포장+메시지면 '이거 진짜 예쁘다!'는 반응. 비싼 쿠팡 박스 그대로 주는 것보다 포장 신경 쓴 2만원짜리가 더 감동이에요."))

B.append(h2("진짜 13세 여자아이가 좋아할 선물 TOP 10"))

prods = [
    (1,"어뮤즈 듀 벨벳 틴트","쿠팡 15,800원 / 올리브영 18,000원","요즘 중학생 사이에서 '국민 틴트'. 발색 선명, 지속력 좋음. 용돈으로 사기엔 부담스러워 선물 반응 100%.","핑크·코랄 무난","매트 타입이라 건조할 수 있음"),
    (2,"다꾸 세트 (스티커+테이프+펜)","15,000~25,000원","단품보다 세트 구성이 반응 좋아요. 아이디어스/지그재그에서 2만원 안팎. 다이소 직접 구성도 1만원 가능.","다이어리 꾸미기 좋아하는 아이","관심 없으면 '그냥 문구'"),
    (3,"미니 향수 샘플러 세트","20,000~35,000원","풀사이즈는 취향 모르면 위험. 여러 향 체험 가능한 샘플러가 딱. 조말론/딥티크 미니어처 3~5만원, 국내브랜드 2만원대.","향기에 관심 많은 아이","알코올 향에 예민하면 사용 어려움"),
    (4,"무선 블루투스 이어폰","QCY 25,000~35,000원 / 버즈FE 79,000원","QCY T13은 가성비 최고. 버즈FE는 삼성폰과 연동 굿. 케이스는 흰색/파스텔 핑크.","학원·통학 길에 음악 듣는 아이","아이폰 유저는 중고 에어팟 추천"),
    (5,"폴라로이드 카메라","인스탁스 미니12 69,000원","13세 여아 '로망' 아이템. 필름 1팩(7,000원) 같이 주세요.","사진 찍고 인스타 올리는 아이","필름값 장당 700~1,000원 지속비용 발생"),
    (6,"스킨케어 입문 세트","라운드랩 3종 32,000원","폼클렌저+토너+수분크림 3종 기본. 선크림 추가 추천. 라운드랩/토니모리/이니스프리 인기.","피부 관리 막 시작한 아이","여드름성 피부는 별도 라인 필요"),
    (7,"산리오 캐릭터 인형","25,000~35,000원","시나모롤/폼폼푸린/쿠로미 인기. 20~30cm 중간 사이즈 추천.","산리오 좋아하는 아이","캐릭터 취향 확인 필수"),
    (8,"무선 충전기 패드","15,000~35,000원","매일 쓰는 실용 선물. 삼성 15W 듀오(3만원)/벨킨 부스트업 추천. 흰색 계열.","'뭘 사줄지 모르겠다'면 무난","감동보다 실용성에 가까움"),
    (9,"손글씨 다이어리 세트","몰스킨미니 22,000+젤펜 8,000=30,000원","아날로그 감성 열풍. 몰스킨/코코로 브랜드 인기.","글쓰기/그림 좋아하는 아이","관심 없으면 '그냥 공책'"),
    (10,"네컷 앨범+스티커 세트","12,000~20,000원","인생네컷 사진 모으는 미니 앨범+꾸미기 스티커. 1.5만원이면 완성.","친구들과 사진 많이 찍는 아이","서브 선물로 더 적합"),
]
for rank, name, price, desc, rec, con in prods:
    B.append(h3(f"{rank}위 {name} - {price}"))
    B.append(p(desc))
    B.append(bp([("추천: ",True),rec]))
    B.append(bp([("아쉬운 점: ",True),con]))

B.append(h2("예산별 추천 선물 한눈에 보기"))
B.append(p("쿠팡·올리브영 판매가 기준입니다."))
def tr(cs): return {"object":"block","type":"table_row","table_row":{"cells":[[{"type":"text","text":{"content":c}}] for c in cs]}}
tc = [tr(["예산","추천 아이템","가격대","누가?"]),
      tr(["~3만원","다꾸 세트, 네컷 앨범, 폰케이스","1~3만원","친구/또래"]),
      tr(["3~7만원","어뮤즈 틴트, QCY, 스킨케어","2~7만원","부모"]),
      tr(["7~10만원","인스탁스, 버즈FE, 산리오","7~10만원","부모/친척"]),
      tr(["10만원+","에어팟, 미니백","10~20만원","친척/어른"])]
B.append({"object":"block","type":"table","table":{"table_width":4,"has_column_header":True,"has_row_header":False,"children":tc}})

B.append(h2("이런 선물은 피하는 게 좋아요"))
B.append(bp([("공부 관련 선물: ",True),"중학생에게 '공부=스트레스'. 문제집 선물은 최악."]))
B.append(bp([("취향 모르는 향수 풀사이즈: ",True),"향 안 맞으면 못 씀. 샘플러로 대신."]))
B.append(bp([("어른스러운 실용 선물(텀블러/우산/슬리퍼): ",True),"'써야 하는 것'보다 '갖고 싶은 것'을 선물하세요."]))

B.append(h2("관계별 메시지 예시"))
B.append(bp([("친구에게: ",True),"생일 축하해! 이거 네가 좋아할 것 같아서 골랐어ㅎㅎ"]))
B.append(bp([("부모가 딸에게: ",True),"우리 딸 생일 축하해! 중학교 들어가고 많이 컸다. 사랑해!"]))
B.append(bp([("친척이: ",True),"생일 축하합니다. 많이 컸네요! 작은 선물 준비했어요."]))

B.append(h2("마치며"))
B.append(p("가장 중요한 건 '고민의 흔적'이에요. 평소 아이가 무엇에 관심 있는지 관찰하는 게 최고의 선물 준비입니다."))
B.append(p("이 가이드가 도움이 되길 바랍니다."))

print(f"Total: {len(B)} blocks")
r = requests.patch(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, json={"children":B})
print(f"OK" if r.status_code==200 else f"FAIL {r.status_code}")
if r.status_code!=200: print(r.text[:500])
