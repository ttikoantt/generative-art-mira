#!/usr/bin/env python3
import json

# マニフェストを読み込む
with open('artworks-manifest.json', 'r', encoding='utf-8') as f:
    manifest = json.load(f)

# 新しいクリエイティブ作品
new_artwork = {
    "id": "particle-flow-art-2026-02-11-03",
    "title": "Particle Flow Art - パーティクルフローアート",
    "description": "150個のパーティクルが美しく流れ、近い粒子同士が線で繋がるインタラクティブアート。マウス移動でパーティクルが避け、クリック/タッチでパーティクルが引き寄せられる引力システム。7種類のネオンカラー（ピンク、シアン、イエロー、パープル、ブルー、オレンジ、グリーン）が輝き、各パーティクルはグロー効果で周囲を照らす。色相は時間とともに変化し続け、トレイル効果で幻想的な光の軌跡を描く。全画面表示対応で、モバイルからも快適に楽しめます。",
    "emoji": "✨",
    "path": "artworks/particle-flow-art.html",
    "tags": [
        "HTML Canvas",
        "JavaScript",
        "Particles",
        "Interactive",
        "Generative Art",
        "Animation"
    ],
    "date": "2026-02-11",
    "featured": True,
    "python": False,
    "script": False,
    "audio": False
}

# 新しいゲーム
new_game = {
    "id": "falling-blocks-2026-02-11-03",
    "title": "Falling Blocks - フォーリングブロックス",
    "description": "クラシックなテトリス風のブロック落としゲーム。7種類のテトリミノ（I、O、T、S、Z、J、L）が落ちてきて、行を埋めると消えてスコア獲得。矢印キーまたはWASDで操作し、ハードドロップ（スペースキー）で素早く落下。一度に複数行消しでボーナスポイント。美しいネオングラデーション背景、次のピースプレビュー、スコア表示、一時停止機能付き。モバイルではタッチコントロールボタンに対応。全画面表示対応で、どこからでも快適に遊べます。",
    "emoji": "🧱",
    "path": "games/falling-blocks/index.html",
    "tags": [
        "HTML",
        "JavaScript",
        "Game",
        "Tetris",
        "Puzzle",
        "Interactive"
    ],
    "date": "2026-02-11",
    "featured": True,
    "python": False,
    "script": False,
    "audio": False
}

# 新しい作品を配列の先頭に追加
manifest['artworks'].insert(0, new_artwork)
manifest['artworks'].insert(1, new_game)

# 更新したマニフェストを保存
with open('artworks-manifest.json', 'w', encoding='utf-8') as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"✅ マニフェストを更新しました！")
print(f"📊 総作品数: {len(manifest['artworks'])}作品")
