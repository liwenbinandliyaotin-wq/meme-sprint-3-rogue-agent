// Meme Sprint 3: AI Agent Goes Rogue — entrypoint.
//
// This program writes the finished meme image (entry.png, sitting next to
// this file) to the output directory as entry.png. The output directory
// comes from MAKEFUN_OUTPUT_DIR and defaults to /output. The bytes written
// are exactly the bytes of entry.png, so every run produces the same image.
//
// Run it locally:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, 'entry.png');

// Sanity check: refuse to ship anything that is not a PNG.
const PNG_SIGNATURE = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
const bytes = readFileSync(source);
if (!bytes.subarray(0, 8).equals(PNG_SIGNATURE)) {
  throw new Error('entry.png does not start with the PNG signature');
}

mkdirSync(outDir, { recursive: true });
copyFileSync(source, join(outDir, 'entry.png'));
console.log(`wrote ${bytes.length} bytes to ${outDir}/entry.png`);
