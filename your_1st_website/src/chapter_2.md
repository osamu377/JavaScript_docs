# II. デザインと<ruby>計画<rt>けいかく</rt></ruby>のガイドブック

ウェブサイトを<ruby>作<rt>つく</rt></ruby>るとき、いきなりパソコンでコード（プログラムの<ruby>言葉<rt>ことば</rt></ruby>）を<ruby>書<rt>か</rt></ruby>き<ruby>始<rt>はじ</rt></ruby>めるのは、おすすめしません。まずは「<ruby>計画<rt>けいかく</rt></ruby>（プランニング）」をしましょう。

このガイドブックでは、ウェブ<ruby>開発<rt>かいはつ</rt></ruby>の<ruby>専門家<rt>せんもんか</rt></ruby>が、<ruby>留学生<rt>りゅうがくせい</rt></ruby>のみなさんにも<ruby>分<rt>わ</rt></ruby>かりやすい「やさしい<ruby>日本語<rt>にほんご</rt></ruby>」で、サイト<ruby>作<rt>づく</rt></ruby>りの<ruby>準備<rt>じゅんび</rt></ruby>について<ruby>教<rt>おし</rt></ruby>えます。

***

## 1. はじめに：なぜ「<ruby>計画<rt>けいかく</rt></ruby>」が<ruby>大切<rt>たいせつ</rt></ruby>なのか

<ruby>家<rt>いえ</rt></ruby>を<ruby>建<rt>た</rt></ruby>てるときに「<ruby>設計図<rt>せっけいず</rt></ruby>」が<ruby>必要<rt>ひつよう</rt></ruby>なように、ウェブサイトにも<ruby>計画<rt>けいかく</rt></ruby>が<ruby>必要<rt>ひつよう</rt></ruby>です。コードを<ruby>書<rt>か</rt></ruby>く<ruby>前<rt>まえ</rt></ruby>に<ruby>計画<rt>けいかく</rt></ruby>を<ruby>立<rt>た</rt></ruby>てるのには、<ruby>大<rt>おお</rt></ruby>きな<ruby>理由<rt>りゆう</rt></ruby>があります。

* 「<ruby>作<rt>つく</rt></ruby>り<ruby>直<rt>なお</rt></ruby>し」をふせぐ： <ruby>何<rt>なに</rt></ruby>も<ruby>決<rt>き</rt></ruby>めずに<ruby>作<rt>つく</rt></ruby>ると、あとで「やっぱり<ruby>違<rt>ちが</rt></ruby>う！」となって、<ruby>時間<rt>じかん</rt></ruby>をむだにしてしまいます。
* <ruby>最後<rt>さいご</rt></ruby>まで<ruby>完成<rt>かんせい</rt></ruby>できる： <ruby>最初<rt>さいしょ</rt></ruby>にやることを<ruby>決<rt>き</rt></ruby>めると、<ruby>迷<rt>まよ</rt></ruby>わずに<ruby>最後<rt>さいご</rt></ruby>まで<ruby>作<rt>つく</rt></ruby>ることができます。

<ruby>計画<rt>けいかく</rt></ruby>を<ruby>立<rt>た</rt></ruby>てることは、プロのエンジニアも<ruby>一番<rt>いちばん</rt></ruby><ruby>大切<rt>たいせつ</rt></ruby>にしているステップです。

***

## 2. ウェブサイトの<ruby>目的<rt>もくてき</rt></ruby>を<ruby>整理<rt>せいり</rt></ruby>する

<ruby>最初<rt>さいしょ</rt></ruby>のプロジェクトでは、<ruby>内容<rt>ないよう</rt></ruby>を「シンプル」にすることが<ruby>成功<rt>せいこう</rt></ruby>のヒミツです。<ruby>大<rt>おお</rt></ruby>きすぎる<ruby>目標<rt>もくひょう</rt></ruby>を<ruby>立<rt>た</rt></ruby>てると、<ruby>途中<rt>とちゅう</rt></ruby>で<ruby>嫌<rt>いや</rt></ruby>になって<ruby>諦<rt>あきら</rt></ruby>めてしまうからです。

まずは、<ruby>次<rt>つぎ</rt></ruby>の3つの<ruby>質問<rt>しつもん</rt></ruby>に<ruby>答<rt>こた</rt></ruby>えてみましょう。

