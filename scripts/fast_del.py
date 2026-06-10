import os, requests, sys
sys.path.insert(0, os.path.dirname(__file__))
from notion_key import get_key

KEY = get_key()
PID = '367975d6-5268-81e8-9f62-c307d2378382'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28'}

ids = []
cur = None
while True:
    p = {'page_size': 100}
    if cur: p['start_cursor'] = cur
    r = requests.get(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, params=p)
    d = r.json()
    ids.extend(b['id'] for b in d.get('results', []))
    if not d.get('has_more'): break
    cur = d.get('next_cursor')

print(f'{len(ids)} blocks')
for bid in ids:
    requests.delete(f'https://api.notion.com/v1/blocks/{bid}', headers=H)
print('Deleted')
