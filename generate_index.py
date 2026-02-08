#!/usr/bin/env python3
"""
Generate index.html from artworks-manifest.json and games-manifest.json
"""
import json
from datetime import datetime

def generate_index():
    # Load manifests
    with open('artworks-manifest.json', 'r') as f:
        artworks_data = json.load(f)

    with open('games-manifest.json', 'r') as f:
        games_data = json.load(f)

    artworks = artworks_data['artworks']
    games = games_data['games']

    # Generate HTML
    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mira's Generative Art Gallery</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
            color: white;
        }}

        .container {{
            max-width: 1400px;
            margin: 0 auto;
        }}

        h1 {{
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}

        .subtitle {{
            text-align: center;
            font-size: 1.1rem;
            margin-bottom: 30px;
            opacity: 0.9;
        }}

        .nav {{
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 30px;
        }}

        .nav a {{
            background: rgba(255,255,255,0.2);
            color: white;
            text-decoration: none;
            padding: 12px 30px;
            border-radius: 25px;
            font-weight: bold;
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
        }}

        .nav a:hover {{
            background: rgba(255,255,255,0.3);
            transform: translateY(-2px);
        }}

        .stats {{
            text-align: center;
            margin-bottom: 30px;
            font-size: 1.1rem;
            opacity: 0.9;
        }}

        .section {{
            background: rgba(255,255,255,0.1);
            border-radius: 20px;
            padding: 30px;
            margin-bottom: 30px;
            backdrop-filter: blur(10px);
        }}

        .section h2 {{
            font-size: 1.8rem;
            margin-bottom: 20px;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
        }}

        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 20px;
        }}

        .card {{
            background: rgba(255,255,255,0.15);
            border-radius: 15px;
            padding: 20px;
            transition: all 0.3s ease;
            cursor: pointer;
            text-decoration: none;
            color: white;
            display: block;
        }}

        .card:hover {{
            background: rgba(255,255,255,0.25);
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }}

        .card-header {{
            display: flex;
            align-items: center;
            margin-bottom: 10px;
        }}

        .card-emoji {{
            font-size: 2rem;
            margin-right: 10px;
        }}

        .card-title {{
            font-size: 1.1rem;
            font-weight: bold;
        }}

        .card-description {{
            font-size: 0.9rem;
            opacity: 0.9;
            margin-bottom: 15px;
            line-height: 1.5;
        }}

        .card-tags {{
            display: flex;
            flex-wrap: wrap;
            gap: 5px;
        }}

        .tag {{
            background: rgba(255,255,255,0.2);
            padding: 4px 10px;
            border-radius: 10px;
            font-size: 0.75rem;
        }}

        .card-date {{
            font-size: 0.8rem;
            opacity: 0.7;
            margin-top: 10px;
        }}

        .featured {{
            border: 2px solid rgba(255,255,255,0.5);
        }}

        @media (max-width: 768px) {{
            .grid {{
                grid-template-columns: 1fr;
            }}

            h1 {{
                font-size: 1.8rem;
            }}

            .nav {{
                flex-direction: column;
                align-items: center;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🎨 Mira's Generative Art Gallery</h1>
        <p class="subtitle">クリエイティブで美しいアートとゲームのコレクション</p>

        <div class="nav">
            <a href="#artworks">🎨 アート作品 ({len(artworks)})</a>
            <a href="#games">🎮 ゲーム ({len(games)})</a>
        </div>

        <div class="stats">
            <p>📊 総作品数: {len(artworks) + len(games)} 作品 | 最終更新: {datetime.now().strftime('%Y年%m月%d日')}</p>
        </div>

        <section id="artworks" class="section">
            <h2>🎨 アート作品</h2>
            <div class="grid">
"""

    # Add artwork cards
    for artwork in artworks[:50]:  # Limit to 50 to keep page size reasonable
        featured_class = 'featured' if artwork.get('featured', False) else ''
        tags_html = ''.join([f'<span class="tag">{tag}</span>' for tag in artwork.get('tags', [])[:5]])

        html += f"""
                <a href="{artwork['path']}" class="card {featured_class}">
                    <div class="card-header">
                        <span class="card-emoji">{artwork.get('emoji', '🎨')}</span>
                        <span class="card-title">{artwork['title']}</span>
                    </div>
                    <div class="card-description">{artwork['description'][:100]}...</div>
                    <div class="card-tags">{tags_html}</div>
                    <div class="card-date">{artwork.get('date', 'N/A')}</div>
                </a>
"""

    html += """
            </div>
        </section>

        <section id="games" class="section">
            <h2>🎮 ゲーム</h2>
            <div class="grid">
"""

    # Add game cards
    for game in games:
        featured_class = 'featured' if game.get('featured', False) else ''
        tags_html = ''.join([f'<span class="tag">{tag}</span>' for tag in game.get('tags', [])[:5]])

        html += f"""
                <a href="{game['path']}" class="card {featured_class}">
                    <div class="card-header">
                        <span class="card-emoji">{game.get('emoji', '🎮')}</span>
                        <span class="card-title">{game['title']}</span>
                    </div>
                    <div class="card-description">{game['description'][:100]}...</div>
                    <div class="card-tags">{tags_html}</div>
                    <div class="card-date">{game.get('date', 'N/A')}</div>
                </a>
"""

    html += """
            </div>
        </section>

        <footer style="text-align: center; margin-top: 50px; opacity: 0.8;">
            <p>✨ Created by Mira | Generative Art & Games ✨</p>
        </footer>
    </div>
</body>
</html>
"""

    # Write index.html
    with open('index.html', 'w') as f:
        f.write(html)

    print(f"✅ Generated index.html")
    print(f"   - {len(artworks)} artworks")
    print(f"   - {len(games)} games")
    print(f"   - Total: {len(artworks) + len(games)} items")

if __name__ == '__main__':
    generate_index()
