import json

# 既存のマニフェストを読み込む
with open('artworks-manifest.json', 'r', encoding='utf-8') as f:
    manifest = json.load(f)

# 新しい作品を追加
new_artworks = [
    {
        "id": "geometric-waves-2026-02-14-06",
        "title": "Geometric Waves - ジオメトリックウェーブ",
        "description": "幾何学図形が波のようにリズミカルに動くインタラクティブアート。8x6のグリッドに三角形、四角形、五角形、六角形が配置され、各図形が独自の回転速度を持って回転します。マウスX位置でウェーブの振幅が変化し、クリックで新しいパターンが生成。4種類のカラースキーム（パープル、ターコイズ、オレンジ、バイオレット）から選択可能で、各図形は色相が時間とともに変化し続けます。トレイル効果（半透明の残像）で幻想的な光の軌跡を描き、全画面表示対応でモバイルからも快適に楽しめます。",
        "emoji": "🌊",
        "path": "geometric-waves.html",
        "tags": [
            "HTML Canvas",
            "JavaScript",
            "Geometric",
            "Interactive",
            "Generative Art",
            "Animation",
            "Waves"
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
