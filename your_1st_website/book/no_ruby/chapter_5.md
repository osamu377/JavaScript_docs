# V. ウェブサイトを動かすJavaScript

ウェブサイトを見たときに、ボタンを押して画面が変わったり、画像が動いたりすることはありませんか？  
それは「JavaScript」という言葉が働いているからです。

このガイドでは、プログラミングが初めての人や、日本語を勉強中の留学生にも分かりやすく、JavaScriptの基本を説明します。

***

## 1. はじめに：JavaScriptとは何か

ウェブサイトを作るとき、HTMLは「骨組み」を、CSSは「見た目」を作ります。そこに「動き」を加えるのがJavaScriptの役割です。

JavaScriptを使うと、ユーザーの操作に合わせてサイトの表示を変えることができます。  
ただ情報を読むだけのページから、ユーザーといっしょに動く「体験」へと変えることができる、とても大切な技術です。

**JavaScriptでできること**

JavaScriptを使って、以下のような動きを作ることができます：

* チェックする： フォームに入力されたデータが正しいか確認します。
* 動かす： ボタンをクリックしたときに、何かを実行します。
* 計算する： ゲームの点数や、数字の計算をおこないます。
* デザインを変える： スタイル（色や大きさ）を自由に変えます。
* アニメーション： 画像や文字をスムーズに動かします。

***

## 2. プログラミングの「基本の道具箱」

プログラムを作るとは、いくつかの道具を組み合わせて「命令」をつくることです。JavaScriptを動かす4つの大切な概念があります。

1. 変数 (Variables)： データを一時的に入れておく「入れ物」。
2. 関数 (Functions)： いくつかの命令をまとめた便利なセット。
3. 条件分岐 (Conditionals)： 「もし〜ならA、そうでなければB」。
4. イベント (Events)： 「クリックされた」などの動作のきっかけ。

***

## 3. 実践：ウェブサイトにJavaScriptを入れる

HTML、CSS、JavaScript の3つが連携してページが動きます。

**設定の手順**

1. scripts フォルダを作り、その中に main.js を作成します。
2. HTMLファイルの `<head>` の終わる直前に次を書きます：

```html
<script src="scripts/main.js"></script>
```

* CSSの `<link>` と同じ仕組みで、JavaScript を読み込みます。

**要素を選んで動かす**

```javascript
let myHeading = document.querySelector('h1');
myHeading.textContent = 'Hello world!';
```

* 1行目： `<h1>` を選び、myHeading に入れます。  
* 2行目： textContent を “Hello world!” に変えます。

ヒント： `//` で書いた行はコメントとして無視されます。

***

## 4. 応用：画像チェンジャーと条件分岐

クリックで画像が入れ替わる仕組みです。

**手順**

1. 画像を JavaScript で選ぶ  
2. クリックされるのを待つ  
3. 今の src を確認  
4. if 文で切り替える  

**実践コード**

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
* if...else： 条件で処理を切り替え

***

## 6. まとめと次のステップ

お疲れさまでした！これでJavaScriptの基礎を学びました。

* HTML/CSS： ページの土台と見た目  
* JavaScript： 動きを加える技術  

JavaScript は ゆっくり学べば確実に身につきます。  
MDNの教材（日本語 / 英語）もとても良い参考になります。

少しずつ練習して、ぜひあなたのオリジナルの動くウェブサイトを作ってください！