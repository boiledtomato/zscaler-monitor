#!/usr/bin/env python3
"""
Claude API で記事を1本生成する（GitHub Actions 用の「APIモード」）。

  ANTHROPIC_API_KEY=... python3 scripts/generate_post.py --site zscaler [--date YYYY-MM-DD]
  ANTHROPIC_API_KEY=... python3 scripts/generate_post.py --site art

※ Claude Code のスケジュール実行（推奨・追加料金なし）を使う場合、このスクリプトは不要です。
  その場合はセッション内の Claude が blogs/SCHEDULED_TASK_PROMPT.md に従って直接記事を書きます。

環境変数:
  BLOG_MODEL   使用モデル（既定: claude-opus-5-5）
  BLOG_EFFORT  low / medium / high（既定: medium）
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import anthropic

sys.path.insert(0, str(Path(__file__).resolve().parent))
import blog_sources  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
MODEL = os.environ.get("BLOG_MODEL", "claude-opus-5-5")
EFFORT = os.environ.get("BLOG_EFFORT", "medium")
PRICES = {  # USD / 1M tokens (input, output)
    "claude-opus-5-5": (4.0, 20.0),
    "claude-sonnet-5-5": (2.0, 10.0),
    "claude-haiku-5-5": (0.10, 0.50),
}

SYSTEM = """あなたは日本語ブログの執筆者です。
添付の執筆ガイドに厳密に従い、記事ファイル1本分（フロントマター付き Markdown）だけを出力してください。
前置き・後書き・コードフェンスは付けないでください。出力の1行目は必ず '---' です。
提供された資料と確立した知識に基づいて書き、不確かな細部は書かないか「公式ドキュメントで要確認」と明記してください。
資料中のURLの内容を確認したい場合は web_fetch ツールを使ってかまいません。"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", choices=blog_sources.SITES, required=True)
    ap.add_argument("--date")
    a = ap.parse_args()
    blog = ROOT / "blogs" / a.site
    d = date.fromisoformat(a.date) if a.date else datetime.now(timezone(timedelta(hours=9))).date()

    brief = blog_sources.build_today(a.site, d)
    if "何もしないで終了" in brief:
        print(brief)
        return 0
    guide = ((ROOT / "blogs" / "WRITING_RULES_COMMON.md").read_text(encoding="utf-8") + "\n\n"
             + (blog / "WRITING_GUIDE.md").read_text(encoding="utf-8"))

    client = anthropic.Anthropic()
    messages = [{"role": "user", "content": f"# 執筆ガイド\n\n{guide}\n\n---\n\n{brief}\n\n日付は {d.isoformat()} としてください。"}]
    tools = [{
        "type": "web_fetch_20260209", "name": "web_fetch", "max_uses": 5,
        "allowed_domains": ["help.zscaler.com", "trust.zscaler.com", "zscaler.com", "metmuseum.org"],
    }]

    usage_in = usage_out = 0
    response = None
    for _ in range(5):  # pause_turn が返った場合は続きを要求する
        with client.beta.messages.stream(
            model=MODEL,
            max_tokens=32000,
            system=SYSTEM,
            thinking={"type": "adaptive"},
            output_config={"effort": EFFORT},
            tools=tools,
            messages=messages,
            betas=["server-side-fallback-2026-07-01"],
            extra_body={"fallbacks": "default"},
        ) as stream:
            response = stream.get_final_message()
        usage_in += response.usage.input_tokens + (response.usage.cache_read_input_tokens or 0)
        usage_out += response.usage.output_tokens
        if response.stop_reason == "pause_turn":
            messages.append({"role": "assistant", "content": response.content})
            continue
        break

    if response is None or response.stop_reason == "refusal":
        print(f"生成できませんでした: stop_reason={getattr(response, 'stop_reason', None)}", file=sys.stderr)
        return 1

    text = "".join(b.text for b in response.content if b.type == "text").strip()
    text = re.sub(r"^```(?:markdown|md)?\n|\n```$", "", text).strip()
    start = text.find("---\n")
    if start < 0:
        print("フロントマターが見つかりません:\n" + text[:500], file=sys.stderr)
        return 1
    text = text[start:] + "\n"

    fm = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    title_slug = "post"
    if fm:
        m = re.search(r"^topic_id:\s*\"?([\w-]+)", fm.group(1), re.M)
        if m:
            title_slug = m.group(1)
    out = blog / "content" / "posts" / f"{d.isoformat()}-{title_slug}.md"
    out.write_text(text, encoding="utf-8")

    check = subprocess.run([sys.executable, str(ROOT / "scripts" / "build_site.py"), "--site", a.site, "--check"],
                           capture_output=True, text=True)
    if check.returncode != 0:
        print(check.stderr, file=sys.stderr)
        out.unlink()
        return 1

    pin, pout = PRICES.get(MODEL, PRICES["claude-opus-5-5"])
    usd = usage_in / 1e6 * pin + usage_out / 1e6 * pout
    costs_path = blog / "data" / "costs.json"
    costs = json.loads(costs_path.read_text(encoding="utf-8"))
    costs["entries"].append({"date": d.isoformat(), "post": out.name, "model": response.model,
                             "input_tokens": usage_in, "output_tokens": usage_out, "usd": round(usd, 4)})
    costs_path.write_text(json.dumps(costs, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)}  (~${usd:.3f})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
