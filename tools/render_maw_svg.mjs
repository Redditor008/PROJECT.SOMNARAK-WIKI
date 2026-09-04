// Dev-only helper: renders docs/assets/art/maw/*.svg to PNG using @resvg/resvg-js.
// Usage: node tools/render_maw_svg.mjs <name.svg> [name.svg ...]
// Output: /tmp/mawhi/<name>.png
import { Resvg } from '@resvg/resvg-js';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const outDir = '/tmp/mawhi';
fs.mkdirSync(outDir, { recursive: true });
const files = process.argv.slice(2);
if (!files.length) { console.error('no svg filenames'); process.exit(1); }
for (const f of files) {
  const svg = fs.readFileSync(path.join(root, 'docs/assets/art/maw', f), 'utf8');
  const r = new Resvg(svg, { fitTo: { mode: 'width', value: 420 } });
  fs.writeFileSync(path.join(outDir, f.replace(/\.svg$/, '.png')), r.render().asPng());
}
console.log('rendered ' + files.length);
