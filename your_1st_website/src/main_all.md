# はじめてのウェブサイト

## I. はじめてのウェブサイト

### 1. はじめに

**ウェブ<ruby>開発<rt>かいはつ</rt></ruby>の<ruby>世界<rt>せかい</rt></ruby>へようこそ**

みなさん、こんにちは！ ウェブサイトを<ruby>作<rt>つく</rt></ruby>ってみたいと<ruby>思<rt>おも</rt></ruby>ったことはありますか？ <ruby>今<rt>いま</rt></ruby>の<ruby>社会<rt>しゃかい</rt></ruby>では、<ruby>自分<rt>じぶん</rt></ruby>の<ruby>考<rt>かんが</rt></ruby>えや<ruby>情報<rt>じょうほう</rt></ruby>を<ruby>世界<rt>せかい</rt></ruby>に<ruby>伝<rt>つた</rt></ruby>えるために、ウェブサイトを<ruby>作<rt>つく</rt></ruby>る<ruby>技術<rt>ぎじゅつ</rt></ruby>はとても<ruby>大<rt>おお</rt></ruby>きな<ruby>力<rt>ちから</rt></ruby>になります。

「ウェブ<ruby>開発<rt>かいはつ</rt></ruby>はむずかしそう……」と<ruby>感<rt>かん</rt></ruby>じるかもしれません。<ruby>確<rt>たし</rt></ruby>かに、Facebook（フェイスブック）のような<ruby>複雑<rt>ふくざつ</rt></ruby>なサイトを、いきなり<ruby>一人<rt>ひとり</rt></ruby>で<ruby>作<rt>つく</rt></ruby>ることは<ruby>難<rt>むずか</rt></ruby>しいです。しかし、<ruby>安心<rt>あんしん</rt></ruby>してください。<ruby>自分<rt>じぶん</rt></ruby>だけのシンプルなウェブサイトなら、<ruby>少<rt>すこ</rt></ruby>しずつ<ruby>進<rt>すす</rt></ruby>むことで、<ruby>誰<rt>だれ</rt></ruby>でも<ruby>作<rt>つく</rt></ruby>ることができます。

このガイドでは、ウェブサイトがどのように<ruby>動<rt>うご</rt></ruby>いているのかを、やさしく<ruby>解説<rt>かいせつ</rt></ruby>します。<ruby>自分<rt>じぶん</rt></ruby>で<ruby>情報<rt>じょうほう</rt></ruby>を<ruby>伝<rt>つた</rt></ruby>える<ruby>力<rt>ちから</rt></ruby>を<ruby>身<rt>み</rt></ruby>につけることは、<ruby>将来<rt>しょうらい</rt></ruby>の<ruby>仕事<rt>しごと</rt></ruby>や<ruby>自分<rt>じぶん</rt></ruby>を<ruby>表現<rt>ひょうげん</rt></ruby>するために、<ruby>必<rt>かなら</rt></ruby>ず<ruby>素晴<rt>すば</rt></ruby>らしいプラスになるはずです。

<ruby>準備<rt>じゅんび</rt></ruby>はいいですか？ まずは、スタートするために<ruby>必要<rt>ひつよう</rt></ruby>なものを<ruby>確認<rt>かくにん</rt></ruby>しましょう。

> [注意]
> この<ruby>資料<rt>しりょう</rt></ruby>はMDNの<a href="https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website">「Your first website」</a>をやさしい<ruby>日本語<rt>にほんご</rt></ruby>にしたものです。

***

### 2. <ruby>準備<rt>じゅんび</rt></ruby>するもの

**スタートラインに<ruby>立<rt>た</rt></ruby>つ**

<ruby>実際<rt>じっさい</rt></ruby>にコード（コンピュータへの<ruby>命令<rt>めいれい</rt></ruby>）を<ruby>書<rt>か</rt></ruby>き<ruby>始<rt>はじ</rt></ruby>める<ruby>前<rt>まえ</rt></ruby>に、<ruby>自分<rt>じぶん</rt></ruby>のコンピュータで<ruby>作業<rt>さぎょう</rt></ruby>ができる<ruby>準備<rt>じゅんび</rt></ruby>をすることが<ruby>大切<rt>たいせつ</rt></ruby>です。これを「<ruby>環境<rt>かんきょう</rt></ruby><ruby>構築<rt>こうちく</rt></ruby>」と<ruby>呼<rt>よ</rt></ruby>びます。

まず、<ruby>以下<rt>いか</rt></ruby>の3つのことがスムーズにできるか<ruby>確認<rt>かくにん</rt></ruby>してください。

1. OS（オペレーティングシステム）の<ruby>操作<rt>そうさ</rt></ruby>： WindowsやmacOSなどの<ruby>基本<rt>きほん</rt></ruby>的な<ruby>使<rt>つか</rt></ruby>い<ruby>方<rt>かた</rt></ruby>がわかる。
2. ファイルシステムの<ruby>理解<rt>りかい</rt></ruby>： ファイルを<ruby>保存<rt>ほぞん</rt></ruby>したり、フォルダを<ruby>作<rt>つく</rt></ruby>って<ruby>整理<rt>せいり</rt></ruby>したりできる。
3. ブラウザの<ruby>利用<rt>りよう</rt></ruby>： インターネットで<ruby>検索<rt>けんさく</rt></ruby>をしたり、サイトを<ruby>見<rt>み</rt></ruby>たりできる。

> [注意]
> 「2. ファイルシステムの<ruby>理解<rt>りかい</rt></ruby>」に<ruby>自信<rt>じしん</rt></ruby>のない<ruby>人<rt>ひと</rt></ruby>は、<ruby>補足<rt>ほそく</rt></ruby><ruby>資料<rt>しりょう</rt></ruby><ruby>集<rt>しゅう</rt></ruby>の「ファイルとフォルダの<ruby>基本<rt>きほん</rt></ruby>」を<ruby>見<rt>み</rt></ruby>てください

<ruby>次<rt>つぎ</rt></ruby>に、<ruby>以下<rt>いか</rt></ruby>の「<ruby>道具<rt>どうぐ</rt></ruby>」を<ruby>用意<rt>ようい</rt></ruby>しましょう。

* コードエディター： プログラムのコードを<ruby>書<rt>か</rt></ruby>くための<ruby>専用<rt>せんよう</rt></ruby>ソフトです。Visual Studio Codeを<ruby>使<rt>つか</rt></ruby>います。すでに<ruby>皆<rt>みな</rt></ruby>さんのPCにインストールされています。
* ウェブブラウザ： <ruby>主<rt>おも</rt></ruby>にGoogle Chrome を<ruby>使<rt>つか</rt></ruby>います。こちらもインストール<ruby>済<rt>ず</rt></ruby>みです。

<ruby>道具<rt>どうぐ</rt></ruby>がそろったら、<ruby>次<rt>つぎ</rt></ruby>は「どんなサイトを<ruby>作<rt>つく</rt></ruby>るか」という<ruby>計画<rt>けいかく</rt></ruby>を<ruby>立<rt>た</rt></ruby>てるステップです。

***

### 3. <ruby>計画<rt>けいかく</rt></ruby>を<ruby>立<rt>た</rt></ruby>てる

**サイトの<ruby>見<rt>み</rt></ruby>た<ruby>目<rt>め</rt></ruby>を<ruby>決<rt>き</rt></ruby>める**

いきなりコードを<ruby>書<rt>か</rt></ruby>き<ruby>始<rt>はじ</rt></ruby>めるのは、<ruby>設計図<rt>せっけいず</rt></ruby>なしで<ruby>家<rt>いえ</rt></ruby>を<ruby>建<rt>た</rt></ruby>てるようなものです。まずは「<ruby>計画<rt>けいかく</rt></ruby>」から<ruby>始<rt>はじ</rt></ruby>めましょう。<ruby>最初<rt>さいしょ</rt></ruby>にしっかり<ruby>計画<rt>けいかく</rt></ruby>を<ruby>立<rt>た</rt></ruby>てることで、<ruby>作業<rt>さぎょう</rt></ruby>の<ruby>途中<rt>とちゅう</rt></ruby>で<ruby>迷<rt>まよ</rt></ruby>わなくなり、<ruby>結果<rt>けっか</rt></ruby>として「<ruby>情報<rt>じょうほう</rt></ruby>の<ruby>整理<rt>せいり</rt></ruby>された<ruby>見<rt>み</rt></ruby>やすいサイト」を<ruby>作<rt>つく</rt></ruby>ることができます。

<ruby>計画<rt>けいかく</rt></ruby>を<ruby>立<rt>た</rt></ruby>てるときは、<ruby>以下<rt>いか</rt></ruby>のポイントを<ruby>整理<rt>せいり</rt></ruby>してみてください。

* どんな<ruby>情報<rt>じょうほう</rt></ruby>を<ruby>載<rt>の</rt></ruby>せるか： <ruby>誰<rt>だれ</rt></ruby>に、<ruby>何<rt>なに</rt></ruby>を<ruby>伝<rt>つた</rt></ruby>えたいですか？（<ruby>自己紹介<rt>じこしょうかい</rt></ruby>、<ruby>趣味<rt>しゅみ</rt></ruby>の<ruby>紹介<rt>しょうかい</rt></ruby>など）
* どんなフォントや<ruby>色<rt>いろ</rt></ruby>を<ruby>使<rt>つか</rt></ruby>うか： <ruby>明<rt>あか</rt></ruby>るいイメージですか？ それともクールで<ruby>落<rt>お</rt></ruby>ち<ruby>着<rt>つ</rt></ruby>いたイメージですか？

<ruby>見<rt>み</rt></ruby>た<ruby>目<rt>め</rt></ruby>のイメージが<ruby>固<rt>かた</rt></ruby>まったら、いよいよサイトの「<ruby>中身<rt>なかみ</rt></ruby>（<ruby>文章<rt>ぶんしょう</rt></ruby>）」と「<ruby>形<rt>かたち</rt></ruby>」を<ruby>作<rt>つく</rt></ruby>っていく<ruby>段階<rt>だんかい</rt></ruby>に<ruby>入<rt>はい</rt></ruby>ります。

> [注意]
> <ruby>見<rt>み</rt></ruby>た<ruby>目<rt>め</rt></ruby>: <ruby>外<rt>そと</rt></ruby>から<ruby>見<rt>み</rt></ruby>た<ruby>物事<rt>ものごと</rt></ruby>のありさま 
> （<ruby>例<rt>れい</rt></ruby> その<ruby>車<rt>くるま</rt></ruby>は **<ruby>見<rt>み</rt></ruby>た<ruby>目<rt>め</rt></ruby>** は<ruby>美<rt>うつく</rt></ruby>しいが<ruby>中身<rt>なかみ</rt></ruby>は<ruby>壊<rt>こわ</rt></ruby>れている）

***

### 4. サイトの「3つの<ruby>要素<rt>ようそ</rt></ruby>」

**HTML、CSS、JavaScript**

ウェブサイトは、<ruby>主<rt>おも</rt></ruby>に3つの<ruby>技術<rt>ぎじゅつ</rt></ruby>が<ruby>組<rt>く</rt></ruby>み<ruby>合<rt>あ</rt></ruby>わさってできています。これを「<ruby>家<rt>いえ</rt></ruby>づくり」に<ruby>例<rt>たと</rt></ruby>えて<ruby>見<rt>み</rt></ruby>てみましょう。

