#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime

# マニフェストファイルのパス
manifest_path = Path("/Users/naokitomono/Documents/generative-art-by-mira/artworks-manifest.json")

# 現在の日付
today = datetime.now().strftime("%Y-%m-%d")

# 新しい作品
new_artworks = [
    {
        "id": f"fractal-tree-animation-{today.replace('-', '-')}",
        "title": "Fractal Tree Animation - フラクタルツリーアニメーション",
        "description": "クリックするたびに成長するフラクタルツリーのインタラクティブアート。再帰的な枝分かれで自然な木を形成し、成長アニメーションで生命感を表現。各ツリーは独自のカラーパレット（5種類のグラデーション）を持ち、10-13層の深さで再帰的に生成。枝分かれ角度と長さの減衰率はランダムに決まり、毎回異なる木が咲きます。クリック/タッチで新しいツリーを生成でき、Auto Growモードで自動的に木が成長し続けます。各枝の端には葉が描かれ、深度に応じて色と太さが変化。グロー効果で幻想的に輝き、トレイル効果で成長プロセスを美しく表現。全画面表示対応で、モバイルからも快適に楽しめます。",
        "emoji": "🌳",
        "path": "fractal-tree/index.html",
        "tags": [
            "HTML Canvas",
            "JavaScript",
            "Fractal",
            "Trees",
            "Generative Art",
            "Interactive",
            "Animation"
        ],
        "date": today,
        "featured": True,
        "python": False,
        "script": False,
        "audio": False
    },
    {
        "id": f"color-match-game-{today.replace('-', '-')}",
        "title": "Color Match - カラーマッチゲーム",
        "description": "色の名前と実際の色が一致しているかを判定するシンプルで中毒性のある脳トレゲーム。8種類の色（RED、BLUE、GREEN、YELLOW、PURPLE、ORANGE、PINK、CYAN）が表示され、文字と色が一致しているかを素早く判断します。60秒の制限時間で、正解するとポイント+コンボボーナス、不正解すると-20pt。制限時間が残り10秒を切るとタイマーバーが赤く変化。ハイスコアはローカルストレージに保存され、コンボシステムで連続正解時にボーナスポイントを獲得。美しいパープル系ネオングラデーション背景、グロー効果、正解/不正解時のビジュアルフィードバック付き。全画面表示対応で、キーボード（矢印キー/WASD）とマウス/タッチ両対応でモバイルからも快適に遊べます。",
        "emoji": "🎨",
        "path": "games/color-match/index.html",
        "tags": [
            "HTML",
            "JavaScript",
            "Game",
            "Color",
            "Reflex",
            "Brain Training",
            "Stroop Effect",
            "Interactive"
        ],
        "date": today,
        "featured": True,
        "python": False,
        "script": False,
        "audio": False
    }
]

# マニフェストを読み込む
with open(manifest_path, 'r', encoding='utf-8') as f:
    manifest = json.load(f)

# 新しい作品を追加（先頭に追加）
for artwork in reversed(new_artworks):
    manifest['artworks'].insert(0, artwork)

# マニフェストを保存
with open(manifest_path, 'w', encoding='utf-8') as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"✅ {len(new_artworks)}個の新しい作品をマニフェストに追加しました！")
