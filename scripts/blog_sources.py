#!/usr/bin/env python3
"""
ブログ記事の「材料」を集めるスクリプト。

  python3 scripts/blog_sources.py --site zscaler today     # 今日の記事タイプを決め、材料一式を出力
  python3 scripts/blog_sources.py --site zscaler digest --days 7   # 週次ダイジェストの材料
  python3 scripts/blog_sources.py --site zscaler topic         # 未執筆のテーマを1つ
  python3 scripts/blog_sources.py --site zscaler used          # 既に使った topic_id 一覧

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
sys.path.insert(0, str(Path(__file__).resolve().parent))
SITES = ("zscaler",)  # 美術ブログは boiledtomato/meiga-note に移した


def site_dir(site: str) -> Path:
    return ROOT / "blogs" / site


def site_config(site: str) -> dict:
    return json.loads((site_dir(site) / "config.json").read_text(encoding="utf-8"))


def site_topics(site: str) -> list[dict]:
    return json.loads((site_dir(site) / "data" / "topics.json").read_text(encoding="utf-8"))

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


def used_topic_ids(site: str) -> set[str]:
    ids = set()
    for p in (site_dir(site) / "content" / "posts").glob("*.md"):
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


# ------------------------------------------------------------------ topics

def next_topic(site: str, used: set[str]) -> dict | None:
    for t in site_topics(site):
        if t["id"] not in used:
            return t
    return None


def topic_brief(site: str, used: set[str]) -> str:
    t = next_topic(site, used)
    if not t:
        return (f"## テーマ在庫切れ\n\nblogs/{site}/data/topics.json に新しいテーマを"
                "5件ほど追加してから（重複しないこと）、その1件目で書くこと。")
    return f"## 今回のテーマ\n\n- topic_id: {t['id']}\n- 仮タイトル: {t['title']}"


# ------------------------------------------------------------------ main

def _head(site: str, d: date, kind: str, n: int | None = None) -> list[str]:
    title = f"# 記事ブリーフ（{site} ブログ）{d.isoformat()}" + (f" — 記事{n}" if n else "")
    return [title, "", f"- 記事タイプ: **{kind}**",
            f"- 保存先: blogs/{site}/content/posts/{d.isoformat()}-<topic_id>.md",
            f"- 執筆ルール: blogs/WRITING_RULES_COMMON.md と blogs/{site}/WRITING_GUIDE.md を必ず読むこと", ""]


def build_zscaler_today(d: date) -> str:
    """Zscaler ブログ: 曜日の定期記事（製品別アップデート／基礎）＋ 不定期の Trust 記事。"""
    import zscaler_sources as zs
    cfg = site_config("zscaler")
    kind = cfg["schedule"].get(str(d.weekday()))
    briefs: list[str] = []

    if kind == "zscaler-update":
        nxt = zs.next_update(d)
        if nxt:
            key, snap, friday = nxt
            briefs.append(("zscaler-update", zs.update_brief(key, snap, friday)))
    elif kind == "zscaler-topic":
        briefs.append(("zscaler-topic", topic_brief("zscaler", used_topic_ids("zscaler"))))

    tcfg = cfg.get("trust") or {}
    for tkind, item in zs.pending_trust(tcfg.get("since", d.isoformat()), int(tcfg.get("daily_limit", 2))):
        briefs.append((f"zscaler-trust-{tkind}", zs.trust_brief(tkind, item)))

    if not briefs:
        why = "今週の製品別アップデートはすべて投稿済みか、更新がありませんでした。" if kind == "zscaler-update" else ""
        return (f"# zscaler ブログ {d.isoformat()}\n\n{why}今日は書く記事がありません"
                "（休みの日です）。何もしないで終了してください。")
    out = [f"# zscaler ブログ {d.isoformat()}: 今日は {len(briefs)} 本書いてください（下のブリーフ1つにつき記事1本）。\n"]
    for i, (k, body) in enumerate(briefs, 1):
        out.append("\n".join(_head("zscaler", d, k, i if len(briefs) > 1 else None)) + "\n" + body + "\n")
    return "\n---\n\n".join(out)


def build_today(site: str, d: date) -> str:
    if site == "zscaler":
        return build_zscaler_today(d)
    kind = site_config(site)["schedule"].get(str(d.weekday()))
    if not kind:
        return f"# {site} ブログ {d.isoformat()}\n\n今日は休みの日です。何もしないで終了してください。"
    used = used_topic_ids(site)
    head = _head(site, d, kind)
    if kind == "zscaler-digest":
        topic_id = f"digest-{d.isoformat()}"
        if topic_id in used:
            return "\n".join(head + ["本日分は既に作成済みです。何もしないで終了してください。"])
        body = f"推奨フロントマター: topic_id: {topic_id}\n\n" + collect_digest(7, d)
    elif kind == "zscaler-topic":
        body = topic_brief(site, used)
    else:
        raise SystemExit(f"unknown kind: {kind}")
    return "\n".join(head) + "\n" + body


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", choices=SITES, required=True)
    sub = ap.add_subparsers(dest="cmd", required=True)
    t = sub.add_parser("today"); t.add_argument("--date")
    g = sub.add_parser("digest"); g.add_argument("--days", type=int, default=7)
    sub.add_parser("topic")
    sub.add_parser("used")
    a = ap.parse_args()

    today = datetime.now(timezone(timedelta(hours=9))).date()  # 日本時間
    if a.cmd == "today":
        print(build_today(a.site, date.fromisoformat(a.date) if a.date else today))
    elif a.cmd == "digest":
        print(collect_digest(a.days, today))
    elif a.cmd == "topic":
        print(topic_brief(a.site, used_topic_ids(a.site)))
    elif a.cmd == "used":
        print("\n".join(sorted(used_topic_ids(a.site))))


if __name__ == "__main__":
    sys.exit(main())
