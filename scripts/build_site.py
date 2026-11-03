#!/usr/bin/env python3
"""
blog/content/posts/*.md から静的サイトを _site/ に生成する。
あわせて blog/REPORT.md（記事数・コスト・売上のレポート）を更新する。

  python3 scripts/build_site.py            # ビルド
  python3 scripts/build_site.py --check    # フロントマター検証のみ（エラーなら終了コード1）
"""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import sys
import urllib.parse
from collections import defaultdict
from datetime import date, datetime, timezone
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).resolve().parent.parent
BLOG = ROOT / "blog"
POSTS_DIR = BLOG / "content" / "posts"
OUT = ROOT / "_site"
CFG = json.loads((BLOG / "config.json").read_text(encoding="utf-8"))
BASE = CFG["base_url"].rstrip("/")
BASE_PATH = urllib.parse.urlparse(BASE).path.rstrip("/")  # 例: /zscaler-monitor

REQUIRED = ["title", "date", "category", "summary", "topic_id", "sources", "learning", "quiz"]
USD_JPY = 150  # レポート用の概算レート


# ------------------------------------------------------------------ load

def load_posts() -> tuple[list[dict], list[str]]:
    posts, errors = [], []
    seen_topics: dict[str, str] = {}
    for p in sorted(POSTS_DIR.glob("*.md")):
        text = p.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
        if not m:
            errors.append(f"{p.name}: フロントマターがありません")
            continue
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError as e:
            errors.append(f"{p.name}: YAML エラー {e}")
            continue
        missing = [k for k in REQUIRED if not fm.get(k)]
        if missing:
            errors.append(f"{p.name}: 必須項目が不足 {missing}")
        if fm.get("category") not in CFG["categories"]:
            errors.append(f"{p.name}: category が不正 ({fm.get('category')})")
        if fm.get("image") and not fm.get("image_credit"):
            errors.append(f"{p.name}: image には image_credit が必要です")
        for q in fm.get("quiz") or []:
            if not (isinstance(q, dict) and q.get("q") and q.get("a")):
                errors.append(f"{p.name}: quiz は q / a のペアで書いてください")
                break
        tid = str(fm.get("topic_id"))
        if tid in seen_topics:
            errors.append(f"{p.name}: topic_id {tid} が {seen_topics[tid]} と重複")
        seen_topics[tid] = p.name
        d = fm.get("date")
        fm["date"] = d if isinstance(d, date) else date.fromisoformat(str(d))
        fm["slug"] = p.stem
        fm["body_md"] = m.group(2)
        fm["tags"] = fm.get("tags") or []
        posts.append(fm)
    posts.sort(key=lambda x: (x["date"], x["slug"]), reverse=True)
    return posts, errors


def load_json(name: str, default):
    f = BLOG / "data" / name
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else default


# ------------------------------------------------------------------ html parts

e = html.escape


def url(path: str) -> str:
    return f"{BASE_PATH}/{path.lstrip('/')}"


