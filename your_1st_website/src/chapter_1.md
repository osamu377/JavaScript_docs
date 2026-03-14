# I. はじめてのウェブサイト

## 1. はじめに

**ウェブ<ruby>開発<rt>かいはつ</rt></ruby>の<ruby>世界<rt>せかい</rt></ruby>へようこそ**

みなさん、こんにちは！ ウェブサイトを<ruby>作<rt>つく</rt></ruby>ってみたいと<ruby>思<rt>おも</rt></ruby>ったことはありますか？ <ruby>今<rt>いま</rt></ruby>の<ruby>社会<rt>しゃかい</rt></ruby>では、<ruby>自分<rt>じぶん</rt></ruby>の<ruby>考<rt>かんが</rt></ruby>えや<ruby>情報<rt>じょうほう</rt></ruby>を<ruby>世界<rt>せかい</rt></ruby>に<ruby>伝<rt>つた</rt></ruby>えるために、ウェブサイトを<ruby>作<rt>つく</rt></ruby>る<ruby>技術<rt>ぎじゅつ</rt></ruby>はとても<ruby>大<rt>おお</rt></ruby>きな<ruby>力<rt>ちから</rt></ruby>になります。

<ruby>特<rt>とく</rt></ruby>に<ruby>留学生<rt>りゅうがくせい</rt></ruby>のみなさんにとって、ウェブサイトは「<ruby>言葉<rt>ことば</rt></ruby>の<ruby>壁<rt>かべ</rt></ruby>」をこえるための<ruby>強<rt>つよ</rt></ruby>い<ruby>味方<rt>みかた</rt></ruby>です。<ruby>完全<rt>かんぜん</rt></ruby>な<ruby>日本語<rt>にほんご</rt></ruby>を<ruby>話<rt>はな</rt></ruby>すのが<ruby>難<rt>むずか</rt></ruby>しくても、ウェブサイトなら<ruby>写真<rt>しゃしん</rt></ruby>やデザイン、<ruby>図<rt>ず</rt></ruby>を<ruby>使<rt>つか</rt></ruby>って、あなたの<ruby>魅力<rt>みりょく</rt></ruby>や<ruby>才能<rt>さいのう</rt></ruby>を<ruby>視覚<rt>しかく</rt></ruby><ruby>的<rt>てき</rt></ruby>に<ruby>伝<rt>つた</rt></ruby>えることができます。

「ウェブ<ruby>開発<rt>かいはつ</rt></ruby>はむずかしそう……」と<ruby>感<rt>かん</rt></ruby>じるかもしれません。<ruby>確<rt>たし</rt></ruby>かに、Facebook（フェイスブック）のような<ruby>複雑<rt>ふくざつ</rt></ruby>なサイトを、いきなり<ruby>一人<rt>ひとり</rt></ruby>で<ruby>作<rt>つく</rt></ruby>ることは<ruby>難<rt>むずか</rt></ruby>しいです。しかし、<ruby>安心<rt>あんしん</rt></ruby>してください。<ruby>自分<rt>じぶん</rt></ruby>だけのシンプルなウェブサイトなら、<ruby>少<rt>すこ</rt></ruby>しずつ<ruby>進<rt>すす</rt></ruby>むことで、<ruby>誰<rt>だれ</rt></ruby>でも<ruby>作<rt>つく</rt></ruby>ることができます。

このガイドでは、ウェブサイトがどのように<ruby>動<rt>うご</rt></ruby>いているのか、そしてどうすれば<ruby>自分<rt>じぶん</rt></ruby>の<ruby>作品<rt>さくひん</rt></ruby>を<ruby>世界<rt>せかい</rt></ruby>に<ruby>広<rt>ひろ</rt></ruby>めることができるのかを、やさしく<ruby>解説<rt>かいせつ</rt></ruby>します。<ruby>自分<rt>じぶん</rt></ruby>で<ruby>情報<rt>じょうほう</rt></ruby>を<ruby>広<rt>ひろ</rt></ruby>める<ruby>力<rt>ちから</rt></ruby>を<ruby>身<rt>み</rt></ruby>につけることは、<ruby>将来<rt>しょうらい</rt></ruby>の<ruby>仕事<rt>しごと</rt></ruby>や<ruby>自分<rt>じぶん</rt></ruby>を<ruby>表現<rt>ひょうげん</rt></ruby>するために、<ruby>必<rt>かなら</rt></ruby>ず<ruby>素晴<rt>すば</rt></ruby>らしいプラスになるはずです。

