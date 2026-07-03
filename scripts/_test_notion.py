"""Notion DB 연결 테스트"""
import os, json, sys

# Read .env
with open(os.path.join(os.path.dirname(__file__), '..', '.env')) as f:
    for line in f:
        line = line.strip()
        if '=' in line and not line.startswith('#'):
            k, v = line.split('=', 1)
            os.environ[k.strip()] = v.strip().strip('"')

key = os.environ.get('NOTION_API_KEY', '')
guides_db = os.environ.get('NOTION_GUIDES_DB_ID', '')
products_db = os.environ.get('NOTION_PRODUCTS_DB_ID', '')

print(f"API Key prefix: {key[:10]}...")
print(f"Guides DB: {guides_db}")
print(f"Products DB: {products_db}")

# Test: query the guides database with slug filter
import urllib.request

url = f"https://api.notion.com/v1/databases/{guides_db}/query"
headers = {
    'Authorization': f'Bearer {key}',
    'Notion-Version': '2022-06-28',
    'Content-Type': 'application/json'
}
body = json.dumps({
    "filter": {
        "property": "slug",
        "rich_text": {"equals": "10세-남자아이-생일선물"}
    }
}).encode()

req = urllib.request.Request(url, data=body, headers=headers, method='POST')
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read())
        results = data.get('results', [])
        print(f"\nFound {len(results)} guide(s) with slug '10세-남자아이-생일선물'")
        if results:
            r = results[0]
            print(f"Page ID: {r['id']}")
            props = r.get('properties', {})
            for k, v in props.items():
                title_val = ''
                if v.get('type') == 'title':
                    title_val = v.get('title', [{}])[0].get('plain_text', '')
                print(f"  {k}: {v.get('type')} = {title_val}")
except urllib.request.HTTPError as e:
    print(f"\nHTTP Error {e.code}: {e.read().decode()}")
except Exception as e:
    print(f"\nError: {e}")
