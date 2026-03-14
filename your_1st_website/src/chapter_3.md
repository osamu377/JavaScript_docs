# III. ウェブサイトの<ruby>形<rt>かたち</rt></ruby>を<ruby>作<rt>つく</rt></ruby>ろう

ウェブサイトを<ruby>作<rt>つく</rt></ruby>るための <ruby>最初<rt>さいしょ</rt></ruby>の<ruby>一歩<rt>いっぽ</rt></ruby>へ ようこそ！ プログラミングや ウェブ<ruby>制作<rt>せいさく</rt></ruby>を <ruby>始<rt>はじ</rt></ruby>めるとき、 <ruby>最初<rt>さいしょ</rt></ruby>に <ruby>覚<rt>おぼ</rt></ruby>えるのが「HTML」です。

HTMLは ウェブサイトの「<ruby>骨組<rt>ほねぐ</rt></ruby>み」、つまり <ruby>構造<rt>こうぞう</rt></ruby>を <ruby>作<rt>つく</rt></ruby>るための <ruby>言葉<rt>ことば</rt></ruby>です。この <ruby>基本<rt>きほん</rt></ruby>を <ruby>正<rt>ただ</rt></ruby>しく <ruby>知<rt>し</rt></ruby>ることは、ウェブサイトを <ruby>作<rt>つく</rt></ruby>る <ruby>プロ<rt>ぷろ</rt></ruby>（<ruby>仕事<rt>しごと</rt></ruby>を する <ruby>人<rt>ひと</rt></ruby>）に なるために、とても <ruby>大切<rt>たいせつ</rt></ruby>なことです。

> [!note]
> 「<ruby>骨組<rt>ほねぐ</rt></ruby>み」は、もとは「からだの<ruby>骨<rt>ほね</rt></ruby>の<ruby>組<rt>く</rt></ruby>み<ruby>立<rt>た</rt></ruby>て」のことですが、そこからの「<ruby>例<rt>たと</rt></ruby>え」で、<ruby>建造物<rt>けんぞうぶつ</rt></ruby>・<ruby>機械<rt>きかい</rt></ruby>などの<ruby>基礎<rt>きそ</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>構造<rt>こうぞう</rt></ruby>の<ruby>部分<rt>ぶぶん</rt></ruby>のことも<ruby>指<rt>さ</rt></ruby>します。

***

## 1. HTMLとは<ruby>何<rt>なに</rt></ruby>？：ウェブの<ruby>基本<rt>きほん</rt></ruby>を<ruby>理解<rt>りかい</rt></ruby>する

**HTML（HyperText Markup Language）** は、テキスト（<ruby>文字<rt>もじ</rt></ruby>）に「<ruby>印<rt>しるし</rt></ruby>」を つけて、ウェブサイトの <ruby>構造<rt>こうぞう</rt></ruby>を <ruby>作<rt>つく</rt></ruby>るための「マークアップ<ruby>言語<rt>げんご</rt></ruby>」です。

HTMLの <ruby>役割<rt>やくわり</rt></ruby>を わかりやすく <ruby>例<rt>たと</rt></ruby>えると、**「<ruby>荷物<rt>にもつ</rt></ruby>に ラベルを <ruby>貼<rt>は</rt></ruby>る <ruby>作業<rt>さぎょう</rt></ruby>」** に <ruby>似<rt>に</rt></ruby>ています。ただの テキストに「これは <ruby>見出<rt>みだ</rt></ruby>しです」「これは <ruby>段落<rt>だんらく</rt></ruby>です」という ラベルを <ruby>貼<rt>は</rt></ruby>ることで、ブラウザ（Google Chromeなど）が その<ruby>意味<rt>いみ</rt></ruby>を <ruby>理解<rt>りかい</rt></ruby>できるようになります。

* <ruby>要素<rt>ようそ</rt></ruby> / Elementとは： テキストを「タグ」と <ruby>呼<rt>よ</rt></ruby>ばれる <ruby>記号<rt>きごう</rt></ruby>で <ruby>囲<rt>かこ</rt></ruby>んだ セットのことです。
* ブラウザへの <ruby>伝言<rt>でんごん</rt></ruby>： タグを <ruby>使<rt>つか</rt></ruby>うことで、ブラウザに「ここから ここまでが <ruby>段落<rt>だんらく</rt></ruby>だ」と <ruby>伝<rt>つた</rt></ruby>えることができます。

