#!/usr/bin/env python3
"""
YouTube Transcript Fetcher & Visualizer (Graphic Recording Style)
yt-dlpを使ってtranscriptを取得し、グラレコ風の要約＆ビジュアライゼーションを作成
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

def summarize_transcript(transcript, max_points=15):
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

def extract_keywords(transcript, top_n=30):
    """キーワード抽出"""
    from collections import Counter

    full_text = ' '.join([item['text'] for item in transcript]).lower()
    words = re.findall(r'\b[a-zA-Z]{3,}\b', full_text)

    stopwords = set(['the', 'and', 'that', 'have', 'for', 'not', 'you', 'with', 'this', 'but', 'his', 'from', 'they', 'she', 'her', 'been', 'than', 'its', 'who', 'was', 'are', 'will', 'would', 'could', 'should', 'about', 'after', 'into', 'over', 'their', 'your', 'what', 'when', 'make', 'like', 'just', 'time', 'them', 'more', 'some', 'only', 'were', 'said', 'each', 'does', 'done', 'come', 'also', 'well', 'much', 'even', 'such', 'because', 'any', 'most', 'many', 'then', 'than', 'too', 'very'])

    filtered_words = [w for w in words if w not in stopwords and len(w) > 3]
    word_counts = Counter(filtered_words)
    top_keywords = word_counts.most_common(top_n)

    return [{"word": word, "count": count} for word, count in top_keywords]

def create_visualization(video_id, transcript, summary, keywords, video_url, output_dir):
    """グラレコ風ビジュアライゼーションHTMLを生成"""
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{video_id}.html")

    total_duration = transcript[-1]['end'] if transcript else 0

    # タイムラインアイテムHTML生成
    timeline_items = []
    for item in summary:
        timeline_items.append(f"""
                    <div class="timeline-item" onclick="jumpToTime({item['start']})">
                        <div class="timeline-time">⏰ {format_time(item['start'])}</div>
                        <div class="timeline-text">{item['text']}</div>
                    </div>
        """)

    timeline_html = '\n'.join(timeline_items)

    # キーワードHTML生成
    max_count = max([k["count"] for k in keywords]) if keywords else 1
    keyword_items = []

    for kw in keywords:
        size_class = "size-md"
        if kw["count"] > max_count * 0.7:
            size_class = "size-lg"
        elif kw["count"] < max_count * 0.3:
            size_class = "size-sm"

        keyword_items.append(f'<span class="keyword {size_class}">{kw["word"]}</span>')

    keyword_html = '\n                    '.join(keyword_items)

    # テンプレート読み込み
    template_path = "/Users/naokitomono/Documents/generative-art-by-mira/templates/youtube_summary_template.html"

    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    # プレースホルダー置換
    html = template.replace('{VIDEO_ID}', video_id)
    html = html.replace('{VIDEO_URL}', video_url)
    html = html.replace('{DURATION}', format_time(total_duration))
    html = html.replace('{TIMELINE_ITEMS}', timeline_html)
    html = html.replace('{KEYWORD_ITEMS}', keyword_html)
    html = html.replace('{SUMMARY_COUNT}', str(len(summary)))
    html = html.replace('{KEYWORD_COUNT}', str(len(keywords)))
    html = html.replace('{SEGMENT_COUNT}', str(len(transcript)))

    # 保存
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    return output_path

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 youtube_summarizer_graphic.py <youtube_url>")
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

    # ビジュアライゼーション作成
    print("🎨 Creating graphic recording style visualization...")
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
