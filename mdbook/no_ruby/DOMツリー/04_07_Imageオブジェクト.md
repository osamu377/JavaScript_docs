## VI. Imageオブジェクト

JavaScriptで<ruby>画像<rt>がぞう</rt></ruby>を扱う **Imageオブジェクト** は、<ruby>画面<rt>がめん</rt></ruby>に写真やイラストを<ruby>表示<rt>ひょうじ</rt></ruby>するための特別な道具です。

留学生の方には、Imageオブジェクトは**「デジタルの『写真立て』」**だと教えてあげてください。新しい写真（データ）を<ruby>読<rt>よ</rt></ruby>み<ruby>込<rt>こ</rt></ruby>んで、それをウェブサイトという「部屋」の好きな場所に飾ることができます。

***

### 1. Imageオブジェクトとは？

HTMLの `<img>` タグと同じ役割をしますが、JavaScriptの中で **「まだ<ruby>画面<rt>がめん</rt></ruby>にない<ruby>画像<rt>がぞう</rt></ruby>」をあらかじめ準備する** のにとても便利です。

作り方は2通りあります：

1. **HTMLから持ってくる：** `document.getElementById("myImg")`
2. **新しく作る：** `new Image()`

***

### 2. よく使うプロパティ（写真の状態）

写真がどんな大きさか、どこにあるかを知るための情報です。

* **`src`**（ソース）
<ruby>画像<rt>がぞう</rt></ruby>の「ファイルの場所（URL）」です。ここを<ruby>書<rt>か</rt></ruby>き<ruby>換<rt>かえ</rt></ruby>えると、別の<ruby>画像<rt>がぞう</rt></ruby>に<ruby>切<rt>きり</rt></ruby>り<ruby>替<rt>か</rt></ruby>わります。
* **`width` / `height**`
<ruby>画像<rt>がぞう</rt></ruby>の「横幅（よこはば）」と「高さ」です。
* **`complete`**
<ruby>画像<rt>がぞう</rt></ruby>の<ruby>読<rt>よ</rt></ruby>み<ruby>込<rt>こ</rt></ruby>みが終わったかどうかを `true` / `false` で教えてくれます。
* **`alt`**（オルト）
<ruby>画像<rt>がぞう</rt></ruby>が<ruby>表示<rt>ひょうじ</rt></ruby>できなかったときに出る「説明文」です。

***

### 3. よく使うイベント（メソッド的な役割）

Imageオブジェクトでは、メソッドよりも **「状態が変わったときのイベント」** をよく使います。

* **`onload`**
<ruby>画像<rt>がぞう</rt></ruby>の<ruby>読<rt>よ</rt></ruby>み<ruby>込<rt>こ</rt></ruby>みが **「成功（せいこう）」** して、<ruby>表示<rt>ひょうじ</rt></ruby>できるようになったときに<ruby>動<rt>うご</rt></ruby>きます。
* **`onerror`**
<ruby>画像<rt>がぞう</rt></ruby>のファイルが見つからないなど、<ruby>読<rt>よ</rt></ruby>み<ruby>込<rt>こ</rt></ruby>みに **「失敗（しっぱい）」** したときに<ruby>動<rt>うご</rt></ruby>きます。

***

### 4. 実際に動かしてみよう！

留学生に「JavaScriptで新しく<ruby>画像<rt>がぞう</rt></ruby>を作って<ruby>表示<rt>ひょうじ</rt></ruby>する」流れを説明するコード<ruby>例<rt>れい</rt></ruby>です。

```javascript
// 1. 新しい「写真立て（Imageオブジェクト）」を作る
const myPic = new Image();

// 2. 読（よ）み込（こ）みが終わったあとの「お祝い」を決める
myPic.onload = function() {
  console.log("画像（がぞう）の準備ができました！サイズは " + myPic.width + "px です。");
  // 画面（がめん）に表示（ひょうじ）する（bodyに追加）
  document.body.appendChild(myPic);
};

// 3. 失敗したとき（エラー）の準備
myPic.onerror = function() {
  console.log("画像（がぞう）が見つかりませんでした...");
};

// 4. 最後に「写真（データ）」を入れる（読（よ）み込（こ）みスタート！）
myPic.src = "https://example.com/japan.jpg";

```

***

### 5. 留学生へのアドバイス：プリロード（<ruby>先読<rt>さきよ</rt></ruby>み）

「どうしてHTMLに書かずにJavaScriptで作るの？」と聞かれたら、こう答えてあげてください。

> **「ゲームや重いサイトでは、<ruby>画像<rt>がぞう</rt></ruby>が出るまで時間がかかるよね。JavaScriptで先に<ruby>読<rt>よ</rt></ruby>み<ruby>込<rt>こ</rt></ruby>んでおけば（プリロード）、ユーザーがボタンを押した瞬間にパッと<ruby>画像<rt>がぞう</rt></ruby>を出せるから、親切なんだよ！」**

***

### まとめテーブル

| プロパティ・イベント | 役割 | <ruby>例<rt>たと</rt></ruby>え話 |
| --- | --- | --- |
| **`src`** | <ruby>画像<rt>がぞう</rt></ruby>の住所 | どの写真を入れるか決める |
| **`width` / `height**` | <ruby>画像<rt>がぞう</rt></ruby>のサイズ | 写真の大きさ |
| **`onload`** | <ruby>読<rt>よ</rt></ruby>み<ruby>込<rt>こ</rt></ruby>み完了 | 「写真の表示が完了した<ruby>現像<rt>げんぞう</rt></ruby>が終わったよ！」 |
| **`onerror`** | <ruby>読<rt>よ</rt></ruby>み<ruby>込<rt>こ</rt></ruby>みエラー | 「写真をなくしちゃった！」 |

***

いかがでしょうか？Imageオブジェクトをマスターすると、スライドショーやキャラクターが動くゲームなどが作れるようになります。