HTMLを <ruby>使<rt>つか</rt></ruby>う <ruby>理由<rt>りゆう</rt></ruby>： もし HTMLが なければ、すべての <ruby>文字<rt>もじ</rt></ruby>が <ruby>一行<rt>いちぎょう</rt></ruby>に つながってしまい、とても <ruby>読<rt>よ</rt></ruby>みにくくなります。また、<ruby>目<rt>め</rt></ruby>が <ruby>見<rt>み</rt></ruby>えにくい <ruby>人<rt>ひと</rt></ruby>が <ruby>使<rt>つか</rt></ruby>う「<ruby>音声<rt>おんせい</rt></ruby><ruby>読<rt>よ</rt></ruby>み<ruby>上<rt>あ</rt></ruby>げソフト」も、どこが <ruby>大事<rt>だいじ</rt></ruby>な <ruby>場所<rt>ばしょ</rt></ruby>なのか わからなくなってしまいます。HTMLで <ruby>正<rt>ただ</rt></ruby>しく <ruby>構造<rt>こうぞう</rt></ruby>を <ruby>作<rt>つく</rt></ruby>ることで、<ruby>誰<rt>だれ</rt></ruby>にでも <ruby>意味<rt>いみ</rt></ruby>が <ruby>伝<rt>つた</rt></ruby>わる ページに なります。

***

## 2. HTMLファイルの<ruby>基本<rt>きほん</rt></ruby>の<ruby>形<rt>かたち</rt></ruby>

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

> [!note]
> 「<ruby>入<rt>い</rt></ruby>れ<ruby>子<rt>こ</rt></ruby>」: <ruby>大<rt>おお</rt></ruby>きな<ruby>箱<rt>はこ</rt></ruby>の<ruby>中<rt>なか</rt></ruby>に<ruby>小<rt>ちい</rt></ruby>さな<ruby>箱<rt>はこ</rt></ruby>が<ruby>入<rt>はい</rt></ruby>っている、というように、あるものの<ruby>中<rt>なか</rt></ruby>に、よく<ruby>似<rt>に</rt></ruby>たあるものが<ruby>入<rt>はい</rt></ruby>っている<ruby>様子<rt>ようす</rt></ruby>を<ruby>指<rt>さ</rt></ruby>す<ruby>日本語<rt>にほんご</rt></ruby>です。

***

## 3. テキストに<ruby>意味<rt>いみ</rt></ruby>をつける：<ruby>見出<rt>みだ</rt></ruby>し、<ruby>段落<rt>だんらく</rt></ruby>、リスト

<ruby>文章<rt>ぶんしょう</rt></ruby>を <ruby>分<rt>わ</rt></ruby>かりやすくするために、<ruby>適切<rt>てきせつ</rt></ruby>な タグを <ruby>使<rt>つか</rt></ruby>います。

* <ruby>見出<rt>みだ</rt></ruby>し（`<h1>`〜`<h6>`）： <ruby>本<rt>ほん</rt></ruby>の「タイトル」や「<ruby>章<rt>しょう</rt></ruby>」の ように、<ruby>情報<rt>じょうほう</rt></ruby>の <ruby>優先順位<rt>ゆうせんじゅんい</rt></ruby>を <ruby>示<rt>しめ</rt></ruby>します。`<h1>`が  もっとも <ruby>重要<rt>じゅうよう</rt></ruby>な タイトルで、<ruby>数字<rt>すうじ</rt></ruby>が <ruby>大<rt>おお</rt></ruby>きくなるほど <ruby>小<rt>ちい</rt></ruby>さな <ruby>見出<rt>みだ</rt></ruby>しに なります。
* <ruby>段落<rt>だんらく</rt></ruby>（`<p>`）： ふつうの <ruby>文章<rt>ぶんしょう</rt></ruby>を まとめるための タグです。
* リスト（<ruby>箇条書<rt>かじょうが</rt></ruby>き）：
  * `<ul>`（<ruby>順序<rt>じゅんじょ</rt></ruby>なし リスト）： <ruby>買<rt>か</rt></ruby>い<ruby>物<rt>もの</rt></ruby>リストの ように、<ruby>順番<rt>じゅんばん</rt></ruby>が <ruby>関係<rt>かんけい</rt></ruby>ないときに <ruby>使<rt>つか</rt></ruby>います。
  * `<ol>`（<ruby>順序<rt>じゅんじょ</rt></ruby>あり リスト）： <ruby>料理<rt>りょうり</rt></ruby>の <ruby>手順<rt>てじゅん</rt></ruby>の ように、<ruby>順番<rt>じゅんばん</rt></ruby>が <ruby>大切<rt>たいせつ</rt></ruby>なときに <ruby>使<rt>つか</rt></ruby>います。
  * ※どちらも、<ruby>中身<rt>なかみ</rt></ruby>の <ruby>項目<rt>こうもく</rt></ruby>は `<li>` タグで <ruby>囲<rt>かこ</rt></ruby>みます。

