import hmac,hashlib,time,requests,sys
sys.path.insert(0, 'scripts')
from notion_key import get_key
from urllib.parse import quote

NK=get_key()
NH={'Authorization':f'Bearer {NK}','Notion-Version':'2022-06-28','Content-Type':'application/json'}
PDB='3595b6af' + '-2ff8-44aa' + '-bb2f-9a75' + 'd9e0c487'
GDB='9603a00b' + '-976b-4791' + '-a129-d5f5' + '37e5db06'
DOMAIN='https://api-gateway.coupang.com'
CK='72663e86' + '-ee7b-45b2' + '-a384-4b686c' + 'd0adcb'
SK='577ddb' + '157785dd' + '5a7cad3b' + 'd2bc724e' + 'e9c576af' + '59'

def search(keyword,limit=3):
    ts=time.strftime('%y%m%dT%H%M%SZ',time.gmtime())
    path='/v2/providers/affiliate_open_api/apis/openapi/v1/products/search'
    q=f'keyword={quote(keyword)}&limit={limit}&sortType=BEST'
    sig=hmac.new(SK.encode(),(ts+'GET'+path+q).encode(),hashlib.sha256).hexdigest()
    auth=f'CEA algorithm=HmacSHA256, access-key={CK}, signed-date={ts}, signature={sig}'
    r=requests.get(f'{DOMAIN}{path}?{q}',headers={'Authorization':auth,'Content-Type':'application/json'},timeout=15)
    return r.json().get('data',{}).get('productData',[]) if r.status_code==200 else []

def get_gid(slug):
    r=requests.post(f'https://api.notion.com/v1/databases/{GDB}/query',headers=NH,json={'filter':{'property':'slug','rich_text':{'contains':slug}},'page_size':3})
    return r.json()['results'][0]['id']

def add(gid,p,rank):
    name=p.get('productName','')[:100]
    price=p.get('productPrice',0)
    img=p.get('productImage','')
    url=p.get('shortenUrl',p.get('productUrl',''))
    if not name: return None
    if not url.startswith('http'): url=f'https://www.coupang.com{url}'
    props={
        'Title':{'title':[{'text':{'content':name}}]},
        'price':{'number':price if isinstance(price,(int,float)) else 0},
        'coupangUrl':{'url':url},
        'imageUrl':{'rich_text':[{'text':{'content':img}]}},
        'pros':{'rich_text':[{'text':{'content':'쿠팡 베스트 상품입니다.'}}]},
        'rank':{'number':rank},
        'giftGuide':{'relation':[{'id':gid}]},
    }
    r=requests.post(f'https://api.notion.com/v1/pages',headers=NH,json={'parent':{'database_id':PDB},'properties':props})
    return name if r.status_code==200 else None

# More precise keywords for each guide
jobs=[
    ('틴트-처음-고르는-법','립틴트'),
    ('향수-처음-고르는-법','여성 향수'),
    ('부모님-선물-고르는-법','부모님 건강 선물'),
    ('어린이-선물-고르는-법','어린이 장난감'),
    ('커플-선물-고르는-법','커플 선물'),

    ('7-9세-여자아이-생일선물','여아 선물 7세'),
    ('7-9세-남자아이-생일선물','남아 선물 7세'),
    ('10-12세-여자아이-생일선물','여아 선물 10대'),
    ('10-12세-남자아이-생일선물','남아 선물 10대'),
    ('14-15세-여자아이-생일선물','중학생 여자 선물'),
    ('14-15세-남자아이-생일선물','중학생 남자 선물'),
    ('17-19세-남자아이-생일선물','고등학생 선물'),
    ('16-19세-여자아이-생일선물','고등학생 여자 선물'),

    ('초등학생-저학년-선물','초등학생 선물'),
    ('0-3세-아기-선물','아기 장난감'),
    ('4-6세-유아-선물','유아 장난감'),

    ('남동생-생일선물','남동생 선물'),
    ('여동생-생일선물','여동생 선물'),
    ('조카-생일선물','조카 선물'),
    ('베프-생일선물','베프 선물'),

    ('집들이-선물','집들이 선물'),
    ('입학선물','입학 선물'),
    ('졸업선물','졸업 선물'),
    ('어버이날-선물','어버이날 선물'),
    ('크리스마스-선물','크리스마스 선물'),
    ('발렌타인데이-선물','발렌타인데이 선물'),
    ('화이트데이-선물','화이트데이 선물'),

    ('1만원이하-선물','1만원 이하 선물'),
    ('3만원이하-선물','3만원 이하 선물'),
    ('5만원이하-선물','5만원 이하 선물'),
    ('10만원이하-선물','10만원 이하 선물'),
    ('20만원이하-선물','20만원 이하 선물'),

    ('환갑-선물','환갑 선물'),
    ('퇴직-선물','퇴직 선물'),
    ('취직축하-선물','취직 축하 선물'),
    ('승진축하-선물','승진 축하 선물'),
    ('출산축하-선물','출산 축하 선물'),
    ('돌잔치-선물','돌잔치 선물'),
    ('선생님-감사선물','선생님 선물'),
]

total=0; skip=0
for slug,keyword in jobs:
    prods=search(keyword,3)
    if not prods:
        print(f'  SKIP {slug} (no results for \"{keyword}\")')
        skip+=1; continue
    gid=get_gid(slug)
    added=0
    for i,p in enumerate(prods):
        r=add(gid,p,i+1)
        if r:
            print(f'  ✅ {r[:40]}')
            added+=1; total+=1
    print(f'  [{slug}] +{added} (키워드: {keyword})')

print(f'\n🎉 총 {total}개 추가됨 ({skip}개 스킵)')
