import os
from pathlib import Path
import re

# 読み込み対象のディレクトリパス
r_directory_path = '原稿/'

# 書き込み対象のディレクトリパス
w_directory_path ='src/'

# ディレクトリ内のファイルとサブディレクトリの一覧を取得
file_list = os.listdir(r_directory_path)

# ファイルを読み込む
for item in file_list:
    if item.endswith(".md"):
        r_file_path = os.path.join(r_directory_path, item)
        try:
            with open(r_file_path, "r", encoding="utf-8") as rf:
                tmp_text = rf.read()

                # 正規表現パターン
                # ｜ : 開始記号
                # (.+?) : ルビを振る文字（グループ1）
                # 《 : 振り仮名の開始
                # (.+?) : 振り仮名（グループ2）
                # 》 : 振り仮名の終了
                pattern = r"｜(.+?)《(.+?)》"

                # 置換後の文字列（\1 と \2 でグループの内容を呼び出す）
                replacement = r"<ruby>\1<rt>\2</rt></ruby>"

                # 置換実行
                result = re.sub(pattern, replacement, tmp_text)

                # 出力: <ruby>aaa<rt>bbb</rt></ruby>

                # resultを書き込みディレクトリに書き込む
                w_file_path = os.path.join(w_directory_path, item)
                with open(w_file_path , "w", encoding="utf-8") as wf:
                    wf.write(result)
                
        except IOError as e:
            print(f"ファイル書き込みエラー: {e}")        

