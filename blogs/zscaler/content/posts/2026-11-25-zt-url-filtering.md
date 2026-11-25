---
title: "URLフィルタリングとクラウドアプリ制御の設計パターン：カテゴリの階層と評価の順番"
date: 2026-11-25
tags: [基礎, ZIA, URLフィルタリング, クラウドアプリ制御]
summary: "ZIAでWebの利用を制御する中心が、URLフィルタリングとクラウドアプリ制御（Cloud App Control）です。カテゴリの3段階の階層、許可・注意・ブロック・分離の4つの動作、2つのポリシーが評価される順番、SSLインスペクションとの関係を、公式ドキュメントをもとに図解します。"
topic_id: zt-url-filtering
sources:
  - "https://help.zscaler.com/zia/about-url-filtering"
  - "https://help.zscaler.com/zia/about-url-categories"
  - "https://help.zscaler.com/zia/about-cloud-app-control"
learning:
  - "ZIA は URL を「クラス → スーパーカテゴリ → カテゴリ」の3段階に分類している。クラスは6つで固定だが、スーパーカテゴリは別のクラスへ移せ、独自のカテゴリも作れる"
  - "URL フィルタリングの動作は、許可（Allow）・注意（Caution）・ブロック（Block）・分離（Isolate）の4つ。許可でも、1日の通信量や時間の上限を付けられる"
  - "既定では、クラウドアプリ制御が URL フィルタリングより先に評価される。両方を適用したい場合は「Allow Cascading to URL Filtering」を有効にする"
quiz:
  - q: "ZIA の URL カテゴリの、最も大きなまとまり（クラス）はいくつあるでしょう？"
    a: "6つ（Bandwidth Loss、Business Use、General Surfing、Legal Liability、Productivity Loss、Privacy Risk）。クラスの追加・編集・削除はできません。"
  - q: "既定で、クラウドアプリ制御と URL フィルタリングのどちらが先に評価されるでしょう？"
    a: "クラウドアプリ制御です。両方を適用したい場合は、Advanced Settings で Allow Cascading to URL Filtering を有効にします。"
  - q: "SSL/TLS インスペクションで検査しない（バイパスする）カテゴリに、URL フィルタリングを効かせるには何が必要でしょう？"
    a: "SSL/TLS インスペクションのルールで「Evaluate Other Policies」を選ぶこと。選ばないと URL フィルタリングが適用されません。"
---

ZIA（Zscaler Internet Access）で「どのサイトを見せるか、どのアプリをどう使わせるか」を決める中心が、**URL フィルタリング**と**クラウドアプリ制御（Cloud App Control）**です。
どちらもルールを並べて作りますが、カテゴリの分け方や、2つのポリシーが評価される**順番**を知らないと、「ブロックしたはずなのに見えてしまう」といった思わぬ結果になります。
11月19日の SSL/TLS インスペクションの記事に続き、今回はこの2つの仕組みと、設計の考え方を整理します。

## URL フィルタリングとクラウドアプリ制御の違い

| | URL フィルタリング | クラウドアプリ制御 |
|---|---|---|
| 何を単位に制御するか | サイトの**カテゴリ**（ニュース、ギャンブルなど） | **クラウドアプリ**（ファイル共有、チャットなど）とその中の操作 |
| できること | カテゴリごとに許可・注意・ブロック・分離 | アプリごと、操作ごとの制御（例：チャットは許可、ファイル送信はブロック） |
| 管理画面 | Internet Access > Policy > URL Filtering | Data Security > Inline CASB > SaaS/Cloud App Policy |

公式ドキュメントの例では、クラウドアプリ制御で「インスタントメッセージのアプリで、チャットは許可し、ファイルの送信はブロックする」といったルールを作れます。URL フィルタリングが「どこへ行けるか」を決めるのに対し、クラウドアプリ制御は「**アプリの中で何ができるか**」まで踏み込めるのが違いです。

## カテゴリの3段階の階層

公式ドキュメント「About URL Categories」によると、ZIA は URL を**3段階の階層**に分類しています。

