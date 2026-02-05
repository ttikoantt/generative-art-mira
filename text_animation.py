#!/usr/bin/env python3
"""
Text-based Animation Art
クリエイティブなテキストアニメーション集
"""

import time
import math
import random
import sys
from collections import deque

# ANSIカラーコード
COLORS = {
    'reset': '\033[0m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
}

def clear_screen():
    """画面をクリア"""
    print('\033[2J\033[H', end='', flush=True)

def get_color(char, t):
    """時間に応じて色を変える"""
    color_cycle = ['cyan', 'magenta', 'yellow', 'green', 'blue']
    idx = int((t * 2 + ord(char)) % len(color_cycle))
    return COLORS[color_cycle[idx]] + char + COLORS['reset']

def sine_wave_animation():
    """サイン波のアニメーション"""
    width = 60
    height = 20
    t = 0

    while True:
        lines = []
        for y in range(height):
            line = []
            for x in range(width):
                # 複数のサイン波を組み合わせる
                wave1 = math.sin((x + t) * 0.1) * 5
                wave2 = math.sin((x + t * 0.7) * 0.2 + 1) * 3
                wave3 = math.cos((y * 0.3 + t * 0.5)) * 2

                # 中心からの距離
                center_dist = abs(y - height // 2)

                # 波の合成
                combined = wave1 + wave2 + wave3

                # 閾値で文字を決定
                if abs(combined - center_dist) < 1.5:
                    char = '●'
                elif abs(combined - center_dist) < 3:
                    char = '○'
                elif abs(combined - center_dist) < 5:
                    char = '·'
                else:
                    char = ' '

                line.append(get_color(char, t) if char != ' ' else ' ')
            lines.append(''.join(line))

        clear_screen()
        print('🌊 Sine Wave Art - Ctrl+C to exit\n')
        print('\n'.join(lines))
        t += 0.3
        time.sleep(0.05)

def spiral_animation():
    """螺旋パターンのアニメーション"""
    width = 60
    height = 25
    t = 0

    while True:
        lines = []
        for y in range(height):
            line = []
            for x in range(width):
                # 中心からの距離と角度
                cx, cy = width // 2, height // 2
                dx, dy = x - cx, y - cy
                dist = math.sqrt(dx * dx + dy * dy)
                angle = math.atan2(dy, dx)

                # 螺旋の計算
                spiral = (dist - t * 2) % 15

                # パターンの決定
                if abs(spiral) < 1:
                    char = '█'
                elif abs(spiral - 2) < 1:
                    char = '▓'
                elif abs(spiral - 4) < 1:
                    char = '▒'
                elif abs(spiral - 6) < 1:
                    char = '░'
                else:
                    char = ' '

                line.append(get_color(char, t) if char != ' ' else ' ')
            lines.append(''.join(line))

        clear_screen()
        print('🌀 Spiral Art - Ctrl+C to exit\n')
        print('\n'.join(lines))
        t += 0.2
        time.sleep(0.05)

def particles_animation():
    """パーティクルシステム"""
    width = 70
    height = 25

    # パーティクルクラス
    class Particle:
        def __init__(self):
            self.reset()

        def reset(self):
            self.x = width // 2
            self.y = height // 2
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(0.5, 2)
            self.vx = math.cos(angle) * speed
            self.vy = math.sin(angle) * speed
            self.life = random.randint(30, 80)
            self.max_life = self.life
            self.char = random.choice(['●', '○', '◆', '◇', '★', '☆', '·'])

        def update(self):
            self.x += self.vx
            self.y += self.vy
            self.vy += 0.02  # 重力
            self.life -= 1

            if self.life <= 0 or self.x < 0 or self.x >= width or self.y < 0 or self.y >= height:
                self.reset()

        def get_render_char(self):
            alpha = self.life / self.max_life
            if alpha > 0.7:
                return self.char
            elif alpha > 0.4:
                return '·'
            else:
                return '·'

    particles = [Particle() for _ in range(80)]
    t = 0

    while True:
        # 画面バッファ
        buffer = [[' ' for _ in range(width)] for _ in range(height)]

        # パーティクルを更新
        for p in particles:
            p.update()
            ix, iy = int(p.x), int(p.y)
            if 0 <= ix < width and 0 <= iy < height:
                buffer[iy][ix] = p.get_render_char()

        # 描画
        clear_screen()
        print('✨ Particle Art - Ctrl+C to exit\n')

        for y in range(height):
            line = []
            for x in range(width):
                char = buffer[y][x]
                if char != ' ':
                    line.append(get_color(char, t))
                else:
                    line.append(' ')
            print(''.join(line))

        t += 0.1
        time.sleep(0.04)

def matrix_rain():
    """マトリックス風の雨"""
    width = 60
    height = 25

    # カラムごとの状態
    columns = [{'pos': random.randint(0, height), 'speed': random.uniform(0.3, 1.0)}
               for _ in range(width)]

    # 文字セット
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZアイウエオカキクケコ'

    t = 0

    while True:
        # 画面バッファ
        buffer = [[' ' for _ in range(width)] for _ in range(height)]

        # 各カラムを更新
        for x, col in enumerate(columns):
            col['pos'] += col['speed']
            if col['pos'] >= height + 10:
                col['pos'] = -10
                col['speed'] = random.uniform(0.3, 1.0)

            # トレイルを描画
            for i in range(10):
                y = int(col['pos']) - i
                if 0 <= y < height:
                    if i == 0:
                        # 先頭は明るい
                        buffer[y][x] = '█'
                    elif i < 3:
                        # 中程は通常
                        buffer[y][x] = random.choice(chars)
                    else:
                        # 尾は薄い
                        buffer[y][x] = '·'

        # 描画
        clear_screen()
        print('💚 Matrix Rain - Ctrl+C to exit\n')

        for y in range(height):
            line = []
            for x in range(width):
                char = buffer[y][x]
                if char != ' ':
                    if char == '█':
                        line.append(COLORS['white'] + char + COLORS['reset'])
                    else:
                        line.append(COLORS['green'] + char + COLORS['reset'])
                else:
                    line.append(' ')
            print(''.join(line))

        t += 0.1
        time.sleep(0.05)

def main():
    """メニューを表示"""
    print("=" * 60)
    print("   🎨 Text Animation Art - Choose your animation")
    print("=" * 60)
    print()
    print("1. 🌊 Sine Wave (サイン波)")
    print("2. 🌀 Spiral (螺旋)")
    print("3. ✨ Particles (パーティクル)")
    print("4. 💚 Matrix Rain (マトリックス)")
    print("5. 🎲 Random (ランダム)")
    print()
    print("Ctrl+C anytime to exit")
    print()

    try:
        choice = input("Select (1-5, or just press Enter for random): ").strip()

        if choice == '1':
            sine_wave_animation()
        elif choice == '2':
            spiral_animation()
        elif choice == '3':
            particles_animation()
        elif choice == '4':
            matrix_rain()
        else:
            # ランダム選択
            animations = [sine_wave_animation, spiral_animation, particles_animation, matrix_rain]
            random.choice(animations)()
    except KeyboardInterrupt:
        print("\n\n👋 Thanks for watching! Bye!")
        sys.exit(0)

if __name__ == '__main__':
    main()
