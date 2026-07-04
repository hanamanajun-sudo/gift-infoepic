"""Notion DB → JSON 캐시 덤프.
@notionhq/client가 이 환경에서 작동하지 않으므로, Python으로 Notion 데이터를 읽어
Astro 빌드가 사용할 수 있는 JSON 캐시 파일을 생성한다.

사용법: python scripts/dump_cache.py
출력: src/data/notion-cache.json

※ 새 가이드를 Notion에 반영(push.mjs 실행)한 후 반드시 이 스크립트를 먼저 돌리고
  npm run build를 실행할 것.
"""
import os, json, urllib.request, sys

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# .env 읽기
with open(os.path.join(project_root, '.env')) as f:
    for line in f:
        line = line.strip()
        if '=' in line and not line.startswith('#'):
            k, v = line.split('=', 1)
            os.environ[k.strip()] = v.strip().strip('"')

KEY = os.environ.get('NOTION_API_KEY')
DB_GUIDES = os.environ.get('NOTION_GUIDES_DB_ID')
DB_PRODUCTS = os.environ.get('NOTION_PRODUCTS_DB_ID')

if not KEY or not DB_GUIDES:
    print("ERROR: NOTION_API_KEY 또는 NOTION_GUIDES_DB_ID가 .env에 없습니다.")
    sys.exit(1)

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

print("=== Guides DB ===")
all_guides = paginate(f'databases/{DB_GUIDES}/query', {
    'filter': {'property': 'published', 'checkbox': {'equals': True}}
})
print(f"  {len(all_guides)}개 가이드")

guides_data = []
for g in all_guides:
    p = g['properties']
    slug = ''.join(r['plain_text'] for r in (p.get('slug', {}).get('rich_text') or []))
    title = p.get('Title', {}).get('title', [{}])[0].get('plain_text', '')

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

    try:
        blocks = paginate(f'blocks/{g["id"]}/children')
        # 테이블 블록의 하위 행도 가져오기
        for b in blocks:
            if b['type'] == 'table':
                b['table']['children'] = paginate(f'blocks/{b["id"]}/children')
        entry['blocks'] = blocks
    except Exception as e:
        print(f"  블록 오류 ({slug}): {e}")
        entry['blocks'] = []

    guides_data.append(entry)

print("=== Products DB ===")
all_products = paginate(f'databases/{DB_PRODUCTS}/query', {
    'sorts': [{'property': 'rank', 'direction': 'ascending'}],
    'page_size': 100
}) if DB_PRODUCTS else []
print(f"  {len(all_products)}개 상품")

products_data = []
for p in all_products:
    props = p['properties']
    title = props.get('Title', {}).get('title', [{}])[0].get('plain_text', '')
    guide_rel = [r['id'] for r in (props.get('giftGuide', {}).get('relation') or [])]
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

out_path = os.path.join(project_root, 'src', 'data', 'notion-cache.json')
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump({'guides': guides_data, 'products': products_data, 'generatedAt': '2026-07-03'}, f, ensure_ascii=False)

print(f"\n✅ {out_path}")
print(f"   가이드: {len(guides_data)}개, 상품: {len(products_data)}개")
