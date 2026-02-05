#!/usr/bin/env python3
"""
パーティクルアニメーションのデモ（3秒で自動終了）
"""

import time
import math
import random

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
    print('\033[2J\033[H', end='', flush=True)

def get_color(char, t):
    color_cycle = ['cyan', 'magenta', 'yellow', 'green', 'blue']
    idx = int((t * 2 + ord(char)) % len(color_cycle))
    return COLORS[color_cycle[idx]] + char + COLORS['reset']

def particles_animation():
    width = 70
    height = 25
    duration = 3  # 3秒で終了
    start_time = time.time()

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
            self.vy += 0.02
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

    while time.time() - start_time < duration:
        buffer = [[' ' for _ in range(width)] for _ in range(height)]

        for p in particles:
            p.update()
            ix, iy = int(p.x), int(p.y)
            if 0 <= ix < width and 0 <= iy < height:
                buffer[iy][ix] = p.get_render_char()

        clear_screen()
        print('✨ Particle Art - 3 second demo\n')

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

    print("\n✨ Demo complete!")

if __name__ == '__main__':
    particles_animation()
