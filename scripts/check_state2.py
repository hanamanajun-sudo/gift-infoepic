"""Quick check of current Notion block state"""
import os, requests, sys
sys.path.insert(0, os.path.dirname(__file__))
from notion_key import get_key

KEY = get_key()
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28'}
PID = '367975d6-5268-81e8-9f62-c307d2378382'

r = requests.get(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, params={'page_size': 5})
d = r.json()
bs = d.get('results', [])
print(f'{len(bs)} blocks')
for b in bs[:5]:
    t = b['type']
    if t in ('paragraph','heading_2','heading_3'):
        txt = ''.join(x.get('plain_text','') for x in b[t].get('rich_text',[]))
        print(f'  [{t}] {txt[:80]}')
    else:
        print(f'  [{t}]')
