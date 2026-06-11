import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

K = get_key()
H = {'Authorization': f'Bearer {K}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}
GDB = '9603a00b-976b-4791-a129-d5f537e5db06'

# 이미 리라이팅 완료된 slug 목록
DONE = [
    '쿠션-선물-추천', '설날-선물-추천', '머그컵-선물-추천', '추석-선물-추천',
    '화장품-선물-추천', '헤드폰-선물-추천', '인형-선물-추천', '책-선물-추천',
    '장인어른-선물', '남동생-선물', '여동생-선물', '캔들-선물-추천',
    '텀블러-선물-추천', '스킨케어-선물-추천', '향수-선물-추천',
    '귀걸이-선물-추천', '가방-선물-추천'
]

r = requests.post(f'https://api.notion.com/v1/databases/{GDB}/query', headers=H, json={'page_size': 100})
all_guides = r.json()['results']

print(f'전체 가이드: {len(all_guides)}개')
print(f'완료: {len(DONE)}개')
print(f'남은: {len(all_guides) - len(DONE)}개')
print()

remaining = []
for g in all_guides:
    props = g['properties']
    slug_cell = props.get('slug', {}).get('rich_text', [])
    slug = slug_cell[0]['text']['content'] if slug_cell else '??'
    title_cell = props.get('title', {}).get('title', [])
    title = title_cell[0]['text']['content'] if title_cell else slug
    
    # 페이지 첫 100자 보기 (intro 대신 page content 첫 블록)
    pid = g['id']
    r2 = requests.get(f'https://api.notion.com/v1/blocks/{pid}/children', headers=H, params={'page_size': 3})
    blocks = r2.json().get('results', [])
    preview = ''
    for b in blocks:
        rt = b.get(b['type'], {}).get('rich_text', [])
        if rt:
            preview = rt[0]['text']['content'][:60]
            break
    
    remaining.append((slug, title, preview))

# DONE 제외
remaining = [r for r in remaining if r[0] not in DONE]

# 주제 추정을 위해 slug로 그룹핑
groups = {
    '연령별': [],
    '관계별': [],
    '상황별': [],
    '예산별': [],
    '아이템별': [],
    '기타': [],
}

for slug, title, preview in remaining:
    # 카테고리 추정
    age_kw = ['7세','초등','중학생','고등학생','20대','30대','40대','50대','13살','14살','15살']
    rel_kw = ['엄마','아빠','할머니','할아버지','남자친구','여자친구','어머니','아버지','시아버지',
              '시어머니','친구','직장','선배','후배','사장님','스승','제자','동료']
    occ_kw = ['생일','크리스마스','어린이날','졸업','입학','발렌타인','화이트데이','빼빼로',
              '집들이','결혼','답례품','명절','어버이날','스승의날']
    bud_kw = ['만원','가격','예산','저렴','가성비','부담']
    item_kw = ['지갑','시계','넥타이','벨트','목도리','장갑','모자','운동화','슬리퍼',
               '이어폰','스피커','보조배터리','마우스','키보드','노트북','태블릿',
               '등받이','안마','건강','영양제','비타민','홍삼']
    
    if any(k in slug for k in age_kw):
        groups['연령별'].append((slug, preview))
    elif any(k in slug for k in rel_kw):
        groups['관계별'].append((slug, preview))
    elif any(k in slug for k in occ_kw):
        groups['상황별'].append((slug, preview))
    elif any(k in slug for k in bud_kw):
        groups['예산별'].append((slug, preview))
    elif any(k in slug for k in item_kw):
        groups['아이템별'].append((slug, preview))
    else:
        groups['기타'].append((slug, preview))

for grp, items in groups.items():
    if items:
        print(f'\n## {grp} ({len(items)}건)')
        for slug, preview in items:
            print(f'  /선물/{slug}/')
            if preview:
                print(f'    → "{preview}..."')
