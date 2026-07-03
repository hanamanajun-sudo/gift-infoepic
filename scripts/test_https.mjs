// https 모듈로 Notion API 테스트
import https from 'https';

const key = process.env.NOTION_API_KEY;
const dbId = process.env.NOTION_GUIDES_DB_ID;

const body = JSON.stringify({
  filter: { property: 'slug', rich_text: { equals: '10세-남자아이-생일선물' } }
});

const options = {
  hostname: 'api.notion.com',
  path: `/v1/databases/${dbId}/query`,
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${key}`,
    'Notion-Version': '2022-06-28',
    'Content-Type': 'application/json',
    'User-Agent': 'test-script/1.0'
  }
};

const req = https.request(options, (res) => {
  let data = '';
  res.on('data', (chunk) => data += chunk);
  res.on('end', () => {
    const parsed = JSON.parse(data);
    console.log('Status:', res.statusCode);
    if (parsed.results?.length > 0) {
      console.log('Page ID:', parsed.results[0].id);
      console.log('Title:', parsed.results[0].properties?.Title?.title?.[0]?.plain_text);
    } else {
      console.log('Response:', JSON.stringify(parsed, null, 2));
    }
  });
});

req.on('error', (e) => console.error('Error:', e.message));
req.write(body);
req.end();
