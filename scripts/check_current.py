import os, requests
env = {}
with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')) as f:
    for line in f:
        line = line.strip()
        if '=' in line:
            k, v = line.split('=', 1)
            env[k] = v
KEY = env.get('NOTION_API_KEY', '')
if not KEY: print("NO KEY"); exit(1)

PID = '367975d6-5268-81e8-9f62-c307d2378382'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}

# Check current blocks
r = requests.get(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, params={'page_size': 100})
d = r.json()
bs = d.get('results', [])
print(f"Blocks: {len(bs)}")
for b in bs[:3]:
    bt = b['type']
    if bt in ('paragraph', 'heading_2', 'heading_3'):
        txt = ''.join(t.get('plain_text','') for t in b[bt].get('rich_text',[]))
        print(f"  [{bt}] {txt[:60]}")
    else:
        print(f"  [{bt}]")
print(f"Has more: {d.get('has_more')}")
