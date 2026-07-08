# Windowオブジェクト

さて、オブジェクトがどんなものか、を<ruby>理解<rt>りかい</rt></ruby>したら、<ruby>次<rt>つぎ</rt></ruby>はブラウザのオブジェクトをもっとくわしく<ruby>見<rt>み</rt></ruby>てみましょう。こうしたオブジェクトはあらかじめ、JavaScriptに<ruby>組<rt>く</rt></ruby>み<ruby>込<rt>こ</rt></ruby>まれているので、そのプロパティもメソッドも、いきなり<ruby>呼<rt>よ</rt></ruby>び<ruby>出<rt>だ</rt></ruby>して<ruby>使<rt>つか</rt></ruby>うことができます。

ブラウザで<ruby>動<rt>うご</rt></ruby>くJavaScriptを<ruby>学習<rt>がくしゅう</rt></ruby>するとき、<ruby>一番大<rt>いちばんおお</rt></ruby>きな<ruby>存在<rt>そんざい</rt></ruby>が **Windowオブジェクト** です。

<ruby>学生<rt>がくせい</rt></ruby>の<ruby>方<rt>かた</rt></ruby>には、Windowオブジェクトは **「ブラウザの<ruby>画面全体<rt>がめんぜんたい</rt></ruby>を<ruby>管理<rt>かんり</rt></ruby>している『<ruby>社長<rt>しゃちょう</rt></ruby>さん』」** だと<ruby>教<rt>おし</rt></ruby>えてあげてください。JavaScriptでできることのほとんどは、この<ruby>社長<rt>しゃちょう</rt></ruby>さんにお<ruby>願<rt>ねが</rt></ruby>いして<ruby>動<rt>うご</rt></ruby>かしています。

***

## 1. Windowオブジェクトとは？

ブラウザの「タブ」ひとつひとつが、ひとつの `window` です。  
JavaScriptを<ruby>実行<rt>じっこう</rt></ruby>するとき、**<ruby>最初<rt>さいしょ</rt></ruby>からそこにいる「グローバルオブジェクト」**（<ruby>一番<rt>いちばん</rt></ruby>えらいオブジェクト）です。

<ruby>実<rt>じつ</rt></ruby>は、<ruby>私<rt>わたし</rt></ruby>たちが<ruby>普段使<rt>ふだんつか</rt></ruby>っている `console.log()` や `alert()` も、<ruby>本当<rt>ほんとう</rt></ruby>は `window.console.log()` や `window.alert()` という<ruby>名前<rt>なまえ</rt></ruby>です。でも、<ruby>社長<rt>しゃちょう</rt></ruby>さんは<ruby>有名<rt>ゆうめい</rt></ruby>すぎるので、**`window.` を<ruby>省略<rt>しょうりゃく</rt></ruby>して<ruby>書<rt>か</rt></ruby>くことができます。**

***

## 2. よく<ruby>使<rt>つか</rt></ruby>うプロパティ（<ruby>画面<rt>がめん</rt></ruby>の<ruby>情報<rt>じょうほう</rt></ruby>）

<ruby>社長<rt>しゃちょう</rt></ruby>さんが<ruby>持<rt>も</rt></ruby>っている「<ruby>今<rt>いま</rt></ruby>のブラウザの<ruby>状態<rt>じょうたい</rt></ruby>」についての<ruby>情報<rt>じょうほう</rt></ruby>です。

### **`window.document`**

<ruby>今見<rt>いまみ</rt></ruby>ている「ウェブサイトの<ruby>中身<rt>なかみ</rt></ruby>（ページ）」そのものです。<ruby>文字<rt>もじ</rt></ruby>の<ruby>色<rt>いろ</rt></ruby>を<ruby>変<rt>か</rt></ruby>えたり、ボタンを<ruby>作<rt>つく</rt></ruby>ったりするときに<ruby>使<rt>つか</rt></ruby>います。

### **`window.location`**