<ruby>準備<rt>じゅんび</rt></ruby>はいいですか？ まずは、スタートするために<ruby>必要<rt>ひつよう</rt></ruby>なものを<ruby>確認<rt>かくにん</rt></ruby>しましょう。

> [!note]
> この<ruby>資料<rt>しりょう</rt></ruby>はMDNの<a href="https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website">「Your first website」</a>をやさしい<ruby>日本語<rt>にほんご</rt></ruby>にしたものです。

***

## 2. <ruby>準備<rt>じゅんび</rt></ruby>するもの

**スタートラインに<ruby>立<rt>た</rt></ruby>つ**

<ruby>実際<rt>じっさい</rt></ruby>にコード（コンピュータへの<ruby>命令<rt>めいれい</rt></ruby>）を<ruby>書<rt>か</rt></ruby>き<ruby>始<rt>はじ</rt></ruby>める<ruby>前<rt>まえ</rt></ruby>に、<ruby>自分<rt>じぶん</rt></ruby>のコンピュータで<ruby>作業<rt>さぎょう</rt></ruby>ができる<ruby>準備<rt>じゅんび</rt></ruby>をすることが<ruby>大切<rt>たいせつ</rt></ruby>です。これを「<ruby>環境<rt>かんきょう</rt></ruby><ruby>構築<rt>こうちく</rt></ruby> / パソコンでサイトを<ruby>作<rt>つく</rt></ruby>るための<ruby>準備<rt>じゅんび</rt></ruby>」と<ruby>呼<rt>よ</rt></ruby>びます。

まず、<ruby>以下<rt>いか</rt></ruby>の3つのことがスムーズにできるか<ruby>確認<rt>かくにん</rt></ruby>してください。

1. OS（オペレーティングシステム）の<ruby>操作<rt>そうさ</rt></ruby>： WindowsやmacOSなどの<ruby>基本<rt>きほん</rt></ruby>的な<ruby>使<rt>つか</rt></ruby>い<ruby>方<rt>かた</rt></ruby>がわかる。
2. ファイルシステムの<ruby>理解<rt>りかい</rt></ruby>： ファイルを<ruby>保存<rt>ほぞん</rt></ruby>したり、フォルダを<ruby>作<rt>つく</rt></ruby>って<ruby>整理<rt>せいり</rt></ruby>したりできる。
3. ブラウザの<ruby>利用<rt>りよう</rt></ruby>： インターネットで<ruby>検索<rt>けんさく</rt></ruby>をしたり、サイトを<ruby>見<rt>み</rt></ruby>たりできる。

> [!note]
> 「2. ファイルシステムの<ruby>理解<rt>りかい</rt></ruby>」に<ruby>自信<rt>じしん</rt></ruby>のない<ruby>人<rt>ひと</rt></ruby>は、<ruby>補足<rt>ほそく</rt></ruby><ruby>資料<rt>しりょう</rt></ruby><ruby>集<rt>しゅう</rt></ruby>の「ファイルとフォルダの<ruby>基本<rt>きほん</rt></ruby>」を<ruby>見<rt>み</rt></ruby>てください

<ruby>次<rt>つぎ</rt></ruby>に、<ruby>以下<rt>いか</rt></ruby>の「<ruby>道具<rt>どうぐ</rt></ruby>」を<ruby>用意<rt>ようい</rt></ruby>しましょう。

