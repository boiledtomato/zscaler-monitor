#!/usr/bin/env python3
"""
Zscaler公式サイト監視スクリプト（改訂版）
- GitHub: git clone/commit/push
- ページ取得: sitemap.xml (ZIA/ZPA/ZDX) / RSS (trust) / 静的HTML (products)
- メール: SMTPプロキシ経由（失敗時はログのみ）
"""

import base64
import difflib
import hashlib
import json
import os
import re
import smtplib
import socket
import ssl
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
import urllib.request
import urllib.error
from datetime import datetime, timezone
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

# ============================================================
# 設定
# ============================================================

GITHUB_TOKEN  = "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"
GITHUB_OWNER  = "boiledtomato"
GITHUB_REPO   = "zscaler-monitor"
GITHUB_BRANCH = "main"

GMAIL_USER     = "ciderred1239@gmail.com"
GMAIL_PASSWORD = "hiiesyutijefmlcz"
NOTIFY_TO      = "ciderred1239@gmail.com"

CA_CERT   = "/root/.ccr/ca-bundle.crt"
REPO_DIR  = Path("/tmp/zscaler-monitor-repo")
REPO_URL  = f"https://{GITHUB_TOKEN}@github.com/{GITHUB_OWNER}/{GITHUB_REPO}.git"

TARGETS = [
    {
        "id":   "zia_release_notes",
        "name": "ZIA リリースノート",
        "url":  "https://help.zscaler.com/zia/release-notes",
        "type": "sitemap",
        "product_prefix": "zia",
    },
    {
        "id":   "zpa_release_notes",
        "name": "ZPA リリースノート",
        "url":  "https://help.zscaler.com/zpa/release-notes",
        "type": "sitemap",
        "product_prefix": "zpa",
    },
    {
        "id":   "zdx_release_notes",
        "name": "ZDX リリースノート",
        "url":  "https://help.zscaler.com/zdx/release-notes",
        "type": "sitemap",
        "product_prefix": "zdx",
    },
    {
        "id":   "security_advisories",
        "name": "セキュリティアドバイザリ",
        "url":  "https://trust.zscaler.com/",
        "type": "trust_rss",
    },
    {
        "id":   "product_updates",
        "name": "製品アップデート",
        "url":  "https://www.zscaler.com/products",
        "type": "static_html",
    },
]


# ============================================================
# HTTP ユーティリティ
# ============================================================

def _ssl_ctx():
    ctx = ssl.create_default_context(cafile=CA_CERT if os.path.exists(CA_CERT) else None)
    return ctx


def http_get(url, extra_headers=None, timeout=30) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
        "Accept": "*/*",
    }
    if extra_headers:
        headers.update(extra_headers)
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, context=_ssl_ctx(), timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


# ============================================================
# ページ取得
# ============================================================

def fetch_sitemap_content(product_prefix: str) -> str:
    """sitemap.xmlからproductのリリースページ一覧をテキストで返す"""
    xml_text = http_get("https://help.zscaler.com/sitemap.xml")
    tree = ET.fromstring(xml_text)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

    pages = []
    for url_el in tree.findall("sm:url", ns):
        loc = url_el.find("sm:loc", ns)
        lastmod = url_el.find("sm:lastmod", ns)
        if loc is not None:
            loc_text = loc.text or ""
            if f"/{product_prefix}/" in loc_text and "release" in loc_text:
                pages.append({
                    "url": loc_text,
                    "lastmod": lastmod.text if lastmod is not None else "",
                })
    pages.sort(key=lambda x: x["lastmod"], reverse=True)

    lines = [f"# {product_prefix.upper()} リリースノート ページ一覧 (sitemap)\n"]
    for p in pages[:30]:
        lines.append(f"- {p['lastmod']} | {p['url']}")

    # 最新5件のページ詳細も追記
    for p in pages[:5]:
        try:
            detail = http_get(p["url"], timeout=15)
            excerpt = detail[:200].replace("\n", " ")
        except Exception:
            excerpt = "(取得不可)"
        lines.append(f"\n## {p['url']}\n最終更新: {p['lastmod']}\n")

    return "\n".join(lines)


