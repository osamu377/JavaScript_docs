# 🧠 JavaScriptの<ruby>記述<rt>きじゅつ</rt></ruby>ルール（<ruby>初心者<rt>しょしんしゃ</rt></ruby><ruby>向け<rt>むけ</rt></ruby>まとめ）

## 1. <ruby>文<rt>ぶん</rt></ruby>の<ruby>終わり<rt>おわり</rt></ruby>にはセミコロン（`;`）をつける

* <ruby>命令<rt>めいれい</rt></ruby>の<ruby>終わり<rt>おわり</rt></ruby>にセミコロンをつけることで、コードの<ruby>区切り<rt>くぎり</rt></ruby>が<ruby>明確<rt>めいかく</rt></ruby>になります。

```javascript
let name = "Taro";
```

***

## 2. <ruby>変数<rt>へんすう</rt></ruby>の<ruby>宣言<rt>せんげん</rt></ruby>には `let` や `const` を<ruby>使う<rt>つかう</rt></ruby>

* `let`：<ruby>変更<rt>へんこう</rt></ruby><ruby>可能<rt>かのう</rt></ruby>な<ruby>変数<rt>へんすう</rt></ruby>
* `const`：<ruby>変更<rt>へんこう</rt></ruby><ruby>不可<rt>ふか</rt></ruby>の<ruby>定数<rt>ていすう</rt></ruby>

```javascript
let age = 20;
const birthYear = 2005;
```

***

## 3. <ruby>文字列<rt>もじれつ</rt></ruby>は `" "` または `' '` で<ruby>囲む<rt>かこむ</rt></ruby>

* どちらでもOKですが、<ruby>統一<rt>とういつ</rt></ruby>して<ruby>使う<rt>つかう</rt></ruby>のが<ruby>良い<rt>よい</rt></ruby><ruby>習慣<rt>しゅうかん</rt></ruby>です。

```javascript
let greeting = "こんにちは";
```

***

## 4. インデント（<ruby>字下げ<rt>じさげ</rt></ruby>）でコードを<ruby>見やすく<rt>みやすく</rt></ruby>する

* <ruby>通常<rt>つうじょう</rt></ruby>はスペース2つまたは4つで<ruby>揃えます<rt>そろえます</rt></ruby>。

```javascript
function sayHello() {
  console.log("こんにちは！");
}
```

***

## 5. コメントを<ruby>使って<rt>つかって</rt></ruby><ruby>説明<rt>せつめい</rt></ruby>を<ruby>書く<rt>かく</rt></ruby>

* `//` を<ruby>使って<rt>つかって</rt></ruby>コードの<ruby>説明<rt>せつめい</rt></ruby>を<ruby>記述<rt>きじゅつ</rt></ruby>できます。

```javascript
// これは挨拶を表示する関数です
function sayHello() {
  console.log("こんにちは！");
}
```

***

## 6. <ruby>命名<rt>めいめい</rt></ruby>はわかりやすく、<ruby>英語<rt>えいご</rt></ruby>で<ruby>書く<rt>かく</rt></ruby>

* <ruby>変数<rt>へんすう</rt></ruby>や<ruby>関数名<rt>かんすうめい</rt></ruby>は<ruby>意味<rt>いみ</rt></ruby>のある<ruby>英語<rt>えいご</rt></ruby>で<ruby>書く<rt>かく</rt></ruby>のが<ruby>一般的<rt>いっぱんてき</rt></ruby>です。

```javascript
let userName = "Taro";
function showMessage() {
  console.log("ようこそ！");
}
```

***

## 7. <ruby>大文字<rt>おおもじ</rt></ruby>と<ruby>小文字<rt>こもじ</rt></ruby>は<ruby>区別<rt>くべつ</rt></ruby>される

* `Name` と `name` は<ruby>別<rt>べつ</rt></ruby>の<ruby>変数<rt>へんすう</rt></ruby>として<ruby>扱われます<rt>あつかわれます</rt></ruby>。

```javascript
let name = "Taro";
let Name = "Hanako";  // ← 別の変数
```

***

## 8. <ruby>文字列<rt>もじれつ</rt></ruby>やコメント<ruby>以外<rt>いがい</rt></ruby>は<ruby>半角文字<rt>はんかくもじ</rt></ruby>で<ruby>記述<rt>きじゅつ</rt></ruby>する

* JavaScriptのコードは<ruby>基本的<rt>きほんてき</rt></ruby>にすべて<ruby>半角英数字<rt>はんかくえいすうじ</rt></ruby>で<ruby>書きます<rt>かきます</rt></ruby>。
* `"こんにちは"` や `// コメント` の<ruby>中<rt>なか</rt></ruby>は<ruby>全角<rt>ぜんかく</rt></ruby>でもOKですが、それ<ruby>以外<rt>いがい</rt></ruby>は<ruby>全角文字<rt>ぜんかくもじ</rt></ruby>を<ruby>使わない<rt>つかわない</rt></ruby>ように<ruby>注意<rt>ちゅうい</rt></ruby>しましょう。

❌ ダメな<ruby>例<rt>れい</rt></ruby>（<ruby>全角<rt>ぜんかく</rt></ruby>スペースや<ruby>全角記号<rt>ぜんかくきごう</rt></ruby>）：

```javascript
ｌｅｔ　name＝"Taro";  // ← 全角が混ざっていてエラーになる可能性あり
```

✅ <ruby>正しい<rt>ただしい</rt></ruby><ruby>例<rt>れい</rt></ruby>（すべて<ruby>半角<rt>はんかく</rt></ruby>）：

```javascript
let name = "Taro";
```

***

## ✅ まとめ<ruby>表<rt>ひょう</rt></ruby>

| <ruby>項目<rt>こうもく</rt></ruby>        | <ruby>内容<rt>ないよう</rt></ruby>                                                                                            |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| セミコロン                               | <ruby>文<rt>ぶん</rt></ruby>の<ruby>終わり<rt>おわり</rt></ruby>に<ruby>付ける<rt>つける</rt></ruby>                                     |
| <ruby>変数宣言<rt>へんすうせんげん</rt></ruby>  | `let` や `const` を<ruby>使う<rt>つかう</rt></ruby>                                                                            |
| <ruby>文字列<rt>もじれつ</rt></ruby>       | `" "` または `' '` で<ruby>囲む<rt>かこむ</rt></ruby>                                                                            |
| インデント                               | <ruby>見やすく<rt>みやすく</rt></ruby>するために<ruby>字下げ<rt>じさげ</rt></ruby>                                                         |
| コメント                                | `//` で<ruby>説明<rt>せつめい</rt></ruby>を<ruby>書く<rt>かく</rt></ruby>                                                           |
| <ruby>命名<rt>めいめい</rt></ruby>        | <ruby>意味<rt>いみ</rt></ruby>のある<ruby>英語<rt>えいご</rt></ruby>で<ruby>書く<rt>かく</rt></ruby>                                     |
| <ruby>大文字小文字<rt>おおもじこもじ</rt></ruby> | <ruby>区別<rt>くべつ</rt></ruby>される                                                                                          |
| <ruby>半角文字<rt>はんかくもじ</rt></ruby>    | <ruby>文字列<rt>もじれつ</rt></ruby>・コメント<ruby>以外<rt>いがい</rt></ruby>は<ruby>半角<rt>はんかく</rt></ruby>で<ruby>記述<rt>きじゅつ</rt></ruby> |

***

<div style="page-break-before:always"></div>