<ruby>今<rt>いま</rt></ruby>の「URL（Web<ruby>上<rt>じょう</rt></ruby>の<ruby>住所<rt>じゅうしょ</rt></ruby>）」の<ruby>情報<rt>じょうほう</rt></ruby>です。

* **<ruby>例<rt>れい</rt></ruby>：** `location.href = "https://google.com";` と<ruby>書<rt>か</rt></ruby>くと、<ruby>別<rt>べつ</rt></ruby>のサイトに<ruby>移動<rt>いどう</rt></ruby>できます。

### **`window.innerWidth` / `innerHeight`**

ブラウザの「<ruby>中身<rt>なかみ</rt></ruby>の<ruby>横幅<rt>よこはば</rt></ruby>と<ruby>高<rt>たか</rt></ruby>さ」です。

* **イメージ：** <ruby>画面<rt>がめん</rt></ruby>の<ruby>大<rt>おお</rt></ruby>きさに<ruby>合<rt>あ</rt></ruby>わせてデザインを<ruby>変<rt>か</rt></ruby>えたいときにチェックします。たとえば「パソコンでは、<ruby>画面<rt>がめん</rt></ruby>の<ruby>横幅<rt>よこはば</rt></ruby>がスマートフォンより<ruby>広<rt>ひろ</rt></ruby>いので、それに<ruby>合<rt>あ</rt></ruby>わせ<ruby>横<rt>よこ</rt></ruby>にメニューなどを<ruby>表示<rt>ひょうじ</rt></ruby>する」というようなことをしたいときに、<ruby>使<rt>つか</rt></ruby>います。

***

## 3. よく<ruby>使<rt>つか</rt></ruby>うメソッド（<ruby>社長<rt>しゃちょう</rt></ruby>さんができること）

### **`alert()` / `prompt()` / `confirm()`**

ユーザーにメッセージを<ruby>出<rt>だ</rt></ruby>したり、<ruby>質問<rt>しつもん</rt></ruby>をしたりする「<ruby>小<rt>ちい</rt></ruby>さな<ruby>窓<rt>まど</rt></ruby>（ダイアログ）」を<ruby>出<rt>だ</rt></ruby>します。

```javascript
alert("こんにちは！"); // メッセージを出す
let name = prompt("お名前は？"); // 名前を入力（にゅうりょく）してもらう
```

### **`setTimeout()` / `setInterval()`**

「タイマー」の<ruby>仕事<rt>しごと</rt></ruby>です。

* **`setTimeout`：** ○<ruby>秒後<rt>びょうご</rt></ruby>に1<ruby>回<rt>かい</rt></ruby>だけ<ruby>実行<rt>じっこう</rt></ruby>する。
* **`setInterval`：** ○<ruby>秒<rt>びょう</rt></ruby>ごとに、ずっと<ruby>繰<rt>く</rt></ruby>り<ruby>返<rt>かえ</rt></ruby>す。

### **`open()` / `close()`**

<ruby>新<rt>あたら</rt></ruby>しいタブを<ruby>開<rt>ひら</rt></ruby>いたり、<ruby>今<rt>いま</rt></ruby>あるタブを<ruby>閉<rt>と</rt></ruby>じたりします。

***

## 4. <ruby>学生<rt>がくせい</rt></ruby>への<ruby>説明<rt>せつめい</rt></ruby>ポイント：`window` と `document` の<ruby>違<rt>ちが</rt></ruby>い

ここが<ruby>一番<rt>いちばん</rt></ruby><ruby>混乱<rt>こんらん</rt></ruby>しやすいポイントです！

> **「Window」は「ブラウザの<ruby>枠全体<rt>わくぜんたい</rt></ruby>」。**  
> **「Document」は「その<ruby>中<rt>なか</rt></ruby>にある<ruby>紙<rt>かみ</rt></ruby>（ページ）」のこと。**

<ruby>社長<rt>しゃちょう</rt></ruby>（window）は、<ruby>秘書<rt>ひしょ</rt></ruby>のドキュメントくん（document）に『このページを<ruby>書<rt>か</rt></ruby>き<ruby>換<rt>か</rt></ruby>えて！』と<ruby>命令<rt>めいれい</rt></ruby>しているんです。