1. このサイトは<ruby>何<rt>なに</rt></ruby>についてのサイトですか？（<ruby>例<rt>れい</rt></ruby>：<ruby>好<rt>す</rt></ruby>きな<ruby>犬<rt>いぬ</rt></ruby>について、<ruby>旅行<rt>りょこう</rt></ruby>したニューヨークについて、パックマン（Pac-Man）についてなど）
2. どんな<ruby>情報<rt>じょうほう</rt></ruby>を<ruby>紹介<rt>しょうかい</rt></ruby>しますか？（ウェブサイトの<ruby>名前<rt>なまえ</rt></ruby>を<ruby>決<rt>き</rt></ruby>めましょう。そして、1つの「<ruby>見出<rt>みだ</rt></ruby>し（タイトル）」、1つの「<ruby>画像<rt>がぞう</rt></ruby>」、2〜3<ruby>個<rt>こ</rt></ruby>の「<ruby>段落<rt>だんらく</rt></ruby>（<ruby>短<rt>みじか</rt></ruby>い<ruby>文章<rt>ぶんしょう</rt></ruby>）」を<ruby>考<rt>かんが</rt></ruby>えてください）
3. どんな<ruby>見<rt>み</rt></ruby>た<ruby>目<rt>め</rt></ruby>のサイトにしますか？（<ruby>背景<rt>はいけい</rt></ruby>は<ruby>何色<rt>なにいろ</rt></ruby>がいいですか？ <ruby>文字<rt>もじ</rt></ruby>の<ruby>形<rt>かたち</rt></ruby>は「まじめ」ですか？ それとも「かわいい」ですか？」）

<ruby>専門家<rt>せんもんか</rt></ruby>の<ruby>知恵<rt>ちえ</rt></ruby>：デザインガイド

<ruby>大<rt>おお</rt></ruby>きなプロジェクトでは、「デザインガイド（デザインシステム）」というルールブックを<ruby>作<rt>つく</rt></ruby>ります。<ruby>例<rt>たと</rt></ruby>えば、Firefoxには「Firefox Acorn Design System」という<ruby>有名<rt>ゆうめい</rt></ruby>なガイドがあります。これを<ruby>見<rt>み</rt></ruby>ると、プロがどうやって「<ruby>色<rt>いろ</rt></ruby>」や「<ruby>文字<rt>もじ</rt></ruby>」のルールを<ruby>統一<rt>とういつ</rt></ruby>して、きれいに<ruby>見<rt>み</rt></ruby>せているかが<ruby>分<rt>わ</rt></ruby>かります。

<ruby>目的<rt>もくてき</rt></ruby>が<ruby>決<rt>き</rt></ruby>まったら、<ruby>次<rt>つぎ</rt></ruby>はそれを<ruby>絵<rt>え</rt></ruby>に<ruby>描<rt>か</rt></ruby>いてみましょう。

> [!note]
> 「プロジェクト」は<ruby>一<rt>ひと</rt></ruby>つのウェブサイトやアプリケーションを<ruby>作<rt>つく</rt></ruby>るための<ruby>計画<rt>けいかく</rt></ruby>、あるいは、その<ruby>計画<rt>けいかく</rt></ruby>に<ruby>関<rt>かか</rt></ruby>わる<ruby>人々<rt>ひとびと</rt></ruby>のグループのことです。そうした<ruby>計画<rt>けいかく</rt></ruby>のためのデジタル<ruby>素材<rt>そざい</rt></ruby>やソースコードなどをまとめたものを<ruby>指<rt>さ</rt></ruby>すこともあります。

***

## 3. デザインのスケッチ：<ruby>見<rt>み</rt></ruby>た<ruby>目<rt>め</rt></ruby>のイメージを<ruby>作<rt>つく</rt></ruby>る

ペンと<ruby>紙<rt>かみ</rt></ruby>を<ruby>使<rt>つか</rt></ruby>って、サイトの<ruby>形<rt>かたち</rt></ruby>を<ruby>自由<rt>じゆう</rt></ruby>に<ruby>描<rt>えが</rt></ruby>いてみましょう。これを「スケッチ」と<ruby>言<rt>い</rt></ruby>います。

