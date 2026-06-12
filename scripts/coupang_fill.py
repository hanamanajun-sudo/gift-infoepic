import hmac,hashlib,time,requests,os
from urllib.parse import quote

NK=os.environ['NOTION_KEY']
NH={'Authorization':f'Bearer {NK}','Notion-Version':'2022-06-28','Content-Type':'application/json'}
PDB='3595b6af-2ff8-44aa-bb2f-9a75d9e0c487'
GDB='9603a00b-976b-4791-a129-d5f537e5db06'

CK='72663e86-ee7b-45b2-a384-4b686cd0adcb'
SK=os.environ['COUPANG_SECRET_KEY']
DOMAIN='https://api-gateway.coupang.com'

def search(keyword,limit=3):
    ts=time.strftime('%y%m%dT%H%M%SZ',time.gmtime())
    path='/v2/providers/affiliate_open_api/apis/openapi/v1/products/search'
    q=f'keyword={quote(keyword)}&limit={limit}&sortType=BEST'
    msg=ts+'GET'+path+q
    sig=hmac.new(SK.encode(),msg.encode(),hashlib.sha256).hexdigest()
    auth=f'CEA algorithm=HmacSHA256, access-key={CK}, signed-date={ts}, signature={sig}'
    r=requests.get(f'{DOMAIN}{path}?{q}',headers={'Authorization':auth},timeout=15)
    if r.status_code==200: return r.json().get('data',{}).get('productData',[])
    return []

def get_gid(slug):
    r=requests.post(f'https://api.notion.com/v1/databases/{GDB}/query',headers=NH,json={'filter':{'property':'slug','rich_text':{'contains':slug}},'page_size':3})
    return r.json()['results'][0]['id']

def add(gid,p,rank):
    name=p.get('productName','')[:100]
    price=p.get('productPrice',0)
    img=p.get('productImage','')
    url=p.get('shortenUrl',p.get('productUrl',''))
    if not name: return False,'no name'
    if not (url.startswith('http')): url=f'https://www.coupang.com{url}'
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
    return r.status_code==200,name,price

# Fill for tint guide
print('=== 틴트 가이드 상품 채우기 ===')
prods=search('어뮤즈 립틴트',3)
if prods:
    gid=get_gid('틴트-처음-고르는-법')
    for i,p in enumerate(prods):
        ok,name,price=add(gid,p,i+1)
        print(f'  {"✅" if ok else "❌"} {name} ({price}원) img={bool(p.get("productImage",""))}')
else:
    print('검색 결과 없음')
