"""Count remaining blocks and check content"""
import os, requests, sys
sys.path.insert(0, os.path.dirname(__file__))
from notion_key import get_key

KEY = get_key()
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28'}
PID = '367975d6-5268-81e8-9f62-c307d2378382'

total = 0
cursor = None
first_heading = None
last_heading = None

while True:
    params = {'page_size': 100}
    if cursor: params['start_cursor'] = cursor
    r = requests.get(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, params=params)
    d = r.json()
    blocks = d.get('results', [])
    for b in blocks:
        total += 1
        t = b['type']
        if t in ('heading_2',):
            txt = ''.join(x.get('plain_text','') for x in b[t].get('rich_text',[]))
            if not first_heading: first_heading = txt
            last_heading = txt
    if not d.get('has_more'): break
    cursor = d.get('next_cursor')

print(f'Total blocks: {total}')
print(f'First H2: {first_heading}')
print(f'Last H2: {last_heading}')