* コードエディター： プログラムのコードを<ruby>書<rt>か</rt></ruby>くための<ruby>専用<rt>せんよう</rt></ruby>ソフトです。Visual Studio Codeを<ruby>使<rt>つか</rt></ruby>います。すでに<ruby>皆<rt>みな</rt></ruby>さんのPCにインストールされています。
* ウェブブラウザ： <ruby>主<rt>おも</rt></ruby>にGoogle Chrome を<ruby>使<rt>つか</rt></ruby>います。こちらもんストール<ruby>済<rt>ず</rt></ruby>みです。

<ruby>道具<rt>どうぐ</rt></ruby>がそろったら、<ruby>次<rt>つぎ</rt></ruby>は「どんなサイトを<ruby>作<rt>つく</rt></ruby>るか」という<ruby>計画<rt>けいかく</rt></ruby>を<ruby>立<rt>た</rt></ruby>てるステップです。

***

## 3. <ruby>計画<rt>けいかく</rt></ruby>を<ruby>立<rt>た</rt></ruby>てる

**サイトの<ruby>見<rt>み</rt></ruby>た<ruby>目<rt>め</rt></ruby>を<ruby>決<rt>き</rt></ruby>める**

いきなりコードを<ruby>書<rt>か</rt></ruby>き<ruby>始<rt>はじ</rt></ruby>めるのは、<ruby>設計図<rt>せっけいず</rt></ruby>なしで<ruby>家<rt>いえ</rt></ruby>を<ruby>建<rt>た</rt></ruby>てるようなものです。まずは「<ruby>計画<rt>けいかく</rt></ruby>」から<ruby>始<rt>はじ</rt></ruby>めましょう。<ruby>最初<rt>さいしょ</rt></ruby>にしっかり<ruby>計画<rt>けいかく</rt></ruby>を<ruby>立<rt>た</rt></ruby>てることで、<ruby>作業<rt>さぎょう</rt></ruby>の<ruby>途中<rt>とちゅう</rt></ruby>で<ruby>迷<rt>まよ</rt></ruby>わなくなり、<ruby>結果<rt>けっか</rt></ruby>として「<ruby>情報<rt>じょうほう</rt></ruby>の<ruby>整理<rt>せいり</rt></ruby>された<ruby>見<rt>み</rt></ruby>やすいサイト」を<ruby>作<rt>つく</rt></ruby>ることができます。

<ruby>計画<rt>けいかく</rt></ruby>を<ruby>立<rt>た</rt></ruby>てるときは、<ruby>以下<rt>いか</rt></ruby>のポイントを<ruby>整理<rt>せいり</rt></ruby>してみてください。

* どんな<ruby>情報<rt>じょうほう</rt></ruby>を<ruby>載<rt>の</rt></ruby>せるか： <ruby>誰<rt>だれ</rt></ruby>に、<ruby>何<rt>なに</rt></ruby>を<ruby>伝<rt>つた</rt></ruby>えたいですか？（<ruby>自己紹介<rt>じこしょうかい</rt></ruby>、<ruby>趣味<rt>しゅみ</rt></ruby>の<ruby>紹介<rt>しょうかい</rt></ruby>など）
* どんなフォントや<ruby>色<rt>いろ</rt></ruby>を<ruby>使<rt>つか</rt></ruby>うか： <ruby>明<rt>あか</rt></ruby>るいイメージですか？ それともクールで<ruby>落<rt>お</rt></ruby>ち<ruby>着<rt>つ</rt></ruby>いたイメージですか？

<ruby>見<rt>み</rt></ruby>た<ruby>目<rt>め</rt></ruby>のイメージが<ruby>固<rt>かた</rt></ruby>まったら、いよいよサイトの「<ruby>中身<rt>なかみ</rt></ruby>（<ruby>文章<rt>ぶんしょう</rt></ruby>）」と「<ruby>形<rt>かたち</rt></ruby>」を<ruby>作<rt>つく</rt></ruby>っていく<ruby>段階<rt>だんかい</rt></ruby>に<ruby>入<rt>はい</rt></ruby>ります。

