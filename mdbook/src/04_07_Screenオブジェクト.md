# Screen（スクリーン）オブジェクト 

**Screen（スクリーン）オブジェクト** は、ユーザーが<ruby>今使<rt>いまつか</rt></ruby>っている「パソコンの<ruby>画面<rt>がめん</rt></ruby>」や「スマホのディスプレイ」そのものの<ruby>情報<rt>じょうほう</rt></ruby>を<ruby>教<rt>おし</rt></ruby>えてくれるオブジェクトです。 

<ruby>留学生<rt>りゅうがくせい</rt></ruby>の<ruby>方<rt>かた</rt></ruby>には、Screenオブジェクトは「パソコンやスマホの<ruby>画面<rt>がめん</rt></ruby>の<ruby>測量士<rt>そくりょうし</rt></ruby>（そくりょうし）」だと<ruby>教<rt>おし</rt></ruby>えてあげてください。<ruby>画面<rt>がめん</rt></ruby>がどれくらい<ruby>大<rt>おお</rt></ruby>きいのか、<ruby>今<rt>いま</rt></ruby>どれくらいの<ruby>広<rt>ひろ</rt></ruby>さを<ruby>使<rt>つか</rt></ruby>えるのか、といったサイズに<ruby>関<rt>かん</rt></ruby>する<ruby>情報<rt>じょうほう</rt></ruby>をすべて<ruby>持<rt>も</rt></ruby>っています。 

***


### 1. Screenオブジェクトとは？ 

`window.screen` を<ruby>通<rt>とお</rt></ruby>じてアクセスします。このオブジェクトを<ruby>見<rt>み</rt></ruby>れば、ユーザーがどんな<ruby>大<rt>おお</rt></ruby>きさのディスプレイ（モニター）でサイトを<ruby>見<rt>み</rt></ruby>ているかが<ruby>分<rt>わ</rt></ruby>かります。 

***


### 2. よく<ruby>使<rt>つか</rt></ruby>うプロパティ（<ruby>画面<rt>がめん</rt></ruby>の<ruby>情報<rt>じょうほう</rt></ruby>） 

「<ruby>画面<rt>がめん</rt></ruby>の<ruby>大<rt>おお</rt></ruby>きさはどれくらい？」を<ruby>知<rt>し</rt></ruby>るためのプロパティです。 

* **`width`**（ウィズ） / **`height`**（ハイト）  
  ディスプレイ<ruby>全体<rt>ぜんたい</rt></ruby>の **<ruby>横幅<rt>よこはば</rt></ruby>** と **<ruby>高<rt>たか</rt></ruby>さ** のピクセル<ruby>数<rt>すう</rt></ruby>です。
* **<ruby>例<rt>れい</rt></ruby>：** フルHDのモニターなら `width` は `1920`、`height` は `1080` が<ruby>返<rt>かえ</rt></ruby>ってきます。スマホやパソコンの「<ruby>画面<rt>がめん</rt></ruby>そのものの<ruby>物理的<rt>ぶつりてき</rt></ruby>な<ruby>限界<rt>げんかい</rt></ruby>サイズ」です。
* **`availWidth`**（アベラブル・ウィズ） / **`availHeight`**（アベラブル・ハイト）   <ruby>実際<rt>じっさい</rt></ruby>にブラウザが<ruby>自由<rt>じゆう</rt></ruby>に<ruby>使<rt>つか</rt></ruby>える **「<ruby>有効<rt>ゆうこう</rt></ruby>（ゆうこう）な<ruby>横幅<rt>よこはば</rt></ruby>と<ruby>高<rt>たか</rt></ruby>さ」** です。
* **<ruby>例<rt>れい</rt></ruby>：** パソコンの<ruby>画面下<rt>がめんした</rt></ruby>にある「タスクバー」や、Macの「メニューバー」など、システムが<ruby>使<rt>つか</rt></ruby>っている<ruby>場所<rt>ばしょ</rt></ruby>を<ruby>引<rt>ひ</rt></ruby>き<ruby>算<rt>ざん</rt></ruby>した、**<ruby>本当<rt>ほんとう</rt></ruby>にアプリが<ruby>動<rt>うご</rt></ruby>ける<ruby>広<rt>ひろ</rt></ruby>さ**を<ruby>教<rt>おし</rt></ruby>えてくれます。
* **`colorDepth`**（カラー・デプス）   <ruby>画面<rt>がめん</rt></ruby>が<ruby>何色<rt>なにいろ</rt></ruby>の<ruby>種類<rt>しゅるい</rt></ruby>を<ruby>表現<rt>ひょうげん</rt></ruby>できるかという **「<ruby>色深度<rt>いろしんど</rt></ruby>（いろしんど）」** です。
* **`orientation`**（オリエンテーション）  
  スマホなどの<ruby>画面<rt>がめん</rt></ruby>が<ruby>今<rt>いま</rt></ruby>、**「<ruby>縦向<rt>たてむ</rt></ruby>き（<ruby>縦長<rt>たてなが</rt></ruby>）」** か **「<ruby>横向<rt>よこむ</rt></ruby>き（<ruby>横長<rt>よこなが</rt></ruby>）」** かという<ruby>向<rt>む</rt></ruby>きの<ruby>情報<rt>じょうほう</rt></ruby>を<ruby>教<rt>おし</rt></ruby>えてくれます。 

