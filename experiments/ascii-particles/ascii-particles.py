#!/usr/bin/env python3
"""
ASCII Particle System - カラフルなパーティクルアート

物理法則に基づいたパーティクルシステムをASCIIで表現
重力、摩擦、弾性衝突を実装
"""

import random
import math
from dataclasses import dataclass
from typing import List

# ANSI color codes
COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'reset': '\033[0m',
    'bold': '\033[1m',
}

PARTICLE_CHARS = ['●', '○', '◐', '◑', '◒', '◓', '✦', '✧', '★', '☆', '♦', '♢', '◆', '◇', '❋', '❊']
COLOR_KEYS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

@dataclass
class Vector:
    x: float
    y: float

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

class Particle:
    def __init__(self, x: float, y: float, canvas_width: int, canvas_height: int):
        self.pos = Vector(x, y)
        self.vel = Vector(random.uniform(-2, 2), random.uniform(-2, 2))
        self.acc = Vector(0, 0)
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.char = random.choice(PARTICLE_CHARS)
        self.color_name = random.choice(COLOR_KEYS)
        self.life = random.uniform(0.5, 1.0)
        self.decay = random.uniform(0.002, 0.008)
        self.size = random.uniform(0.5, 1.5)

    def apply_force(self, force: Vector):
        self.acc = self.acc + force

    def update(self):
        # Update velocity and position
        self.vel = self.vel + self.acc
        self.pos = self.pos + self.vel
        self.acc = Vector(0, 0)  # Reset acceleration

        # Boundary collision with energy loss
        bounce = 0.8
        if self.pos.x < 0:
            self.pos.x = 0
            self.vel.x *= -bounce
        elif self.pos.x >= self.canvas_width:
            self.pos.x = self.canvas_width - 1
            self.vel.x *= -bounce

        if self.pos.y < 0:
            self.pos.y = 0
            self.vel.y *= -bounce
        elif self.pos.y >= self.canvas_height:
            self.pos.y = self.canvas_height - 1
            self.vel.y *= -bounce

        # Apply friction
        friction = 0.99
        self.vel = self.vel * friction

        # Apply gravity (gentle)
        gravity = Vector(0, 0.03)
        self.vel = self.vel + gravity

        # Life decay
        self.life -= self.decay

    def is_alive(self):
        return self.life > 0

class ParticleSystem:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.particles: List[Particle] = []
        self.frame = 0

    def emit(self, count: int = 1):
        """Emit new particles from center"""
        cx, cy = self.width / 2, self.height / 2
        for _ in range(count):
            # Add some randomness to emission position
            x = cx + random.uniform(-3, 3)
            y = cy + random.uniform(-3, 3)
            p = Particle(x, y, self.width, self.height)
            # Burst outward
            angle = random.uniform(0, math.pi * 2)
            speed = random.uniform(0.8, 2.5)
            p.vel = Vector(math.cos(angle) * speed, math.sin(angle) * speed)
            self.particles.append(p)

    def update(self):
        self.frame += 1
        for p in self.particles:
            p.update()
        # Remove dead particles
        self.particles = [p for p in self.particles if p.is_alive()]

    def render(self) -> str:
        """Render a single frame as colored text"""
        # Create canvas with particle positions
        grid = {}
        for p in self.particles:
            x = int(round(p.pos.x))
            y = int(round(p.pos.y))
            if 0 <= x < self.width and 0 <= y < self.height:
                key = (y, x)
                # If multiple particles in same spot, pick the one with highest life
                if key not in grid or p.life > grid[key][0]:
                    grid[key] = (p.life, p)

        # Build output lines
        lines = []
        for y in range(self.height):
            line_parts = []
            for x in range(self.width):
                if (y, x) in grid:
                    life, p = grid[(y, x)]
                    color = COLORS[p.color_name]
                    line_parts.append(f'{color}{p.char}{COLORS["reset"]}')
                else:
                    line_parts.append(' ')
            lines.append(''.join(line_parts))

        return '\n'.join(lines)

def generate_static_art():
    """Generate a static ASCII art snapshot"""
    WIDTH, HEIGHT = 50, 25

    ps = ParticleSystem(WIDTH, HEIGHT)

    # Initial burst
    ps.emit(count=30)

    # Run simulation for some frames to get nice spread
    for _ in range(15):
        # Add more particles periodically
        if _ % 5 == 0:
            ps.emit(count=10)
        ps.update()

    # Add one final burst
    ps.emit(count=15)
    ps.update()

    # Render and return
    header = f'{COLORS["bold"]}{COLORS["cyan"]}✨ ASCII Particle Art ✨{COLORS["reset"]}\n'
    header += f'Frame: {ps.frame} | Particles: {len(ps.particles)}\n'
    header += '━' * WIDTH + '\n'

    art = ps.render()

    footer = '\n' + '━' * WIDTH
    footer += f'\n{COLORS["yellow"]}Physics: Gravity + Friction + Elastic Collision{COLORS["reset"]}'
    footer += f'\n{COLORS["green"]}Each particle has unique: velocity, life, color, shape{COLORS["reset"]}'

    return header + art + footer

def main():
    print(generate_static_art())

if __name__ == '__main__':
    main()
