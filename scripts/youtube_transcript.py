#!/usr/bin/env python3
"""
YouTube Transcript Fetcher
YouTube動画のtranscriptを取得して要約
"""

import sys
import json
import os

# youtube-transcript-apiをインストール
try:
    from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled
except ImportError:
    print("Installing youtube-transcript-api...")
    os.system("pip3 install youtube-transcript-api")
    from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled

def get_video_id(url):
    """YouTube URLから動画IDを抽出"""
    if "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    elif "watch?v=" in url:
        return url.split("watch?v=")[1].split("&")[0]
    return url

def get_transcript(video_id, languages=None):
    """transcriptを取得"""
    if languages is None:
        languages = ['ja', 'en']  # 日本語、英語の順で試す

    for lang in languages:
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang])
            return transcript, lang
        except (NoTranscriptFound, TranscriptsDisabled) as e:
            continue
        except Exception as e:
            print(f"Error fetching transcript for {lang}: {e}")
            continue

    # どの言語でも見つからない場合、利用可能なtranscriptを試す
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript, 'unknown'
    except Exception as e:
        print(f"Error: {e}")
        return None, None

def format_time(seconds):
    """秒をHH:MM:SS形式に変換"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 youtube_transcript.py <youtube_url>")
        sys.exit(1)

    url = sys.argv[1]
    video_id = get_video_id(url)

    if not video_id:
        print("❌ Invalid YouTube URL")
        sys.exit(1)

    print(f"🎬 Fetching transcript for: {video_id}")

    # transcriptを取得
    transcript, lang = get_transcript(video_id)

    if not transcript:
        print("❌ No transcript available")
        sys.exit(1)

    print(f"✅ Got transcript in language: {lang}")
    print(f"📝 Total segments: {len(transcript)}")

    # transcriptをテキストに変換
    full_text = "\n".join([
        f"[{format_time(item['start'])}] {item['text']}"
        for item in transcript
    ])

    # JSONで保存
    output_data = {
        "video_id": video_id,
        "language": lang,
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
