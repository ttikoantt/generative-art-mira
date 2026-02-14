#!/usr/bin/env python3
"""
YouTube Transcript Fetcher & Visualizer
yt-dlpを使ってtranscriptを取得し、要約＆ビジュアライゼーションを作成
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
        # 字幕をダウンロード
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

        # VTTファイルが存在するか確認
        if not os.path.exists(temp_file):
            # ファイル名が異なる可能性があるので確認
            for file in os.listdir('/tmp'):
                if file.startswith(f'youtube_subs_{video_id}') and file.endswith('.vtt'):
                    temp_file = f'/tmp/{file}'
                    break

        if os.path.exists(temp_file):
            with open(temp_file, 'r', encoding='utf-8') as f:
                vtt_content = f.read()

            # クリーンアップ
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

        # タイムスタンプ行（00:00:00.000 --> 00:00:05.000）
        timestamp_match = re.match(r'(\d{2}:\d{2}:\d{2}\.\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2}\.\d{3})', line)

        if timestamp_match:
            # 前のセグメントを保存
            if current_start is not None and current_text:
                text = ' '.join(current_text)
                # VTTタグを削除
                text = re.sub(r'<c>|</c>|<\d{2}:\d{2}:\d{2}\.\d{3}>', '', text)
                text = re.sub(r'<\d{2}:\d{2}:\d{2}\.\d{3}><c>|</c>', '', text)
                if text.strip():
                    transcript.append({
                        'start': current_start,
                        'end': current_end,
                        'text': text.strip()
                    })

            # 新しいセグメントを開始
            current_start = timestamp_to_seconds(timestamp_match.group(1))
            current_end = timestamp_to_seconds(timestamp_match.group(2))
            current_text = []

        elif line and not line.startswith('WEBVTT') and not line.startswith('Kind:') and not line.startswith('Language:'):
            # テキスト行
            current_text.append(line)

    # 最後のセグメントを保存
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
    """タイムスタンプを秒に変換（00:00:00.000 -> float）"""
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

def summarize_transcript(transcript, max_points=15):
    """transcriptを要約（重要なポイントを抽出）"""
    if not transcript:
        return []

    # テキストを結合
    full_text = ' '.join([item['text'] for item in transcript])

    # セグメントの長さに基づいて重要度を計算
    scored_segments = []
    for seg in transcript:
        duration = seg['end'] - seg['start']
        word_count = len(seg['text'].split())
        score = duration * (1 + word_count / 10)  # 長さ＆単語数でスコアリング
        scored_segments.append({
            'text': seg['text'],
            'start': seg['start'],
            'end': seg['end'],
            'score': score
        })

    # スコア順にソート
    scored_segments.sort(key=lambda x: x['score'], reverse=True)

    # 上位のセグメントを抽出
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

    # 時間順にソート
    key_points.sort(key=lambda x: x['start'])

    return key_points

def extract_keywords(transcript, top_n=30):
    """キーワード抽出"""
    from collections import Counter

    full_text = ' '.join([item['text'] for item in transcript]).lower()

    # 単語を抽出
    words = re.findall(r'\b[a-zA-Z]{3,}\b', full_text)

    # ストップワード除去
    stopwords = set(['the', 'and', 'that', 'have', 'for', 'not', 'you', 'with', 'this', 'but', 'his', 'from', 'they', 'she', 'her', 'been', 'than', 'its', 'who', 'was', 'are', 'will', 'would', 'could', 'should', 'about', 'after', 'into', 'over', 'their', 'your', 'what', 'when', 'make', 'like', 'just', 'time', 'them', 'more', 'some', 'only', 'were', 'said', 'each', 'does', 'done', 'come', 'also', 'well', 'much', 'even', 'such', 'because', 'any', 'most', 'many', 'then', 'than', 'too', 'very'])

    filtered_words = [w for w in words if w not in stopwords and len(w) > 3]

    # 頻度カウント
    word_counts = Counter(filtered_words)

    # 上位N個を取得
    top_keywords = word_counts.most_common(top_n)

    return [{"word": word, "count": count} for word, count in top_keywords]

def create_visualization(video_id, transcript, summary, keywords, video_url, output_dir):
    """ビジュアライズHTMLを生成"""
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{video_id}.html")

    total_duration = transcript[-1]['end'] if transcript else 0

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

        .timeline {{
            position: relative;
            padding-left: 30px;
            max-height: 600px;
            overflow-y: auto;
        }}

        .timeline::-webkit-scrollbar {{
            width: 8px;
        }}

        .timeline::-webkit-scrollbar-track {{
            background: #f1f1f1;
            border-radius: 10px;
        }}

        .timeline::-webkit-scrollbar-thumb {{
            background: #667eea;
            border-radius: 10px;
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
            font-size: 0.9rem;
        }}

        .timeline-text {{
            color: #333;
            line-height: 1.6;
        }}

        .keyword-cloud {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            justify-content: center;
            max-height: 400px;
            overflow-y: auto;
            padding: 10px;
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

        .video-button {{
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

        .video-button:hover {{
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
            <h1>🎬 YouTube動画要約＆ビジュアライゼーション</h1>
            <p>Video ID: {video_id}</p>
            <a href="{video_url}" target="_blank" class="video-button">▶️ 動画を見る</a>
        </div>

        <div class="grid">
            <!-- タイムライン -->
            <div class="card">
                <h2>📅 重要ポイントタイムライン</h2>
                <div class="timeline">
    """

    # タイムラインアイテム追加
    for item in summary:
        html += f"""
                    <div class="timeline-item" onclick="jumpToTime({item['start']})">
                        <div class="timeline-time">⏰ {format_time(item['start'])}</div>
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
                    <div class="stat-item">
                        <div class="stat-value">{len(transcript)}</div>
                        <div class="stat-label">セグメント数</div>
                    </div>
                    <div class="stat-item">
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

    # 保存
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    return output_path

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 youtube_summarizer_v2.py <youtube_url>")
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

    # ビジュアライズ作成
    print("🎨 Creating visualization...")
    output_dir = "/Users/naokitomono/Documents/generative-art-by-mira/outputs/youtube-summaries"
    html_path = create_visualization(video_id, transcript, summary, keywords, youtube_url, output_dir)

    print(f"✅ Visualization created: {html_path}")

    # 結果を出力
    result = {
        "video_id": video_id,
        "url": youtube_url,
        "summary_points": len(summary),
        "keywords": len(keywords),
        "segments": len(transcript),
        "html_path": html_path,
        "timestamp": datetime.now().isoformat()
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