<figure class="fig">
<svg viewBox="0 0 720 270" role="img" aria-label="URL カテゴリの階層。6つのクラスの下にスーパーカテゴリ、その下にカテゴリがある">
<rect x="20" y="20" width="680" height="80" rx="12" class="nf"/><text x="40" y="46" class="tw">クラス（6つ・固定）</text><text x="40" y="68" class="tw">Bandwidth Loss ／ Business Use ／ General Surfing</text><text x="40" y="88" class="tw">Legal Liability ／ Productivity Loss ／ Privacy Risk</text>
<rect x="60" y="120" width="640" height="60" rx="12" class="na"/><text x="80" y="146" class="tb">スーパーカテゴリ</text><text x="80" y="166" class="tm">追加・削除はできないが、別のクラスへ移せる</text>
<rect x="100" y="200" width="600" height="56" rx="12" class="n"/><text x="120" y="224" class="tb">カテゴリ</text><text x="120" y="244" class="tm">URL・キーワード・IP を追加できる。独自のカテゴリも作れる</text>
</svg>
<figcaption>図1：URL カテゴリの階層（公式ドキュメント「About URL Categories」をもとに作成）</figcaption>
</figure>

- **クラス**：6つ（Bandwidth Loss、Business Use、General Surfing、Legal Liability、Productivity Loss、Privacy Risk）。追加・編集・削除はできない
- **スーパーカテゴリ**：各クラスの下のまとまり。追加・削除はできないが、**別のクラスへ移す**ことはできる。たとえばエンターテインメント業界の組織なら、Entertainment/Recreation を Business Use に移せる
- **カテゴリ**：その下の細かい分類。定義済みのカテゴリに URL やサブドメイン（mail.google.com など）、キーワード、IP の範囲を追加でき、**独自のカテゴリ**も作れる

URL を独自のカテゴリに追加するときは、**元のカテゴリにも属したままにするか**を選べます。たとえば www.google.com を独自のカテゴリに入れても、元の Web Search カテゴリに残すかどうかを指定できます。
IP アドレスは、1つの IP で複数のサイトが動いていることがあるため、原則として定義済みのカテゴリには入れられません。ただし、SaaS やクラウドの事業者が特定のアプリ専用にしている IP は分類されます。

## 4つの動作

URL フィルタリングのルールには、カテゴリのほか、ユーザー、グループ、部署、ロケーション、時間帯などの条件を指定し、次のどれかの**動作**を選びます。

| 動作 | 内容 | 使いどころの例 |
|---|---|---|
| 許可（Allow） | アクセスを許可。1日の**通信量**や**時間**の上限も付けられる | 動画サイトは許可するが、業務の通信を圧迫しないよう通信量を制限 |
| 注意（Caution） | 注意の画面を表示し、利用者が確認してから進める | 業務で必要なこともあるが、注意を促したいカテゴリ |
| ブロック（Block） | ブロックの画面を表示。一部の人に**上書き（Allow Override）**を許すこともできる | 原則禁止だが、特定の部署だけパスワードで通したい |
| 分離（Isolate） | リモートのブラウザ（ブラウザ分離）を通して表示する | 分類できない新しいサイトなど、リスクはあるが見せたいもの |

ブロックの上書き（Allow Override）を許された人は、パスワード（シングルサインオンの認証情報など）を入力すると、**そのブラウザのセッションの間だけ**ブロックされたページを見られます。分離については、11月21日の記事で分離プロファイルを紹介しました。

## 評価の順番：クラウドアプリ制御が先

設計で最も注意したいのが、2つのポリシーの**評価の順番**です。公式ドキュメント「About URL Filtering」によると、

- **既定では、クラウドアプリ制御が URL フィルタリングより優先**される。サービスは、まずクラウドアプリ制御のポリシーを適用し、その後に URL フィルタリングを適用する
- クラウドアプリ制御のポリシーが適用されたあとでも URL フィルタリングを適用したい場合は、Advanced Settings で **Allow Cascading to URL Filtering** を有効にする

