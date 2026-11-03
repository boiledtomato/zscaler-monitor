# スケジュール実行用プロンプト（Claude Code 定期タスク）

以下を Claude Code の定期タスク（毎日1回・新規セッション）のプロンプトとして登録します。
サブスクリプション内で動くため API 料金はかかりません。1回の実行で2つのブログを順に処理します。

---

2つの個人ブログ「ゼロトラスト実践ノート」（blogs/zscaler）と「一枚の名画から」（blogs/art）の毎日の記事作成です。
リポジトリは boiledtomato/zscaler-monitor、ブランチは main。2つのブログは別サイトなので、話題を混ぜないこと。

1. `git checkout main && git pull origin main` と `pip install -q markdown PyYAML`
2. zscaler → art の順に、各ブログ <site> について：
   a. `python3 scripts/blog_sources.py --site <site> today` で今日のブリーフを取得。
      「何もしないで終了」と出たら、そのブログは今日は休み（次のブログへ）。
   b. `blogs/WRITING_RULES_COMMON.md` と `blogs/<site>/WRITING_GUIDE.md` を読み、ルールに厳密に従って記事を1本書く。
      - zscaler-digest：ブリーフに挙がった公式URLのうち重要なもの（最大5件）を WebFetch で確認し、実際の変更点を記事にする。
      - art-artwork：ブリーフの作品データと所蔵館ページを根拠に書く。画像はブリーフの「画像(小)」URL を使う。
      - topic 系：ブリーフのテーマで書く。細部は公式情報で確認できたものだけを書く。
      - 保存先は `blogs/<site>/content/posts/<今日の日付>-<topic_id>.md`。
   c. `python3 scripts/build_site.py --site <site> --check` が OK になるまで修正する。
3. `python3 scripts/build_site.py` を実行（各ブログの REPORT.md が更新される）。
4. 記事を書いた場合のみ `git add blogs/ && git commit -m "blog: <日付> <記事タイトル>"` して `git push origin main`。
   push に失敗したらネットワークエラー時のみ最大4回リトライ。
5. 報告は各ブログ1行：記事タイトルと公開URL（config.json の base_url + /posts/<ファイル名から .md を除いたもの>/）。休みの日は「休み」。
