#!/usr/bin/env python3
"""
Generate artwork detail page
"""
import json
from pathlib import Path

def generate_detail_page():
    """Generate detail.html that shows artwork details based on URL parameter"""
    
    # Load manifests
    with open('artworks-manifest.json', 'r') as f:
        artworks = json.load(f)['artworks']
    
    with open('games-manifest.json', 'r') as f:
        games = json.load(f)['games']
    
    # Create lookup
    all_works = []
    for art in artworks:
        art['type'] = 'artwork'
        all_works.append(art)
    
    for game in games:
        game['type'] = 'game'
        all_works.append(game)
    
    # Generate HTML
    html = """<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title id="pageTitle">作品詳細</title>
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
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        .header {
            margin-bottom: 30px;
        }

        .back-btn {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(102, 126, 234, 0.3);
            color: white;
            text-decoration: none;
            padding: 12px 24px;
            border-radius: 20px;
            transition: all 0.3s ease;
            border: 1px solid rgba(102, 126, 234, 0.5);
        }

        .back-btn:hover {
            background: rgba(102, 126, 234, 0.5);
            transform: translateX(-5px);
        }

        .detail-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-bottom: 40px;
        }

        @media (max-width: 768px) {
            .detail-content {
                grid-template-columns: 1fr;
            }
        }

        .preview-section {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 20px;
            padding: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .preview-frame {
            width: 100%;
            height: 500px;
            border: none;
            border-radius: 15px;
            background: white;
        }

        .info-section {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 20px;
            padding: 30px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .work-header {
            display: flex;
            align-items: flex-start;
            gap: 15px;
            margin-bottom: 20px;
        }

        .work-emoji {
            font-size: 3rem;
            line-height: 1;
        }

        .work-title-group {
            flex: 1;
        }

        .work-title {
            font-size: 1.8rem;
            margin-bottom: 8px;
        }

        .work-type {
            display: inline-block;
            background: rgba(102, 126, 234, 0.3);
            padding: 5px 12px;
            border-radius: 10px;
            font-size: 0.85rem;
        }

        .work-description {
            font-size: 1.1rem;
            opacity: 0.9;
            margin-bottom: 25px;
            line-height: 1.8;
        }

        .meta-section {
            margin-bottom: 20px;
        }

        .meta-label {
            font-size: 0.85rem;
            opacity: 0.6;
            margin-bottom: 8px;
        }

        .tags {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }

        .tag {
            background: rgba(102, 126, 234, 0.3);
            padding: 6px 14px;
            border-radius: 15px;
            font-size: 0.85rem;
        }

        .date {
            font-size: 0.95rem;
            opacity: 0.8;
        }

        .actions {
            display: flex;
            gap: 15px;
            margin-top: 30px;
            flex-wrap: wrap;
        }

        .action-btn {
            flex: 1;
            min-width: 150px;
            padding: 15px 25px;
            border: none;
            border-radius: 15px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            text-align: center;
            text-decoration: none;
            display: inline-block;
        }

        .btn-primary {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
        }

        .btn-secondary {
            background: rgba(255, 255, 255, 0.1);
            color: white;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .btn-secondary:hover {
            background: rgba(255, 255, 255, 0.2);
        }

        .related-section {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 20px;
            padding: 30px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .related-title {
            font-size: 1.5rem;
            margin-bottom: 20px;
        }

        .related-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 20px;
        }

        .related-card {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            padding: 20px;
            transition: all 0.3s ease;
            cursor: pointer;
            text-decoration: none;
            color: white;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .related-card:hover {
            transform: translateY(-3px);
            background: rgba(255, 255, 255, 0.1);
        }

        .related-card-header {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 10px;
        }

        .related-emoji {
            font-size: 1.5rem;
        }

        .related-title {
            font-weight: 600;
        }

        .related-description {
            font-size: 0.85rem;
            opacity: 0.7;
        }
    </style>
</head>
<body>
    <div class="container">
        <header class="header">
            <a href="index.html" class="back-btn">
                ← トップに戻る
            </a>
        </header>

        <div id="detailContainer">
            <p style="text-align: center; opacity: 0.6;">読み込み中...</p>
        </div>

        <div id="relatedContainer"></div>
    </div>

    <script>
        // Load all works data
        const allWorks = """ + json.dumps(all_works, ensure_ascii=False) + """;

        function getWorkById(id) {
            return allWorks.find(work => work.id === id);
        }

        function getRelatedWorks(work, limit = 6) {
            // Find works with similar tags
            const workTags = work.tags || [];
            const related = allWorks
                .filter(w => w.id !== work.id)
                .filter(w => {
                    const wTags = w.tags || [];
                    return wTags.some(t => workTags.includes(t));
                })
                .slice(0, limit);
            
            return related;
        }

        function renderDetail(work) {
            if (!work) {
                document.getElementById('detailContainer').innerHTML = `
                    <div style="text-align: center; padding: 50px;">
                        <h2>作品が見つかりません</h2>
                        <a href="index.html" style="color: #667eea;">トップに戻る</a>
                    </div>
                `;
                return;
            }

            // Update page title
            document.title = `${work.title} - Mira's Gallery`;
            document.getElementById('pageTitle').textContent = work.title;

            // Render detail
            const container = document.getElementById('detailContainer');
            const tagsHtml = (work.tags || []).map(tag => 
                `<span class="tag">${tag}</span>`
            ).join('');

            const typeLabel = work.type === 'artwork' ? '🎨 アート' : '🎮 ゲーム';

            container.innerHTML = `
                <div class="detail-content">
                    <div class="preview-section">
                        <iframe src="${work.path}" class="preview-frame"></iframe>
                    </div>
                    <div class="info-section">
                        <div class="work-header">
                            <div class="work-emoji">${work.emoji}</div>
                            <div class="work-title-group">
                                <div class="work-title">${work.title}</div>
                                <span class="work-type">${typeLabel}</span>
                            </div>
                        </div>
                        <div class="work-description">${work.description}</div>
                        
                        <div class="meta-section">
                            <div class="meta-label">タグ</div>
                            <div class="tags">${tagsHtml}</div>
                        </div>
                        
                        <div class="meta-section">
                            <div class="meta-label">作成日</div>
                            <div class="date">${work.date}</div>
                        </div>
                        
                        <div class="actions">
                            <a href="${work.path}" target="_blank" class="action-btn btn-primary">
                                全画面で開く
                            </a>
                            <button onclick="copyLink('${work.id}')" class="action-btn btn-secondary">
                                🔗 リンクをコピー
                            </button>
                        </div>
                    </div>
                </div>
            `;

            // Render related works
            const related = getRelatedWorks(work);
            if (related.length > 0) {
                const relatedContainer = document.getElementById('relatedContainer');
                const relatedHtml = related.map(r => `
                    <a href="detail.html?id=${r.id}" class="related-card">
                        <div class="related-card-header">
                            <span class="related-emoji">${r.emoji}</span>
                            <div class="related-title">${r.title}</div>
                        </div>
                        <div class="related-description">${r.description}</div>
                    </a>
                `).join('');

                relatedContainer.innerHTML = `
                    <div class="related-section">
                        <div class="related-title">🔗 関連作品</div>
                        <div class="related-grid">
                            ${relatedHtml}
                        </div>
                    </div>
                `;
            }
        }

        function copyLink(id) {
            const url = window.location.href;
            navigator.clipboard.writeText(url).then(() => {
                alert('リンクをコピーしました！');
            });
        }

        // Load work on page load
        window.addEventListener('DOMContentLoaded', () => {
            const params = new URLSearchParams(window.location.search);
            const workId = params.get('id');
            
            if (workId) {
                const work = getWorkById(workId);
                renderDetail(work);
            } else {
                document.getElementById('detailContainer').innerHTML = `
                    <div style="text-align: center; padding: 50px;">
                        <h2>作品IDが指定されていません</h2>
                        <a href="index.html" style="color: #667eea;">トップに戻る</a>
                    </div>
                `;
            }
        });
    </script>
</body>
</html>
"""

    # Save detail page
    with open('detail.html', 'w') as f:
        f.write(html)
    
    print("✅ detail.htmlを生成しました！")

if __name__ == '__main__':
    generate_detail_page()
