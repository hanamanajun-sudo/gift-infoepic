"""Delete remaining blocks from the guide page."""
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

# Get all block IDs
r = requests.get(f'https://api.notion.com/v1/blocks/{PID}/children', headers=H, params={'page_size': 100})
all_blocks = r.json().get('results', [])
print(f"Found {len(all_blocks)} blocks")
for b in all_blocks:
    print(f"  Deleting {b['id'][:20]}...", end=' ', flush=True)
    dr = requests.delete(f'https://api.notion.com/v1/blocks/{b["id"]}', headers=H)
    print(f"{'OK' if dr.status_code in (200,204) else f'FAIL {dr.status_code}'}")
print("All deleted")
