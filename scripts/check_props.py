"""Check 시어머니 page properties in Notion"""
import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

KEY = get_key()
GUIDES_DB = '9603a00b-976b-4791-a129-d5f537e5db06'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}

r = requests.post(f'https://api.notion.com/v1/databases/{GUIDES_DB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'equals': '시어머니-선물'}}
})
p = r.json()['results'][0]
props = p['properties']
for k, v in props.items():
    ptype = v['type']
    if ptype == 'checkbox':
        print(f'{k}: {v[ptype]}')
    elif ptype == 'rich_text':
        arr = v.get(ptype, [])
        txt = arr[0]['plain_text'][:60] if arr else '(empty)'
        print(f'{k}: {txt}')
    elif ptype == 'title':
        arr = v[ptype]
        print(f'{k}: {arr[0]["plain_text"]}')
    elif ptype in ('select', 'multi_select'):
        val = v.get(ptype, [])
        if isinstance(val, list):
            names = [x['name'] for x in val]
            print(f'{k}: {names}')
        elif val:
            print(f'{k}: {val["name"]}')
        else:
            print(f'{k}: (none)')
    elif ptype == 'number':
        print(f'{k}: {v[ptype]}')
    else:
        print(f'{k} ({ptype}): {str(v.get(ptype,""))[:60]}')