CSS = """
:root{--bg:#fbfaf7;--fg:#1f2328;--muted:#5d646d;--line:#e3e0d8;--card:#fff;--accent:#2f5d8a;--accent2:#9a4e2b;--code:#f2efe8}
@media (prefers-color-scheme:dark){:root{--bg:#16181c;--fg:#e6e6e6;--muted:#a2a8b0;--line:#2c3036;--card:#1d2025;--accent:#8ab4e0;--accent2:#e0a07e;--code:#24282e}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.85 "Hiragino Sans","Noto Sans JP","Yu Gothic",system-ui,sans-serif}
a{color:var(--accent)}img{max-width:100%;height:auto}
.wrap{max-width:780px;margin:0 auto;padding:0 16px}
header.site{border-bottom:1px solid var(--line);background:var(--card)}
header.site .wrap{display:flex;flex-wrap:wrap;gap:8px 20px;align-items:baseline;padding-top:14px;padding-bottom:14px}
header.site .brand{font-weight:700;font-size:1.1rem;text-decoration:none;color:var(--fg)}
header.site nav a{margin-right:14px;font-size:.92rem;text-decoration:none}
main{padding:28px 0 48px}
h1{font-size:1.6rem;line-height:1.45;margin:.2em 0 .4em}h2{font-size:1.25rem;margin-top:2em;border-left:4px solid var(--accent);padding-left:10px}
h3{font-size:1.08rem;margin-top:1.6em}
.meta{color:var(--muted);font-size:.85rem}
.chip{display:inline-block;font-size:.75rem;padding:1px 8px;border-radius:99px;border:1px solid var(--line);margin-right:4px;color:var(--muted);text-decoration:none}
.chip.zscaler{color:var(--accent);border-color:var(--accent)}.chip.art{color:var(--accent2);border-color:var(--accent2)}
.list{list-style:none;padding:0;margin:0}.list li{padding:16px 0;border-bottom:1px solid var(--line)}
.list a.t{font-weight:700;font-size:1.05rem;text-decoration:none;color:var(--fg)}.list p{margin:.3em 0 0;color:var(--muted);font-size:.92rem}
table{border-collapse:collapse;width:100%;display:block;overflow-x:auto;font-size:.92rem}th,td{border:1px solid var(--line);padding:6px 10px;text-align:left;vertical-align:top}th{background:var(--code)}
code{background:var(--code);padding:1px 5px;border-radius:4px;font-size:.9em}pre{background:var(--code);padding:12px;overflow-x:auto;border-radius:6px}pre code{padding:0}
blockquote{margin:1em 0;padding:.2em 1em;border-left:3px solid var(--line);color:var(--muted)}
.box{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:14px 18px;margin:24px 0}
.box h2{margin-top:0;border:0;padding:0;font-size:1.05rem}
details{margin:.5em 0;padding:8px 12px;border:1px solid var(--line);border-radius:6px;background:var(--bg)}summary{cursor:pointer;font-weight:600}
figure{margin:0 0 20px}figcaption{font-size:.8rem;color:var(--muted)}
.pr{font-size:.78rem;color:var(--muted)}
footer{border-top:1px solid var(--line);color:var(--muted);font-size:.82rem;padding:20px 0 40px}
.kpi{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px}.kpi div{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:12px}.kpi b{display:block;font-size:1.4rem}
"""


