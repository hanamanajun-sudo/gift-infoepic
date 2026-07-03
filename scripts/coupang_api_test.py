import requests, time, hmac, hashlib, json
from urllib.parse import quote
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

K = get_key()
H = {'Authorization': f'Bearer {K}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}
PDB = '3595b6af-2ff8-44aa-bb2f-9a75d9e0c487'
GDB = '9603a00b-976b-4791-a129-d5f537e5db06'

# Coupang API config
ACCESS_KEY = '72663e86-ee7b-45b2-a384-4b686cd0adcb'
SECRET_KEY='***'
DOMAIN = 'https://api-gateway.coupang.com'

def search_products(keyword, limit=3):
    ts = time.strftime('%y%m%dT%H%M%SZ', time.gmtime())
    path = '/v2/providers/affiliate_open_api/apis/openapi/v1/products/search'
    query = f'keyword={quote(keyword)}&limit={limit}&sortType=BEST'
    msg = ts + 'GET' + path + query
    sig = hmac.new(SECRET_KEY.encode(), msg.encode(), hashlib.sha256).hexdigest()
    auth = f'CEA algorithm=HmacSHA256, access-key={ACCESS_KEY}, signed-date={ts}, signature={sig}'
    headers = {'Authorization': auth, 'Content-Type': 'application/json'}
    r = requests.get(f'{DOMAIN}{path}?{query}', headers=headers, timeout=15)
    if r.status_code == 200:
        return r.json().get('data', {}).get('productData', [])
    return []

def get_guide_id(slug):
    r = requests.post(f'https://api.notion.com/v1/databases/{GDB}/query', headers=H, json={
        'filter': {'property': 'slug', 'rich_text': {'contains': slug}}, 'page_size': 3})
    return r.json()['results'][0]['id']

def add_product(guide_slug, product, rank):
    """Add a product from Coupang API result to Products DB"""
    gid = get_guide_id(guide_slug)
    name = product.get('productName', '')
    price = product.get('productPrice', 0)
    image = product.get('productImage', '')
    url = product.get('productUrl', '')
    
    if not name:
        return False
    
    props = {
        'Title': {'title': [{'text': {'content': name[:100]}}]},
        'price': {'number': price if isinstance(price, (int, float)) else 0},
        'coupangUrl': {'url': url if url.startswith('http') else f'https://www.coupang.com{url}'},
        'pros': {'rich_text': [{'text': {'content': f'쿠팡 API 검색 결과. 가격과 이미지는 쿠팡에서 확인하세요.'}}]},
        'rank': {'number': rank},
        'giftGuide': {'relation': [{'id': gid}]},
    }
    if image:
        props['imageUrl'] = {'rich_text': [{'text': {'content': image}}]}
    
    r = requests.post(f'https://api.notion.com/v1/pages', headers=H, 
        json={'parent': {'database_id': PDB}, 'properties': props})
    return r.status_code == 200, name, price, url

# Test: Search products for '어뮤즈 립틴트'
print('=== 쿠팡 API 검색 테스트 ===')
prods = search_products('어뮤즈 립틴트', 3)
print(f'검색 결과: {len(prods)}개')
for i, p in enumerate(prods[:3]):
    name = p.get('productName','?')
    price = p.get('productPrice','?')
    url = p.get('productUrl','?')
    img = p.get('productImage','')
    print(f'  {i+1}. {name[:50]}')
    print(f'     가격: {price}원')
    print(f'     링크: {url[:60]}')
    print(f'     이미지: {"있음" if img else "없음"}')
    
    # Add to Products DB
    ok, _, _, _ = add_product('틴트-처음-고르는-법', p, i+1)
    print(f'     DB 입력: {"✅" if ok else "❌"}')
