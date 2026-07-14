#!/usr/bin/env python3
"""
Zscaler公式サイト監視スクリプト
- 初回実行: 全ページをMDファイルとして初版保存（メール通知なし）
- 2回目以降: 差分を検出したページのみCHANGELOG.mdに追記＋メール通知
"""

import os
import base64
import smtplib
import difflib
import hashlib
import json
import time
from datetime import datetime, timezone
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

# ============================================================
# 設定
# ============================================================

GITHUB_TOKEN  = os.getenv("GITHUB_TOKEN", "")
GITHUB_OWNER  = os.getenv("GITHUB_OWNER", "")
GITHUB_REPO   = os.getenv("GITHUB_REPO",  "zscaler-monitor")
GITHUB_BRANCH = os.getenv("GITHUB_BRANCH", "main")

GMAIL_USER     = os.getenv("GMAIL_USER", "")
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD", "")
NOTIFY_TO      = os.getenv("NOTIFY_TO", GMAIL_USER)

FETCH_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/125.0.0.0 Safari/537.36"
    )
}

GITHUB_API = "https://api.github.com"

TARGETS = [
    {
        "id":       "zia_release_notes",
        "name":     "ZIA リリースノート",
        "url":      "https://help.zscaler.com/zia/release-notes",
        "selector": "article.field-items, div.field-body, main",
    },
    {
        "id":       "zpa_release_notes",
        "name":     "ZPA リリースノート",
        "url":      "https://help.zscaler.com/zpa/release-notes",
        "selector": "article.field-items, div.field-body, main",
    },
    {
        "id":       "zdx_release_notes",
        "name":     "ZDX リリースノート",
        "url":      "https://help.zscaler.com/zdx/release-notes",
        "selector": "article.field-items, div.field-body, main",
    },
    {
        "id":       "security_advisories",
        "name":     "セキュリティアドバイザリ",
        "url":      "https://trust.zscaler.com/",
        "selector": "main, #main-content, .content",
    },
    {
        "id":       "product_updates",
        "name":     "製品アップデート",
        "url":      "https://www.zscaler.com/products",
        "selector": "main, .main-content, article",
    },
]


# ============================================================
# GitHub API
# ============================================================

def _gh_headers() -> dict:
    return {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }


def gh_get_file(path: str) -> tuple[str, str]:
    """(content, sha) を返す。存在しなければ ('', '')"""
    url = f"{GITHUB_API}/repos/{GITHUB_OWNER}/{GITHUB_REPO}/contents/{path}"
    resp = requests.get(url, headers=_gh_headers(),
                        params={"ref": GITHUB_BRANCH}, timeout=15)
    if resp.status_code == 404:
        return "", ""
    resp.raise_for_status()
    data = resp.json()
    return base64.b64decode(data["content"]).decode("utf-8"), data["sha"]


def gh_put_file(path: str, content: str, sha: str, commit_msg: str) -> None:
    url = f"{GITHUB_API}/repos/{GITHUB_OWNER}/{GITHUB_REPO}/contents/{path}"
    payload: dict = {
        "message": commit_msg,
        "content": base64.b64encode(content.encode("utf-8")).decode("ascii"),
        "branch":  GITHUB_BRANCH,
    }
    if sha:
        payload["sha"] = sha
    resp = requests.put(url, headers=_gh_headers(), json=payload, timeout=15)
    resp.raise_for_status()


def load_state() -> tuple[dict, str]:
    content, sha = gh_get_file("state.json")
    return (json.loads(content) if content else {}), sha


def save_state(state: dict, sha: str) -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    gh_put_file("state.json",
                json.dumps(state, ensure_ascii=False, indent=2),
                sha,
                f"chore: update state [{now}]")


# ============================================================
# ページ取得
# ============================================================

