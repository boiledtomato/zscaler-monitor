---
title: "SSLインスペクションはなぜ必要か：証明書の配り方と除外設計の考え方"
date: 2026-11-19
tags: [基礎, ZIA, SSLインスペクション, 証明書]
summary: "今のWeb通信の多くはHTTPSで暗号化されていて、中身を見ないとマルウェアも情報漏えいも止められません。ZIAのSSL/TLSインスペクションの仕組み、端末に配る証明書、証明書ピンニングによる失敗、除外ルールの設計と段階的な展開を、公式ドキュメントをもとに図解します。"
topic_id: zt-ssl-inspection
sources:
  - "https://help.zscaler.com/zia/understanding-ssl-inspection"
  - "https://help.zscaler.com/zia/choosing-ca-certificate-ssl-inspection"
  - "https://help.zscaler.com/zia/about-intermediate-ca-certificates"
  - "https://help.zscaler.com/zia/about-ssl-inspection-policy"
  - "https://help.zscaler.com/zia/certificate-pinning-and-ssl-inspection"
  - "https://help.zscaler.com/zia/best-practices-testing-and-rolling-out-ssl-inspection"
  - "https://help.zscaler.com/zia/deployment-scenarios-ssl-inspection"
learning:
  - "ZIA の SSL/TLS インスペクションは、端末と Zscaler、Zscaler と宛先サーバーの間にそれぞれ別の暗号化トンネルを張り、その間で通信を復号して検査する（中間者型のプロキシ）"
  - "端末が Zscaler の発行する証明書を信頼できるよう、Zscaler の中間 CA 証明書（または自社の中間 CA）を端末に配る必要がある。Zscaler は証明書を自動ではインストールしないため、Client Connector・GPO・MDM などで配る"
  - "証明書ピンニングを使うアプリは検査すると通信が失敗するため、除外が必要。公式は、小さな拠点やテスト環境から始め、URL カテゴリを段階的に広げる展開を推奨している"
quiz:
  - q: "SSL/TLS インスペクションで、端末側に配る必要があるのは何でしょう？"
    a: "Zscaler の中間 CA 証明書、または自社の CA で署名したカスタムの中間 CA 証明書。端末がこれを信頼していないと、Zscaler が提示する証明書がエラーになります。"
  - q: "証明書ピンニングを使うアプリを検査すると、どうなるでしょう？"
    a: "アプリが、Zscaler が発行した証明書を自分の知っている証明書と一致しないと判断し、接続が失敗します。対策は、そのアプリやドメインを検査対象から除外することです。"
  - q: "トランスペアレント（透過）プロキシの構成で、「Miscellaneous or Unknown」カテゴリを除外してはいけないのはなぜでしょう？"
    a: "透過モードでは SNI と IP アドレスの両方で除外が判定され、多くの IP アドレスがこのカテゴリに分類されるため、ほとんどの通信が検査されなくなってしまうからです。"
---

今の Web 通信の大半は **HTTPS**、つまり SSL/TLS で暗号化されています。暗号化は通信を守る一方で、ZIA（Zscaler Internet Access）のようなセキュリティの仕組みからも中身を隠してしまいます。
中身が見えなければ、マルウェアのダウンロードも、機密ファイルのアップロードも見つけられません。そこで必要になるのが **SSL/TLS インスペクション**です。
11月18日の記事では、通信を Zscaler に「届ける」方法を比べました。今回は、届いた暗号化通信を「見る」ための仕組みと、導入時に一番つまずきやすい**証明書**と**除外設計**を整理します。

## なぜ必要か：暗号化は攻撃者にも使われる

公式ドキュメント「Understanding SSL/TLS Inspection」は、SSL/TLS が次のように悪用されていると説明しています。

- ウイルスやスパイウェアなどのマルウェアを、暗号化で隠して届ける
- 攻撃者が、自分で SSL/TLS に対応したサイトを作る
- よく知られた信頼できる HTTPS サイトに、悪意のあるコンテンツを仕込む
- 機密の財務資料などの持ち出し（情報漏えい）を、暗号化で隠す
- 法的リスクのあるカテゴリのサイトの閲覧を隠す

