# V. ウェブサイトを<ruby>動<rt>うご</rt></ruby>かすJavaScript

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