<figure class="fig">
<svg viewBox="0 0 720 230" role="img" aria-label="通信は SSL/TLS インスペクションで復号されたあと、クラウドアプリ制御、URL フィルタリングの順に評価される。既定ではクラウドアプリ制御で決まった通信は URL フィルタリングに進まない。Allow Cascading を有効にすると URL フィルタリングも適用される">
<defs><marker id="u2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#888"/></marker></defs>
<rect x="20" y="70" width="150" height="80" rx="10" class="n"/><text x="95" y="104" text-anchor="middle" class="tb">SSL/TLS</text><text x="95" y="126" text-anchor="middle" class="tb">インスペクション</text>
<rect x="230" y="70" width="170" height="80" rx="12" class="nf"/><text x="315" y="104" text-anchor="middle" class="tw">クラウドアプリ制御</text><text x="315" y="128" text-anchor="middle" class="tw">（既定で先）</text>
<rect x="510" y="70" width="190" height="80" rx="12" class="na"/><text x="605" y="104" text-anchor="middle" class="tb">URL フィルタリング</text><text x="605" y="128" text-anchor="middle" class="tm">カテゴリで判定</text>
<line x1="172" y1="110" x2="226" y2="110" class="la" marker-end="url(#u2)"/>
<line x1="402" y1="110" x2="506" y2="110" class="ln" marker-end="url(#u2)" stroke-dasharray="5 4"/>
<text x="454" y="96" text-anchor="middle" class="tm">Cascading</text><text x="454" y="140" text-anchor="middle" class="tm">有効時</text>
<rect x="230" y="170" width="470" height="50" rx="10" class="nx"/><text x="465" y="191" text-anchor="middle" class="tm">既定では、クラウドアプリ制御で決まった通信は</text><text x="465" y="210" text-anchor="middle" class="tm">URL フィルタリングに進まない</text>
</svg>
<figcaption>図2：2つのポリシーの評価の順番（公式ドキュメントをもとに簡略化して作成。全ポリシーの順番は公式の「Understanding Policy Enforcement」を参照）</figcaption>
</figure>

たとえば、クラウドアプリ制御であるファイル共有アプリを**許可**していると、既定では、URL フィルタリングで同じサイトのカテゴリを**ブロック**していても、ブロックは効きません。「URL フィルタリングで止めたはずなのに見える」という問い合わせの多くは、この順番が原因になりがちです（個人の整理です）。

## SSL/TLS インスペクションとの関係

URL フィルタリングは、HTTPS の通信では、復号して中身（URL のパス）を見て初めて細かく判断できます。公式ドキュメントは、次の点に注意するよう書いています。

- テスト用のサイトなどで期待どおりに動かすには、そのカテゴリで **SSL/TLS インスペクションを有効**にする必要がある
- SSL/TLS インスペクションのルールでカテゴリをバイパス（検査しない）にし、**Evaluate Other Policies を選んでいない**場合、そのカテゴリには **URL フィルタリングが適用されない**

11月19日の記事で紹介したとおり、検査しない通信では、ポリシーはドメイン部分しか判断できません。除外の設計は、URL フィルタリングの効き方にも影響します。

## 設計パターン

公式ドキュメントの内容をもとに、ルールを組み立てるときの考え方を整理します（個人の整理です）。

1. **まず推奨ポリシーを確認する**：URL フィルタリングには、Zscaler の推奨ポリシーが用意されている
2. **アプリ単位で決めたいものは、クラウドアプリ制御で**：ファイル共有、チャット、生成AIなど、「使ってよいが、この操作は禁止」としたいものはクラウドアプリ制御に寄せる
3. **カテゴリで大きく決めるものは、URL フィルタリングで**：法的なリスクのあるカテゴリのブロックなど
4. **順番を意識する**：両方で同じサイトを扱うときは、既定ではクラウドアプリ制御が先に決まることを前提にする。必要なら Allow Cascading を使う
5. **新しいドメインに備える**：公式は、新しく登録・観測されたドメイン（Registered、Observed、Revived）をすばやく識別できるとしている。分類が定まらないサイトには、注意や分離を使う

## よくある落とし穴

- **クラウドアプリ制御で許可したアプリを、URL フィルタリングでブロックしようとする**：既定の順番では効かない
- **SSL/TLS インスペクションで除外したカテゴリに、細かい URL フィルタリングを期待する**：Evaluate Other Policies を選ばないと適用されない
- **独自カテゴリに追加した URL が、元のカテゴリのルールにも当たる**：「元のカテゴリにも残す」設定を確認する

## まとめ

- URL は「6つのクラス → スーパーカテゴリ → カテゴリ」の3段階で分類され、独自のカテゴリも作れる。動作は許可・注意・ブロック・分離の4つ
- 既定ではクラウドアプリ制御が URL フィルタリングより先に評価される。両方を効かせたいときは Allow Cascading to URL Filtering
- SSL/TLS インスペクションで除外したカテゴリは、Evaluate Other Policies を選ばないと URL フィルタリングが適用されない

設定の具体的な手順や最新の仕様は、必ず [Zscaler Help](https://help.zscaler.com/zia) の公式ドキュメントで確認してください。
