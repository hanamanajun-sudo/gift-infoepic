import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key
KEY = get_key()
GUIDES_DB = '9603a00b-976b-4791-a129-d5f537e5db06'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}

for slug_search, title in [
    ('쿠션-선물', '쿠션 선물, 어떤 게 좋을까요? 네이버 쇼핑에서 인기 있는 쿠션·방석 제품을 정리했습니다.'),
    ('설날-선물', '설날 선물, 뭘 준비해야 할지 고민되시죠? 네이버 블로그에서 언급된 인기 설날 선물을 정리했습니다.'),
    ('머그컵-선물', '머그컵 선물, 예쁘고 실용적인 컵을 찾고 계신가요? 네이버 쇼핑 인기 머그컵을 정리했습니다.'),
    ('추석-선물', '추석 선물, 부모님·친지께 뭘 드려야 할지 고민이세요? 네이버 쇼핑에서 인기 있는 추석 선물을 정리했습니다.'),
    ('화장품-선물', '화장품 선물, 어떤 제품을 골라야 할지 모르겠다면? 네이버 쇼핑 인기 화장품 선물 세트를 정리했습니다.'),
    ('헤드폰-선물', '헤드폰 선물, 음질과 가격 어떤 걸 골라야 할까요? 네이버 쇼핑에서 인기 있는 헤드폰을 정리했습니다.'),
]:
    r = requests.post(f'https://api.notion.com/v1/databases/{GUIDES_DB}/query', headers=H, json={
        'filter': {'property': 'slug', 'rich_text': {'contains': slug_search}},
        'page_size': 5
    })
    results = r.json().get('results', [])
    if not results: 
        print(f'{slug_search}: NOT FOUND'); continue
    p = results[0]
    PID = p['id']
    print(f'{slug_search}: {PID[:30]}...')
    
    requests.patch(f'https://api.notion.com/v1/pages/{PID}', headers=H, json={
        'properties': {'intro': {'rich_text': [{'text': {'content': title}}]}}
    })
    
    ids = []
    cur = None
    while True:
        pp = {'page_size': 100}
        if cur: pp['start_cursor'] = cur
        r2 = requests.get(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, params=pp)
        d = r2.json()
        ids.extend(b['id'] for b in d.get('results', []))
        if not d.get('has_more'): break
        cur = d.get('next_cursor')
    for bid in ids: requests.delete(f'https://api.notion.com/v1/blocks/{bid}', headers=H)
    
    def h2(t): return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':t}}]}}
    def h3(t): return {'object':'block','type':'heading_3','heading_3':{'rich_text':[{'type':'text','text':{'content':t}}]}}
    def p(t): return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':t}}]}}
    def bp(pts):
        r = []
        for pt in pts:
            if isinstance(pt,tuple): r.append({'type':'text','text':{'content':pt[0]},'annotations':{'bold':True}})
            else: r.append({'type':'text','text':{'content':pt}})
        return {'object':'block','type':'paragraph','paragraph':{'rich_text':r}}
    
    B = []
    if slug_search == '쿠션-선물':
        B.append(h2('쿠션 선물, 고르기 전에 생각할 3가지'))
        B.append(p('쿠션은 집들이 선물, 생일 선물로 부담 없는 가격에 인기입니다. 네이버 쇼핑에서 인기 있는 쿠션 제품들을 기준으로 정리했습니다.'))
        B.append(h3('1. 용도에 따라 모양이 다릅니다'))
        B.append(p('등받이 쿠션(허리), 바디필로우(수면), 방석(의자), 인테리어 쿠션(소파)까지 용도에 따라 제품이 다릅니다. 받는 사람의 필요를 먼저 생각하세요.'))
        B.append(h3('2. 디자인과 색상이 중요합니다'))
        B.append(p('쿠션은 인테리어 소품이기도 합니다. 받는 사람의 방이나 거실 인테리어 스타일에 맞는 디자인을 고르는 게 좋습니다. 무난한 베이지·그레이·크림 계열이 안전합니다.'))
        B.append(h3('3. 가격대'))
        B.append(bp([('~2만원',True),' 소형 인테리어 쿠션, 등받이 쿠션']))
        B.append(bp([('2~5만원',True),' 바디필로우, 대형 쿠션, 방석 세트']))
        B.append(bp([('5만원+',True),' 기능성 쿠션(목·허리), 고급 소재 쿠션']))
        B.append(h2('인기 쿠션 종류'))
        B.append(h3('등받이·허리 쿠션 — 1~3만원대'))
        B.append(p('의자에 앉아 오래 일하는 사람에게 좋은 선물입니다. 메모리폼 소재가 인기. 네이버 쇼핑 리뷰 수천 개 이상의 제품이 많습니다.'))
        B.append(h3('바디필로우 — 2~4만원대'))
        B.append(p('잠잘 때 안고 자는 바디필로우는 여성에게 특히 인기. 긴 베개 형태로 옆으로 누워 잘 때 편안함을 줍니다.'))
        B.append(h3('인테리어 쿠션 — 1~3만원대'))
        B.append(p('소파나 침대에 올려두는 인테리어 소품용 쿠션. 귀여운 디자인이나 감성적인 패턴이 인기입니다. 집들이 선물로 가장 좋습니다.'))
        B.append(h2('마치며'))
        B.append(p('쿠션 선물은 가격 부담이 적고 실용적이라 실패 확률이 낮습니다. 받는 사람의 인테리어 취향을 고려해서 고르면 더 좋은 반응을 얻을 수 있습니다.'))

    elif slug_search == '설날-선물':
        B.append(h2('설날 선물, 고르기 전에 생각할 3가지'))
        B.append(p('설날은 가족·친지에게 감사의 마음을 전하는 대표적인 명절입니다. 네이버 쇼핑에서 인기 있는 설날 선물 세트를 기준으로 정리했습니다.'))
        B.append(h3('1. 건강식품이 1순위'))
        B.append(p('정관장 홍삼 세트, 종합비타민, 한과 선물 세트가 설날 선물로 가장 인기입니다. 네이버 쇼핑 명절 선물 코너에서 매년 인기입니다.'))
        B.append(h3('2. 가격대별 추천'))
        B.append(bp([('3~5만원',True),' 한과 세트, 과일 세트, 커피 선물 세트']))
        B.append(bp([('5~10만원',True),' 홍삼 세트(소), 건강기능식품, 스팸 선물 세트']))
        B.append(bp([('10~20만원',True),' 홍삼 세트(대), 한우 세트, 굴비 세트']))
        B.append(h3('3. 전통적인 선물이 무난합니다'))
        B.append(p('매년 새로운 트렌드가 나오지만, 명절에는 전통적인 선물(홍삼, 한우, 과일, 굴비, 참치)이 가장 무난하고 실패 확률이 낮습니다.'))
        B.append(h2('자주 언급된 선물'))
        B.append(h3('건강기능식품 — 5~15만원'))
        B.append(p('정관장 홍삼 세트가 가장 전통적인 명절 선물. 네이버 명절 선물 코너에서 매년 1위를 차지합니다.'))
        B.append(h3('한우·굴비 세트 — 5~20만원'))
        B.append(p('명절에 특히 인기 있는 식품 선물. 쿠팡과 네이버쇼핑에서 등급과 구성에 따라 가격대가 다양합니다.'))
        B.append(h3('과일 세트 — 3~10만원'))
        B.append(p('사과·배 선물 세트가 전통적인 설 선물. 제철 과일인 사과, 배, 한라봉 등이 인기입니다.'))
        B.append(h2('마치며'))
        B.append(p('설날 선물은 트렌드보다 전통이 중요합니다. 매년 달라지는 신상품보다는 정관장 홍삼, 한우, 과일 세트 같은 검증된 선물이 가장 안전합니다.'))

    elif slug_search == '머그컵-선물':
        B.append(h2('머그컵 선물, 고르기 전에 생각할 3가지'))
        B.append(p('머그컵은 부담 없는 가격에 실용적인 선물로 인기입니다. 네이버 쇼핑에서 인기 있는 머그컵 제품을 기준으로 정리했습니다.'))
        B.append(h3('1. 디자인이 가장 중요'))
        B.append(p('머그컵은 매일 사용하는 만큼 디자인이 가장 중요합니다. 받는 사람의 취향(미니멀, 감성, 캐릭터)을 고려하세요.'))
        B.append(h3('2. 소재와 기능'))
        B.append(p('도자기(전자레인지 가능), 스테인리스(보온), 유리(투명)까지 소재에 따라 용도가 다릅니다. 선물할 사람의 사용 패턴을 생각해보세요.'))
        B.append(h3('3. 가격대'))
        B.append(bp([('~1만원',True),' 감성 머그컵, 캐릭터 머그컵 1~2개']))
        B.append(bp([('1~3만원',True),' 머그컵 2~4개 세트, 고급 도자기 머그']))
        B.append(bp([('3만원+',True),' 브랜드 머그 세트, 수제 도자기 머그']))
        B.append(h2('인기 머그컵'))
        B.append(h3('감성 머그컵 — 5,000~15,000원'))
        B.append(p('감성 문구나 귀여운 디자인의 단독 머그컵. 카카오톡 선물하기에서도 인기. 부담 없는 가격에 가벼운 선물로 좋습니다.'))
        B.append(h3('머그컵 세트 — 2~3만원'))
        B.append(p('2~4개들이 세트는 집들이 선물로 특히 인기. 모던한 디자인부터 클래식한 패턴까지 다양합니다.'))
        B.append(h3('보온 머그 (스테인리스·텀블러) — 1~3만원'))
        B.append(p('보온 기능이 있는 머그는 직장인에게 실용적인 선물입니다. 스탠리, 스웰, 서모스 브랜드가 인기입니다.'))
        B.append(h2('마치며'))
        B.append(p('머그컵은 가격 부담이 적고 매일 사용하는 실용적인 선물입니다. 받는 사람의 취향만 고려하면 실패 확률이 매우 낮습니다.'))

    elif slug_search == '추석-선물':
        B.append(h2('추석 선물, 고르기 전에 생각할 3가지'))
        B.append(p('추석은 설과 함께 가장 큰 명절 선물 시즌입니다. 네이버 쇼핑에서 인기 있는 추석 선물 세트를 기준으로 정리했습니다.'))
        B.append(h3('1. 선물 세트가 대세'))
        B.append(p('네이버쇼핑·쿠팡의 명절 선물 코너에서 다양한 선물 세트를 판매합니다. 홍삼, 건강식품, 과일, 한우 등이 가장 인기입니다.'))
        B.append(h3('2. 가격대별 추천'))
        B.append(bp([('3~5만원',True),' 건강음료 세트, 과일 세트(소), 커피 선물 세트']))
        B.append(bp([('5~10만원',True),' 홍삼 세트, 건강기능식품, 참치·스팸 세트']))
        B.append(bp([('10~20만원',True),' 한우 세트, 굴비 세트, 프리미엄 홍삼']))
        B.append(h3('3. 사전 예약이 필수'))
        B.append(p('명절 선물은 2~3주 전에 미리 주문해야 원하는 제품을 받을 수 있습니다. 네이버쇼핑과 쿠팡은 명절 3~4주 전부터 선물 코너를 오픈합니다.'))
        B.append(h2('자주 언급된 선물'))
        B.append(h3('건강기능식품 — 5~15만원'))
        B.append(p('정관장 홍삼, 종합비타민, 오메가3가 대표적인 추석 선물입니다. 작년 대비 가격 변동이 있을 수 있으니 미리 확인하세요.'))
        B.append(h3('한우 세트 — 10~20만원'))
        B.append(p('추석에 가장 인기 있는 선물 중 하나. 등급(1+ 등급 추천)과 부위(불고기, 구이용 혼합)를 확인하고 구매하세요.'))
        B.append(h3('과일 세트 — 5~10만원'))
        B.append(p('사과·배·샤인머스캣 등 제철 과일 세트가 인기입니다. 당일 배송보다 예약 배송이 안전합니다.'))
        B.append(h2('마치며'))
        B.append(p('추석 선물도 설과 마찬가지로 전통적인 선물이 가장 안전합니다. 검증된 브랜드의 선물 세트를 미리 준비하는 게 좋습니다.'))

    elif slug_search == '화장품-선물':
        B.append(h2('화장품 선물, 고르기 전에 생각할 3가지'))
        B.append(p('화장품은 여성 선물의 단골 아이템이지만, 취향을 몰라서 망설여지는 경우가 많습니다. 네이버 쇼핑에서 인기 있는 화장품 선물 세트를 기준으로 정리했습니다.'))
        B.append(h3('1. 스킨케어 세트가 가장 무난'))
        B.append(p('립스틱이나 파운데이션 같은 색조 화장품은 취향을 많이 타지만, 스킨케어(토너, 로션, 크림) 세트는 비교적 무난합니다. 설화수·후 같은 한방 브랜드나 라운드랩·토니모리 같은 중저가 브랜드가 인기입니다.'))
        B.append(h3('2. 가격대별 추천'))
        B.append(bp([('~3만원',True),' 핸드크림 세트, 립 제품, 시트마스크 팩']))
        B.append(bp([('3~7만원',True),' 스킨케어 미니 세트, 향수 샘플러']))
        B.append(bp([('7~15만원',True),' 설화수·후 기획세트, 고급 에센스']))
        B.append(h3('3. 잘 모르겠다면 세트 상품으로'))
        B.append(p('낱개보다 세트 상품이 포장도 예쁘고 선물용으로 좋습니다. 백화점이나 네이버쇼핑 브랜드스토어에서 기획세트를 확인하세요.'))
        B.append(h2('인기 화장품 선물'))
        B.append(h3('스킨케어 세트 — 5~15만원'))
        B.append(p('설화수 자음 2종 세트, 후 공진향 세트, 라운드랩 미니 세트가 대표적입니다. 명절 선물로도 인기입니다.'))
        B.append(h3('립 제품 세트 — 2~5만원'))
        B.append(p('여자 친구·동료 선물로 인기. 여러 색상이 들어있는 세트가 낱개보다 좋습니다. 롬앤, 에뚜드, 어뮤즈 등이 인기 브랜드입니다.'))
        B.append(h3('향수 — 3~15만원'))
        B.append(p('취향을 모르면 실패할 수 있습니다. 가벼운 선물이라면 샘플러 세트(2~3만원)가 안전합니다.'))
        B.append(h2('마치며'))
        B.append(p('화장품 선물은 받는 사람의 피부 타입과 평소 사용하는 브랜드를 확인하는 게 가장 중요합니다. 모르겠다면 스킨케어 세트나 핸드크림 세트가 무난합니다.'))

    elif slug_search == '헤드폰-선물':
        B.append(h2('헤드폰 선물, 고르기 전에 생각할 3가지'))
        B.append(p('헤드폰은 게임, 음악 감상, 업무용으로 다양하게 사용되는 실용적인 선물입니다. 네이버 쇼핑에서 인기 있는 헤드폰을 기준으로 정리했습니다.'))
        B.append(h3('1. 무선 vs 유선'))
        B.append(p('요즘은 무선 헤드폰(블루투스)이 대세입니다. 유선은 고음질 감상용으로만 사용하는 추세입니다. 선물이라면 무선 헤드폰을 추천합니다.'))
        B.append(h3('2. 용도에 따라 다릅니다'))
        B.append(p('게임용(마이크+가상 7.1채널), 음악 감상용(고음질, ANC), 운동용(방수, 가벼움), 업무용(노이즈캔슬링) 등 용도에 따라 추천 제품이 다릅니다.'))
        B.append(h3('3. 가격대별 추천'))
        B.append(bp([('~5만원',True),' QCY, 브리츠 등 가성비 무선 헤드폰']))
        B.append(bp([('5~15만원',True),' Sony WH-1000X, 보스 QC, JBL 등']))
        B.append(bp([('15~30만원',True),' 에어팟 맥스, Sony WH-1000XM5, 보스 QC 울트라']))
        B.append(h2('인기 헤드폰'))
        B.append(h3('가성비 무선 헤드폰 — 3~7만원'))
        B.append(p('QCY H2(약 3만원), 브리츠(4~5만원) 등이 가성비로 인기입니다. 학생이나 첫 헤드폰을 찾는 사람에게 좋습니다.'))
        B.append(h3('노이즈캔슬링 헤드폰 — 10~30만원'))
        B.append(p('Sony WH-1000XM5(약 30만원), 보스 QC(약 25만원)가 최고의 노이즈캔슬링 성능을 자랑합니다. 비행기, 카페, 도서관에서 사용하기 좋습니다.'))
        B.append(h3('게이밍 헤드셋 — 5~15만원'))
        B.append(p('로지텍 G733, 커세어 HS 시리즈 등이 인기. 마이크 품질과 가상 7.1채널이 게이밍 헤드셋의 핵심입니다.'))
        B.append(h2('마치며'))
        B.append(p('헤드폰은 용도에 따라 천차만별이지만, 일단 무선 블루투스 제품을 고르면 크게 실패하지 않습니다. 개별 제품의 가격은 쿠팡·네이버쇼핑에서 확인하세요.'))
    
    print(f'{len(B)} blocks')
    r = requests.patch(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, json={'children': B})
    print(f"{'OK' if r.status_code==200 else f'FAIL {r.status_code}'}")