def fetch_trust_rss() -> str:
    """trust.zscaler.com RSSフィードを取得してテキスト化"""
    rss_text = http_get("https://trust.zscaler.com/rss-feed")

    # XMLをパース
    try:
        tree = ET.fromstring(rss_text)
        items = tree.findall(".//item")
        lines = ["# Zscaler Trust - インシデント/アドバイザリ RSS\n"]
        for item in items[:20]:
            title = item.findtext("title", "")
            pub = item.findtext("pubDate", "")
            link = item.findtext("link", "")
            status = item.findtext("Status", "")
            category = item.findtext("category", "")
            impact = item.findtext("customerImpact", "")
            desc_raw = item.findtext("description", "")
            # HTMLタグを除去
            desc = re.sub(r"<[^>]+>", " ", desc_raw)
            desc = re.sub(r"\s+", " ", desc).strip()
            lines.append(
                f"## {title}\n"
                f"- 公開: {pub}\n"
                f"- ステータス: {status}  カテゴリ: {category}\n"
                f"- URL: {link}\n"
                f"- 影響: {impact}\n\n"
                f"{desc[:500]}\n\n---\n"
            )
        return "\n".join(lines)
    except Exception:
        return rss_text[:5000]


def fetch_products_static() -> str:
    """www.zscaler.com/products の静的コンテンツを取得"""
    html = http_get("https://www.zscaler.com/products", timeout=30)
    clean = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.DOTALL)
    clean = re.sub(r"<style[^>]*>.*?</style>", "", clean, flags=re.DOTALL)
    clean = re.sub(r"<[^>]+>", " ", clean)
    clean = re.sub(r"\s+", " ", clean).strip()
    return clean[:8000]


def fetch_page(target: dict) -> str:
    t = target["type"]
    if t == "sitemap":
        return fetch_sitemap_content(target["product_prefix"])
    elif t == "trust_rss":
        return fetch_trust_rss()
    elif t == "static_html":
        return fetch_products_static()
    raise ValueError(f"Unknown type: {t}")


def compute_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# ============================================================
# Git 操作
# ============================================================

def _git(args: list, cwd=None) -> str:
    env = os.environ.copy()
    env["GIT_TERMINAL_PROMPT"] = "0"
    result = subprocess.run(
        ["git"] + args,
        cwd=str(cwd or REPO_DIR),
        capture_output=True,
        text=True,
        env=env,
    )
    if result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {result.stderr}")
    return result.stdout.strip()


def setup_repo() -> None:
    if REPO_DIR.exists():
        try:
            _git(["fetch", "origin", GITHUB_BRANCH])
            _git(["reset", "--hard", f"origin/{GITHUB_BRANCH}"])
            print("  [git] リポジトリ更新完了")
            return
        except Exception:
            import shutil
            shutil.rmtree(REPO_DIR)

    REPO_DIR.mkdir(parents=True, exist_ok=True)
    _git(["clone", "--depth=1", "-b", GITHUB_BRANCH, REPO_URL, str(REPO_DIR)], cwd="/tmp")
    print(f"  [git] クローン完了: {REPO_DIR}")


def configure_git() -> None:
    _git(["config", "user.email", "monitor-bot@zscaler-monitor.local"])
    _git(["config", "user.name", "Zscaler Monitor Bot"])


def commit_and_push(message: str) -> None:
    try:
        _git(["add", "-A"])
        status = _git(["status", "--porcelain"])
        if not status:
            print("  [git] 変更なし、コミットスキップ")
            return
        _git(["commit", "-m", message])
        for attempt in range(4):
            try:
                _git(["push", "-u", "origin", GITHUB_BRANCH])
                print(f"  [git] プッシュ完了")
                return
            except Exception as e:
                if attempt < 3:
                    wait = 2 ** (attempt + 1)
                    print(f"  [git] プッシュ失敗、{wait}秒後リトライ: {e}")
                    time.sleep(wait)
                else:
                    raise
    except Exception as e:
        print(f"  [git] コミット/プッシュエラー: {e}")