|<ruby>技術名<rt>ぎじゅつめい</rt></ruby>|<ruby>役割<rt>やくわり</rt></ruby>（<ruby>家<rt>いえ</rt></ruby>の<ruby>例<rt>たと</rt></ruby>え）|<ruby>詳<rt>くわ</rt></ruby>しい<ruby>説明<rt>せつめい</rt></ruby>|
|---|---|---|
|HTML|<ruby>構造<rt>こうぞう</rt></ruby>|<ruby>段落<rt>だんらく</rt></ruby>、リスト、<ruby>画像<rt>がぞう</rt></ruby>など、コンテンツの「<ruby>意味<rt>いみ</rt></ruby>」や「<ruby>土台<rt>どだい</rt></ruby>」を<ruby>作<rt>つく</rt></ruby>ります。|
|CSS|<ruby>見<rt>み</rt></ruby>た<ruby>目<rt>め</rt></ruby>（かざり）|<ruby>色<rt>いろ</rt></ruby>、サイズ、<ruby>配置<rt>はいち</rt></ruby>、<ruby>背景<rt>はいけい</rt></ruby>など、サイトを「<ruby>美<rt>うつく</rt></ruby>しく」<ruby>整<rt>ととの</rt></ruby>えます。|
|JavaScript|<ruby>動<rt>うご</rt></ruby>き|ボタンの<ruby>反応<rt>はんのう</rt></ruby>、アニメーション、ゲームなど「<ruby>便利<rt>べんり</rt></ruby>な<ruby>機能<rt>きのう</rt></ruby>」を<ruby>加<rt>くわ</rt></ruby>えます。|

これらの<ruby>技術<rt>ぎじゅつ</rt></ruby>は、どれか<ruby>一<rt>ひと</rt></ruby>つ<ruby>欠<rt>か</rt></ruby>けてもうまくいきません。たとえば、HTMLだけでは<ruby>文字<rt>もじ</rt></ruby>が<ruby>並<rt>なら</rt></ruby>んでいるだけで<ruby>読<rt>よ</rt></ruby>みにくく、CSSがないとデザインがバラバラになります。また、JavaScriptがないと<ruby>動<rt>うご</rt></ruby>きのない<ruby>静<rt>しず</rt></ruby>かなサイトになってしまいます。

これらを<ruby>正<rt>ただ</rt></ruby>しく<ruby>組<rt>く</rt></ruby>み<ruby>合<rt>あ</rt></ruby>わせることで、ユーザーにとって「<ruby>読<rt>よ</rt></ruby>みやすく」「<ruby>使<rt>つか</rt></ruby>いやすく」「<ruby>楽<rt>たの</rt></ruby>しい」ウェブサイトが<ruby>完成<rt>かんせい</rt></ruby>するのです。

> [注意]
> <ruby>段落<rt>だんらく</rt></ruby>：<ruby>長<rt>なが</rt></ruby>い<ruby>文章<rt>ぶんしょう</rt></ruby>を<ruby>内容<rt>ないよう</rt></ruby>などから<ruby>分<rt>わ</rt></ruby>けた、<ruby>言葉<rt>ことば</rt></ruby>の<ruby>集<rt>あつ</rt></ruby>まり

> [注意]
> リスト：<ruby>複数<rt>ふくすう</rt></ruby>の<ruby>項目<rt>こうもく</rt></ruby>や<ruby>要素<rt>ようそ</rt></ruby>を<ruby>集<rt>あつ</rt></ruby>めたもの

> [注意]
> <ruby>画像<rt>がぞう</rt></ruby>：<ruby>写真<rt>しゃしん</rt></ruby>や<ruby>絵<rt>え</rt></ruby>など

***

### 5. <ruby>世界<rt>せかい</rt></ruby>へ<ruby>公開<rt>こうかい</rt></ruby>する

> [注意]
> <ruby>授業<rt>じゅぎょう</rt></ruby>では、このステップは<ruby>実施<rt>じっし</rt></ruby>しません。<ruby>興味<rt>きょうみ</rt></ruby>のある<ruby>方<rt>かた</rt></ruby>は、<a href="https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website/Publishing_your_website">ここをクリック</a>してMDNの<ruby>関連<rt>かんれん</rt></ruby>サイトを<ruby>参照<rt>さんしょう</rt></ruby>してください。

**パブリッシング**

<ruby>自分<rt>じぶん</rt></ruby>のパソコンで<ruby>作<rt>つく</rt></ruby>ったファイルは、そのままでは<ruby>自分<rt>じぶん</rt></ruby>にしか<ruby>見<rt>み</rt></ruby>ることができません。これをインターネット<ruby>上<rt>じょう</rt></ruby>にアップロードして、<ruby>世界中<rt>せかいじゅう</rt></ruby>の<ruby>誰<rt>だれ</rt></ruby>でも<ruby>見<rt>み</rt></ruby>られる<ruby>状態<rt>じょうたい</rt></ruby>にすることを「<ruby>公開<rt>こうかい</rt></ruby>（パブリッシング）」と<ruby>言<rt>い</rt></ruby>います。

<ruby>公開<rt>こうかい</rt></ruby>の<ruby>手順<rt>てじゅん</rt></ruby>をシンプルにまとめると、<ruby>以下<rt>いか</rt></ruby>のようになります。

1. コードを<ruby>書<rt>か</rt></ruby>き<ruby>終<rt>お</rt></ruby>える： HTML、CSS、JavaScriptを<ruby>完成<rt>かんせい</rt></ruby>させます。
2. ファイルを<ruby>整理<rt>せいり</rt></ruby>する： <ruby>画像<rt>がぞう</rt></ruby>やコードのファイルを<ruby>正<rt>ただ</rt></ruby>しいフォルダにまとめます。
3. オンラインにアップロードする： 「サーバー」と<ruby>呼<rt>よ</rt></ruby>ばれる、インターネット<ruby>上<rt>じょう</rt></ruby>の<ruby>場所<rt>ばしょ</rt></ruby>へファイルを<ruby>送<rt>おく</rt></ruby>ります。

***

### 6. まとめと<ruby>次<rt>つぎ</rt></ruby>のステップ

ここまで、ウェブサイト<ruby>制作<rt>せいさく</rt></ruby>の<ruby>全体像<rt>ぜんたいぞう</rt></ruby>を<ruby>見<rt>み</rt></ruby>てきました。ウェブ<ruby>開発<rt>かいはつ</rt></ruby>の<ruby>学習<rt>がくしゅう</rt></ruby>は、<ruby>一度<rt>いちど</rt></ruby>で<ruby>完璧<rt>かんぺき</rt></ruby>にする<ruby>必要<rt>ひつよう</rt></ruby>はありません。<ruby>小<rt>ちい</rt></ruby>さな「できた！」を<ruby>積<rt>つ</rt></ruby>み<ruby>重<rt>かさ</rt></ruby>ねていくプロセスそのものが<ruby>大切<rt>たいせつ</rt></ruby>です。

<div style="page-break-before:always"></div>

## II. デザインと<ruby>計画<rt>けいかく</rt></ruby>のガイドブック

ウェブサイトを<ruby>作<rt>つく</rt></ruby>るとき、いきなりパソコンでコード（プログラムの<ruby>言葉<rt>ことば</rt></ruby>）を<ruby>書<rt>か</rt></ruby>き<ruby>始<rt>はじ</rt></ruby>めるのは、おすすめしません。まずは「<ruby>計画<rt>けいかく</rt></ruby>（プランニング）」をしましょう。

このガイドブックでは、ウェブ<ruby>開発<rt>かいはつ</rt></ruby>の<ruby>専門家<rt>せんもんか</rt></ruby>が、<ruby>留学生<rt>りゅうがくせい</rt></ruby>のみなさんにも<ruby>分<rt>わ</rt></ruby>かりやすい「やさしい<ruby>日本語<rt>にほんご</rt></ruby>」で、サイト<ruby>作<rt>づく</rt></ruby>りの<ruby>準備<rt>じゅんび</rt></ruby>について<ruby>教<rt>おし</rt></ruby>えます。

***

### 1. はじめに

**なぜ「<ruby>計画<rt>けいかく</rt></ruby>」が<ruby>大切<rt>たいせつ</rt></ruby>なのか**

<ruby>家<rt>いえ</rt></ruby>を<ruby>建<rt>た</rt></ruby>てるときに「<ruby>設計図<rt>せっけいず</rt></ruby>」が<ruby>必要<rt>ひつよう</rt></ruby>なように、ウェブサイトにも<ruby>計画<rt>けいかく</rt></ruby>が<ruby>必要<rt>ひつよう</rt></ruby>です。コードを<ruby>書<rt>か</rt></ruby>く<ruby>前<rt>まえ</rt></ruby>に<ruby>計画<rt>けいかく</rt></ruby>を<ruby>立<rt>た</rt></ruby>てるのには、<ruby>大<rt>おお</rt></ruby>きな<ruby>理由<rt>りゆう</rt></ruby>があります。

* 「<ruby>作<rt>つく</rt></ruby>り<ruby>直<rt>なお</rt></ruby>し」をふせぐ： <ruby>何<rt>なに</rt></ruby>も<ruby>決<rt>き</rt></ruby>めずに<ruby>作<rt>つく</rt></ruby>ると、あとで「やっぱり<ruby>違<rt>ちが</rt></ruby>う！」となって、<ruby>時間<rt>じかん</rt></ruby>をむだにしてしまいます。
* <ruby>最後<rt>さいご</rt></ruby>まで<ruby>完成<rt>かんせい</rt></ruby>できる： <ruby>最初<rt>さいしょ</rt></ruby>にやることを<ruby>決<rt>き</rt></ruby>めると、<ruby>迷<rt>まよ</rt></ruby>わずに<ruby>最後<rt>さいご</rt></ruby>まで<ruby>作<rt>つく</rt></ruby>ることができます。

<ruby>計画<rt>けいかく</rt></ruby>を<ruby>立<rt>た</rt></ruby>てることは、プロのエンジニアも<ruby>一番<rt>いちばん</rt></ruby><ruby>大切<rt>たいせつ</rt></ruby>にしているステップです。

***

### 2. ウェブサイトの<ruby>目的<rt>もくてき</rt></ruby>を<ruby>整理<rt>せいり</rt></ruby>する

<ruby>最初<rt>さいしょ</rt></ruby>のプロジェクトでは、<ruby>内容<rt>ないよう</rt></ruby>を「シンプル」にすることが<ruby>成功<rt>せいこう</rt></ruby>のヒミツです。<ruby>大<rt>おお</rt></ruby>きすぎる<ruby>目標<rt>もくひょう</rt></ruby>を<ruby>立<rt>た</rt></ruby>てると、<ruby>途中<rt>とちゅう</rt></ruby>で<ruby>嫌<rt>いや</rt></ruby>になって<ruby>諦<rt>あきら</rt></ruby>めてしまうからです。

