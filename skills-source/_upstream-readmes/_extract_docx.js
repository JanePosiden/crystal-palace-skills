const fs = require('fs');
const path = require('path');

const xmlPath = path.join(process.env.TEMP, 'supersaga_extract', 'unz', 'word', 'document.xml');
const outPath = path.join(__dirname, 'SuperSAGA.extracted.txt');
const xml = fs.readFileSync(xmlPath, 'utf8');
const paras = xml.split(/<\/w:p>/);
const lines = [];
for (const para of paras) {
  const parts = [...para.matchAll(/<w:t[^>]*>([^<]*)<\/w:t>/g)].map((m) => m[1]);
  const line = parts
    .join('')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .trim();
  if (line) lines.push(line);
}
fs.writeFileSync(outPath, lines.join('\n'), 'utf8');
console.log('lines', lines.length);
console.log(lines.slice(0, 150).join('\n'));
