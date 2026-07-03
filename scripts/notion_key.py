"""Read Notion API key from .env"""
import os

def get_key():
    env_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
    with open(env_file, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('NOTION_API_KEY='):
                return line.split('=', 1)[1].strip()
    return ''
