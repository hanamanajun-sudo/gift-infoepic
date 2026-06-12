import requests, time, hmac, hashlib, uuid, json

ACCESS_KEY = '72663e86-ee7b-45b2-a384-4b686cd0adcb'
SECRET_KEY='577ddb...af59'
BASE = 'https://api-gateway.coupang.com'

def generate_signature(method, path, query=''):
    timestamp = str(int(time.time() * 1000))
    request_id = str(uuid.uuid4())
    url_path = path + ('?' + query if query else '')
    message = f'{method} {url_path}\n{timestamp}\n{request_id}'
    sig = hmac.new(
        SECRET_KEY.encode('utf-8'),
        message.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()
    return timestamp, request_id, sig

def coupang_get(path, query=''):
    ts, rid, sig = generate_signature('GET', path, query)
    headers = {
        'Authorization': f'HMAC-SHA256 apiKey={ACCESS_KEY}, signedDate={ts}, signature={sig}',
        'Content-Type': 'application/json;charset=UTF-8'
    }
    url = BASE + path + ('?' + query if query else '')
    r = requests.get(url, headers=headers, timeout=15)
    return r

def coupang_post(path, body=None):
    ts, rid, sig = generate_signature('POST', path)
    headers = {
        'Authorization': f'HMAC-SHA256 apiKey={ACCESS_KEY}, signedDate={ts}, signature={sig}',
        'Content-Type': 'application/json;charset=UTF-8'
    }
    url = BASE + path
    r = requests.post(url, headers=headers, json=body, timeout=15)
    return r

# Test 1: Search products
print('=== 1. 상품 검색 ===')
r = coupang_get('/v2/providers/affiliate_open_api/apis/openapi/products/search', 'keyword=립글로우&limit=3')
print(f'Status: {r.status_code}')
if r.status_code == 200:
    print(json.dumps(r.json(), indent=2, ensure_ascii=False)[:1500])
else:
    print(r.text[:500])

# Test 2: Deep link (POST) - convert a regular coupang URL to affiliate link
print('\n=== 2. 딥링크 생성 (POST) ===')
r2 = coupang_post('/v2/providers/affiliate_open_api/apis/openapi/deeplink', {
    'coupangUrls': ['https://www.coupang.com/vp/products/80602959']
})
print(f'Status: {r2.status_code}')
if r2.status_code == 200:
    print(json.dumps(r2.json(), indent=2, ensure_ascii=False)[:1000])
else:
    print(r2.text[:500])
