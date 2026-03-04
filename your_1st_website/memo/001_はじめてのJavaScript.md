# 初めてのJavaScript

JavaScriptの最初のプロジェクトを作るのはとても楽しいステップです！ここでは、**Visual Studio Code（VS Code）を使って「Hello, World!」を表示する基本的なWebページを作る方法**を、初心者向けにわかりやすく説明します。

Creating your first JavaScript project is a very fun step! Here's an easy-to-follow beginner's guide on **How to create a basic web page that displays "Hello, World!" using Visual Studio Code (VS Code)**.

---
## 準備 *preparation*

### JavaScriptで使う記号(キーボード) *Symbols used in JavaScript (keyboard)*

教科書 見開き

### 学習用フォルダの作成 *Creating a learning folder*

JSLearnフォルダをsourceフォルダ内に作り、それをピン止めする

Create a JSLearn folder in the source folder and pin it

1. ファイルエクスプローラを開き、PC > ローカルディスク > ユーザー を開く *Open File Explorer and go to PC > ローカルディスク > ユーザー.*
<img src="img/001/101.png">

1. student1 を開く *Open student1.*
<img src="img/001/102.png">

1. source を開く *Open source*
<img src="img/001/103.png">

1. 左上の+新規作成をクリックして、フォルダーをクリック *Click +New in the top left corner and click on Folders.*
<img src="img/001/104.png">

1. 新しいフォルダの名前を"JSLearn"にする *Name the new folder "JSLearn".*
<img src="img/001/105.png">
<img src="img/001/106.png">

1. "JSLearn"をクリックして選択した状態で右クリックし、現れたポップアップ・メニューで「クイック アクセスにピン留めする」をクリック *Click on "JSLearn" to select it, right-click and in the pop-up menu that appears, click on "Pin to Quick Access".*
<img src="img/001/107.png">

1. ファイルエクスプローラの左側に、JSLearnフォルダがピン留めされたことを確認する *Ensure that the JSLearn folder is pinned to the left-hand side of the file explorer.*
<img src="img/001/108.png">

### **Live Server拡張機能のインストール Install Live Server extensions** 

1. 拡張機能アイコンをクリック *Click on the extension icon*
<img src="img/001/201.png">

1. 検索ウィンドウに"Live Server"と入力 *Type 'Live Server' in the search window.*
<img src="img/001/202.png">

1. "インストール"をクリック *Click on "インストール".
<img src="img/001/203.png">

1. インストールされたことを確認 *Confirmation that it has been installed.*
<img src="img/001/204.png">

---

## 🪜 ステップバイステップ：JavaScriptプロジェクトの作成 *Step by step: creating a JavaScript project*

### ① 新しいフォルダーを作成 *Create a new folder*
- JSLearnフォルダに `MyFirstJSProject` というフォルダを作成

- Create a folder called `MyFirstJSProject` in the JSLearn folder

### ② VS Codeでフォルダーを開く *Open the folder in VS Code.*
- VS Codeを起動 → 「フォルダーを開く」 → 作成したフォルダーを選択

- Start VS Code → 'Open folder' → Select the folder you created.

### ③ ファイルを作成 *Create file*
- `index.html`（HTMLファイル）

- `index.html` (HTML file).

---

### ✍️ ファイルの中身 *What's in the file*

#### `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>My First JavaScript</title>
</head>
<body>
  <h1>Hello, World!</h1>
  <p>This is a paragraph.</p>
  <button onclick="sayHello()">Clieck Me</button>

  <script>
    function sayHello() {
      alert("Hello! Welcome to the world of JavaScript!");
    }
  </script>