まずは、<ruby>次<rt>つぎ</rt></ruby>の3つの<ruby>質問<rt>しつもん</rt></ruby>に<ruby>答<rt>こた</rt></ruby>えてみましょう。

1. このサイトは<ruby>何<rt>なに</rt></ruby>についてのサイトですか？（<ruby>例<rt>れい</rt></ruby>：<ruby>好<rt>す</rt></ruby>きな<ruby>犬<rt>いぬ</rt></ruby>について、<ruby>旅行<rt>りょこう</rt></ruby>したニューヨークについて、パックマン（Pac-Man）についてなど）
2. どんな<ruby>情報<rt>じょうほう</rt></ruby>を<ruby>紹介<rt>しょうかい</rt></ruby>しますか？（ウェブサイトの<ruby>名前<rt>なまえ</rt></ruby>を<ruby>決<rt>き</rt></ruby>めましょう。そして、1つの「<ruby>見出<rt>みだ</rt></ruby>し（タイトル）」、1つの「<ruby>画像<rt>がぞう</rt></ruby>」、2〜3<ruby>個<rt>こ</rt></ruby>の「<ruby>段落<rt>だんらく</rt></ruby>（<ruby>短<rt>みじか</rt></ruby>い<ruby>文章<rt>ぶんしょう</rt></ruby>）」を<ruby>考<rt>かんが</rt></ruby>えてください）
3. どんな<ruby>見<rt>み</rt></ruby>た<ruby>目<rt>め</rt></ruby>のサイトにしますか？（<ruby>背景<rt>はいけい</rt></ruby>は<ruby>何色<rt>なにいろ</rt></ruby>がいいですか？ <ruby>文字<rt>もじ</rt></ruby>の<ruby>形<rt>かたち</rt></ruby>は「まじめ」ですか？ それとも「かわいい」ですか？」）

<ruby>専門家<rt>せんもんか</rt></ruby>の<ruby>知恵<rt>ちえ</rt></ruby>：デザインガイド

<ruby>大<rt>おお</rt></ruby>きなプロジェクトでは、「デザインガイド（デザインシステム）」というルールブックを<ruby>作<rt>つく</rt></ruby>ります。<ruby>例<rt>たと</rt></ruby>えば、Firefoxには「Firefox Acorn Design System」という<ruby>有名<rt>ゆうめい</rt></ruby>なガイドがあります。これを<ruby>見<rt>み</rt></ruby>ると、プロがどうやって「<ruby>色<rt>いろ</rt></ruby>」や「<ruby>文字<rt>もじ</rt></ruby>」のルールを<ruby>統一<rt>とういつ</rt></ruby>して、きれいに<ruby>見<rt>み</rt></ruby>せているかが<ruby>分<rt>わ</rt></ruby>かります。

<ruby>目的<rt>もくてき</rt></ruby>が<ruby>決<rt>き</rt></ruby>まったら、<ruby>次<rt>つぎ</rt></ruby>はそれを<ruby>絵<rt>え</rt></ruby>に<ruby>描<rt>か</rt></ruby>いてみましょう。

> [注意]
> 「プロジェクト」は<ruby>一<rt>ひと</rt></ruby>つのウェブサイトやアプリケーションを<ruby>作<rt>つく</rt></ruby>るための<ruby>計画<rt>けいかく</rt></ruby>、あるいは、その<ruby>計画<rt>けいかく</rt></ruby>に<ruby>関<rt>かか</rt></ruby>わる<ruby>人々<rt>ひとびと</rt></ruby>のグループのことです。そうした<ruby>計画<rt>けいかく</rt></ruby>のためのデジタル<ruby>素材<rt>そざい</rt></ruby>やソースコードなどをまとめたものを<ruby>指<rt>さ</rt></ruby>すこともあります。

***

### 3. デザインのスケッチ

**<ruby>見<rt>み</rt></ruby>た<ruby>目<rt>め</rt></ruby>のイメージを<ruby>作<rt>つく</rt></ruby>る**

ペンと<ruby>紙<rt>かみ</rt></ruby>を<ruby>使<rt>つか</rt></ruby>って、サイトの<ruby>形<rt>かたち</rt></ruby>を<ruby>自由<rt>じゆう</rt></ruby>に<ruby>描<rt>えが</rt></ruby>いてみましょう。これを「スケッチ」と<ruby>言<rt>い</rt></ruby>います。

プロも、<ruby>最初<rt>さいしょ</rt></ruby>はパソコンを<ruby>使<rt>つか</rt></ruby>わず、<ruby>紙<rt>かみ</rt></ruby>に<ruby>書<rt>か</rt></ruby>くことから<ruby>始<rt>はじ</rt></ruby>めます。ここで<ruby>大切<rt>たいせつ</rt></ruby>なのは、**「<ruby>完璧<rt>かんぺき</rt></ruby>を<ruby>目指<rt>めざ</rt></ruby>さないこと」** です。<ruby>有名<rt>ゆうめい</rt></ruby>な<ruby>画家<rt>がか</rt></ruby>のゴッホ（Van Gogh）のように<ruby>上手<rt>じょうず</rt></ruby>に<ruby>描<rt>か</rt></ruby>く<ruby>必要<rt>ひつよう</rt></ruby>はありません。どこにタイトルがあり、どこに<ruby>画像<rt>がぞう</rt></ruby>があるか、<ruby>自分<rt>じぶん</rt></ruby>が<ruby>分<rt>わ</rt></ruby>かれば<ruby>十分<rt>じゅうぶん</rt></ruby>です。

また、ウェブ<ruby>制作<rt>せいさく</rt></ruby>の<ruby>現場<rt>げんば</rt></ruby>には、2つの<ruby>役割<rt>やくわり</rt></ruby>があります。

| デザイナーの<ruby>種類<rt>しゅるい</rt></ruby> | どんな<ruby>仕事<rt>しごと</rt></ruby>をする<ruby>人<rt>ひと</rt></ruby>？ |
|---|---|
| グラフィックデザイナー | ウェブサイトの <ruby>見<rt>み</rt></ruby>た<ruby>目<rt>め</rt></ruby>を きれいに デザインする <ruby>人<rt>ひと</rt></ruby> |
| UXデザイナー | ユーザーが ボタンを <ruby>押<rt>お</rt></ruby>しやすくしたり、<ruby>情報<rt>じょうほう</rt></ruby>を <ruby>見<rt>み</rt></ruby>つけやすくしたりする <ruby>人<rt>ひと</rt></ruby> |

<ruby>今<rt>いま</rt></ruby>は、あなたがこの<ruby>両方<rt>りょうほう</rt></ruby>の<ruby>仕事<rt>しごと</rt></ruby>をします。<ruby>自分<rt>じぶん</rt></ruby>のアイデアを<ruby>自由<rt>じゆう</rt></ruby>に<ruby>紙<rt>かみ</rt></ruby>に<ruby>書<rt>か</rt></ruby>いてみてください。

***

### 4. テーマカラー（<ruby>色<rt>いろ</rt></ruby>の<ruby>名前<rt>なまえ</rt></ruby>とコード）を<ruby>決<rt>き</rt></ruby>める

サイトの<ruby>印象<rt>いんしょう</rt></ruby>を<ruby>決<rt>き</rt></ruby>める「<ruby>色<rt>いろ</rt></ruby>」を<ruby>選<rt>えら</rt></ruby>びましょう。

1. <ruby>色<rt>いろ</rt></ruby>を<ruby>選<rt>えら</rt></ruby>ぶ： カラーピッカーなどのツールで、<ruby>背景<rt>はいけい</rt></ruby>に<ruby>使<rt>つか</rt></ruby>いたい<ruby>色<rt>いろ</rt></ruby>を<ruby>探<rt>さが</rt></ruby>します。
2. コードをメモする： <ruby>色<rt>いろ</rt></ruby>を<ruby>選<rt>えら</rt></ruby>ぶと、#660066 のような「6つの<ruby>英数字<rt>えいすうじ</rt></ruby>」が<ruby>表示<rt>ひょうじ</rt></ruby>されます。これを **16<ruby>進数<rt>しんすう</rt></ruby>コード（hex code／ヘックスコード）** と<ruby>呼<rt>よ</rt></ruby>びます。

> [注意]
> 16<ruby>進数<rt>しんすう</rt></ruby>コード（hex code）とは
> コンピュータが「この<ruby>色<rt>いろ</rt></ruby>です！」と<ruby>正<rt>ただ</rt></ruby>しく<ruby>理解<rt>りかい</rt></ruby>するための<ruby>専用<rt>せんよう</rt></ruby>の<ruby>番号<rt>ばんごう</rt></ruby>です。あとでコードを<ruby>書<rt>か</rt></ruby>くときに<ruby>使<rt>つか</rt></ruby>うので、<ruby>必<rt>かなら</rt></ruby>ずメモしておきましょう。

***

### 5. <ruby>画像<rt>がぞう</rt></ruby>の<ruby>準備<rt>じゅんび</rt></ruby>

**ルールを<ruby>守<rt>まも</rt></ruby>って<ruby>探<rt>さが</rt></ruby>す<ruby>方法<rt>ほうほう</rt></ruby>**

インターネットにある<ruby>画像<rt>がぞう</rt></ruby>には「<ruby>持<rt>も</rt></ruby>ち<ruby>主<rt>ぬし</rt></ruby>」があります。これを **<ruby>著作権<rt>ちょさくけん</rt></ruby>（コピーライト）** と<ruby>言<rt>い</rt></ruby>います。<ruby>勝手<rt>かって</rt></ruby>に<ruby>使<rt>つか</rt></ruby>うと<ruby>法律<rt>ほうりつ</rt></ruby>のトラブルになることがあるので、<ruby>注意<rt>ちゅうい</rt></ruby>してください。

「<ruby>自由<rt>じゆう</rt></ruby>に<ruby>使<rt>つか</rt></ruby>ってもいい<ruby>画像<rt>がぞう</rt></ruby>」をGoogleで<ruby>探<rt>さが</rt></ruby>す<ruby>方法<rt>ほうほう</rt></ruby>は、<ruby>次<rt>つぎ</rt></ruby>の<ruby>通<rt>とお</rt></ruby>りです。

1. Google<ruby>画像<rt>がぞう</rt></ruby><ruby>検索<rt>けんさく</rt></ruby>を<ruby>使<rt>つか</rt></ruby>う： <ruby>好<rt>す</rt></ruby>きな<ruby>言葉<rt>ことば</rt></ruby>で<ruby>検索<rt>けんさく</rt></ruby>します。
2. ツールを<ruby>使<rt>つか</rt></ruby>う： <ruby>検索結果<rt>けんさくけっか</rt></ruby>の<ruby>画面<rt>がめん</rt></ruby>にある「ツール」ボタンをクリックします。
3. ライセンスを<ruby>選<rt>えら</rt></ruby>ぶ： その<ruby>下<rt>した</rt></ruby>に<ruby>表示<rt>ひょうじ</rt></ruby>される「<ruby>使用権<rt>しようけん</rt></ruby>」をクリックし、「クリエイティブ・コモンズ ライセンス」を<ruby>選<rt>えら</rt></ruby>びます。
4. <ruby>保存<rt>ほぞん</rt></ruby>する： <ruby>好<rt>す</rt></ruby>きな<ruby>画像<rt>がぞう</rt></ruby>を<ruby>見<rt>み</rt></ruby>つけたら、<ruby>右<rt>みぎ</rt></ruby>クリック（Macは Ctrl + クリック）をして、「<ruby>名前<rt>なまえ</rt></ruby>を<ruby>付<rt>つ</rt></ruby>けて<ruby>画像<rt>がぞう</rt></ruby>を<ruby>保存<rt>ほぞん</rt></ruby>」を<ruby>選<rt>えら</rt></ruby>びます。

