import fs from 'fs';

// Read .env like Python does
const envPath = new URL('../.env', import.meta.url);
const content = fs.readFileSync(envPath, 'utf-8');
console.log('File length:', content.length);
console.log('First 100 chars:', JSON.stringify(content.slice(0, 100)));

// Parse it
const lines = content.split('\n');
for (const line of lines) {
  const trimmed = line.trim();
  if (trimmed && !trimmed.startsWith('#') && trimmed.includes('=')) {
    const eqIdx = trimmed.indexOf('=');
    const key = trimmed.slice(0, eqIdx).trim();
    let value = trimmed.slice(eqIdx + 1).trim();
    if (value.startsWith('"') && value.endsWith('"')) {
      value = value.slice(1, -1);
    }
    console.log(`  ${key}=${value.slice(0, 20)}...`);
  }
}