# ============================================================
# ファイル操作（REPO_DIR内）
# ============================================================

def read_file(rel_path: str) -> str:
    p = REPO_DIR / rel_path
    return p.read_text(encoding="utf-8") if p.exists() else ""


def write_file(rel_path: str, content: str) -> None:
    p = REPO_DIR / rel_path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")


def load_state() -> dict:
    content = read_file("state.json")
    return json.loads(content) if content else {}


def save_state(state: dict) -> None:
    write_file("state.json", json.dumps(state, ensure_ascii=False, indent=2))


# ============================================================
# 差分解析
# ============================================================

def extract_changes(old: str, new: str) -> dict:
    old_lines = old.splitlines()
    new_lines  = new.splitlines()
    added = []
    removed = []
    headings = []
    matcher = difflib.SequenceMatcher(None, old_lines, new_lines)
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            continue
        if tag in ("replace", "insert"):
            for line in new_lines[j1:j2]:
                s = line.strip()
                if s.startswith("#"):
                    headings.append(s)
                elif s:
                    added.append(s)
        if tag in ("replace", "delete"):
            for line in old_lines[i1:i2]:
                s = line.strip()
                if s and not s.startswith("#"):
                    removed.append(s)
    return {
        "added":    added[:30],
        "removed":  removed[:30],
        "headings": list(dict.fromkeys(headings))[:10],
    }


def build_diff(old: str, new: str) -> str:
    diff = difflib.unified_diff(
        old.splitlines(keepends=True),
        new.splitlines(keepends=True),
        fromfile="前回", tofile="今回",
        n=3,
    )
    return "".join(list(diff)[:200])


# ============================================================
# CHANGELOG更新
# ============================================================

def update_changelog(target_name: str, url: str, changes: dict, now_str: str) -> None:
    path = "CHANGELOG.md"
    old = read_file(path)

    h_text = ""
    if changes["headings"]:
        h_text = "\n**更新セクション:**\n" + "\n".join(f"- {h}" for h in changes["headings"])

    a_text = ""
    if changes["added"]:
        preview = changes["added"][:5]
        a_text = "\n**追加内容（抜粋）:**\n" + "\n".join(f"> {l}" for l in preview)
        if len(changes["added"]) > 5:
            a_text += f"\n> ...他 {len(changes['added']) - 5} 件"

    r_text = ""
    if changes["removed"]:
        preview = changes["removed"][:3]
        r_text = "\n**削除内容（抜粋）:**\n" + "\n".join(f"> ~~{l}~~" for l in preview)

    entry = (
        f"\n## {now_str} — {target_name}\n\n"
        f"ソース: [{url}]({url}){h_text}{a_text}{r_text}\n\n---"
    )

    if not old:
        content = "# Zscaler 更新履歴\n\n自動生成 by zscaler-monitor\n" + entry
    else:
        lines = old.split("\n", 4)
        insert_after = min(3, len(lines))
        content = "\n".join(lines[:insert_after]) + entry + "\n" + "\n".join(lines[insert_after:])

    write_file(path, content)


# ============================================================
# メール送信
# ============================================================

