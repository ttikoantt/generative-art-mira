#!/usr/bin/env python3
"""
Generate new index.html with curated top works by category
"""
import json
from pathlib import Path

def categorize_artworks(artworks, limit=500):
    """Categorize artworks by tags"""
    categories = {
        'Particles': ['Particle', 'particle', 'Particles'],
        'Fractal': ['Fractal', 'fractal'],
        'Geometric': ['Geometric', 'geometric', 'Geometry', 'geometry'],
        'Wave': ['Wave', 'wave', 'Flow', 'flow', 'Ripple', 'ripple'],
        'Audio': ['Audio', 'audio', 'Sound', 'sound', 'Music', 'music'],
        'ASCII': ['ASCII', 'ascii'],
        'Nature': ['Nature', 'nature', 'Sakura', 'sakura', 'Cherry', 'Firefly', 'firefly'],
        'Cosmic': ['Cosmic', 'cosmic', 'Space', 'space', 'Galaxy', 'galaxy', 'Star', 'star'],
        'Interactive': ['Interactive', 'interactive'],
        'Experimental': ['Experimental', 'experimental', 'Quantum', 'quantum']
    }
    
    by_category = {}
    for cat, keywords in categories.items():
        by_category[cat] = []
    
    for art in artworks[:limit]:
        for cat, keywords in categories.items():
            for tag in art.get('tags', []):
                for keyword in keywords:
                    if keyword.lower() in tag.lower():
                        by_category[cat].append(art)
                        break
                if art in by_category[cat]:
                    break
    
    # Top 3 per category
    top_by_category = {}
    for cat, arts in by_category.items():
        if len(arts) >= 3:
            top3 = sorted(arts, key=lambda x: (x.get('featured', False), x['date']), reverse=True)[:3]
            top_by_category[cat] = top3
    
    return top_by_category

def categorize_games(games, limit=500):
    """Categorize games by tags"""
    categories = {
        'Puzzle': ['Puzzle', 'puzzle', 'Memory', 'memory'],
        'Action': ['Action', 'action', 'Runner', 'runner', 'Dodge', 'dodge'],
        'Reaction': ['Reaction', 'reaction', 'Speed', 'speed', 'Tap', 'tap'],
        'Rhythm': ['Rhythm', 'rhythm'],
        'Arcade': ['Arcade', 'arcade'],
        'Casual': ['Casual', 'casual'],
        'Creative': ['Creative', 'creative', 'Art', 'art']
    }
    
    by_category = {}
    for cat, keywords in categories.items():
        by_category[cat] = []
    
    for game in games[:limit]:
        for cat, keywords in categories.items():
            for tag in game.get('tags', []):
                for keyword in keywords:
                    if keyword.lower() in tag.lower():
                        by_category[cat].append(game)
                        break
                if game in by_category[cat]:
                    break
    
    # Top 3 per category
    top_by_category = {}
    for cat, games_list in by_category.items():
        if len(games_list) >= 3:
            top3 = sorted(games_list, key=lambda x: (x.get('featured', False), x['date']), reverse=True)[:3]
            top_by_category[cat] = top3
    
    return top_by_category

