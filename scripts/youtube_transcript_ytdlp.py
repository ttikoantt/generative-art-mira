#!/usr/bin/env python3
"""
YouTube Transcript Fetcher using yt-dlp
yt-dlpを使ってYouTube動画のtranscriptを取得
"""

import sys
import json
import os
import subprocess
import re

def get_video_id(url):
    """YouTube URLから動画IDを抽出"""
    if "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    elif "watch?v=" in url:
        return url.split("watch?v=")[1].split("&")[0]
    return url

def download_subs_with_ytdlp(video_id):
    """yt-dlpを使って字幕をダウンロード"""
    url = f"https://www.youtube.com/watch?v={video_id}"
    ytdlp_path = os.path.expanduser('~/Library/Python/3.11/bin/yt-dlp')

    # 作業ディレクトリ
    work_dir = f"/tmp/youtube_subs_{video_id}"
    os.makedirs(work_dir, exist_ok=True)

    try:
        # 字幕をダウンロード（VTT形式）
        result = subprocess.run(
            [
                ytdlp_path,
                '--write-subs',
                '--write-auto-subs',
                '--sub-langs', 'all',
                '--sub-format', 'vtt',
                '--skip-download',
                '--output', f'{work_dir}/sub',
                url
            ],
            capture_output=True,
            text=True,
            timeout=60
        )

        # VTTファイルを探す
        vtt_files = []
        for file in os.listdir(work_dir):
            if file.endswith('.vtt'):
                vtt_files.append(os.path.join(work_dir, file))

        if not vtt_files:
            print("No subtitle files found")
            return None

        # 最初のVTTファイルを読み込む
        vtt_file = vtt_files[0]
        with open(vtt_file, 'r', encoding='utf-8') as f:
            vtt_content = f.read()

        # VTTをパースしてtranscriptを作成
        transcript = parse_vtt(vtt_content)

        # クリーンアップ
        for file in vtt_files:
            os.remove(file)
        os.rmdir(work_dir)

        return transcript

    except Exception as e:
        print(f"Error: {e}")
        # クリーンアップ
        if os.path.exists(work_dir):
            for file in os.listdir(work_dir):
                os.remove(os.path.join(work_dir, file))
            os.rmdir(work_dir)
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
                transcript.append({
                    'start': current_start,
                    'end': current_end,
                    'text': ' '.join(current_text)
                })

            # 新しいセグメントを開始
            current_start = timestamp_to_seconds(timestamp_match.group(1))
            current_end = timestamp_to_seconds(timestamp_match.group(2))
            current_text = []

        elif line and not line.startswith('WEBVTT') and not line.startswith('NOTE'):
            # テキスト行
            current_text.append(line)

    # 最後のセグメントを保存
    if current_start is not None and current_text:
        transcript.append({
            'start': current_start,
            'end': current_end,
            'text': ' '.join(current_text)
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

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 youtube_transcript_ytdlp.py <youtube_url>")
        sys.exit(1)

    url = sys.argv[1]
    video_id = get_video_id(url)

    if not video_id:
        print("❌ Invalid YouTube URL")
        sys.exit(1)

    print(f"🎬 Fetching transcript for: {video_id}")

    # transcriptを取得
    transcript = download_subs_with_ytdlp(video_id)

    if not transcript or len(transcript) == 0:
        print("❌ No transcript available")
        sys.exit(1)

    print(f"✅ Got transcript with {len(transcript)} segments")

    # transcriptをテキストに変換
    full_text = "\n".join([
        f"[{format_time(item['start'])}] {item['text']}"
        for item in transcript
    ])

    # JSONで保存
    output_data = {
        "video_id": video_id,
        "transcript": transcript,
        "full_text": full_text
    }

    output_file = f"/Users/naokitomono/Documents/generative-art-by-mira/outputs/transcripts/{video_id}.json"
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"✅ Saved to: {output_file}")

    # 要約を表示
    print("\n📄 Transcript Preview (first 1000 chars):")
    print(full_text[:1000] + "..." if len(full_text) > 1000 else full_text)

if __name__ == "__main__":
    main()
