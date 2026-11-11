# スケジュール実行用プロンプト（Claude Code 定期タスク）

以下を Claude Code の定期タスク（毎日1回）のプロンプトとして使います。
サブスクリプション内で動くため API 料金はかかりません。1回の実行で2つのブログを順に処理します。

---

2つの個人ブログ「ゼロトラスト実践ノート」（blogs/zscaler）と「一枚の名画から」（blogs/art）の毎日の記事作成です。
リポジトリは boiledtomato/zscaler-monitor、ブランチは main。2つのブログは別サイトなので、話題を混ぜないこと。

1. `git checkout main && git pull origin main` と `pip install -q markdown PyYAML`
2. zscaler → art の順に、各ブログ <site> について：
   a. `python3 scripts/blog_sources.py --site <site> today` で今日のブリーフを取得。
      「何もしないで終了」と出たら、そのブログは今日は休み（次のブログへ）。
      **zscaler は1日に複数本になることがある**（定期記事＋不定期の Trust 記事）。ブリーフ1つにつき記事1本を書く。
      金曜は製品別アップデートの材料集め（ヘッドレスブラウザで公式リリースノートを読む）に数分かかる。
      これで `blogs/zscaler/data/weekly/<金曜の日付>.json` ができるので、記事と一緒に commit する。
   b. `blogs/WRITING_RULES_COMMON.md` と `blogs/<site>/WRITING_GUIDE.md` を読み、記事タイプごとのルールに厳密に従って書く。
      - zscaler-update：ブリーフの公式リリースノート抜粋を根拠に、機能の説明・対象となる設定・運用者がやることまで書く。
        細部が足りなければブリーフの「関連ドキュメント」URL を Playwright で読んで補う（WebFetch は help.zscaler.com を読めない）。
      - zscaler-trust-incident / zscaler-trust-vuln：ブリーフの Trust 原文を根拠に、原因と影響範囲を正確に書く。
      - zscaler-topic / art-topic：ブリーフのテーマで書く。細部は公式情報で確認できたものだけを書く。
      - art-artwork：ブリーフの作品データと所蔵館ページを根拠に書く。画像はブリーフの「画像(小)」URL を使う。
      - 保存先は `blogs/<site>/content/posts/<今日の日付>-<topic_id>.md`。
   c. 本文の文字数を数え、ガイドの分量に収まっているか確かめる。
   d. `python3 scripts/build_site.py --site <site> --check` が OK になるまで修正する。
3. `python3 scripts/build_site.py` を実行（各ブログの REPORT.md が更新される）。
4. 記事を書いた場合のみ `git add blogs/ && git commit -m "blog: <日付> <記事タイトル>"` して `git push origin main`。
   リモートが進んでいたら `git pull --rebase origin main` してから push。push に失敗したらネットワークエラー時のみ最大4回リトライ。
5. push 後、公開URL が HTTP 200 を返すまで最大5分待って確認する（GitHub Actions のデプロイ待ち）。
6. 報告は記事ごとに1行：記事タイトルと公開URL（config.json の base_url + /posts/<ファイル名から .md を除いたもの>/）。
   休みのブログは「休み」。公開確認できなかった場合はその旨を書く。