> [!note]
> <ruby>見<rt>み</rt></ruby>た<ruby>目<rt>め</rt></ruby>: <ruby>外<rt>そと</rt></ruby>から<ruby>見<rt>み</rt></ruby>た<ruby>物事<rt>ものごと</rt></ruby>のありさま 
> （<ruby>例<rt>れい</rt></ruby> その<ruby>車<rt>くるま</rt></ruby>は **<ruby>見<rt>み</rt></ruby>た<ruby>目<rt>め</rt></ruby>** は<ruby>美<rt>うつく</rt></ruby>しいが<ruby>中身<rt>なかみ</rt></ruby>は<ruby>壊<rt>こわ</rt></ruby>れている）

***

## 4. サイトの「3つの<ruby>要素<rt>ようそ</rt></ruby>」

**HTML、CSS、JavaScript**

ウェブサイトは、<ruby>主<rt>おも</rt></ruby>に3つの<ruby>技術<rt>ぎじゅつ</rt></ruby>が<ruby>組<rt>く</rt></ruby>み<ruby>合<rt>あ</rt></ruby>わさってできています。これを「<ruby>家<rt>いえ</rt></ruby>づくり」に<ruby>例<rt>たと</rt></ruby>えて<ruby>見<rt>み</rt></ruby>てみましょう。

|<ruby>技術名<rt>ぎじゅつめい</rt></ruby>|<ruby>役割<rt>やくわり</rt></ruby>（<ruby>家<rt>いえ</rt></ruby>の<ruby>例<rt>たと</rt></ruby>え）|<ruby>詳<rt>くわ</rt></ruby>しい<ruby>説明<rt>せつめい</rt></ruby>|
|---|---|---|
|HTML|<ruby>構造<rt>こうぞう</rt></ruby>|<ruby>段落<rt>だんらく</rt></ruby>、リスト、<ruby>画像<rt>がぞう</rt></ruby>など、コンテンツの「<ruby>意味<rt>いみ</rt></ruby>」や「<ruby>土台<rt>どだい</rt></ruby>」を<ruby>作<rt>つく</rt></ruby>ります。|
|CSS|<ruby>見<rt>み</rt></ruby>た<ruby>目<rt>め</rt></ruby>（かざり）|<ruby>色<rt>いろ</rt></ruby>、サイズ、<ruby>配置<rt>はいち</rt></ruby>、<ruby>背景<rt>はいけい</rt></ruby>など、サイトを「<ruby>美<rt>うつく</rt></ruby>しく」<ruby>整<rt>ととの</rt></ruby>えます。|
|JavaScript|<ruby>動<rt>うご</rt></ruby>き|ボタンの<ruby>反応<rt>はんのう</rt></ruby>、アニメーション、ゲームなど「<ruby>便利<rt>べんり</rt></ruby>な<ruby>機能<rt>きのう</rt></ruby>」を<ruby>加<rt>くわ</rt></ruby>えます。|

これらの<ruby>技術<rt>ぎじゅつ</rt></ruby>は、どれか<ruby>一<rt>ひと</rt></ruby>つ<ruby>欠<rt>か</rt></ruby>けてもうまくいきません。たとえば、HTMLだけでは<ruby>文字<rt>もじ</rt></ruby>が<ruby>並<rt>なら</rt></ruby>んでいるだけで<ruby>読<rt>よ</rt></ruby>みにくく、CSSがないとデザインがバラバラになります。また、JavaScriptがないと<ruby>動<rt>うご</rt></ruby>きのない<ruby>静<rt>しず</rt></ruby>かなサイトになってしまいます。

これらを<ruby>正<rt>ただ</rt></ruby>しく<ruby>組<rt>く</rt></ruby>み<ruby>合<rt>あ</rt></ruby>わせることで、ユーザーにとって「<ruby>読<rt>よ</rt></ruby>みやすく」「<ruby>使<rt>つか</rt></ruby>いやすく」「<ruby>楽<rt>たの</rt></ruby>しい」ウェブサイトが<ruby>完成<rt>かんせい</rt></ruby>するのです。