def fetch_page(url: str, selector: str) -> str:
    resp = requests.get(url, headers=FETCH_HEADERS, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    element = None
    for sel in selector.split(", "):
        element = soup.select_one(sel.strip())
        if element:
            break
    if element is None:
        element = soup.body or soup
    for tag in element.select("script, style, nav, footer, header, iframe, noscript"):
        tag.decompose()
    return markdownify(str(element), heading_style="ATX").strip()


def compute_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# ============================================================
# 差分解析
# ============================================================

def extract_changes(old: str, new: str) -> dict:
    """追加行・削除行・変更見出しを抽出して返す"""
    old_lines = old.splitlines()
    new_lines  = new.splitlines()

    added    = []
    removed  = []
    headings = []

    matcher = difflib.SequenceMatcher(None, old_lines, new_lines)
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            continue
        if tag in ("replace", "insert"):
            for line in new_lines[j1:j2]:
                stripped = line.strip()
                if stripped.startswith("#"):
                    headings.append(stripped)
                elif stripped:
                    added.append(stripped)
        if tag in ("replace", "delete"):
            for line in old_lines[i1:i2]:
                stripped = line.strip()
                if stripped and not stripped.startswith("#"):
                    removed.append(stripped)

    return {
        "added":    added[:30],    # 最大30行
        "removed":  removed[:30],
        "headings": list(dict.fromkeys(headings))[:10],  # 重複除去・最大10件
    }


def build_unified_diff(old: str, new: str) -> str:
    diff = difflib.unified_diff(
        old.splitlines(keepends=True),
        new.splitlines(keepends=True),
        fromfile="前回", tofile="今回",
        lineterm="",
        n=3,
    )
    return "".join(list(diff)[:200])  # 最大200行


# ============================================================
# CHANGELOG更新
# ============================================================

def update_changelog(target_name: str, url: str,
                     changes: dict, now_str: str) -> None:
    changelog_path = "CHANGELOG.md"
    old_content, sha = gh_get_file(changelog_path)

    heading_text = ""
    if changes["headings"]:
        heading_text = "\n**更新セクション:**\n" + "\n".join(
            f"- {h}" for h in changes["headings"]
        )

    added_text = ""
    if changes["added"]:
        preview = changes["added"][:5]
        added_text = "\n**追加内容（抜粋）:**\n" + "\n".join(
            f"> {line}" for line in preview
        )
        if len(changes["added"]) > 5:
            added_text += f"\n> ...他 {len(changes['added']) - 5} 件"

    removed_text = ""
    if changes["removed"]:
        preview = changes["removed"][:3]
        removed_text = "\n**削除内容（抜粋）:**\n" + "\n".join(
            f"> ~~{line}~~" for line in preview
        )

    new_entry = (
        f"\n## {now_str} — {target_name}\n\n"
        f"ソース: [{url}]({url}){heading_text}{added_text}{removed_text}\n\n"
        "---"
    )

    if not old_content:
        full_content = "# Zscaler 更新履歴\n\n自動生成 by zscaler-monitor\n" + new_entry
    else:
        # 既存のchangelogの先頭見出しの直後に挿入
        lines = old_content.split("\n", 4)
        insert_after = min(3, len(lines))
        full_content = "\n".join(lines[:insert_after]) + new_entry + "\n" + "\n".join(lines[insert_after:])

    gh_put_file(changelog_path, full_content, sha,
                f"update: {target_name} changed [{now_str}]")


# ============================================================
# メール送信
# ============================================================

def _esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def send_email(subject: str, body_text: str, body_html: str) -> None:
    if not GMAIL_USER or not GMAIL_PASSWORD:
        print("  [WARN] Gmail未設定のためメール送信スキップ")
        return
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"]    = GMAIL_USER
    msg["To"]      = NOTIFY_TO
    msg.attach(MIMEText(body_text, "plain", "utf-8"))
    msg.attach(MIMEText(body_html, "html",  "utf-8"))
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        server.sendmail(GMAIL_USER, NOTIFY_TO, msg.as_string())
    print(f"  [OK] メール送信 → {NOTIFY_TO}")


def format_email(target_name: str, url: str, changes: dict,
                 diff_text: str, repo_url: str, now_str: str) -> tuple[str, str, str]:
    subject = f"[Zscaler更新通知] {target_name} ({now_str})"

    heading_lines = "\n".join(f"  ・{h}" for h in changes["headings"]) or "  （見出し変更なし）"
    added_lines   = "\n".join(f"  + {l}" for l in changes["added"][:10])   or "  （なし）"
    removed_lines = "\n".join(f"  - {l}" for l in changes["removed"][:5])  or "  （なし）"

    text = (
        f"Zscalerに更新が検出されました。\n\n"
        f"ページ : {target_name}\n"
        f"URL   : {url}\n"
        f"日時  : {now_str}\n\n"
        f"▼ 更新されたセクション\n{heading_lines}\n\n"
        f"▼ 追加された内容（抜粋）\n{added_lines}\n\n"
        f"▼ 削除された内容（抜粋）\n{removed_lines}\n\n"
        f"詳細はGitHubのCHANGELOG.mdを確認してください:\n{repo_url}\n"
    )

    # HTML版
    heading_html = "".join(f"<li>{_esc(h)}</li>" for h in changes["headings"]) or "<li>（見出し変更なし）</li>"
    added_html   = "".join(
        f'<li style="color:green">{_esc(l)}</li>'
        for l in changes["added"][:10]
    ) or "<li>（なし）</li>"
    removed_html = "".join(
        f'<li style="color:red;text-decoration:line-through">{_esc(l)}</li>'
        for l in changes["removed"][:5]
    ) or "<li>（なし）</li>"

    diff_html_lines = []
    for line in diff_text.splitlines():
        if line.startswith("+") and not line.startswith("+++"):
            diff_html_lines.append(f'<span style="color:green;background:#eaffea">{_esc(line)}</span>')
        elif line.startswith("-") and not line.startswith("---"):
            diff_html_lines.append(f'<span style="color:red;background:#ffeaea">{_esc(line)}</span>')
        elif line.startswith("@@"):
            diff_html_lines.append(f'<span style="color:#888">{_esc(line)}</span>')
        else:
            diff_html_lines.append(_esc(line))

    changelog_url = f"https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}/blob/{GITHUB_BRANCH}/CHANGELOG.md"

    html = f"""<!DOCTYPE html>
<html><body style="font-family:sans-serif;font-size:14px;max-width:800px">
<h2 style="color:#1a73e8">Zscaler更新通知</h2>
<table style="border-collapse:collapse;margin-bottom:16px">
  <tr><td style="padding:4px 12px 4px 0;font-weight:bold;color:#555">ページ</td>
      <td><a href="{url}">{_esc(target_name)}</a></td></tr>
  <tr><td style="padding:4px 12px 4px 0;font-weight:bold;color:#555">検出日時</td>
      <td>{now_str}</td></tr>
</table>

<h3 style="border-left:4px solid #1a73e8;padding-left:8px">更新されたセクション</h3>
<ul>{heading_html}</ul>

<h3 style="border-left:4px solid #34a853;padding-left:8px">追加された内容（抜粋）</h3>
<ul>{added_html}</ul>

<h3 style="border-left:4px solid #ea4335;padding-left:8px">削除された内容（抜粋）</h3>
<ul>{removed_html}</ul>

<h3>詳細diff</h3>
<pre style="background:#f8f8f8;padding:12px;border-radius:4px;font-size:12px;overflow-x:auto;white-space:pre-wrap">{"<br>".join(diff_html_lines)}</pre>

<p style="color:#666;font-size:12px">
  全更新履歴: <a href="{changelog_url}">CHANGELOG.md</a> |
  最新MD: <a href="{repo_url}">{target_name}.md</a>
</p>
</body></html>"""

    return subject, text, html


# ============================================================
# メイン処理
# ============================================================

def check_target(target: dict, state: dict) -> str:
    """
    'init'   : 初版保存（メールなし）
    'updated': 更新検出（メールあり）
    'no_change': 変更なし
    'error'  : エラー
    """
    tid  = target["id"]
    name = target["name"]
    url  = target["url"]
    print(f"チェック中: {name}")

    try:
        new_content = fetch_page(url, target["selector"])
    except Exception as e:
        print(f"  [ERROR] フェッチ失敗: {e}")
        return "error"

    new_hash = compute_hash(new_content)
    old_hash = state.get(tid, {}).get("hash", "")
    is_first = not bool(old_hash)

    if not is_first and new_hash == old_hash:
        print("  変更なし")
        return "no_change"

    # GitHubの既存MDを取得
    gh_path = f"docs/zscaler_{tid}.md"
    old_md, old_sha = gh_get_file(gh_path)

    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    # 新MDを作成してGitHubへ保存
    new_md = (
        f"# {name}\n\n"
        f"> 最終更新: {now_str}  \n"
        f"> ソース: {url}\n\n"
        "---\n\n"
    ) + new_content

    commit_prefix = "init" if is_first else "update"
    gh_put_file(gh_path, new_md, old_sha, f"{commit_prefix}({tid}): {now_str}")
    gh_file_url = f"https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}/blob/{GITHUB_BRANCH}/{gh_path}"

    if is_first:
        print(f"  初版保存: {gh_file_url}")
    else:
        # 変更内容を解析
        changes    = extract_changes(old_md, new_content)
        diff_text  = build_unified_diff(old_md, new_content)

        # CHANGELOG更新
        update_changelog(name, url, changes, now_str)

        # メール送信
        subj, txt, html_body = format_email(name, url, changes, diff_text,
                                            gh_file_url, now_str)
        send_email(subj, txt, html_body)
        print(f"  更新検出・通知完了: {gh_file_url}")

    # ステート更新
    state[tid] = {
        "hash":         new_hash,
        "last_checked": datetime.now(timezone.utc).isoformat(),
        "last_updated": datetime.now(timezone.utc).isoformat(),
        "initialized":  True,
    }
    return "init" if is_first else "updated"


def main():
    print(f"=== Zscaler監視開始 {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')} ===")

    if not GITHUB_TOKEN or not GITHUB_OWNER:
        raise SystemExit("[ERROR] GITHUB_TOKEN / GITHUB_OWNER が未設定です。")

    state, state_sha = load_state()
    counts = {"init": 0, "updated": 0, "no_change": 0, "error": 0}

    for target in TARGETS:
        result = check_target(target, state)
        counts[result] = counts.get(result, 0) + 1
        time.sleep(2)

    save_state(state, state_sha)

    print(f"\n完了 — 初版保存: {counts['init']} / 更新検出: {counts['updated']} / "
          f"変更なし: {counts['no_change']} / エラー: {counts['error']}")


if __name__ == "__main__":
    main()