***

## まとめテーブル

| <ruby>種類<rt>しゅるい</rt></ruby> | <ruby>名前<rt>なまえ</rt></ruby> | やっていること                                                                                                            |
| ---------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **プロパティ**                    | **`document`**              | ページの<ruby>内容<rt>ないよう</rt></ruby>をいじる                                                                               |
| **プロパティ**                    | **`location`**              | <ruby>住所<rt>じゅうしょ</rt></ruby>（URL）を<ruby>確認<rt>かくにん</rt></ruby>・<ruby>移動<rt>いどう</rt></ruby>する                      |
| **メソッド**                     | **`alert()`**               | お<ruby>知<rt>し</rt></ruby>らせを<ruby>表示<rt>ひょうじ</rt></ruby>する                                                         |
| **メソッド**                     | **`setTimeout()`**          | タイマーをセットする                                                                                                         |
| **メソッド**                     | **`scrollTo()`**            | <ruby>画面<rt>がめん</rt></ruby>を<ruby>上<rt>うえ</rt></ruby>や<ruby>下<rt>した</rt></ruby>に<ruby>動<rt>うご</rt></ruby>かす（スクロール） |

***

いかがでしょうか？ **「ブラウザのボス」** というイメージが<ruby>伝<rt>つた</rt></ruby>われば、Windowオブジェクトの<ruby>理解<rt>りかい</rt></ruby>はバッチリです！

### プロパティとメソッド

##### 🌐 <ruby>別<rt>べつ</rt></ruby>のオブジェクト（<ruby>子分<rt>こぶん</rt></ruby>たち）

* **`document`**（ドキュメント）：

* **<ruby>意味<rt>いみ</rt></ruby>：** <ruby>今<rt>いま</rt></ruby><ruby>画面<rt>がめん</rt></ruby>に<ruby>見<rt>み</rt></ruby>えている「Webページの<ruby>白<rt>しろ</rt></ruby>い<ruby>紙<rt>かみ</rt></ruby>（HTMLの<ruby>中身<rt>なかみ</rt></ruby>）」を<ruby>捕<rt>つか</rt></ruby>まえるとき（`document.getElementById`）にいつも<ruby>使<rt>つか</rt></ruby>う<ruby>超重要<rt>ちょうじゅうよう</rt></ruby>プロパティです。

* **`history`**（ヒストリー）：

* **<ruby>意味<rt>いみ</rt></ruby>：** ブラウザの「<ruby>戻<rt>もど</rt></ruby>る」「<ruby>進<rt>すす</rt></ruby>む」の<ruby>履歴<rt>りれき</rt></ruby>（<ruby>歴史<rt>れきし</rt></ruby>）を<ruby>管理<rt>かんり</rt></ruby>するオブジェクトです。

* **`location`**（ロケーション）：

* **<ruby>意味<rt>いみ</rt></ruby>：** <ruby>今見<rt>いまみ</rt></ruby>ているWebページの「URL（<ruby>住所<rt>じゅうしょ</rt></ruby>）」の<ruby>情報<rt>じょうほう</rt></ruby>です。ここに<ruby>新<rt>あたら</rt></ruby>しいURLを<ruby>代入<rt>だいにゅう</rt></ruby>すると、<ruby>別<rt>べつ</rt></ruby>のページに<ruby>画面<rt>がめん</rt></ruby>が<ruby>変<rt>か</rt></ruby>わります。

##### 🪟 <ruby>画面<rt>がめん</rt></ruby>の<ruby>大<rt>おお</rt></ruby>きさ（サイズ）

* **`innerWidth` / `innerHeight`**（インナー・ウィズ / ハイト）：

