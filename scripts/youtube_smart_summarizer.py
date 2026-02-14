#!/usr/bin/env python3
"""
YouTube Smart Summarizer with CSS Fix & Quality Summaries
CSS修正と高品質な要約アルゴリズム
"""

import sys
import json
import os
import subprocess
import re
from datetime import datetime
from collections import Counter

def get_video_id(url):
    """YouTube URLから動画IDを抽出"""
    if "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    elif "watch?v=" in url:
        return url.split("watch?v=")[1].split("&")[0]
    return url

def download_subs(video_id, lang='en'):
    """yt-dlpを使って字幕をダウンロード"""
    url = f"https://www.youtube.com/watch?v={video_id}"
    ytdlp_path = os.path.expanduser('~/Library/Python/3.11/bin/yt-dlp')
    temp_file = f"/tmp/youtube_subs_{video_id}_{lang}.vtt"

    try:
        result = subprocess.run(
            [
                ytdlp_path,
                '--write-auto-subs',
                '--sub-langs', lang,
                '--skip-download',
                '--sub-format', 'vtt',
                '--output', temp_file.replace('.vtt', ''),
                url
            ],
            capture_output=True,
            text=True,
            timeout=60
        )

        if not os.path.exists(temp_file):
            for file in os.listdir('/tmp'):
                if file.startswith(f'youtube_subs_{video_id}') and file.endswith('.vtt'):
                    temp_file = f'/tmp/{file}'
                    break

        if os.path.exists(temp_file):
            with open(temp_file, 'r', encoding='utf-8') as f:
                vtt_content = f.read()

            os.remove(temp_file)
            return vtt_content
        else:
            return None

    except Exception as e:
        print(f"Error downloading subs: {e}")
        return None

def parse_vtt(vtt_content):
    """VTTファイルをパースしてtranscriptを作成"""
    lines = vtt_content.split('\n')

    transcript = []
    current_start = None
    current_end = None
    current_text = []

    for line in lines:
        line = line.strip()

        timestamp_match = re.match(r'(\d{2}:\d{2}:\d{2}\.\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2}\.\d{3})', line)

        if timestamp_match:
            if current_start is not None and current_text:
                text = ' '.join(current_text)
                text = re.sub(r'<c>|</c>|<\d{2}:\d{2}:\d{2}\.\d{3}>', '', text)
                text = re.sub(r'<\d{2}:\d{2}:\d{2}\.\d{3}><c>|</c>', '', text)
                if text.strip():
                    transcript.append({
                        'start': current_start,
                        'end': current_end,
                        'text': text.strip()
                    })

            current_start = timestamp_to_seconds(timestamp_match.group(1))
            current_end = timestamp_to_seconds(timestamp_match.group(2))
            current_text = []

        elif line and not line.startswith('WEBVTT') and not line.startswith('Kind:') and not line.startswith('Language:'):
            current_text.append(line)

    if current_start is not None and current_text:
        text = ' '.join(current_text)
        text = re.sub(r'<c>|</c>|<\d{2}:\d{2}:\d{2}\.\d{3}>', '', text)
        text = re.sub(r'<\d{2}:\d{2}:\d{2}\.\d{3}><c>|</c>', '', text)
        if text.strip():
            transcript.append({
                'start': current_start,
                'end': current_end,
                'text': text.strip()
            })

    return transcript

def timestamp_to_seconds(timestamp):
    """タイムスタンプを秒に変換"""
    parts = timestamp.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = float(parts[2])
    return hours * 3600 + minutes * 60 + seconds