def generate_new_index():
    """Generate new curated index.html"""
    
    # Load manifests
    with open('artworks-manifest.json', 'r') as f:
        artworks_data = json.load(f)
    
    with open('games-manifest.json', 'r') as f:
        games_data = json.load(f)
    
    artworks = artworks_data['artworks']
    games = games_data['games']
    
    # Categorize
    artwork_categories = categorize_artworks(artworks)
    game_categories = categorize_games(games)
    
    # Generate HTML
    html = """<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mira's Generative Art & Games Gallery</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            min-height: 100vh;
            color: #eee;
            line-height: 1.6;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }

        /* Header */
        .hero {
            text-align: center;
            padding: 60px 20px;
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.2) 0%, rgba(118, 75, 162, 0.2) 100%);
            border-radius: 20px;
            margin-bottom: 40px;
        }

        .hero h1 {
            font-size: clamp(2rem, 5vw, 3.5rem);
            margin-bottom: 15px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .hero p {
            font-size: clamp(1rem, 2vw, 1.3rem);
            opacity: 0.9;
            margin-bottom: 20px;
        }

        .stats {
            display: flex;
            justify-content: center;
            gap: 30px;
            flex-wrap: wrap;
            margin-top: 30px;
        }

        .stat-item {
            background: rgba(255, 255, 255, 0.1);
            padding: 15px 30px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
        }

        .stat-number {
            font-size: 2rem;
            font-weight: bold;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .stat-label {
            font-size: 0.9rem;
            opacity: 0.8;
        }

        /* Search */
        .search-container {
            margin-bottom: 40px;
        }

        .search-box {
            position: relative;
            max-width: 600px;
            margin: 0 auto;
        }

        .search-box input {
            width: 100%;
            padding: 18px 50px 18px 25px;
            font-size: 1.1rem;
            border: 2px solid rgba(255, 255, 255, 0.1);
            border-radius: 50px;
            background: rgba(255, 255, 255, 0.05);
            color: white;
            transition: all 0.3s ease;
        }

        .search-box input:focus {
            outline: none;
            border-color: rgba(102, 126, 234, 0.5);
            background: rgba(255, 255, 255, 0.1);
        }

        .search-box input::placeholder {
            color: rgba(255, 255, 255, 0.5);
        }

        /* Sections */
        .section {
            margin-bottom: 50px;
        }

        .section-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 25px;
            flex-wrap: wrap;
            gap: 15px;
        }

        .section-title {
            font-size: clamp(1.5rem, 3vw, 2rem);
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .section-title .emoji {
            font-size: 1.5em;
        }

        .view-all-btn {
            background: rgba(102, 126, 234, 0.3);
            color: white;
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 20px;
            font-size: 0.9rem;
            transition: all 0.3s ease;
            border: 1px solid rgba(102, 126, 234, 0.5);
        }

        .view-all-btn:hover {
            background: rgba(102, 126, 234, 0.5);
            transform: translateY(-2px);
        }

        /* Grid */
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 20px;
        }

        @media (max-width: 768px) {
            .grid {
                grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
                gap: 15px;
            }
        }

        /* Cards */
        .card {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            padding: 20px;
            transition: all 0.3s ease;
            cursor: pointer;
            text-decoration: none;
            color: white;
            display: block;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .card:hover {
            transform: translateY(-5px);
            background: rgba(255, 255, 255, 0.1);
            border-color: rgba(102, 126, 234, 0.5);
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.2);
        }

        .card-header {
            display: flex;
            align-items: flex-start;
            gap: 12px;
            margin-bottom: 12px;
        }

        .card-emoji {
            font-size: 2rem;
            line-height: 1;
        }

        .card-title {
            font-size: 1.1rem;
            font-weight: 600;
            flex: 1;
        }

        .card-description {
            font-size: 0.9rem;
            opacity: 0.8;
            margin-bottom: 12px;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }

        .card-meta {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            font-size: 0.75rem;
        }

        .card-tag {
            background: rgba(102, 126, 234, 0.3);
            padding: 4px 10px;
            border-radius: 10px;
            opacity: 0.9;
        }

        .card-date {
            opacity: 0.6;
            margin-left: auto;
        }

        /* Category Section */
        .category-section {
            margin-bottom: 40px;
        }

        .category-title {
            font-size: 1.3rem;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .category-title .emoji {
            font-size: 1.3em;
        }

        /* Footer */
        .footer {
            text-align: center;
            padding: 40px 20px;
            opacity: 0.7;
            font-size: 0.9rem;
        }

        .footer a {
            color: #667eea;
            text-decoration: none;
        }

        /* Navigation */
        .nav {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-bottom: 30px;
            flex-wrap: wrap;
        }

        .nav a {
            background: rgba(255, 255, 255, 0.1);
            color: white;
            text-decoration: none;
            padding: 10px 25px;
            border-radius: 20px;
            font-weight: 500;
            transition: all 0.3s ease;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .nav a:hover {
            background: rgba(102, 126, 234, 0.3);
            border-color: rgba(102, 126, 234, 0.5);
            transform: translateY(-2px);
        }

        /* Mobile optimizations */
        @media (max-width: 768px) {
            .hero {
                padding: 40px 15px;
            }

            .stats {
                gap: 15px;
            }

            .stat-item {
                padding: 12px 20px;
                min-width: 120px;
            }

            .section-header {
                flex-direction: column;
                align-items: flex-start;
            }

            .view-all-btn {
                align-self: flex-start;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Navigation -->
        <nav class="nav">
            <a href="#artworks">🎨 アート</a>
            <a href="#games">🎮 ゲーム</a>
            <a href="https://github.com/ttikoantt/generative-art-mira" target="_blank">📦 GitHub</a>
        </nav>

        <!-- Hero Section -->
        <div class="hero">
            <h1>✨ Mira's Creative Gallery</h1>
            <p>AIによるジェネレーティブアート & ゲーム</p>
            <div class="stats">
                <div class="stat-item">
                    <div class="stat-number">""" + str(len(artworks)) + """</div>
                    <div class="stat-label">アート作品</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">""" + str(len(games)) + """</div>
                    <div class="stat-label">ゲーム</div>
                </div>
            </div>
        </div>

        <!-- Search -->
        <div class="search-container">
            <div class="search-box">
                <input 
                    type="text" 
                    id="searchInput" 
                    placeholder="🔍 作品を検索..."
                    oninput="handleSearch(this.value)"
                >
            </div>
        </div>

        <!-- Artworks Section -->
        <section class="section" id="artworks">
"""

    # Add artwork categories
    for cat_name, cat_arts in sorted(artwork_categories.items()):
        emoji_map = {
            'Particles': '✨',
            'Fractal': '🌀',
            'Geometric': '📐',
            'Wave': '🌊',
            'Audio': '🎵',
            'ASCII': '💻',
            'Nature': '🌸',
            'Cosmic': '🌌',
            'Interactive': '👆',
            'Experimental': '🔬'
        }
        
        html += f"""
            <div class="category-section">
                <div class="category-title">
                    <span class="emoji">{emoji_map.get(cat_name, '🎨')}</span>
                    {cat_name}
                </div>
                <div class="grid">
"""
        
        for art in cat_arts:
            tags_html = ' '.join([f'<span class="card-tag">{tag}</span>' for tag in art.get('tags', [])[:3]])
            html += f"""
                    <a href="{art['path']}" class="card">
                        <div class="card-header">
                            <span class="card-emoji">{art['emoji']}</span>
                            <div class="card-title">{art['title']}</div>
                        </div>
                        <div class="card-description">{art['description']}</div>
                        <div class="card-meta">
                            {tags_html}
                            <span class="card-date">{art['date']}</span>
                        </div>
                    </a>
"""
        
        html += """
                </div>
            </div>
"""

    html += """
        </section>

        <!-- Games Section -->
        <section class="section" id="games">
"""

    # Add game categories
    for cat_name, cat_games in sorted(game_categories.items()):
        emoji_map = {
            'Puzzle': '🧩',
            'Action': '⚡',
            'Reaction': '⚡',
            'Rhythm': '🎵',
            'Arcade': '🕹️',
            'Casual': '🎮',
            'Creative': '🎨'
        }
        
        html += f"""
            <div class="category-section">
                <div class="category-title">
                    <span class="emoji">{emoji_map.get(cat_name, '🎮')}</span>
                    {cat_name}
                </div>
                <div class="grid">
"""
        
        for game in cat_games:
            tags_html = ' '.join([f'<span class="card-tag">{tag}</span>' for tag in game.get('tags', [])[:3]])
            html += f"""
                    <a href="{game['path']}" class="card">
                        <div class="card-header">
                            <span class="card-emoji">{game['emoji']}</span>
                            <div class="card-title">{game['title']}</div>
                        </div>
                        <div class="card-description">{game['description']}</div>
                        <div class="card-meta">
                            {tags_html}
                            <span class="card-date">{game['date']}</span>
                        </div>
                    </a>
"""
        
        html += """
                </div>
            </div>
"""

    html += f"""
        </section>

        <!-- Footer -->
        <footer class="footer">
            <p>Made with ❤️ by Mira | <a href="https://github.com/ttikoantt/generative-art-mira" target="_blank">GitHub</a></p>
            <p style="margin-top: 10px; opacity: 0.6;">1時間ごとに新しい作品を追加中！</p>
        </footer>
    </div>

    <script>
        // Simple search functionality
        function handleSearch(query) {{
            const cards = document.querySelectorAll('.card');
            const lowerQuery = query.toLowerCase();
            
            cards.forEach(card => {{
                const title = card.querySelector('.card-title').textContent.toLowerCase();
                const description = card.querySelector('.card-description').textContent.toLowerCase();
                const tags = Array.from(card.querySelectorAll('.card-tag'))
                    .map(tag => tag.textContent.toLowerCase())
                    .join(' ');
                
                const matches = title.includes(lowerQuery) || 
                               description.includes(lowerQuery) || 
                               tags.includes(lowerQuery);
                
                card.style.display = matches ? 'block' : 'none';
            }});
        }}

        // Smooth scroll for navigation
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
            anchor.addEventListener('click', function (e) {{
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {{
                    target.scrollIntoView({{ behavior: 'smooth' }});
                }}
            }});
        }});
    </script>
</body>
</html>
"""

    # Save new index
    with open('index.html', 'w') as f:
        f.write(html)
    
    print("✅ 新しいindex.htmlを生成しました！")
    print(f"  - アートカテゴリ: {len(artwork_categories)}個")
    print(f"  - ゲームカテゴリ: {len(game_categories)}個")

if __name__ == '__main__':
    generate_new_index()