def layout(title: str, body: str, *, description: str = "", canonical: str = "", noindex: bool = False,
           og_image: str = "", json_ld: dict | None = None) -> str:
    desc = description or CFG["site_description"]
    full_title = title if title == CFG["site_title"] else f"{title} | {CFG['site_title']}"
    ads = CFG["monetization"].get("adsense_client")
    head_extra = []
    if ads:
        head_extra.append(f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={e(ads)}" crossorigin="anonymous"></script>')
    if noindex:
        head_extra.append('<meta name="robots" content="noindex">')
    if canonical:
        head_extra.append(f'<link rel="canonical" href="{e(canonical)}">')
        head_extra.append(f'<meta property="og:url" content="{e(canonical)}">')
    if og_image:
        head_extra.append(f'<meta property="og:image" content="{e(og_image)}">')
    if json_ld:
        head_extra.append(f'<script type="application/ld+json">{json.dumps(json_ld, ensure_ascii=False)}</script>')
    cats = "".join(f'<a href="{url("category/" + k + "/")}">{e(v["name"])}</a>' for k, v in CFG["categories"].items())
    return f"""<!doctype html>
<html lang="{CFG['language']}"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(full_title)}</title><meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(full_title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:type" content="website">
<link rel="alternate" type="application/rss+xml" title="{e(CFG['site_title'])}" href="{url('feed.xml')}">
<link rel="stylesheet" href="{url('style.css')}">
{chr(10).join(head_extra)}
</head><body>
<header class="site"><div class="wrap"><a class="brand" href="{url('')}">{e(CFG['site_title'])}</a>
<nav>{cats}<a href="{url('learn/')}">学習ノート</a><a href="{url('about/')}">このブログについて</a></nav></div></header>
<main><div class="wrap">{body}</div></main>
<footer><div class="wrap">{e(CFG['monetization']['pr_disclosure'])}<br>
本ブログは個人の学習記録であり、Zscaler, Inc. および各美術館とは関係ありません。製品情報は必ず公式ドキュメントでご確認ください。<br>
© {date.today().year} {e(CFG['author'])} · <a href="{url('about/')}">プライバシーポリシー</a> · <a href="{url('feed.xml')}">RSS</a></div></footer>
</body></html>"""


def chips(p: dict) -> str:
    cat = p["category"]
    out = f'<a class="chip {cat}" href="{url("category/" + cat + "/")}">{e(CFG["categories"][cat]["name"])}</a>'
    out += "".join(f'<span class="chip">{e(str(t))}</span>' for t in p["tags"][:4])
    return out


def post_list(posts: list[dict]) -> str:
    items = []
    for p in posts:
        items.append(f'<li><div class="meta">{p["date"].isoformat()} {chips(p)}</div>'
                     f'<a class="t" href="{url("posts/" + p["slug"] + "/")}">{e(p["title"])}</a>'
                     f'<p>{e(p["summary"])}</p></li>')
    return f'<ul class="list">{"".join(items)}</ul>' if items else "<p>まだ記事がありません。</p>"


def affiliate_box(cat: str) -> str:
    mon = CFG["monetization"]
    tag = mon.get("amazon_associate_tag")
    links = mon.get("affiliates", {}).get(cat) or []
    if not tag or not links:
        return ""
    lis = "".join(
        f'<li><a href="https://www.amazon.co.jp/s?k={urllib.parse.quote(l["amazon_keyword"])}&tag={urllib.parse.quote(tag)}" '
        f'rel="sponsored noopener" target="_blank">{e(l["label"])}</a></li>' for l in links)
    return f'<div class="box"><h2>さらに学ぶための本</h2><ul>{lis}</ul><p class="pr">PR：上記はアフィリエイトリンクです。</p></div>'


def render_md(text: str) -> str:
    return markdown.markdown(text, extensions=["tables", "fenced_code", "toc", "sane_lists"])


def post_page(p: dict, prev_p: dict | None, next_p: dict | None) -> str:
    canonical = f"{BASE}/posts/{p['slug']}/"
    fig = ""
    if p.get("image"):
        fig = (f'<figure><img src="{e(p["image"])}" alt="{e(p["title"])}" loading="lazy">'
               f'<figcaption>{e(p["image_credit"])}</figcaption></figure>')
    learn = "".join(f"<li>{e(str(x))}</li>" for x in p["learning"])
    quiz = "".join(f"<details><summary>Q{i}. {e(q['q'])}</summary><p>{e(q['a'])}</p></details>"
                   for i, q in enumerate(p["quiz"], 1))
    srcs = "".join(f'<li><a href="{e(s)}" rel="noopener" target="_blank">{e(s)}</a></li>' for s in p["sources"])
    nav = []
    if next_p:
        nav.append(f'← <a href="{url("posts/" + next_p["slug"] + "/")}">{e(next_p["title"])}</a>')
    if prev_p:
        nav.append(f'<a href="{url("posts/" + prev_p["slug"] + "/")}">{e(prev_p["title"])}</a> →')
    body = f"""<article>
<div class="meta">{p['date'].isoformat()} {chips(p)}</div>
<h1>{e(p['title'])}</h1>
{fig}
<div class="box"><h2>この記事で学べること</h2><ul>{learn}</ul></div>
{render_md(p['body_md'])}
<div class="box"><h2>確認クイズ</h2>{quiz}</div>
{affiliate_box(p['category'])}
<div class="box"><h2>参考・出典</h2><ul>{srcs}</ul></div>
</article>
<p class="meta">{'　'.join(nav)}</p>"""
    ld = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["title"],
          "datePublished": p["date"].isoformat(), "author": {"@type": "Person", "name": CFG["author"]},
          "description": p["summary"], "mainEntityOfPage": canonical}
    if p.get("image"):
        ld["image"] = p["image"]
    return layout(p["title"], body, description=p["summary"], canonical=canonical,
                  og_image=p.get("image", ""), json_ld=ld)


def learn_page(posts: list[dict]) -> str:
    parts = ["<h1>学習ノート</h1><p>全記事の学習ポイントと確認クイズをまとめた復習用ページです。</p>"]
    for cat, meta in CFG["categories"].items():
        ps = [p for p in posts if p["category"] == cat]
        parts.append(f"<h2>{e(meta['name'])}（{len(ps)}本）</h2>")
        for p in ps:
            pts = "".join(f"<li>{e(str(x))}</li>" for x in p["learning"])
            qs = "".join(f"<details><summary>{e(q['q'])}</summary><p>{e(q['a'])}</p></details>" for q in p["quiz"])
            parts.append(f'<h3><a href="{url("posts/" + p["slug"] + "/")}">{e(p["title"])}</a></h3>'
                         f'<div class="meta">{p["date"].isoformat()}</div><ul>{pts}</ul>{qs}')
    return layout("学習ノート", "".join(parts))