def _esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def send_email_via_proxy(subject: str, body_text: str, body_html: str) -> bool:
    """HTTPプロキシのCONNECTトンネル経由でSMTP 587を試みる"""
    proxy_host = "127.0.0.1"
    proxy_port = int(os.environ.get("HTTPS_PROXY", "http://127.0.0.1:33689").split(":")[-1])

    try:
        raw = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        raw.settimeout(15)
        raw.connect((proxy_host, proxy_port))
        raw.send(b"CONNECT smtp.gmail.com:587 HTTP/1.1\r\nHost: smtp.gmail.com:587\r\n\r\n")
        resp = b""
        while True:
            c = raw.recv(4096)
            resp += c
            if b"\r\n\r\n" in resp:
                break
        if b"200" not in resp:
            raw.close()
            return False

        ctx = _ssl_ctx()
        s = smtplib.SMTP(timeout=15)
        s.sock = raw
        s._tls_required = False
        code, _ = s.getreply()
        s.ehlo("localhost")
        s.starttls(context=ctx)
        s.ehlo("localhost")
        s.login(GMAIL_USER, GMAIL_PASSWORD)

        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"]    = GMAIL_USER
        msg["To"]      = NOTIFY_TO
        msg.attach(MIMEText(body_text, "plain", "utf-8"))
        msg.attach(MIMEText(body_html, "html",  "utf-8"))
        s.sendmail(GMAIL_USER, NOTIFY_TO, msg.as_string())
        s.quit()
        return True
    except Exception as e:
        print(f"    [SMTP proxy] 失敗: {e}")
        return False


def send_email_direct(subject: str, body_text: str, body_html: str) -> bool:
    """SMTPへ直接接続（ポート465/587）"""
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"]    = GMAIL_USER
    msg["To"]      = NOTIFY_TO
    msg.attach(MIMEText(body_text, "plain", "utf-8"))
    msg.attach(MIMEText(body_html, "html",  "utf-8"))
    ctx = _ssl_ctx()

    # ポート465 SSL
    try:
        addrs = socket.getaddrinfo("smtp.gmail.com", 465, socket.AF_INET, socket.SOCK_STREAM)
        ip = addrs[0][4][0]
        with smtplib.SMTP_SSL(ip, 465, context=ctx, timeout=10) as s:
            s.login(GMAIL_USER, GMAIL_PASSWORD)
            s.sendmail(GMAIL_USER, NOTIFY_TO, msg.as_string())
        return True
    except Exception as e:
        print(f"    [SMTP 465] 失敗: {e}")

    # ポート587 STARTTLS
    try:
        addrs = socket.getaddrinfo("smtp.gmail.com", 587, socket.AF_INET, socket.SOCK_STREAM)
        ip = addrs[0][4][0]
        with smtplib.SMTP(ip, 587, timeout=10) as s:
            s.ehlo()
            s.starttls(context=ctx)
            s.ehlo()
            s.login(GMAIL_USER, GMAIL_PASSWORD)
            s.sendmail(GMAIL_USER, NOTIFY_TO, msg.as_string())
        return True
    except Exception as e:
        print(f"    [SMTP 587] 失敗: {e}")

    return False


def send_email(subject: str, body_text: str, body_html: str) -> None:
    print(f"  メール送信中: {subject[:60]}")
    if send_email_via_proxy(subject, body_text, body_html):
        print(f"  [OK] メール送信 → {NOTIFY_TO} (proxy)")
        return
    if send_email_direct(subject, body_text, body_html):
        print(f"  [OK] メール送信 → {NOTIFY_TO} (direct)")
        return
    print(f"  [WARN] メール送信失敗。GmailのSMTPポートがブロックされています。")


