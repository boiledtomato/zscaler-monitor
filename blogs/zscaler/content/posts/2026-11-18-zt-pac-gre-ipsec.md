---
title: "ZIAへの転送方式を比較：PACファイル・GRE・IPsec・Client Connectorの使い分け"
date: 2026-11-18
tags: [基礎, ZIA, 転送方式, GRE, IPsec, PAC]
summary: "ZIAは通信が届いて初めて検査できます。ブラウザに設定するPACファイル、拠点から張るGRE・IPsecトンネル、端末に入れるClient Connector。それぞれ何を送れて、どこで効くのか。公式ドキュメントをもとに仕組みと使い分けを図解します。"
topic_id: zt-pac-gre-ipsec
sources:
  - "https://help.zscaler.com/zia/understanding-pac-file"
  - "https://help.zscaler.com/zia/about-gre-tunnels"
  - "https://help.zscaler.com/zia/understanding-ipsec-vpns"
  - "https://help.zscaler.com/zia/understanding-third-party-proxy-chaining"
  - "https://help.zscaler.com/zia/choosing-traffic-forwarding-methods"
  - "https://help.zscaler.com/zia/best-practices-traffic-forwarding"
learning:
  - "PAC ファイルはブラウザに「どの通信をどのプロキシへ送るか」を教える JavaScript のファイル。設定が簡単な反面、PAC を参照しないアプリの通信は送れない"
  - "GRE と IPsec は拠点のルーターやファイアウォールから Zscaler へトンネルを張る方式。拠点内の端末をまとめて送れるが、拠点の外にいる端末は守れない"
  - "公式は、全プロトコル・全ポートの通信を Zscaler に送ることと、トンネル・PAC・Surrogate IP・Client Connector を組み合わせることを推奨している"
quiz:
  - q: "Zscaler が IPsec で推奨している鍵交換の方式は、IKEv1 と IKEv2 のどちらでしょう？"
    a: "IKEv2。新しい標準として広く使われ、IKEv1 より速く、セキュリティが高く、新しい暗号方式にも対応しているためです。"
  - q: "GRE トンネルを1つの固定 IP アドレスから2本（プライマリとセカンダリ）張るのは何のためでしょう？"
    a: "片方のトンネルが使えなくなったときに、もう片方へ切り替える（フェイルオーバーする）ためです。"
  - q: "PAC ファイルだけで導入したとき、Zscaler に届かない通信の例は？"
    a: "PAC ファイルを参照しないアプリの通信（ブラウザ以外の業務アプリなど）。拠点のトンネルや Client Connector と組み合わせて補います。"
---

ZIA（Zscaler Internet Access）の検査やポリシーは、通信が Zscaler に**届いて初めて**効きます。そのため導入の設計で一番大事なのが、通信をどうやって Zscaler に送るか、つまり**転送方式**です。
11月4日の ZIA の記事で転送方式の一覧を紹介しましたが、今回はその中から代表的な **PAC ファイル・GRE・IPsec・Client Connector** を取り上げ、それぞれ何を送れて、どこで効くのかを比べます。

## 4つの方式の全体像

<figure class="fig">
<svg viewBox="0 0 720 300" role="img" aria-label="PAC ファイルはブラウザの通信を、GRE と IPsec は拠点のルーターからまとめて、Client Connector は端末から直接、Zscaler に送ることを示す図">
<defs><marker id="f1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#888"/></marker></defs>
<rect x="20" y="20" width="330" height="190" rx="12" class="nm"/><text x="36" y="44" class="tb">拠点（社内ネットワーク）</text>
<rect x="40" y="60" width="130" height="50" rx="8" class="n"/><text x="105" y="82" text-anchor="middle">ブラウザ</text><text x="105" y="100" text-anchor="middle" class="tm">PAC ファイル</text>
<rect x="40" y="130" width="130" height="50" rx="8" class="n"/><text x="105" y="152" text-anchor="middle">業務アプリ</text><text x="105" y="170" text-anchor="middle" class="tm">PAC を参照しない</text>
<rect x="210" y="95" width="120" height="60" rx="8" class="na"/><text x="270" y="120" text-anchor="middle" class="tb">ルーター</text><text x="270" y="140" text-anchor="middle" class="tm">GRE / IPsec</text>
<line x1="172" y1="152" x2="206" y2="135" class="ln" marker-end="url(#f1)"/>
<line x1="172" y1="78" x2="206" y2="112" class="ln" marker-end="url(#f1)"/>
<rect x="20" y="230" width="330" height="56" rx="12" class="nm"/><text x="36" y="254" class="tb">社外（自宅・出張先）</text>
<rect x="190" y="240" width="150" height="38" rx="8" class="na"/><text x="265" y="264" text-anchor="middle">Client Connector</text>
<rect x="520" y="90" width="180" height="120" rx="12" class="nf"/><text x="610" y="140" text-anchor="middle" class="tw">Zscaler</text><text x="610" y="164" text-anchor="middle" class="tw">（ZIA）</text>
<line x1="332" y1="125" x2="516" y2="140" class="la" marker-end="url(#f1)"/><text x="424" y="120" text-anchor="middle" class="tm">トンネル（拠点まるごと）</text>
<line x1="172" y1="70" x2="516" y2="104" class="ln" marker-end="url(#f1)" stroke-dasharray="5 4"/><text x="380" y="70" text-anchor="middle" class="tm">PAC：プロキシとして直接送る</text>
<line x1="342" y1="258" x2="516" y2="190" class="la" marker-end="url(#f1)"/><text x="440" y="250" text-anchor="middle" class="tm">端末から直接送る</text>
</svg>
<figcaption>図1：4つの転送方式の位置づけ（公式ドキュメントをもとに簡略化して作成）</figcaption>
</figure>

