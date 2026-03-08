import re
import argparse
import sys
import glob

def convert_ruby_in_code_blocks(input_text):
    """テキスト内のコードブロックにあるルビを置換するコアロジック"""
    lines = input_text.splitlines()
    in_code_block = False
    ruby_pattern = re.compile(r'<ruby>(.+?)<rt>(.+?)</rt></ruby>')
    output_lines = []

    for line in lines:
        if line.startswith('```'):
            in_code_block = not in_code_block
            output_lines.append(line)
            continue

        if in_code_block:
            line = ruby_pattern.sub(r'\1（\2）', line)
        
        output_lines.append(line)
    
    return "\n".join(output_lines)

def main():
    parser = argparse.ArgumentParser(description="Markdownのコードブロック内のルビを置換します。")
    parser.add_argument("input_file", help="入力するMarkdownファイル名 (ワイルドカード対応)")
    parser.add_argument("-o", "--output", help="出力ファイル名 (指定がない場合は標準出力)")
    parser.add_argument("-i", "--inplace", action="store_true", help="ファイルを上書き保存します")

    args = parser.parse_args()

    # ワイルドカード対応
    input_files = glob.glob(args.input_file)
    if not input_files:
        print(f"Error: {args.input_file} にマッチするファイルが見つかりません。", file=sys.stderr)
        return

    for input_file in input_files:
        # ファイルの読み込み
        try:
            with open(input_file, "r", encoding="utf-8") as f:
                content = f.read()
        except FileNotFoundError:
            print(f"Error: {input_file} が見つかりません。", file=sys.stderr)
            continue

        # 変換処理
        result = convert_ruby_in_code_blocks(content)

        # 出力処理
        if args.inplace:
            with open(input_file, "w", encoding="utf-8") as f:
                f.write(result)
            print(f"Done: {input_file} を上書き保存しました。")
        elif args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(result)
            print(f"Done: {args.output} に保存しました。")
        else:
            print(result)

if __name__ == "__main__":
    main()