***


### 3. よく<ruby>使<rt>つか</rt></ruby>うメソッド（<ruby>便利<rt>べんり</rt></ruby>な<ruby>機能<rt>きのう</rt></ruby>） 

Screenオブジェクト<ruby>自体<rt>じたい</rt></ruby>には、<ruby>直接動<rt>ちょくせつうご</rt></ruby>かすような<ruby>一般的<rt>いっぱんてき</rt></ruby>なメソッド（<ruby>関数<rt>かんすう</rt></ruby>）はほとんどありません。なぜなら、Screenは「<ruby>画面<rt>がめん</rt></ruby>の<ruby>状態<rt>じょうたい</rt></ruby>を<ruby>調<rt>しら</rt></ruby>べるための<ruby>観察日記<rt>かんさつにっき</rt></ruby>」のようなものだからです。 

しかし、<ruby>先<rt>さき</rt></ruby>ほど<ruby>登場<rt>とうじょう</rt></ruby>した `orientation`（<ruby>向<rt>む</rt></ruby>き）プロパティと<ruby>組<rt>く</rt></ruby>み<ruby>合<rt>あ</rt></ruby>わせることで、<ruby>最近<rt>さいきん</rt></ruby>のスマホブラウザでは<ruby>画面<rt>がめん</rt></ruby>の<ruby>向<rt>む</rt></ruby>きをコントロールすることができます。 

#### **`orientation.lock()`** 

スマホの<ruby>画面<rt>がめん</rt></ruby>を **「<ruby>縦向<rt>たてむ</rt></ruby>き、または<ruby>横向<rt>よこむ</rt></ruby>きに<ruby>固定<rt>こてい</rt></ruby>（ロック）」** します。 

* `screen.orientation.lock("landscape");`（<ruby>画面<rt>がめん</rt></ruby>を<ruby>横向<rt>よこむ</rt></ruby>きに<ruby>固定<rt>こてい</rt></ruby>します） 

#### **`orientation.unlock()`** 

<ruby>画面<rt>がめん</rt></ruby>の **「<ruby>固定<rt>こてい</rt></ruby>を<ruby>解除<rt>かいじょ</rt></ruby>（かいじょ）」** して、スマホを<ruby>傾<rt>かたむ</rt></ruby>けたら<ruby>自由<rt>じゆう</rt></ruby>に<ruby>回<rt>まわ</rt></ruby>るように<ruby>戻<rt>もど</rt></ruby>します。 

* **イメージ：** スマホ<ruby>用<rt>よう</rt></ruby>のブラウザゲームなどを<ruby>作<rt>つく</rt></ruby>る<ruby>時<rt>とき</rt></ruby>に、<ruby>勝手<rt>かって</rt></ruby>に<ruby>画面<rt>がめん</rt></ruby>が<ruby>回<rt>まわ</rt></ruby>らないようにするために<ruby>使<rt>つか</rt></ruby>います。 

***


