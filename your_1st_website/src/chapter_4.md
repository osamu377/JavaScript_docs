# IV. ウェブサイトをデザインするCSS

## 1. はじめに：CSSとは<ruby>何<rt>なん</rt></ruby>でしょうか？

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

## 2. CSSの<ruby>書<rt>か</rt></ruby>き<ruby>方<rt>かた</rt></ruby>（<ruby>構文<rt>こうぶん</rt></ruby>）を<ruby>覚<rt>おぼ</rt></ruby>えましょう

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

## 3. HTMLにCSSを<ruby>読<rt>よ</rt></ruby>み<ruby>込<rt>こ</rt></ruby>ませる<ruby>方法<rt>ほうほう</rt></ruby>

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

## 4. <ruby>文字<rt>もじ</rt></ruby>のデザインをきれいにする（フォントとテキスト）

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

## 5. すべては「<ruby>箱<rt>はこ</rt></ruby>（ボックス）」でできている

CSS の<ruby>世界<rt>せかい</rt></ruby>では、すべての<ruby>要素<rt>ようそ</rt></ruby>（<ruby>見出<rt>みだ</rt></ruby>し・<ruby>文章<rt>ぶんしょう</rt></ruby>・<ruby>画像<rt>がぞう</rt></ruby>など）は「<ruby>箱<rt>はこ</rt></ruby>」の<ruby>中<rt>なか</rt></ruby>にあると<ruby>考<rt>かんが</rt></ruby>えます。これを **ボックスモデル** と<ruby>呼<rt>よ</rt></ruby>びます。

|<ruby>要素<rt>ようそ</rt></ruby>|やさしい<ruby>説明<rt>せつめい</rt></ruby>|
|---|---|
|Content|<ruby>文<rt>もん</rt></ruby>字や<ruby>画<rt>が</rt></ruby>像が入る中心部|
|Padding|<ruby>中身<rt>なかみ</rt></ruby>と<ruby>枠線<rt>わくせん</rt></ruby>の<ruby>内側<rt>うちがわ</rt></ruby>の<ruby>余白<rt>よはく</rt></ruby>|
|Border|<ruby>枠線<rt>わくせん</rt></ruby>そのもの|
|Margin|<ruby>枠線<rt>わくせん</rt></ruby>の<ruby>外側<rt>そとがわ</rt></ruby>の<ruby>余白<rt>よはく</rt></ruby>|

***

## 6. <ruby>ページ<rt>ぺーじ</rt></ruby><ruby>全体<rt>ぜんたい</rt></ruby>のレイアウトを<ruby>整<rt>ととの</rt></ruby>える（<ruby>色<rt>いろ</rt></ruby>と<ruby>配置<rt>はいち</rt></ruby>）

<ruby>背景<rt>はいけい</rt></ruby>に<ruby>色<rt>いろ</rt></ruby>をつけ、body の<ruby>幅<rt>はば</rt></ruby>を600pxにし、<ruby>中<rt>なか</rt></ruby>央寄せする<ruby>典型<rt>てんけい</rt></ruby>的な<ruby>設定<rt>せってい</rt></ruby>です。

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

## 7. おわりに：<ruby>素敵<rt>すてき</rt></ruby>なウェブサイトを<ruby>作<rt>つく</rt></ruby>るために

CSS の<ruby>基礎<rt>きそ</rt></ruby>は、<ruby>将来<rt>しょうらい</rt></ruby>のアニメーションや高度レイアウトの<ruby>土台<rt>どだい</rt></ruby>になります。

1. <ruby>値<rt>あたい</rt></ruby>を変えて効果を確認  
2. 他サイトを<ruby>箱<rt>はこ</rt></ruby>として観察  
3. 1項目ずつ保存しながら確認

<ruby>楽<rt>たの</rt></ruby>しみながら、美しいサイトを完成させてください！