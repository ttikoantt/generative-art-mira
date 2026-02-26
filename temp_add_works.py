#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')
from update_gallery import add_artwork, add_game
from datetime import datetime

now = datetime.now()
hour_id = now.strftime('%Y-%m-%d-%H')

# クリエイティブ作品を追加
add_artwork(
    id=f'fractal-tree-{hour_id}',
    title='Fractal Tree',
    description='再帰的なフラクタルパターンで美しい木の構造を生成。アニメーション付きで、複数の配色パターンを切り替え可能。',
    emoji='🌳',
    path='fractal-tree.html',
    tags=['HTML Canvas', 'JavaScript', 'Fractal', 'Generative Art'],
    date=now.strftime('%Y-%m-%d')
)

# ゲームを追加
add_game(
    id=f'dot-catcher-{hour_id}',
    title='Dot Catcher',
    description='現れる点をクリックしてキャッチ！30秒間でハイスコアを目指す。コンボシステムとサイズによるポイント差。',
    emoji='🎯',
    path='games/dot-catcher/index.html',
    tags=['HTML', 'JavaScript', 'Game', 'Reflex'],
    date=now.strftime('%Y-%m-%d')
)

print('作品をマニフェストに追加完了')
