"""Notion DB 전체 데이터를 JSON으로 덤프 (Node @notionhq/client 우회)"""
import os, json, urllib.request, unicodedata

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Read .env
with open(os.path.join(project_root, '.env')) as f:
    for line in f:
        line = line.strip()
        if '=' in line and not line.startswith('#'):
            k, v = line.split('=', 1)
            os.environ[k.strip()] = v.strip().strip('"')

KEY = os.environ['NOTION_API_KEY']
DB_GUIDES = os.environ['NOTION_GUIDES_DB_ID']
DB_PRODUCTS = os.environ['NOTION_PRODUCTS_DB_ID']
HEADERS = {
    'Authorization': f'Bearer {KEY}',
    'Notion-Version': '2022-06-28',
    'Content-Type': 'application/json'
}

def notion(path, body=None):
    url = f'https://api.notion.com/v1/{path}'
    data = json.dumps(body, ensure_ascii=False).encode() if body else None
    req = urllib.request.Request(url, data=data, headers=HEADERS, method='POST' if body else 'GET')
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())

def paginate(path, body=None):
    """전체 페이지네이션"""
    results = []
    cursor = None
    while True:
        b = dict(body or {})
        if cursor:
            b['start_cursor'] = cursor
        data = notion(path, b)
        results.extend(data.get('results', []))
        cursor = data.get('next_cursor')
        if not cursor:
            break
    return results

print("=== 1. Guide DB 전체 덤프 ===")
all_guides = paginate(f'databases/{DB_GUIDES}/query', {
    'filter': {'property': 'published', 'checkbox': {'equals': True}}
})
print(f"  총 {len(all_guides)}개 가이드")

# 각 가이드의 본문 블록도 가져오기
guides_data = []
for g in all_guides:
    p = g['properties']
    slug = ''
    if p.get('slug', {}).get('rich_text'):
        slug = ''.join(r['plain_text'] for r in p['slug']['rich_text'])
    
    title = ''
    if p.get('Title', {}).get('title'):
        title = p['Title']['title'][0]['plain_text']
    
    entry = {
        'id': g['id'],
        'slug': slug,
        'title': title,
        'description': ''.join(r['plain_text'] for r in (p.get('description', {}).get('rich_text') or [])),
        'intro': ''.join(r['plain_text'] for r in (p.get('intro', {}).get('rich_text') or [])),
        'recipientAge': p.get('recipientAge', {}).get('number'),
        'recipientGender': (p.get('recipientGender', {}).get('select') or {}).get('name') or '',
        'relation': [s['name'] for s in (p.get('relation', {}).get('multi_select') or [])],
        'occasion': [s['name'] for s in (p.get('occasion', {}).get('multi_select') or [])],
        'ageGroup': [s['name'] for s in (p.get('ageGroup', {}).get('multi_select') or [])],
        'budgetTag': [s['name'] for s in (p.get('budgetTag', {}).get('multi_select') or [])],
        'priceMin': p.get('priceMin', {}).get('number'),
        'priceMax': p.get('priceMax', {}).get('number'),
        'interests': [s['name'] for s in (p.get('interests', {}).get('multi_select') or [])],
        'thumbnail': ''.join(r['plain_text'] for r in (p.get('thumbnail', {}).get('rich_text') or [])),
        'updatedAt': g['last_edited_time'],
    }
    
    # 본문 블록 가져오기
    try:
        blocks = paginate(f'blocks/{g["id"]}/children')
        entry['blocks'] = blocks
    except Exception as e:
        print(f"  블록 읽기 실패 ({slug}): {e}")
        entry['blocks'] = []
    
    guides_data.append(entry)
    print(f"  [{slug}] {title} — 블록 {len(entry['blocks'])}개")

print("\n=== 2. Products DB 전체 덤프 ===")
# Products DB는 filter 없이 query가 안 될 수 있어 rank 기준 정렬로 쿼리
all_products = paginate(f'databases/{DB_PRODUCTS}/query', {
    'sorts': [{'property': 'rank', 'direction': 'ascending'}],
    'page_size': 100
})
print(f"  총 {len(all_products)}개 상품")

products_data = []
for p in all_products:
    props = p['properties']
    title = ''
    if props.get('Title', {}).get('title'):
        title = props['Title']['title'][0]['plain_text']
    
    guide_rel = []
    if props.get('giftGuide', {}).get('relation'):
        guide_rel = [r['id'] for r in props['giftGuide']['relation']]
    
    products_data.append({
        'id': p['id'],
        'name': title,
        'price': props.get('price', {}).get('number'),
        'coupangUrl': (props.get('coupangUrl', {}).get('url') or ''),
        'naverUrl': (props.get('naverUrl', {}).get('url') or ''),
        'imageUrl': ''.join(r['plain_text'] for r in (props.get('imageUrl', {}).get('rich_text') or [])),
        'rank': props.get('rank', {}).get('number') or 99,
        'pros': ''.join(r['plain_text'] for r in (props.get('pros', {}).get('rich_text') or [])),
        'guideId': guide_rel[0] if guide_rel else None,
    })

# JSON 저장
output = {
    'guides': guides_data,
    'products': products_data,
    'generatedAt': '2026-07-03T23:50:00Z',
}

out_path = os.path.join(project_root, 'src', 'data', 'notion-cache.json')
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"\n✅ 캐시 저장 완료: {out_path}")
print(f"   가이드: {len(guides_data)}개")
print(f"   상품: {len(products_data)}개")
print(f"   파일 크기: {os.path.getsize(out_path):,} 바이트")
