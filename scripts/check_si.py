import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

KEY = get_key()
PID = '367975d6-5268-81ab-8024-e8adbeddb137'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28'}

r = requests.get(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, params={'page_size': 5})
bs = r.json().get('results', [])
print(f'{len(bs)} blocks remain')
for b in bs[:3]:
    t = b['type']
    if t in ('paragraph','heading_2','heading_3'):
        txt = ''.join(x.get('plain_text','') for x in b[t].get('rich_text',[]))
        print(f'  {txt[:60]}')
    else:
        print(f'  [{t}]')