</body>
</html>
```
---

### ④ Live Serverで実行 *Run on Live Server*

1. `index.html`を開いて、右下の「Go Live」ボタンをクリック
2. ブラウザが開いて、ページが表示される

1. open `index.html` and click the 'Go Live' button in the bottom right-hand corner.
2. your browser will open and the page will be displayed

---

### 🎉 実行結果 *Execution Result*

- ページに「Hello, World!」と表示される
- ボタンをクリックすると、JavaScriptが動いて「Hello!」とアラートが出る

- The page displays 'Hello, World!
- When the button is clicked, JavaScript runs and an alert appears saying "Hello!

---

### 🔹 `<!DOCTYPE html>`
- **意味**：この文書がHTML5で書かれていることをブラウザに伝える宣言です。
- **ポイント**：ページの表示を正しくするために、最初に必ず書きます。

- **Meaning**: This declaration tells the browser that the document is written in HTML5.
- **Point**: Always place this at the very beginning to ensure the page displays correctly.

---

### 🔹 `<html lang="en">`
- **意味**：HTML文書の始まりを示します。`lang="en"`は、このページの言語が英語であることを示しています。
- **ポイント**：日本語のページなら `lang="ja"` にすると良いです。

- **Meaning**: Indicates the beginning of an HTML document. The attribute `lang="en"` specifies that the language of the page is English.
- **Point**: For Japanese pages, it's better to use `lang="ja"`.

---

### 🔹 `<head>` ～ `</head>`
- **意味**：ページの「頭」の部分で、表示されない情報（設定など）をまとめます。
- **中に含まれるタグ**：
  - `<meta charset="UTF-8">`：文字コードをUTF-8に設定。日本語なども正しく表示されます。
  - `<title>`：ブラウザのタブに表示されるページのタイトル。

- **Meaning**: This is the "head" section of the page, where you include information that is not directly displayed (such as settings).
- **Tags included**:
  - `<meta charset="UTF-8">`: Sets the character encoding to UTF-8, allowing correct display of Japanese and other characters.
  - `<title>`: Specifies the title shown in the browser tab.

---

### 🔹 `<body>` ～ `</body>`
- **意味**：実際に画面に表示される内容を書く部分です。

- **Meaning**: This section contains the content that is actually displayed on the screen.

---

### 🔹 `<h1>Hello, World!</h1>`
- **意味**：大きな見出し（タイトル）を表示します。
- **ポイント**：`<h1>`は一番大きな見出し。数字が大きくなるほど小さな見出しになります（例：`<h2>`、`<h3>`）。

- **Meaning**: Displays a large heading (title).
- **Point**: `<h1>` is the largest heading. The higher the number, the smaller the heading (e.g., `<h2>`, `<h3>`).

---

### 🔹 `<p>This is a paragraph.</p>`：段落（パラグラフ）を表すタグ
- **意味**： `<p>`タグは、**文章のまとまり（段落）**を表すために使います。
- **ポイント**：「段落」とは、ひとつの考えや話題をまとめた文章のかたまりのことです。

- **Meaning**: The `<p>` tag is used to represent a **block of text (a paragraph)**.
- **Point**: A paragraph is a group of sentences that express a single idea or topic.

---

### 🔹 `<button onclick="sayHello()">Click Me</button>`
- **意味**：クリックできるボタンを表示します。
- **`onclick="sayHello()"`**：ボタンがクリックされたときに、JavaScriptの `sayHello()` 関数を実行します。

- **Meaning**: Displays a clickable button.
- **`onclick="sayHello()"`**: When the button is clicked, it runs the JavaScript function `sayHello()`.

---

### 🔹 `<script>` ～ `</script>`
- **意味**：JavaScriptというプログラミング言語を書くためのタグです。
- **中のコード**：
  ```javascript
  function sayHello() {
    alert("Hello! Welcome to the world of JavaScript!");
  }
  ```
  - `sayHello()` という関数を定義しています。
  - ボタンをクリックすると、ポップアップで「Hello! Welcome to the world of JavaScript!」と表示されます。

- **Meaning**: This tag is used to write JavaScript, a programming language.
- **Code inside**:
  ```javascript
  function sayHello() {
    alert("Hello! Welcome to the world of JavaScript!");
  }
  ```
  - Defines a function called `sayHello()`.
  - When the button is clicked, a popup message saying “Hello! Welcome to the world of JavaScript!” appears.


---
