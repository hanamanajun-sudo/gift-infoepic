import requests, time, hmac, hashlib, uuid, json

ACCESS_KEY = '72663e86-ee7b-45b2-a384-4b686cd0adcb'
SECRET_KEY = '577ddb157785dd5a7cad3bd2bc724ee9c576af59'
BASE_URL = 'https://api-gateway.coupang.com'

def coupang_request(method, path, query=''):
    timestamp = str(int(time.time() * 1000))
    request_id = str(uuid.uuid4())
    
    full_path = path + ('?' + query if query else '')
    message = method + ' ' + full_path + '\n' + timestamp + '\n' + request_id
    
    signature = hmac.new(
        SECRET_KEY.encode('utf-8'),
        message.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()
    
    headers = {
        'Authorization': f'HMAC-SHA256 apiKey={ACCESS_KEY}, signedDate={timestamp}, signature={signature}',
        'Content-Type': 'application/json'
    }
    
    url = BASE_URL + full_path
    r = requests.get(url, headers=headers, timeout=15)
    return r

# Test 1: Simple product search
print('=== Test 1: 상품 검색 (립글로우) ===')
r = coupang_request('GET', '/v2/providers/affiliate_open_api/apis/openapi/products/search', 'keyword=립글로우&limit=3')
print(f'Status: {r.status_code}')
if r.status_code == 200:
    data = r.json()
    print(json.dumps(data, indent=2, ensure_ascii=False)[:2000])
else:
    print(f'Error: {r.text[:500]}')

print()

# Test 2: Try different endpoint
print('=== Test 2: 베스트 상품 ===')
r2 = coupang_request('GET', '/v2/providers/affiliate_open_api/apis/openapi/products/bestcategories', 'categoryId=100&limit=3')
print(f'Status: {r2.status_code}')
if r2.status_code == 200:
    print(json.dumps(r2.json(), indent=2, ensure_ascii=False)[:500])
else:
    print(f'Error: {r2.text[:300]}')

print()
print('=== Test 3: 대량 URL 생성 ===')
# Test with a known product ID - try a simple approach
r3 = coupang_request('GET', '/v2/providers/affiliate_open_api/apis/openapi/deeplink', 'coupangUrl=https://www.coupang.com/vp/products/80602959')
print(f'Status: {r3.status_code}')
if r3.status_code == 200:
    print(json.dumps(r3.json(), indent=2, ensure_ascii=False)[:500])
else:
    print(f'Error: {r3.text[:300]}')
