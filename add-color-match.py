#!/usr/bin/env python3
import json
from datetime import datetime

# マニフェストを読み込み
with open('artworks-manifest.json', 'r') as f:
    manifest = json.load(f)

# Color Matchを追加
new_artwork = {
    "id": "color-match",
    "title": "Color Match - 色判定ゲーム",
    "description": "ストループ効果を使った脳トレゲーム。色の名前と文字の色が一致しているか判定。60秒の制限時間でコンボシステム付き。全画面表示対応でモバイルからも快適に遊べます。10種類の色（赤、青、緑、黄、橙、紫、ピンク、シアン、茶、黒）で、正解でポイントとコンボ獲得。",
    "emoji": "🎨",
    "path": "games/color-match/index.html",
    "tags": [
        "HTML",
        "JavaScript",
        "Game",
        "Brain Training",
        "Interactive"
    ],
    "date": "2026-02-07",
    "featured": True,
    "python": False,
    "script": False,
    "audio": False
}

# artworksの最後に追加
manifest['artworks'].append(new_artwork)

# statsを更新
manifest['stats']['total'] = 70
manifest['stats']['html'] = 55
manifest['stats']['featured'] = 60

# lastUpdatedを更新
manifest['lastUpdated'] = datetime.now().isoformat() + 'Z'

# 保存
with open('artworks-manifest.json', 'w') as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

print("Color Matchをマニフェストに追加しました！")
print(f"総作品数: {manifest['stats']['total']}")
