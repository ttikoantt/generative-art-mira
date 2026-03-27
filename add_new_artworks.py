#!/usr/bin/env python3
"""Add new artworks to manifest"""
import sys
sys.path.insert(0, '.')
import update_gallery
from datetime import datetime

now = datetime.now()

# クリエイティブ作品を追加
update_gallery.add_artwork(
    id='neon-rain',
    title='Neon Rain Generator',
    description='ネオン色の雨が降るインタラクティブアート。クリックやタッチで新しい雨粒を追加できます。',
    emoji='🌧️',
    path='neon-rain.html',
    tags=['HTML Canvas', 'JavaScript', 'Interactive Art'],
    date=now.strftime('%Y-%m-%d')
)

# ゲームを追加
update_gallery.add_game(
    id='dot-chaser',
    title='Dot Chaser',
    description='画面上の点をタップしてスコアを稼ぐシンプルな反応ゲーム。コンボシステムとパーティクルエフェクト付き。',
    emoji='🔴',
    path='games/dot-chaser/index.html',
    tags=['HTML', 'JavaScript', 'Game', 'Touch'],
    date=now.strftime('%Y-%m-%d')
)

print('作品をマニフェストに追加しました')
