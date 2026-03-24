#!/usr/bin/env python3
"""成果物をマニフェストに登録するスクリプト"""
import sys
sys.path.insert(0, '/Users/naokitomono/Documents/generative-art-by-mira')

from update_gallery import add_artwork, add_game
from datetime import datetime

now = datetime.now()

# クリエイティブ作品を追加
add_artwork(
    id='particle-flow-2026-03-25-01',
    title='Particle Flow',
    description='マウスに反応する有機的なパーティクルフロー。パーティクル同士が繋がり、美しい光の模様を描く。',
    emoji='✨',
    path='particle-flow/index.html',
    tags=['HTML Canvas', 'JavaScript', 'Particle System', 'Generative Art'],
    date=now.strftime('%Y-%m-%d')
)

# ゲームを追加
add_game(
    id='timing-hit-2026-03-25-01',
    title='Timing Hit',
    description='ターゲットが出現したらタイミングよくタップ！コンボを稼いで高得点を目指すシンプルなタイミングゲーム。',
    emoji='🎯',
    path='games/timing-hit/index.html',
    tags=['HTML', 'JavaScript', 'Game', 'Timing', 'Casual'],
    date=now.strftime('%Y-%m-%d')
)

print("✨ 成果物を登録しました！")
