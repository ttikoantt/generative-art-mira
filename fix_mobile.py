#!/usr/bin/env python3
"""
モバイル対応改善スクリプト

index.html のモバイル操作性を改善する：
- スクロール中の誤タップを防止
- タップとスワイプを明確に区別
- ホバー効果をモバイルで無効化
"""

import re
from pathlib import Path

# 設定
INDEX_PATH = Path(__file__).parent / "index.html"

def improve_mobile_usability():
    """モバイル操作性を改善"""
    
    # HTMLを読み込み
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 古いタッチイベントハンドラーを削除
    old_touch_handler = r'''        // Touch-friendly scroll for mobile
        if \('ontouchstart' in window\) \{
            document\.querySelectorAll\('\.card'\)\.forEach\(card => \{
                card\.addEventListener\('touchend', function\(\) \{
                    this\.click\(\);
                \}\);
            \}\);
        \}'''
    
    content = re.sub(old_touch_handler, '', content, flags=re.MULTILINE | re.DOTALL)
    
    # 新しいCSSを追加（モバイルでのホバー効果を無効化）
    css_addition = '''
        /* Mobile improvements */
        @media (hover: none) and (pointer: coarse) {
            .card:hover {
                transform: none;
                box-shadow: none;
            }

            .card:active {
                transform: scale(0.98);
                transition: transform 0.1s ease;
            }
        }

        /* Touch-friendly */
        @media (max-width: 768px) {
            .gallery-grid {
                gap: 25px;
            }

            .card {
                cursor: pointer;
                -webkit-tap-highlight-color: rgba(102, 126, 234, 0.2);
            }
        }
'''
    
    # 既存のモバイルレスポンシブCSSの前に追加
    mobile_css_pattern = r'(/\* Mobile Responsive \*/\n        @media \(max-width: 768px\) \{)'
    content = re.sub(mobile_css_pattern, css_addition + r'\1', content)
    
    # 新しいJavaScriptを追加
    new_js = '''        // Mobile-friendly touch handling
        if ('ontouchstart' in window) {
            document.querySelectorAll('.card').forEach(card => {
                let touchStartX = 0;
                let touchStartY = 0;
                let touchStartTime = 0;
                let isScrolling = false;

                card.addEventListener('touchstart', function(e) {
                    touchStartX = e.touches[0].clientX;
                    touchStartY = e.touches[0].clientY;
                    touchStartTime = Date.now();
                    isScrolling = false;
                }, { passive: true });

                card.addEventListener('touchmove', function(e) {
                    // スクロール中はフラグを立てる
                    isScrolling = true;
                }, { passive: true });

                card.addEventListener('touchend', function(e) {
                    const touchEndX = e.changedTouches[0].clientX;
                    const touchEndY = e.changedTouches[0].clientY;
                    const touchEndTime = Date.now();

                    // 移動距離を計算
                    const moveX = Math.abs(touchEndX - touchStartX);
                    const moveY = Math.abs(touchEndY - touchStartY);
                    const duration = touchEndTime - touchStartTime;

                    // スクロール中や、移動距離が大きい場合はタップとみなさない
                    if (isScrolling || moveX > 10 || moveY > 10 || duration > 300) {
                        return;
                    }

                    // 短いタップのみクリックとして扱う
                    this.click();
                }, { passive: false });
            });
        }

        // Close modal on Escape key'''
    
    # 古いJavaScriptを削除して新しいものを追加
    content = re.sub(
        r"        // Close modal on Escape key",
        new_js,
        content
    )
    
    # 書き込み
    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ モバイル操作性を改善しました！")
    print("   - スクロール中の誤タップを防止")
    print("   - タップとスワイプを明確に区別")
    print("   - ホバー効果をモバイルで無効化")
    print("   - カード間のマージンを調整")

if __name__ == '__main__':
    improve_mobile_usability()
