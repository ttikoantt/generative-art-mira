#!/usr/bin/env python3
"""
AlgoPoet - Algorithmic Poetry Generator
Generates short, meaning-deep poems in Japanese and English
"""

import random
import sys

class AlgoPoet:
    def __init__(self):
        # Japanese word pools
        self.jp_nouns = [
            "光", "時", "夜", "夢", "風", "星", "海", "空", "影", "道",
            "心", "静寂", "永遠", "瞬間", "記憶", "波", "月", "花", "雨", "雪",
            "朝", "夕", "森", "山", "川", "火", "水", "地球", "宇宙", "命"
        ]

        self.jp_verbs = [
            "踊る", "歌う", "眠る", "醒める", "流れる", "燃える", "消える",
            "舞う", "揺れる", "輝く", "降る", "抱く", "解く", "纺ぐ", "咲く"
        ]

        self.jp_adjectives = [
            "静かな", "遠き", "優しき", "深き", "高き", "青き", "白き",
            "永遠の", "儚き", "美しき", "暗き", "明るき", "静謐な", "悠久の"
        ]

        self.jp_connectors = [
            "〜の", "に", "で", "から", "へ", "と"
        ]

        # English word pools
        self.en_nouns = [
            "light", "time", "night", "dream", "wind", "star", "sea", "sky",
            "shadow", "path", "heart", "silence", "eternity", "moment",
            "memory", "wave", "moon", "flower", "rain", "snow", "dawn",
            "dusk", "forest", "mountain", "river", "fire", "water", "earth",
            "universe", "life"
        ]

        self.en_verbs = [
            "dances", "sings", "sleeps", "wakes", "flows", "burns", "fades",
            "floats", "sways", "shines", "falls", "embraces", "unfolds", "blooms"
        ]

        self.en_adjectives = [
            "silent", "distant", "gentle", "deep", "high", "blue", "white",
            "eternal", "fragile", "beautiful", "dark", "bright", "serene"
        ]

        self.en_prepositions = [
            "in", "of", "from", "to", "with", "beyond"
        ]

    def generate_jp_poem(self, lines=3):
        """Generate a Japanese poem"""
        poem = []

        patterns = [
            lambda: f"{random.choice(self.jp_adjectives)}{random.choice(self.jp_nouns)}",
            lambda: f"{random.choice(self.jp_nouns)}{random.choice(self.jp_connectors)}",
            lambda: f"{random.choice(self.jp_nouns)}が{random.choice(self.jp_verbs)}",
            lambda: f"{random.choice(self.jp_nouns)}の{random.choice(self.jp_nouns)}",
            lambda: f"{random.choice(self.jp_adjectives)}{random.choice(self.jp_nouns)}が{random.choice(self.jp_verbs)}",
        ]

        for _ in range(lines):
            line = random.choice(patterns)()
            poem.append(line)

        return poem

    def generate_en_poem(self, lines=3):
        """Generate an English poem"""
        poem = []

        patterns = [
            lambda: f"{random.choice(self.en_adjectives)} {random.choice(self.en_nouns)}",
            lambda: f"{random.choice(self.en_nouns)} {random.choice(self.en_verbs)}",
            lambda: f"{random.choice(self.en_nouns)} {random.choice(self.en_prepositions)} {random.choice(self.en_nouns)}",
            lambda: f"The {random.choice(self.en_adjectives)} {random.choice(self.en_nouns)} {random.choice(self.en_verbs)}",
            lambda: f"{random.choice(self.en_noun_plural) if hasattr(self, 'en_noun_plural') else random.choice(self.en_nouns)} {random.choice(self.en_verbs)} {random.choice(self.en_prepositions)} {random.choice(self.en_adjectives)} {random.choice(self.en_nouns)}",
        ]

        for _ in range(lines):
            line = random.choice(patterns)()
            # Capitalize first letter
            line = line[0].upper() + line[1:]
            poem.append(line)

        return poem

    def generate_both(self, lines=3):
        """Generate both Japanese and English versions"""
        return {
            "japanese": self.generate_jp_poem(lines),
            "english": self.generate_en_poem(lines)
        }

def print_poem(poem, title=""):
    """Print a poem with nice formatting"""
    if title:
        print(f"\n{'='*40}")
        print(f"{title:^40}")
        print('='*40)

    for line in poem:
        print(f"  {line}")
    print()

def main():
    poet = AlgoPoet()

    # Generate multiple poems
    print("\n" + "="*50)
    print(" "*15 + "✨ AlgoPoet ✨")
    print("="*50 + "\n")

    # Poem 1: Japanese
    print("🇯🇵 Japanese Poem")
    print_poem(poet.generate_jp_poem(4))

    # Poem 2: English
    print("🇺🇸 English Poem")
    print_poem(poet.generate_en_poem(4))

    # Poem 3: Both versions
    print("🌸 Dual Language Poem")
    both = poet.generate_both(3)
    print("\nJapanese:")
    print_poem(both["japanese"])
    print("\nEnglish:")
    print_poem(both["english"])

if __name__ == "__main__":
    main()