SNS を含め、多くのサイトが HTTPS になった今、HTTPS 通信を検査・制御できることは、組織のセキュリティに欠かせない要素になっています。

## 仕組み：2本のトンネルの間で中身を見る

ZIA の SSL/TLS インスペクションは、**完全な SSL/TLS プロキシ**（中間者型、MITM プロキシ）として動きます。端末と宛先サーバーの間に1本のトンネルを通すのではなく、**2本の別々のトンネル**を張ります。

<figure class="fig">
<svg viewBox="0 0 720 270" role="img" aria-label="端末と Zscaler の間、Zscaler と宛先サーバーの間に、別々の暗号化トンネルを張り、Zscaler の中で復号して検査する。端末には Zscaler の中間 CA が署名したサーバー証明書が届く">
<defs><marker id="s1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#888"/></marker></defs>
<rect x="20" y="70" width="150" height="80" rx="10" class="n"/><text x="95" y="104" text-anchor="middle" class="tb">端末</text><text x="95" y="126" text-anchor="middle" class="tm">ブラウザ・アプリ</text>
<rect x="270" y="50" width="180" height="120" rx="12" class="nf"/><text x="360" y="92" text-anchor="middle" class="tw">Zscaler（ZIA）</text><text x="360" y="118" text-anchor="middle" class="tw">復号して検査</text><text x="360" y="140" text-anchor="middle" class="tw">→ 再び暗号化</text>
<rect x="550" y="70" width="150" height="80" rx="10" class="n"/><text x="625" y="104" text-anchor="middle" class="tb">宛先サーバー</text><text x="625" y="126" text-anchor="middle" class="tm">本物の証明書</text>
<line x1="172" y1="110" x2="266" y2="110" class="la" marker-end="url(#s1)" marker-start="url(#s1)"/><text x="219" y="98" text-anchor="middle" class="tm">トンネル①</text>
<line x1="452" y1="110" x2="546" y2="110" class="la" marker-end="url(#s1)" marker-start="url(#s1)"/><text x="499" y="98" text-anchor="middle" class="tm">トンネル②</text>
<rect x="20" y="190" width="430" height="64" rx="10" class="nm"/><text x="36" y="214" class="tb">端末に届く証明書</text><text x="36" y="238" class="tm">Zscaler の中間 CA（または自社の中間 CA）が署名したサーバー証明書</text>
<rect x="470" y="190" width="230" height="64" rx="10" class="nm"/><text x="486" y="214" class="tb">Zscaler が受け取る証明書</text><text x="486" y="238" class="tm">宛先サーバーの本物の証明書</text>
</svg>
<figcaption>図1：SSL/TLS インスペクションの流れ（公式ドキュメント「Understanding SSL/TLS Inspection」をもとに簡略化して作成）</figcaption>
</figure>

公式の説明を順に追うと、次のようになります。

1. ユーザーがブラウザで HTTPS のリクエストを送る
2. Zscaler がそのリクエストを受け取り、**別のトンネル**で宛先サーバーに自分からリクエストを送る
3. 宛先サーバーが、公開鍵を含む自分の証明書を Zscaler に送り、Zscaler と宛先サーバーのハンドシェイク（暗号化の取り決め）が完了する
4. Zscaler はブラウザ側ともハンドシェイクを行い、**Zscaler の中間 CA が署名したサーバー証明書**などを送る。ブラウザは、自分の証明書ストアで証明書のつながり（証明書チェーン）を確認する
5. ブラウザ側のハンドシェイクも完了し、通信が流れ始める

Zscaler が発行する証明書には、Zscaler が運用する **CRL 配布ポイント**（失効した証明書の一覧の置き場所）が含まれています。
なお、公式は**相互 TLS（Mutual TLS）を必須とするサイト**は SSL/TLS インスペクションの対象にできないとしています。

## 証明書：端末に「Zscaler を信頼させる」

