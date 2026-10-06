// Render an SVG figure to PNG so it can be inspected (optionally in greyscale).
//
// Usage (run from anywhere; needs `npm install` once inside tools/):
//   node tools/svg_preview.mjs <in.svg> <out.png> [grey]
//
// "grey" applies CSS filter: grayscale(1), simulating a black-and-white print.
import puppeteer from 'puppeteer';
import fs from 'fs';

const [, , inp, out, grey] = process.argv;
if (!inp || !out) {
  console.error('usage: node tools/svg_preview.mjs <in.svg> <out.png> [grey]');
  process.exit(2);
}
const svg = fs.readFileSync(inp, 'utf8');
const browser = await puppeteer.launch({ headless: 'new', protocolTimeout: 240000 });
try {
  const page = await browser.newPage();
  await page.setViewport({ width: 960, height: 900 });
  await page.setContent(
    `<html><body style="margin:0;background:#fff;${grey ? 'filter:grayscale(1)' : ''}">` +
    `<div style="width:960px">${svg}</div></body></html>`);
  const el = await page.$('div');
  await el.screenshot({ path: out });
} finally {
  await browser.close();
}
