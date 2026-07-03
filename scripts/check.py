import requests, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from notion_key import get_key

KEY = get_key()
PID = '367975d6-5268-81e8-9f62-c307d2378382'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28'}

r = requests.get(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, params={'page_size': 5})
d = r.json()
print(f'{len(d.get("results",[]))} blocks')
for b in d['results'][:5]:
    t = b['type']
    if t in ('paragraph', 'heading_2', 'heading_3'):
        txt = ''.join(x.get('plain_text','') for x in b[t].get('rich_text',[]))
        print(f'  {txt[:80]}')
    else:
        print(f'  [{t}]')
