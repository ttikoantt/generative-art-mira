import sys
sys.path.insert(0, '.')
from update_gallery import add_artwork, add_game
from datetime import datetime

now = datetime.now()

# クリエイティブ作品を追加
add_artwork(
    id='galaxy-spiral-art',
    title='Galaxy Spiral Art',
    description='銀河のような螺旋状の粒子アート。中央から放射状に広がる粒子が、美しい螺旋パターンを描く。クリックで新しい銀河を生成。',
    emoji='🌌',
    path='galaxy-spiral-art.html',
    tags=['HTML Canvas', 'JavaScript', 'Particle System'],
    date=now.strftime('%Y-%m-%d')
)

# ゲームを追加
add_game(
    id='tap-dash',
    title='Tap Dash',
    description='タップしてプレイヤーがダッシュするシンプルなアクションゲーム。障害物を避けながら、できるだけ遠くまで進む。ネオンスタイリング。',
    emoji='🏃',
    path='games/tap-dash/index.html',
    tags=['HTML', 'JavaScript', 'Game', 'Action'],
    date=now.strftime('%Y-%m-%d')
)

print("✅ Added artworks to manifest")
