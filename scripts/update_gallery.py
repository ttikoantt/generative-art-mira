#!/usr/bin/env python3
"""
成果物一覧自動更新スクリプト

artworks-manifest.json から index.html のギャラリーセクションを自動生成する。
新しい成果物を追加したら、このスクリプトを実行して index.html を更新する。

使用方法:
    python update_gallery.py
"""

import json
import os
from pathlib import Path
from datetime import datetime

# 設定
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
MANIFEST_PATH = PROJECT_ROOT / "artworks-manifest.json"
INDEX_PATH = PROJECT_ROOT / "index.html"

def load_manifest():
    """マニフェストファイルを読み込む"""
    with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_card_html(artwork):
    """作品カードのHTMLを生成"""
    # 拡張子で判定
    is_html = artwork['path'].endswith('.html')
    is_python = artwork.get('python', False)
    is_script = artwork.get('script', False)
    
    # クリック可能かどうか
    clickable = is_html or is_script
    
    # オンクリック属性
    if is_python:
        onclick = ""
        extra_button = f'''
            <div class="card-actions">
                <button class="card-button secondary" onclick="alert('Pythonスクリプトです。コードはGitHubで確認できます！')">
                    コードを見る
                </button>
            </div>
        '''
    elif is_script:
        onclick = f" onclick=\"openModal('{artwork['path']}', '{artwork['title']}', true)\""
        extra_button = ''
    else:
        onclick = f" onclick=\"openModal('{artwork['path']}', '{artwork['title']}')\""
        extra_button = ''
    
    # タグ生成
    tags_html = '\n                '.join([
        f'<span class="card-tag">{tag}</span>'
        for tag in artwork['tags']
    ])
    
    # カードHTML生成
    card_html = f'''            <!-- {artwork['title']} -->
            <div class="card"{onclick}>
                <div class="card-preview">
                    <div class="card-emoji">{artwork['emoji']}</div>
                </div>
                <div class="card-content">
                    <h3 class="card-title">{artwork['title']}</h3>
                    <p class="card-description">{artwork['description']}</p>
                    <div class="card-meta">
                        {tags_html}
                    </div>
                    {extra_button if not clickable else ''}
                </div>
            </div>
'''
    return card_html

def generate_gallery_html(manifest):
    """ギャラリーセクションのHTMLを生成"""
    # featured順、日付順でソート
    artworks = sorted(
        manifest['artworks'],
        key=lambda x: (not x.get('featured', False), x['date']),
        reverse=True
    )
    
    # 全作品カードを生成
    cards_html = ''.join([generate_card_html(artwork) for artwork in artworks])
    
    return cards_html

def update_index_html():
    """index.htmlを更新"""
    # マニフェスト読み込み
    manifest = load_manifest()
    
    # ギャラリーHTML生成
    gallery_html = generate_gallery_html(manifest)
    
    # 既存のindex.htmlを読み込み
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # ギャラリーセクションを置換
    # <!-- Gallery --> から </div> の閉じタグまでを探す
    import re
    
    # ギャラリーセクションを抽出
    pattern = r'(<div class="gallery">[\s\S]*?)(<div class="gallery-grid">[\s\S]*?)(</div>\s*</div>)'
    
    def replace_gallery(match):
        return match.group(1) + '\n        <div class="gallery-grid">\n' + gallery_html + '\n        </div>\n' + match.group(3)
    
    new_content = re.sub(pattern, replace_gallery, content)
    
    # 統計情報も更新
    stats = manifest['stats']
    stats_pattern = r'<div class="stat-number">(\d+)</div>\s*<div class="stat-label">作品数</div>'
    stats_replacement = f'<div class="stat-number">{stats["total"]}</div>\n                <div class="stat-label">作品数</div>'
    new_content = re.sub(stats_pattern, stats_replacement, new_content)
    
    # 書き込み
    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ index.htmlを更新しました！")
    print(f"   - 作品数: {stats['total']}作品")
    print(f"   - HTML: {stats['html']}作品")
    print(f"   - JavaScript: {stats['javascript']}作品")
    print(f"   - Python: {stats['python']}作品")

def add_artwork_to_manifest(artwork_data):
    """
    新しい作品をマニフェストに追加
    
    Args:
        artwork_data (dict): 作品情報
            {
                'id': 'unique-id',
                'title': '作品タイトル',
                'description': '説明文',
                'emoji': '🎨',
                'path': 'path/to/file.html',
                'tags': ['HTML Canvas', 'JavaScript'],
                'featured': True/False (optional)
            }
    """
    manifest = load_manifest()
    
    # 既存のIDかチェック
    existing_ids = [a['id'] for a in manifest['artworks']]
    if artwork_data['id'] in existing_ids:
        print(f"⚠️  ID '{artwork_data['id']}' は既に存在します。上書きします。")
        # 該当する作品を更新
        for i, artwork in enumerate(manifest['artworks']):
            if artwork['id'] == artwork_data['id']:
                manifest['artworks'][i] = artwork_data
                break
    else:
        # 新規追加
        manifest['artworks'].append(artwork_data)
    
    # 統計情報を更新
    manifest['stats']['total'] = len(manifest['artworks'])
    manifest['stats']['html'] = sum(1 for a in manifest['artworks'] if a['path'].endswith('.html'))
    manifest['stats']['javascript'] = sum(1 for a in manifest['artworks'] if a['path'].endswith('.js'))
    manifest['stats']['python'] = sum(1 for a in manifest['artworks'] if a.get('python', False))
    manifest['stats']['featured'] = sum(1 for a in manifest['artworks'] if a.get('featured', False))
    manifest['lastUpdated'] = datetime.now().isoformat()
    
    # マニフェストを保存
    with open(MANIFEST_PATH, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    
    print(f"✅ マニフェストに作品を追加しました: {artwork_data['title']}")
    
    # index.htmlも更新
    update_index_html()

def list_missing_artworks():
    """
    マニフェストに登録されていないファイルをリストアップ
    """
    import subprocess
    
    # 除外リスト
    exclude_files = {
        'index.html', 'artworks-manifest.json', 'update_gallery.py',
        '.gitignore', 'README.md'
    }
    
    # 全ファイルリストを取得
    result = subprocess.run(
        ['find', '.', '-type', 'f', '-name', '*.html', '-o', '-name', '*.js', '-o', '-name', '*.py'],
        capture_output=True,
        text=True,
        cwd=Path(__file__).parent
    )
    
    files = set()
    for line in result.stdout.strip().split('\n'):
        if line:
            # 先頭の ./ を削除
            file_path = line.lstrip('./')
            if file_path not in exclude_files:
                files.add(file_path)
    
    # マニフェストのファイルを取得
    manifest = load_manifest()
    manifest_files = set(a['path'] for a in manifest['artworks'])
    
    # 未登録のファイル
    missing = files - manifest_files
    
    if missing:
        print("📋 マニフェストに未登録のファイル:")
        for f in sorted(missing):
            print(f"   - {f}")
    else:
        print("✅ 全てのファイルがマニフェストに登録されています")
    
    return missing

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == 'check':
            list_missing_artworks()
        elif command == 'update':
            update_index_html()
        else:
            print(f"使い方: python update_gallery.py [check|update]")
            print("  check  - 未登録のファイルを確認")
            print("  update - index.htmlを更新")
    else:
        # デフォルトは更新
        update_index_html()
        print("\n💡 ヒント: 'python update_gallery.py check' で未登録のファイルを確認できます")