def format_email(target_name: str, url: str, changes: dict,
                 diff_text: str, gh_file_url: str, now_str: str):
    subject = f"[Zscaler更新通知] {target_name} ({now_str})"

    heading_lines = "\n".join(f"  ・{h}" for h in changes["headings"]) or "  （なし）"
    added_lines   = "\n".join(f"  + {l}" for l in changes["added"][:10]) or "  （なし）"
    removed_lines = "\n".join(f"  - {l}" for l in changes["removed"][:5]) or "  （なし）"

    text = (
        f"Zscalerに更新が検出されました。\n\n"
        f"ページ : {target_name}\nURL   : {url}\n日時  : {now_str}\n\n"
        f"▼ 更新セクション\n{heading_lines}\n\n"
        f"▼ 追加（抜粋）\n{added_lines}\n\n"
        f"▼ 削除（抜粋）\n{removed_lines}\n\n"
        f"GitHubリンク: {gh_file_url}\n"
    )

    heading_html = "".join(f"<li>{_esc(h)}</li>" for h in changes["headings"]) or "<li>（なし）</li>"
    added_html   = "".join(f'<li style="color:green">{_esc(l)}</li>' for l in changes["added"][:10]) or "<li>（なし）</li>"
    removed_html = "".join(f'<li style="color:red;text-decoration:line-through">{_esc(l)}</li>' for l in changes["removed"][:5]) or "<li>（なし）</li>"

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
<table><tr><td><b>ページ</b></td><td><a href="{url}">{_esc(target_name)}</a></td></tr>
<tr><td><b>検出日時</b></td><td>{now_str}</td></tr></table>
<h3>更新セクション</h3><ul>{heading_html}</ul>
<h3>追加内容</h3><ul>{added_html}</ul>
<h3>削除内容</h3><ul>{removed_html}</ul>
<h3>Diff</h3><pre style="background:#f8f8f8;padding:12px;font-size:12px;overflow-x:auto">{"<br>".join(diff_html_lines)}</pre>
<p><a href="{changelog_url}">CHANGELOG.md</a> | <a href="{gh_file_url}">最新MD</a></p>
</body></html>"""

    return subject, text, html


# ============================================================
# メイン処理
# ============================================================

def check_target(target: dict, state: dict) -> str:
    """'init' | 'updated' | 'no_change' | 'error'"""
    tid   = target["id"]
    name  = target["name"]
    url   = target["url"]
    print(f"\nチェック中: {name}")

    try:
        new_content = fetch_page(target)
    except Exception as e:
        print(f"  [ERROR] フェッチ失敗: {e}")
        return "error"

    new_hash = compute_hash(new_content)
    old_info = state.get(tid, {})
    old_hash = old_info.get("hash", "")
    is_first = not bool(old_hash)

    if not is_first and new_hash == old_hash:
        print("  変更なし")
        return "no_change"

    # 既存MDを読む
    gh_path = f"docs/zscaler_{tid}.md"
    old_md  = read_file(gh_path)

    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    # 新MDを作成
    new_md = (
        f"# {name}\n\n"
        f"> 最終更新: {now_str}  \n"
        f"> ソース: {url}\n\n"
        "---\n\n"
    ) + new_content

    write_file(gh_path, new_md)

    gh_file_url = (
        f"https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}"
        f"/blob/{GITHUB_BRANCH}/{gh_path}"
    )

    if is_first:
        print(f"  初版保存: {gh_file_url}")
    else:
        changes   = extract_changes(old_md, new_content)
        diff_text = build_diff(old_md, new_content)

        update_changelog(name, url, changes, now_str)

        subj, txt, html_body = format_email(name, url, changes, diff_text, gh_file_url, now_str)
        send_email(subj, txt, html_body)
        print(f"  更新検出・完了: {gh_file_url}")

    state[tid] = {
        "hash":         new_hash,
        "last_checked": datetime.now(timezone.utc).isoformat(),
        "last_updated": datetime.now(timezone.utc).isoformat(),
        "initialized":  True,
    }
    return "init" if is_first else "updated"


def main():
    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    print(f"=== Zscaler監視開始 {now_str} ===")

    # リポジトリ準備
    setup_repo()
    configure_git()

    state  = load_state()
    counts = {"init": 0, "updated": 0, "no_change": 0, "error": 0}

    for target in TARGETS:
        result = check_target(target, state)
        counts[result] = counts.get(result, 0) + 1
        time.sleep(1)

    save_state(state)

    commit_msg = (
        f"monitor: {now_str} — "
        f"init={counts['init']} update={counts['updated']} "
        f"nochange={counts['no_change']} error={counts['error']}"
    )
    commit_and_push(commit_msg)

    summary = (
        f"初版保存: {counts['init']} / 更新検出: {counts['updated']} / "
        f"変更なし: {counts['no_change']} / エラー: {counts['error']}"
    )
    print(f"\n=== 完了 — {summary} ===")
    return counts


if __name__ == "__main__":
    main()
