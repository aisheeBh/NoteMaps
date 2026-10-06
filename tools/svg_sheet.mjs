// Render several SVG figures onto contact sheets for fast visual inspection.
//
// Usage: node tools/svg_sheet.mjs <out-prefix> <per-sheet> [grey] -- <a.svg> <b.svg> ...
// Writes <out-prefix>-1.png, <out-prefix>-2.png, ... each holding <per-sheet> figures
// stacked vertically with their filenames above them, using one browser session.
import puppeteer from 'puppeteer';
import fs from 'fs';
import path from 'path';

const argv = process.argv.slice(2);
const sep = argv.indexOf('--');
const [prefix, perSheetArg, greyArg] = argv.slice(0, sep);
const files = argv.slice(sep + 1);
const perSheet = parseInt(perSheetArg || '3', 10);
const grey = greyArg === 'grey';

const browser = await puppeteer.launch({ headless: 'new', protocolTimeout: 600000 });
try {
  const page = await browser.newPage();
  await page.setViewport({ width: 960, height: 800 });
  for (let i = 0, n = 1; i < files.length; i += perSheet, n++) {
    const chunk = files.slice(i, i + perSheet);
    const body = chunk.map(f =>
      `<div style="font:14px Arial;padding:6px;background:#eee">${path.basename(f)}</div>` +
      `<div style="width:960px">${fs.readFileSync(f, 'utf8')}</div>`).join('');
    await page.setContent(`<html><body style="margin:0;background:#fff;${grey ? 'filter:grayscale(1)' : ''}">${body}</body></html>`);
    await page.screenshot({ path: `${prefix}-${n}.png`, fullPage: true });
    console.log(`${prefix}-${n}.png`);
  }
} finally {
  await browser.close();
}
