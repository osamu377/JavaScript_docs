import os
from pathlib import Path
import sys
import re

# 読み込み対象のディレクトリパス
r_directory_path = 'mdbook/src/'

# 書き込み対象のディレクトリパス
w_directory_path ='mdbook/no_ruby'

# 書き込み対象のディレクトリ作成
if not os.path.exists(w_directory_path):
    os.makedirs(w_directory_path)
    print(f"{w_directory_path} を作成しました。")

# コマンドライン引数からファイルリストを作成
# file_list = sys.argv

# ファイルリストを作成
#file_list = ["05_03_日付.md", "05_04_数学オブジェクト.md"]
# file_list = ["05_05_正規表現.md"]
#file_list = ["06_00_JavaScriptとオブジェクト指向.md","06_01_自分のオブジェクトを作る.md","06_02_オブジェクトを改造する.md","06_03_クラスはオブジェクトの設計図.md"]
file_list = ["04_00_ブラウザのオブジェクト.md","04_01_オブジェクトの中を見てみよう.md","04_02_Windowオブジェクト.md","04_03_DOMツリー.md","04_04_イベント処理.md","04_05_Window操作.md"]

# ファイルを読み込む
for item in file_list:
    if item == "SUMMARY.md":
        continue
    if item.endswith(".md"):
        r_file_path = os.path.join(r_directory_path, item)
        try:
            with open(r_file_path, "r", encoding="utf-8") as rf:
                tmp_text = rf.read()
                # 1. <rt>...</rt> (読み仮名) と <rp>...</rp> (括弧など) を中身ごと消す
                clean_text = re.sub(r'<(rt|rp)>.*?</(rt|rp)>', '', tmp_text)
                # 2. 残った <ruby> と </ruby> タグ自体を消す
                clean_text = re.sub(r'</?ruby>', '', clean_text)

                # resultを書き込みディレクトリに書き込む
                w_file_path = os.path.join(w_directory_path, item)
                with open(w_file_path , "w", encoding="utf-8") as wf:
                    wf.write(clean_text)

                # print(clean_text)
                # 出力: これは漢字のテストです。
        except IOError as e:
            print(f"ファイル書き込みエラー: {e}")        