プロも、<ruby>最初<rt>さいしょ</rt></ruby>はパソコンを<ruby>使<rt>つか</rt></ruby>わず、<ruby>紙<rt>かみ</rt></ruby>に<ruby>書<rt>か</rt></ruby>くことから<ruby>始<rt>はじ</rt></ruby>めます。ここで<ruby>大切<rt>たいせつ</rt></ruby>なのは、**「<ruby>完璧<rt>かんぺき</rt></ruby>を<ruby>目指<rt>めざ</rt></ruby>さないこと」** です。<ruby>有名<rt>ゆうめい</rt></ruby>な<ruby>画家<rt>がか</rt></ruby>のゴッホ（Van Gogh）のように<ruby>上手<rt>じょうず</rt></ruby>に<ruby>描<rt>か</rt></ruby>く<ruby>必要<rt>ひつよう</rt></ruby>はありません。どこにタイトルがあり、どこに<ruby>画像<rt>がぞう</rt></ruby>があるか、<ruby>自分<rt>じぶん</rt></ruby>が<ruby>分<rt>わ</rt></ruby>かれば<ruby>十分<rt>じゅうぶん</rt></ruby>です。

また、ウェブ<ruby>制作<rt>せいさく</rt></ruby>の<ruby>現場<rt>げんば</rt></ruby>には、2つの<ruby>役割<rt>やくわり</rt></ruby>があります。

| デザイナーの<ruby>種類<rt>しゅるい</rt></ruby> | どんな<ruby>仕事<rt>しごと</rt></ruby>をする<ruby>人<rt>ひと</rt></ruby>？ |
|---|---|
| グラフィックデザイナー | ウェブサイトの <ruby>見<rt>み</rt></ruby>た<ruby>目<rt>め</rt></ruby>を きれいに デザインする <ruby>人<rt>ひと</rt></ruby> |
| UXデザイナー | ユーザーが ボタンを <ruby>押<rt>お</rt></ruby>しやすくしたり、<ruby>情報<rt>じょうほう</rt></ruby>を <ruby>見<rt>み</rt></ruby>つけやすくしたりする <ruby>人<rt>ひと</rt></ruby> |

<ruby>今<rt>いま</rt></ruby>は、あなたがこの<ruby>両方<rt>りょうほう</rt></ruby>の<ruby>仕事<rt>しごと</rt></ruby>をします。<ruby>自分<rt>じぶん</rt></ruby>のアイデアを<ruby>自由<rt>じゆう</rt></ruby>に<ruby>紙<rt>かみ</rt></ruby>に<ruby>書<rt>か</rt></ruby>いてみてください。

***

## 4. テーマカラー（<ruby>色<rt>いろ</rt></ruby>の<ruby>名前<rt>なまえ</rt></ruby>とコード）を<ruby>決<rt>き</rt></ruby>める

サイトの<ruby>印象<rt>いんしょう</rt></ruby>を<ruby>決<rt>き</rt></ruby>める「<ruby>色<rt>いろ</rt></ruby>」を<ruby>選<rt>えら</rt></ruby>びましょう。

1. <ruby>色<rt>いろ</rt></ruby>を<ruby>選<rt>えら</rt></ruby>ぶ： カラーピッカーなどのツールで、<ruby>背景<rt>はいけい</rt></ruby>に<ruby>使<rt>つか</rt></ruby>いたい<ruby>色<rt>いろ</rt></ruby>を<ruby>探<rt>さが</rt></ruby>します。
2. コードをメモする： <ruby>色<rt>いろ</rt></ruby>を<ruby>選<rt>えら</rt></ruby>ぶと、#660066 のような「6つの<ruby>英数字<rt>えいすうじ</rt></ruby>」が<ruby>表示<rt>ひょうじ</rt></ruby>されます。これを **16<ruby>進数<rt>しんすう</rt></ruby>コード（hex code／ヘックスコード）** と<ruby>呼<rt>よ</rt></ruby>びます。