def about_page() -> str:
    body = f"""<h1>このブログについて</h1>
<p>{e(CFG['site_description'])}</p>
<p>記事は、公開情報（Zscaler 公式ヘルプ・ステータスページ、美術館のオープンアクセスデータ等）をもとに、
AI（Claude）の支援を受けて作成し、出典を明記しています。内容の正確性には注意していますが、
製品の仕様・設定は必ず公式ドキュメントでご確認ください。誤りに気づかれた場合はお知らせください。</p>
<h2>画像について</h2>
<p>美術作品の画像は、メトロポリタン美術館の Open Access（パブリックドメイン / CC0）として公開されているもののみを使用しています。</p>
<h2>プライバシーポリシー</h2>
<p>当ブログでは、第三者配信の広告サービス（Google AdSense）やアフィリエイトプログラム（Amazonアソシエイト等）を利用する場合があります。
これらの事業者は、ユーザーの興味に応じた広告を表示するために Cookie を使用することがあります。
Cookie を無効にする方法や Google の広告に関する詳細は
<a href="https://policies.google.com/technologies/ads?hl=ja">Google のポリシーと規約</a>をご覧ください。</p>
<p>当ブログは Amazon.co.jp を宣伝しリンクすることによってサイトが紹介料を獲得できる手段を提供することを目的に設定された
アフィリエイトプログラムである、Amazonアソシエイト・プログラムの参加者です（参加後に有効）。</p>
<h2>免責事項</h2>
<p>当ブログの情報を利用して生じた損害について、一切の責任を負いかねます。</p>"""
    return layout("このブログについて", body)


# ------------------------------------------------------------------ report

def finance(posts: list[dict]) -> dict:
    costs = load_json("costs.json", {"entries": []})["entries"]
    revenue = load_json("revenue.json", {"entries": []})["entries"]
    months: dict[str, dict] = defaultdict(lambda: {"posts": 0, "cost_jpy": 0.0, "revenue_jpy": 0.0})
    for p in posts:
        months[p["date"].strftime("%Y-%m")]["posts"] += 1
    for c in costs:
        jpy = c.get("jpy", c.get("usd", 0) * USD_JPY)
        months[str(c["date"])[:7]]["cost_jpy"] += jpy
    for r in revenue:
        months[r["month"]]["revenue_jpy"] += r.get("amount_jpy", 0)
    tot = {k: sum(m[k] for m in months.values()) for k in ("posts", "cost_jpy", "revenue_jpy")}
    by_source: dict[str, float] = defaultdict(float)
    for r in revenue:
        by_source[r.get("source", "不明")] += r.get("amount_jpy", 0)
    return {"months": dict(sorted(months.items(), reverse=True)), "total": tot, "by_source": dict(by_source)}


def write_report(posts: list[dict], fin: dict) -> None:
    t = fin["total"]
    lines = ["# ブログ運用レポート", "",
             f"_自動生成: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}（scripts/build_site.py）_", "",
             f"- 公開記事数: **{t['posts']}**（Zscaler {sum(p['category']=='zscaler' for p in posts)} / 美術 {sum(p['category']=='art' for p in posts)}）",
             f"- 累計売上: **{t['revenue_jpy']:,.0f} 円**",
             f"- 累計コスト: **{t['cost_jpy']:,.0f} 円**（API・ドメイン等。サブスク内の実行は0円計上）",
             f"- 累計収支: **{t['revenue_jpy'] - t['cost_jpy']:,.0f} 円**", "",
             "## 月別", "", "| 月 | 記事数 | 売上(円) | コスト(円) | 収支(円) |", "|---|---:|---:|---:|---:|"]
    for m, v in fin["months"].items():
        lines.append(f"| {m} | {v['posts']} | {v['revenue_jpy']:,.0f} | {v['cost_jpy']:,.0f} | {v['revenue_jpy'] - v['cost_jpy']:,.0f} |")
    if fin["by_source"]:
        lines += ["", "## 収益源別", "", "| 収益源 | 累計(円) |", "|---|---:|"]
        lines += [f"| {k} | {v:,.0f} |" for k, v in fin["by_source"].items()]
    lines += ["", "## 最近の記事", ""]
    lines += [f"- {p['date']} [{p['category']}] {p['title']}" for p in posts[:10]]
    lines += ["", "売上は `blog/data/revenue.json` に月ごとに記録します（Claude に「11月のAdSenseは○円」と伝えれば追記されます）。", ""]
    (BLOG / "REPORT.md").write_text("\n".join(lines), encoding="utf-8")


