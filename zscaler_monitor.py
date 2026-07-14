#!/usr/bin/env python3
"""
Zscaler公式サイト監視スクリプト
- リリースノート・製品アップデート・セキュリティアドバイザリを監視
- 更新があればGitHubリポジトリのMDファイルを更新
- 差分をGmail SMTPでメール通知
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

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).parent / ".env")

# ============================================================
# 設定
# ============================================================

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
GITHUB_OWNER = os.getenv("GITHUB_OWNER", "")   # GitHubユーザー名
GITHUB_REPO  = os.getenv("GITHUB_REPO",  "zscaler-monitor")
GITHUB_BRANCH = os.getenv("GITHUB_BRANCH", "main")

GMAIL_USER     = os.getenv("GMAIL_USER", "")
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD", "")  # Gmailアプリパスワード
NOTIFY_TO      = os.getenv("NOTIFY_TO", GMAIL_USER)

FETCH_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/125.0.0.0 Safari/537.36"
    )
}

GITHUB_API = "https://api.github.com"

# 監視対象ページ定義
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
    """GitHubからファイルを取得。(content, sha) を返す。存在しなければ ('', '')"""
    url = f"{GITHUB_API}/repos/{GITHUB_OWNER}/{GITHUB_REPO}/contents/{path}"
    resp = requests.get(url, headers=_gh_headers(),
                        params={"ref": GITHUB_BRANCH}, timeout=15)
    if resp.status_code == 404:
        return "", ""
    resp.raise_for_status()
    data = resp.json()
    content = base64.b64decode(data["content"]).decode("utf-8")
    return content, data["sha"]


def gh_put_file(path: str, content: str, sha: str, commit_msg: str) -> None:
    """GitHubにファイルを作成 or 更新する"""
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


def load_state() -> dict:
    content, _ = gh_get_file("state.json")
    if content:
        return json.loads(content)
    return {}


def save_state(state: dict, old_sha: str) -> None:
    gh_put_file(
        "state.json",
        json.dumps(state, ensure_ascii=False, indent=2),
        old_sha,
        f"chore: update state [{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}]",
    )


# ============================================================
# Zscalerページ取得
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


def build_diff(old: str, new: str) -> str:
    diff = difflib.unified_diff(
        old.splitlines(keepends=True),
        new.splitlines(keepends=True),
        fromfile="前回", tofile="今回",
        lineterm="",
    )
    return "".join(diff)


# ============================================================
# メール送信
# ============================================================

def send_email(subject: str, body_text: str, body_html: str) -> None:
    if not GMAIL_USER or not GMAIL_PASSWORD:
        print("  [WARN] Gmailの認証情報が未設定のためメール送信をスキップします")
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

    print(f"  [OK] メール送信完了 → {NOTIFY_TO}")


def _esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def format_email(target_name: str, url: str, diff_text: str,
                 repo_url: str) -> tuple[str, str, str]:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    subject = f"[Zscaler更新通知] {target_name} ({now})"

    text = (
        f"Zscaler公式サイトに更新が検出されました。\n\n"
        f"ページ : {target_name}\n"
        f"URL   : {url}\n"
        f"日時  : {now}\n"
        f"GitHub: {repo_url}\n\n"
        f"--- 差分 ---\n{diff_text}\n"
    )

    diff_html_lines = []
    for line in diff_text.splitlines():
        if line.startswith("+") and not line.startswith("+++"):
            diff_html_lines.append(
                f'<span style="color:green;background:#eaffea">{_esc(line)}</span>'
            )
        elif line.startswith("-") and not line.startswith("---"):
            diff_html_lines.append(
                f'<span style="color:red;background:#ffeaea">{_esc(line)}</span>'
            )
        elif line.startswith("@@"):
            diff_html_lines.append(f'<span style="color:#888">{_esc(line)}</span>')
        else:
            diff_html_lines.append(_esc(line))

    html = f"""<!DOCTYPE html>
<html><body style="font-family:sans-serif;font-size:14px">
<h2>Zscaler更新通知</h2>
<table style="border-collapse:collapse">
  <tr><td style="padding:4px 8px;font-weight:bold">ページ</td>
      <td style="padding:4px 8px">{_esc(target_name)}</td></tr>
  <tr><td style="padding:4px 8px;font-weight:bold">URL</td>
      <td style="padding:4px 8px"><a href="{url}">{url}</a></td></tr>
  <tr><td style="padding:4px 8px;font-weight:bold">検出日時</td>
      <td style="padding:4px 8px">{now}</td></tr>
  <tr><td style="padding:4px 8px;font-weight:bold">GitHub</td>
      <td style="padding:4px 8px"><a href="{repo_url}">{repo_url}</a></td></tr>
</table>
<h3>差分</h3>
<pre style="background:#f5f5f5;padding:12px;border-radius:4px;overflow-x:auto;white-space:pre-wrap">{"<br>".join(diff_html_lines)}</pre>
</body></html>"""

    return subject, text, html


# ============================================================
# メイン
# ============================================================

def check_target(target: dict, state: dict) -> bool:
    tid  = target["id"]
    name = target["name"]
    url  = target["url"]
    print(f"チェック中: {name}")

    try:
        new_content = fetch_page(url, target["selector"])
    except Exception as e:
        print(f"  [ERROR] フェッチ失敗: {e}")
        return False

    new_hash = compute_hash(new_content)
    old_hash = state.get(tid, {}).get("hash", "")

    if new_hash == old_hash:
        print("  変更なし")
        return False

    # GitHubから旧MDを取得
    gh_path = f"docs/zscaler_{tid}.md"
    old_md, old_sha = gh_get_file(gh_path)
    diff_text = build_diff(old_md, new_content)

    # 新MDをGitHubへ保存
    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    new_md = (
        f"# {name}\n\n"
        f"> 最終更新: {now_str}  \n"
        f"> ソース: {url}\n\n"
        "---\n\n"
    ) + new_content

    gh_put_file(
        gh_path, new_md, old_sha,
        f"update({tid}): {now_str}",
    )
    repo_url = f"https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}/blob/{GITHUB_BRANCH}/{gh_path}"
    print(f"  GitHub更新: {repo_url}")

    # メール送信
    subj, txt, html_body = format_email(name, url, diff_text, repo_url)
    send_email(subj, txt, html_body)

    state[tid] = {
        "hash":         new_hash,
        "last_checked": datetime.now(timezone.utc).isoformat(),
        "last_updated": datetime.now(timezone.utc).isoformat(),
    }
    return True


def main():
    print(f"=== Zscaler監視開始 {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')} ===")

    if not GITHUB_TOKEN or not GITHUB_OWNER:
        raise SystemExit("[ERROR] GITHUB_TOKEN / GITHUB_OWNER が未設定です。.env を確認してください。")

    state_content, state_sha = gh_get_file("state.json")
    state = json.loads(state_content) if state_content else {}
    updated = 0

    for target in TARGETS:
        try:
            if check_target(target, state):
                updated += 1
        except Exception as e:
            print(f"  [ERROR] {target['name']}: {e}")
        time.sleep(2)

    save_state(state, state_sha)
    print(f"\n完了: {updated}/{len(TARGETS)} ページで更新を検出")


if __name__ == "__main__":
    main()
