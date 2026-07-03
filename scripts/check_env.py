import os
with open('.env', 'rb') as f:
    for line in f:
        line = line.strip()
        if b'NOTION_API_KEY=*** in line:
            key = line.split(b'=', 1)[1]
            print(f'Key bytes: {len(key)}')
            print(f'First 10: {key[:10]}')
            print(f'Last 10: {key[-10:]}')
            break

# Also check if Astro can access it by reading Astro env
import subprocess
result = subprocess.run(['node', '-e', '''
require("dotenv").config({path: ".env"});
console.log("KEY from dotenv:", process.env.NOTION_API_KEY?.substring(0, 15));
'''], capture_output=True, text=True, cwd='.')
print('Node stdout:', result.stdout)
print('Node stderr:', result.stderr[:200])
