# Navigator（ナビゲーター）オブジェクト 

**Navigator（ナビゲーター）オブジェクト**は、<ruby>今使<rt>いまつか</rt></ruby>っている「ブラウザ（ChromeやSafariなど）」や「パソコン・スマホの<ruby>状態<rt>じょうたい</rt></ruby>」を<ruby>教<rt>おし</rt></ruby>えてくれるオブジェクトです。 

<ruby>学生<rt>がくせい</rt></ruby>の<ruby>方<rt>かた</rt></ruby>には、Navigatorオブジェクトは **「ブラウザの<ruby>身分証明書<rt>みぶんしょうめいしょ</rt></ruby>（みぶんしょうめいしょ）」** だと<ruby>教<rt>おし</rt></ruby>えてあげてください。どこの<ruby>国<rt>くに</rt></ruby>の<ruby>言葉<rt>ことば</rt></ruby>を<ruby>使<rt>つか</rt></ruby>っているか、インターネットにつながっているか、などの<ruby>情報<rt>じょうほう</rt></ruby>をすべて<ruby>持<rt>も</rt></ruby>っています。 

***


### 1. Navigatorオブジェクトとは？ 

`window.navigator` を<ruby>通<rt>とお</rt></ruby>じてアクセスします。このオブジェクトを<ruby>見<rt>み</rt></ruby>れば、ユーザーがどんな<ruby>環境<rt>かんきょう</rt></ruby>でサイトを<ruby>見<rt>み</rt></ruby>ているかが<ruby>分<rt>わ</rt></ruby>かります。 

***


### 2. よく<ruby>使<rt>つか</rt></ruby>うプロパティ（ブラウザの<ruby>情報<rt>じょうほう</rt></ruby>） 

「この<ruby>人<rt>ひと</rt></ruby>は<ruby>誰<rt>だれ</rt></ruby>？」「どんな<ruby>設定<rt>せってい</rt></ruby>？」を<ruby>知<rt>し</rt></ruby>るためのプロパティです。 

* **`userAgent`**（ユーザーエージェント）  
  ブラウザの<ruby>名前<rt>なまえ</rt></ruby>やバージョン、OS（WindowsかMacか）などの<ruby>詳細<rt>しょうさい</rt></ruby>な<ruby>情報<rt>じょうほう</rt></ruby>です。
* **<ruby>例<rt>れい</rt></ruby>：** これを<ruby>見<rt>み</rt></ruby>て「iPhoneの<ruby>人<rt>ひと</rt></ruby>にはiPhone<ruby>用<rt>よう</rt></ruby>の<ruby>画面<rt>がめん</rt></ruby>を<ruby>見<rt>み</rt></ruby>せる」といった<ruby>判断<rt>はんだん</rt></ruby>ができます。 


* **`language`**  
  ブラウザで<ruby>設定<rt>せってい</rt></ruby>されている「<ruby>言語<rt>げんご</rt></ruby>」です。
* **<ruby>例<rt>れい</rt></ruby>：** <ruby>日本語<rt>にほんご</rt></ruby>なら `ja`、<ruby>英語<rt>えいご</rt></ruby>なら `en-US` が<ruby>返<rt>かえ</rt></ruby>ってきます。これを<ruby>使<rt>つか</rt></ruby>えば、<ruby>自動<rt>じどう</rt></ruby>でメッセージを<ruby>英語<rt>えいご</rt></ruby>に<ruby>変<rt>か</rt></ruby>えられます。 


* **`onLine`**   <ruby>今<rt>いま</rt></ruby>、インターネットに **つながっているか（オンラインか）** を `true` / `false` で<ruby>教<rt>おし</rt></ruby>えてくれます。
* **`cookieEnabled`**  
  クッキー（ブラウザにデータを<ruby>保存<rt>ほぞん</rt></ruby>する<ruby>機能<rt>きのう</rt></ruby>）が<ruby>使<rt>つか</rt></ruby>える<ruby>設定<rt>せってい</rt></ruby>になっているかを<ruby>確認<rt>かくにん</rt></ruby>できます。 

