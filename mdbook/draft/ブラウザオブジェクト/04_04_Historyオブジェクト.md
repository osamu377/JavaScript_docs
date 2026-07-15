# Historyオブジェクト 

**Historyオブジェクト**は、ブラウザの「<ruby>戻<rt>もど</rt></ruby>る」ボタンや「<ruby>進<rt>すす</rt></ruby>む」ボタンと<ruby>同<rt>おな</rt></ruby>じ<ruby>役割<rt>やくわり</rt></ruby>をするオブジェクトです。 

<ruby>学生<rt>がくせい</rt></ruby>の<ruby>方<rt>かた</rt></ruby>には、Historyオブジェクトは**「ブラウザの<ruby>中<rt>なか</rt></ruby>にある『タイムマシン』」**だと<ruby>教<rt>おし</rt></ruby>えてあげてください。ユーザーが<ruby>今<rt>いま</rt></ruby>までに<ruby>見<rt>み</rt></ruby>てきたページの<ruby>履歴<rt>りれき</rt></ruby>（ひれき）を<ruby>管理<rt>かんり</rt></ruby>しています。 

***

### 1. Historyオブジェクトとは？ 

`window.history` を<ruby>通<rt>とお</rt></ruby>じてアクセスします。ユーザーがそのタブでこれまでに<ruby>訪<rt>おとず</rt></ruby>れたページのリストを<ruby>持<rt>も</rt></ruby>っていて、JavaScriptから「1つ<ruby>前<rt>まえ</rt></ruby>のページに<ruby>戻<rt>もど</rt></ruby>る」といった<ruby>操作<rt>そうさ</rt></ruby>ができます。 

***

### 2. よく<ruby>使<rt>つか</rt></ruby>うプロパティ（<ruby>履歴<rt>りれき</rt></ruby>の<ruby>情報<rt>じょうほう</rt></ruby>） 

* **`length`**   <ruby>現在<rt>げんざい</rt></ruby>のタブの<ruby>履歴<rt>りれき</rt></ruby>リストに、<ruby>全部<rt>ぜんぶ</rt></ruby>でいくつページがあるかを<ruby>教<rt>おし</rt></ruby>えてくれます。
* `console.log(history.length);`
* <ruby>初<rt>はじ</rt></ruby>めて<ruby>開<rt>ひら</rt></ruby>いたタブなら `1` になります。 

***

### 3. よく<ruby>使<rt>つか</rt></ruby>うメソッド（タイムマシンを<ruby>動<rt>うご</rt></ruby>かす） 

<ruby>直感的<rt>ちょっかんてき</rt></ruby>に<ruby>使<rt>つか</rt></ruby>えるメソッドが<ruby>揃<rt>そろ</rt></ruby>っています。 

#### **`back()`** 

ブラウザの「<ruby>戻<rt>もど</rt></ruby>る（←）」ボタンを<ruby>押<rt>お</rt></ruby>すのと<ruby>同<rt>おな</rt></ruby>じです。1つ<ruby>前<rt>まえ</rt></ruby>のページに<ruby>戻<rt>もど</rt></ruby>ります。 

* `history.back();` 

#### **`forward()`** 

ブラウザの「<ruby>進<rt>すす</rt></ruby>む（→）」ボタンを<ruby>押<rt>お</rt></ruby>すのと<ruby>同<rt>おな</rt></ruby>じです。 

* `history.forward();` 

#### **`go(数字)`** 

<ruby>指定<rt>してい</rt></ruby>した<ruby>数<rt>かず</rt></ruby>だけ、<ruby>履歴<rt>りれき</rt></ruby>を<ruby>移動<rt>いどう</rt></ruby>します。 

* `history.go(-1);` （1つ<ruby>戻<rt>もど</rt></ruby>る。`back()` と<ruby>同<rt>おな</rt></ruby>じ）
* `history.go(-2);` （2つ<ruby>戻<rt>もど</rt></ruby>る）
* `history.go(1);` （1つ<ruby>進<rt>すす</rt></ruby>む。`forward()` と<ruby>同<rt>おな</rt></ruby>じ） 

***

### 4. <ruby>高度<rt>こうど</rt></ruby>なメソッド：URLを<ruby>書<rt>か</rt></ruby>き<ruby>換<rt>か</rt></ruby>える（<ruby>履歴<rt>りれき</rt></ruby>を<ruby>作<rt>つく</rt></ruby>る） 

<ruby>最近<rt>さいきん</rt></ruby>のモダンなウェブサイト（SPAなど）でよく<ruby>使<rt>つか</rt></ruby>われる、<ruby>少<rt>すこ</rt></ruby>し<ruby>魔法<rt>まほう</rt></ruby>のようなメソッドです。 

#### **`pushState(データ, タイトル, URL)`** 

