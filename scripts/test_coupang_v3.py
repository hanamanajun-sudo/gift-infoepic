import requests, time, hmac, hashlib, uuid, json

ACCESS_KEY = '72663e86-ee7b-45b2-a384-4b686cd0adcb'
SECRET_KEY='577ddb...af59'
BASE = 'https://api-gateway.coupang.com'

# Try different HMAC formats
def try_api(name, method, path, query='', body=None, use_uri_encoded=False, sig_uppercase=False):
    timestamp = str(int(time.time() * 1000))
    request_id = str(uuid.uuid4())
    
    url_path = path + ('?' + query if query else '')
    
    # Try: method + ' ' + path + '\n' + timestamp + '\n' + request_id
    message = f'{method} {url_path}\n{timestamp}\n{request_id}'
    
    sig = hmac.new(
        SECRET_KEY.encode('utf-8'),
        message.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()
    
    if sig_uppercase:
        sig = sig.upper()
    
    auth = f'HMAC-SHA256 apiKey={ACCESS_KEY}, signedDate={timestamp}, signature={sig}'
    headers = {
        'Authorization': auth,
        'Content-Type': 'application/json',
        'X-Request-Id': request_id,
    }
    
    url = BASE + url_path
    
    try:
        if method == 'GET':
            r = requests.get(url, headers=headers, timeout=10)
        else:
            r = requests.post(url, headers=headers, json=body, timeout=10)
        print(f'{name}: {r.status_code}')
        if r.status_code == 200:
            print(f'  ✅ SUCCESS!')
            print(json.dumps(r.json(), indent=2, ensure_ascii=False)[:500])
            return True
        else:
            # Don't print full error, just status
            pass
    except Exception as e:
        print(f'{name}: EXCEPTION {e}')
    return False

# Try many different formats
found = False

# Format 1: Standard
found = try_api('1. Standard GET', 'GET', '/v2/providers/affiliate_open_api/apis/openapi/products/search', 'keyword=립글로우&limit=3') or found

# Wait a bit for rate limits
time.sleep(1)

# Format 2: Uppercase signature
found = try_api('2. Uppercase sig', 'GET', '/v2/providers/affiliate_open_api/apis/openapi/products/search', 'keyword=립글로우&limit=3', sig_uppercase=True) or found

time.sleep(1)

# Format 3: Post deeplink with standard format
found = try_api('3. POST deeplink', 'POST', '/v2/providers/affiliate_open_api/apis/openapi/deeplink', 
                body={'coupangUrls': ['https://www.coupang.com/vp/products/80602959']}) or found

time.sleep(1)

# Format 4: Alternative API path format
found = try_api('4. Alt path', 'GET', '/v2/providers/affiliate_open_api/apis/openapi/products/search', 'keyword=립글로우&limit=1') or found

if not found:
    print('\n❌ 모든 형식 실패')
    print('키가 발급된 후 활성화에 시간이 필요할 수 있습니다.')
    print('또는 파트너스 > API 연동 관리에서 IP 허용이 필요할 수 있습니다.')
