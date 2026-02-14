#!/usr/bin/env python3
import json
from pathlib import Path

# マニフェストのパス
manifest_path = Path("artworks-manifest.json")

# マニフェストを読み込む
with open(manifest_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# 新しい作品
new_artworks = [
    {
        "id": "grid-sums-2026-02-15-02",
        "title": "Grid Sums - 数字パズル",
        "description": "5x5のグリッド上の数字を選んで目標値を作るシンプルで中毒性のあるパズルゲーム。1〜9の数字がランダムに配置され、目標値（ラウンドに応じて難易度上昇）を超えないように数字を選んで合計を目標値に合わせます。正解するとコンボボーナスとラウンドボーナスを獲得し、使用した数字は消去されます。全数字を使い切ると次のラウンドへ進行し、ラウンドが上がるほど目標値が高くなる。コンボシステムで連続正解時にボーナスポイント（最大+50pt）を獲得し、現在の合計がリアルタイムで表示される。美しいパープル系ネオングラデーション背景、グロー効果、選択したセルがパルスアニメーションでハイライトされるビジュアルフィードバック。全画面表示対応で、モバイルからも快適に遊べます。",
        "emoji": "🔢",
        "path": "games/grid-sums/index.html",
        "tags": [
            "HTML",
            "JavaScript",
            "Game",
            "Puzzle",
            "Math",
            "Brain Training",
            "Interactive",
            "Neon Design"
        ],
        "date": "2026-02-15",
        "featured": True,
        "python": False,
        "script": False,
        "audio": False
    },
    {
        "id": "quantum-entanglement-2026-02-15-01",
        "title": "Quantum Entanglement - 量子もつれの可視化",
        "description": "量子物理学の「量子もつれ」現象をインタラクティブに可視化するアート作品。6対（12個）の量子粒子が互いに量子もつれを起こし、離れていても互いの状態に影響を与え合います。各粒子は量子スピンを持ち、もつれたペアは波打つ線で繋がれて視覚的に表現されます。マウス/タッチ操作で「観測者効果」を再現でき、観測すると量子コヒーレンスが低下してデコヒーレンス（量子の重ね合わせが壊れる現象）が発生。3つのボタン（もつれ強化・デコヒーレンス・リセット）で量子状態を操作可能。量子場の背景効果と各粒子のグロー効果で幻想的な雰囲気を演出。ネオンカラー（ターコイズ系）で統一されたおしゃれなデザイン。全画面表示対応で、モバイルからも快適に楽しめます。",
        "emoji": "⚛️",
        "path": "artworks/quantum-entanglement.html",
        "tags": [
            "HTML Canvas",
            "JavaScript",
            "Quantum Physics",
            "Interactive",
            "Generative Art",
            "Animation",
            "Science Visualization"
        ],
        "date": "2026-02-15",
        "featured": True,
        "python": False,
        "script": False,
        "audio": False
    }
]

# 新しい作品を先頭に挿入
data["artworks"] = new_artworks + data["artworks"]

# マニフェストを保存
with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ Added 2 new artworks to manifest")
