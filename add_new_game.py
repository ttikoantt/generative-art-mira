#!/usr/bin/env python3
import json
from datetime import datetime

# Load games manifest
with open('games-manifest.json', 'r', encoding='utf-8') as f:
    manifest = json.load(f)

# New game
reaction_rush = {
    "id": "reaction-rush",
    "title": "Reaction Rush - 反応スピードゲーム",
    "description": "3x3のグリッドでターゲットを素早くタップする反応速度ゲーム。30秒の制限時間でスコアを競い、連続ヒットでストリークボーナスを獲得。スコアに応じて出現速度が上昇し、ハイスコアはローカルストレージに保存。美しいグラデーションデザイン、アニメーション効果（パルス、ポップイン、シェイク）、モバイル対応で快適に遊べます。",
    "emoji": "⚡",
    "path": "games/reaction-rush/index.html",
    "tags": [
        "HTML5 Game",
        "Reaction",
        "Speed",
        "Reflex",
        "Touch Controls",
        "Mouse Controls"
    ],
    "date": "2026-02-08",
    "featured": True
}

# Add to beginning of list
manifest["games"].insert(0, reaction_rush)

# Save manifest
with open('games-manifest.json', 'w', encoding='utf-8') as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print("✅ Added new game to games manifest")
print(f"Total games: {len(manifest['games'])}")
