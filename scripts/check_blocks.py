import os, requests

with open('.env') as f:
    for line in f:
        line = line.strip()
        if line.startswith('NOTION_API_KEY='):
            key = line.split('=', 1)[1].strip()
            break

PAGE_ID = '367975d6-5268-81e8-9f62-c307d2378382'
headers = {
    'Authorization': f'Bearer {key}',
    'Notion-Version': '2022-06-28',
    'Content-Type': 'application/json',
}

# Check current blocks state
r = requests.get(
    f'https://api.notion.com/v1/blocks/{PAGE_ID}/children',
    headers=headers,
    params={'page_size': 20}
)
data = r.json()
results = data.get('results', [])
print(f'Current blocks (first page): {len(results)}')
for b in results[:10]:
    bt = b['type']
    if bt in ('paragraph', 'heading_2', 'heading_3', 'heading_4'):
        texts = [t.get('plain_text','') for t in b[bt].get('rich_text', [])]
        print(f'  [{bt}] {"".join(texts)[:80]}')
    elif bt == 'table_row':
        print(f'  [table_row]')
    elif bt == 'table':
        print(f'  [table]')
    else:
        print(f'  [{bt}]')

print(f'Has more: {data.get("has_more")}')