***

### 6. フォント（<ruby>文字<rt>もじ</rt></ruby>の<ruby>形<rt>かたち</rt></ruby>）の<ruby>選択<rt>せんたく</rt></ruby>

フォントには2つのタイプがあります。

* ウェブセーフフォント： どのパソコンにも<ruby>最初<rt>さいしょ</rt></ruby>から<ruby>入<rt>はい</rt></ruby>っている<ruby>安心<rt>あんしん</rt></ruby>なフォントです（<ruby>例<rt>れい</rt></ruby>：Arial, Times New Roman）。
* Google Fonts： デザイン<ruby>性<rt>せい</rt></ruby>が<ruby>高<rt>たか</rt></ruby>いフォントを<ruby>無料<rt>むりょう</rt></ruby>で<ruby>借<rt>か</rt></ruby>りられるサービスです。

ここでは、Google Fontsを<ruby>使<rt>つか</rt></ruby>う<ruby>手順<rt>てじゅん</rt></ruby>を<ruby>説明<rt>せつめい</rt></ruby>します。

1. Google Fontsへ<ruby>行<rt>い</rt></ruby>く： サイトのイメージに<ruby>合<rt>あ</rt></ruby>うフォントを<ruby>探<rt>さが</rt></ruby>します。
2. コードを<ruby>取得<rt>しゅとく</rt></ruby>する： <ruby>好<rt>す</rt></ruby>きなフォントを<ruby>選<rt>えら</rt></ruby>び、「Get font」ボタンを<ruby>押<rt>お</rt></ruby>してから、「Get embed code（<ruby>埋<rt>う</rt></ruby>め<ruby>込<rt>こ</rt></ruby>みコードを<ruby>取得<rt>しゅとく</rt></ruby>）」をクリックします。
3. 2つのコードを<ruby>保存<rt>ほぞん</rt></ruby>する： <ruby>画面<rt>がめん</rt></ruby>に<ruby>表示<rt>ひょうじ</rt></ruby>された **2つのコードブロック（2つのまとまったコード）** を<ruby>両方<rt>りょうほう</rt></ruby>ともコピーして、メモ<ruby>帳<rt>ちょう</rt></ruby>などに<ruby>保存<rt>ほぞん</rt></ruby>してください。フォントを<ruby>動<rt>うご</rt></ruby>かすには、この2つが<ruby>両方<rt>りょうほう</rt></ruby><ruby>必要<rt>ひつよう</rt></ruby>です。

⚠️ <ruby>注意<rt>ちゅうい</rt></ruby>：<ruby>商業利用<rt>しょうぎょうりよう</rt></ruby>について フォントにもライセンスがあります。<ruby>勉強<rt>べんきょう</rt></ruby>で<ruby>使<rt>つか</rt></ruby>うのは<ruby>大丈夫<rt>だいじょうぶ</rt></ruby>ですが、<ruby>将来<rt>しょうらい</rt></ruby>、<ruby>仕事<rt>しごと</rt></ruby>でサイトを<ruby>作<rt>つく</rt></ruby>るときは、<ruby>必<rt>かなら</rt></ruby>ず「<ruby>商売<rt>しょうばい</rt></ruby>（ビジネス）で<ruby>使<rt>つか</rt></ruby>ってもいいか」を<ruby>確認<rt>かくにん</rt></ruby>しましょう。

***

### 7. まとめと<ruby>次<rt>つぎ</rt></ruby>のステップ

お<ruby>疲<rt>つか</rt></ruby>れさまでした！これで「サイトの<ruby>設計図<rt>せっけいず</rt></ruby>」と「<ruby>素材<rt>そざい</rt></ruby>」がすべて<ruby>揃<rt>そろ</rt></ruby>いました。

* <ruby>計画<rt>けいかく</rt></ruby>： どんな<ruby>内容<rt>ないよう</rt></ruby>にするか<ruby>決<rt>き</rt></ruby>めた。
* スケッチ： レイアウトを<ruby>紙<rt>かみ</rt></ruby>に<ruby>書<rt>か</rt></ruby>いた。
* <ruby>素材<rt>そざい</rt></ruby>： <ruby>色<rt>いろ</rt></ruby>のコード、<ruby>画像<rt>がぞう</rt></ruby>、フォントの<ruby>準備<rt>じゅんび</rt></ruby>ができた。

しっかりとした「<ruby>土台<rt>どだい</rt></ruby>」ができたので、<ruby>次<rt>つぎ</rt></ruby>のステップである「HTMLやCSSを<ruby>書<rt>か</rt></ruby>く<ruby>作業<rt>さぎょう</rt></ruby>」を、<ruby>自信<rt>じしん</rt></ruby>を<ruby>持<rt>も</rt></ruby>って<ruby>進<rt>すす</rt></ruby>めることができます。

<ruby>準備<rt>じゅんび</rt></ruby>はバッチリです。さあ、<ruby>次<rt>つぎ</rt></ruby>は<ruby>実際<rt>じっさい</rt></ruby>にコンピュータで、あなただけのウェブサイトを<ruby>形<rt>かたち</rt></ruby>にしていきましょう！

<div style="page-break-before:always"></div>

## III. ウェブサイトの<ruby>形<rt>かたち</rt></ruby>を<ruby>作<rt>つく</rt></ruby>ろう

ウェブサイトを<ruby>作<rt>つく</rt></ruby>るための <ruby>最初<rt>さいしょ</rt></ruby>の<ruby>一歩<rt>いっぽ</rt></ruby>へ ようこそ！ プログラミングや ウェブ<ruby>制作<rt>せいさく</rt></ruby>を <ruby>始<rt>はじ</rt></ruby>めるとき、 <ruby>最初<rt>さいしょ</rt></ruby>に <ruby>覚<rt>おぼ</rt></ruby>えるのが「HTML」です。

HTMLは ウェブサイトの「<ruby>骨組<rt>ほねぐ</rt></ruby>み」、つまり <ruby>構造<rt>こうぞう</rt></ruby>を <ruby>作<rt>つく</rt></ruby>るための <ruby>言葉<rt>ことば</rt></ruby>です。この <ruby>基本<rt>きほん</rt></ruby>を <ruby>正<rt>ただ</rt></ruby>しく <ruby>知<rt>し</rt></ruby>ることは、ウェブサイトを <ruby>作<rt>つく</rt></ruby>る <ruby>プロ<rt>ぷろ</rt></ruby>（<ruby>仕事<rt>しごと</rt></ruby>を する <ruby>人<rt>ひと</rt></ruby>）に なるために、とても <ruby>大切<rt>たいせつ</rt></ruby>なことです。

> [注意]
> 「<ruby>骨組<rt>ほねぐ</rt></ruby>み」は、もとは「からだの<ruby>骨<rt>ほね</rt></ruby>の<ruby>組<rt>く</rt></ruby>み<ruby>立<rt>た</rt></ruby>て」のことですが、そこからの「<ruby>例<rt>たと</rt></ruby>え」で、<ruby>建造物<rt>けんぞうぶつ</rt></ruby>・<ruby>機械<rt>きかい</rt></ruby>などの<ruby>基礎<rt>きそ</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>構造<rt>こうぞう</rt></ruby>の<ruby>部分<rt>ぶぶん</rt></ruby>のことも<ruby>指<rt>さ</rt></ruby>します。

***

### 1. HTMLとは<ruby>何<rt>なに</rt></ruby>？：ウェブの<ruby>基本<rt>きほん</rt></ruby>を<ruby>理解<rt>りかい</rt></ruby>する

**HTML（HyperText Markup Language）** は、テキスト（<ruby>文字<rt>もじ</rt></ruby>）に「<ruby>印<rt>しるし</rt></ruby>」を つけて、ウェブサイトの <ruby>構造<rt>こうぞう</rt></ruby>を <ruby>作<rt>つく</rt></ruby>るための「マークアップ<ruby>言語<rt>げんご</rt></ruby>」です。

HTMLの <ruby>役割<rt>やくわり</rt></ruby>を わかりやすく <ruby>例<rt>たと</rt></ruby>えると、**「<ruby>荷物<rt>にもつ</rt></ruby>に ラベルを <ruby>貼<rt>は</rt></ruby>る <ruby>作業<rt>さぎょう</rt></ruby>」** に <ruby>似<rt>に</rt></ruby>ています。ただの テキストに「これは <ruby>見出<rt>みだ</rt></ruby>しです」「これは <ruby>段落<rt>だんらく</rt></ruby>です」という ラベルを <ruby>貼<rt>は</rt></ruby>ることで、ブラウザ（Google Chromeなど）が その<ruby>意味<rt>いみ</rt></ruby>を <ruby>理解<rt>りかい</rt></ruby>できるようになります。

* <ruby>要素<rt>ようそ</rt></ruby> / Elementとは： テキストを「タグ」と <ruby>呼<rt>よ</rt></ruby>ばれる <ruby>記号<rt>きごう</rt></ruby>で <ruby>囲<rt>かこ</rt></ruby>んだ セットのことです。
* ブラウザへの <ruby>伝言<rt>でんごん</rt></ruby>： タグを <ruby>使<rt>つか</rt></ruby>うことで、ブラウザに「ここから ここまでが <ruby>段落<rt>だんらく</rt></ruby>だ」と <ruby>伝<rt>つた</rt></ruby>えることができます。

HTMLを <ruby>使<rt>つか</rt></ruby>う <ruby>理由<rt>りゆう</rt></ruby>： もし HTMLが なければ、すべての <ruby>文字<rt>もじ</rt></ruby>が <ruby>一行<rt>いちぎょう</rt></ruby>に つながってしまい、とても <ruby>読<rt>よ</rt></ruby>みにくくなります。また、<ruby>目<rt>め</rt></ruby>が <ruby>見<rt>み</rt></ruby>えにくい <ruby>人<rt>ひと</rt></ruby>が <ruby>使<rt>つか</rt></ruby>う「<ruby>音声<rt>おんせい</rt></ruby><ruby>読<rt>よ</rt></ruby>み<ruby>上<rt>あ</rt></ruby>げソフト」も、どこが <ruby>大事<rt>だいじ</rt></ruby>な <ruby>場所<rt>ばしょ</rt></ruby>なのか わからなくなってしまいます。HTMLで <ruby>正<rt>ただ</rt></ruby>しく <ruby>構造<rt>こうぞう</rt></ruby>を <ruby>作<rt>つく</rt></ruby>ることで、<ruby>誰<rt>だれ</rt></ruby>にでも <ruby>意味<rt>いみ</rt></ruby>が <ruby>伝<rt>つた</rt></ruby>わる ページに なります。

***

### 2. HTMLファイルの<ruby>基本<rt>きほん</rt></ruby>の<ruby>形<rt>かたち</rt></ruby>