手順4で端末に届く証明書は、本物のサーバー証明書ではなく、Zscaler の中間 CA が署名したものです。端末がこの中間 CA を信頼していなければ、ブラウザは証明書エラーを出します。そのため、**端末に CA 証明書を配る**作業が欠かせません。

公式ドキュメント「Choosing the CA Certificate for SSL/TLS Inspection」によると、選べる証明書は2種類です。

| 選択肢 | 内容 | 向いている場面 |
|---|---|---|
| Zscaler の中間 CA 証明書 | Zscaler が用意する既定の証明書 | 手早く始めたいとき |
| カスタムの中間 CA 証明書 | 自社が信頼する CA で署名した中間 CA | 社内の PKI（証明書の管理基盤）にそろえたいとき |

中間 CA 証明書を使うことで、大事なルート CA 証明書を守りつつ、証明書の発行を効率よく管理できます。管理画面では **Internet Access > Resources > SSL Intermediate Certificate** で管理し、鍵の保護方式として Software Protection と Cloud HSM Protection を選べます。

**大事な注意点**：Zscaler は、SSL/TLS インスペクションのために端末へ証明書を**自動でインストールしません**。配り方は次のとおりです。

- [ ] Windows・macOS で Client Connector を使っている：Client Connector のアプリプロファイル（App Profile）の設定で配れる
- [ ] Client Connector を使っていない Windows・macOS：Active Directory の GPO や MDM で配る
- [ ] Android・iOS：手動、または MDM で入れる
- [ ] ブラウザ以外のアプリが独自の証明書ストアを持つ場合（開発ツールなど）：そのアプリ側にも証明書の追加が必要か確認する

## 証明書ピンニング：検査すると壊れるアプリ

**証明書ピンニング**とは、ブラウザ以外のアプリ（デスクトップアプリやスマホアプリ）が、サーバーから届いた証明書を、アプリに埋め込まれた既知の証明書と照らし合わせる仕組みです。中間者攻撃を防ぐための仕組みですが、SSL/TLS インスペクションとは相性がよくありません。

- Zscaler が発行した証明書は、アプリが知っている証明書と一致しないため、**接続が失敗する**
- 端末がピンニングを使っていることを知らせる仕組みはないため、Zscaler 側では**ピンニングを検知できない**
- 失敗の仕方もアプリによってまちまち（「Unknown CA」のエラー、接続のリセットなど）

公式の対策は、**そのアプリを検査対象から除外する**ことです。クラウドアプリ単位、またはカスタム URL カテゴリでドメイン単位に除外します。公式ドキュメントには、Adobe 製品の更新など、ピンニングを使う代表的なアプリの一覧も載っています。

## 除外設計：何を検査しないか

SSL/TLS インスペクションのポリシーは、**通信の送信元と宛先**で、検査する・しないを決めます。設計で押さえたいのは次の点です。

<figure class="fig">
<svg viewBox="0 0 720 250" role="img" aria-label="除外の考え方。Zscaler 推奨の除外、ピンニングなど技術的に検査できないもの、方針で除外するものを分け、それ以外はすべて検査する">
<rect x="20" y="20" width="680" height="210" rx="14" class="nm"/><text x="40" y="48" class="tb">すべての HTTPS 通信（原則：検査する）</text>
<rect x="40" y="70" width="200" height="140" rx="10" class="n"/><text x="140" y="100" text-anchor="middle" class="tb">Zscaler 推奨の除外</text><text x="140" y="126" text-anchor="middle" class="tm">既定で有効の特別ルール</text><text x="140" y="148" text-anchor="middle" class="tm">数十の宛先</text><text x="140" y="170" text-anchor="middle" class="tm">通常は通信の1%未満</text>
<rect x="260" y="70" width="200" height="140" rx="10" class="n"/><text x="360" y="100" text-anchor="middle" class="tb">技術的な除外</text><text x="360" y="126" text-anchor="middle" class="tm">証明書ピンニング</text><text x="360" y="148" text-anchor="middle" class="tm">相互 TLS が必須のサイト</text><text x="360" y="170" text-anchor="middle" class="tm">アプリ・ドメイン単位で</text>
<rect x="480" y="70" width="200" height="140" rx="10" class="nx"/><text x="580" y="100" text-anchor="middle" class="tb">方針による除外</text><text x="580" y="126" text-anchor="middle" class="tm">金融・医療など</text><text x="580" y="148" text-anchor="middle" class="tm">（プライバシー配慮）</text><text x="580" y="170" text-anchor="middle" class="tm">公式は全カテゴリの</text><text x="580" y="190" text-anchor="middle" class="tm">検査を推奨</text>
</svg>
<figcaption>図2：除外の3つの種類。除外は「理由のある例外」だけに絞る（公式ドキュメントをもとに作成）</figcaption>
</figure>

