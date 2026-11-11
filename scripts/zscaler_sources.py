#!/usr/bin/env python3
"""
Zscaler ブログ用の材料集め（製品別アップデートと Trust 記事）。

  # 金曜日時点の製品別スナップショットを作る（前週金曜〜木曜の7日分）
  python3 scripts/zscaler_sources.py snapshot --friday 2026-11-13

  # Trust（trust.zscaler.com）から、まだ記事にしていない障害・脆弱性を一覧
  python3 scripts/zscaler_sources.py trust

blog_sources.py の `today` からも呼ばれる。リリースノートのページは JavaScript で描画されるため、
scripts/release_notes_extract.js（Playwright）で本文を取り出す。
"""

from __future__ import annotations

import argparse
import html
import json
import re
import subprocess
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, timedelta
from email.utils import parsedate_to_datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BLOG = ROOT / "blogs" / "zscaler"
WEEKLY_DIR = BLOG / "data" / "weekly"

# 製品別アップデートの投稿順（金→土→月→火）。更新がない製品は飛ばす
PRODUCTS = {
    "zcc": {
        "name": "Zscaler Client Connector（ZCC）",
        "pages": ["zscaler-client-connector/client-connector-app-release-summary-{y}",
                  "zscaler-client-connector/release-upgrade-summary-{y}"],
    },
    "zia": {
        "name": "Zscaler Internet Access（ZIA）",
        "pages": ["zia/release-upgrade-summary-{y}"],
    },
    "zpa": {
        "name": "Zscaler Private Access（ZPA）",
        "pages": ["zpa/release-upgrade-summary-{y}",
                  "zpa/app-connector-release-summary-{y}",
                  "zpa/zpa-private-service-edge-release-summary-{y}"],
    },
    "zdx": {
        "name": "Zscaler Digital Experience（ZDX）",
        "pages": ["zdx/release-upgrade-summary-{y}",
                  "zscaler-client-connector/zdx-module-release-summary-{y}"],
    },
}

TRUST_RSS = "https://trust.zscaler.com/rss-feed"


# ------------------------------------------------------------------ helpers

def used_topic_ids() -> set[str]:
    ids = set()
    for p in (BLOG / "content" / "posts").glob("*.md"):
        m = re.search(r"^topic_id:\s*(\S+)", p.read_text(encoding="utf-8"), re.M)
        if m:
            ids.add(m.group(1).strip("\"'"))
    return ids


def http_get(url: str) -> str:
    import ssl
    ctx = ssl.create_default_context()
    ca = Path("/root/.ccr/ca-bundle.crt")
    if ca.exists():
        ctx.load_verify_locations(str(ca))
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (personal-blog-builder)"})
    with urllib.request.urlopen(req, timeout=60, context=ctx) as r:
        return r.read().decode("utf-8", errors="replace")


def week_friday(d: date) -> date:
    """d 以前で最も近い金曜日（d が金曜ならその日）。"""
    return d - timedelta(days=(d.weekday() - 4) % 7)


# ------------------------------------------------------------------ weekly snapshot

def snapshot_path(friday: date) -> Path:
    return WEEKLY_DIR / f"{friday.isoformat()}.json"


def make_snapshot(friday: date) -> dict:
    """前週金曜〜木曜（friday-7 〜 friday-1）にデプロイされた項目を製品別に保存する。"""
    since, until = friday - timedelta(days=7), friday - timedelta(days=1)
    years = sorted({since.year, until.year})
    snap = {"friday": friday.isoformat(), "since": since.isoformat(), "until": until.isoformat(),
            "products": {}}
    for key, prod in PRODUCTS.items():
        paths = [p.format(y=y) for p in prod["pages"] for y in years]
        out = subprocess.run(
            ["node", str(ROOT / "scripts" / "release_notes_extract.js"), since.isoformat(), until.isoformat(), *paths],
            capture_output=True, text=True, timeout=900)
        if out.returncode != 0:
            raise RuntimeError(f"{key}: release_notes_extract.js failed: {out.stderr[-500:]}")
        pages = json.loads(out.stdout)
        # OS別に同じ項目が出ることがあるので、日付+タイトル+本文で重複を除き、OS名をまとめる
        merged: dict[tuple, dict] = {}
        errors = []
        for pg in pages:
            if pg.get("error"):
                errors.append(f"{pg['page']}: {pg['error']}")
            for e in pg["entries"]:
                k = (e["date"], e["title"], e["text"][:200])
                item = merged.setdefault(k, {**e, "page": pg["url"], "cloud": pg.get("cloud", ""), "platforms": []})
                if pg.get("platform") and pg["platform"] not in item["platforms"]:
                    item["platforms"].append(pg["platform"])
        snap["products"][key] = {"name": prod["name"], "entries": sorted(merged.values(), key=lambda x: x["date"]),
                                 "errors": errors, "pages": [f"https://help.zscaler.com/{p}" for p in paths]}
    WEEKLY_DIR.mkdir(parents=True, exist_ok=True)
    snapshot_path(friday).write_text(json.dumps(snap, ensure_ascii=False, indent=1), encoding="utf-8")
    return snap


def load_or_make_snapshot(friday: date) -> dict:
    p = snapshot_path(friday)
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    return make_snapshot(friday)


def next_update(d: date) -> tuple[str, dict, date] | None:
    """今週のスナップショットから、まだ書いていない（更新のある）製品を投稿順に1つ返す。"""
    friday = week_friday(d)
    snap = load_or_make_snapshot(friday)
    used = used_topic_ids()
    for key in PRODUCTS:
        prod = snap["products"].get(key) or {}
        if prod.get("entries") and f"update-{key}-{friday.isoformat()}" not in used:
            return key, snap, friday
    return None