ウェブページを <ruby>正<rt>ただ</rt></ruby>しく <ruby>動<rt>うご</rt></ruby>かすためには、<ruby>決<rt>き</rt></ruby>まった「<ruby>型<rt>かた</rt></ruby>」が <ruby>必要<rt>ひつよう</rt></ruby>です。

**<ruby>主要<rt>しゅよう</rt></ruby>な <ruby>構成要素<rt>こうせいようそ</rt></ruby>**

MDNの ルールに <ruby>基<rt>もと</rt></ruby>づいた、<ruby>基本<rt>きほん</rt></ruby><ruby>的<rt>てき</rt></ruby>な パーツは <ruby>以下<rt>いか</rt></ruby>の <ruby>通<rt>とお</rt></ruby>りです。

* `<!doctype html>`：ページを <ruby>正<rt>ただ</rt></ruby>しく <ruby>表示<rt>ひょうじ</rt></ruby>させるために、ファイルの  いちばん <ruby>上<rt>うえ</rt></ruby>に <ruby>書<rt>か</rt></ruby>かなければならない ルールです。
* `<html>`：ページの すべての <ruby>内容<rt>ないよう</rt></ruby>を <ruby>包<rt>つつ</rt></ruby>む「 いちばん <ruby>外側<rt>そとがわ</rt></ruby>の <ruby>箱<rt>はこ</rt></ruby>」です。
* `<head>`：<ruby>画面<rt>がめん</rt></ruby>には <ruby>見<rt>み</rt></ruby>えないけれど、ブラウザや <ruby>検索<rt>けんさく</rt></ruby>エンジンのための <ruby>大切<rt>たいせつ</rt></ruby>な <ruby>情報<rt>じょうほう</rt></ruby>（<ruby>情報<rt>じょうほう</rt></ruby>/メタデータ）を <ruby>入<rt>い</rt></ruby>れる <ruby>場所<rt>ばしょ</rt></ruby>です。
* `<title>`：ブラウザの「タブ」に <ruby>出<rt>で</rt></ruby>る <ruby>名前<rt>なまえ</rt></ruby>や、ブックマーク（<ruby>お気<rt>き</rt></ruby>に<ruby>入<rt>い</rt></ruby>り）したときの <ruby>名前<rt>なまえ</rt></ruby>になります。
* `<body>`：<ruby>実際<rt>じっさい</rt></ruby>に ユーザーが <ruby>見<rt>み</rt></ruby>る コンテンツ（<ruby>文章<rt>ぶんしょう</rt></ruby>や <ruby>画像<rt>がぞう</rt></ruby>など）を すべて <ruby>入<rt>い</rt></ruby>れる <ruby>場所<rt>ばしょ</rt></ruby>です。

**メタデータ（<ruby>大切<rt>たいせつ</rt></ruby>な <ruby>設定<rt>せってい</rt></ruby>）の <ruby>価値<rt>かち</rt></ruby>**

`<head>`の <ruby>中<rt>なか</rt></ruby>には、<ruby>以下<rt>いか</rt></ruby>の ような <ruby>設定<rt>せってい</rt></ruby>を <ruby>書<rt>か</rt></ruby>きます。

* <ruby>文字<rt>もじ</rt></ruby>コード（UTF-8）： これを <ruby>書<rt>か</rt></ruby>かないと、<ruby>日本語<rt>にほんご</rt></ruby>などが <ruby>変<rt>へん</rt></ruby>な <ruby>記号<rt>きごう</rt></ruby>に なる「<ruby>文字化<rt>もじば</rt></ruby>け」が <ruby>起<rt>お</rt></ruby>きることが あります。
* ビューポート（viewport）： スマートフォンの <ruby>画面<rt>がめん</rt></ruby>サイズに <ruby>合<rt>あ</rt></ruby>わせて、きれいに <ruby>表示<rt>ひょうじ</rt></ruby>するために <ruby>必要<rt>ひつよう</rt></ruby>です。

**タグの <ruby>構造<rt>こうぞう</rt></ruby>：<ruby>入<rt>い</rt></ruby>れ<ruby>子<rt>こ</rt></ruby>**

HTMLは「タグの <ruby>中<rt>なか</rt></ruby>に <ruby>別<rt>べつ</rt></ruby>の タグが <ruby>入<rt>はい</rt></ruby>る」という「<ruby>入<rt>い</rt></ruby>れ<ruby>子<rt>こ</rt></ruby>」の <ruby>形<rt>かたち</rt></ruby>に なります。

```html
<html> <!--一番外側の箱-->
  <head> <!--ブラウザのための情報の箱-->
    <title> ページの名前 </title>
  </head>
  <body> <!--私たちが見る中身の箱-->
    <h1> タイトル </h1>
    <p> 文章の 段落（だんらく） </p>
  </body>
</html>
```

> [注意]
> 「<ruby>入<rt>い</rt></ruby>れ<ruby>子<rt>こ</rt></ruby>」: <ruby>大<rt>おお</rt></ruby>きな<ruby>箱<rt>はこ</rt></ruby>の<ruby>中<rt>なか</rt></ruby>に<ruby>小<rt>ちい</rt></ruby>さな<ruby>箱<rt>はこ</rt></ruby>が<ruby>入<rt>はい</rt></ruby>っている、というように、あるものの<ruby>中<rt>なか</rt></ruby>に、よく<ruby>似<rt>に</rt></ruby>たあるものが<ruby>入<rt>はい</rt></ruby>っている<ruby>様子<rt>ようす</rt></ruby>を<ruby>指<rt>さ</rt></ruby>す<ruby>日本語<rt>にほんご</rt></ruby>です。

***

### 3. テキストに<ruby>意味<rt>いみ</rt></ruby>をつける：<ruby>見出<rt>みだ</rt></ruby>し、<ruby>段落<rt>だんらく</rt></ruby>、リスト

<ruby>文章<rt>ぶんしょう</rt></ruby>を <ruby>分<rt>わ</rt></ruby>かりやすくするために、<ruby>適切<rt>てきせつ</rt></ruby>な タグを <ruby>使<rt>つか</rt></ruby>います。

* <ruby>見出<rt>みだ</rt></ruby>し（`<h1>`〜`<h6>`）： <ruby>本<rt>ほん</rt></ruby>の「タイトル」や「<ruby>章<rt>しょう</rt></ruby>」の ように、<ruby>情報<rt>じょうほう</rt></ruby>の <ruby>優先順位<rt>ゆうせんじゅんい</rt></ruby>を <ruby>示<rt>しめ</rt></ruby>します。`<h1>`が  もっとも <ruby>重要<rt>じゅうよう</rt></ruby>な タイトルで、<ruby>数字<rt>すうじ</rt></ruby>が <ruby>大<rt>おお</rt></ruby>きくなるほど <ruby>小<rt>ちい</rt></ruby>さな <ruby>見出<rt>みだ</rt></ruby>しに なります。
* <ruby>段落<rt>だんらく</rt></ruby>（`<p>`）： ふつうの <ruby>文章<rt>ぶんしょう</rt></ruby>を まとめるための タグです。

<div style="page-break-before:always"></div>

* リスト（<ruby>箇条書<rt>かじょうが</rt></ruby>き）：
  * `<ul>`（<ruby>順序<rt>じゅんじょ</rt></ruby>なし リスト）： <ruby>買<rt>か</rt></ruby>い<ruby>物<rt>もの</rt></ruby>リストの ように、<ruby>順番<rt>じゅんばん</rt></ruby>が <ruby>関係<rt>かんけい</rt></ruby>ないときに <ruby>使<rt>つか</rt></ruby>います。
  * `<ol>`（<ruby>順序<rt>じゅんじょ</rt></ruby>あり リスト）： <ruby>料理<rt>りょうり</rt></ruby>の <ruby>手順<rt>てじゅん</rt></ruby>の ように、<ruby>順番<rt>じゅんばん</rt></ruby>が <ruby>大切<rt>たいせつ</rt></ruby>なときに <ruby>使<rt>つか</rt></ruby>います。
  * ※どちらも、<ruby>中身<rt>なかみ</rt></ruby>の <ruby>項目<rt>こうもく</rt></ruby>は `<li>` タグで <ruby>囲<rt>かこ</rt></ruby>みます。

HTMLコメント（`<!-- -->`）の メリット： コードの <ruby>中<rt>なか</rt></ruby>に `<!-- メモ -->` と <ruby>書<rt>か</rt></ruby>くと、ブラウザには <ruby>表示<rt>ひょうじ</rt></ruby>されません。これは「<ruby>自分<rt>じぶん</rt></ruby>や <ruby>仲間<rt>なかま</rt></ruby>」のための メモです。あとで <ruby>見直<rt>みなお</rt></ruby>したときに、<ruby>何<rt>なに</rt></ruby>をしたのか すぐに <ruby>分<rt>わ</rt></ruby>かるように なります。

***

### 4. <ruby>画像<rt>がぞう</rt></ruby>を <ruby>表示<rt>ひょうじ</rt></ruby>する：`<img>`<ruby>要素<rt>ようそ</rt></ruby>の<ruby>使<rt>つか</rt></ruby>い<ruby>方<rt>かた</rt></ruby>

<ruby>画像<rt>がぞう</rt></ruby>を <ruby>表示<rt>ひょうじ</rt></ruby>するには `<img>` <ruby>要素<rt>ようそ</rt></ruby>を <ruby>使<rt>つか</rt></ruby>います。

* src<ruby>属性<rt>ぞくせい</rt></ruby>： <ruby>画像<rt>がぞう</rt></ruby>が ある <ruby>場所<rt>ばしょ</rt></ruby>（パス）を <ruby>指定<rt>してい</rt></ruby>します。
* alt<ruby>属性<rt>ぞくせい</rt></ruby>： <ruby>画像<rt>がぞう</rt></ruby>の <ruby>説明<rt>せつめい</rt></ruby>を <ruby>文字<rt>もじ</rt></ruby>で <ruby>書<rt>か</rt></ruby>きます。
  * <ruby>重要性<rt>じゅうようせい</rt></ruby>： <ruby>目<rt>め</rt></ruby>が <ruby>不自由<rt>ふじゆう</rt></ruby>な <ruby>人<rt>ひと</rt></ruby>が <ruby>使<rt>つか</rt></ruby>う ソフトが この<ruby>文字<rt>もじ</rt></ruby>を <ruby>読<rt>よ</rt></ruby>み<ruby>上<rt>あ</rt></ruby>げます。また、<ruby>画像<rt>がぞう</rt></ruby>が エラーで <ruby>出<rt>で</rt></ruby>ないときにも <ruby>代<rt>か</rt></ruby>わりに <ruby>表示<rt>ひょうじ</rt></ruby>されます。
  * <ruby>良<rt>よ</rt></ruby>い <ruby>例<rt>れい</rt></ruby>： alt="Firefoxのロゴ：<ruby>地球<rt>ちきゅう</rt></ruby>を<ruby>包<rt>つつ</rt></ruby>む<ruby>燃<rt>も</rt></ruby>えるキツネ" の ように、<ruby>何<rt>なに</rt></ruby>が <ruby>書<rt>か</rt></ruby>いてあるか <ruby>具体的<rt>ぐたいてき</rt></ruby>に <ruby>書<rt>か</rt></ruby>くのが <ruby>正<rt>ただ</rt></ruby>しい <ruby>使<rt>つか</rt></ruby>い<ruby>方<rt>かた</rt></ruby>です。

