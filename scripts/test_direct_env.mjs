// .env 직접 파싱 후 Notion API 호출
import fs from 'fs';
import https from 'https';

function parseEnv(path) {
  const content = fs.readFileSync(path, 'utf-8');
  const env = {};
  for (const line of content.split('\n')) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#') || !trimmed.includes('=')) continue;
    const eqIdx = trimmed.indexOf('=');
    let key = trimmed.slice(0, eqIdx).trim();
    let value = trimmed.slice(eqIdx + 1).trim();
    if (value.startsWith('"') && value.endsWith('"')) value = value.slice(1, -1);
    env[key] = value;
  }
  return env;
}

const env = parseEnv(new URL('../.env', import.meta.url));
const key = env.NOTION_API_KEY;
const dbId = env.NOTION_GUIDES_DB_ID;

console.log('Key:', key?.slice(0, 15) + '...');
console.log('DB:', dbId);

const body = JSON.stringify({
  filter: { property: 'slug', rich_text: { equals: '10세-남자아이-생일선물' } }
});

const req = https.request({
  hostname: 'api.notion.com',
  path: `/v1/databases/${dbId}/query`,
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${key}`,
    'Notion-Version': '2022-06-28',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
  }
}, (res) => {
  let data = '';
  res.on('data', (c) => data += c);
  res.on('end', () => {
    const j = JSON.parse(data);
    console.log('Status:', res.statusCode);
    console.log('Results:', j.results?.length ?? j.message);
  });
});
req.on('error', (e) => console.error('Error:', e.message));
req.write(body);
req.end();
