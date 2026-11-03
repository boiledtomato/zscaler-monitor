#!/usr/bin/env python3
"""
ブログ記事の「材料」を集めるスクリプト。

  python3 scripts/blog_sources.py today              # 今日の記事タイプを決め、材料一式を出力
  python3 scripts/blog_sources.py today --date 2026-11-09
  python3 scripts/blog_sources.py digest --days 7    # Zscaler 週次ダイジェストの材料
  python3 scripts/blog_sources.py artwork            # Met 美術館のパブリックドメイン作品を1点
  python3 scripts/blog_sources.py topic zscaler      # 未執筆の解説テーマを1つ
  python3 scripts/blog_sources.py used               # 既に使った topic_id 一覧

出力は Markdown のブリーフ（人間/Claude がそのまま読める形式）。
外部ライブラリは PyYAML のみ使用。
"""

from __future__ import annotations

import argparse
import json
import random
import re
import ssl
import sys
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
BLOG = ROOT / "blog"
POSTS_DIR = BLOG / "content" / "posts"
CONFIG = json.loads((BLOG / "config.json").read_text(encoding="utf-8"))
TOPICS = json.loads((BLOG / "data" / "topics.json").read_text(encoding="utf-8"))

MET_API = "https://collectionapi.metmuseum.org/public/collection/v1"
MET_SEARCH = "https://collectionapi.metmuseum.org/public/collection/v1.1/search"
ART_QUERIES = [
    "painting", "portrait", "landscape", "sculpture", "ukiyo-e", "woodblock print",
    "Egypt", "Greek", "Roman", "Renaissance", "Impressionism", "still life",
    "illuminated manuscript", "screen", "ceramic", "Hokusai", "Hiroshige",
    "Rembrandt", "Vermeer", "Monet", "Degas", "icon", "armor", "tapestry",
]


# ------------------------------------------------------------------ helpers

def _ssl_ctx() -> ssl.SSLContext:
    ctx = ssl.create_default_context()
    for ca in ("/root/.ccr/ca-bundle.crt",):
        if Path(ca).exists():
            ctx.load_verify_locations(ca)
    return ctx


def http_json(url: str, timeout: int = 30):
    req = urllib.request.Request(url, headers={"User-Agent": "personal-blog-builder/1.0"})
    with urllib.request.urlopen(req, timeout=timeout, context=_ssl_ctx()) as r:
        return json.loads(r.read().decode("utf-8"))


def read_front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    return yaml.safe_load(m.group(1)) or {}


def used_topic_ids() -> set[str]:
    ids = set()
    for p in POSTS_DIR.glob("*.md"):
        tid = read_front_matter(p).get("topic_id")
        if tid:
            ids.add(str(tid))
    return ids


# ------------------------------------------------------------------ zscaler digest

HEADING_RE = re.compile(r"^## (\d{4}-\d{2}-\d{2})[ T]?[^\n]*?[—-]\s*(.+)$")


def collect_digest(days: int, today: date) -> str:
    """CHANGELOG.md（監視ツールの出力）から直近 days 日分の変更を抜き出す。"""
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    since = today - timedelta(days=days)
    sections: dict[str, list[str]] = {}
    current = None
    buf: list[str] = []

    def flush():
        if current and buf:
            sections.setdefault(current[1], []).append(f"### {current[0]}\n" + "\n".join(buf))

    for line in changelog.splitlines():
        m = HEADING_RE.match(line)
        if m:
            flush()
            d = date.fromisoformat(m.group(1))
            current = (m.group(1), m.group(2).strip()) if since < d <= today else None
            buf = []
        elif current:
            buf.append(line)
    flush()

    out = [f"## 監視ツールが検出した変更（{since.isoformat()} 〜 {today.isoformat()}）\n"]
    # 製品ページはナビゲーション文言の差分ばかりなので短く切る
    limits = {"製品アップデート": 1500}
    for name, chunks in sections.items():
        body = "\n\n".join(chunks)
        limit = limits.get(name, 6000)
        if len(body) > limit:
            body = body[:limit] + "\n…（以下省略）"
        out.append(f"## {name}\n\n{body}\n")

    # sitemap 上で期間内に更新されたリリースノートURL
    out.append("## 期間内に更新された公式リリースノートページ\n")
    for f in sorted((ROOT / "docs").glob("zscaler_*release_notes.md")):
        for line in f.read_text(encoding="utf-8").splitlines():
            m = re.match(r"- (\d{4}-\d{2}-\d{2})T\S* \| (https?://\S+)", line)
            if m and since < date.fromisoformat(m.group(1)) <= today:
                out.append(f"- {m.group(1)} {m.group(2)}")
    out.append("\n※ 各URLの本文は WebFetch 等で確認してから記事に反映すること。")
    return "\n".join(out)


# ------------------------------------------------------------------ art

