#!/usr/bin/env python3
"""
YouTube Summarizer & Visualizer
DiscordでYouTube URLが投げられたら、要約とビジュアライズを自動生成
"""

import os
import sys
import json
import re
import subprocess
from datetime import datetime
from urllib.parse import urlparse, parse_qs

def get_video_id(url):
    """YouTube URLから動画IDを抽出"""
    if "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    elif "watch?v=" in url:
        return url.split("watch?v=")[1].split("&")[0]
    return None

def get_transcript_with_ytdlp(video_id):
    """yt-dlpを使ってtranscriptを取得"""
    url = f"https://www.youtube.com/watch?v={video_id}"
    ytdlp_path = os.path.expanduser('~/Library/Python/3.11/bin/yt-dlp')

    try:
        # 字幕をJSON形式で取得
        result = subprocess.run(
            [
                ytdlp_path,
                '--write-subs',
                '--write-auto-subs',
                '--skip-download',
                '--sub-format', 'json3',
                '--sub-langs', 'all',
                '--output', 'subtitles',
                url
            ],
            capture_output=True,
            text=True,
            timeout=60
        )

        # 字幕ファイルを探す
        for file in os.listdir('.'):
            if file.startswith('subtitles') and file.endswith('.json3'):
                with open(file, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                # 字幕データを解析
                if 'events' in data:
                    transcript = []
                    for event in data['events']:
                        if 'segs' in event:
                            text = ''.join([seg.get('utf8', '') for seg in event['segs']])
                            if text.strip():
                                transcript.append({
                                    'text': text.strip(),
                                    'start': event.get('tStartMs', 0) / 1000,
                                    'duration': event.get('dDurationMs', 0) / 1000
                                })

                    # 一時ファイルを削除
                    os.remove(file)

                    return transcript

    except Exception as e:
        print(f"Error with yt-dlp: {e}")

    return None

def get_transcript_with_api(video_id):
    """YouTube Data APIを使ってtranscriptを取得（簡易版）"""
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except Exception as e:
        print(f"Error with youtube-transcript-api: {e}")
        return None

def get_transcript(video_id):
    """複数の方法でtranscriptを取得"""
    # 方法1: youtube-transcript-api
    print("Trying youtube-transcript-api...")
    transcript = get_transcript_with_api(video_id)
    if transcript:
        return transcript

    # 方法2: yt-dlp
    print("Trying yt-dlp...")
    transcript = get_transcript_with_ytdlp(video_id)
    if transcript:
        return transcript

    return None

def extract_video_info(url):
    """URLから動画IDを取得"""
    video_id = get_video_id(url)
    if not video_id:
        return None
    return {"video_id": video_id, "url": url}

def summarize_transcript(transcript, max_points=10):
    """transcriptを要約（重要なポイントを抽出）"""
    if not transcript:
        return []

    # シンプルな要約：時間の長いセグメントを重要とみなす
    sorted_segments = sorted(transcript, key=lambda x: x["duration"], reverse=True)

    # 上位のセグメントを抽出
    key_points = []
    for seg in sorted_segments[:max_points * 2]:
        if len(key_points) >= max_points:
            break
        if seg["text"] not in [p["text"] for p in key_points]:
            key_points.append({
                "text": seg["text"],
                "start": seg["start"],
                "duration": seg["duration"]
            })

    # 時間順にソート
    key_points.sort(key=lambda x: x["start"])

    return key_points

def extract_keywords(transcript, top_n=20):
    """キーワード抽出（シンプルな頻度ベース）"""
    from collections import Counter
    import re

    # テキストを結合
    full_text = " ".join([item["text"] for item in transcript]).lower()

    # 単語を抽出
    words = re.findall(r'\b[a-zA-Z]+\b', full_text)

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

def format_time(seconds):
    """秒をHH:MM:SS形式に変換"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"

def create_visualization(video_id, transcript, summary, keywords, output_dir):
    """ビジュアライズHTMLを生成"""
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{video_id}.html")

    # タイムラインデータ作成
    timeline_data = []
    for point in summary:
        timeline_data.append({
            "time": format_time(point["start"]),
            "text": point["text"],
            "seconds": point["start"]
        })

    # セクション分割（5分ごと）
    total_duration = transcript[-1]["start"] + transcript[-1]["duration"] if transcript else 0
    sections = []
    section_duration = 300  # 5分
    for i in range(0, int(total_duration), section_duration):
        sections.append({
            "start": format_time(i),
            "end": format_time(min(i + section_duration, total_duration)),
            "duration": section_duration / 60
        })

    # HTML生成
    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YouTube Video Summary - {video_id}</title>
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

        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }}

        .card {{
            background: white;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }}

        .card h2 {{
            color: #667eea;
            margin-bottom: 20px;
            font-size: 1.8rem;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
        }}

        /* タイムライン */
        .timeline {{
            position: relative;
            padding-left: 30px;
        }}

        .timeline::before {{
            content: '';
            position: absolute;
            left: 10px;
            top: 0;
            bottom: 0;
            width: 3px;
            background: linear-gradient(to bottom, #667eea, #764ba2);
            border-radius: 3px;
        }}

        .timeline-item {{
            position: relative;
            margin-bottom: 20px;
            padding: 15px;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            border-radius: 10px;
            transition: transform 0.3s, box-shadow 0.3s;
            cursor: pointer;
        }}

        .timeline-item:hover {{
            transform: translateX(5px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }}

        .timeline-item::before {{
            content: '';
            position: absolute;
            left: -28px;
            top: 50%;
            transform: translateY(-50%);
            width: 12px;
            height: 12px;
            background: #667eea;
            border: 3px solid white;
            border-radius: 50%;
            box-shadow: 0 0 0 3px #667eea;
        }}

        .timeline-time {{
            font-weight: bold;
            color: #667eea;
            margin-bottom: 5px;
        }}

        .timeline-text {{
            color: #333;
            line-height: 1.6;
        }}

        /* キーワードクラウド */
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

        /* 統計カード */
        .stats {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;
            margin-top: 20px;
        }}

        .stat-item {{
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 15px;
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

        /* 全画面ボタン */
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
            .grid {{
                grid-template-columns: 1fr;
            }}

            .header h1 {{
                font-size: 1.8rem;
            }}

            .stats {{
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
            <h1>🎬 動画サマリー＆ビジュアライゼーション</h1>
            <p>YouTube ID: {video_id}</p>
        </div>

        <div class="grid">
            <!-- タイムライン -->
            <div class="card">
                <h2>📅 重要ポイントタイムライン</h2>
                <div class="timeline">
    """

    # タイムラインアイテム追加
    for item in timeline_data:
        html += f"""
                    <div class="timeline-item" onclick="jumpToTime({item['seconds']})">
                        <div class="timeline-time">⏰ {item['time']}</div>
                        <div class="timeline-text">{item['text']}</div>
                    </div>
        """

    html += """
                </div>
            </div>

            <!-- キーワードクラウド -->
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

                <div class="stats">
                    <div class="stat-item">
                        <div class="stat-value">{len(summary)}</div>
                        <div class="stat-label">重要ポイント</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">{len(keywords)}</div>
                        <div class="stat-label">キーワード</div>
                    </div>
                </div>
            </div>
        </div>

        <div class="card">
            <h2>📊 動画情報</h2>
            <p><strong>動画ID:</strong> {video_id}</p>
            <p><strong>総再生時間:</strong> {format_time(total_duration)}</p>
            <p><strong>セクション数:</strong> {len(sections)}</p>
            <p><strong>要約ポイント数:</strong> {len(summary)}</p>
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
            window.open(`https://www.youtube.com/watch?v={video_id}&t=${Math.floor(seconds)}s`, '_blank');
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
        print("Usage: python3 youtube_summarizer.py <youtube_url>")
        sys.exit(1)

    youtube_url = sys.argv[1]

    print(f"🎬 Processing YouTube URL: {youtube_url}")

    # 動画ID取得
    video_info = extract_video_info(youtube_url)
    if not video_info:
        print("❌ Failed to extract video ID")
        sys.exit(1)

    video_id = video_info["video_id"]
    print(f"📹 Video ID: {video_id}")

    # transcript取得
    print("📥 Fetching transcript...")
    transcript = get_transcript(video_id)
    if not transcript:
        print("❌ Failed to get transcript")
        sys.exit(1)

    print(f"✅ Got {len(transcript)} transcript segments")

    # 要約
    print("📝 Summarizing...")
    summary = summarize_transcript(transcript)
    print(f"✅ Generated {len(summary)} key points")

    # キーワード抽出
    print("🏷️ Extracting keywords...")
    keywords = extract_keywords(transcript)
    print(f"✅ Extracted {len(keywords)} keywords")

    # ビジュアライズ作成
    print("🎨 Creating visualization...")
    output_dir = "/Users/naokitomono/Documents/generative-art-by-mira/outputs/youtube-summaries"
    html_path = create_visualization(video_id, transcript, summary, keywords, output_dir)

    print(f"✅ Visualization created: {html_path}")

    # 結果を出力
    result = {
        "video_id": video_id,
        "url": youtube_url,
        "summary_points": len(summary),
        "keywords": len(keywords),
        "html_path": html_path,
        "timestamp": datetime.now().isoformat()
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
