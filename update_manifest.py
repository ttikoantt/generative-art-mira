import json

# 既存のマニフェストを読み込む
with open('artworks-manifest.json', 'r', encoding='utf-8') as f:
    manifest = json.load(f)

# 新しい作品を追加
new_artworks = [
    {
        "id": "particle-flow-2026-02-14-05",
        "title": "Particle Flow - パーティクルフロー",
        "description": "3000個のパーティクルが美しく流れるインタラクティブアート。マウス/タッチ操作でパーティクルが引き寄せられ、クリックで4種類のカラースキームが切り替わります。各パーティクルは独自のサイズ、速度、色相を持ち、有機的に流れる動きを形成。マウスの影響範囲内でパーティクルが加速し、トレイル効果（半透明の残像）で幻想的な光の軌跡を描きます。画面サイズに応じてパーティクル数が自動調整され、全画面表示対応でモバイルからも快適に楽しめます。",
        "emoji": "✨",
        "path": "particle-flow.html",
        "tags": [
            "HTML Canvas",
            "JavaScript",
            "Particles",
            "Interactive",
            "Generative Art",
            "Animation"
        ],
        "date": "2026-02-14",
        "featured": True,
        "python": False,
        "script": False,
        "audio": False
    }
]

# 新しい作品をマニフェストの先頭に追加
manifest["artworks"] = new_artworks + manifest["artworks"]

# マニフェストを保存
with open('artworks-manifest.json', 'w', encoding='utf-8') as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print("✅ artworks-manifest.json を更新しました！")