HTMLコメント（`<!-- -->`）の メリット： コードの <ruby>中<rt>なか</rt></ruby>に `<!-- メモ -->` と <ruby>書<rt>か</rt></ruby>くと、ブラウザには <ruby>表示<rt>ひょうじ</rt></ruby>されません。これは「<ruby>自分<rt>じぶん</rt></ruby>や <ruby>仲間<rt>なかま</rt></ruby>」のための メモです。あとで <ruby>見直<rt>みなお</rt></ruby>したときに、<ruby>何<rt>なに</rt></ruby>をしたのか すぐに <ruby>分<rt>わ</rt></ruby>かるように なります。

***

## 4. <ruby>画像<rt>がぞう</rt></ruby>を <ruby>表示<rt>ひょうじ</rt></ruby>する：`<img>`<ruby>要素<rt>ようそ</rt></ruby>の<ruby>使<rt>つか</rt></ruby>い<ruby>方<rt>かた</rt></ruby>

<ruby>画像<rt>がぞう</rt></ruby>を <ruby>表示<rt>ひょうじ</rt></ruby>するには `<img>` <ruby>要素<rt>ようそ</rt></ruby>を <ruby>使<rt>つか</rt></ruby>います。

* src<ruby>属性<rt>ぞくせい</rt></ruby>： <ruby>画像<rt>がぞう</rt></ruby>が ある <ruby>場所<rt>ばしょ</rt></ruby>（パス）を <ruby>指定<rt>してい</rt></ruby>します。
* alt<ruby>属性<rt>ぞくせい</rt></ruby>： <ruby>画像<rt>がぞう</rt></ruby>の <ruby>説明<rt>せつめい</rt></ruby>を <ruby>文字<rt>もじ</rt></ruby>で <ruby>書<rt>か</rt></ruby>きます。
  * <ruby>重要性<rt>じゅうようせい</rt></ruby>： <ruby>目<rt>め</rt></ruby>が <ruby>不自由<rt>ふじゆう</rt></ruby>な <ruby>人<rt>ひと</rt></ruby>が <ruby>使<rt>つか</rt></ruby>う ソフトが この<ruby>文字<rt>もじ</rt></ruby>を <ruby>読<rt>よ</rt></ruby>み<ruby>上<rt>あ</rt></ruby>げます。また、<ruby>画像<rt>がぞう</rt></ruby>が エラーで <ruby>出<rt>で</rt></ruby>ないときにも <ruby>代<rt>か</rt></ruby>わりに <ruby>表示<rt>ひょうじ</rt></ruby>されます。
  * <ruby>良<rt>よ</rt></ruby>い <ruby>例<rt>れい</rt></ruby>： alt="Firefoxのロゴ：<ruby>地球<rt>ちきゅう</rt></ruby>を<ruby>包<rt>つつ</rt></ruby>む<ruby>燃<rt>も</rt></ruby>えるキツネ" の ように、<ruby>何<rt>なに</rt></ruby>が <ruby>書<rt>か</rt></ruby>いてあるか <ruby>具体的<rt>ぐたいてき</rt></ruby>に <ruby>書<rt>か</rt></ruby>くのが <ruby>正<rt>ただ</rt></ruby>しい <ruby>使<rt>つか</rt></ruby>い<ruby>方<rt>かた</rt></ruby>です。

<ruby>空要素<rt>からようそ</rt></ruby> / void element： `<img>` は <ruby>文章<rt>ぶんしょう</rt></ruby>を <ruby>囲<rt>かこ</rt></ruby>まないので、<ruby>終<rt>お</rt></ruby>わりの タグ（`</img>`）が いりません。これを「<ruby>空要素<rt>からようそ</rt></ruby>」と <ruby>呼<rt>よ</rt></ruby>びます。

ファイル<ruby>管理<rt>かんり</rt></ruby>のアドバイス： <ruby>画像<rt>がぞう</rt></ruby>は images/ という <ruby>名前<rt>なまえ</rt></ruby>の フォルダを <ruby>作<rt>つく</rt></ruby>って、その<ruby>中<rt>なか</rt></ruby>に <ruby>入<rt>い</rt></ruby>れましょう。HTMLからは `src="images/写真の名前.jpg"` の ように <ruby>指定<rt>してい</rt></ruby>します。こうすることで、たくさんの ファイルを きれいに <ruby>整<rt>せい</rt></ruby>りできます。

***

## 5. リンクを<ruby>作<rt>つく</rt></ruby>ってページをつなぐ：`<a>`<ruby>要素<rt>ようそ</rt></ruby>

