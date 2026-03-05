#!/usr/bin/env python3
import sys
sys.path.insert(0, '/Users/naokitomono/Documents/generative-art-by-mira')
from update_gallery import add_artwork, add_game
from datetime import datetime

now = datetime.now()
hour_id = now.strftime('%Y-%m-%d-%H')

# クリエイティブ作品を追加
add_artwork(
    id=f'noise-flow-art-{hour_id}',
    title='Noise Flow Art',
    description='Perlin Noise風のアルゴリズムで有機的なパターンを生成するジェネレーティブアート。クリックで新規生成、スクロールでズーム調整が可能。5種類のカラースキームを搭載。',
    emoji='🌊',
    path='noise-flow-art.html',
    tags=['HTML Canvas', 'JavaScript', 'Generative Art', 'Noise'],
    date=now.strftime('%Y-%m-%d')
)

# ゲームを追加
add_game(
    id=f'falling-blocks-{hour_id}',
    title='Falling Blocks',
    description='シンプルで中毒性のある落ちゲー（テトリス風）。矢印キーまたはボタンで操作。ライン消去でスコア獲得。モバイル対応。',
    emoji='🎮',
    path='games/falling-blocks/index.html',
    tags=['HTML', 'JavaScript', 'Game', 'Tetris', 'Falling Blocks'],
    date=now.strftime('%Y-%m-%d')
)

print(f"✅ 作品を登録しました: {hour_id}")