> [!note]
> 16<ruby>進数<rt>しんすう</rt></ruby>コード（hex code）とは
> コンピュータが「この<ruby>色<rt>いろ</rt></ruby>です！」と<ruby>正<rt>ただ</rt></ruby>しく<ruby>理解<rt>りかい</rt></ruby>するための<ruby>専用<rt>せんよう</rt></ruby>の<ruby>番号<rt>ばんごう</rt></ruby>です。あとでコードを<ruby>書<rt>か</rt></ruby>くときに<ruby>使<rt>つか</rt></ruby>うので、<ruby>必<rt>かなら</rt></ruby>ずメモしておきましょう。

***

## 5. <ruby>画像<rt>がぞう</rt></ruby>の<ruby>準備<rt>じゅんび</rt></ruby>：ルールを<ruby>守<rt>まも</rt></ruby>って<ruby>探<rt>さが</rt></ruby>す<ruby>方法<rt>ほうほう</rt></ruby>

インターネットにある<ruby>画像<rt>がぞう</rt></ruby>には「<ruby>持<rt>も</rt></ruby>ち<ruby>主<rt>ぬし</rt></ruby>」があります。これを **<ruby>著作権<rt>ちょさくけん</rt></ruby>（コピーライト）** と<ruby>言<rt>い</rt></ruby>います。<ruby>勝手<rt>かって</rt></ruby>に<ruby>使<rt>つか</rt></ruby>うと<ruby>法律<rt>ほうりつ</rt></ruby>のトラブルになることがあるので、<ruby>注意<rt>ちゅうい</rt></ruby>してください。

「<ruby>自由<rt>じゆう</rt></ruby>に<ruby>使<rt>つか</rt></ruby>ってもいい<ruby>画像<rt>がぞう</rt></ruby>」をGoogleで<ruby>探<rt>さが</rt></ruby>す<ruby>方法<rt>ほうほう</rt></ruby>は、<ruby>次<rt>つぎ</rt></ruby>の<ruby>通<rt>とお</rt></ruby>りです。

1. Google<ruby>画像<rt>がぞう</rt></ruby><ruby>検索<rt>けんさく</rt></ruby>を<ruby>使<rt>つか</rt></ruby>う： <ruby>好<rt>す</rt></ruby>きな<ruby>言葉<rt>ことば</rt></ruby>で<ruby>検索<rt>けんさく</rt></ruby>します。
2. ツールを<ruby>使<rt>つか</rt></ruby>う： <ruby>検索結果<rt>けんさくけっか</rt></ruby>の<ruby>画面<rt>がめん</rt></ruby>にある「ツール」ボタンをクリックします。
3. ライセンスを<ruby>選<rt>えら</rt></ruby>ぶ： その<ruby>下<rt>した</rt></ruby>に<ruby>表示<rt>ひょうじ</rt></ruby>される「<ruby>使用権<rt>しようけん</rt></ruby>」をクリックし、「クリエイティブ・コモンズ ライセンス」を<ruby>選<rt>えら</rt></ruby>びます。
4. <ruby>保存<rt>ほぞん</rt></ruby>する： <ruby>好<rt>す</rt></ruby>きな<ruby>画像<rt>がぞう</rt></ruby>を<ruby>見<rt>み</rt></ruby>つけたら、<ruby>右<rt>みぎ</rt></ruby>クリック（Macは Ctrl + クリック）をして、「<ruby>名前<rt>なまえ</rt></ruby>を<ruby>付<rt>つ</rt></ruby>けて<ruby>画像<rt>がぞう</rt></ruby>を<ruby>保存<rt>ほぞん</rt></ruby>」を<ruby>選<rt>えら</rt></ruby>びます。

***

## 6. フォント（<ruby>文字<rt>もじ</rt></ruby>の<ruby>形<rt>かたち</rt></ruby>）の<ruby>選択<rt>せんたく</rt></ruby>

フォントには2つのタイプがあります。

* ウェブセーフフォント： どのパソコンにも<ruby>最初<rt>さいしょ</rt></ruby>から<ruby>入<rt>はい</rt></ruby>っている<ruby>安心<rt>あんしん</rt></ruby>なフォントです（<ruby>例<rt>れい</rt></ruby>：Arial, Times New Roman）。
* Google Fonts： デザイン<ruby>性<rt>せい</rt></ruby>が<ruby>高<rt>たか</rt></ruby>いフォントを<ruby>無料<rt>むりょう</rt></ruby>で<ruby>借<rt>か</rt></ruby>りられるサービスです。

