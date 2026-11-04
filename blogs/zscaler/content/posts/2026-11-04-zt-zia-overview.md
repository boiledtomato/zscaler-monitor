---
title: "ZIAの全体像：クラウドプロキシ型SWGの仕組みと構成要素"
date: 2026-11-04
tags: [基礎, ZIA, SWG, SSLインスペクション]
summary: "Zscaler Internet Access（ZIA）は、インターネットとSaaSへの通信をクラウド上で中継して検査するサービスです。Central Authority・Public Service Edge・Nanolog の3つの構成要素、通信の転送方式、SSL/TLSインスペクションの流れを、公式ドキュメントをもとに整理します。"
topic_id: zt-zia-overview
sources:
  - "https://help.zscaler.com/zia/understanding-zscaler-cloud-architecture"
  - "https://help.zscaler.com/zia/choosing-traffic-forwarding-methods"
  - "https://help.zscaler.com/zia/best-practices-traffic-forwarding"
  - "https://help.zscaler.com/zia/about-ssl-inspection"
  - "https://www.zscaler.com/products-and-solutions/zscaler-internet-access"
  - "https://www.zscaler.com/resources/security-terms-glossary/what-is-secure-web-gateway"
learning:
  - "ZIA のクラウドは、設定と脅威情報を配る Central Authority、通信を検査する Public Service Edge、ログを保管する Nanolog クラスタの3つで構成される"
  - "通信を ZIA に届ける方法は、Client Connector・GRE/IPSec トンネル・PAC ファイルなど複数あり、公式は組み合わせて使うことを推奨している"
  - "SSL/TLS インスペクションでは ZIA が利用者側とサーバー側で別々の TLS セッションを張るため、端末に Zscaler（または自社）の中間証明書を信頼させる必要がある"
quiz:
  - q: "ZIA のクラウドで、ポリシーや設定、脅威情報を集中管理する構成要素は何でしょう？"
    a: "Central Authority（CA）。公式ドキュメントでは Zscaler クラウドの「頭脳であり神経系」と表現され、1台のアクティブと2台のスタンバイで冗長化されています。"
  - q: "Public Service Edge が生成したログはどこに送られるでしょう？"
    a: "Log Router を経由して、組織ごとに適切な地域にある Nanolog クラスタに送られます。Public Service Edge 自体はデータをディスクに保存しません。"
  - q: "SSL/TLS インスペクションを有効にしても検査できないサイトの例は？"
    a: "相互 TLS（Mutual TLS）を必須とするサイト。公式ドキュメントで、これらは SSL/TLS インスペクションの対象外と明記されています。"
---

前回の記事では、ゼロトラストの考え方と、Zscaler の製品がどこにあてはまるかを整理しました。
今回はそのうち、インターネットと SaaS への通信を守る **ZIA（Zscaler Internet Access）** を取り上げます。
「ZIA の裏側で何が動いているのか」「通信はどうやって ZIA に届くのか」を、公式ドキュメントで確認できた範囲で整理します。

## ZIA は何をするサービスか

ZIA は、利用者と Web・SaaS の間に入って通信を検査する**クラウド型の SWG（Secure Web Gateway）**を中心としたサービスです。
Zscaler は現在、ZIA を SSE（Security Service Edge）製品と位置づけています。

SWG の基本的な役割は、利用者が Web サイトにアクセスするときに次のようなことを行うことです。

- URL を分類データベースと照合し、ポリシーに従って許可・ブロックする
- アップロードや共有など、アプリ内の操作を制御する
- ダウンロードするファイルにマルウェアが含まれていないかを調べる
- 暗号化された通信の中身を検査する
- 機密データの持ち出しを検知する
- 通信の記録をログとして残す

ZIA の製品ページを見ると、SWG 以外にも次の機能が並んでいます。

| 機能 | ひとことで言うと |
|---|---|
| URL フィルタリング / SWG | Web アクセスの許可・ブロック |
| Zero Trust Firewall | Web 以外も含め、全ポート・全プロトコルの通信を検査するクラウド型ファイアウォール |
| Cloud Sandbox | 未知のファイルを隔離環境で動かして振る舞いを分析する |
| Cloud DLP | 送信データに含まれる機密情報を検知する |
| CASB | SaaS の利用状況の可視化と制御 |
| SSL/TLS インスペクション | 暗号化通信を復号して上記の検査を可能にする |
| その他 | IPS、DNS セキュリティ、ブラウザ分離、帯域制御など |

どの機能を使えるかは契約内容によって変わります。自社の契約範囲は、営業担当や管理画面で確認してください。

## クラウドの3つの構成要素

公式ドキュメント「Understanding the Zscaler Cloud Architecture for Internet & SaaS」によると、ZIA のクラウドは主に次の3つでできています。

### 1. Central Authority（CA）

ドキュメントでは、Zscaler クラウドの「brain and nervous system」（頭脳であり神経系）と表現されています。

- クラウド全体を監視する
- ソフトウェアやデータベースの更新、ポリシーと設定、脅威情報を一か所で管理する
- 1台のアクティブと2台のスタンバイで構成され、データはリアルタイムに複製される。各サーバーは別々の場所に置かれる

管理画面でポリシーを変えたとき、その内容を各拠点に配るのがこの CA の仕事です。

### 2. Public Service Edge

利用者の通信を実際に受けて検査する、インラインのセキュリティゲートウェイです。