***


### 3. よく<ruby>使<rt>つか</rt></ruby>うメソッド（<ruby>便利<rt>べんり</rt></ruby>な<ruby>機能<rt>きのう</rt></ruby>） 

<ruby>最近<rt>さいきん</rt></ruby>のブラウザでは、Navigatorを<ruby>使<rt>つか</rt></ruby>って<ruby>高度<rt>こうど</rt></ruby>な<ruby>機能<rt>きのう</rt></ruby>（カメラ、<ruby>位置情報<rt>いちじょうほう</rt></ruby>、コピーなど）を<ruby>動<rt>うご</rt></ruby>かすことができます。 

#### **`clipboard.writeText()`** 

<ruby>文字<rt>もじ</rt></ruby>を **「クリップボードにコピー」** します。 

* `navigator.clipboard.writeText("コピーしたい文字");` 

#### **`geolocation.getCurrentPosition()`** 

ユーザーの **「<ruby>今<rt>いま</rt></ruby>の<ruby>場所<rt>ばしょ</rt></ruby>（GPS）」** を<ruby>取得<rt>しゅとく</rt></ruby>します。 

* **イメージ：** <ruby>地図<rt>ちず</rt></ruby>アプリなどを<ruby>作<rt>つく</rt></ruby>る<ruby>時<rt>とき</rt></ruby>に<ruby>使<rt>つか</rt></ruby>います。 

***


#### 🛠️ ページの<ruby>設定<rt>せってい</rt></ruby>・<ruby>状態<rt>じょうたい</rt></ruby> 

* **`title`**（タイトル）：
* **<ruby>意味<rt>いみ</rt></ruby>：** HTMLの `&lt;title&gt;` タグに<ruby>書<rt>か</rt></ruby>いた、ブラウザの「タブ」に<ruby>出<rt>で</rt></ruby>るページのタイトルです。JavaScriptから `document.title = "新しい名前";` と<ruby>書<rt>か</rt></ruby>けば、<ruby>途中<rt>とちゅう</rt></ruby>でタブの<ruby>名前<rt>なまえ</rt></ruby>を<ruby>変<rt>か</rt></ruby>えられます。 


* **`lastModified`**（ラスト・モディファイド）：
* **<ruby>意味<rt>いみ</rt></ruby>：** このHTMLファイルが「<ruby>最後<rt>さいご</rt></ruby>に<ruby>更新<rt>こうしん</rt></ruby>（セーブ）されたのはいつか」という<ruby>日時<rt>にちじ</rt></ruby>（<ruby>日付<rt>ひづけ</rt></ruby>と<ruby>時間<rt>じかん</rt></ruby>）を<ruby>教<rt>おし</rt></ruby>えてくれます。 


* **`cookie`**（クッキー）：
* **<ruby>意味<rt>いみ</rt></ruby>：** ブラウザにユーザーのログイン<ruby>状態<rt>じょうたい</rt></ruby>や<ruby>設定<rt>せってい</rt></ruby>を<ruby>一時的<rt>いちじてき</rt></ruby>に<ruby>保存<rt>ほぞん</rt></ruby>しておくための「<ruby>小<rt>ちい</rt></ruby>さなメモ<ruby>帳<rt>ちょう</rt></ruby>」のようなデータです。 


***


### 4. <ruby>実際<rt>じっさい</rt></ruby>に<ruby>動<rt>うご</rt></ruby>かしてみよう！ 

<ruby>学生<rt>がくせい</rt></ruby>に「おもてなし（<ruby>自動言語切<rt>じどうげんごき</rt></ruby>り<ruby>替<rt>か</rt></ruby>え）」のイメージでコードを<ruby>見<rt>み</rt></ruby>せてあげましょう。 

