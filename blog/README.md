# 自動ブログ副業：「ゼロトラストと美術のノート」

Zscaler の監視ツール（このリポジトリの本来の機能）が毎日集めている公式アップデート情報と、
メトロポリタン美術館のパブリックドメイン作品データを材料に、Claude が毎日1本ずつ記事を書き、
GitHub Pages で公開する仕組みです。

## 全体像

```
[毎日 08:00 JST] zscaler-monitor 定期タスク（既存） ─→ CHANGELOG.md / docs/ を更新
[毎日 ブログ用定期タスク] Claude Code セッション
    1. scripts/blog_sources.py today   … 曜日ごとの記事タイプを決めて材料を集める
    2. WRITING_GUIDE.md に従って記事を書く → blog/content/posts/*.md
    3. scripts/build_site.py --check   … 品質チェック（必須項目・重複・画像クレジット）
    4. main に push
[push をきっかけに] GitHub Actions (.github/workflows/blog.yml)
    → _site/ をビルドして GitHub Pages に公開、blog/REPORT.md を更新
```

| 曜日 | 記事タイプ | 内容 |
|---|---|---|
| 月 | zscaler-digest | 監視ツールが検出した1週間分の ZIA/ZPA/ZDX/trust の変更まとめ |
| 火・土 | art-artwork | Met 美術館のパブリックドメイン名品を1点解説（画像つき） |
| 水・金 | zscaler-topic | ゼロトラスト/Zscaler の基礎・設計解説（topics.json のテーマを順に） |
| 木・日 | art-topic | 美術史テーマ（古代〜現代、時代のつながりを重視） |

## 初回セットアップ（1回だけ・約15分）

1. **GitHub Pages を有効化**：リポジトリ Settings → Pages → Source を「GitHub Actions」にする。
2. このブランチを main にマージする（Actions が走り、`https://boiledtomato.github.io/zscaler-monitor/` で公開）。
3. **定期タスクを登録**：`blog/SCHEDULED_TASK_PROMPT.md` の内容で毎日実行の Claude Code 定期タスクを作る
   （Claude に「ブログの定期タスクを登録して」と頼めば作成します）。
4. **収益化の申請**（記事が20〜30本たまってから）
   - Amazonアソシエイト：審査通過後、`blog/config.json` の `amazon_associate_tag` にトラッキングIDを入れる
   - Google AdSense：独自ドメインがあると審査に通りやすい。通過後 `adsense_client`（`ca-pub-...`）を入れる
   - A8.net などの ASP：セキュリティ資格講座・美術系講座などの案件を `affiliates` に追加

### APIモード（任意）

Claude Code の定期タスクを使わず、GitHub Actions だけで完結させたい場合：
リポジトリの Secrets に `ANTHROPIC_API_KEY`、Variables に `BLOG_MODE=api` を設定すると、
毎日 10:20 JST に `scripts/generate_post.py` が記事を生成します（1本あたり概算 0.1〜0.3 USD、`blog/data/costs.json` に自動記録）。

## 見たいときに見る場所

- **稼いだ金額・コスト・記事数** → `blog/REPORT.md`（ビルドのたびに自動更新）
- **復習・学習** → サイトの「学習ノート」ページ（全記事の学習ポイントとクイズを一覧化）
- 売上の記録は `blog/data/revenue.json`。Claude に「10月の AdSense は 320円だった」と伝えれば追記します。

## 収益の現実的な見通し

正直に書いておくと、ブログ収益は**最初の3〜6か月はほぼ0円**が普通です。検索エンジンに評価されるまで時間がかかるためです。

- 0〜3か月：記事の蓄積期。収益 0〜数百円/月
- 3〜12か月：検索流入が出始める。ニッチな日本語 Zscaler 解説は競合が少なく、月数千円〜が目標ライン
- それ以降：アクセスが育てば、セキュリティ系は広告単価が比較的高く、資格書籍・講座のアフィリエイトも狙える

伸ばすコツ：Zscaler の日本語情報は少ないので「設定手順」「エラーの対処」など検索されやすいテーマを増やす。
美術記事は学習・教養需要が安定しており、長く読まれる記事になりやすい。

## 守っているルール（アカウント停止・炎上を防ぐため）

- 出典を全記事に明記。公式文書の丸写しはしない
- Zscaler 社の公式を装わない（「個人の学習ノート」と明記、ロゴ不使用）
- 画像は CC0 のパブリックドメインのみ。著作権が残る作品は画像を載せない
- アフィリエイトには「PR」表記（2023年10月施行のステマ規制対応）
- 同じテーマの重複記事を作らない（ビルド時にチェック）