**ページを<ruby>読<rt>よ</rt></ruby>み<ruby>直<rt>なお</rt></ruby>さずに、URLだけを<ruby>新<rt>あたら</rt></ruby>しく<ruby>書<rt>か</rt></ruby>き<ruby>換<rt>か</rt></ruby>えて<ruby>履歴<rt>りれき</rt></ruby>に<ruby>追加<rt>ついか</rt></ruby>します。** 

* **<ruby>例<rt>れい</rt></ruby>：** <ruby>検索結果<rt>けんさくけっか</rt></ruby>をフィルタリングしたときに、ページはそのままでURLだけを<ruby>変<rt>か</rt></ruby>えたいときに<ruby>使<rt>つか</rt></ruby>います。 

#### **`replaceState(データ, タイトル, URL)`** 

<ruby>今<rt>いま</rt></ruby>の<ruby>履歴<rt>りれき</rt></ruby>を、<ruby>新<rt>あたら</rt></ruby>しいURLで **<ruby>上書<rt>うわが</rt></ruby>き（<ruby>書<rt>か</rt></ruby>き<ruby>換<rt>か</rt></ruby>え）** します。 

***

### 5. <ruby>実際<rt>じっさい</rt></ruby>に<ruby>動<rt>うご</rt></ruby>かしてみよう！ 

<ruby>学生<rt>がくせい</rt></ruby>に「<ruby>戻<rt>もど</rt></ruby>るボタン」を<ruby>自作<rt>じさく</rt></ruby>する<ruby>方法<rt>ほうほう</rt></ruby>を<ruby>教<rt>おし</rt></ruby>えてあげましょう。 

```javascript
// 「戻る」ボタンを作るとき
function goBack() {
  // 履歴が1つ以上あれば戻る
  if (history.length > 1) {
    history.back();
  } else {
    alert("戻るページがありません！");
  }
}
```

***

### 6. <ruby>学生<rt>がくせい</rt></ruby>へのアドバイス：プライバシーに<ruby>注意<rt>ちゅうい</rt></ruby>！ 

<ruby>学生<rt>がくせい</rt></ruby>が「ユーザーがどのサイトから<ruby>来<rt>き</rt></ruby>たか（URLの<ruby>中身<rt>なかみ</rt></ruby>）」を<ruby>知<rt>し</rt></ruby>りたがることがありますが、それはできません。 

> **「Historyオブジェクトは『<ruby>何個戻<rt>なんこもど</rt></ruby>れるか』や『<ruby>戻<rt>もど</rt></ruby>れ！』という<ruby>命令<rt>めいれい</rt></ruby>はできるけど、プライバシーを<ruby>守<rt>まも</rt></ruby>るために『<ruby>戻<rt>もど</rt></ruby>る<ruby>先<rt>さき</rt></ruby>の<ruby>具体的<rt>ぐたいてき</rt></ruby>なURL』を<ruby>覗<rt>のぞ</rt></ruby>くことはできないんだよ」**

***

### まとめテーブル 

| プロパティ・メソッド | <ruby>役割<rt>やくわり</rt></ruby> | <ruby>例<rt>たと</rt></ruby>え<ruby>話<rt>ばなし</rt></ruby> |
| --- | --- | --- |
| **`length`** | <ruby>履歴<rt>りれき</rt></ruby>の<ruby>数<rt>かず</rt></ruby> | <ruby>今<rt>いま</rt></ruby>まで<ruby>何箇所<rt>なんかしょ</rt></ruby>の<ruby>駅<rt>えき</rt></ruby>を<ruby>通<rt>とお</rt></ruby>ったか |
| **`back()`** | <ruby>戻<rt>もど</rt></ruby>る | <ruby>電車<rt>でんしゃ</rt></ruby>を1<ruby>駅戻<rt>えきもど</rt></ruby>す |
| **`forward()`** | <ruby>進<rt>すす</rt></ruby>む | <ruby>電車<rt>でんしゃ</rt></ruby>を1<ruby>駅進<rt>えきすす</rt></ruby>める |
| **`go(-2)`** | <ruby>指定<rt>してい</rt></ruby>した<ruby>数戻<rt>かずもど</rt></ruby>る | <ruby>特急<rt>とっきゅう</rt></ruby>で2<ruby>駅分戻<rt>えきぶんもど</rt></ruby>る |
| **`pushState()`** | <ruby>履歴<rt>りれき</rt></ruby>を<ruby>偽造<rt>ぎぞう</rt></ruby>（？）する | <ruby>実際<rt>じっさい</rt></ruby>に<ruby>移動<rt>いどう</rt></ruby>せずに、<ruby>切符<rt>きっぷ</rt></ruby>のスタンプだけ<ruby>増<rt>ふ</rt></ruby>やす |

***

いかがでしょうか？「タイムマシンのボタン」をJavaScriptで<ruby>操作<rt>そうさ</rt></ruby>できると、よりアプリらしい<ruby>便利<rt>べんり</rt></ruby>なサイトが<ruby>作<rt>つく</rt></ruby>れるようになります。 
