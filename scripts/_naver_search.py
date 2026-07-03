"""네이버 쇼핑 검색 API 헬퍼"""
import json, os, re, urllib.request, sys

# Read .env from project root
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path = os.path.join(project_root, '.env')
env = {}
with open(env_path) as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('#') and '=' in line:
            k, v = line.split('=', 1)
            env[k.strip()] = v.strip().strip('"')

client_id = env.get('NAVER_CLIENT_ID')
client_secret = env.get('NAVER_CLIENT_SECRET')

def search_shop(query, display=3):
    encoded = urllib.parse.quote(query)
    url = f"https://openapi.naver.com/v1/search/shop.json?query={encoded}&display={display}&sort=sim"
    req = urllib.request.Request(url)
    req.add_header('X-Naver-Client-Id', client_id)
    req.add_header('X-Naver-Client-Secret', client_secret)
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read())
    results = []
    for item in data.get('items', [])[:display]:
        title = re.sub(r'<[^>]+>', '', item['title'])
        results.append({
            'title': title,
            'price': item['lprice'],
            'link': item['link'],
            'image': item['image'],
            'mall': item['mallName']
        })
    return results

if __name__ == '__main__':
    query = sys.argv[1]
    results = search_shop(query)
    for r in results:
        title_clean = r['title'].replace('<b>', '').replace('</b>', '')
        print(f"상품명: {title_clean}")
        print(f"가격: {int(r['price']):,}원")
        print(f"링크: {r['link']}")
        print(f"이미지: {r['image']}")
        print(f"쇼핑몰: {r['mall']}")
        print()
