#!/usr/bin/env python3
"""
Music Visualizer - 音乐を視覚パターンに変換するジェネレーター
音楽の「メロディ」「リズム」「ハーモニー」を色付きASCIIアートで表現
"""

import random
import sys

# ANSI カラーコード
COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'bright_red': '\033[38;5;196m',
    'bright_green': '\033[38;5;46m',
    'bright_yellow': '\033[38;5;226m',
    'bright_blue': '\033[38;5;21m',
    'bright_magenta': '\033[38;5;201m',
    'bright_cyan': '\033[38;5;51m',
    'orange': '\033[38;5;208m',
    'pink': '\033[38;5;213m',
    'purple': '\033[38;5;141m',
    'reset': '\033[0m',
    'bold': '\033[1m',
}

def colorize(text, color):
    """テキストに色を適用"""
    return f"{COLORS[color]}{text}{COLORS['reset']}"

def random_color():
    """ランダムな色を選択"""
    return random.choice(list(COLORS.keys())[:-3])  # reset, boldを除外

class MusicPattern:
    """音楽的なパターンを生成"""

    PATTERNS = {
        'melody': ['♪', '♫', '♬', '♩', '♭', '♯', '𝅘𝅥𝅮', '𝅘𝅥𝅯', '𝅘𝅥𝅰', '𝅘𝅥𝅱'],
        'rhythm': ['▓', '▒', '░', '█', '▄', '▀', '■', '□'],
        'harmony': ['○', '●', '◎', '◉', '⊕', '⊗', '◌', '◍'],
        'ambient': ['·', '•', '∙', '∘', '◦', '∼', '≈', '∿'],
        'electronic': ['▣', '▢', '▤', '▥', '▦', '▧', '▨', '▩'],
    }

    def __init__(self, style='random'):
        self.style = style if style != 'random' else random.choice(['ambient', 'electronic', 'melodic', 'rhythmic'])

    def generate_line(self, width=60):
        """一行のパターンを生成"""
        pattern_type = random.choice(list(self.PATTERNS.keys()))
        chars = self.PATTERNS[pattern_type]

        # パターンの密度を決定
        density = random.uniform(0.3, 0.8)

        line = []
        for i in range(width):
            if random.random() < density:
                char = random.choice(chars)
                color = random_color()
                line.append(colorize(char, color))
            else:
                line.append(' ')

        return ''.join(line)

    def generate_composition(self, height=20, width=60):
        """全体の構成を生成"""
        composition = []

        # タイトル
        style_names = {
            'ambient': '🎵 Ambient Soundscape',
            'electronic': '⚡ Electronic Pulse',
            'melodic': '🎶 Melodic Flow',
            'rhythmic': '🥁 Rhythmic Pattern',
        }

        title = style_names.get(self.style, '🎵 Musical Pattern')
        composition.append(colorize(f"\n{title}\n", 'bold'))
        composition.append(colorize('─' * width + '\n', 'white'))

        # パターンを生成
        for _ in range(height):
            composition.append(self.generate_line(width) + '\n')

        # ボトムライン
        composition.append(colorize('─' * width, 'white'))

        return ''.join(composition)

def main():
    """メイン処理"""
    print(colorize('\n' + '=' * 60, 'bold'))
    print(colorize('🎵 Music Visualizer - 音乐を視覚化', 'bold'))
    print(colorize('=' * 60 + '\n', 'bold'))

    # 複数のスタイルを生成
    styles = ['ambient', 'electronic', 'melodic', 'rhythmic']

    for i, style in enumerate(styles, 1):
        pattern = MusicPattern(style=style)
        composition = pattern.generate_composition(height=12, width=60)
        print(composition)
        print()

    print(colorize('✨ 毎回違うパターンが生成されます', 'cyan'))
    print(colorize('=' * 60, 'bold'))

if __name__ == '__main__':
    main()
