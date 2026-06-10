"""Update the budget section in Notion - replace table with formatted list."""
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

# First find the table block and the adjacent blocks
r = requests.get(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, params={'page_size': 100})
blocks = r.json().get('results', [])

# Find table block and the blocks around it
table_bid = None
prev_bid = None
next_bid = None
for i, b in enumerate(blocks):
    if b['type'] == 'table':
        table_bid = b['id']
        if i > 0: prev_bid = blocks[i-1]['id']
        if i < len(blocks)-1: next_bid = blocks[i+1]['id']
        break

if not table_bid:
    print("No table found - might already be fixed")
    exit(0)

print(f"Found table: {table_bid[:25]}")
print(f"Previous block: {prev_bid[:25] if prev_bid else 'none'}")
print(f"Next block: {next_bid[:25] if next_bid else 'none'}")

# Delete the table block
dr = requests.delete(f'https://api.notion.com/v1/blocks/{table_bid}', headers=H)
print(f"Delete table: {'OK' if dr.status_code in (200,204) else f'FAIL {dr.status_code}'}")

# Now append new list blocks AFTER the previous block
# Actually, Notion always appends at the end. So let me just append them.
# The table was between "예산별 추천" paragraph and "이런 선물은 피하는 게 좋아요" heading.
# Since the table is gone now, the section will have a gap.
# Let me replace it with formatted content

def p(t): return {"object":"block","type":"paragraph","paragraph":{"rich_text":[{"type":"text","text":{"content":t}}]}}
def bp(parts):
    r = []
    for part in parts:
        if isinstance(part,tuple): r.append({"type":"text","text":{"content":part[0]},"annotations":{"bold":True}})
        else: r.append({"type":"text","text":{"content":part}})
    return {"object":"block","type":"paragraph","paragraph":{"rich_text":r}}

new_blocks = [
    bp([("~3만원 (친구·또래): ", True), "다꾸 세트, 네컷 앨범, 폰케이스, 마카롱 기프티콘"]),
    bp([("3~7만원 (부모가 딸에게): ", True), "어뮤즈 틴트, QCY 이어폰, 스킨케어 세트, 인스탁스 미니"]),
    bp([("7~10만원 (부모·친척): ", True), "인스탁스 링크2, 갤럭시 버즈FE, 산리오 인형 세트"]),
    bp([("10만원+ (친척·어른): ", True), "에어팟, 아이패드 악세서리, 미니백"]),
]

r = requests.patch(
    f'https://api.notion.com/v1/blocks/{PID}/children',
    headers=H,
    json={"children": new_blocks}
)
if r.status_code == 200:
    print(f"OK! Appended {len(new_blocks)} replacement blocks")
else:
    print(f"FAIL: {r.status_code} {r.text[:300]}")