* **<ruby>意味<rt>いみ</rt></ruby>：** Webページが<ruby>実際<rt>じっさい</rt></ruby>に<ruby>見<rt>み</rt></ruby>えている「<ruby>内側<rt>うちがわ</rt></ruby>の<ruby>白<rt>しろ</rt></ruby>い<ruby>部分<rt>ぶぶん</rt></ruby>の<ruby>幅<rt>はば</rt></ruby>と<ruby>高<rt>たか</rt></ruby>さ」（ピクセル<ruby>単位<rt>たんい</rt></ruby>）です。スクロールバーは<ruby>含<rt>ふく</rt></ruby>みません。

* **`outerWidth` / `outerHeight`**（アウター・ウィズ / ハイト）：

* **<ruby>意味<rt>いみ</rt></ruby>：** ブラウザの<ruby>枠<rt>わく</rt></ruby>やメニューバーなども<ruby>全部合<rt>ぜんぶあ</rt></ruby>わせた「<ruby>一番外側<rt>いちばんそとがわ</rt></ruby>のウィンドウ<ruby>全体<rt>ぜんたい</rt></ruby>の<ruby>幅<rt>はば</rt></ruby>と<ruby>高<rt>たか</rt></ruby>さ」です。

> [!note]
> ユーザーの<ruby>画面<rt>がめん</rt></ruby>サイズに<ruby>合<rt>あ</rt></ruby>わせて<ruby>動<rt>うご</rt></ruby>き（レスポンシブ）を<ruby>変<rt>か</rt></ruby>えたいときは、<ruby>内側<rt>うちがわ</rt></ruby>のサイズである `innerWidth` をよく<ruby>使<rt>つか</rt></ruby>います。また、<ruby>一覧<rt>いちらん</rt></ruby>の `outeWridth` や `innerheight` は<ruby>大文字小文字<rt>おおもじこもじ</rt></ruby>のタイポ（<ruby>打<rt>う</rt></ruby>ち<ruby>間違<rt>まちが</rt></ruby>い）になりやすいので、**`innerWidth` / `innerHeight` / `outerWidth` / `outerHeight`** と<ruby>正<rt>ただ</rt></ruby>しく<ruby>教<rt>おし</rt></ruby>えてあげてください。

##### 🆕 <ruby>新<rt>あたら</rt></ruby>しいウィンドウ・タブの<ruby>状態<rt>じょうたい</rt></ruby>

* **`closed`**（クローズド）：

* **<ruby>意味<rt>いみ</rt></ruby>：** そのウィンドウが「すでに<ruby>閉<rt>と</rt></ruby>じられているか・いないか」を `true` / `false` で<ruby>教<rt>おし</rt></ruby>えてくれます。

* **`opener`**（オープナー）：

* **<ruby>意味<rt>いみ</rt></ruby>：** <ruby>自分<rt>じぶん</rt></ruby>のウィンドウを<ruby>新<rt>あたら</rt></ruby>しく<ruby>開<rt>ひら</rt></ruby>いてくれた「<ruby>親<rt>おや</rt></ruby>のウィンドウ」を<ruby>指<rt>さ</rt></ruby>します。

* **`name`**（ネーム）：

* **<ruby>意味<rt>いみ</rt></ruby>：** ウィンドウにつけられた「<ruby>名前<rt>なまえ</rt></ruby>」です。リンクを<ruby>別<rt>べつ</rt></ruby>のウィンドウで<ruby>開<rt>ひら</rt></ruby>くターゲット（`target="名前"`）に<ruby>使<rt>つか</rt></ruby>います。

##### 💬 ブラウザの<ruby>下<rt>した</rt></ruby>のバー（<ruby>現在<rt>げんざい</rt></ruby>はあまり<ruby>使<rt>つか</rt></ruby>われません）

* **`status` / `defaultStatus`**（ステータス / デフォルト・ステータス）：
* **<ruby>意味<rt>いみ</rt></ruby>：** ブラウザの<ruby>一番下<rt>いちばんした</rt></ruby>に<ruby>昔<rt>むかし</rt></ruby>あった「ステータスバー」という<ruby>場所<rt>ばしょ</rt></ruby>に<ruby>文字<rt>もじ</rt></ruby>を<ruby>表示<rt>ひょうじ</rt></ruby>するための<ruby>設定<rt>せってい</rt></ruby>です。（※<ruby>現在<rt>げんざい</rt></ruby>のモダンなブラウザでは、セキュリティの<ruby>理由<rt>りゆう</rt></ruby>でほとんど<ruby>動<rt>うご</rt></ruby>きません）