- 通信を双方向に検査し、マルウェア対策やセキュリティ・コンプライアンスのポリシーを適用する
- 世界中のどの Public Service Edge にも通信を送れる。位置情報をもとに、最寄りの Public Service Edge へ誘導する仕組みもある
- 利用者が別の場所へ移動しても、移動先の Public Service Edge が必要なポリシーを取得するため、ポリシーが利用者についていく
- データをディスクに保存しない
- 世界中でアクティブ/アクティブの負荷分散で動き、CA が稼働状況を監視する

「どこからつないでも同じポリシーがかかる」という ZIA の特徴は、この仕組みによるものです。

### 3. Nanolog クラスタ

通信ログを保管し、レポートを作る役割です。

- Public Service Edge で生成されたログは、圧縮・トークン化されたうえで TLS で Log Router に送られる。Log Router は組織ごとに、適切な地域の Nanolog クラスタへログを振り分ける
- CA と同じく、1台のアクティブと2台のスタンバイで構成される
- ログを SIEM に転送したい場合は、Nanolog Streaming Service（NSS）という仮想アプライアンスを使う

ログの保管場所が地域ごとに分かれている点は、データの所在を気にする組織にとって確認しておきたいポイントです。

## 通信をどうやって ZIA に届けるか

ZIA は「通信が届いて初めて」検査できます。そのため、導入設計でいちばん時間を使うのが**転送方式（Traffic Forwarding）**です。
公式ドキュメント「Choosing Traffic Forwarding Methods」には、次の方式が挙がっています。

| 方式 | 主な使いどころ |
|---|---|
| Zscaler Client Connector | 端末にエージェントを入れる。社外・在宅でも適用できる |
| GRE トンネル | 拠点のルーターやファイアウォールから Zscaler へトンネルを張る |
| IPSec トンネル | 同上。SD-WAN 機器との連携でよく使われる |
| PAC ファイル | ブラウザのプロキシ設定で Zscaler に向ける |
| Proxy Chaining | 既存のオンプレミスのプロキシから Zscaler へつなぐ |
| Zscaler Cloud Connector | クラウド（IaaS）上のワークロードの通信を転送する |
| Zscaler Branch Connector | 拠点の通信を転送する |

公式のベストプラクティスでは、**すべてのインターネット通信（全プロトコル・全ポート）を Zscaler に送る**こと、そしてトンネル・PAC ファイル・Surrogate IP・Client Connector を**組み合わせて**使うことが推奨されています。

設計では、次の点を判断することになります。

- **社外の端末をどう守るか**：拠点のトンネルだけでは、在宅の PC は守れません。Client Connector を入れるかどうかが分かれ目になります
- **ブラウザ以外の通信をどうするか**：PAC ファイルはブラウザなど PAC を参照するアプリにしか効きません。それ以外のアプリの通信は、トンネルや Client Connector で送る必要があります
- **ユーザーをどう識別するか**：拠点からのトンネル通信は、そのままだと「どの拠点か」しかわかりません。ユーザーごとのポリシーを使うには、認証の設計が必要です（Surrogate IP もそのための仕組みのひとつです。詳細は公式情報で要確認）

## SSL/TLS インスペクションの流れ

いまや Web 通信の大半は HTTPS です。暗号化されたままでは中身を検査できないため、ZIA の多くの機能は **SSL/TLS インスペクション**が前提になります。
公式ドキュメントによると、ZIA は「full SSL/TLS proxy」として動き、流れは次のとおりです。

1. 利用者のブラウザが HTTPS リクエストを送る
2. ZIA がそれを受け取り、**別の TLS セッション**で宛先サーバーと接続する
3. サーバーから証明書を受け取り、サーバー側の TLS ハンドシェイクを完了する
4. ブラウザ側には、Zscaler の中間 CA（または組織独自の中間 CA）で署名したサーバー証明書を提示する
5. ブラウザが証明書チェーンを検証し、利用者側の TLS ハンドシェイクを完了する

つまり、利用者とサーバーの間で **TLS を2つに分けて**、その間で中身を検査しています。
そのため、**端末側に Zscaler（または自社）のルート/中間証明書を信頼させておく**必要があります。これを忘れると、証明書エラーが大量に出ます。

## よくある落とし穴

- **証明書を配らないままインスペクションを有効にする**：ブラウザやアプリで証明書エラーが起きます。端末管理ツールで証明書を配ってから段階的に有効にします
- **独自の証明書ストアを持つアプリ**：OS の証明書ストアを使わない開発ツールやランタイムでは、別途証明書を登録しないとエラーになることがあります
- **相互 TLS（mTLS）を必須とするサイト**：公式ドキュメントで、SSL/TLS インスペクションの対象外と明記されています。こうした通信は検査の除外を設計に入れておきます
- **「一部の通信しか送っていない」状態**：PAC ファイルだけで導入すると、ブラウザ以外の通信が素通りになりがちです。公式の推奨どおり、全通信を送る構成を目指します

## まとめ

- ZIA は、インターネットと SaaS への通信をクラウド上で中継して検査する SWG 中心のサービス
- 裏側は Central Authority（設定と脅威情報）・Public Service Edge（検査）・Nanolog（ログ）の3つで動いている
- 導入の要は転送方式と SSL/TLS インスペクション。複数の転送方式を組み合わせ、証明書を配る準備をしてから始める

次回は、社内アプリへのアクセスを担う ZPA を取り上げる予定です。設定の具体的な手順や最新の仕様は、必ず [Zscaler Help](https://help.zscaler.com/zia) の公式ドキュメントで確認してください。
