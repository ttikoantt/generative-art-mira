import json

# 既存のマニフェストを読み込む
with open('games-manifest.json', 'r', encoding='utf-8') as f:
    manifest = json.load(f)

# 新しいゲームを追加
new_game = {
    "id": "memory-match-2026-02-14-05",
    "title": "Memory Match - メモリマッチ",
    "description": "カードをめくって同じ絵柄のペアを探すシンプルで中毒性のあるメモリゲーム。4x4のグリッドに16枚のカード（8ペア）が配置され、1ターンに2枚ずつめくってペアを探します。8種類の絵文字（🎨🎭🎪🎯🎲🎸🎹🎺）が使われ、カードをめくると3Dフリップアニメーションで絵文字が表示されます。ペアが見つかるとカードがマッチングアニメーションで光り、全8ペアを見つけるとクリアで、スコア（移動回数、タイム）が記録されます。ハイスコアはローカルストレージに保存され、ベストタイムと最少移動回数を競います。美しいパープル系ネオングラデーション背景、グロー効果、マッチング時の視覚的フィードバック（パルスアニメーション）付き。全画面表示対応で、大きなタップエリアでモバイルからも快適に遊べます。",
    "emoji": "🎴",
    "path": "games/memory-match/index.html",
    "tags": [
        "HTML",
        "JavaScript",
        "Game",
        "Memory",
        "Puzzle",
        "Interactive",
        "Emoji"
    ],
    "date": "2026-02-14",
    "featured": True,
    "python": False,
    "script": False,
    "audio": False
}

# 新しいゲームをマニフェストの先頭に追加
manifest["games"] = [new_game] + manifest["games"]

# マニフェストを保存
with open('games-manifest.json', 'w', encoding='utf-8') as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print("✅ games-manifest.json を更新しました！")