def format_time(seconds):
    """秒をHH:MM:SS形式に変換"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"

# 改善された要約アルゴリズム
def smart_summarize(transcript, max_points=8):
    """transcriptをスマートに要約 - トピックごとにグループ化して要約"""
    if not transcript:
        return []

    # 1. トピックを抽出（名詞・動詞・重要な単語）
    topics = extract_topics(transcript)

    # 2. 各トピックについてのセグメントをグループ化
    topic_segments = {}
    for seg in transcript:
        words = seg['text'].lower().split()
        for topic in topics:
            if any(topic in word for word in words):
                if topic not in topic_segments:
                    topic_segments[topic] = []
                topic_segments[topic].append(seg)
                break

    # 3. 各トピックから代表セグメントを選択
    summary = []
    for topic, segments in topic_segments.items():
        if len(segments) > 0:
            # 最も長いセグメントを選択（重要度が高い）
            best = max(segments, key=lambda s: len(s['text'].split()))
            summary.append({
                'text': best['text'],
                'start': best['start'],
                'end': best['end'],
                'topic': topic
            })

    # 4. 時間順にソート
    summary.sort(key=lambda x: x['start'])

    # 5. 上位N個に制限
    return summary[:max_points]

def extract_topics(transcript):
    """transcriptからトピックを抽出"""
    # 全テキストを結合
    full_text = ' '.join([seg['text'] for seg in transcript]).lower()

    # ストップワード除去
    stopwords = set(['the', 'and', 'that', 'have', 'for', 'not', 'you', 'with', 'this', 'but', 'his', 'from', 'they', 'she', 'her', 'been', 'than', 'its', 'who', 'was', 'are', 'will', 'would', 'could', 'should', 'about', 'after', 'into', 'over', 'their', 'your', 'what', 'when', 'make', 'like', 'just', 'time', 'them', 'more', 'some', 'only', 'were', 'said', 'each', 'does', 'done', 'come', 'also', 'well', 'much', 'even', 'such', 'because', 'any', 'most', 'many', 'then', 'than', 'too', 'very'])

    # 単語を抽出
    words = re.findall(r'\b[a-zA-Z]{4,}\b', full_text)
    filtered_words = [w for w in words if w not in stopwords]

    # 頻度分析
    word_counts = Counter(filtered_words)
    top_words = word_counts.most_common(10)

    # トピックとして返却
    return [word for word, count in top_words if count >= 2]

def extract_keywords(transcript, top_n=20):
    """キーワード抽出"""
    full_text = ' '.join([item['text'] for item in transcript]).lower()
    words = re.findall(r'\b[a-zA-Z]{3,}\b', full_text)

    stopwords = set(['the', 'and', 'that', 'have', 'for', 'not', 'you', 'with', 'this', 'but', 'his', 'from', 'they', 'she', 'her', 'been', 'than', 'its', 'who', 'was', 'are', 'will', 'would', 'could', 'should', 'about', 'after', 'into', 'over', 'their', 'your', 'what', 'when', 'make', 'like', 'just', 'time', 'them', 'more', 'some', 'only', 'were', 'said', 'each', 'does', 'done', 'come', 'also', 'well', 'much', 'even', 'such', 'because', 'any', 'most', 'many', 'then', 'than', 'too', 'very'])

    filtered_words = [w for w in words if w not in stopwords and len(w) > 3]
    word_counts = Counter(filtered_words)
    top_keywords = word_counts.most_common(top_n)

    return [{"word": word, "count": count} for word, count in top_keywords]

# CSS修正済みのHTML生成
def create_smart_summary(video_id, summary, keywords, video_url, output_path):
    """CSS修正済みのスマート要約HTMLを生成"""

    timeline_items = []
    for item in summary:
        topic_badge = f"<span class=\"topic-badge\">{item.get('topic', '')}</span>" if 'topic' in item else ""
        timeline_items.append(f"""
                    <div class="timeline-item" onclick="jumpToTime({item['start']})">
                        <div class="timeline-header">
                            <div class="timeline-time">{format_time(item['start'])}</div>
                            {topic_badge}
                        </div>
                        <div class="timeline-text">{item['text']}</div>
                    </div>
        """)

    timeline_html = '\n'.join(timeline_items)

    keyword_items = []
    max_count = max([k["count"] for k in keywords]) if keywords else 1
    for kw in keywords:
        size = 0.75 + (kw["count"] / max_count) * 0.5
        keyword_items.append(f'<span class="keyword" style="font-size: {size}rem;">{kw["word"]}</span>')
    keyword_html = '\n                    '.join(keyword_items)

    total_duration = summary[-1]['end'] if summary else 0

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YouTube Video Summary - {video_id}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 40px 20px;
            line-height: 1.6;
            color: #1a1a1a;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}

        .header {{
            text-align: center;
            margin-bottom: 48px;
        }}

        .header-badge {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 8px 16px;
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
            border-radius: 100px;
            font-size: 14px;
            font-weight: 600;
            color: white;
            margin-bottom: 24px;
            letter-spacing: 0.5px;
            text-transform: uppercase;
        }}

        .header h1 {{
            font-size: clamp(32px, 5vw, 56px);
            font-weight: 800;
            color: white;
            margin-bottom: 16px;
            text-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            letter-spacing: -0.02em;
            line-height: 1.1;
        }}

        .header-meta {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 24px;
            font-size: 15px;
            color: rgba(255, 255, 255, 0.9);
            font-weight: 500;
        }}

        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 24px;
            margin-bottom: 24px;
        }}

        .card {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            border-radius: 20px;
            padding: 32px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
            border: 1px solid rgba(255, 255, 255, 0.3);
        }}

        .card-header {{
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 24px;
        }}

        .card-title {{
            font-size: 24px;
            font-weight: 700;
            color: #1a1a1a;
        }}

        .card-icon {{
            font-size: 28px;
        }}

        .timeline {{
            position: relative;
            padding-left: 32px;
            max-height: 600px;
            overflow-y: auto;
            padding-right: 16px;
        }}

        .timeline::-webkit-scrollbar {{
            width: 8px;
        }}

        .timeline::-webkit-scrollbar-track {{
            background: rgba(0, 0, 0, 0.05);
            border-radius: 10px;
        }}

        .timeline::-webkit-scrollbar-thumb {{
            background: linear-gradient(135deg, #667eea, #764ba2);
            border-radius: 10px;
        }}

        .timeline::before {{
            content: '';
            position: absolute;
            left: 12px;
            top: 16px;
            bottom: 16px;
            width: 2px;
            background: linear-gradient(to bottom, #667eea, #764ba2);
            border-radius: 2px;
            opacity: 0.3;
        }}

        .timeline-item {{
            position: relative;
            padding: 20px;
            margin-bottom: 20px;
            background: rgba(248, 250, 252, 0.8);
            border-radius: 12px;
            border-left: 3px solid transparent;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            cursor: pointer;
        }}

        .timeline-item:hover {{
            transform: translateX(8px) scale(1.02);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
            border-left-color: #667eea;
        }}

        .timeline-item::before {{
            content: '';
            position: absolute;
            left: -32px;
            top: 24px;
            width: 10px;
            height: 10px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            border-radius: 50%;
            box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.3);
            transition: all 0.3s ease;
        }}

        .timeline-item:hover::before {{
            transform: scale(1.3);
            box-shadow: 0 0 0 6px rgba(102, 126, 234, 0.5);
        }}

        .timeline-header {{
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 8px;
        }}

        .timeline-time {{
            font-size: 13px;
            font-weight: 600;
            color: #667eea;
            font-family: 'JetBrains Mono', monospace;
            letter-spacing: 0.5px;
        }}

        .topic-badge {{
            padding: 4px 10px;
            background: linear-gradient(135deg, #f093fb, #f5576c);
            color: white;
            border-radius: 100px;
            font-size: 11px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .timeline-text {{
            color: #1a1a1a;
            line-height: 1.7;
            font-weight: 400;
            font-size: 15px;
        }}

        .keyword-cloud {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            justify-content: center;
            padding: 20px;
        }}

        .keyword {{
            padding: 8px 18px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border-radius: 100px;
            font-size: 14px;
            font-weight: 500;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            cursor: pointer;
            box-shadow: 0 2px 8px rgba(102, 126, 234, 0.2);
            letter-spacing: 0.2px;
        }}

        .keyword:hover {{
            transform: scale(1.1) translateY(-2px);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
        }}

        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 16px;
            margin-top: 24px;
        }}

        .stat-card {{
            background: rgba(248, 250, 252, 0.9);
            padding: 20px;
            border-radius: 12px;
            text-align: center;
            transition: all 0.3s ease;
            border: 1px solid rgba(0, 0, 0, 0.05);
        }}

        .stat-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
            border-color: rgba(102, 126, 234, 0.2);
        }}

        .stat-value {{
            font-size: 36px;
            font-weight: 800;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 8px;
            letter-spacing: -0.02em;
            line-height: 1;
        }}

        .stat-label {{
            color: #6b7280;
            font-size: 13px;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .video-button {{
            display: inline-flex;
            align-items: center;
            gap: 12px;
            margin-top: 32px;
            padding: 16px 32px;
            background: rgba(255, 255, 255, 0.95);
            color: #667eea;
            text-decoration: none;
            border-radius: 100px;
            font-weight: 600;
            font-size: 16px;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
            letter-spacing: 0.3px;
        }}

        .video-button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 12px 32px rgba(0, 0, 0, 0.3);
        }}

        .fullscreen-btn {{
            position: fixed;
            top: 24px;
            right: 24px;
            width: 56px;
            height: 56px;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(0, 0, 0, 0.1);
            border-radius: 50%;
            cursor: pointer;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            z-index: 1000;
        }}

        .fullscreen-btn:hover {{
            transform: scale(1.1);
            box-shadow: 0 12px 32px rgba(0, 0, 0, 0.25);
        }}

        @media (max-width: 768px) {{
            body {{
                padding: 24px 16px;
            }}

            .header h1 {{
                font-size: 32px;
            }}

            .grid {{
                grid-template-columns: 1fr;
                gap: 16px;
            }}

            .card {{
                padding: 24px;
            }}

            .stats-grid {{
                grid-template-columns: 1fr;
            }}

            .timeline {{
                padding-left: 24px;
                max-height: 400px;
            }}

            .fullscreen-btn {{
                top: 16px;
                right: 16px;
                width: 48px;
                height: 48px;
                font-size: 20px;
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
            <div class="header-badge">
                <span>🎬</span>
                <span>YouTube Video Summary</span>
            </div>
            <h1>動画要約＆ビジュアライゼーション</h1>
            <div class="header-meta">
                <span>📹 {video_id}</span>
                <span>⏱️ {format_time(total_duration)}</span>
            </div>
            <a href="{video_url}" target="_blank" class="video-button">
                <span>▶️</span>
                <span>動画を見る</span>
            </a>
        </div>

        <div class="grid">
            <div class="card">
                <div class="card-header">
                    <div class="card-title">
                        <span class="card-icon">📅</span>
                        <span>重要ポイント</span>
                    </div>
                </div>
                <div class="timeline">
                    {timeline_html}
                </div>
            </div>

            <div class="card">
                <div class="card-header">
                    <div class="card-title">
                        <span class="card-icon">🏷️</span>
                        <span>キーワード</span>
                    </div>
                </div>
                <div class="keyword-cloud">
                    {keyword_html}
                </div>
                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="stat-value">{len(summary)}</div>
                        <div class="stat-label">重要ポイント</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value">{len(keywords)}</div>
                        <div class="stat-label">キーワード</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value">{len(transcript) if 'transcript' in dir() else 0}</div>
                        <div class="stat-label">セグメント数</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value">{format_time(total_duration)}</div>
                        <div class="stat-label">動画時間</div>
                    </div>
                </div>
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

        function jumpToTime(seconds) {{
            window.open(`{video_url}&t=${{Math.floor(seconds)}}s`, '_blank');
        }}
    </script>
</body>
</html>
    """

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    return output_path

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 youtube_smart_summarizer.py <youtube_url>")
        sys.exit(1)

    youtube_url = sys.argv[1]
    video_id = get_video_id(youtube_url)

    if not video_id:
        print("❌ Invalid YouTube URL")
        sys.exit(1)

    print(f"🎬 Processing YouTube URL: {youtube_url}")
    print(f"📹 Video ID: {video_id}")

    # transcriptを取得
    print("📥 Fetching transcript...")
    vtt_content = download_subs(video_id, lang='en')

    if not vtt_content:
        print("❌ No transcript available")
        sys.exit(1)

    transcript = parse_vtt(vtt_content)
    print(f"✅ Got {len(transcript)} transcript segments")

    # 改善された要約アルゴリズム
    print("🧠 Smart summarizing with topic extraction...")
    summary = smart_summarize(transcript)
    print(f"✅ Generated {len(summary)} key points with topics")

    # トピックを表示
    topics = extract_topics(transcript)
    print(f"📋 Extracted topics: {', '.join(topics[:5])}")

    # キーワード抽出
    print("🏷️ Extracting keywords...")
    keywords = extract_keywords(transcript)
    print(f"✅ Extracted {len(keywords)} keywords")

    # HTML生成
    print("🎨 Creating smart summary with fixed CSS...")
    output_dir = "/Users/naokitomono/Documents/generative-art-by-mira/outputs/youtube-summaries"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{video_id}.html")

    html_path = create_smart_summary(video_id, summary, keywords, youtube_url, output_path)

    print(f"✅ Visualization created: {html_path}")

    # 結果を出力
    result = {
        "video_id": video_id,
        "url": youtube_url,
        "summary_points": len(summary),
        "topics": topics[:5],
        "keywords": len(keywords),
        "segments": len(transcript),
        "html_path": html_path,
        "timestamp": datetime.now().isoformat()
    }

    print("\n" + "="*60)
    print("✅ Smart Summary with Fixed CSS Created!")
    print("="*60)
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
