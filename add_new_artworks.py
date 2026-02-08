#!/usr/bin/env python3
import json
from datetime import datetime

# Load manifest
with open('artworks-manifest.json', 'r', encoding='utf-8') as f:
    manifest = json.load(f)

# New creative artwork
particle_aurora = {
    "id": "particle-aurora",
    "title": "Particle Aurora - パーティクル・オーロラ",
    "description": "オーロラのように美しく舞うパーティクルアート。250個の粒子が波のように有機的に動き、4種類のカラーパターン（Aurora、Sunset、Ocean、Fire）を切り替え可能。マウス/タッチ操作でパーティクルを誘導し、クリックで爆発エフェクトを発生。近くのパーティクル同士が線で繋がり、幻想的な光のネットワークを形成。滑らかなアニメーションと美しいグラデーションで、全画面表示対応でモバイルからも快適に楽しめます。",
    "emoji": "✨",
    "path": "artworks/particle-aurora/index.html",
    "tags": [
        "HTML Canvas",
        "JavaScript",
        "Particles",
        "Aurora",
        "Generative Art",
        "Interactive",
        "Animation"
    ],
    "date": "2026-02-08",
    "featured": True,
    "python": False,
    "script": False,
    "audio": False
}

# New game
reaction_rush = {
    "id": "reaction-rush",
    "title": "Reaction Rush - 反応スピードゲーム",
    "description": "3x3のグリッドでターゲットを素早くタップする反応速度ゲーム。30秒の制限時間でスコアを競い、連続ヒットでストリークボーナスを獲得。スコアに応じて出現速度が上昇し、ハイスコアはローカルストレージに保存。美しいグラデーションデザイン、アニメーション効果（パルス、ポップイン、シェイク）、モバイル対応で快適に遊べます。",
    "emoji": "⚡",
    "path": "games/reaction-rush/index.html",
    "tags": [
        "HTML",
        "JavaScript",
        "Game",
        "Reaction",
        "Speed",
        "Interactive"
    ],
    "date": "2026-02-08",
    "featured": True,
    "python": False,
    "script": False,
    "audio": False
}

# Add to beginning of list
manifest["artworks"].insert(0, particle_aurora)
manifest["artworks"].insert(1, reaction_rush)

# Update stats
manifest["stats"]["total"] = len(manifest["artworks"])
manifest["stats"]["html"] = sum(1 for art in manifest["artworks"] if not art.get("python", False) and not art.get("script", False))
manifest["stats"]["python"] = sum(1 for art in manifest["artworks"] if art.get("python", False))
manifest["stats"]["javascript"] = sum(1 for art in manifest["artworks"] if art.get("script", False))
manifest["stats"]["featured"] = sum(1 for art in manifest["artworks"] if art.get("featured", False))
manifest["stats"]["script"] = sum(1 for art in manifest["artworks"] if art.get("script", False))

# Update timestamp
manifest["lastUpdated"] = datetime.utcnow().isoformat() + "+00:00"

# Save manifest
with open('artworks-manifest.json', 'w', encoding='utf-8') as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print("✅ Added 2 new artworks to manifest")
print(f"Total artworks: {manifest['stats']['total']}")
print(f"  HTML: {manifest['stats']['html']}")
print(f"  Python: {manifest['stats']['python']}")
print(f"  JavaScript: {manifest['stats']['javascript']}")
print(f"  Featured: {manifest['stats']['featured']}")
