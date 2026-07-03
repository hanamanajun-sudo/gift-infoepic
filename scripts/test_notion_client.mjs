// 디버그: @notionhq/client 독립 테스트
import { Client } from '@notionhq/client';

const key = process.env.NOTION_API_KEY;
const dbId = process.env.NOTION_GUIDES_DB_ID;

console.log('Key prefix:', key?.slice(0, 12) + '...');
console.log('DB ID:', dbId);

const notion = new Client({ auth: key });

try {
  const resp = await notion.databases.query({
    database_id: dbId,
    filter: { property: 'slug', rich_text: { equals: '10세-남자아이-생일선물' } },
  });
  console.log('Success! Results:', resp.results.length);
  console.log('First result:', resp.results[0]?.id);
} catch (err) {
  console.error('Error:', err.message);
  console.error('Body:', err.body);
}
