#!/usr/bin/env python3
"""
Math Art: マンダラ風数式パターン
数学関数の美しさをASCIIアートで表現
"""

import math
import random

def mandala_pattern(size=12, zoom=1.0):
    """数式からマンダラ風パターンを生成"""
    width = size * 2 + 1
    height = size * 2 + 1
    result = []

    # 数式パラメータ（黄金比・円周率・フィボナッチ）
    phi = (1 + math.sqrt(5)) / 2  # 黄金比
    pi = math.pi

    # 数式パターン選択
    patterns = [
        # 0: 黄金比スパイラル
        lambda r, theta: abs(math.sin(r * phi + theta * 3)),
        # 1: 円周率フラクタル
        lambda r, theta: abs(math.cos(r * pi / 2) * math.sin(theta * pi)),
        # 2: フィボナッチ螺旋
        lambda r, theta: abs(math.sin(r * 1.618) * math.cos(theta * 2.618)),
        # 3: 超越関数ブレンド
        lambda r, theta: abs(math.sin(r) * math.cos(theta) + math.cos(r * theta)),
        # 4: 複素数的パターン
        lambda r, theta: abs(math.sin(r * math.cos(theta)) * math.cos(r * math.sin(theta))),
    ]

    pattern = patterns[random.randint(0, len(patterns) - 1)]

    for y in range(-size, size + 1):
        row = ""
        for x in range(-size, size + 1):
            # 極座標変換
            r = math.sqrt(x * x + y * y) * zoom / size
            theta = math.atan2(y, x)

            # 数式でパターン生成
            value = pattern(r, theta)

            # 文字マッピング（密度で表現）
            if value < 0.2:
                char = "  "
            elif value < 0.3:
                char = "░░"
            elif value < 0.4:
                char = "▒▒"
            elif value < 0.5:
                char = "▓▓"
            elif value < 0.6:
                char = "██"
            elif value < 0.7:
                char = "◇◇"
            elif value < 0.8:
                char = "◆◆"
            elif value < 0.9:
                char = "★ "
            else:
                char = "✦ "

            row += char
        result.append(row)

    return "\n".join(result)

def interactive_mandala():
    """インタラクティブにマンダラを生成"""
    print("=" * 50)
    print("🔬 Math Art: マンダラ風数式パターン")
    print("=" * 50)
    print("数式の美しさをASCIIアートで表現")
    print("\nコマンド:")
    print("  Enter - 新しいパターン生成")
    print("  s [N] - サイズ変更 (4-16, デフォルト12)")
    print("  z [N] - ズーム (0.5-3.0, デフォルト1.0)")
    print("  q - 終了\n")

    size = 12
    zoom = 1.0
    count = 0

    while True:
        print(f"\n--- Pattern #{count + 1} (size={size}, zoom={zoom:.1f}) ---")
        print(mandala_pattern(size, zoom))

        cmd = input("\n> ").strip().lower()

        if cmd == "q":
            print("\n🎨 数式の美しさ、楽しんでくれてありがとう！")
            break
        elif cmd.startswith("s "):
            try:
                size = max(4, min(16, int(cmd.split()[1])))
            except:
                size = 12
        elif cmd.startswith("z "):
            try:
                zoom = max(0.5, min(3.0, float(cmd.split()[1])))
            except:
                zoom = 1.0
        elif cmd == "":
            count += 1

if __name__ == "__main__":
    interactive_mandala()
