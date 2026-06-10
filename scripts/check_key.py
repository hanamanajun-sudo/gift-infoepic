with open('.env') as f:
    for line in f:
        line = line.strip()
        if line.startswith('NOTION_API_KEY='):
            key = line.split('=', 1)[1].strip()
            print(f"Key starts with: {key[:12]}")
            print(f"Key length: {len(key)}")
            break
