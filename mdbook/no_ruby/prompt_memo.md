以下のルールでHTML５のフリガナを振ってください

- すべての漢字に HTML ルビ <ruby>…<rt>…</rt></ruby> を付与
- Markdown構造・表・画像は原文のまま維持
- バッククォートや記号を壊さないように注意して処理

---ここからフリガナ対象

### 3. `i` フラグの `i` は何の略？

この `i` は、英語の **IgnoreCase（イグノア・ケース：大文字小文字を無視する）** という言葉の頭文字です。

通常、JavaScriptの正規表現は大文字と小文字を「完全に別の文字」として区別します。しかし、`i` フラグをつけると、それらを **同じ文字** として扱ってくれるようになります。

#### コードで見る違い（フラグがある時・ない時）

自分のパソコンのブランド（Apple）について書いた文章から文字を探してみましょう。

```javascript
const text = "My computer is an apple MacBook."; // 小文字の apple

// 1. i フラグを【つけない】とき（きびしく さがす）
const regExp1 = new RegExp("Apple"); // 大文字の A
console.log(text.match(regExp1) !== null); // false （大文字と小文字がちがうので、見つからない！）

// 2. i フラグを【つける】とき（やさしく さがす）
const regExp2 = new RegExp("Apple", "i"); // うしろに i をつけました！
console.log(text.match(regExp2) !== null); // true  （大文字小文字をむしするので、見つかった！）

```

このように、パターンのスラッシュの後ろに `/パターン/i` と書くだけで、`Apple` も `apple` も `APPLE` も、ぜんぶ一緒に見つけてくれるようになります。

#### 前に習った `g` フラグと一緒に使える？

はい、**一緒に使えます！** 順番は `ig` でも `gi` でもどちらでも大丈夫です。
これらを組み合わせると、**「大文字小文字を気にせず（ `i` ）、文章全体からすべて集める（ `g` ）」** という強力な捜査ができます。

```javascript
const text = "JavaScript is great. I love javascript!";

// 大文字小文字を気にせず（i）、ぜんぶ集める（g）
const myRegExp = new RegExp("javascript", "ig"); 

const result = text.match(myRegExp);
console.log(result); // ["JavaScript", "javascript"] （両方ともしっかり捕まえた！）

```