***

#### 2. windowオブジェクトのメソッド（<ruby>命令<rt>めいれい</rt></ruby>）

##### 🖥️ ウィンドウを<ruby>動<rt>うご</rt></ruby>かす・<ruby>開<rt>ひら</rt></ruby>く

* **`open()` / `close()`**：

* **<ruby>意味<rt>いみ</rt></ruby>：** <ruby>新<rt>あたら</rt></ruby>しいウィンドウ（またはタブ）を\*\*<ruby>開<rt>ひら</rt></ruby>く\*\*<ruby>命令<rt>めいれい</rt></ruby>と、<ruby>今<rt>いま</rt></ruby>あるウィンドウを\*\*<ruby>閉<rt>と</rt></ruby>じる\*\*<ruby>命令<rt>めいれい</rt></ruby>です。

* **`moveTo(x, y)` / `moveBy(x, y)`**：

* **<ruby>意味<rt>いみ</rt></ruby>：** ウィンドウの<ruby>画面上<rt>がめんじょう</rt></ruby>の<ruby>位置<rt>いち</rt></ruby>を<ruby>動<rt>うご</rt></ruby>かす<ruby>命令<rt>めいれい</rt></ruby>です。`moveTo` は<ruby>指定<rt>してい</rt></ruby>した<ruby>座標<rt>ざひょう</rt></ruby>（<ruby>絶対位置<rt>ぜったいいち</rt></ruby>）へジャンプし、`moveBy` は<ruby>今<rt>いま</rt></ruby>の<ruby>場所<rt>ばしょ</rt></ruby>から<ruby>指定<rt>してい</rt></ruby>した<ruby>数<rt>かず</rt></ruby>だけ（<ruby>相対位置<rt>そうたいいち</rt></ruby>）<ruby>動<rt>うご</rt></ruby>きます。

* **`resizeTo(w, h)` / `resizeBy(w, h)`**：

* **<ruby>意味<rt>いみ</rt></ruby>：** ウィンドウの<ruby>大<rt>おお</rt></ruby>きさを<ruby>変<rt>か</rt></ruby>える<ruby>命令<rt>めいれい</rt></ruby>です。`resizeTo` は<ruby>指定<rt>してい</rt></ruby>した<ruby>幅<rt>はば</rt></ruby>と<ruby>高<rt>たか</rt></ruby>さに<ruby>変更<rt>へんこう</rt></ruby>し、`resizeBy` は<ruby>今<rt>いま</rt></ruby>の<ruby>大<rt>おお</rt></ruby>きさからプラスマイナスします。

> [!note]
> これらの<ruby>画面自体<rt>がめんじたい</rt></ruby>を<ruby>動<rt>うご</rt></ruby>かしたりサイズを<ruby>変<rt>か</rt></ruby>えたりするメソッドは、ユーザーをびっくりさせないよう、<ruby>現在<rt>げんざい</rt></ruby>の<ruby>一般的<rt>いっぱんてき</rt></ruby>なブラウザではセキュリティガードがかかり、<ruby>動<rt>うご</rt></ruby>かない<ruby>設定<rt>せってい</rt></ruby>になっていることが<ruby>多<rt>おお</rt></ruby>いです。

* **`focus()` / `blur()`**：
* **<ruby>意味<rt>いみ</rt></ruby>：** そのウィンドウを<ruby>一番前<rt>いちばんまえ</rt></ruby>に<ruby>持<rt>も</rt></ruby>ってきてパソコンの<ruby>主役<rt>しゅやく</rt></ruby>にする（フォーカスを<ruby>当<rt>あ</rt></ruby>てる）<ruby>命令<rt>めいれい</rt></ruby>と、<ruby>逆<rt>ぎゃく</rt></ruby>に<ruby>主役<rt>しゅやく</rt></ruby>から<ruby>外<rt>はず</rt></ruby>す（フォーカスを<ruby>外<rt>はず</rt></ruby>す）<ruby>命令<rt>めいれい</rt></ruby>です。

