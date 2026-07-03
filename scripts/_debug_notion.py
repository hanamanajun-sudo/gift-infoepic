"""디버그: Python vs Node.js Notion API 차이"""
import os, json, urllib.request, ssl

with open(os.path.join(os.path.dirname(__file__), '..', '.env')) as f:
    for line in f:
        line = line.strip()
        if '=' in line and not line.startswith('#'):
            k, v = line.split('=', 1)
            os.environ[k.strip()] = v.strip().strip('"')

key = os.environ['NOTION_API_KEY']
db_id = os.environ['NOTION_GUIDES_DB_ID']

url = f'https://api.notion.com/v1/databases/{db_id}/query'
body = json.dumps({"filter": {"property": "slug", "rich_text": {"equals": "10세-남자아이-생일선물"}}}).encode()

# Test 1: Python with default SSL
req = urllib.request.Request(url, data=body, headers={
    'Authorization': f'Bearer {key}',
    'Notion-Version': '2022-06-28',
    'Content-Type': 'application/json',
    'User-Agent': 'Python/urllib'
}, method='POST')

ctx = ssl.create_default_context()
try:
    with urllib.request.urlopen(req, context=ctx) as resp:
        data = json.loads(resp.read())
        print(f"Python Test 1 (default SSL): {resp.status}")
        print(f"  Results: {len(data.get('results', []))}")
        if data.get('results'):
            print(f"  Page ID: {data['results'][0]['id']}")
except urllib.request.HTTPError as e:
    print(f"Python Test 1 (default SSL): HTTP {e.code}")
    print(f"  Body: {e.read().decode()[:200]}")

# Test 2: Same but with curl-style headers
req2 = urllib.request.Request(url, data=body, headers={
    'Authorization': f'Bearer {key}',
    'Notion-Version': '2022-06-28',
    'Content-Type': 'application/json',
}, method='POST')
try:
    with urllib.request.urlopen(req2, context=ctx) as resp:
        data = json.loads(resp.read())
        print(f"\nPython Test 2 (no UA): {resp.status}")
        print(f"  Results: {len(data.get('results', []))}")
except urllib.request.HTTPError as e:
    print(f"\nPython Test 2 (no UA): HTTP {e.code}")
    print(f"  Body: {e.read().decode()[:200]}")

# Test 3: The exact ID format
print(f"\nID format: '{db_id}' (len={len(db_id)})")
# Try with dashes
dashed_id = f"{db_id[:8]}-{db_id[8:12]}-{db_id[12:16]}-{db_id[16:20]}-{db_id[20:]}"
print(f"Dashed ID: '{dashed_id}' (len={len(dashed_id)})")
