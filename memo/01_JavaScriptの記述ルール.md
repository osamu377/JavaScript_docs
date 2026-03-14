# JavaScriptの記述ルール

## 🌐 Webページにおける3つの技術の役割

### 1. HTML（HyperText Markup Language）

*   役割：Webページの「骨組み」を作る。
*   例：見出し、段落、画像、リンクなどの構造を定義。
*   イメージ：家の「柱」や「壁」のようなもの。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>こんにちは！</h1>
    <p>これはHTMLで書かれた段落です。</p>
</body>
</html>
```



### 2. CSS（Cascading Style Sheets）

*   役割：Webページの「見た目」を整える。
*   例：文字の色、サイズ、背景色、レイアウトなどを指定。
*   イメージ：家の「ペンキ」や「インテリア」のようなもの。

```css
h1 {
  color: blue;
  font-size: 36px;
}
```

<div style="page-break-before:always"></div>


### 3. JavaScript

*   役割：Webページに「動き」や「機能」を追加する。
*   例：ボタンをクリックしたらメッセージを表示、フォームの入力チェックなど。
*   イメージ：家の「電気」や「機械装置」のようなもの。

```javascript
alert("こんにちは！");
```



## 📄 HTMLファイルにCSSとJavaScriptを含める方法

### ✅ 基本のフォーマット（例）

```html
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>サンプルページ</title>

  <!-- CSSはここに書く -->
  <style>
    h1 {
      color: green;
    }
  </style>
</head>
<body>

  <h1>ようこそ！</h1>
  <button onclick="sayHello()">クリックしてね</button>

  <!-- JavaScriptはここに書く -->
  <script>
    function sayHello() {
      alert("こんにちは！");
    }
  </script>

</body>
</html>
```



### 🔧補足

*   CSSは`<style> </style>`タグで`<head>`内に書くことが多いです。
*   JavaScriptは`<script> </script>`タグで`<body>`の最後に書くと、ページの読み込みがスムーズになります。
*   外部ファイルとして分けることもできます（例：`style.css`, `script.js`）。


---

<div style="page-break-before:always"></div>

## 🧠 JavaScriptの記述ルール（初心者向けまとめ）

### 1. 文の終わりにはセミコロン（`;`）をつける
- 命令の終わりにセミコロンをつけることで、コードの区切りが明確になります。
```javascript
let name = "Taro";
```

---

### 2. 変数の宣言には `let` や `const` を使う
- `let`：変更可能な変数
- `const`：変更不可の定数
```javascript
let age = 20;
const birthYear = 2005;
```

---

### 3. 文字列は `" "` または `' '` で囲む
- どちらでもOKですが、統一して使うのが良い習慣です。
```javascript
let greeting = "こんにちは";
```

---

### 4. インデント（字下げ）でコードを見やすくする
- 通常はスペース2つまたは4つで揃えます。
```javascript
function sayHello() {
  console.log("こんにちは！");
}
```

---

### 5. コメントを使って説明を書く
- `//` を使ってコードの説明を記述できます。
```javascript
// これは挨拶を表示する関数です
function sayHello() {
  console.log("こんにちは！");
}
```

---

### 6. 命名はわかりやすく、英語で書く
- 変数や関数名は意味のある英語で書くのが一般的です。
```javascript
let userName = "Taro";
function showMessage() {
  console.log("ようこそ！");
}
```

---

### 7. 大文字と小文字は区別される
- `Name` と `name` は別の変数として扱われます。
```javascript
let name = "Taro";
let Name = "Hanako";  // ← 別の変数
```

---

### 8. 文字列やコメント以外は半角文字で記述する
- JavaScriptのコードは基本的にすべて半角英数字で書きます。
- `"こんにちは"` や `// コメント` の中は全角でもOKですが、それ以外は全角文字を使わないように注意しましょう。

❌ ダメな例（全角スペースや全角記号）：
```javascript
ｌｅｔ　name＝"Taro";  // ← 全角が混ざっていてエラーになる可能性あり
```

✅ 正しい例（すべて半角）：
```javascript
let name = "Taro";
```
<div style="page-break-before:always"></div>

---

## ✅ まとめ表

| 項目 | 内容 |
|------|------|
| セミコロン | 文の終わりに付ける |
| 変数宣言 | `let` や `const` を使う |
| 文字列 | `" "` または `' '` で囲む |
| インデント | 見やすくするために字下げ |
| コメント | `//` で説明を書く |
| 命名 | 意味のある英語で書く |
| 大文字小文字 | 区別される |
| 半角文字 | 文字列・コメント以外は半角で記述 |

---