> [!note]
> <ruby>段落<rt>だんらく</rt></ruby>：<ruby>長<rt>なが</rt></ruby>い<ruby>文章<rt>ぶんしょう</rt></ruby>を<ruby>内容<rt>ないよう</rt></ruby>などから<ruby>分<rt>わ</rt></ruby>けた、<ruby>言葉<rt>ことば</rt></ruby>の<ruby>集<rt>あつ</rt></ruby>まり

> [!note]
> リスト：<ruby>複数<rt>ふくすう</rt></ruby>の<ruby>項目<rt>こうもく</rt></ruby>や<ruby>要素<rt>ようそ</rt></ruby>を<ruby>集<rt>あつ</rt></ruby>めたもの

> [!note]
> <ruby>画像<rt>がぞう</rt></ruby>：<ruby>写真<rt>しゃしん</rt></ruby>や<ruby>絵<rt>え</rt></ruby>など

***

## 5. <ruby>世界<rt>せかい</rt></ruby>へ<ruby>公開<rt>こうかい</rt></ruby>する

**パブリッシング**

<ruby>自分<rt>じぶん</rt></ruby>のパソコンで<ruby>作<rt>つく</rt></ruby>ったファイルは、そのままでは<ruby>自分<rt>じぶん</rt></ruby>にしか<ruby>見<rt>み</rt></ruby>ることができません。これをインターネット<ruby>上<rt>じょう</rt></ruby>にアップロードして、<ruby>世界中<rt>せかいじゅう</rt></ruby>の<ruby>誰<rt>だれ</rt></ruby>でも<ruby>見<rt>み</rt></ruby>られる<ruby>状態<rt>じょうたい</rt></ruby>にすることを「<ruby>公開<rt>こうかい</rt></ruby>（パブリッシング）」と<ruby>言<rt>い</rt></ruby>います。

<ruby>公開<rt>こうかい</rt></ruby>の<ruby>手順<rt>てじゅん</rt></ruby>をシンプルにまとめると、<ruby>以下<rt>いか</rt></ruby>のようになります。

1. コードを<ruby>書<rt>か</rt></ruby>き<ruby>終<rt>お</rt></ruby>える： HTML、CSS、JavaScriptを<ruby>完成<rt>かんせい</rt></ruby>させます。
2. ファイルを<ruby>整理<rt>せいり</rt></ruby>する： <ruby>画像<rt>がぞう</rt></ruby>やコードのファイルを<ruby>正<rt>ただ</rt></ruby>しいフォルダにまとめます。
3. オンラインにアップロードする： 「サーバー」と<ruby>呼<rt>よ</rt></ruby>ばれる、インターネット<ruby>上<rt>じょう</rt></ruby>の<ruby>場所<rt>ばしょ</rt></ruby>へファイルを<ruby>送<rt>おく</rt></ruby>ります。

> [!note]
> <ruby>授業<rt>じゅぎょう</rt></ruby>では、このステップは<ruby>実施<rt>じっし</rt></ruby>しません。<ruby>興味<rt>きょうみ</rt></ruby>のある<ruby>方<rt>かた</rt></ruby>は、<a href="https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website/Publishing_your_website">ここをクリック</a>してMDNの<ruby>関連<rt>かんれん</rt></ruby>サイトを<ruby>参照<rt>さんしょう</rt></ruby>してください。

***

## 6. まとめと<ruby>次<rt>つぎ</rt></ruby>のステップ

ここまで、ウェブサイト<ruby>制作<rt>せいさく</rt></ruby>の<ruby>全体像<rt>ぜんたいぞう</rt></ruby>を<ruby>見<rt>み</rt></ruby>てきました。ウェブ<ruby>開発<rt>かいはつ</rt></ruby>の<ruby>学習<rt>がくしゅう</rt></ruby>は、<ruby>一度<rt>いちど</rt></ruby>で<ruby>完璧<rt>かんぺき</rt></ruby>にする<ruby>必要<rt>ひつよう</rt></ruby>はありません。<ruby>小<rt>ちい</rt></ruby>さな「できた！」を<ruby>積<rt>つ</rt></ruby>み<ruby>重<rt>かさ</rt></ruby>ねていくプロセスそのものが<ruby>大切<rt>たいせつ</rt></ruby>です。