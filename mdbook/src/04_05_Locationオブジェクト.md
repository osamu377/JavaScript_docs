# Locationオブジェクト

**Locationオブジェクト** は、<ruby>今<rt>いま</rt></ruby>ブラウザで<ruby>見<rt>み</rt></ruby>ているウェブサイトの「<ruby>住所<rt>じゅうしょ</rt></ruby>（URL）」を<ruby>管理<rt>かんり</rt></ruby>するオブジェクトです。

<ruby>学生<rt>がくせい</rt></ruby>の<ruby>方<rt>かた</rt></ruby>には、Locationオブジェクトは **「ブラウザの<ruby>住所録<rt>じゅうしょろく</rt></ruby>（じゅうしょろく）」** や **「カーナビ」** だと<ruby>教<rt>おし</rt></ruby>えてあげてください。<ruby>今<rt>いま</rt></ruby>の<ruby>場所<rt>ばしょ</rt></ruby>を<ruby>知<rt>し</rt></ruby>ることもできるし、<ruby>新<rt>あたら</rt></ruby>しい<ruby>場所<rt>ばしょ</rt></ruby>へ<ruby>移動<rt>いどう</rt></ruby>することもできます。

***

### 1. Locationオブジェクトとは？

`window.location` を<ruby>通<rt>とお</rt></ruby>じてアクセスします。URLを「プロトコル」「ドメイン」「パス」などのパーツに<ruby>分<rt>わ</rt></ruby>けて<ruby>持<rt>も</rt></ruby>っているので、JavaScriptで<ruby>簡単<rt>かんたん</rt></ruby>にURLの<ruby>情報<rt>じょうほう</rt></ruby>を<ruby>調<rt>しら</rt></ruby>べたり、<ruby>変更<rt>へんこう</rt></ruby>したりできます。

***

### 2. よく<ruby>使<rt>つか</rt></ruby>うプロパティ（<ruby>住所<rt>じゅうしょ</rt></ruby>の<ruby>情報<rt>じょうほう</rt></ruby>）
<ruby>現在<rt>げんざい</rt></ruby>のURLの「どの<ruby>部分<rt>ぶぶん</rt></ruby>を<ruby>知<rt>し</rt></ruby>りたいか」によって<ruby>使<rt>つか</rt></ruby>い<ruby>分<rt>わ</rt></ruby>けます。   <ruby>例<rt>れい</rt></ruby>：`https://example.com:8080/search?q=js#result` というURLの<ruby>場合<rt>ばあい</rt></ruby>

* **`href`**  
  URLの<ruby>全部<rt>ぜんぶ</rt></ruby>です。 `console.log(location.href);`のように使います。
* **`protocol`**  
  「http:」や「https:」の<ruby>部分<rt>ぶぶん</rt></ruby>です。
* **`host`**  
  ドメイン<ruby>名<rt>めい</rt></ruby>とポート<ruby>番号<rt>ばんごう</rt></ruby>です。（`example.com:8080`）
* **`pathname`**  
  ドメインの<ruby>後<rt>あと</rt></ruby>の「フォルダやファイル」の<ruby>場所<rt>ばしょ</rt></ruby>です。（`/search`）
* **`search`**  
  `?` から<ruby>始<rt>はじ</rt></ruby>まる「クエリパラメータ」です。<ruby>検索<rt>けんさく</rt></ruby>キーワードなどが<ruby>入<rt>はい</rt></ruby>ります。（`?q=js`）
* **`hash`**  
  `#` から<ruby>始<rt>はじ</rt></ruby>まる「アンカー（ページ<ruby>内<rt>ない</rt></ruby>の<ruby>場所<rt>ばしょ</rt></ruby>）」です。（`#result`）

***

### 3. よく<ruby>使<rt>つか</rt></ruby>うメソッド（<ruby>場所<rt>ばしょ</rt></ruby>を<ruby>移動<rt>いどう</rt></ruby>する）

<ruby>新<rt>あたら</rt></ruby>しいページへ<ruby>行<rt>い</rt></ruby>きたいときや、<ruby>今<rt>いま</rt></ruby>のページをやり<ruby>直<rt>なお</rt></ruby>したいときに<ruby>使<rt>つか</rt></ruby>います。

#### **`assign("URL")`**

<ruby>指定<rt>してい</rt></ruby>したURLに<ruby>移動<rt>いどう</rt></ruby>します。
* **<ruby>特徴<rt>とくちょう</rt></ruby>：** ブラウザの「<ruby>戻<rt>もど</rt></ruby>る」ボタンで、<ruby>前<rt>まえ</rt></ruby>のページに<ruby>戻<rt>もど</rt></ruby>れます。

* `location.assign("https://google.com");`

#### **`replace("URL")`**

<ruby>新<rt>あたら</rt></ruby>しいURLに<ruby>移動<rt>いどう</rt></ruby>しますが、**<ruby>今<rt>いま</rt></ruby>のページの<ruby>履歴<rt>りれき</rt></ruby>（ひれき）を<ruby>消<rt>け</rt></ruby>します。**
* **<ruby>特徴<rt>とくちょう</rt></ruby>：** 「<ruby>戻<rt>もど</rt></ruby>る」ボタンを<ruby>押<rt>お</rt></ruby>しても、<ruby>今<rt>いま</rt></ruby>のページには<ruby>戻<rt>もど</rt></ruby>れません。ログイン<ruby>後<rt>ご</rt></ruby>の<ruby>画面<rt>がめん</rt></ruby>などでよく<ruby>使<rt>つか</rt></ruby>います。

