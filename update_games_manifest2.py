import json

# 既存のマニフェストを読み込む
with open('games-manifest.json', 'r', encoding='utf-8') as f:
    manifest = json.load(f)

# 新しいゲームを追加
new_game = {
    "id": "speed-tap-2026-02-14-06",
    "title": "Speed Tap - スピードタップ",
    "description": "3x3のグリッドでターゲットを素早くタップするシンプルで中毒性のある反応速度ゲーム。30秒の制限時間で、ピンク色のターゲットをタップしてスコアを稼ぎます。正解すると10ポイント+コンボボーナス（コンボ数×2ポイント）を獲得し、連続ヒットでコンボが増加。コンボ3以上で画面中央にコンボ数が表示され、スコアに応じてターゲットの移動間隔が短縮されて難易度が上昇。ハイスコアはローカルストレージに保存され、最大コンボ数も記録。美しいパープル系ネオングラデーション背景、ターゲットのパルスアニメーション、クリック時のポップエフェクト、コンボ表示のポップアップアニメーション付き。全画面表示対応で、大きなタップエリアでモバイルからも快適に遊べます。",
    "emoji": "⚡",
    "path": "games/speed-tap/index.html",
    "tags": [
        "HTML",
        "JavaScript",
        "Game",
        "Speed",
        "Reflex",
        "Interactive",
        "Combo System"
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
