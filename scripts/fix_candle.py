import requests, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from notion_key import get_key

K = get_key()
H = {'Authorization': f'Bearer {K}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}
GDB = '9603a00b-976b-4791-a129-d5f537e5db06'

r = requests.post(f'https://api.notion.com/v1/databases/{GDB}/query', headers=H, json={
    'filter': {'property': 'slug', 'rich_text': {'contains': '캔들-선물'}}, 'page_size': 3
})
pid = r.json()['results'][0]['id']

B = [{
    'object': 'block', 'type': 'paragraph', 'paragraph': {
        'rich_text': [{'type': 'text', 'text': {'content': '캔들 선물은 예쁜 포장이 반이라고 할 정도로 패키지가 중요합니다. 리본이나 선물 상자까지 신경 쓴 제품을 고르면 받는 사람의 만족도가 훨씬 높아집니다. 선물용 포장이 기본으로 포함된 제품을 선택하는 게 좋습니다.'}}]
    }
}]
r2 = requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children', headers=H, json={'children': B})
print(f'OK {r2.status_code}')