#### **`reload()`**

<ruby>今<rt>いま</rt></ruby>のページを「<ruby>再読<rt>さいよ</rt></ruby>み<ruby>込<rt>こ</rt></ruby>み」します。ブラウザの<ruby>更新<rt>こうしん</rt></ruby>ボタンを<ruby>押<rt>お</rt></ruby>すのと<ruby>同<rt>おな</rt></ruby>じです。

***

### 4. <ruby>実際<rt>じっさい</rt></ruby>に<ruby>動<rt>うご</rt></ruby>かしてみよう！
<ruby>学生<rt>がくせい</rt></ruby>がよく<ruby>使<rt>つか</rt></ruby>う「ボタンを<ruby>押<rt>お</rt></ruby>して<ruby>別<rt>べつ</rt></ruby>のページへ<ruby>行<rt>い</rt></ruby>く」コードです。

```javascript
// 3秒後に自動（じどう）でGoogleへ移動する
setTimeout(function() {
  location.href = "https://google.com";
  // 実は location.assign() と同じ意味になります
}, 3000);
// 「更新（こうしん）ボタン」を作るなら
function refreshPage() {
  location.reload();
}
```

***

### 5. <ruby>学生<rt>がくせい</rt></ruby>へのアドバイス：`href` の<ruby>書<rt>か</rt></ruby>き<ruby>換<rt>か</rt></ruby>えが<ruby>一番人気<rt>いちばんにんき</rt></ruby>

URLを<ruby>操作<rt>そうさ</rt></ruby>する<ruby>方法<rt>ほうほう</rt></ruby>はたくさんありますが、<ruby>現場<rt>げんば</rt></ruby>で<ruby>一番<rt>いちばん</rt></ruby>よく<ruby>使<rt>つか</rt></ruby>われるのは **`location.href`** への<ruby>代入<rt>だいにゅう</rt></ruby>です。

> **「<ruby>一番簡単<rt>いちばんかんたん</rt></ruby>な<ruby>移動<rt>いどう</rt></ruby>のやり<ruby>方<rt>かた</rt></ruby>は、`location.href` に<ruby>新<rt>あたら</rt></ruby>しい<ruby>住所<rt>じゅうしょ</rt></ruby>を<ruby>代入<rt>だいにゅう</rt></ruby>することだよ。<ruby>一番覚<rt>いちばんおぼ</rt></ruby>えやすくて<ruby>便利<rt>べんり</rt></ruby>だよ！」**

***

### まとめテーブル

| プロパティ・メソッド | <ruby>役割<rt>やくわり</rt></ruby>| <ruby>例<rt>たと</rt></ruby>え<ruby>話<rt>ばなし</rt></ruby>|
| --- | --- | --- |
| **`href`** | URLのすべて | <ruby>正式<rt>せいしき</rt></ruby>な<ruby>住所<rt>じゅうしょ</rt></ruby> |
| **`pathname`**  | ファイルの<ruby>場所<rt>ばしょ</rt></ruby> | <ruby>建物<rt>たてもの</rt></ruby>の「<ruby>何階<rt>なんかい</rt></ruby>の<ruby>何号室<rt>なんごうしつ</rt></ruby>」か |
| **`search`**    | <ruby>検索<rt>けんさく</rt></ruby>データ | <ruby>住所<rt>じゅうしょ</rt></ruby>に<ruby>添<rt>そ</rt></ruby>えられた「おまけ<ruby>情報<rt>じょうほう</rt></ruby>」 |
| **`assign()`**  | ページを<ruby>移動<rt>いどう</rt></ruby>する | <ruby>次<rt>つぎ</rt></ruby>の<ruby>目的地<rt>もくてきち</rt></ruby>へ<ruby>歩<rt>ある</rt></ruby>いていく（<ruby>戻<rt>もど</rt></ruby>れる） |
| **`replace()`** | <ruby>履歴<rt>りれき</rt></ruby>を<ruby>残<rt>のこ</rt></ruby>さず<ruby>移動<rt>いどう</rt></ruby> | <ruby>瞬間移動<rt>しゅんかんいどう</rt></ruby>して<ruby>前<rt>まえ</rt></ruby>の<ruby>場所<rt>ばしょ</rt></ruby>を<ruby>忘<rt>わす</rt></ruby>れる（<ruby>戻<rt>もど</rt></ruby>れない） |
| **`reload()`**  | ページを<ruby>更新<rt>こうしん</rt></ruby>する | <ruby>同<rt>おな</rt></ruby>じ<ruby>場所<rt>ばしょ</rt></ruby>でもう<ruby>一度<rt>いちど</rt></ruby>やり<ruby>直<rt>なお</rt></ruby>す |

***

いかがでしょうか？URLをパーツごとに<ruby>理解<rt>りかい</rt></ruby>できると、<ruby>特定<rt>とくてい</rt></ruby>のページだけで<ruby>動<rt>うご</rt></ruby>くプログラムを<ruby>作<rt>つく</rt></ruby>ったり、ユーザーを<ruby>別<rt>べつ</rt></ruby>のページに<ruby>誘導<rt>ゆうどう</rt></ruby>したりできるようになります。

