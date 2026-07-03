"""Check Notion page state after rewrite attempt"""
import os, requests

env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
with open(env_path, encoding='utf-8') as f:
    raw = f.read()

secret = ''
for line in raw.splitlines():
    if line.startswith('NOTION_API_KEY='):
        secret = line.split('=', 1)[1].strip()
        break

PAGE_ID = '367975d6-5268-81e8-9f62-c307d2378382'
headers = {
    'Authorization': f'Bearer {secret}',
    'Notion-Version': '2022-06-28',
    'Content-Type': 'application/json',
}

r = requests.get(f'https://api.notion.com/v1/pages/{PAGE_ID}', headers=headers)
data = r.json()
props = data.get('properties', {})
intro_rich = props.get('intro', {}).get('rich_text', [])
if intro_rich:
    print(f"Intro: {intro_rich[0].get('plain_text', '')[:100]}")
else:
    print("Intro: EMPTY")

r2 = requests.get(
    f'https://api.notion.com/v1/blocks/{PAGE_ID}/children',
    headers=headers,
    params={'page_size': 5}
)
blocks = r2.json().get('results', [])
print(f"Blocks remaining: {len(blocks)}")