##### 🚨 ユーザーへのメッセージ（ダイアログ）

* **`alert("メッセージ")`**：

* **<ruby>意味<rt>いみ</rt></ruby>：** <ruby>画面<rt>がめん</rt></ruby>に「OK」ボタンだけの<ruby>警告<rt>けいこく</rt></ruby>メッセージを<ruby>出<rt>だ</rt></ruby>す、<ruby>一番<rt>いちばん</rt></ruby>おなじみの<ruby>命令<rt>めいれい</rt></ruby>です。

* **`confirm("いいですか？")`**：

* **<ruby>意味<rt>いみ</rt></ruby>：** 「OK」と「キャンセル」の2つのボタンを<ruby>出<rt>だ</rt></ruby>す<ruby>命令<rt>めいれい</rt></ruby>です。ユーザーが「OK」を<ruby>押<rt>お</rt></ruby>すと `true`、「キャンセル」を<ruby>押<rt>お</rt></ruby>すと `false` が<ruby>戻<rt>もど</rt></ruby>り<ruby>値<rt>ち</rt></ruby>として<ruby>返<rt>かえ</rt></ruby>ってきます。

* **`prompt("名前は？")`**：

* **<ruby>意味<rt>いみ</rt></ruby>：** <ruby>文字<rt>もじ</rt></ruby>を<ruby>入力<rt>にゅうりょく</rt></ruby>できるボックスを<ruby>出<rt>だ</rt></ruby>す<ruby>命令<rt>めいれい</rt></ruby>です。<ruby>入力<rt>にゅうりょく</rt></ruby>された<ruby>文字<rt>もじ</rt></ruby>が<ruby>戻<rt>もど</rt></ruby>り<ruby>値<rt>ち</rt></ruby>になります。

##### ⏱️ タイマー（<ruby>時間<rt>じかん</rt></ruby>をコントロールする）

<ruby>留学生<rt>りゅうがくせい</rt></ruby>のゲーム<ruby>作<rt>づく</rt></ruby>りやWebサイトの<ruby>動<rt>うご</rt></ruby>き（アニメーション）で<ruby>大活躍<rt>だいかつやく</rt></ruby>するツートップです！

* **`setTimeout(関数, ミリ秒)` / `clearTimeout(タイマーID)`**：

* **<ruby>意味<rt>いみ</rt></ruby>：** 「<ruby>指定<rt>してい</rt></ruby>した<ruby>秒数<rt>びょうすう</rt></ruby>が<ruby>経<rt>た</rt></ruby>ったあとに、1<ruby>回<rt>かい</rt></ruby>だけ<ruby>関数<rt>かんすう</rt></ruby>を<ruby>実行<rt>じっこう</rt></ruby>する」<ruby>命令<rt>めいれい</rt></ruby>です（※1000ミリ<ruby>秒<rt>びょう</rt></ruby> ＝ 1<ruby>秒<rt>びょう</rt></ruby>）。<ruby>途中<rt>とちゅう</rt></ruby>でストップしたいときは `clearTimeout` を<ruby>使<rt>つか</rt></ruby>います。

* **`setInterval(関数, ミリ秒)` / `clearInterval(タイマーID)`**：

* **<ruby>意味<rt>いみ</rt></ruby>：** 「<ruby>指定<rt>してい</rt></ruby>した<ruby>秒数<rt>びょうすう</rt></ruby>ごとに、ずーっと<ruby>何回<rt>なんかい</rt></ruby>も<ruby>関数<rt>かんすう</rt></ruby>を<ruby>繰<rt>く</rt></ruby>り<ruby>返<rt>かえ</rt></ruby>す」<ruby>命令<rt>めいれい</rt></ruby>です。<ruby>時計<rt>とけい</rt></ruby>やアクションゲームの<ruby>動<rt>うご</rt></ruby>きに<ruby>使<rt>つか</rt></ruby>います。<ruby>止<rt>と</rt></ruby>めるときは<ruby>必<rt>かなら</rt></ruby>ず `clearInterval` で<ruby>消<rt>け</rt></ruby>す<ruby>必要<rt>ひつよう</rt></ruby>があります。

