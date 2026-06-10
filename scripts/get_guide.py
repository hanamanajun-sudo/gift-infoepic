"""Fetch current Notion guide content for 13세-여자아이-생일선물"""
import os, json, requests

# Read API key from .env
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
with open(env_path) as f:
    for line in f:
        line = line.strip()
        if line.startswith('NOTION_API_KEY='):
            NOTION_API_KEY = line.split('=', 1)[1]
            break

if not NOTION_API_KEY:
    print("NO KEY")
    exit(1)

NOTION_GUIDES_DB_ID = '9603a00b-976b-4791-a129-d5f537e5db06'
headers = {
    'Authorization': f'Bearer {NOTION_API_KEY}',
    'Notion-Version': '2022-06-28',
    'Content-Type': 'application/json',
}

# Find guide by slug
resp = requests.post(
    f'https://api.notion.com/v1/databases/{NOTION_GUIDES_DB_ID}/query',
    headers=headers,
    json={
        'filter': {
            'property': 'slug',
            'rich_text': {'equals': '13세-여자아이-생일선물'}
        }
    }
)
data = resp.json()
results = data.get('results', [])
if not results:
    print('No results found')
    print(json.dumps(data, indent=2, ensure_ascii=False)[:2000])
    exit(1)

page = results[0]
page_id = page['id']
props = page['properties']
print(f"Page ID: {page_id}")
print(f"Title: {props['Title']['title'][0]['plain_text']}")
print(f"Slug: {props['slug']['rich_text'][0]['plain_text']}")
intro_text = props.get('intro', {}).get('rich_text', [{}])[0].get('plain_text', '')[:200]
print(f"Intro: {intro_text}")
print()

# Fetch all blocks with pagination
all_blocks = []
cursor = None
while True:
    params = {'page_size': 100}
    if cursor:
        params['start_cursor'] = cursor
    blocks_resp = requests.get(
        f'https://api.notion.com/v1/blocks/{page_id}/children',
        headers=headers, params=params
    )
    blocks_data = blocks_resp.json()
    all_blocks.extend(blocks_data.get('results', []))
    if not blocks_data.get('has_more'):
        break
    cursor = blocks_data.get('next_cursor')

print(f"Total blocks: {len(all_blocks)}")
print(f"{'='*70}")
for i, block in enumerate(all_blocks):
    btype = block['type']
    if btype in ('paragraph', 'heading_2', 'heading_3', 'heading_4', 'heading_1'):
        texts = [t.get('plain_text','') for t in block[btype].get('rich_text', [])]
        text = ''.join(texts)
        if 'heading_2' in btype:
            marker = '[H2]'
        elif 'heading_3' in btype:
            marker = '[H3]'
        elif 'heading_1' in btype:
            marker = '[H1]'
        elif 'heading_4' in btype:
            marker = '[H4]'
        else:
            marker = '[P]'
        print(f"{i+1:03d} {marker} {text[:180]}")
    elif btype in ('bulleted_list_item', 'numbered_list_item'):
        texts = [t.get('plain_text','') for t in block[btype].get('rich_text', [])]
        text = ''.join(texts)
        if 'bulleted' in btype:
            prefix = '  *'
        else:
            prefix = '  1.'
        print(f"{i+1:03d} {prefix} {text[:180]}")
    elif btype == 'divider':
        print(f"{i+1:03d} [---divider---]")
    elif btype == 'quote':
        texts = [t.get('plain_text','') for t in block[btype].get('rich_text', [])]
        print(f"{i+1:03d} [Q] {''.join(texts)[:180]}")
    elif btype == 'image':
        print(f"{i+1:03d} [IMAGE]")
    elif btype == 'callout':
        texts = [t.get('plain_text','') for t in block[btype].get('rich_text', [])]
        print(f"{i+1:03d} [CALLOUT] {''.join(texts)[:180]}")
    else:
        print(f"{i+1:03d} [{btype}]")

print(f"\nPage ID for update: {page_id}")
