#!/usr/bin/env python3
import json

# マニフェストを読み込む
with open('games-manifest.json', 'r', encoding='utf-8') as f:
    manifest = json.load(f)

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
    "mobile": True
}

# 新しいゲームを配列の先頭に追加
manifest['games'].insert(0, new_game)

# 更新したマニフェストを保存
with open('games-manifest.json', 'w', encoding='utf-8') as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"✅ ゲームマニフェストを更新しました！")
print(f"📊 総ゲーム数: {len(manifest['games'])}ゲーム")
