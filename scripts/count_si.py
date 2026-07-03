import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

KEY = get_key()
PID = '367975d6-5268-81ab-8024-e8adbeddb137'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28'}

r = requests.get(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, params={'page_size': 100})
d = r.json()
bs = d.get('results', [])
print(f'{len(bs)} blocks, has_more: {d.get("has_more")}')
if bs:
    t = bs[0]['type']
    if t in ('paragraph','heading_2','heading_3'):
        txt = ''.join(x.get('plain_text','') for x in bs[0][t].get('rich_text',[]))
        print(f'First: {txt[:60]}')
    t2 = bs[-1]['type']
    if t2 in ('paragraph','heading_2','heading_3'):
        txt2 = ''.join(x.get('plain_text','') for x in bs[-1][t2].get('rich_text',[]))
        print(f'Last: {txt2[:60]}')