<ruby>空要素<rt>からようそ</rt></ruby> / void element： `<img>` は <ruby>文章<rt>ぶんしょう</rt></ruby>を <ruby>囲<rt>かこ</rt></ruby>まないので、<ruby>終<rt>お</rt></ruby>わりの タグ（`</img>`）が いりません。これを「<ruby>空要素<rt>からようそ</rt></ruby>」と <ruby>呼<rt>よ</rt></ruby>びます。

ファイル<ruby>管理<rt>かんり</rt></ruby>のアドバイス： <ruby>画像<rt>がぞう</rt></ruby>は images/ という <ruby>名前<rt>なまえ</rt></ruby>の フォルダを <ruby>作<rt>つく</rt></ruby>って、その<ruby>中<rt>なか</rt></ruby>に <ruby>入<rt>い</rt></ruby>れましょう。HTMLからは `src="images/写真の名前.jpg"` の ように <ruby>指定<rt>してい</rt></ruby>します。こうすることで、たくさんの ファイルを きれいに <ruby>整<rt>せい</rt></ruby>りできます。

***

### 5. リンクを<ruby>作<rt>つく</rt></ruby>ってページをつなぐ：`<a>`<ruby>要素<rt>ようそ</rt></ruby>

ウェブ（<ruby>蜘蛛<rt>くも</rt></ruby>の<ruby>巣<rt>す</rt></ruby>：くものす）の <ruby>名前<rt>なまえ</rt></ruby>の とおり、ページどうしを つなぐのが「リンク」です。

リンクの<ruby>作<rt>つく</rt></ruby>り<ruby>方<rt>かた</rt></ruby>

1. リンクに したい テキストを <ruby>選<rt>えら</rt></ruby>びます。
2. その テキストを `<a>` タグで <ruby>囲<rt>かこ</rt></ruby>みます。

<div style="page-break-before:always"></div>

3. href <ruby>属性<rt>ぞくせい</rt></ruby>に、<ruby>行<rt>い</rt></ruby>きたい <ruby>先<rt>さき</rt></ruby>の アドレス（URL）を <ruby>書<rt>か</rt></ruby>きます。

```html
<a href="https://www.mozilla.org/">Mozillaのウェブサイト</a>
```

<ruby>大切<rt>たいせつ</rt></ruby>な <ruby>注意点<rt>ちゅういてん</rt></ruby>： アドレスを <ruby>書<rt>か</rt></ruby>くときは、<ruby>必<rt>かなら</rt></ruby>ず `https://` などの <ruby>通信<rt>つうしん</rt></ruby>の ルール（プロトコル） から <ruby>書<rt>か</rt></ruby>き<ruby>始<rt>はじ</rt></ruby>めてください。これがないと、リンクが <ruby>正<rt>ただ</rt></ruby>しく <ruby>動<rt>うご</rt></ruby>きません。また、リンクにする <ruby>言葉<rt>ことば</rt></ruby>は「ここを クリック」ではなく「Mozillaの ウェブサイト」の ように、どこに <ruby>行<rt>い</rt></ruby>くのか わかる <ruby>言葉<rt>ことば</rt></ruby>を <ruby>選<rt>えら</rt></ruby>びましょう。

***

### 6. まとめ：<ruby>自分<rt>じぶん</rt></ruby>のウェブサイトを<ruby>作<rt>つく</rt></ruby>ってみよう

「<ruby>構造<rt>こうぞう</rt></ruby>（HTML）」「テキスト」「<ruby>画像<rt>がぞう</rt></ruby>」「リンク」が <ruby>組<rt>く</rt></ruby>み<ruby>合<rt>あ</rt></ruby>わさることで、<ruby>一<rt>ひと</rt></ruby>つの ページが <ruby>完成<rt>かんせい</rt></ruby>します。

<ruby>初心者<rt>しょしんしゃ</rt></ruby>のための チェックリスト

<ruby>公開<rt>こうかい</rt></ruby>する <ruby>前<rt>まえ</rt></ruby>に、これを <ruby>確認<rt>かくにん</rt></ruby>しましょう：

* [ ] タグの <ruby>閉<rt>と</rt></ruby>じ<ruby>忘<rt>わす</rt></ruby>れは ありませんか？（`<img>`  <ruby>以外<rt>いがい</rt></ruby>、<ruby>終<rt>お</rt></ruby>わりのタグが <ruby>必要<rt>ひつよう</rt></ruby>です）
* [ ] ファイルの<ruby>名前<rt>なまえ</rt></ruby>は <ruby>正<rt>ただ</rt></ruby>しいですか？（<ruby>大文字<rt>おおもじ</rt></ruby>と <ruby>小文字<rt>こもじ</rt></ruby>の <ruby>間違<rt>まちが</rt></ruby>いは ありませんか？ Index.html と index.html は <ruby>違<rt>ちが</rt></ruby>います）
* [ ] <ruby>画像<rt>がぞう</rt></ruby>の パス（フォルダの<ruby>場所<rt>ばしょ</rt></ruby>）は <ruby>正<rt>ただ</rt></ruby>しいですか？（images/ フォルダの <ruby>中<rt>なか</rt></ruby>に <ruby>画像<rt>がぞう</rt></ruby>が ありますか？）
* [ ] リンクの https:// を <ruby>忘<rt>わす</rt></ruby>れていませんか？
* [ ] alt<ruby>属性<rt>ぞくせい</rt></ruby>は わかりやすく <ruby>書<rt>か</rt></ruby>きましたか？

<ruby>次<rt>つぎ</rt></ruby>のステップ： HTMLで <ruby>形<rt>かたち</rt></ruby>が できたら、<ruby>次<rt>つぎ</rt></ruby>は 「CSS」 を <ruby>学<rt>まな</rt></ruby>んで <ruby>色<rt>いろ</rt></ruby>や デザインを きれいに しましょう。さらに 「JavaScript」 を <ruby>使<rt>つか</rt></ruby>えば、<ruby>動<rt>うご</rt></ruby>きのある ページに なります。

<div style="page-break-before:always"></div>

## IV. ウェブサイトをデザインするCSS

### 1. はじめに：CSSとは<ruby>何<rt>なん</rt></ruby>でしょうか？

ウェブサイトを<ruby>作<rt>つく</rt></ruby>るとき、<ruby>文字<rt>もじ</rt></ruby>や<ruby>画像<rt>がぞう</rt></ruby>などの「<ruby>内容<rt>ないよう</rt></ruby>」を<ruby>準備<rt>じゅんび</rt></ruby>するだけでは、まだデザインが<ruby>完成<rt>かんせい</rt></ruby>していません。そこで<ruby>使<rt>つか</rt></ruby>われるのが **CSS（シーエスエス）** です。

CSSは、ウェブサイトの「<ruby>見<rt>み</rt></ruby>た<ruby>目<rt>め</rt></ruby>」を<ruby>整<rt>ととの</rt></ruby>えるための<ruby>専用<rt>せんよう</rt></ruby>の<ruby>言葉<rt>ことば</rt></ruby>です。HTMLで<ruby>作成<rt>さくせい</rt></ruby>した<ruby>文章<rt>ぶんしょう</rt></ruby>に<ruby>色<rt>いろ</rt></ruby>をつけたり、<ruby>大<rt>おお</rt></ruby>きさを変えたり、<ruby>好<rt>す</rt></ruby>きな<ruby>場所<rt>ばしょ</rt></ruby>に<ruby>並<rt>なら</rt></ruby>べたりすることができます。

**HTML（内容）とCSS（スタイル）の<ruby>違<rt>ちが</rt></ruby>い**

ウェブサイトは、<ruby>主<rt>おも</rt></ruby>に2つの<ruby>役割<rt>やくわり</rt></ruby>が<ruby>組<rt>く</rt></ruby>み<ruby>合<rt>あ</rt></ruby>わさってできています。

* HTML（<ruby>内容<rt>ないよう</rt></ruby>）： 「ここにタイトルがある」「ここに<ruby>文章<rt>ぶんしょう</rt></ruby>がある」という、サイトの<ruby>骨組<rt>ほねぐ</rt></ruby>み（<ruby>土台<rt>どだい</rt></ruby>）を<ruby>作<rt>つく</rt></ruby>ります。
* CSS（スタイル）： 「タイトルを<ruby>青色<rt>あおいろ</rt></ruby>にする」「<ruby>文章<rt>ぶんしょう</rt></ruby>の<ruby>横幅<rt>よこはば</rt></ruby>を600ピクセルにする」といった、<ruby>見<rt>み</rt></ruby>た<ruby>目<rt>め</rt></ruby>を<ruby>美<rt>うつく</rt></ruby>しく<ruby>飾<rt>かざ</rt></ruby>ります。

CSSを<ruby>使<rt>つか</rt></ruby>ってデザインを<ruby>整<rt>ととの</rt></ruby>えることで、ウェブサイトはもっと<ruby>読<rt>よ</rt></ruby>みやすくなり、<ruby>訪<rt>おとず</rt></ruby>れた<ruby>人<rt>ひと</rt></ruby>に「<ruby>使<rt>つか</rt></ruby>いやすい」と<ruby>感<rt>かん</rt></ruby>じてもらえるようになります。

**CSSの<ruby>定義<rt>ていぎ</rt></ruby>**

* スタイルシート<ruby>言語<rt>げんご</rt></ruby>： プログラミング<ruby>言語<rt>げんご</rt></ruby>ではなく、<ruby>見<rt>み</rt></ruby>た<ruby>目<rt>め</rt></ruby>を<ruby>指定<rt>してい</rt></ruby>するための<ruby>特別<rt>とくべつ</rt></ruby>な<ruby>言葉<rt>ことば</rt></ruby>です。
* <ruby>要素<rt>ようそ</rt></ruby>の<ruby>装飾<rt>そうしょく</rt></ruby>： HTMLで<ruby>書<rt>か</rt></ruby>かれた<ruby>特定<rt>とくてい</rt></ruby>の<ruby>場所<rt>ばしょ</rt></ruby>を<ruby>選<rt>えら</rt></ruby>んで、<ruby>見<rt>み</rt></ruby>た<ruby>目<rt>め</rt></ruby>を変えることができます。

<ruby>次<rt>つぎ</rt></ruby>のセクションでは、CSSを<ruby>実際<rt>じっさい</rt></ruby>にどうやって<ruby>書<rt>か</rt></ruby>くのか、その<ruby>基本<rt>きほん</rt></ruby>ルールを<ruby>学<rt>まな</rt></ruby>びましょう。

***

### 2. CSSの<ruby>書<rt>か</rt></ruby>き<ruby>方<rt>かた</rt></ruby>（<ruby>構文<rt>こうぶん</rt></ruby>）を<ruby>覚<rt>おぼ</rt></ruby>えましょう