| 方式 | どこに設定するか | 送れる通信 | 社外の端末 | 主な注意点 |
|---|---|---|---|---|
| PAC ファイル | ブラウザ（端末） | PAC を参照するブラウザなどの通信 | ○（ブラウザのみ） | PAC を参照しないアプリの通信は送れない |
| GRE トンネル | 拠点のルーター | 拠点からのインターネット通信 | × | 固定 IP アドレスが必要。暗号化はしない |
| IPsec トンネル | 拠点のルーター・ファイアウォール | 拠点からのインターネット通信 | × | 対応機器の設定（IKE の方式など）が必要 |
| Client Connector | 端末のエージェント | 設定により全ポート・全プロトコル | ○ | 端末への配布・管理が必要 |

## PAC ファイル：ブラウザに道順を教える

公式ドキュメント「Understanding PAC Files」によると、**PAC（Proxy Auto-Configuration）ファイル**は、ブラウザに「宛先へ直接ではなく、プロキシサーバーへ送るように」と指示するテキストファイルです。

- 中身は JavaScript で、どのプロキシを使うか、どんな条件で使うか（曜日や時間帯、特定のドメインは送らない、など）を書ける
- 主要なブラウザはすべて対応しており、PAC ファイルの場所（アドレス）を設定するだけで使える
- Zscaler は、位置情報をもとに**最寄りの Public Service Edge** へ送る既定の PAC ファイルを用意している。独自の PAC ファイルをアップロードすることもできる

**向いている場面**：手早く導入したいとき、特定の通信だけ例外にしたいとき。
**弱点**：PAC ファイルを参照しないアプリ（ブラウザ以外の業務アプリなど）の通信は、Zscaler に届きません。

## GRE トンネル：拠点まるごと、シンプルに

公式ドキュメント「About GRE Tunnels」によると、GRE トンネルは、社内ネットワークから Zscaler へインターネット通信を送るためのトンネルで、管理画面から自分で設定（セルフプロビジョニング）できます。

- 地理的に最も近い Zscaler のデータセンターへトンネルを張れる
- **1つの固定 IP アドレスからプライマリとセカンダリの2本**を張り、片方が使えなくなったときに切り替えられる
- 複数のトンネルを CSV ファイルでまとめて設定できる

GRE は、通信をトンネルに包んで送るだけで、それ自体には暗号化の仕組みはありません（一般的な GRE の性質）。拠点の固定 IP アドレスが前提になります。

**向いている場面**：固定 IP アドレスのある拠点から、拠点内の全端末の通信をまとめて送りたいとき。

## IPsec トンネル：暗号化して送る

公式ドキュメント「Understanding IPSec VPNs」によると、IPsec は、ネットワーク層で通信を保護する一連のプロトコルで、拠点のゲートウェイと Zscaler の Public Service Edge の間に VPN を作れます。

- **機密性**（第三者に読まれない）、**完全性**（途中で改ざんされていない）、**認証**（相手が本物か）を守る
- 鍵交換の方式（IKE）には IKEv1 と IKEv2 があり、Zscaler は **IKEv2 を推奨**（新しい標準で広く使われ、速く、安全性が高く、新しい暗号方式に対応しているため）
- Cisco、Juniper、FortiGate、Palo Alto Networks、SonicWall などの製品で、IKEv2 での接続が確認されている

**向いている場面**：固定 IP アドレスがない拠点（認証情報に FQDN を使う構成）や、SD-WAN 機器と組み合わせて送りたいとき。

## Client Connector：端末から、どこにいても

**Client Connector** は、端末に入れるエージェントです。11月12日の記事で解説したとおり、Z-Tunnel 2.0 を使えば全ポート・全プロトコルの通信を送れます。
拠点のトンネルとの一番の違いは、**社外にいる端末も守れる**ことです。自宅や出張先からのアクセスも、同じポリシーで検査できます。

**向いている場面**：テレワークや出張が多い組織、端末単位でユーザーを識別したいとき。

## 使い分けの考え方

公式のベストプラクティスは、次の2点を勧めています。

1. **すべてのインターネット通信（全プロトコル・全ポート）**を Zscaler に送る
2. トンネル・PAC ファイル・Surrogate IP・Client Connector を**組み合わせて**使う

| 状況 | 組み合わせの例 |
|---|---|
| 拠点が中心で、社外利用は少ない | GRE または IPsec ＋ PAC ファイル |
| テレワークが多い | Client Connector を中心に、拠点はトンネルで補う |
| 既存のオンプレミスのプロキシを残したい | Proxy Chaining（既存のプロキシから Zscaler へつなぐ）で段階的に移行 |

## よくある落とし穴

- **PAC ファイルだけで「導入完了」にしてしまう**：ブラウザ以外の通信が検査されないまま残ります
- **トンネルを1本だけにする**：GRE はプライマリとセカンダリの2本が前提です。片方の障害でインターネットが止まらないよう、両方を設定します
- **転送方式ごとの抜け道を確認しない**：拠点・社外・VPN 利用時など、場面ごとにどの方式で送られているかを表にして、検査されない経路がないか確認しましょう

## まとめ

- PAC ファイルはブラウザ向けで手軽だが、PAC を参照しない通信は送れない
- GRE・IPsec は拠点まるごと送れるが、拠点の外の端末は守れない。IPsec は IKEv2 が推奨
- Client Connector は社外の端末も守れる。公式は全通信を送り、複数の方式を組み合わせることを推奨している

設定の具体的な手順や最新の仕様は、必ず [Zscaler Help](https://help.zscaler.com/zia) の公式ドキュメントで確認してください。