- **Zscaler 推奨の除外（Zscaler-Recommended Exemptions）**：証明書ピンニングなどで検査できない既知の宛先を、自動で除外する特別ルール。既定で有効で、該当する通信は通常1%未満。Web ログの「SSL/TLS Policy Reason」で、このルールで検査されなかった通信を確認できる
- **方針による除外**：プライバシーへの配慮から、金融（Finance）や医療（Health）のカテゴリを除外する組織もある。ただし公式は、**すべての URL カテゴリを検査する**ことを推奨している
- **除外すると見えなくなるもの**：検査しない通信では、URL フィルタリングなどのポリシーが**ドメイン部分しか**判断できない。たとえば sample.com/chatBotAI という URL でも sample.com しか見えないため、パスごとの分類ができない

### 透過プロキシでの落とし穴

公式は、通信を**トランスペアレント（透過）プロキシ**で送っている場合、**「Miscellaneous or Unknown」カテゴリを除外しない**よう注意しています。透過モードでは SNI（接続先のホスト名）と IP アドレスの両方で除外が判定され、多くの IP アドレスがこのカテゴリに分類されるため、**ほとんどの通信が検査されなくなる**からです。明示的なプロキシ（PAC ファイルなど）の場合は SNI だけで判定されます。

## 展開：小さく始めて、段階的に広げる

公式ドキュメント「Best Practices for Testing and Rolling Out SSL/TLS Inspection」は、次の進め方を推奨しています。

1. 中間 CA 証明書を端末に配る
2. **小さな拠点やテスト環境**だけで SSL/TLS インスペクションを有効にする
3. テストするユーザーを決める（IT 部門のアプリ担当者・サポート担当・セキュリティ担当、IT 以外の部署の管理職や一般ユーザーなど）
4. 業務で毎日使うサイトやアプリ（取引先のものも含む）の一覧を作り、検査を有効にして動作を確かめる
5. URL カテゴリを**少しずつ**検査対象に加え、準備ができたら**すべてのカテゴリ**を検査する

うまく動かないサイトは、恒久的に除外するか、原因の調査を Zscaler サポートに依頼します。

## よくある落とし穴

- **証明書を配る前に有効にする**：全社で証明書エラーが出ます。配布と確認が先です
- **除外を「とりあえず」増やす**：除外した通信はマルウェア検査も情報漏えい対策も効きません。除外には理由と見直しの時期を残しましょう
- **ブラウザだけで動作確認する**：ピンニングを使うのは主にブラウザ以外のアプリです。業務アプリやスマホアプリもテストの一覧に入れます

## まとめ

- HTTPS は攻撃者にも使われるため、中身を見ない限りマルウェアや情報漏えいは止められない。ZIA は2本のトンネルの間で通信を復号して検査する
- 端末が Zscaler の証明書を信頼できるよう、中間 CA 証明書を Client Connector・GPO・MDM などで配る。Zscaler は自動では配らない
- 除外は「Zscaler 推奨」「技術的に検査できないもの」「方針によるもの」に絞り、小さく始めて段階的に広げる

設定の具体的な手順や最新の仕様は、必ず [Zscaler Help](https://help.zscaler.com/zia) の公式ドキュメントで確認してください。
