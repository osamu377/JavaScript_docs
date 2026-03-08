BEGIN {
    in_code_block = 0
}

/^```/ {
    in_code_block = !in_code_block
    print
    next
}

{
    if (in_code_block) {
        gsub(/<ruby>(.+?)<rt>(.+?)<\/rt><\/ruby>/, "\\1（\\2）")
    }
    print
}