***

#### 3. <ruby>留学生向<rt>りゅうがくせいむ</rt></ruby>けのまとめ

> **JavaScriptの<ruby>大<rt>だい</rt></ruby>ボス `window`**  
> `window` オブジェクトは、ブラウザの<ruby>画面全体<rt>がめんぜんたい</rt></ruby>を<ruby>支配<rt>しはい</rt></ruby>している「<ruby>一番大<rt>いちばんおお</rt></ruby>きなお<ruby>父<rt>とう</rt></ruby>さん」のようなオブジェクトです。  
> <ruby>実<rt>じつ</rt></ruby>は、いつも<ruby>使<rt>つか</rt></ruby>っている `alert()` も、<ruby>正<rt>ただ</rt></ruby>しくは **`window.alert()`** と<ruby>書<rt>か</rt></ruby>きます。でも、<ruby>一番大<rt>いちばんおお</rt></ruby>ボスの<ruby>命令<rt>めいれい</rt></ruby>はいちいち `window.` と<ruby>書<rt>か</rt></ruby>かなくても、<ruby>省略<rt>しょうりゃく</rt></ruby>して `alert()` だけで<ruby>使<rt>つか</rt></ruby>っていいルールになっています。  
> \* **<ruby>中身<rt>なかみ</rt></ruby>を<ruby>知<rt>し</rt></ruby>る（プロパティ）**： `document`（ページの<ruby>中身<rt>なかみ</rt></ruby>）や `innerWidth`（<ruby>画面<rt>がめん</rt></ruby>の<ruby>幅<rt>はば</rt></ruby>）など、<ruby>今<rt>いま</rt></ruby>のブラウザの<ruby>状態<rt>じょうたい</rt></ruby>を<ruby>教<rt>おし</rt></ruby>えてくれます。  
> \* **タイマーを<ruby>動<rt>うご</rt></ruby>かす（メソッド）**： **`setTimeout`**（◯<ruby>秒後<rt>びょうご</rt></ruby>に1<ruby>回動<rt>かいうご</rt></ruby>かす）や **`setInterval`**（◯<ruby>秒<rt>びょう</rt></ruby>ごとに<ruby>繰<rt>く</rt></ruby>り<ruby>返<rt>かえ</rt></ruby>し<ruby>動<rt>うご</rt></ruby>かす）は、Webサイトに<ruby>楽<rt>たの</rt></ruby>しい<ruby>動<rt>うご</rt></ruby>きやゲームを<ruby>作<rt>つく</rt></ruby>るために<ruby>絶対<rt>ぜったい</rt></ruby>に<ruby>必要<rt>ひつよう</rt></ruby>な<ruby>命令<rt>めいれい</rt></ruby>なので、<ruby>使<rt>つか</rt></ruby>い<ruby>方<rt>かた</rt></ruby>をしっかり<ruby>覚<rt>おぼ</rt></ruby>えましょう！  
>

***

いかがでしょうか。<ruby>数<rt>かず</rt></ruby>が<ruby>多<rt>おお</rt></ruby>くて<ruby>圧倒<rt>あっとう</rt></ruby>されがちですが、<ruby>実務<rt>じつむ</rt></ruby>や<ruby>課題<rt>かだい</rt></ruby>で<ruby>今<rt>いま</rt></ruby>でも<ruby>主役<rt>しゅやく</rt></ruby>としてよく<ruby>使<rt>つか</rt></ruby>うのは、「<ruby>子分<rt>こぶん</rt></ruby>オブジェクト（`document`, `location`）」、「ダイアログ（`alert`, `confirm`）」、「タイマー（`setTimeout`, `setInterval`）」の3<ruby>大<rt>だい</rt></ruby>グループです。

***