```javascript
// 1. ユーザーの言語をチェック
const userLang = navigator.language;
if (userLang.includes("ja")) {
  console.log("こんにちは！");
} else if (userLang.includes("en")) {
  console.log("Hello!");
}
// 2. ネットがつながっているか監視（かんし）する
if (navigator.onLine) {
  console.log("オンラインです 🟢");
} else {
  alert("ネットワークが切れています 🔴");
}
```


***


### 5. <ruby>学生<rt>がくせい</rt></ruby>へのアドバイス：<ruby>情報<rt>じょうほう</rt></ruby>の<ruby>正確性<rt>せいかくせい</rt></ruby> 

「`userAgent` を<ruby>見<rt>み</rt></ruby>れば、100% <ruby>正確<rt>せいかく</rt></ruby>にブラウザがわかりますか？」と<ruby>聞<rt>き</rt></ruby>かれたら、こう<ruby>答<rt>こた</rt></ruby>えてあげてください。 

> **「`userAgent` は<ruby>昔<rt>むかし</rt></ruby>からの<ruby>複雑<rt>ふくざつ</rt></ruby>な<ruby>歴史<rt>れきし</rt></ruby>があって、<ruby>実<rt>じつ</rt></ruby>は<ruby>少<rt>すこ</rt></ruby>しウソが<ruby>混<rt>ま</rt></ruby>ざっていることもあるんだ（Chrome なのに Safari と<ruby>書<rt>か</rt></ruby>いてあったりする）。  
> だから、あまり<ruby>深<rt>ふか</rt></ruby>く<ruby>信<rt>しん</rt></ruby>じすぎず、『だいたいこんな<ruby>感<rt>かん</rt></ruby>じ』と<ruby>判断<rt>はんだん</rt></ruby>するために<ruby>使<rt>つか</rt></ruby>うのがプロのコツだよ！」**


***


### まとめテーブル 

| プロパティ・メソッド                                                  | <ruby>役割<rt>やくわり</rt></ruby>         | <ruby>例<rt>たと</rt></ruby>え<ruby>話<rt>ばなし</rt></ruby>                                           |
| ----------------------------------------------------------- | ------------------------------------ | ---------------------------------------------------------------------------------------------- |
| **`userAgent`**   | ブラウザ・OS<ruby>情報<rt>じょうほう</rt></ruby> | <ruby>自己紹介<rt>じこしょうかい</rt></ruby>（<ruby>名前<rt>なまえ</rt></ruby>や<ruby>出身地<rt>しゅっしんち</rt></ruby>） |
| **`language`**    | <ruby>言語設定<rt>げんごせってい</rt></ruby>    | <ruby>何語<rt>なにご</rt></ruby>で<ruby>話<rt>はな</rt></ruby>してほしいか                                    |
| **`onLine`**      | <ruby>通信状態<rt>つうしんじょうたい</rt></ruby>  | <ruby>今<rt>いま</rt></ruby>、<ruby>電話<rt>でんわ</rt></ruby>がつながっているか                                 |
| **`clipboard`**   | コピー<ruby>機能<rt>きのう</rt></ruby>       | メモをクリップで<ruby>留<rt>と</rt></ruby>める                                                             |
| **`geolocation`** | <ruby>位置情報<rt>いちじょうほう</rt></ruby>    | <ruby>今<rt>いま</rt></ruby>どこにいるか<ruby>教<rt>おし</rt></ruby>える                                     |


***


いかがでしょうか？「<ruby>身分証明書<rt>みぶんしょうめいしょ</rt></ruby>」であるNavigatorオブジェクトを<ruby>使<rt>つか</rt></ruby>えば、<ruby>世界中<rt>せかいじゅう</rt></ruby>のユーザー<ruby>一人<rt>ひとり</rt></ruby>ひとりに<ruby>合<rt>あ</rt></ruby>わせた<ruby>親切<rt>しんせつ</rt></ruby>なサイトが<ruby>作<rt>つく</rt></ruby>れるようになります。 
 

