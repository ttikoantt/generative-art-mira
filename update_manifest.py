#!/usr/bin/env python3
import json
from datetime import datetime

# マニフェストファイルを読み込み
with open('artworks-manifest.json', 'r', encoding='utf-8') as f:
    manifest = json.load(f)

# 新しい作品を追加
new_artworks = [
    {
        "id": "magic-waves-2026-02-15-17",
        "title": "Magic Waves - マジックウェーブ",
        "description": "複数の波が干渉して美しいパターンを生成するインタラクティブアート。クリック/タップで新しい波の中心を追加でき、最大10個まで波が重なります。各波は独自の振幅、周波数、位相、速度、色相（HSL）を持ち、時間とともに動的に変化します。波同士が干渉して美しい色彩パターンを形成し、各波の中心点はグロー効果で輝きます。オートモードでは2秒ごとに自動的に新しい波が生成され、クリアボタンですべての波を消去。ランダム生成ボタンで3-5個の波がランダムな位置に生成。全画面表示対応で、モバイルからも快適に楽しめます。",
        "emoji": "🌊",
        "path": "artworks/magic-waves/index.html",
        "tags": [
            "HTML Canvas",
            "JavaScript",
            "Wave Interference",
            "Interactive",
            "Generative Art",
            "Animation",
            "Physics"
        ],
        "date": "2026-02-15",
        "featured": True,
        "python": False,
        "script": False,
        "audio": False
    }
]

# 既存のsliding-puzzleがあれば更新、なければ追加
sliding_puzzle_exists = False
for artwork in manifest['artworks']:
    if artwork['id'] == 'sliding-puzzle-2026-02-14-01':
        # 既存のものを更新
        artwork.update({
            "title": "Sliding Puzzle - 15パズル（新版）",
            "description": "4x4のグリッドで数字を並べ替えるクラシックなパズルゲーム。15個のタイルと1つの空白スペースがあり、タップ/クリックで隣接するタイルを空白スペースに移動させて数字を順番（1-15）に並べます。逆移動で必ず解ける状態（ソルバブル）のみを生成し、移動回数とタイムをリアルタイムで計測。クリア時には移動回数とタイムを表示する祝賀メッセージが表示されます。美しいパープル系ネオングラデーション背景、グロー効果、タイルのホバー効果、正しい位置のタイルがグリーンでハイライトされるビジュアルフィードバック。全画面表示対応で、大きなタップエリアでモバイルからも快適に遊べます。",
            "path": "games/sliding-puzzle/index.html"
        })
        sliding_puzzle_exists = True
        break

if not sliding_puzzle_exists:
    # 新規追加
    new_artworks.append({
        "id": "sliding-puzzle-2026-02-15-17",
        "title": "Sliding Puzzle - 15パズル",
        "description": "4x4のグリッドで数字を並べ替えるクラシックなパズルゲーム。15個のタイルと1つの空白スペースがあり、タップ/クリックで隣接するタイルを空白スペースに移動させて数字を順番（1-15）に並べます。逆移動で必ず解ける状態（ソルバブル）のみを生成し、移動回数とタイムをリアルタイムで計測。クリア時には移動回数とタイムを表示する祝賀メッセージが表示されます。美しいパープル系ネオングラデーション背景、グロー効果、タイルのホバー効果、正しい位置のタイルがグリーンでハイライトされるビジュアルフィードバック。全画面表示対応で、大きなタップエリアでモバイルからも快適に遊べます。",
        "emoji": "🧩",
        "path": "games/sliding-puzzle/index.html",
        "tags": [
            "HTML",
            "JavaScript",
            "Game",
            "Puzzle",
            "15 Puzzle",
            "Brain Training",
            "Interactive"
        ],
        "date": "2026-02-15",
        "featured": True,
        "python": False,
        "script": False,
        "audio": False
    })

# 新しい作品をマニフェストの先頭に追加
manifest['artworks'] = new_artworks + manifest['artworks']

# 統計を更新
manifest['stats']['total'] = len(manifest['artworks'])
manifest['lastUpdated'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# マニフェストファイルを書き込み
with open('artworks-manifest.json', 'w', encoding='utf-8') as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"マニフェストを更新しました！")
print(f"総作品数: {manifest['stats']['total']}")
