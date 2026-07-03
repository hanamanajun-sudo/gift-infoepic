import os, requests
env = {}
with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')) as f:
    for line in f:
        line = line.strip()
        if '=' in line:
            k, v = line.split('=', 1)
            env[k] = v
KEY = env.get('NOTION_API_KEY', '')
PID = '367975d6-5268-81e8-9f62-c307d2378382'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28'}
r = requests.get(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, params={'page_size': 100})
d = r.json()
print(f"Total: {len(d.get('results',[]))}")
for b in d.get('results', []):
    bt = b['type']
    bid = b['id'][:25]
    if bt in ('paragraph','heading_2','heading_3'):
        txt = ''.join(t.get('plain_text','') for t in b[bt].get('rich_text',[]))
        print(f"  {bid} [{bt}] {txt[:50]}")
    elif bt == 'table':
        print(f"  {bid} [TABLE]")
    elif bt == 'table_row':
        cells = b.get('table_row',{}).get('cells',[])
        txt = '|'.join(c[0].get('text',{}).get('content','') if c else '' for c in cells[:3])
        print(f"  {bid} [TABLE_ROW] {txt[:50]}")
    else:
        print(f"  {bid} [{bt}]")