CSSを<ruby>書<rt>か</rt></ruby>くときには、<ruby>決<rt>き</rt></ruby>まった<ruby>形<rt>かたち</rt></ruby>（<ruby>構文<rt>こうぶん</rt></ruby>）があります。「どこの」「<ruby>何<rt>なに</rt></ruby>を」「どう変えるか」という<ruby>順番<rt>じゅんばん</rt></ruby>で<ruby>指示<rt>しじ</rt></ruby>を<ruby>書<rt>か</rt></ruby>きます。

CSSを<ruby>構成<rt>こうせい</rt></ruby>するパーツ

CSSは、<ruby>以下<rt>いか</rt></ruby>のパーツを<ruby>組<rt>く</rt></ruby>み<ruby>合<rt>あ</rt></ruby>わせて<ruby>作<rt>つく</rt></ruby>ります。

1. セレクター（<ruby>選<rt>えら</rt></ruby>びたい<ruby>場所<rt>ばしょ</rt></ruby>）： デザインを変えたいHTMLの<ruby>要素<rt>ようそ</rt></ruby>を<ruby>指定<rt>してい</rt></ruby>します。
2. プロパティ（<ruby>変<rt>か</rt></ruby>えたい<ruby>項目<rt>こうもく</rt></ruby>）： <ruby>色<rt>いろ</rt></ruby>、<ruby>大<rt>おお</rt></ruby>きさ、<ruby>場所<rt>ばしょ</rt></ruby>など。
3. <ruby>値<rt>あたい</rt></ruby>（<ruby>設定<rt>せってい</rt></ruby>する<ruby>内容<rt>ないよう</rt></ruby>）： <ruby>具体的<rt>ぐたいてき</rt></ruby>にどんな<ruby>色<rt>いろ</rt></ruby>にするか、どれくらいの<ruby>大<rt>おお</rt></ruby>きさにするかを<ruby>決<rt>き</rt></ruby>めます。

**<ruby>宣言<rt>せんげん</rt></ruby>とルールセット**

CSSでは、プロパティと<ruby>値<rt>あたい</rt></ruby>を<ruby>組<rt>く</rt></ruby>み<ruby>合<rt>あ</rt></ruby>わせたペアを **「<ruby>宣言<rt>せんげん</rt></ruby>」** と<ruby>呼<rt>よ</rt></ruby>びます。また、セレクターと { } で<ruby>囲<rt>かこ</rt></ruby>まれた<ruby>複数<rt>ふくすう</rt></ruby>の<ruby>宣言<rt>せんげん</rt></ruby>をまとめたものを「ルールセット（Ruleset）」と<ruby>呼<rt>よ</rt></ruby>びます。

<ruby>書<rt>か</rt></ruby>き<ruby>方<rt>かた</rt></ruby>のルールとコード<ruby>例<rt>れい</rt></ruby>

プロパティの<ruby>後<rt>あと</rt></ruby>には<ruby>必<rt>かなら</rt></ruby>ずコロン **`:`** を、<ruby>値<rt>あたい</rt></ruby>の<ruby>後<rt>あと</rt></ruby>には<ruby>必<rt>かなら</rt></ruby>ずセミコロン **`;`** を<ruby>書<rt>か</rt></ruby>きます。

```css
p {
  color: red; /* 宣言1：文字の色（プロパティ）を赤（値）にします */
  font-size: 16px; /* 宣言2：文字の大きさ（プロパティ）を16ピクセル（値）にします */
}
```

<ruby>書<rt>か</rt></ruby>き<ruby>方<rt>かた</rt></ruby>を<ruby>理解<rt>りかい</rt></ruby>したら、<ruby>次<rt>つぎ</rt></ruby>はCSSをHTMLに<ruby>読<rt>よ</rt></ruby>み<ruby>込<rt>こ</rt></ruby>ませる<ruby>方法<rt>ほうほう</rt></ruby>を<ruby>確認<rt>かくにん</rt></ruby>しましょう。

***

### 3. HTMLにCSSを<ruby>読<rt>よ</rt></ruby>み<ruby>込<rt>こ</rt></ruby>ませる<ruby>方法<rt>ほうほう</rt></ruby>

CSSを<ruby>書<rt>か</rt></ruby>くだけでは、ウェブサイトにデザインは<ruby>反映<rt>はんえい</rt></ruby>されません。HTMLとCSSを<ruby>正<rt>ただ</rt></ruby>しくつなぐ<ruby>手順<rt>てじゅん</rt></ruby>が<ruby>必要<rt>ひつよう</rt></ruby>です。

**<ruby>正確<rt>せいかく</rt></ruby>な<ruby>設定<rt>せってい</rt></ruby>が<ruby>大切<rt>たいせつ</rt></ruby>な<ruby>理由<rt>りゆう</rt></ruby>**

ウェブサイトを<ruby>作<rt>つく</rt></ruby>るときは、ファイルを<ruby>整<rt>せい</rt></ruby>りするために styles という<ruby>名前<rt>なまえ</rt></ruby>のフォルダを<ruby>作<rt>つく</rt></ruby>り、その<ruby>中<rt>なか</rt></ruby>に style.css を<ruby>作成<rt>さくせい</rt></ruby>します。

HTMLファイルの `<head>` （ヘッド：サイトの<ruby>設定<rt>せってい</rt></ruby>を書く<ruby>場所<rt>ばしょ</rt></ruby>）<ruby>内<rt>ない</rt></ruby>に、<ruby>以下<rt>いか</rt></ruby>の1行を書きます。

```html
<link href="styles/style.css" rel="stylesheet" />
```

【トラブルを<ruby>避<rt>さ</rt></ruby>けるポイント】  
フォルダ<ruby>名<rt>めい</rt></ruby>やファイル<ruby>名<rt>めい</rt></ruby>が1<ruby>文字<rt>もじ</rt></ruby>でも<ruby>間違<rt>まちが</rt></ruby>っていると、デザインは<ruby>全<rt>まった</rt></ruby>く<ruby>表示<rt>ひょうじ</rt></ruby>されません。  
styles/style.css という「<ruby>道<rt>みち</rt></ruby>すじ（パス）」が<ruby>実際<rt>じっさい</rt></ruby>のフォルダ<ruby>構成<rt>こうせい</rt></ruby>と<ruby>合<rt>あ</rt></ruby>っているか<ruby>慎重<rt>しんちょう</rt></ruby>に<ruby>確認<rt>かくにん</rt></ruby>しましょう。

***

### 4. <ruby>文字<rt>もじ</rt></ruby>のデザインをきれいにする（フォントとテキスト）

<ruby>文字<rt>もじ</rt></ruby>の<ruby>見<rt>み</rt></ruby>た<ruby>目<rt>め</rt></ruby>は、サイトを<ruby>訪<rt>おとず</rt></ruby>れる<ruby>人<rt>ひと</rt></ruby>の「<ruby>読<rt>よ</rt></ruby>みやすさ」に<ruby>大<rt>おお</rt></ruby>きな<ruby>影響<rt>えいきょう</rt></ruby>があります。<ruby>適切<rt>てきせつ</rt></ruby>なフォント選びは、サイトを<ruby>信頼<rt>しんらい</rt></ruby>できる<ruby>印象<rt>いんしょう</rt></ruby>にするための<ruby>戦略<rt>せんりゃく</rt></ruby>です。

**Google Fonts の<ruby>利用<rt>りよう</rt></ruby>**

<ruby>標準<rt>ひょうじゅん</rt></ruby>のフォント<ruby>以外<rt>いがい</rt></ruby>を<ruby>使<rt>つか</rt></ruby>いたいとき、Google Fonts のサービスを<ruby>使<rt>つか</rt></ruby>います。HTML の `<head>` に **自分のstyle.cssより前** に<ruby>読<rt>よ</rt></ruby>み<ruby>込<rt>こ</rt></ruby>ませます。

```html
<!-- Google Fontsの読み込み例（自分のCSSより前に書きます） -->
<link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet" />
<link href="styles/style.css" rel="stylesheet" />
```

**<ruby>読<rt>よ</rt></ruby>みやすさを<ruby>高<rt>たか</rt></ruby>めるプロパティ**

* font-family： フォントの<ruby>種<rt>しゅ</rt></ruby>類  
* font-size： <ruby>文字<rt>もじ</rt></ruby>の<ruby>大<rt>おお</rt></ruby>きさ  
* text-align： <ruby>文<rt>ぶん</rt></ruby>を<ruby>中<rt>なか</rt></ruby>央に<ruby>寄<rt>よ</rt></ruby>せる  
* line-height： <ruby>行間<rt>ぎょうかん</rt></ruby>  
* letter-spacing： <ruby>文<rt>も</rt></ruby>字の<ruby>間隔<rt>かんかく</rt></ruby>

***

### 5. すべては「<ruby>箱<rt>はこ</rt></ruby>（ボックス）」でできている

CSS の<ruby>世界<rt>せかい</rt></ruby>では、すべての<ruby>要素<rt>ようそ</rt></ruby>（<ruby>見出<rt>みだ</rt></ruby>し・<ruby>文章<rt>ぶんしょう</rt></ruby>・<ruby>画像<rt>がぞう</rt></ruby>など）は「<ruby>箱<rt>はこ</rt></ruby>」の<ruby>中<rt>なか</rt></ruby>にあると<ruby>考<rt>かんが</rt></ruby>えます。これを **ボックスモデル** と<ruby>呼<rt>よ</rt></ruby>びます。

|<ruby>要素<rt>ようそ</rt></ruby>|やさしい<ruby>説明<rt>せつめい</rt></ruby>|
|---|---|
|Content|<ruby>文<rt>もん</rt></ruby>字や<ruby>画<rt>が</rt></ruby>像が入る中心部|
|Padding|<ruby>中身<rt>なかみ</rt></ruby>と<ruby>枠線<rt>わくせん</rt></ruby>の<ruby>内側<rt>うちがわ</rt></ruby>の<ruby>余白<rt>よはく</rt></ruby>|
|Border|<ruby>枠線<rt>わくせん</rt></ruby>そのもの|
|Margin|<ruby>枠線<rt>わくせん</rt></ruby>の<ruby>外側<rt>そとがわ</rt></ruby>の<ruby>余白<rt>よはく</rt></ruby>|

***

### 6. <ruby>ページ<rt>ぺーじ</rt></ruby><ruby>全体<rt>ぜんたい</rt></ruby>のレイアウトを<ruby>整<rt>ととの</rt></ruby>える（<ruby>色<rt>いろ</rt></ruby>と<ruby>配置<rt>はいち</rt></ruby>）

<ruby>背景<rt>はいけい</rt></ruby>に<ruby>色<rt>いろ</rt></ruby>をつけ、body の<ruby>幅<rt>はば</rt></ruby>を600pxにし、<ruby>中<rt>なか</rt></ruby>央寄せする<ruby>典型<rt>てんけい</rt></ruby>的な<ruby>設定<rt>せってい</rt></ruby>です。

<div style="page-break-before:always"></div>

```css
html {
  background-color: #00539F; /* ページ全体の背景を青にします */
}

body {
  width: 600px; /* 全体の幅を600ピクセルに固定します */
  margin: 0 auto; /* 上下は0、左右は「自動（auto）」で分けて中央に寄せます */
  background-color: #FF9500; /* bodyの背景を赤みのあるオレンジにします */
  padding: 0 20px 20px 20px; /* 内側に余白を作ります */
  border: 5px solid black; /* 黒い枠線で囲みます */
}
```

