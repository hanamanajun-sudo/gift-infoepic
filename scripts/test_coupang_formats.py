import requests, time, hmac, hashlib, json
from urllib.parse import quote

ACCESS_KEY='72663e86-ee7b-45b2-a384-4b686cd0adcb'
SECRET_KEY='***'
DOMAIN = 'https://api-gateway.coupang.com'

def test_format(name, msg_fn, auth_fn):
    ts = time.strftime('%y%m%dT%H%M%SZ', time.gmtime())
    method = 'GET'
    path = '/v2/providers/affiliate_open_api/apis/openapi/v1/products/search'
    query = f'keyword={quote("립글로우")}&limit=1&sortType=BEST'
    
    msg = msg_fn(ts, method, path, query)
    sig = hmac.new(SECRET_KEY.encode(), msg.encode(), hashlib.sha256).hexdigest()
    auth = auth_fn(ts, ACCESS_KEY, sig)
    
    url = f'{DOMAIN}{path}?{query}'
    r = requests.get(url, headers={'Authorization': auth, 'Content-Type': 'application/json'}, timeout=10)
    if r.status_code == 200:
        print(f'✅ {name}: SUCCESS!')
        print(json.dumps(r.json(), indent=2, ensure_ascii=False)[:300])
        return True
    else:
        err = r.json().get('message','')
        print(f'  {name}: {r.status_code} — {err}')
        return False

tests = [
    # Format 1: ts+method+path+query (no ? in query)
    ('1. ts+method+path+query', 
     lambda ts,m,p,q: ts+m+p+q,
     lambda ts,k,s: f'CEA algorithm=HmacSHA256, access-key={k}, signed-date={ts}, signature={s}'),
    
    # Format 2: method+path+query+ts
    ('2. method+path+query+ts', 
     lambda ts,m,p,q: m+p+q+ts,
     lambda ts,k,s: f'CEA algorithm=HmacSHA256, access-key={k}, signed-date={ts}, signature={s}'),
    
    # Format 3: ts+method+path+?query (with ?)
    ('3. ts+method+path+?query', 
     lambda ts,m,p,q: ts+m+p+'?'+q,
     lambda ts,k,s: f'CEA algorithm=HmacSHA256, access-key={k}, signed-date={ts}, signature={s}'),
    
    # Format 4: Try different auth header format (lowercase)
    ('4. lowercase auth', 
     lambda ts,m,p,q: ts+m+p+q,
     lambda ts,k,s: f'CEA algorithm=HmacSHA256, access-key={k}, signed-date={ts}, signature={s}'),
]

for name, msg_fn, auth_fn in tests:
    if test_format(name, msg_fn, auth_fn):
        break
    time.sleep(0.5)