def update_brief(key: str, snap: dict, friday: date) -> str:
    prod = snap["products"][key]
    others = [k for k in PRODUCTS if (snap["products"].get(k) or {}).get("entries")]
    lines = [
        f"## {prod['name']} 週次アップデート（{snap['since']} 〜 {snap['until']} のデプロイ分）",
        "",
        f"推奨フロントマター: topic_id: update-{key}-{friday.isoformat()}",
        f"今週のシリーズ: {' → '.join(PRODUCTS[k]['name'] for k in others)}（金・土・月・火の順に1製品ずつ）",
        f"取得元ページ: {', '.join(prod['pages'])}",
    ]
    if prod.get("errors"):
        lines.append(f"⚠ 取得に失敗したページ: {'; '.join(prod['errors'])}（記事で触れる必要はないが、報告に書くこと）")
    lines.append(f"\n全{len(prod['entries'])}件。本文は公式リリースノートからの抜粋（英語）。\n")
    for i, e in enumerate(prod["entries"], 1):
        where = f"OS: {', '.join(e['platforms'])}" if e.get("platforms") else f"クラウド表示: {e.get('cloud') or '-'}"
        lines += [
            f"### {i}. {e['title']}",
            f"- デプロイ日: {e['date']} / 区分: {e['category']} / {where}",
            f"- 掲載ページ: {e['page']}{'#' + e['anchor'] if e.get('anchor') else ''}",
            f"- 関連ドキュメント: {', '.join(e.get('links') or []) or 'なし'}",
            "",
            e["text"],
            "",
        ]
    return "\n".join(lines)


# ------------------------------------------------------------------ trust

def _clean(s: str) -> str:
    s = html.unescape(s or "")
    s = re.sub(r"<br\s*/?>|</p>|</li>", "\n", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s).replace("\xa0", " ")
    return re.sub(r"[ \t]+", " ", re.sub(r"\n\s*\n+", "\n", s)).strip()


def trust_items() -> list[dict]:
    root = ET.fromstring(http_get(TRUST_RSS))
    items = []
    for it in root.findall(".//item"):
        get = lambda k: (it.findtext(k) or "").strip()
        m = re.search(r"/posts/(\d+)", get("link"))
        if not m:
            continue
        items.append({
            "id": m.group(1), "title": get("title"), "link": get("link"),
            "category": get("category"), "status": get("Status"), "event_type": get("eventType"),
            "published": parsedate_to_datetime(get("pubDate")).date().isoformat() if get("pubDate") else "",
            "start": get("startTime"), "end": get("endTime"), "resolved": get("ResolvedDate"),
            "impact": get("customerImpact"), "how_found": get("HowFound"),
            "workaround": get("availableWorkaround"), "description": _clean(get("description")),
        })
    return items


def classify(item: dict) -> str | None:
    """記事にする対象かどうか。vuln（脆弱性）/ incident（障害）/ None。"""
    if "CVE-" in item["title"] or "vulnerab" in item["title"].lower():
        return "vuln"
    if (item["category"] == "Recent incident" and item["status"] == "Resolved"
            and re.search(r"root cause", item["description"], re.I)):
        return "incident"
    return None


def pending_trust(since: str, limit: int) -> list[tuple[str, dict]]:
    used = used_topic_ids()
    out = []
    for it in sorted(trust_items(), key=lambda x: x["published"]):
        kind = classify(it)
        if kind and it["published"] >= since and f"trust-{it['id']}" not in used:
            out.append((kind, it))
    # 脆弱性を優先し、1日あたり limit 件まで
    out.sort(key=lambda x: (x[0] != "vuln", x[1]["published"]))
    return out[:limit]


def trust_brief(kind: str, it: dict) -> str:
    label = "脆弱性（CVE）への Zscaler の対応" if kind == "vuln" else "障害（インシデント）の振り返り"
    lines = [
        f"## Trust 記事: {label}",
        "",
        f"推奨フロントマター: topic_id: trust-{it['id']}",
        f"- タイトル（原文）: {it['title']}",
        f"- URL: {it['link']}",
        f"- カテゴリ: {it['category']} / ステータス: {it['status'] or '-'} / 種別: {it['event_type'] or '-'}",
        f"- 公開: {it['published']} / 開始: {it['start'] or '-'} / 終了: {it['end'] or '-'} / 解決: {it['resolved'] or '-'}",
        f"- 影響（原文）: {it['impact'] or '-'}",
        f"- 検知経路: {it['how_found'] or '-'} / 回避策: {it['workaround'] or '-'}",
        "",
        "### 本文（原文）",
        it["description"][:6000],
    ]
    return "\n".join(lines)


# ------------------------------------------------------------------ main

def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("snapshot"); s.add_argument("--friday", required=True)
    t = sub.add_parser("trust"); t.add_argument("--since", default="2026-11-09"); t.add_argument("--limit", type=int, default=2)
    a = ap.parse_args()
    if a.cmd == "snapshot":
        snap = make_snapshot(date.fromisoformat(a.friday))
        for k, v in snap["products"].items():
            print(f"{k}: {len(v['entries'])} entries" + (f" (errors: {v['errors']})" if v["errors"] else ""))
    elif a.cmd == "trust":
        for kind, it in pending_trust(a.since, a.limit):
            print(trust_brief(kind, it), "\n")


if __name__ == "__main__":
    sys.exit(main())
