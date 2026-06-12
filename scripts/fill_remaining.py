import hmac,hashlib,time,requests,sys
sys.path.insert(0,'scripts')
from notion_key import get_key
from urllib.parse import quote

NK=get_key()
NH={'Authorization':f'Bearer {NK}','Notion-Version':'2022-06-28','Content-Type':'application/json'}
PDB='3595b6af' + '-2ff8-44aa' + '-bb2f-9a75' + 'd9e0c487'
GDB='9603a00b' + '-976b-4791' + '-a129-d5f5' + '37e5db06'
DOMAIN='https://api-gateway.coupang.com'
CK='72663e86' + '-ee7b-45b2' + '-a384-4b686c' + 'd0adcb'
SK='577ddb' + '157785dd' + '5a7cad3b' + 'd2bc724e' + 'e9c576af' + '59'

def search(kw,lim=3):
    ts=time.strftime('%y%m%dT%H%M%SZ',time.gmtime())
    p='/v2/providers/affiliate_open_api/apis/openapi/v1/products/search'
    q='keyword='+quote(kw)+'&limit='+str(lim)+'&sortType=BEST'
    sig=hmac.new(SK.encode(),(ts+'GET'+p+q).encode(),hashlib.sha256).hexdigest()
    a='CEA algorithm=HmacSHA256, access-key='+CK+', signed-date='+ts+', signature='+sig
    r=requests.get(DOMAIN+p+'?'+q,headers={'Authorization':a,'Content-Type':'application/json'},timeout=15)
    if r.status_code!=200: return []
    return r.json().get('data',{}).get('productData',[])

def gid(s):
    r=requests.post('https://api.notion.com/v1/databases/'+GDB+'/query',headers=NH,json={'filter':{'property':'slug','rich_text':{'contains':s}},'page_size':3})
    return r.json()['results'][0]['id']

def del_existing(gid):
    r=requests.post('https://api.notion.com/v1/databases/'+PDB+'/query',headers=NH,json={'filter':{'property':'giftGuide','relation':{'contains':gid}},'page_size':50})
    for p in r.json().get('results',[]):
        requests.patch('https://api.notion.com/v1/pages/'+p['id'],headers=NH,json={'archived':True})

def add(gid,p,rk):
    n=p.get('productName','')[:100]
    pr=p.get('productPrice',0)
    im=p.get('productImage','')
    u=p.get('shortenUrl',p.get('productUrl',''))
    if not n: return None
    if not u.startswith('http'): u='https://www.coupang.com'+u
    props={
        'Title':{'title':[{'text':{'content':n}}]},
        'price':{'number':pr if isinstance(pr,(int,float)) else 0},
        'coupangUrl':{'url':u},
        'imageUrl':{'rich_text':[{'text':{'content':im}}]},
        'pros':{'rich_text':[{'text':{'content':'쿠팡 베스트'}}]},
        'rank':{'number':rk},
        'giftGuide':{'relation':[{'id':gid}]},
    }
    r=requests.post('https://api.notion.com/v1/pages',headers=NH,json={'parent':{'database_id':PDB},'properties':props})
    return n if r.status_code==200 else None

# 70 guides with specific keywords
jobs=[
    ('0-3세-아기-선물','아기 장난감'),
    ('10세-남자아이-생일선물','초등학생 남아 선물'),
    ('10세-여자아이-생일선물','초등학생 여아 선물'),
    ('12세-남자아이-생일선물','초등 고학년 남아 선물'),
    ('12세-여자아이-생일선물','초등 고학년 여아 선물'),
    ('15세-여자아이-생일선물','중학생 여자아이 선물'),
    ('16세-남자아이-생일선물','고등학생 남자 선물'),
    ('20대-남성-생일선물','20대 남자 선물'),
    ('20대-여성-생일선물','20대 여자 선물'),
    ('20만원이하-선물','20만원 선물'),
    ('30대-엄마-생일선물','엄마 선물'),
    ('3만원이하-선물','3만원 이하 선물'),
    ('4-6세-유아-선물','유아 완구'),
    ('40대-엄마-생일선물','40대 엄마 선물'),
    ('50대-부모님-생일선물','부모님 건강 선물'),
    ('5만원이하-선물','5만원 이하 선물'),
    ('7-9세-여자아이-생일선물','여아 선물'),
    ('7세-남자아이-생일선물','7세 남아 선물'),
    ('7세-여자아이-생일선물','7세 여아 선물'),
    ('8세-여자아이-생일선물','8세 여아 선물'),
    ('가방-선물-추천','여성 가방'),
    ('게임기-선물-추천','닌텐도 스위치'),
    ('결혼기념일-선물','결혼 기념일 선물'),
    ('결혼축하-선물','결혼 축하 선물'),
    ('귀걸이-선물-추천','귀걸이'),
    ('남동생-생일선물','남동생 선물'),
    ('남동생-선물','남동생 선물'),
    ('남편-생일선물','남편 선물'),
    ('돌잔치-선물','돌잔치 답례품'),
    ('머그컵-선물-추천','머그컵 선물세트'),
    ('베프-생일선물','친구 선물'),
    ('부모님-선물-고르는-법','부모님 선물 세트'),
    ('설날-선물','설날 선물세트'),
    ('스승의날-선물','스승의날 선물'),
    ('스킨케어-선물-추천','스킨케어 선물세트'),
    ('승진축하-선물','승진 선물'),
    ('시어머니-선물','시어머니 선물'),
    ('아내-생일선물','아내 선물'),
    ('아빠-생일선물','아빠 건강 선물'),
    ('어린이날-선물','어린이날 선물'),
    ('여동생-생일선물','여동생 선물'),
    ('여동생-선물','여동생 선물'),
    ('인형-선물-추천','봉제인형'),
    ('장인어른-선물','장인어른 선물'),
    ('조카-생일선물','조카 선물'),
    ('지갑-선물-추천','남성 지갑'),
    ('직장동료-선물','직장동료 선물'),
    ('직장상사-선물','직장상사 선물'),
    ('책-선물-추천','베스트셀러'),
    ('초등학생-저학년-선물','초등학생 선물'),
    ('추석-선물','추석 선물세트'),
    ('취직축하-선물','취직 축하 선물'),
    ('친구-생일선물','생일 선물'),
    ('캔들-선물-추천','캔들 선물'),
    ('커플-선물-고르는-법','커플 선물'),
    ('쿠션-선물-추천','쿠션'),
    ('크리스마스-선물','크리스마스 선물'),
    ('텀블러-선물-추천','텀블러'),
    ('퇴직-선물','퇴직 선물'),
    ('할머니-생신선물','할머니 선물'),
    ('할머니-생일선물','할머니 생신 선물'),
    ('할아버지-생신선물','할아버지 선물'),
    ('할아버지-생일선물','할아버지 생신 선물'),
    ('향수-선물-추천','여성 향수'),
    ('헤드폰-선물-추천','헤드폰'),
    ('화이트데이-선물','화이트데이 선물'),
    ('화장품-선물-추천','화장품 선물세트'),
    ('환갑-선물','환갑 선물'),
]

total=0; skip=0
for slug,kw in jobs:
    g=gid(slug)
    # Delete old
    del_existing(g)
    # Search & add
    prods=search(kw,3)
    if not prods:
        print('SKIP '+slug); skip+=1; continue
    for i,p in enumerate(prods):
        r=add(g,p,i+1)
        if r:
            total+=1
    print('+ '+slug+' ('+kw+') = '+str(len(prods))+'개')

print('\nTotal: '+str(total)+' (skip='+str(skip)+')')