def pick_artwork(used: set[str], tries: int = 12) -> dict:
    for _ in range(tries):
        q = random.choice(ART_QUERIES)
        base = {"q": q, "isHighlight": "true", "hasImages": "true"}
        first = http_json(f"{MET_SEARCH}?{urllib.parse.urlencode({**base, 'limit': 1})}")
        total = int(first.get("total") or 0)
        if not total:
            continue
        offset = random.randrange(0, min(total, 1000))
        res = http_json(f"{MET_SEARCH}?{urllib.parse.urlencode({**base, 'limit': 20, 'offset': offset})}")
        for oid in random.sample(res.get("objectIDs") or [], k=len(res.get("objectIDs") or [])):
            if f"met-{oid}" in used:
                continue
            obj = http_json(f"{MET_API}/objects/{oid}")
            if obj.get("isPublicDomain") and obj.get("primaryImage"):
                return obj
    raise RuntimeError("条件に合う作品が見つかりませんでした（再実行してください）")


def artwork_brief(obj: dict) -> str:
    fields = [
        ("objectID", "ID"), ("title", "作品名"), ("artistDisplayName", "作者"),
        ("artistDisplayBio", "作者情報"), ("objectDate", "制作年"), ("culture", "文化圏"),
        ("period", "時代"), ("medium", "技法・素材"), ("dimensions", "寸法"),
        ("classification", "分類"), ("department", "部門"), ("creditLine", "クレジット"),
        ("objectURL", "所蔵館ページ"), ("primaryImage", "画像(大)"), ("primaryImageSmall", "画像(小)"),
    ]
    lines = ["## 作品データ（The Met Collection API / Public Domain）\n"]
    for key, label in fields:
        if obj.get(key):
            lines.append(f"- {label}: {obj[key]}")
    tags = [t.get("term") for t in (obj.get("tags") or []) if t.get("term")]
    if tags:
        lines.append(f"- タグ: {', '.join(tags)}")
    lines.append(f"\n推奨フロントマター: topic_id: met-{obj['objectID']} / image: {obj.get('primaryImageSmall') or obj.get('primaryImage')}"
                 " / image_credit: \"The Metropolitan Museum of Art, Public Domain (CC0)\"")
    return "\n".join(lines)


# ------------------------------------------------------------------ topics

def next_topic(category: str, used: set[str]) -> dict | None:
    for t in TOPICS.get(category, []):
        if t["id"] not in used:
            return t
    return None


def topic_brief(category: str, used: set[str]) -> str:
    t = next_topic(category, used)
    if not t:
        return (f"## テーマ在庫切れ（{category}）\n\nblog/data/topics.json の {category} に新しいテーマを"
                "5件ほど追加してから（重複しないこと）、その1件目で書くこと。")
    return f"## 今回のテーマ\n\n- topic_id: {t['id']}\n- 仮タイトル: {t['title']}"


# ------------------------------------------------------------------ main

def build_today(d: date) -> str:
    kind = CONFIG["schedule"][str(d.weekday())]
    used = used_topic_ids()
    head = [f"# 記事ブリーフ {d.isoformat()}", "", f"- 記事タイプ: **{kind}**",
            f"- 保存先: blog/content/posts/{d.isoformat()}-<slug>.md",
            "- 執筆ルール: blog/WRITING_GUIDE.md を必ず読むこと", ""]
    if kind == "zscaler-digest":
        topic_id = f"digest-{d.isoformat()}"
        if topic_id in used:
            return "\n".join(head + ["本日分は既に作成済みです。何もしないで終了してください。"])
        body = f"推奨フロントマター: category: zscaler / topic_id: {topic_id}\n\n" + collect_digest(7, d)
    elif kind == "zscaler-topic":
        body = "推奨フロントマター: category: zscaler\n\n" + topic_brief("zscaler", used)
    elif kind == "art-artwork":
        body = "推奨フロントマター: category: art\n\n" + artwork_brief(pick_artwork(used))
    elif kind == "art-topic":
        body = "推奨フロントマター: category: art\n\n" + topic_brief("art", used)
    else:
        raise SystemExit(f"unknown kind: {kind}")
    return "\n".join(head) + "\n" + body


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    t = sub.add_parser("today"); t.add_argument("--date")
    g = sub.add_parser("digest"); g.add_argument("--days", type=int, default=7)
    sub.add_parser("artwork")
    tp = sub.add_parser("topic"); tp.add_argument("category", choices=["zscaler", "art"])
    sub.add_parser("used")
    a = ap.parse_args()

    today = datetime.now(timezone(timedelta(hours=9))).date()  # 日本時間
    if a.cmd == "today":
        print(build_today(date.fromisoformat(a.date) if a.date else today))
    elif a.cmd == "digest":
        print(collect_digest(a.days, today))
    elif a.cmd == "artwork":
        print(artwork_brief(pick_artwork(used_topic_ids())))
    elif a.cmd == "topic":
        print(topic_brief(a.category, used_topic_ids()))
    elif a.cmd == "used":
        print("\n".join(sorted(used_topic_ids())))


if __name__ == "__main__":
    sys.exit(main())
