"""
SeleniumBase で認証付きプロキシを通してブラウザを操作するサンプル。

プロキシのユーザー名/パスワードを SeleniumBase に渡すと、
「プロキシ認証が必要です」のポップアップが出ずに自動でログインされる。

準備:
    pip install -r requirements-selenium.txt

設定 (.env もしくは環境変数):
    PROXY_HOST=proxy.example.com
    PROXY_PORT=8080
    PROXY_USER=your-user
    PROXY_PASS=your-password
    PROXY_BYPASS=localhost,127.0.0.1      # 任意: プロキシを通さないホスト
    HEADLESS=false                         # 任意: true で画面を出さない

実行:
    python scripts/selenium_proxy_sample.py https://example.com
"""

import os
import sys

from dotenv import load_dotenv
from seleniumbase import Driver


def build_proxy_string() -> str:
    """SeleniumBase に渡す "user:pass@host:port" 形式の文字列を作る。"""
    host = os.environ.get("PROXY_HOST")
    port = os.environ.get("PROXY_PORT")
    user = os.environ.get("PROXY_USER")
    password = os.environ.get("PROXY_PASS")

    missing = [
        name
        for name, value in [
            ("PROXY_HOST", host),
            ("PROXY_PORT", port),
            ("PROXY_USER", user),
            ("PROXY_PASS", password),
        ]
        if not value
    ]
    if missing:
        sys.exit(f"[ERROR] 環境変数が未設定です: {', '.join(missing)}")

    # SeleniumBase は文字列を ":" と "@" で区切って解釈するため、
    # ユーザー名/パスワードにこれらの記号が含まれると正しく認識できない。
    for name, value in [("PROXY_USER", user), ("PROXY_PASS", password)]:
        if ":" in value or "@" in value:
            sys.exit(
                f"[ERROR] {name} に ':' または '@' が含まれています。"
                "SeleniumBase の proxy 指定では使えません。"
            )

    return f"{user}:{password}@{host}:{port}"


def main() -> None:
    load_dotenv()

    url = sys.argv[1] if len(sys.argv) > 1 else "https://example.com"
    headless = os.environ.get("HEADLESS", "false").lower() == "true"
    bypass = os.environ.get("PROXY_BYPASS") or None

    driver = Driver(
        browser="chrome",
        proxy=build_proxy_string(),
        proxy_bypass_list=bypass,
        headless=headless,
    )
    try:
        driver.get(url)
        print(f"[OK] タイトル: {driver.title}")
        print(f"[OK] URL    : {driver.current_url}")

        # ここから先は通常の Selenium と同じように操作できる。例:
        # from selenium.webdriver.common.by import By
        # driver.find_element(By.ID, "username").send_keys("...")
        # driver.find_element(By.ID, "login").click()

        os.makedirs("logs", exist_ok=True)
        driver.save_screenshot("logs/selenium_proxy_sample.png")
        print("[OK] スクリーンショット: logs/selenium_proxy_sample.png")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
