#!/usr/bin/env node
/*
 * help.zscaler.com のリリース概要ページ（JavaScript で描画される）をヘッドレスブラウザで開き、
 * デプロイ日ごとの項目を JSON で出力する。scripts/zscaler_sources.py から呼ばれる。
 *
 *   node scripts/release_notes_extract.js <since YYYY-MM-DD> <until YYYY-MM-DD> <path> [<path> ...]
 *   例: node scripts/release_notes_extract.js 2026-11-06 2026-11-12 zia/release-upgrade-summary-2026
 *
 * 出力: [{page, url, cloud, entries: [{date, category, title, text, anchor}]}]
 * ページ側の構造: div.parent-release-notes#YYYY-MM-DD > (カテゴリ) > li.release-notes > h3 + 本文
 */
const { chromium } = require('playwright');

(async () => {
  const [since, until, ...paths] = process.argv.slice(2);
  if (!since || !until || paths.length === 0) {
    console.error('usage: release_notes_extract.js <since> <until> <path>...');
    process.exit(2);
  }
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const results = [];
  for (const path of paths) {
    const url = 'https://help.zscaler.com/' + path;
    try {
      await page.goto(url, { waitUntil: 'networkidle', timeout: 90000 });
      await page.waitForSelector('.parent-release-notes', { timeout: 30000 });
      // Client Connector のアプリ版はOSごとにページ内容が切り替わる。OSの選択肢があれば全部回る
      const pfIndex = await page.evaluate(() =>
        [...document.querySelectorAll('select')].findIndex((s) =>
          [...s.options].some((o) => o.text.trim() === 'Windows') &&
          [...s.options].some((o) => o.text.trim() === 'macOS')));
      const platforms = pfIndex < 0 ? [['', '']] : await page.evaluate((i) =>
        [...document.querySelectorAll('select')[i].options].map((o) => [o.value, o.text.trim()]), pfIndex);
      for (const [pfValue, pfName] of platforms) {
        if (pfName) {
          await page.locator('select').nth(pfIndex).selectOption(pfValue);
          await page.waitForTimeout(3000);
        }
      const data = await page.evaluate(([since, until]) => {
        const clean = (s) => (s || '').replace(/[ \t]+/g, ' ').replace(/\n{2,}/g, '\n').trim();
        const sel = document.querySelector('select.form-select');
        const cloud = sel ? (sel.options[sel.selectedIndex] || {}).text || '' : '';
        const entries = [];
        for (const block of document.querySelectorAll('.parent-release-notes')) {
          const d = block.id;
          if (!/^\d{4}-\d{2}-\d{2}$/.test(d) || d < since || d > until) continue;
          for (const li of block.querySelectorAll('li.release-notes')) {
            const h = li.querySelector('.release-notes-title');
            // 直近の上位カテゴリ（Feature Available / Feature Update など）を探す
            let category = '';
            const group = li.closest('ul.child');
            const head = group && group.previousElementSibling;
            if (head) category = clean(head.innerText);
            const body = li.querySelector('.article-page');
            const links = body ? [...body.querySelectorAll('a[href^="/"]')]
              .map((a) => 'https://help.zscaler.com' + a.getAttribute('href'))
              .filter((v, i, arr) => arr.indexOf(v) === i).slice(0, 5) : [];
            entries.push({
              date: d,
              category,
              title: clean(h ? h.innerText : ''),
              text: clean(body ? body.innerText.replace(/See image\.|Close/g, '') : '').slice(0, 2500),
              links,
              anchor: li.id || '',
            });
          }
        }
        return { cloud, entries };
      }, [since, until]);
      results.push({ page: path, url, cloud: data.cloud, platform: pfName || '', entries: data.entries });
      }
    } catch (e) {
      results.push({ page: path, url, error: String(e.message || e).slice(0, 300), entries: [] });
    }
  }
  await browser.close();
  process.stdout.write(JSON.stringify(results, null, 1));
})();
