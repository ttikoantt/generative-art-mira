#!/usr/bin/env python3
"""
Multiple Design Pattern YouTube Summarizer
グラデコ風のデザインを5種類作成して比較
"""

import sys
import json
import os
import subprocess
import re
from datetime import datetime

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

def summarize_transcript(transcript, max_points=10):
    """transcriptを要約"""
    if not transcript:
        return []

    scored_segments = []
    for seg in transcript:
        duration = seg['end'] - seg['start']
        word_count = len(seg['text'].split())
        score = duration * (1 + word_count / 10)
        scored_segments.append({
            'text': seg['text'],
            'start': seg['start'],
            'end': seg['end'],
            'score': score
        })

    scored_segments.sort(key=lambda x: x['score'], reverse=True)

    key_points = []
    seen_texts = set()
    for seg in scored_segments:
        if len(key_points) >= max_points:
            break
        if seg['text'] not in seen_texts:
            key_points.append({
                'text': seg['text'],
                'start': seg['start'],
                'end': seg['end']
            })
            seen_texts.add(seg['text'])

    key_points.sort(key=lambda x: x['start'])
    return key_points

def extract_keywords(transcript, top_n=20):
    """キーワード抽出"""
    from collections import Counter

    full_text = ' '.join([item['text'] for item in transcript]).lower()
    words = re.findall(r'\b[a-zA-Z]{3,}\b', full_text)

    stopwords = set(['the', 'and', 'that', 'have', 'for', 'not', 'you', 'with', 'this', 'but', 'his', 'from', 'they', 'she', 'her', 'been', 'than', 'its', 'who', 'was', 'are', 'will', 'would', 'could', 'should', 'about', 'after', 'into', 'over', 'their', 'your', 'what', 'when', 'make', 'like', 'just', 'time', 'them', 'more', 'some', 'only', 'were', 'said', 'each', 'does', 'done', 'come', 'also', 'well', 'much', 'even', 'such', 'because', 'any', 'most', 'many', 'then', 'than', 'too', 'very'])

    filtered_words = [w for w in words if w not in stopwords and len(w) > 3]
    word_counts = Counter(filtered_words)
    top_keywords = word_counts.most_common(top_n)

    return [{"word": word, "count": count} for word, count in top_keywords]

