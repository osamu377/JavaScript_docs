## IV. Styleオブジェクト

**Styleオブジェクト**は、JavaScriptを使ってウェブサイトの<ruby>見<rt>み</rt></ruby>た<ruby>目<rt>め</rt></ruby>（CSS）を自由に変えるための道具です。

留学生の方には、Styleオブジェクトは**「パーツに新しい服を着せたり、メイクをしたりする『スタイリストさん』」**だと教えてあげてください。

***

### 1. Styleオブジェクトとは？

HTMLの各要素（Element）が持っているオブジェクトです。これを使うと、ボタンの色を赤くしたり、文字を大きくしたり、アニメーションのように動かしたりできます。

基本の<ruby>書<rt>か</rt></ruby>き<ruby>方<rt>かた</rt></ruby>はこうです：
`要素.style.プロパティ = "値";`

***

### 2. よく使うプロパティ（<ruby>見<rt>み</rt></ruby>た<ruby>目<rt>め</rt></ruby>の変更）

CSSのプロパティ名とほぼ同じですが、**1つだけ大きなルール**があります。

#### **「キャメルケース」で書く！**

CSSでハイフン（`-`）を使う名前は、JavaScriptではハイフンを消して、次の文字を**大文字**にします。

* `background-color` → **`backgroundColor`**
* `font-size` → **`fontSize`**
* `margin-top` → **`marginTop`**

| よく使うプロパティ | 役割 |
| --- | --- |
| **`color`** | 文字の色を変える |
| **`backgroundColor`** | <ruby>背景<rt>はいけい</rt></ruby>（はいけい）の色を変える |
| **`display`** | パーツを<ruby>表示<rt>ひょうじ</rt></ruby>するか消す（`none`）か決める |
| **`width` / `height**` | 幅と高さを変える（**"100px"** のように単位が必要！） |
| **`borderRadius`** | 角を丸くする |

***

### 3. よく使うメソッド（より高度な操作）

`style.color = "red"` のような直接の変更以外に、便利な命令（メソッド）もあります。

#### **`setProperty("プロパティ名", "値")`**

CSSのプロパティをセットします。これを使うときは、CSSと同じ形（`background-color`）で書けます。

* `element.style.setProperty("background-color", "blue");`

#### **`removeProperty("プロパティ名")`**

JavaScriptで<ruby>設定<rt>せってい</rt></ruby>したスタイルを消して、元のCSSの状態に戻します。

#### **`getPropertyValue("プロパティ名")`**

<ruby>設定<rt>せってい</rt></ruby>されているスタイルの値を<ruby>取得<rt>しゅとく</rt></ruby>します。

***

### 4. 実際に動かしてみよう！

留学生に「マウスが乗ったら色が変わるボタン」の<ruby>仕組<rt>しく</rt></ruby>みを説明するコード<ruby>例<rt>れい</rt></ruby>です。

```javascript
const box = document.querySelector(".box");

// 1. 背景（はいけい）をオレンジ色にする
box.style.backgroundColor = "orange";

// 2. 文字を白くして、大きくする
box.style.color = "white";
box.style.fontSize = "24px"; // ⚠️ "px" を忘れないで！

// 3. 枠線（わくせん）をつける
box.style.border = "5px solid black";

```

***

### 5. 留学生へのアドバイス：Styleオブジェクトの限界

ここが<ruby>中級<rt>ちゅうきゅう</rt></ruby>者へのステップアップとして大切なポイントです。

> 「`element.style` で調べられるのは、**JavaScriptで直接つけたスタイルだけ**なんだ。
> もともとCSSファイル（`.css`）に書いてあるスタイルを知りたいときは、**`getComputedStyle(element)`** という別の<ruby>魔法<rt>まほう</rt></ruby>を使う必要があるよ！」

***

### まとめテーブル

| 特徴 | 内容 |
| --- | --- |
| **役割** | JavaScriptからCSSを操作する |
| **<ruby>書<rt>か</rt></ruby>き<ruby>方<rt>かた</rt></ruby>のルール** | ハイフンなしの「キャメルケース」 |
| **値のルール** | 必ず **" "**（ダブルクォーテーション）で囲む文字列にする |
| **単位** | <ruby>数値<rt>すうち</rt></ruby>だけでなく **"px"** や **"%"** を必ずつける |

***

いかがでしょうか？「スタイリストのStyleくん」を使えば、クリックしたときに<ruby>画面<rt>がめん</rt></ruby>を暗くしたり、メニューを横から出したりするような、リッチなサイトが作れるようになります。