ウェブ（<ruby>蜘蛛<rt>くも</rt></ruby>の<ruby>巣<rt>す</rt></ruby>：くものす）の <ruby>名前<rt>なまえ</rt></ruby>の とおり、ページどうしを つなぐのが「リンク」です。

リンクの<ruby>作<rt>つく</rt></ruby>り<ruby>方<rt>かた</rt></ruby>

1. リンクに したい テキストを <ruby>選<rt>えら</rt></ruby>びます。
2. その テキストを `<a>` タグで <ruby>囲<rt>かこ</rt></ruby>みます。
3. href <ruby>属性<rt>ぞくせい</rt></ruby>に、<ruby>行<rt>い</rt></ruby>きたい <ruby>先<rt>さき</rt></ruby>の アドレス（URL）を <ruby>書<rt>か</rt></ruby>きます。

```html
<a href="https://www.mozilla.org/">Mozillaのウェブサイト</a>
```

<ruby>大切<rt>たいせつ</rt></ruby>な <ruby>注意点<rt>ちゅういてん</rt></ruby>： アドレスを <ruby>書<rt>か</rt></ruby>くときは、<ruby>必<rt>かなら</rt></ruby>ず `https://` などの <ruby>通信<rt>つうしん</rt></ruby>の ルール（プロトコル） から <ruby>書<rt>か</rt></ruby>き<ruby>始<rt>はじ</rt></ruby>めてください。これがないと、リンクが <ruby>正<rt>ただ</rt></ruby>しく <ruby>動<rt>うご</rt></ruby>きません。また、リンクにする <ruby>言葉<rt>ことば</rt></ruby>は「ここを クリック」ではなく「Mozillaの ウェブサイト」の ように、どこに <ruby>行<rt>い</rt></ruby>くのか わかる <ruby>言葉<rt>ことば</rt></ruby>を <ruby>選<rt>えら</rt></ruby>びましょう。

***

## 6. まとめ：<ruby>自分<rt>じぶん</rt></ruby>のウェブサイトを<ruby>作<rt>つく</rt></ruby>ってみよう

「<ruby>構造<rt>こうぞう</rt></ruby>（HTML）」「テキスト」「<ruby>画像<rt>がぞう</rt></ruby>」「リンク」が <ruby>組<rt>く</rt></ruby>み<ruby>合<rt>あ</rt></ruby>わさることで、<ruby>一<rt>ひと</rt></ruby>つの ページが <ruby>完成<rt>かんせい</rt></ruby>します。

<ruby>初心者<rt>しょしんしゃ</rt></ruby>のための チェックリスト

<ruby>公開<rt>こうかい</rt></ruby>する <ruby>前<rt>まえ</rt></ruby>に、これを <ruby>確認<rt>かくにん</rt></ruby>しましょう：

* [ ] タグの <ruby>閉<rt>と</rt></ruby>じ<ruby>忘<rt>わす</rt></ruby>れは ありませんか？（`<img>`  <ruby>以外<rt>いがい</rt></ruby>、<ruby>終<rt>お</rt></ruby>わりのタグが <ruby>必要<rt>ひつよう</rt></ruby>です）
* [ ] ファイルの<ruby>名前<rt>なまえ</rt></ruby>は <ruby>正<rt>ただ</rt></ruby>しいですか？（<ruby>大文字<rt>おおもじ</rt></ruby>と <ruby>小文字<rt>こもじ</rt></ruby>の <ruby>間違<rt>まちが</rt></ruby>いは ありませんか？ Index.html と index.html は <ruby>違<rt>ちが</rt></ruby>います）
* [ ] <ruby>画像<rt>がぞう</rt></ruby>の パス（フォルダの<ruby>場所<rt>ばしょ</rt></ruby>）は <ruby>正<rt>ただ</rt></ruby>しいですか？（images/ フォルダの <ruby>中<rt>なか</rt></ruby>に <ruby>画像<rt>がぞう</rt></ruby>が ありますか？）
* [ ] リンクの https:// を <ruby>忘<rt>わす</rt></ruby>れていませんか？
* [ ] alt<ruby>属性<rt>ぞくせい</rt></ruby>は わかりやすく <ruby>書<rt>か</rt></ruby>きましたか？

<ruby>次<rt>つぎ</rt></ruby>のステップ： HTMLで <ruby>形<rt>かたち</rt></ruby>が できたら、<ruby>次<rt>つぎ</rt></ruby>は 「CSS」 を <ruby>学<rt>まな</rt></ruby>んで <ruby>色<rt>いろ</rt></ruby>や デザインを きれいに しましょう。さらに 「JavaScript」 を <ruby>使<rt>つか</rt></ruby>えば、<ruby>動<rt>うご</rt></ruby>きのある ページに なります。