margin: 0 auto; の<ruby>仕組<rt>しく</rt></ruby>み：  
ブラウザが左右の空きを半分ずつ割り当て、body が<ruby>中<rt>なか</rt></ruby>央に配置されます。

**タイトルに<ruby>影<rt>かげ</rt></ruby>をつける**

```css
h1 {
  text-shadow: 3px 3px 1px black; /* 横に3px、縦に3px、ぼかし1px、黒い影 */
}
```

**<ruby>画像<rt>がぞう</rt></ruby>を<ruby>中<rt>ちゅう</rt></ruby>央に置く**

```css
img {
  display: block; /* 画像を「ボックス」として扱うように変えます */
  margin: 0 auto; /* これで中央に寄るようになります */
}
```

***

### 7. おわりに：<ruby>素敵<rt>すてき</rt></ruby>なウェブサイトを<ruby>作<rt>つく</rt></ruby>るために

CSS の<ruby>基礎<rt>きそ</rt></ruby>は、<ruby>将来<rt>しょうらい</rt></ruby>のアニメーションや高度レイアウトの<ruby>土台<rt>どだい</rt></ruby>になります。

1. <ruby>値<rt>あたい</rt></ruby>を変えて効果を確認  
2. 他サイトを<ruby>箱<rt>はこ</rt></ruby>として観察  
3. 1項目ずつ保存しながら確認

<ruby>楽<rt>たの</rt></ruby>しみながら、美しいサイトを完成させてください！

<div style="page-break-before:always"></div>

## V. ウェブサイトを<ruby>動<rt>うご</rt></ruby>かすJavaScript

ウェブサイトを<ruby>見<rt>み</rt></ruby>たときに、ボタンを<ruby>押<rt>お</rt></ruby>して<ruby>画面<rt>がめん</rt></ruby>が<ruby>変<rt>か</rt></ruby>わったり、<ruby>画像<rt>がぞう</rt></ruby>が<ruby>動<rt>うご</rt></ruby>いたりすることはありませんか？  
それは「JavaScript」という<ruby>言葉<rt>ことば</rt></ruby>が<ruby>働<rt>はたら</rt></ruby>いているからです。

このガイドでは、プログラミングが<ruby>初<rt>はじ</rt></ruby>めての<ruby>人<rt>ひと</rt></ruby>や、<ruby>日本語<rt>にほんご</rt></ruby>を<ruby>勉強<rt>べんきょう</rt></ruby>中の<ruby>留学生<rt>りゅうがくせい</rt></ruby>にも<ruby>分<rt>わ</rt></ruby>かりやすく、JavaScriptの<ruby>基本<rt>きほん</rt></ruby>を<ruby>説明<rt>せつめい</rt></ruby>します。

***

### 1. はじめに：JavaScriptとは<ruby>何<rt>なに</rt></ruby>か

ウェブサイトを<ruby>作<rt>つく</rt></ruby>るとき、HTMLは「<ruby>骨組<rt>ほねぐ</rt></ruby>み」を、CSSは「<ruby>見<rt>み</rt></ruby>た<ruby>目<rt>め</rt></ruby>」を<ruby>作<rt>つく</rt></ruby>ります。そこに「<ruby>動<rt>うご</rt></ruby>き」を<ruby>加<rt>くわ</rt></ruby>えるのがJavaScriptの<ruby>役割<rt>やくわり</rt></ruby>です。

JavaScriptを<ruby>使<rt>つか</rt></ruby>うと、ユーザーの<ruby>操作<rt>そうさ</rt></ruby>に<ruby>合<rt>あ</rt></ruby>わせてサイトの<ruby>表示<rt>ひょうじ</rt></ruby>を<ruby>変<rt>か</rt></ruby>えることができます。  
ただ<ruby>情報<rt>じょうほう</rt></ruby>を読むだけのページから、ユーザーといっしょに<ruby>動<rt>うご</rt></ruby>く「<ruby>体験<rt>たいけん</rt></ruby>」へと変えることができる、とても<ruby>大切<rt>たいせつ</rt></ruby>な<ruby>技術<rt>ぎじゅつ</rt></ruby>です。

**JavaScriptでできること**

JavaScriptを<ruby>使<rt>つか</rt></ruby>って、<ruby>以<rt>い</rt></ruby>下のような<ruby>動<rt>うご</rt></ruby>きを<ruby>作<rt>つく</rt></ruby>ることができます：

* チェックする： フォームに<ruby>入力<rt>にゅうりょく</rt></ruby>されたデータが<ruby>正<rt>ただ</rt></ruby>しいか<ruby>確認<rt>かくにん</rt></ruby>します。
* <ruby>動<rt>うご</rt></ruby>かす： ボタンをクリックしたときに、<ruby>何<rt>なに</rt></ruby>かを<ruby>実行<rt>じっこう</rt></ruby>します。
* <ruby>計算<rt>けいさん</rt></ruby>する： ゲームの<ruby>点数<rt>てんすう</rt></ruby>や、<ruby>数字<rt>すうじ</rt></ruby>の<ruby>計算<rt>けいさん</rt></ruby>をおこないます。
* デザインを<ruby>変<rt>か</rt></ruby>える： スタイル（<ruby>色<rt>いろ</rt></ruby>や<ruby>大<rt>おお</rt></ruby>きさ）を<ruby>自由<rt>じゆう</rt></ruby>に<ruby>変<rt>か</rt></ruby>えます。
* アニメーション： <ruby>画像<rt>がぞう</rt></ruby>や<ruby>文字<rt>もじ</rt></ruby>をスムーズに<ruby>動<rt>うご</rt></ruby>かします。

***

### 2. プログラミングの「<ruby>基本<rt>きほん</rt></ruby>の<ruby>道具箱<rt>どうぐばこ</rt></ruby>」

プログラムを<ruby>作<rt>つく</rt></ruby>るとは、いくつかの<ruby>道具<rt>どうぐ</rt></ruby>を<ruby>組<rt>く</rt></ruby>み<ruby>合<rt>あ</rt></ruby>わせて「<ruby>命令<rt>めいれい</rt></ruby>」をつくることです。JavaScriptを<ruby>動<rt>うご</rt></ruby>かす4つの<ruby>大切<rt>たいせつ</rt></ruby>な<ruby>概念<rt>がいねん</rt></ruby>があります。

1. <ruby>変数<rt>へんすう</rt></ruby> (Variables)： データを<ruby>一時的<rt>いちじてき</rt></ruby>に<ruby>入<rt>い</rt></ruby>れておく「<ruby>入<rt>い</rt></ruby>れ<ruby>物<rt>もの</rt></ruby>」。
2. <ruby>関数<rt>かんすう</rt></ruby> (Functions)： いくつかの<ruby>命令<rt>めいれい</rt></ruby>をまとめた<ruby>便利<rt>べんり</rt></ruby>なセット。
3. <ruby>条件分岐<rt>じょうけんぶんき</rt></ruby> (Conditionals)： 「もし〜ならA、そうでなければB」。
4. イベント (Events)： 「クリックされた」などの<ruby>動作<rt>どうさ</rt></ruby>のきっかけ。

***

### 3. <ruby>実践<rt>じっせん</rt></ruby>：ウェブサイトにJavaScriptを<ruby>入<rt>い</rt></ruby>れる

HTML、CSS、JavaScript の3つが<ruby>連携<rt>れんけい</rt></ruby>してページが<ruby>動<rt>うご</rt></ruby>きます。

**<ruby>設定<rt>せってい</rt></ruby>の<ruby>手順<rt>てじゅん</rt></ruby>**

1. scripts フォルダを作り、その中に main.js を作成します。
2. HTMLファイルの `<head>` の終わる直前に次を<ruby>書<rt>か</rt></ruby>きます：

```html
<script src="scripts/main.js"></script>
```

* CSSの `<link>` と同じ仕組みで、JavaScript を<ruby>読<rt>よ</rt></ruby>み込みます。

**<ruby>要素<rt>ようそ</rt></ruby>を<ruby>選<rt>えら</rt></ruby>んで<ruby>動<rt>うご</rt></ruby>かす**

```javascript
let myHeading = document.querySelector('h1');
myHeading.textContent = 'Hello world!';
```

* 1行目： `<h1>` を<ruby>選<rt>えら</rt></ruby>び、myHeading に<ruby>入<rt>い</rt></ruby>れます。  
* 2行目： textContent を “Hello world!” に<ruby>変<rt>か</rt></ruby>えます。

ヒント： `//` で<ruby>書<rt>か</rt></ruby>いた<ruby>行<rt>ぎょう</rt></ruby>はコメントとして<ruby>無視<rt>むし</rt></ruby>されます。

***

### 4. <ruby>応用<rt>おうよう</rt></ruby>：<ruby>画像<rt>がぞう</rt></ruby>チェンジャーと<ruby>条件分岐<rt>じょうけんぶんき</rt></ruby>

クリックで<ruby>画像<rt>がぞう</rt></ruby>が入れ替わる仕組みです。

**<ruby>手順<rt>てじゅん</rt></ruby>**

1. <ruby>画像<rt>がぞう</rt></ruby>を JavaScript で<ruby>選<rt>えら</rt></ruby>ぶ  
2. クリックされるのを待つ  
3. 今の src を<ruby>確認<rt>かくにん</rt></ruby>  
4. if 文で切り替える  

<div style="page-break-before:always"></div>

**<ruby>実践<rt>じっせん</rt></ruby>コード**

```javascript
let myImage = document.querySelector('img');

myImage.onclick = function() {
  let mySrc = myImage.getAttribute('src');
  if (mySrc === 'images/images/photo1.jpg') {
    myImage.setAttribute('src', 'images/photo2.jpg');
  } else {
    myImage.setAttribute('src', 'images/photo1.jpg');
  }
}
```

* myImage.onclick： クリック時のイベント  
* getAttribute： 現在の src を調べる  
* setAttribute： src を書き換える  
* if...else： <ruby>条件<rt>じょうけん</rt></ruby>で<ruby>処理<rt>しょり</rt></ruby>を切り替え

***

### 6. <ruby>まとめ<rt>まとめ</rt></ruby>と<ruby>次<rt>つぎ</rt></ruby>のステップ

お<ruby>疲<rt>つか</rt></ruby>れさまでした！これでJavaScriptの<ruby>基礎<rt>きそ</rt></ruby>を学びました。

* HTML/CSS： ページの<ruby>土台<rt>どだい</rt></ruby>と<ruby>見<rt>み</rt></ruby>た<ruby>目<rt>め</rt></ruby>  
* JavaScript： <ruby>動<rt>うご</rt></ruby>きを加える<ruby>技術<rt>ぎじゅつ</rt></ruby>  

JavaScript は ゆっくり学べば確実に身につきます。  
MDNの教材（日本語 / 英語）もとても良い参考になります。

少しずつ練習して、ぜひあなたのオリジナルの<ruby>動<rt>うご</rt></ruby>くウェブサイトを<ruby>作<rt>つく</rt></ruby>ってください！

