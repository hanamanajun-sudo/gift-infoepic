import requests, time, hmac, hashlib, json
from urllib.parse import quote

ACCESS_KEY='72663e86-ee7b-45b2-a384-4b686cd0adcb'
SECRET_KEY='577ddb...af59'
DOMAIN = 'https://api-gateway.coupang.com'

def generate_timestamp():
    return time.strftime('%y%m%dT%H%M%SZ', time.gmtime())

def generate_hmac(method, path, query, secret_key, access_key):
    ts = generate_timestamp()
    msg = ts + method + path + (query if query else '')
    signature = hmac.new(secret_key.encode(), msg.encode(), hashlib.sha256).hexdigest()
    auth = f'CEA algorithm=HmacSHA256, access-key={access_key}, signed-date={ts}, signature={signature}'
    return auth

# Test 1: Product search (correct format)
keyword = '립글로우'
encoded = quote(keyword)
path = '/v2/providers/affiliate_open_api/apis/openapi/v1/products/search'
query = f'keyword={encoded}&limit=3&sortType=BEST'
auth = generate_hmac('GET', path, query, SECRET_KEY, ACCESS_KEY)
headers = {'Authorization': auth, 'Content-Type': 'application/json'}
url = f'{DOMAIN}{path}?{query}'

print('=== Test 1: 상품 검색 ===')
print(f'URL: {url}')
r = requests.get(url, headers=headers, timeout=15)
print(f'Status: {r.status_code}')
if r.status_code == 200:
    print('✅ SUCCESS!')
    data = r.json()
    products = data.get('data', {}).get('productData', [])
    for p in products[:3]:
        name = p.get('productName','?')
        price = p.get('productPrice','?')
        img = p.get('productImage','')
        url = p.get('productUrl','')
        print(f'  - {name} | {price}원')
        print(f'    이미지: {img[:80] if img else "없음"}')
        print(f'    쿠팡: {url[:60] if url else "없음"}')
else:
    print(f'Error: {r.text[:500]}')

# Test 2: Deep link
print('\n=== Test 2: 딥링크 생성 ===')
import uuid
ts = generate_timestamp()
# For POST, the message format might be different
# Let's try with the deeplink endpoint
body_json = json.dumps({'coupangUrls': ['https://www.coupang.com/vp/products/80602959']})
path2 = '/v2/providers/affiliate_open_api/apis/openapi/v1/deeplink'
auth2 = generate_hmac('POST', path2, '', SECRET_KEY, ACCESS_KEY)
headers2 = {'Authorization': auth2, 'Content-Type': 'application/json'}
r2 = requests.post(f'{DOMAIN}{path2}', headers=headers2, json={'coupangUrls': ['https://www.coupang.com/vp/products/80602959']}, timeout=15)
print(f'Status: {r2.status_code}')
if r2.status_code == 200:
    print('✅ SUCCESS!')
    print(json.dumps(r2.json(), indent=2, ensure_ascii=False)[:500])
else:
    print(f'Error: {r2.text[:300]}')
