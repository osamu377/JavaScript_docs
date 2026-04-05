#!/usr/bin/awk -f
# MarkDown テキストのコメント部分を削除して表示
# また空行も削除

/^#/{
	print "";
	print  $0;
	print "";
	next;
} 

/^\*\*\*/{
	print "";
	print  $0;
	print "";
	next;
} 

/^---/{
	print  $0;
	print "";
	next;
} 

/^\s*$/{
    next;     # 次の行へ
}

/^「/ {
    print $0; # 行頭が「の場合はそのまま出力
    next;     # 次の行へ
}

/^（/ {
    print $0; # 行頭が（の場合はそのまま出力
    next;     # 次の行へ
}

{
    # 行頭が「でない場合、行頭に文字列を追加して出力
    print "　" $0;
}

