#!/usr/bin/env python3
"""
YouTube Video Info & Visualizer
YouTubeの動画情報を取得して、ビジュアライゼーションを作成
"""

import os
import sys
import json
import re
from datetime import datetime
from urllib.parse import urlparse, parse_qs

# yt-dlpで動画情報を取得
import subprocess

def get_video_id(url):
    """YouTube URLから動画IDを抽出"""
    if "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    elif "watch?v=" in url:
        return url.split("watch?v=")[1].split("&")[0]
    return None

def get_video_info(video_id):
    """yt-dlpを使って動画情報を取得"""
    url = f"https://www.youtube.com/watch?v={video_id}"
    ytdlp_path = os.path.expanduser('~/Library/Python/3.11/bin/yt-dlp')

    try:
        result = subprocess.run(
            [
                ytdlp_path,
                '--dump-json',
                '--no-playlist',
                url
            ],
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode == 0:
            video_data = json.loads(result.stdout)
            return video_data
        else:
            print(f"Error: {result.stderr}")
            return None

    except Exception as e:
        print(f"Error getting video info: {e}")
        return None

def extract_keywords(text, top_n=20):
    """テキストからキーワードを抽出"""
    from collections import Counter
    import re

    # 単語を抽出
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

    # ストップワード除去
    stopwords = set(['the', 'a', 'an', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
                     'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could',
                     'should', 'may', 'might', 'must', 'shall', 'can', 'need', 'dare',
                     'ought', 'used', 'to', 'of', 'in', 'for', 'on', 'with', 'at', 'by',
                     'from', 'as', 'into', 'through', 'during', 'before', 'after', 'above',
                     'below', 'between', 'under', 'again', 'further', 'then', 'once',
                     'here', 'there', 'when', 'where', 'why', 'how', 'all', 'each', 'few',
                     'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only',
                     'own', 'same', 'so', 'than', 'too', 'very', 'just', 'but', 'and',
                     'or', 'if', 'it', 'its', 'this', 'that', 'these', 'those', 'he', 'she',
                     'they', 'we', 'you', 'i', 'me', 'him', 'her', 'us', 'them', 'my',
                     'your', 'his', 'their', 'our', 'its', 'what', 'which', 'who', 'whom',
                     'this', 'that', 'these', 'those'])

    filtered_words = [w for w in words if len(w) > 3 and w not in stopwords]

    # 頻度カウント
    word_counts = Counter(filtered_words)

    # 上位N個を取得
    top_keywords = word_counts.most_common(top_n)

    return [{"word": word, "count": count} for word, count in top_keywords]

def format_duration(seconds):
    """秒をHH:MM:SS形式に変換"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"

def format_number(num):
    """数字を整形（1K, 1Mなど）"""
    if num >= 1000000:
        return f"{num / 1000000:.1f}M"
    elif num >= 1000:
        return f"{num / 1000:.1f}K"
    else:
        return str(num)

def create_visualization(video_data, output_dir):
    """ビジュアライズHTMLを生成"""
    os.makedirs(output_dir, exist_ok=True)
    video_id = video_data.get('id', 'unknown')
    output_path = os.path.join(output_dir, f"{video_id}.html")

    # 動画情報を抽出
    title = video_data.get('title', 'Unknown Title')
    description = video_data.get('description', '')
    uploader = video_data.get('uploader', 'Unknown')
    duration = video_data.get('duration', 0)
    view_count = video_data.get('view_count', 0)
    like_count = video_data.get('like_count', 0)
    upload_date = video_data.get('upload_date', '')

    # 日付を整形
    if upload_date:
        try:
            date_obj = datetime.strptime(upload_date, '%Y%m%d')
            formatted_date = date_obj.strftime('%Y年%m月%d日')
        except:
            formatted_date = upload_date
    else:
        formatted_date = 'Unknown'

    # タグを取得
    tags = video_data.get('tags', [])[:20]

    # キーワード抽出
    combined_text = f"{title} {description} {' '.join(tags)}"
    keywords = extract_keywords(combined_text, top_n=20)

    # カテゴリ
    category = video_data.get('categories', ['Unknown'])[0] if video_data.get('categories') else 'Unknown'

    # HTML生成
    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - YouTube Video Info</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Helvetica Neue', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}

        .header {{
            text-align: center;
            color: white;
            margin-bottom: 30px;
        }}

        .header h1 {{
            font-size: 2.5rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}

        .header p {{
            font-size: 1.2rem;
            opacity: 0.9;
        }}

        .card {{
            background: white;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            margin-bottom: 20px;
        }}

        .card h2 {{
            color: #667eea;
            margin-bottom: 20px;
            font-size: 1.8rem;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
        }}

        .video-title {{
            font-size: 1.8rem;
            color: #333;
            margin-bottom: 20px;
            line-height: 1.4;
        }}

        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-bottom: 20px;
        }}

        .stat-item {{
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }}

        .stat-value {{
            font-size: 2rem;
            font-weight: bold;
            color: #667eea;
            margin-bottom: 5px;
        }}

        .stat-label {{
            color: #666;
            font-size: 0.9rem;
        }}

        .description {{
            background: #f5f7fa;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
            line-height: 1.6;
            color: #333;
            white-space: pre-wrap;
        }}

        .keyword-cloud {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            justify-content: center;
        }}

        .keyword {{
            padding: 8px 16px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 20px;
            font-size: 0.9rem;
            transition: transform 0.3s, box-shadow 0.3s;
            cursor: pointer;
        }}

        .keyword:hover {{
            transform: scale(1.1);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }}

        .tags {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 15px;
        }}

        .tag {{
            padding: 5px 12px;
            background: #667eea;
            color: white;
            border-radius: 15px;
            font-size: 0.8rem;
        }}

        .video-link {{
            display: inline-block;
            margin-top: 20px;
            padding: 12px 24px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-decoration: none;
            border-radius: 25px;
            font-weight: bold;
            transition: transform 0.3s, box-shadow 0.3s;
        }}

        .video-link:hover {{
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }}

        .fullscreen-btn {{
            position: fixed;
            top: 20px;
            right: 20px;
            background: white;
            border: none;
            padding: 15px;
            border-radius: 50%;
            cursor: pointer;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
            transition: transform 0.3s;
            z-index: 1000;
        }}

        .fullscreen-btn:hover {{
            transform: scale(1.1);
        }}

        @media (max-width: 768px) {{
            .header h1 {{
                font-size: 1.8rem;
            }}

            .stats-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <button class="fullscreen-btn" onclick="toggleFullScreen()" title="全画面表示">
        ⛶
    </button>

    <div class="container">
        <div class="header">
            <h1>🎬 YouTube動画情報</h1>
            <p>動画ID: {video_id}</p>
        </div>

        <div class="card">
            <h2 class="video-title">{title}</h2>

            <div class="stats-grid">
                <div class="stat-item">
                    <div class="stat-value">{format_number(view_count)}</div>
                    <div class="stat-label">再生回数</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value">{format_number(like_count)}</div>
                    <div class="stat-label">高評価</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value">{format_duration(duration)}</div>
                    <div class="stat-label">動画時間</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value">{formatted_date}</div>
                    <div class="stat-label">投稿日</div>
                </div>
            </div>

            <p><strong>チャンネル:</strong> {uploader}</p>
            <p><strong>カテゴリ:</strong> {category}</p>

            <a href="https://www.youtube.com/watch?v={video_id}" target="_blank" class="video-link">
                ▶️ 動画を見る
            </a>

            <div class="description">
                <strong>📝 説明:</strong>
                {description[:1000]}{'...' if len(description) > 1000 else ''}
            </div>

            <div class="tags">
    """

    # タグ追加
    for tag in tags[:15]:
        html += f"""
                <span class="tag">#{tag}</span>
        """

    html += """
            </div>
        </div>

        <div class="card">
            <h2>🏷️ キーワードクラウド</h2>
            <div class="keyword-cloud">
    """

    # キーワード追加（サイズを頻度に応じて変える）
    max_count = max([k["count"] for k in keywords]) if keywords else 1
    for kw in keywords:
        size = 0.8 + (kw["count"] / max_count) * 0.5
        html += f"""
                    <span class="keyword" style="font-size: {size}rem;">{kw['word']}</span>
        """

    html += f"""
            </div>
        </div>
    </div>

    <script>
        function toggleFullScreen() {{
            if (!document.fullscreenElement) {{
                document.documentElement.requestFullscreen();
            }} else {{
                document.exitFullscreen();
            }}
        }}
    </script>
</body>
</html>
    """

    # 保存
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    return output_path

def main():
    """メイン処理"""
    if len(sys.argv) < 2:
        print("Usage: python3 youtube_info.py <youtube_url>")
        sys.exit(1)

    youtube_url = sys.argv[1]

    print(f"🎬 Processing YouTube URL: {youtube_url}")

    # 動画ID取得
    video_id = get_video_id(youtube_url)
    if not video_id:
        print("❌ Failed to extract video ID")
        sys.exit(1)

    print(f"📹 Video ID: {video_id}")

    # 動画情報取得
    print("📥 Fetching video info...")
    video_data = get_video_info(video_id)
    if not video_data:
        print("❌ Failed to get video info")
        sys.exit(1)

    print(f"✅ Got video info: {video_data.get('title', 'Unknown')}")

    # ビジュアライズ作成
    print("🎨 Creating visualization...")
    output_dir = "/Users/naokitomono/Documents/generative-art-by-mira/outputs/youtube-summaries"
    html_path = create_visualization(video_data, output_dir)

    print(f"✅ Visualization created: {html_path}")

    # 結果を出力
    result = {
        "video_id": video_id,
        "title": video_data.get('title', ''),
        "view_count": video_data.get('view_count', 0),
        "html_path": html_path,
        "timestamp": datetime.now().isoformat()
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
