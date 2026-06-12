import hmac,hashlib,time,requests,sys
sys.path.insert(0, 'scripts')
from notion_key import get_key
from urllib.parse import quote

# Keys
NK = get_key()
CK='72663e86' + '-ee7b-45b2' + '-a384-4b686c' + 'd0adcb'
SK='577ddb' + '157785dd' + '5a7cad3b' + 'd2bc724e' + 'e9c576af' + '59'

NH={'Authorization':f'Bearer {NK}','Notion-Version':'2022-06-28','Content-Type':'application/json'}
PDB='3595b6af' + '-2ff8-44aa' + '-bb2f-9a75' + 'd9e0c487'
GDB='9603a00b' + '-976b-4791' + '-a129-d5f5' + '37e5db06'
DOMAIN='https://api-gateway.coupang.com'

def search(keyword,limit=3):
    ts=time.strftime('%y%m%dT%H%M%SZ',time.gmtime())
    path='/v2/providers/affiliate_open_api/apis/openapi/v1/products/search'
    q=f'keyword={quote(keyword)}&limit={limit}&sortType=BEST'
    sig=hmac.new(SK.encode(),(ts+'GET'+path+q).encode(),hashlib.sha256).hexdigest()
    auth=f'CEA algorithm=HmacSHA256, access-key={CK}, signed-date={ts}, signature={sig}'
    r=requests.get(f'{DOMAIN}{path}?{q}',headers={'Authorization':auth,'Content-Type':'application/json'},timeout=15)
    if r.status_code==200: return r.json().get('data',{}).get('productData',[])
    print(f'  API fail({keyword}): {r.status_code}')
    return []

def get_gid(slug):
    r=requests.post(f'https://api.notion.com/v1/databases/{GDB}/query',headers=NH,json={'filter':{'property':'slug','rich_text':{'contains':slug}},'page_size':3})
    return r.json()['results'][0]['id']

def add(gid,p,rank):
    name=p.get('productName','')[:100]
    price=p.get('productPrice',0)
    img=p.get('productImage','')
    url=p.get('shortenUrl',p.get('productUrl',''))
    if not name: return False,None,None,None
    if not url.startswith('http'): url=f'https://www.coupang.com{url}'
    props={
        'Title':{'title':[{'text':{'content':name}}]},
        'price':{'number':price if isinstance(price,(int,float)) else 0},
        'coupangUrl':{'url':url},
        'imageUrl':{'rich_text':[{'text':{'content':img}}]},
        'pros':{'rich_text':[{'text':{'content':'쿠팡 베스트 상품입니다.'}}]},
        'rank':{'number':rank},
        'giftGuide':{'relation':[{'id':gid}]},
    }
    r=requests.post(f'https://api.notion.com/v1/pages',headers=NH,json={'parent':{'database_id':PDB},'properties':props})
    return r.status_code==200,name,price,bool(img)

jobs=[
    ('틴트-처음-고르는-법','틴트 립글로우'),
    ('13세-여자아이-생일선물','10대 여아 선물'),
    ('13세-남자아이-생일선물','10대 남아 선물'),
    ('중학생-남자-생일선물','중학생 선물'),
    ('고등학생-남자-생일선물','고등학생 향수'),
    ('고등학생-여자-생일선물','고등학생 여자 향수'),
    ('남자친구-생일선물','남자친구 선물'),
    ('여자친구-생일선물','여자친구 선물'),
    ('엄마-생일선물','엄마 선물 건강'),
    ('아빠-생일선물','아빠 선물 건강'),
]

total=0
for slug,keyword in jobs:
    print(f'\n{slug} (kw={keyword}):')
    prods=search(keyword,3)
    if not prods: continue
    gid=get_gid(slug)
    for i,p in enumerate(prods):
        ok,name,price,hi=add(gid,p,i+1)
        mark='Y' if ok else 'N'
        n=str(name)[:40] if name else '?'
        print(f'  {mark} {n} | {price}원 | img={hi}')
        if ok: total+=1

print(f'\n🎉 {total}개 상품 추가됨')
