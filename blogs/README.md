# 自動ブログ副業（2ブログ構成）

| ブログ | 場所 | 公開URL | 更新日 |
|---|---|---|---|
| ゼロトラスト実践ノート（Zscaler） | このリポジトリの `blogs/zscaler/` | https://boiledtomato.github.io/zscaler-monitor/zscaler/ | 金・土・月・火（製品別アップデート：ZCC→ZIA→ZPA→ZDX）・水・木（基礎/設計）・不定期（障害・脆弱性） |
| 一枚の名画から（美術） | 別リポジトリ [boiledtomato/meiga-note](https://github.com/boiledtomato/meiga-note) | https://boiledtomato.github.io/meiga-note/ | 火・土（今日の一枚）・木・日（美術史） |

美術ブログは 2026-11-11 に別リポジトリへ分離しました。旧URL（/zscaler-monitor/art/…）には新URLへの転送ページを
`blogs/moved_sites.json` をもとに `scripts/build_site.py` が生成しています。

## 仕組み

```
[毎日 08:00 JST] zscaler-monitor 定期タスク（既存） → CHANGELOG.md / docs/ を更新
[毎日 ブログ用定期タスク] Claude Code セッション
    zscaler-monitor（blogs/SCHEDULED_TASK_PROMPT.md）→ meiga-note（SCHEDULED_TASK_PROMPT.md）の順に：
    1. scripts/blog_sources.py --site <blog> today  … その日の記事タイプと材料（休みの日は何もしない）
       zscaler は scripts/zscaler_sources.py が
         ・金曜：公式リリースノートを製品別に取得 → blogs/zscaler/data/weekly/<金曜>.json（scripts/release_notes_extract.js）
         ・毎日：trust.zscaler.com の RSS から、解決済みで原因公表済みの障害と CVE アドバイザリを拾う
    2. 執筆ガイドに従って記事を書く → blogs/<blog>/content/posts/*.md
    3. scripts/build_site.py --site <blog> --check   … 品質チェック
    4. main に push
[push をきっかけに] GitHub Actions → 各リポジトリでビルドして GitHub Pages に公開
```

## フォルダ構成

```
blogs/
  WRITING_RULES_COMMON.md   執筆ルール
  SCHEDULED_TASK_PROMPT.md  定期タスク用の手順
  moved_sites.json          別リポジトリに移したサイトの転送設定
  zscaler/
    config.json             サイト名・URL・デザイン・広告ID・曜日スケジュール
    WRITING_GUIDE.md        ブログ固有の執筆ガイド
    content/posts/          記事
    data/topics.json        書くテーマの在庫（上から順に使う）
    data/revenue.json       売上の記録
    data/costs.json         コストの記録
    REPORT.md               記事数・売上・コスト・収支（自動更新）
```

## 見たいときに見る場所

- **稼いだ金額** → `blogs/zscaler/REPORT.md` と meiga-note の `REPORT.md`
- **学習・復習** → 各ブログの「学習ノート」ページ（全記事の学習ポイントとクイズ）
- 売上の記録は Claude に「美術ブログの11月の AdSense は 320円」のように伝えれば追記します。

## 初回セットアップ

1. リポジトリ Settings → Pages → Source を「GitHub Actions」にする
2. このブランチを main にマージ
3. 定期タスクを登録（Claude に依頼）
4. 記事が20〜30本たまったら、ブログごとに Amazonアソシエイト / AdSense / A8.net を申請し、
   各 `config.json` の `monetization` に ID を入れる

## 独自ドメインにする場合（AdSense 申請前に推奨）

AdSense は `github.io` のサブパスでは審査に出せないため、収益化するなら独自ドメインが実質必要です
（例：`zt-note.com` と `meiga-note.com`、各 年1,500円前後）。
美術ブログは別リポジトリに分離済みなので、それぞれに独自ドメインを設定できます。

1. ドメイン業者で DNS を設定し、各リポジトリの Settings → Pages → Custom domain に入力
2. 各ブログの `config.json` の `base_url` を新しいドメインに変更

## APIモード（任意）

Claude Code の定期タスクの代わりに GitHub Actions だけで動かす場合：
Secrets に `ANTHROPIC_API_KEY`、Variables に `BLOG_MODE=api` を設定すると、毎日 10:20 JST に
`scripts/generate_post.py --site zscaler` が実行されます（美術ブログは対象外）（1本あたり概算 0.1〜0.3 USD、costs.json に自動記録）。

## 収益の現実的な見通し

最初の3〜6か月はほぼ0円が普通です。Zscaler ブログは日本語の競合が少なく広告単価も比較的高いため収益化の本命、
美術ブログは教養需要が安定していて長く読まれる記事が積み上がる「資産型」、という役割分担になります。
