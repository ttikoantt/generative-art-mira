#!/usr/bin/env python3
"""
Adobe製品ニュース・リリース追跡スクリプト（改良版）
"""

import json
import re
from datetime import datetime, timedelta
from pathlib import Path
import subprocess
import hashlib

# 設定
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
WORKSPACE = PROJECT_ROOT.parent / ".openclaw" / "workspace"
TRACKING_FILE = WORKSPACE / "memory" / "adobe-tracking.json"
LAST_CHECK_FILE = WORKSPACE / "memory" / "last-adobe-check.txt"

# ニュースソース（URLを最新のものに更新）
NEWS_SOURCES = {
    "photoshop_release": {
        "name": "Photoshop Release Notes",
        "url": "https://helpx.adobe.com/photoshop/whats-new.html",
        "type": "release_notes"
    },
    "illustrator_release": {
        "name": "Illustrator Release Notes",
        "url": "https://helpx.adobe.com/illustrator/whats-new.html",
        "type": "release_notes"
    },
    "premiere_release": {
        "name": "Premiere Pro Release Notes",
        "url": "https://helpx.adobe.com/premiere-pro/whats-new.html",
        "type": "release_notes"
    },
    "lightroom_release": {
        "name": "Lightroom Release Notes",
        "url": "https://helpx.adobe.com/lightroom/whats-new.html",
        "type": "release_notes"
    },
    "aftereffects_release": {
        "name": "After Effects Release Notes",
        "url": "https://helpx.adobe.com/after-effects/whats-new.html",
        "type": "release_notes"
    },
    "adobe_blog": {
        "name": "Adobe Blog",
        "url": "https://blog.adobe.com/",
        "type": "blog"
    }
}

def load_tracking_data():
    """追跡データを読み込む"""
    if TRACKING_FILE.exists():
        with open(TRACKING_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_tracking_data(data):
    """追跡データを保存"""
    TRACKING_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(TRACKING_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_last_check():
    """最終チェック時刻を読み込む"""
    if LAST_CHECK_FILE.exists():
        with open(LAST_CHECK_FILE, 'r') as f:
            return datetime.fromisoformat(f.read().strip())
    return datetime.now() - timedelta(days=30)

def save_last_check(check_time):
    """最終チェック時刻を保存"""
    LAST_CHECK_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LAST_CHECK_FILE, 'w') as f:
        f.write(check_time.isoformat())

def generate_content_hash(content):
    """コンテンツハッシュを生成"""
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def check_url_changes(source_key, url):
    """URLの変更をチェック"""
    try:
        result = subprocess.run(
            ['curl', '-s', '-L', url],
            capture_output=True,
            text=True,
            timeout=15
        )

        if result.returncode == 0:
            # ページの内容から日付情報を抽出
            content = result.stdout
            content_hash = generate_content_hash(content[:10000])  # 最初の10KBをハッシュ化

            tracking_data = load_tracking_data()
            last_hash = tracking_data.get(source_key, {}).get('last_hash')

            # 最新の情報を抽出（現在の年または近い将来のみ）
            current_year = datetime.now().year
            dates = re.findall(r'(20[2-9][0-9])', content)
            # 不自然な年（2095など）を除外
            valid_dates = [int(d) for d in dates if current_year - 1 <= int(d) <= current_year + 2]
            latest_year = str(max(valid_dates)) if valid_dates else 'N/A'

            is_changed = last_hash != content_hash

            tracking_data[source_key] = {
                'name': NEWS_SOURCES[source_key]['name'],
                'url': url,
                'type': NEWS_SOURCES[source_key]['type'],
                'last_hash': content_hash,
                'latest_year': latest_year,
                'last_checked': datetime.now().isoformat(),
                'changed': is_changed
            }
            save_tracking_data(tracking_data)

            return is_changed, latest_year
        return False, 'Error'
    except Exception as e:
        print(f"Error checking {url}: {e}")
        return False, 'Error'

def generate_report(all_items):
    """レポートを生成"""
    if not all_items:
        return ""

    report = ["📰 **Adobe製品最新情報**\n"]
    report.append(f"チェック時刻: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")

    release_notes = [item for item in all_items if item['type'] == 'release_notes']
    blogs = [item for item in all_items if item['type'] == 'blog']

    if release_notes:
        report.append("\n📋 **リリースノート:**")
        for item in release_notes:
            year = item.get('latest_year', 'N/A')
            report.append(f"- [{item['name']}]({item['url']}) (最新: {year})")

    if blogs:
        report.append("\n📝 **ブログ/ニュース:**")
        for item in blogs:
            year = item.get('latest_year', 'N/A')
            report.append(f"- [{item['name']}]({item['url']}) (最新: {year})")

    return "\n".join(report)

def main():
    """メイン処理"""
    print("🔍 Adobe製品ニュースチェック中...")

    for source_key, source_info in NEWS_SOURCES.items():
        print(f"Checking {source_info['name']}...")
        is_changed, latest_year = check_url_changes(source_key, source_info['url'])

        if is_changed:
            print(f"  → 変更検出！最新年: {latest_year}")
        else:
            print(f"  → 変更なし (最新年: {latest_year})")

    # 最新のチェック時刻を保存
    save_last_check(datetime.now())

    # レポートを生成
    tracking_data = load_tracking_data()
    all_items = list(tracking_data.values())

    report = generate_report(all_items)
    return report

if __name__ == "__main__":
    report = main()
    if report:
        print("\n" + "="*60)
        print(report)
        print("="*60)
