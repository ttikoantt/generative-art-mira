#!/usr/bin/env python3
import json

# マニフェストを読み込み
with open('artworks-manifest.json', 'r') as f:
    manifest = json.load(f)

# 新しい作品を追加
new_artworks = [
    {
        "id": "fractal-garden-2026-02-13-04",
        "title": "Fractal Garden - フラクタルガーデン",
        "description": "再帰的な分岐構造で植物のようなフラクタルを生成するインタラクティブアート。3種類の分岐バリエーション（広がり型・対称型・非対称型）が自然な植物の成長を表現し、各植物は独自のカラーパレット（3種類の美しい配色）を持つ。クリック/タッチで種を植えると新しい植物が成長し始め、枝が伸びるアニメーションで生命感を表現。成長が完了すると枝先に花が咲き、グロー効果で幻想的に輝く。Clearボタンで庭をリセットし、Auto Growボタンで自動的に種が植えられる。色相は時間とともに変化し続け、半透明のオーバーレイで美しいトレイル効果を描く。全画面表示対応で、モバイルからも快適に楽しめます。",
        "emoji": "🌿",
        "path": "artworks/fractal-garden.html",
        "tags": [
            "HTML Canvas",
            "JavaScript",
            "Fractal",
            "Generative Art",
            "Interactive",
            "Animation",
            "Plants"
        ],
        "date": "2026-02-13",
        "featured": True,
        "python": False,
        "script": False,
        "audio": False
    },
    {
        "id": "pattern-match-2026-02-13-04",
        "title": "Pattern Match - パターンマッチ",
        "description": "一瞬表示されるパターンを記憶して、同じパターンを再現するシンプルな記憶ゲーム。3つの難易度（Easy 3x3 / Normal 4x4 / Hard 5x5）から選択可能。ゲーム開始時にパターンが表示され、その後隠されるので記憶して同じタイルをタップします。レベルが進むにつれてパターンの数が増加（最大2倍グリッドサイズ）。ライフシステム（3つ）で間違えるとライフ減少、0でゲームオーバー。正解でレベルアップとスコア獲得（レベル×100ポイント）。間違えると正解パターンが表示され、次のレベルへ進む。ハイスコアはローカルストレージに保存され、現在のレベル・スコア・ライフをリアルタイム表示。美しいパープル系ネオングラデーション背景、パルスアニメーション、マッチング時のエフェクト付き。全画面表示対応で、モバイルからも快適に遊べます。",
        "emoji": "🎴",
        "path": "games/pattern-match/index.html",
        "tags": [
            "HTML",
            "JavaScript",
            "Game",
            "Memory",
            "Puzzle",
            "Pattern",
            "Interactive"
        ],
        "date": "2026-02-13",
        "featured": True,
        "python": False,
        "script": False,
        "audio": False
    }
]

# 作品を追加
manifest['artworks'].extend(new_artworks)

# マニフェストを保存
with open('artworks-manifest.json', 'w') as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"✅ {len(new_artworks)}作品を追加しました！")
print(f"総作品数: {len(manifest['artworks'])}作品")
