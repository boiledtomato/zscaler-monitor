# スケジュール実行用プロンプト（Claude Code 定期タスク）

以下を Claude Code の定期タスク（毎日1回・新規セッション）のプロンプトとして登録します。
サブスクリプション内で動くため API 料金はかかりません。

---

ブログ「ゼロトラストと美術のノート」の毎日の記事作成です。リポジトリは boiledtomato/zscaler-monitor、ブランチは main。

1. `git checkout main && git pull origin main`
2. `pip install -q markdown PyYAML` を実行し、`python3 scripts/blog_sources.py today` で今日のブリーフを取得する。
   「何もしないで終了」と出たら、何もせず「本日分は作成済み」とだけ報告して終了。
3. `blog/WRITING_GUIDE.md` を読み、ルールに厳密に従って記事を1本書く。
   - zscaler-digest の場合：ブリーフに挙がった公式URLのうち重要なもの（最大5件）を WebFetch で確認し、実際の変更点を記事にする。
   - art-artwork の場合：ブリーフの作品データと所蔵館ページを根拠に書く。画像はブリーフの「画像(小)」URL を使う。
   - topic 系：ブリーフのテーマで書く。仕様の細部は help.zscaler.com 等で確認できたものだけを書く。
   - 保存先は `blog/content/posts/<今日の日付>-<topic_id>.md`。
4. `python3 scripts/build_site.py --check` が OK になるまで修正し、続けて `python3 scripts/build_site.py` を実行（blog/REPORT.md が更新される）。
5. `git add blog/ && git commit -m "blog: <日付> <記事タイトル>"` して `git push origin main`。
   push に失敗したらネットワークエラー時のみ最大4回リトライ。
6. 報告は2〜3行：記事タイトル、記事タイプ、公開URL（https://boiledtomato.github.io/zscaler-monitor/posts/<ファイル名から .md を除いたもの>/）。
