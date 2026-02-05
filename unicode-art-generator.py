#!/usr/bin/env python3
"""
Unicode Art Pattern Generator
美しいUnicode文字でパターンを生成する
"""

import random
import hashlib
import sys

class UnicodeArtGenerator:
    """Unicode文字を使ったアートパターンジェネレーター"""

    # Unicode文字セット
    BLOCKS = ['█', '▀', '▄', '▌', '▐', '░', '▒', '▓', '▪', '▫']
    GEOMETRIC = ['◆', '◇', '○', '●', '■', '□', '▲', '▼', '◀', '▶', '△', '▽', '◢', '◣', '◤', '◥']
    ARROWS = ['←', '→', '↑', '↓', '↖', '↗', '↘', '↙', '⇐', '⇒', '⇑', '⇓', '⟵', '⟶', '⟵', '⟶']
    STARS = ['✦', '✧', '★', '☆', '✪', '✫', '✬', '✭', '✮', '✯', '✰', '✱', '✲', '✳', '✴', '✵']
    FLOWERS = ['✿', '❀', '❁', '❂', '❃', '❄', '❅', '❆', '❇', '❈', '❉', '❊', '❋']
    SPECIAL = ['♠', '♣', '♥', '♦', '♤', '♧', '♡', '♢', '☀', '☁', '☂', '☃', '☄', '★', '☆']

    def __init__(self, seed=None):
        """シードを設定（文字列からハッシュ生成）"""
        if seed is None:
            seed = str(random.random())
        # 文字列から数値シードを生成
        hash_obj = hashlib.md5(seed.encode())
        self.seed = int(hash_obj.hexdigest(), 16) % (2**32)
        random.seed(self.seed)

    def generate_symmetric(self, width=40, height=15, char_set='GEOMETRIC'):
        """対称的なパターンを生成"""
        chars = getattr(self, char_set, self.GEOMETRIC)
        pattern = []

        for y in range(height):
            row = []
            for x in range(width):
                # 左半分だけ生成
                if x < width // 2:
                    char = random.choice(chars)
                    row.append(char)
                else:
                    # 対称にコピー
                    row.append(row[width - 1 - x])
            pattern.append(''.join(row))

        return '\n'.join(pattern)

    def generate_waves(self, width=50, height=12, char_set='BLOCKS'):
        """波のようなパターンを生成"""
        chars = getattr(self, char_set, self.BLOCKS)
        pattern = []

        for y in range(height):
            row = []
            for x in range(width):
                # 波の計算
                wave = (x + y) % len(chars)
                row.append(chars[wave])
            pattern.append(''.join(row))

        return '\n'.join(pattern)

    def generate_fractal_like(self, width=40, height=15, char_set='STARS'):
        """フラクタル風のパターン"""
        chars = getattr(self, char_set, self.STARS)
        pattern = []

        for y in range(height):
            row = []
            for x in range(width):
                # シンプルなフラクタル風パターン
                if (x * y) % 7 == 0 or (x + y) % 5 == 0:
                    row.append(random.choice(chars))
                else:
                    row.append(' ')
            pattern.append(''.join(row))

        return '\n'.join(pattern)

    def generate_matrix_rain(self, width=30, height=20):
        """マトリックス風の雨"""
        chars = ['0', '1', '█', '▓', '▒', '░', '■', '□']
        pattern = []

        # ランダムな「雨滴」の位置
        raindrops = [random.randint(0, width-1) for _ in range(5)]

        for y in range(height):
            row = []
            for x in range(width):
                if x in raindrops:
                    row.append(random.choice(chars))
                else:
                    # 確率的に文字を表示
                    if random.random() < 0.1:
                        row.append(random.choice(chars))
                    else:
                        row.append(' ')
            pattern.append(''.join(row))

        return '\n'.join(pattern)

    def generate_from_text(self, text, pattern_type='symmetric'):
        """テキストからパターンを生成"""
        self.__init__(seed=text)  # テキストをシードとして再初期化

        if pattern_type == 'symmetric':
            return self.generate_symmetric()
        elif pattern_type == 'waves':
            return self.generate_waves()
        elif pattern_type == 'fractal':
            return self.generate_fractal_like()
        elif pattern_type == 'matrix':
            return self.generate_matrix_rain()
        else:
            return self.generate_symmetric()


def main():
    """メイン実行関数"""
    print("=" * 50)
    print("🎨 Unicode Art Pattern Generator")
    print("=" * 50)
    print()

    gen = UnicodeArtGenerator(seed="autonomous-experiment-05")

    # パターン1: 対称的幾何学
    print("🔷 Symmetric Geometric")
    print("-" * 40)
    print(gen.generate_symmetric(width=40, height=10, char_set='GEOMETRIC'))
    print()

    # パターン2: 波ブロック
    print("🌊 Wave Blocks")
    print("-" * 40)
    gen.__init__(seed="waves")
    print(gen.generate_waves(width=45, height=10, char_set='BLOCKS'))
    print()

    # パターン3: フラクタル星
    print("✨ Fractal Stars")
    print("-" * 40)
    gen.__init__(seed="stars")
    print(gen.generate_fractal_like(width=35, height=12, char_set='STARS'))
    print()

    # パターン4: マトリックス風
    print("💻 Matrix Rain")
    print("-" * 40)
    gen.__init__(seed="matrix")
    print(gen.generate_matrix_rain(width=30, height=15))
    print()

    # パターン5: テキスト「MIRA」から
    print("🔤 From 'MIRA'")
    print("-" * 40)
    print(gen.generate_from_text("MIRA", pattern_type='symmetric'))
    print()


if __name__ == "__main__":
    main()
