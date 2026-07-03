// raw fetch Notion API 테스트 (without @notionhq/client)
const key = process.env.NOTION_API_KEY;
const dbId = process.env.NOTION_GUIDES_DB_ID;
console.log('Key prefix:', key?.slice(0, 12) + '...');
console.log('DB ID:', dbId);

const url = `https://api.notion.com/v1/databases/${dbId}/query`;
const body = JSON.stringify({
  filter: { property: 'slug', rich_text: { equals: '10세-남자아이-생일선물' } }
});

const resp = await fetch(url, {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${key}`,
    'Notion-Version': '2022-06-28',
    'Content-Type': 'application/json'
  },
  body
});

const data = await resp.json();
console.log('Status:', resp.status);
console.log('Results:', data.results?.length);
if (data.results?.length > 0) {
  console.log('Page ID:', data.results[0].id);
  console.log('Title:', data.results[0].properties?.Title?.title?.[0]?.plain_text);
} else {
  console.log('Error:', JSON.stringify(data, null, 2));
}