# デザインパターン1: Modern Clean
def create_moden_clean(video_id, summary, keywords, video_url, output_path):
    """モダンでクリーンなデザイン（ミニマル・白ベース）"""

    timeline_items = []
    for item in summary:
        timeline_items.append(f"""
                    <div class="timeline-item" onclick="jumpToTime({item['start']})">
                        <div class="timeline-time">{format_time(item['start'])}</div>
                        <div class="timeline-text">{item['text']}</div>
                    </div>
        """)

    timeline_html = '\n'.join(timeline_items)

    keyword_items = []
    for kw in keywords:
        keyword_items.append(f'<span class="keyword">{kw["word"]}</span>')
    keyword_html = '\n                    '.join(keyword_items)

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Summary - {video_id}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #ffffff;
            color: #1a1a1a;
            line-height: 1.6;
            padding: 60px 20px;
        }}

        .container {{
            max-width: 900px;
            margin: 0 auto;
        }}

        .header {{
            margin-bottom: 60px;
            text-align: center;
        }}

        .header h1 {{
            font-size: 48px;
            font-weight: 700;
            letter-spacing: -0.02em;
            margin-bottom: 12px;
            color: #1a1a1a;
        }}

        .header p {{
            font-size: 16px;
            color: #6b7280;
            font-weight: 400;
        }}

        .section {{
            margin-bottom: 60px;
        }}

        .section-title {{
            font-size: 14px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            color: #9ca3af;
            margin-bottom: 24px;
        }}

        .card {{
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 12px;
            padding: 32px;
            box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
        }}

        .timeline {{
            position: relative;
            padding-left: 24px;
        }}

        .timeline::before {{
            content: '';
            position: absolute;
            left: 0;
            top: 8px;
            bottom: 8px;
            width: 2px;
            background: #e5e7eb;
        }}

        .timeline-item {{
            position: relative;
            padding: 20px 0;
            border-bottom: 1px solid #f3f4f6;
        }}

        .timeline-item:last-child {{
            border-bottom: none;
        }}

        .timeline-item::before {{
            content: '';
            position: absolute;
            left: -24px;
            top: 4px;
            width: 10px;
            height: 10px;
            background: #1a1a1a;
            border-radius: 50%;
        }}

        .timeline-time {{
            font-size: 13px;
            font-weight: 500;
            color: #6b7280;
            margin-bottom: 8px;
            font-family: 'SF Mono', 'Monaco', 'Inconsolata', 'Fira Code', monospace;
        }}

        .timeline-text {{
            font-size: 15px;
            line-height: 1.7;
            color: #374151;
        }}

        .keyword-cloud {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }}

        .keyword {{
            padding: 6px 14px;
            background: #f3f4f6;
            color: #1a1a1a;
            border-radius: 6px;
            font-size: 13px;
            font-weight: 500;
        }}

        .stats {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 16px;
            margin-top: 32px;
        }}

        .stat {{
            padding: 24px;
            background: #f9fafb;
            border-radius: 8px;
            text-align: center;
        }}

        .stat-value {{
            font-size: 32px;
            font-weight: 700;
            color: #1a1a1a;
            margin-bottom: 4px;
        }}

        .stat-label {{
            font-size: 12px;
            color: #6b7280;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}

        .video-button {{
            display: inline-block;
            margin-top: 32px;
            padding: 14px 28px;
            background: #1a1a1a;
            color: #ffffff;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 500;
            font-size: 14px;
            transition: all 0.2s;
        }}

        .video-button:hover {{
            background: #374151;
        }}

        @media (max-width: 768px) {{
            body {{
                padding: 40px 16px;
            }}

            .header h1 {{
                font-size: 36px;
            }}

            .stats {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Video Summary</h1>
            <p>{video_id}</p>
        </div>

        <div class="section">
            <div class="section-title">Key Moments</div>
            <div class="card">
                <div class="timeline">
                    {timeline_html}
                </div>
            </div>
        </div>

        <div class="section">
            <div class="section-title">Keywords</div>
            <div class="card">
                <div class="keyword-cloud">
                    {keyword_html}
                </div>
                <div class="stats">
                    <div class="stat">
                        <div class="stat-value">{len(summary)}</div>
                        <div class="stat-label">Key Points</div>
                    </div>
                    <div class="stat">
                        <div class="stat-value">{len(keywords)}</div>
                        <div class="stat-label">Keywords</div>
                    </div>
                </div>
            </div>
        </div>

        <div style="text-align: center;">
            <a href="{video_url}" target="_blank" class="video-button">▶ Watch Video</a>
        </div>
    </div>

    <script>
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

# デザインパターン2: Vibrant Gradient
def create_vibrant_gradient(video_id, summary, keywords, video_url, output_path):
    """鮮やかなグラデーションを使ったデザイン（色フル・動的）"""

    timeline_items = []
    for item in summary:
        timeline_items.append(f"""
                    <div class="timeline-item" onclick="jumpToTime({item['start']})">
                        <div class="timeline-time">{format_time(item['start'])}</div>
                        <div class="timeline-text">{item['text']}</div>
                    </div>
        """)

    timeline_html = '\n'.join(timeline_items)

    keyword_items = []
    max_count = max([k["count"] for k in keywords]) if keywords else 1
    for kw in keywords:
        size = 0.8 + (kw["count"] / max_count) * 0.4
        keyword_items.append(f'<span class="keyword" style="font-size: {size}rem;">{kw["word"]}</span>')
    keyword_html = '\n                    '.join(keyword_items)

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Summary - {video_id}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'SF Pro Display', -apple-system, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
            background-size: 400% 400%;
            animation: gradientShift 15s ease infinite;
            color: #ffffff;
            line-height: 1.6;
            padding: 60px 20px;
            min-height: 100vh;
        }}

        @keyframes gradientShift {{
            0% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}

        .container {{
            max-width: 900px;
            margin: 0 auto;
        }}

        .header {{
            margin-bottom: 60px;
            text-align: center;
        }}

        .header h1 {{
            font-size: 56px;
            font-weight: 800;
            letter-spacing: -0.03em;
            margin-bottom: 16px;
            text-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        }}

        .section {{
            margin-bottom: 60px;
        }}

        .section-title {{
            font-size: 16px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.15em;
            margin-bottom: 24px;
            opacity: 0.9;
        }}

        .card {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        }}

        .timeline {{
            position: relative;
            padding-left: 32px;
        }}

        .timeline::before {{
            content: '';
            position: absolute;
            left: 0;
            top: 16px;
            bottom: 16px;
            width: 3px;
            background: linear-gradient(to bottom, #667eea, #764ba2, #f093fb);
            border-radius: 3px;
        }}

        .timeline-item {{
            position: relative;
            padding: 24px 0;
            margin-bottom: 24px;
        }}

        .timeline-item::before {{
            content: '';
            position: absolute;
            left: -32px;
            top: 6px;
            width: 12px;
            height: 12px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            border-radius: 50%;
            box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.4);
        }}

        .timeline-time {{
            font-size: 14px;
            font-weight: 700;
            color: #667eea;
            margin-bottom: 8px;
            font-family: 'SF Mono', 'Monaco', monospace;
        }}

        .timeline-text {{
            font-size: 16px;
            line-height: 1.8;
            color: #1a1a1a;
            font-weight: 500;
        }}

        .keyword-cloud {{
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            justify-content: center;
        }}

        .keyword {{
            padding: 10px 20px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border-radius: 100px;
            font-weight: 600;
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
            transition: transform 0.2s;
        }}

        .keyword:hover {{
            transform: scale(1.1);
        }}

        .stats {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
            margin-top: 32px;
        }}

        .stat {{
            padding: 28px;
            background: rgba(255, 255, 255, 0.9);
            border-radius: 16px;
            text-align: center;
        }}

        .stat-value {{
            font-size: 40px;
            font-weight: 800;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 8px;
        }}

        .stat-label {{
            font-size: 12px;
            color: #6b7280;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.1em;
        }}

        .video-button {{
            display: inline-block;
            margin-top: 40px;
            padding: 16px 40px;
            background: white;
            color: #667eea;
            text-decoration: none;
            border-radius: 100px;
            font-weight: 700;
            font-size: 16px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
            transition: all 0.2s;
        }}

        .video-button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 12px 32px rgba(0, 0, 0, 0.4);
        }}

        @media (max-width: 768px) {{
            body {{
                padding: 40px 16px;
            }}

            .header h1 {{
                font-size: 40px;
            }}

            .card {{
                padding: 32px;
            }}

            .stats {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>VIDEO SUMMARY</h1>
        </div>

        <div class="section">
            <div class="section-title">Key Moments</div>
            <div class="card">
                <div class="timeline">
                    {timeline_html}
                </div>
            </div>
        </div>

        <div class="section">
            <div class="section-title">Keywords</div>
            <div class="card">
                <div class="keyword-cloud">
                    {keyword_html}
                </div>
                <div class="stats">
                    <div class="stat">
                        <div class="stat-value">{len(summary)}</div>
                        <div class="stat-label">Points</div>
                    </div>
                    <div class="stat">
                        <div class="stat-value">{len(keywords)}</div>
                        <div class="stat-label">Keywords</div>
                    </div>
                </div>
            </div>
        </div>

        <div style="text-align: center;">
            <a href="{video_url}" target="_blank" class="video-button">▶ WATCH VIDEO</a>
        </div>
    </div>

    <script>
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

# デザインパターン3: Dark Mode
def create_dark_mode(video_id, summary, keywords, video_url, output_path):
    """ダークモードデザイン（ダークテーマ・ネオン）"""

    timeline_items = []
    for item in summary:
        timeline_items.append(f"""
                    <div class="timeline-item" onclick="jumpToTime({item['start']})">
                        <div class="timeline-time">{format_time(item['start'])}</div>
                        <div class="timeline-text">{item['text']}</div>
                    </div>
        """)

    timeline_html = '\n'.join(timeline_items)

    keyword_items = []
    for kw in keywords:
        keyword_items.append(f'<span class="keyword">{kw["word"]}</span>')
    keyword_html = '\n                    '.join(keyword_items)

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Summary - {video_id}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Inter', -apple-system, sans-serif;
            background: #0d1117;
            color: #e2e8f0;
            line-height: 1.6;
            padding: 60px 20px;
        }}

        .container {{
            max-width: 900px;
            margin: 0 auto;
        }}

        .header {{
            margin-bottom: 60px;
            text-align: center;
        }}

        .header h1 {{
            font-size: 52px;
            font-weight: 800;
            letter-spacing: -0.02em;
            margin-bottom: 16px;
            background: linear-gradient(135deg, #667eea, #764ba2, #f093fb);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        .section {{
            margin-bottom: 60px;
        }}

        .section-title {{
            font-size: 14px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.15em;
            margin-bottom: 24px;
            color: #94a3b8;
        }}

        .card {{
            background: rgba(22, 33, 62, 0.5);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(148, 163, 184, 0.1);
            border-radius: 16px;
            padding: 40px;
            box-shadow: 0 0 40px rgba(0, 0, 0, 0.3);
        }}

        .timeline {{
            position: relative;
            padding-left: 32px;
        }}

        .timeline::before {{
            content: '';
            position: absolute;
            left: 0;
            top: 16px;
            bottom: 16px;
            width: 2px;
            background: linear-gradient(to bottom, #667eea, #764ba2, #f093fb);
        }}

        .timeline-item {{
            position: relative;
            padding: 20px 0;
            border-bottom: 1px solid rgba(148, 163, 184, 0.1);
        }}

        .timeline-item:last-child {{
            border-bottom: none;
        }}

        .timeline-item::before {{
            content: '';
            position: absolute;
            left: -32px;
            top: 4px;
            width: 12px;
            height: 12px;
            background: #667eea;
            border-radius: 50%;
            box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.5);
        }}

        .timeline-time {{
            font-size: 13px;
            font-weight: 600;
            color: #667eea;
            margin-bottom: 8px;
            font-family: 'SF Mono', 'Monaco', monospace;
        }}

        .timeline-text {{
            font-size: 15px;
            line-height: 1.7;
            color: #e2e8f0;
        }}

        .keyword-cloud {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            justify-content: center;
        }}

        .keyword {{
            padding: 8px 18px;
            background: rgba(102, 126, 234, 0.2);
            border: 1px solid rgba(102, 126, 234, 0.3);
            color: #e2e8f0;
            border-radius: 8px;
            font-size: 13px;
            font-weight: 500;
            transition: all 0.2s;
        }}

        .keyword:hover {{
            background: rgba(102, 126, 234, 0.3);
            border-color: rgba(102, 126, 234, 0.5);
            transform: translateY(-2px);
        }}

        .stats {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 16px;
            margin-top: 32px;
        }}

        .stat {{
            padding: 24px;
            background: rgba(22, 33, 62, 0.3);
            border: 1px solid rgba(148, 163, 184, 0.1);
            border-radius: 12px;
            text-align: center;
        }}

        .stat-value {{
            font-size: 36px;
            font-weight: 800;
            color: #667eea;
            margin-bottom: 8px;
        }}

        .stat-label {{
            font-size: 12px;
            color: #94a3b8;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.1em;
        }}

        .video-button {{
            display: inline-block;
            margin-top: 40px;
            padding: 16px 40px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            text-decoration: none;
            border-radius: 12px;
            font-weight: 600;
            font-size: 16px;
            box-shadow: 0 4px 16px rgba(102, 126, 234, 0.4);
            transition: all 0.2s;
        }}

        .video-button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 8px 24px rgba(102, 126, 234, 0.6);
        }}

        @media (max-width: 768px) {{
            body {{
                padding: 40px 16px;
            }}

            .header h1 {{
                font-size: 40px;
            }}

            .stats {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>VIDEO SUMMARY</h1>
        </div>

        <div class="section">
            <div class="section-title">Key Moments</div>
            <div class="card">
                <div class="timeline">
                    {timeline_html}
                </div>
            </div>
        </div>

        <div class="section">
            <div class="section-title">Keywords</div>
            <div class="card">
                <div class="keyword-cloud">
                    {keyword_html}
                </div>
                <div class="stats">
                    <div class="stat">
                        <div class="stat-value">{len(summary)}</div>
                        <div class="stat-label">Points</div>
                    </div>
                    <div class="stat">
                        <div class="stat-value">{len(keywords)}</div>
                        <div class="stat-label">Keywords</div>
                    </div>
                </div>
            </div>
        </div>

        <div style="text-align: center;">
            <a href="{video_url}" target="_blank" class="video-button">▶ WATCH VIDEO</a>
        </div>
    </div>

    <script>
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

# デザインパターン4: Typography First
def create_typography_first(video_id, summary, keywords, video_url, output_path):
    """タイポグラフィ重視のデザイン（巨大な文字・強調）"""

    timeline_items = []
    for item in summary:
        timeline_items.append(f"""
                    <div class="timeline-item" onclick="jumpToTime({item['start']})">
                        <div class="timeline-time">{format_time(item['start'])}</div>
                        <div class="timeline-text">{item['text']}</div>
                    </div>
        """)

    timeline_html = '\n'.join(timeline_items)

    keyword_items = []
    for kw in keywords[:15]:
        keyword_items.append(f'<span class="keyword">{kw["word"]}</span>')
    keyword_html = '\n                    '.join(keyword_items)

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Summary - {video_id}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'New York', serif;
            background: #fafafa;
            color: #1a1a1a;
            line-height: 1.5;
            padding: 80px 40px;
        }}

        .container {{
            max-width: 800px;
            margin: 0 auto;
        }}

        .header {{
            margin-bottom: 80px;
        }}

        .header h1 {{
            font-size: clamp(48px, 8vw, 96px);
            font-weight: 800;
            letter-spacing: -0.04em;
            line-height: 0.95;
            margin-bottom: 32px;
        }}

        .header p {{
            font-size: 18px;
            color: #6b7280;
            font-weight: 400;
            font-style: italic;
        }}

        .section {{
            margin-bottom: 80px;
        }}

        .section-title {{
            font-size: 12px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.2em;
            margin-bottom: 32px;
            color: #9ca3af;
        }}

        .timeline-item {{
            padding: 32px 0;
            border-bottom: 2px solid #1a1a1a;
        }}

        .timeline-item:last-child {{
            border-bottom: none;
        }}

        .timeline-time {{
            font-size: 14px;
            font-weight: 600;
            color: #6b7280;
            margin-bottom: 16px;
            font-family: 'SF Mono', 'Monaco', monospace;
            letter-spacing: 0.1em;
        }}

        .timeline-text {{
            font-size: clamp(18px, 3vw, 28px);
            line-height: 1.4;
            color: #1a1a1a;
            font-weight: 400;
        }}

        .keyword-cloud {{
            display: flex;
            flex-wrap: wrap;
            gap: 16px;
        }}

        .keyword {{
            font-size: clamp(14px, 2vw, 20px);
            font-weight: 600;
            color: #1a1a1a;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}

        .stats {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 32px;
            margin-top: 48px;
        }}

        .stat {{
            text-align: center;
        }}

        .stat-value {{
            font-size: clamp(48px, 8vw, 72px);
            font-weight: 800;
            color: #1a1a1a;
            margin-bottom: 8px;
            letter-spacing: -0.02em;
        }}

        .stat-label {{
            font-size: 12px;
            color: #6b7280;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.15em;
        }}

        .video-button {{
            display: inline-block;
            margin-top: 48px;
            padding: 16px 48px;
            background: #1a1a1a;
            color: #ffffff;
            text-decoration: none;
            font-weight: 600;
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            transition: all 0.2s;
        }}

        .video-button:hover {{
            background: #374151;
        }}

        @media (max-width: 768px) {{
            body {{
                padding: 60px 24px;
            }}

            .stats {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Summary</h1>
            <p>{video_id}</p>
        </div>

        <div class="section">
            <div class="section-title">Key Moments</div>
            <div class="timeline">
                {timeline_html}
            </div>
        </div>

        <div class="section">
            <div class="section-title">Keywords</div>
            <div class="keyword-cloud">
                {keyword_html}
            </div>
            <div class="stats">
                <div class="stat">
                    <div class="stat-value">{len(summary)}</div>
                    <div class="stat-label">Points</div>
                </div>
                <div class="stat">
                    <div class="stat-value">{len(keywords)}</div>
                    <div class="stat-label">Keywords</div>
                </div>
            </div>
        </div>

        <div style="text-align: center;">
            <a href="{video_url}" target="_blank" class="video-button">▶ WATCH VIDEO</a>
        </div>
    </div>

    <script>
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

# デザインパターン5: Data Visualization
def create_data_viz(video_id, summary, keywords, video_url, output_path):
    """データ可視化重視のデザイン（チャート・グラフ風）"""

    # キーワードのカウントからパーセンテージを計算
    total_count = sum([k["count"] for k in keywords])
    max_count = max([k["count"] for k in keywords]) if keywords else 1

    timeline_items = []
    for item in summary:
        timeline_items.append(f"""
                    <div class="timeline-item" onclick="jumpToTime({item['start']})">
                        <div class="timeline-time">{format_time(item['start'])}</div>
                        <div class="timeline-text">{item['text']}</div>
                    </div>
        """)

    timeline_html = '\n'.join(timeline_items)

    keyword_items = []
    for kw in keywords:
        percentage = (kw["count"] / total_count) * 100
        keyword_items.append(f'''
                    <div class="keyword-bar">
                        <div class="keyword-text">{kw["word"]}</div>
                        <div class="keyword-bar-bg">
                            <div class="keyword-bar-fill" style="width: {percentage}%"></div>
                        </div>
                        <div class="keyword-count">{kw["count"]}</div>
                    </div>
        ''')
    keyword_html = '\n                    '.join(keyword_items)

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Summary - {video_id}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, sans-serif;
            background: #f8f9fa;
            color: #1a1a1a;
            line-height: 1.6;
            padding: 60px 20px;
        }}

        .container {{
            max-width: 1000px;
            margin: 0 auto;
        }}

        .header {{
            margin-bottom: 60px;
            text-align: center;
        }}

        .header h1 {{
            font-size: 40px;
            font-weight: 700;
            letter-spacing: -0.01em;
            margin-bottom: 16px;
            color: #1a1a1a;
        }}

        .header-stats {{
            display: flex;
            justify-content: center;
            gap: 48px;
            font-size: 14px;
            color: #6b7280;
        }}

        .section {{
            margin-bottom: 60px;
        }}

        .section-title {{
            font-size: 16px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            margin-bottom: 24px;
            color: #374151;
        }}

        .card {{
            background: #ffffff;
            border-radius: 12px;
            padding: 40px;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        }}

        .timeline {{
            position: relative;
            padding-left: 24px;
        }}

        .timeline::before {{
            content: '';
            position: absolute;
            left: 0;
            top: 8px;
            bottom: 8px;
            width: 2px;
            background: #e5e7eb;
        }}

        .timeline-item {{
            position: relative;
            padding: 16px 0;
            border-bottom: 1px solid #f3f4f6;
        }}

        .timeline-item:last-child {{
            border-bottom: none;
        }}

        .timeline-item::before {{
            content: '';
            position: absolute;
            left: -24px;
            top: 4px;
            width: 10px;
            height: 10px;
            background: #374151;
            border-radius: 50%;
        }}

        .timeline-time {{
            font-size: 12px;
            font-weight: 600;
            color: #6b7280;
            margin-bottom: 8px;
            font-family: 'SF Mono', 'Monaco', monospace;
        }}

        .timeline-text {{
            font-size: 15px;
            line-height: 1.7;
            color: #1a1a1a;
        }}

        .keyword-list {{
            display: flex;
            flex-direction: column;
            gap: 12px;
        }}

        .keyword-bar {{
            display: grid;
            grid-template-columns: 150px 1fr 60px;
            gap: 12px;
            align-items: center;
        }}

        .keyword-text {{
            font-size: 14px;
            font-weight: 500;
            color: #1a1a1a;
        }}

        .keyword-bar-bg {{
            height: 24px;
            background: #f3f4f6;
            border-radius: 4px;
            overflow: hidden;
        }}

        .keyword-bar-fill {{
            height: 100%;
            background: linear-gradient(90deg, #667eea, #764ba2);
            border-radius: 4px;
            transition: width 0.5s ease;
        }}

        .keyword-count {{
            font-size: 14px;
            font-weight: 600;
            color: #6b7280;
            text-align: right;
        }}

        .video-button {{
            display: inline-block;
            margin-top: 40px;
            padding: 14px 32px;
            background: #374151;
            color: #ffffff;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 500;
            font-size: 14px;
            transition: all 0.2s;
        }}

        .video-button:hover {{
            background: #1a1a1a;
        }}

        @media (max-width: 768px) {{
            body {{
                padding: 40px 16px;
            }}

            .keyword-bar {{
                grid-template-columns: 1fr;
                gap: 8px;
            }}

            .keyword-bar-bg {{
                grid-column: 1 / -1;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Video Summary</h1>
            <div class="header-stats">
                <span>{len(summary)} key moments</span>
                <span>{len(keywords)} keywords found</span>
            </div>
        </div>

        <div class="section">
            <div class="section-title">Key Moments</div>
            <div class="card">
                <div class="timeline">
                    {timeline_html}
                </div>
            </div>
        </div>

        <div class="section">
            <div class="section-title">Keywords Distribution</div>
            <div class="card">
                <div class="keyword-list">
                    {keyword_html}
                </div>
            </div>
        </div>

        <div style="text-align: center;">
            <a href="{video_url}" target="_blank" class="video-button">▶ WATCH VIDEO</a>
        </div>
    </div>

    <script>
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
        print("Usage: python3 youtube_design_patterns.py <youtube_url>")
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

    # 要約
    print("📝 Summarizing...")
    summary = summarize_transcript(transcript)
    print(f"✅ Generated {len(summary)} key points")

    # キーワード抽出
    print("🏷️ Extracting keywords...")
    keywords = extract_keywords(transcript)
    print(f"✅ Extracted {len(keywords)} keywords")

    # 5種類のデザインパターンを作成
    output_dir = "/Users/naokitomono/Documents/generative-art-by-mira/outputs/design-patterns"
    os.makedirs(output_dir, exist_ok=True)

    print("\n🎨 Creating 5 design patterns...")

    # 1. Modern Clean
    print("1/5: Modern Clean...")
    path1 = create_moden_clean(video_id, summary, keywords, youtube_url,
                                   os.path.join(output_dir, f"{video_id}-moden-clean.html"))
    print(f"✅ {path1}")

    # 2. Vibrant Gradient
    print("2/5: Vibrant Gradient...")
    path2 = create_vibrant_gradient(video_id, summary, keywords, youtube_url,
                                       os.path.join(output_dir, f"{video_id}-vibrant-gradient.html"))
    print(f"✅ {path2}")

    # 3. Dark Mode
    print("3/5: Dark Mode...")
    path3 = create_dark_mode(video_id, summary, keywords, youtube_url,
                                os.path.join(output_dir, f"{video_id}-dark-mode.html"))
    print(f"✅ {path3}")

    # 4. Typography First
    print("4/5: Typography First...")
    path4 = create_typography_first(video_id, summary, keywords, youtube_url,
                                        os.path.join(output_dir, f"{video_id}-typography.html"))
    print(f"✅ {path4}")

    # 5. Data Visualization
    print("5/5: Data Visualization...")
    path5 = create_data_viz(video_id, summary, keywords, youtube_url,
                                os.path.join(output_dir, f"{video_id}-data-viz.html"))
    print(f"✅ {path5}")

    # 結果を出力
    result = {
        "video_id": video_id,
        "url": youtube_url,
        "summary_points": len(summary),
        "keywords": len(keywords),
        "segments": len(transcript),
        "design_patterns": [
            {
                "name": "Modern Clean",
                "path": path1,
                "description": "ミニマルでクリーン、白ベース、余計を活かしたシンプルなデザイン"
            },
            {
                "name": "Vibrant Gradient",
                "path": path2,
                "description": "鮮やかなグラデーション背景、動的なアニメーション、カラフルな配色"
            },
            {
                "name": "Dark Mode",
                "path": path3,
                "description": "ダークテーマ、ネオンカラーのアクセント、深い青グレーの背景"
            },
            {
                "name": "Typography First",
                "path": path4,
                "description": "巨大なタイポグラフィ、強調された文字、エレガントなセリフ体"
            },
            {
                "name": "Data Visualization",
                "path": path5,
                "description": "データ可視化重視、チャート風のキーワード表示、数量的な表現"
            }
        ],
        "timestamp": datetime.now().isoformat()
    }

    print("\n" + "="*60)
    print("✅ All 5 design patterns created!")
    print("="*60)
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
