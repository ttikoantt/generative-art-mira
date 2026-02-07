#!/usr/bin/env python3
import json
from datetime import datetime

# Update artworks manifest
with open('artworks-manifest.json', 'r') as f:
    artworks_data = json.load(f)

new_artwork = {
    "id": "lissajous-art",
    "title": "Lissajous Art - リサージュ図形",
    "description": "正弦波を組み合わせて美しい曲線を描くインタラクティブアート。x = sin(A·t), y = sin(B·t) という数式から生まれる複雑で美しい図形。周波数A・B、位相、速度をリアルタイムで調整可能。複数のレイヤーが重なり合い、時間とともに形が変化する。マウス/タッチで動きを変化させ、Randomizeボタンで新しいパターンを生成。全画面表示対応で、モバイルからも快適に楽しめます。",
    "emoji": "🌀",
    "path": "artworks/lissajous-art.html",
    "tags": [
        "HTML Canvas",
        "JavaScript",
        "Lissajous",
        "Generative Art",
        "Interactive",
        "Mathematics"
    ],
    "date": "2026-02-08",
    "featured": True,
    "python": False,
    "script": False,
    "audio": False
}

artworks_data["artworks"].insert(0, new_artwork)

with open('artworks-manifest.json', 'w') as f:
    json.dump(artworks_data, f, indent=2, ensure_ascii=False)

print(f"Updated artworks manifest: {len(artworks_data['artworks'])} artworks")

# Update games manifest
with open('games-manifest.json', 'r') as f:
    games_data = json.load(f)

new_game = {
    "id": "helix-jump",
    "title": "Helix Jump - ヘリックスジャンプ",
    "description": "回転する螺旋プラットフォームでボールを落下させるゲーム。マウスドラッグまたはタッチスワイプで塔を回転させ、隙間を見つけてボールを通過させよう。赤い危険ゾーンに触れるとゲームオーバー！スコアシステム、ベストスコア記録（ローカルストレージ）、美しい粒子エフェクトとトレイルアニメーション。全画面表示対応で、モバイルのタッチ操作にも完全対応しています。",
    "emoji": "🌀",
    "path": "games/helix-jump/index.html",
    "tags": [
        "HTML5 Game",
        "Action",
        "Rotation",
        "Mouse Controls",
        "Touch Controls",
        "Helix Jump"
    ],
    "date": "2026-02-08",
    "featured": True
}

games_data["games"].insert(0, new_game)

with open('games-manifest.json', 'w') as f:
    json.dump(games_data, f, indent=2, ensure_ascii=False)

print(f"Updated games manifest: {len(games_data['games'])} games")
