#!/bin/sh

# タイトル取得
python3 get_title.py
TITLE_JA=$(python3 get_title.py)

# 個別にテキスト化
ls 原稿/*.md > "_tmp/filelist.txt"
while IFS= read -r md_file; do
    txt_file="${md_file%.md}.txt"
    txt_file="text/${txt_file##*/}"
    cat "$md_file" | ./fmthl.awk > "$txt_file"
done < "_tmp/filelist.txt"


# まとめてテキスト化
cat 原稿/*.md > "_tmp/$TITLE_JA.md"
cat "_tmp/$TITLE_JA.md"  | ./fmthl.awk > "text/$TITLE_JA.txt"

rm -rf _tmp/*

exit 0

