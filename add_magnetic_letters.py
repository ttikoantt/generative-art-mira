#!/usr/bin/env python3
import json
from datetime import datetime

# Load manifest
with open('artworks-manifest.json', 'r') as f:
    data = json.load(f)

# New artwork
new_artwork = {
    "id": f"magnetic-letters-{datetime.now().strftime('%Y-%m-%d-%H')}",
    "title": "Magnetic Letters - 磁気文字",
    "description": "文字が磁石のように動くインタラクティブアート。50個の文字が物理法則に従って動き、マウスカーソルに引き寄せられたり、互いに反発したりします。文字同士が近づくと線で繋がれ、美しい光のネットワークを形成。各文字は速度に応じてサイズと輝きが変化し、背景には浮遊するパーティクル。色相は位置に応じて変化し、回転やトレイル効果で動きが強調されます。クリック/タップで新しい文字を追加可能。全画面表示対応でモバイルからも快適に楽しめます。",
    "emoji": "🧲",
    "path": "artworks/magnetic-letters/index.html",
    "tags": ["HTML Canvas", "JavaScript", "Interactive", "Physics", "Generative Art", "Animation"],
    "date": datetime.now().strftime('%Y-%m-%d'),
    "featured": True,
    "python": False,
    "script": False,
    "audio": False
}

# Add to beginning (newest first)
data['artworks'].insert(0, new_artwork)

# Save
with open('artworks-manifest.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Added artwork: {new_artwork['title']}")
print(f"Total artworks: {len(data['artworks'])}")