ここでは、Google Fontsを<ruby>使<rt>つか</rt></ruby>う<ruby>手順<rt>てじゅん</rt></ruby>を<ruby>説明<rt>せつめい</rt></ruby>します。

1. Google Fontsへ<ruby>行<rt>い</rt></ruby>く： サイトのイメージに<ruby>合<rt>あ</rt></ruby>うフォントを<ruby>探<rt>さが</rt></ruby>します。
2. コードを<ruby>取得<rt>しゅとく</rt></ruby>する： <ruby>好<rt>す</rt></ruby>きなフォントを<ruby>選<rt>えら</rt></ruby>び、「Get font」ボタンを<ruby>押<rt>お</rt></ruby>してから、「Get embed code（<ruby>埋<rt>う</rt></ruby>め<ruby>込<rt>こ</rt></ruby>みコードを<ruby>取得<rt>しゅとく</rt></ruby>）」をクリックします。
3. 2つのコードを<ruby>保存<rt>ほぞん</rt></ruby>する： <ruby>画面<rt>がめん</rt></ruby>に<ruby>表示<rt>ひょうじ</rt></ruby>された **2つのコードブロック（2つのまとまったコード）** を<ruby>両方<rt>りょうほう</rt></ruby>ともコピーして、メモ<ruby>帳<rt>ちょう</rt></ruby>などに<ruby>保存<rt>ほぞん</rt></ruby>してください。フォントを<ruby>動<rt>うご</rt></ruby>かすには、この2つが<ruby>両方<rt>りょうほう</rt></ruby><ruby>必要<rt>ひつよう</rt></ruby>です。

⚠️ <ruby>注意<rt>ちゅうい</rt></ruby>：<ruby>商業利用<rt>しょうぎょうりよう</rt></ruby>について フォントにもライセンスがあります。<ruby>勉強<rt>べんきょう</rt></ruby>で<ruby>使<rt>つか</rt></ruby>うのは<ruby>大丈夫<rt>だいじょうぶ</rt></ruby>ですが、<ruby>将来<rt>しょうらい</rt></ruby>、<ruby>仕事<rt>しごと</rt></ruby>でサイトを<ruby>作<rt>つく</rt></ruby>るときは、<ruby>必<rt>かなら</rt></ruby>ず「<ruby>商売<rt>しょうばい</rt></ruby>（ビジネス）で<ruby>使<rt>つか</rt></ruby>ってもいいか」を<ruby>確認<rt>かくにん</rt></ruby>しましょう。

***

## 7. まとめと<ruby>次<rt>つぎ</rt></ruby>のステップ

お<ruby>疲<rt>つか</rt></ruby>れさまでした！これで「サイトの<ruby>設計図<rt>せっけいず</rt></ruby>」と「<ruby>素材<rt>そざい</rt></ruby>」がすべて<ruby>揃<rt>そろ</rt></ruby>いました。

* <ruby>計画<rt>けいかく</rt></ruby>： どんな<ruby>内容<rt>ないよう</rt></ruby>にするか<ruby>決<rt>き</rt></ruby>めた。
* スケッチ： レイアウトを<ruby>紙<rt>かみ</rt></ruby>に<ruby>書<rt>か</rt></ruby>いた。
* <ruby>素材<rt>そざい</rt></ruby>： <ruby>色<rt>いろ</rt></ruby>のコード、<ruby>画像<rt>がぞう</rt></ruby>、フォントの<ruby>準備<rt>じゅんび</rt></ruby>ができた。

しっかりとした「<ruby>土台<rt>どだい</rt></ruby>」ができたので、<ruby>次<rt>つぎ</rt></ruby>のステップである「HTMLやCSSを<ruby>書<rt>か</rt></ruby>く<ruby>作業<rt>さぎょう</rt></ruby>」を、<ruby>自信<rt>じしん</rt></ruby>を<ruby>持<rt>も</rt></ruby>って<ruby>進<rt>すす</rt></ruby>めることができます。

<ruby>準備<rt>じゅんび</rt></ruby>はバッチリです。さあ、<ruby>次<rt>つぎ</rt></ruby>は<ruby>実際<rt>じっさい</rt></ruby>にコンピュータで、あなただけのウェブサイトを<ruby>形<rt>かたち</rt></ruby>にしていきましょう！
