#!/usr/bin/env python3
import json
from datetime import datetime

# Load manifest
with open('games-manifest.json', 'r') as f:
    data = json.load(f)

# New game
new_game = {
    "id": f"number-snap-{datetime.now().strftime('%Y-%m-%d-%H')}",
    "title": "Number Snap - ナンバーサップ",
    "description": "現在のカードと前のカードが同じ数字なら素早くタップ！シンプルだけど中毒性のあるスピードマッチングゲーム。60秒の制限時間で、正解で10点+連続ボーナス、間違えると-5点。数字は1-9で、5が出やすくなる重み付けでランダム生成。連続ヒットでストリークが増え、ボーナスポイント獲得。カードはタップでSNAP、スペースキーでも操作可能。美しいグラデーション背景とアニメーション効果で視覚的に魅力的。全画面表示対応で、モバイルからも快適に遊べます。",
    "emoji": "🔢",
    "path": "games/number-snap/index.html",
    "tags": ["HTML", "JavaScript", "Game", "Speed", "Reflex", "Puzzle"],
    "date": datetime.now().strftime('%Y-%m-%d'),
    "featured": True,
    "mobile": True
}

# Add to beginning (newest first)
data['games'].insert(0, new_game)

# Save
with open('games-manifest.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Added game: {new_game['title']}")
print(f"Total games: {len(data['games'])}")
