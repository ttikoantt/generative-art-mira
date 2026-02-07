#!/usr/bin/env python3
"""
アルゴリズム音楽ジェネレーター
Generative Music using Pentatonic Scale

ペンタトニックスケール（五音音階）を使って、
ランダム性が生む美しいメロディを生成します。
"""

import random
from datetime import datetime

# ペンタトニックスケール（Cメジャー・ペンタトニック）
# C, D, E, G, A の5つの音
PENTATONIC_SCALE = [
    ('C', 'ド'),
    ('D', 'レ'),
    ('E', 'ミ'),
    ('G', 'ソ'),
    ('A', 'ラ'),
]

# 音価（リズム）
DURATIONS = ['1', '2', '4', '8']

class GenerativeMelody:
    def __init__(self, length=16):
        self.length = length
        self.melody = []
        self.generate()

    def generate(self):
        """メロディを生成"""
        for i in range(self.length):
            note = random.choice(PENTATONIC_SCALE)
            duration = random.choice(DURATIONS)
            self.melody.append({
                'note': note[0],
                'name': note[1],
                'duration': duration
            })

    def display(self):
        """メロディを表示"""
        output = []
        output.append("🎵 アルゴリズム生成メロディ")
        output.append("=" * 40)
        output.append(f"生成時刻: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        output.append(f"長さ: {self.length} 音符")
        output.append("")
        output.append("楽譜（数字は音価、大きいほど長い）:")
        output.append("")

        # 視覚的な楽譜
        for i, m in enumerate(self.melody):
            bar_length = int(m['duration'])
            visual_bar = '█' * bar_length
            output.append(f"{i+1:2d}. {m['note']} ({m['name']}) 音価:{m['duration']}  {visual_bar}")

        output.append("")
        output.append("🎼 ASCII楽譜:")
        output.append("")

        # 簡易ASCII楽譜
        notes_only = [m['note'] for m in self.melody]
        output.append(" | ".join(notes_only))

        output.append("")
        output.append("=" * 40)
        output.append("✨ 予想外の調和を楽しんでください！")

        return "\n".join(output)

    def to_midi_notation(self):
        """MIDI風記譜"""
        notation = []
        for m in self.melody:
            notation.append(f"{m['note']}{m['duration']}")
        return " ".join(notation)


def main():
    print("\n" + "="*50)
    print("🎹 アルゴリズム音楽ジェネレーター")
    print("="*50 + "\n")

    # 複数のメロディを生成
    for i in range(3):
        melody = GenerativeMelody(length=random.randint(8, 16))
        print(f"\n--- バリエーション {i+1} ---\n")
        print(melody.display())
        print(f"\nMIDI記譜: {melody.to_midi_notation()}\n")
        print("-" * 50)


if __name__ == "__main__":
    main()
