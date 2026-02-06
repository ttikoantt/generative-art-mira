#!/usr/bin/env python3
"""
Text-to-ASCII Art Converter
画像をASCIIアートに変換するツール

標準ライブラリのみ使用（追加パッケージ不要）
"""

import sys
import argparse
from PIL import Image

# ASCII文字セット（暗い→明い）
ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    """アスペクト比を保って画像をリサイズ"""
    original_width, original_height = image.size
    aspect_ratio = original_height / original_width
    new_height = int(new_width * aspect_ratio * 0.55)  # 0.55は文字の縦横比補正
    return image.resize((new_width, new_height))

def grayscale(image):
    """画像をグレースケールに変換"""
    return image.convert("L")

def pixels_to_ascii(image):
    """ピクセルをASCII文字に変換"""
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 32]
    return ascii_str

def image_to_ascii(image_path, width=100):
    """画像をASCIIアートに変換"""
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"エラー: 画像を開けませんでした: {e}")
        return None

    image = resize_image(image, width)
    grayscale_image = grayscale(image)
    ascii_str = pixels_to_ascii(grayscale_image)

    # 改行を挿入
    ascii_width = width
    ascii_art = "\n".join([ascii_str[i:i+ascii_width] for i in range(0, len(ascii_str), ascii_width)])

    return ascii_art

def main():
    parser = argparse.ArgumentParser(description="画像をASCIIアートに変換")
    parser.add_argument("image", help="画像ファイルのパス")
    parser.add_argument("-w", "--width", type=int, default=100, help="出力幅（デフォルト: 100）")
    parser.add_argument("-o", "--output", help="出力ファイル（オプション）")
    parser.add_argument("-i", "--invert", action="store_true", help="色を反転（明るい→暗い）")

    args = parser.parse_args()

    # 色反転
    global ASCII_CHARS
    if args.invert:
        ASCII_CHARS = " .:-=+*#%@"

    ascii_art = image_to_ascii(args.image, args.width)

    if ascii_art is None:
        sys.exit(1)

    # 出力
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(ascii_art)
        print(f"✅ ASCIIアートを保存しました: {args.output}")
    else:
        print(ascii_art)

if __name__ == "__main__":
    main()