def dashboard_page(fin: dict) -> str:
    t = fin["total"]
    rows = "".join(f"<tr><td>{m}</td><td>{v['posts']}</td><td>{v['revenue_jpy']:,.0f}</td><td>{v['cost_jpy']:,.0f}</td>"
                   f"<td>{v['revenue_jpy'] - v['cost_jpy']:,.0f}</td></tr>" for m, v in fin["months"].items())
    body = f"""<h1>運用ダッシュボード</h1>
<div class="kpi"><div>記事数<b>{t['posts']}</b></div><div>累計売上<b>{t['revenue_jpy']:,.0f}円</b></div>
<div>累計コスト<b>{t['cost_jpy']:,.0f}円</b></div><div>収支<b>{t['revenue_jpy'] - t['cost_jpy']:,.0f}円</b></div></div>
<h2>月別</h2><table><tr><th>月</th><th>記事</th><th>売上</th><th>コスト</th><th>収支</th></tr>{rows}</table>"""
    return layout("運用ダッシュボード", body, noindex=True)


# ------------------------------------------------------------------ feeds

def feed_xml(posts: list[dict]) -> str:
    items = []
    for p in posts[:30]:
        link = f"{BASE}/posts/{p['slug']}/"
        pub = datetime.combine(p["date"], datetime.min.time(), tzinfo=timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")
        items.append(f"<item><title>{e(p['title'])}</title><link>{link}</link><guid>{link}</guid>"
                     f"<pubDate>{pub}</pubDate><description>{e(p['summary'])}</description></item>")
    return (f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>{e(CFG["site_title"])}</title>'
            f'<link>{BASE}/</link><description>{e(CFG["site_description"])}</description><language>ja</language>'
            f'{"".join(items)}</channel></rss>')


def sitemap_xml(posts: list[dict]) -> str:
    urls = [f"{BASE}/", f"{BASE}/learn/", f"{BASE}/about/"] + [f"{BASE}/category/{k}/" for k in CFG["categories"]]
    entries = [f"<url><loc>{u}</loc></url>" for u in urls]
    entries += [f"<url><loc>{BASE}/posts/{p['slug']}/</loc><lastmod>{p['date'].isoformat()}</lastmod></url>" for p in posts]
    return f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{"".join(entries)}</urlset>'


# ------------------------------------------------------------------ main

def write(rel: str, content: str) -> None:
    f = OUT / rel
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(content, encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    posts, errors = load_posts()
    if errors:
        print("\n".join("ERROR: " + x for x in errors), file=sys.stderr)
        return 1
    if a.check:
        print(f"OK: {len(posts)} posts")
        return 0

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    write("style.css", CSS.strip())
    write(".nojekyll", "")
    intro = f"<p>{e(CFG['site_description'])}</p>"
    write("index.html", layout(CFG["site_title"], intro + post_list(posts), canonical=f"{BASE}/"))
    for k, v in CFG["categories"].items():
        ps = [p for p in posts if p["category"] == k]
        write(f"category/{k}/index.html", layout(v["name"], f"<h1>{e(v['name'])}</h1><p>{e(v['description'])}</p>" + post_list(ps),
                                                  canonical=f"{BASE}/category/{k}/"))
    for i, p in enumerate(posts):
        prev_p = posts[i + 1] if i + 1 < len(posts) else None
        next_p = posts[i - 1] if i > 0 else None
        write(f"posts/{p['slug']}/index.html", post_page(p, prev_p, next_p))
    write("learn/index.html", learn_page(posts))
    write("about/index.html", about_page())
    write("feed.xml", feed_xml(posts))
    write("sitemap.xml", sitemap_xml(posts))
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
    ads = CFG["monetization"].get("adsense_client")
    if ads:
        write("ads.txt", f"google.com, {ads.replace('ca-', '')}, DIRECT, f08c47fec0942fa0\n")
    fin = finance(posts)
    if CFG.get("publish_dashboard"):
        write("dashboard/index.html", dashboard_page(fin))
    write_report(posts, fin)
    print(f"Built {len(posts)} posts -> {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
