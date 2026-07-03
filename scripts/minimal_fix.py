import requests, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from notion_key import get_key

KEY = get_key()
PID = '367975d6-5268-81e8-9f62-c307d2378382'
H = {'Authorization': f'Bearer {KEY}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}

# Update intro with honest sourcing
intro = "13살 여자아이 생일선물, 뭘 사줘야 할지 고민된다면? 네이버 블로그·카페에서 실제로 언급된 아이템과 가격대를 기준으로 정리했습니다."
r = requests.patch(f'https://api.notion.com/v1/pages/{PID}', headers=H, json={
    "properties": {"intro": {"rich_text": [{"text": {"content": intro}}]}}
})
print(f"Intro: {'OK' if r.status_code==200 else f'FAIL {r.status_code}'}")

# Update first paragraph via block update (if it's the very first block)
r = requests.get(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, params={'page_size': 5})
blocks = r.json().get('results', [])
if blocks:
    first = blocks[0]
    if first['type'] == 'heading_2':
        # Update the very first heading to be more honest
        bid = first['id']
        rr = requests.patch(f'https://api.notion.com/v1/blocks/{bid}', headers=H, json={
            "heading_2": {"rich_text": [{"type": "text", "text": {"content": "13살 여자아이 생일선물, 고르기 전에 알아두면 좋은 3가지"}}]}
        })
        print(f"H2: {'OK' if rr.status_code==200 else f'FAIL {rr.status_code}'}")

# Also update description (SEO meta) to use 13살
props = {
    "description": {"rich_text": [{"text": {"content": "13살 여자아이 생일선물 추천. 네이버 블로그·카페에서 언급된 선물 아이템과 가격대를 정리했습니다."}}]}
}
rr = requests.patch(f'https://api.notion.com/v1/pages/{PID}', headers=H, json={"properties": props})
print(f"Description: {'OK' if rr.status_code==200 else f'FAIL {rr.status_code}'}")

# Check current blocks
r2 = requests.get(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, params={'page_size': 100})
all_blocks = r2.json().get('results', [])
print(f"\nTotal blocks: {len(all_blocks)}")
for b in all_blocks[-3:]:
    t = b['type']
    if t in ('paragraph', 'heading_2', 'heading_3'):
        txt = ''.join(x.get('plain_text','') for x in b[t].get('rich_text',[]))
        print(f"  Last: [{t}] {txt[:60]}")
