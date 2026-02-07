#!/usr/bin/env python3
"""
ASCII Art Generator - Generative Art with Characters
Creates random patterns and shapes using ASCII characters.
"""

import random
import math
from datetime import datetime

class ASCIIArtGenerator:
    def __init__(self, width=80, height=40):
        self.width = width
        self.height = height

    def clear_canvas(self):
        return [[' ' for _ in range(self.width)] for _ in range(self.height)]

    def random_shape(self, canvas):
        """Draw random shapes: circles, rectangles, lines"""
        shape_type = random.choice(['circle', 'rect', 'line', 'spiral'])
        chars = random.choice(['@', '#', '*', '+', 'o', 'x', '~', ':'])
        
        cx, cy = random.randint(0, self.width-1), random.randint(0, self.height-1)
        
        if shape_type == 'circle':
            radius = random.randint(3, min(self.width, self.height) // 4)
            for y in range(self.height):
                for x in range(self.width):
                    dist = math.sqrt((x - cx)**2 + (y - cy)**2)
                    if abs(dist - radius) < 1.5:
                        canvas[y][x] = chars
                        
        elif shape_type == 'rect':
            w, h = random.randint(5, 20), random.randint(3, 10)
            x1, y1 = max(0, cx - w//2), max(0, cy - h//2)
            x2, y2 = min(self.width-1, cx + w//2), min(self.height-1, cy + h//2)
            for x in range(x1, x2+1):
                if 0 <= y1 < self.height: canvas[y1][x] = chars
                if 0 <= y2 < self.height: canvas[y2][x] = chars
            for y in range(y1, y2+1):
                if 0 <= x1 < self.width: canvas[y][x1] = chars
                if 0 <= x2 < self.width: canvas[y][x2] = chars
                
        elif shape_type == 'line':
            x2, y2 = random.randint(0, self.width-1), random.randint(0, self.height-1)
            steps = max(abs(x2 - cx), abs(y2 - cy)) or 1
            for i in range(steps + 1):
                t = i / steps
                x, y = int(cx + (x2 - cx) * t), int(cy + (y2 - cy) * t)
                if 0 <= x < self.width and 0 <= y < self.height:
                    canvas[y][x] = chars
                    
        elif shape_type == 'spiral':
            angle = 0
            radius = 1
            max_radius = min(self.width, self.height) // 3
            x, y = cx, cy
            for _ in range(200):
                nx = int(cx + radius * math.cos(angle))
                ny = int(cy + radius * math.sin(angle))
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    canvas[ny][nx] = chars
                angle += 0.3
                radius += 0.1
                if radius > max_radius:
                    break

    def random_pattern(self, canvas):
        """Add random patterns: dots, noise, waves"""
        pattern_type = random.choice(['dots', 'noise', 'waves', 'gradient'])
        
        if pattern_type == 'dots':
            for _ in range(random.randint(20, 100)):
                x, y = random.randint(0, self.width-1), random.randint(0, self.height-1)
                canvas[y][x] = random.choice(['.', "'", '`', '°'])
                
        elif pattern_type == 'noise':
            for y in range(self.height):
                for x in range(self.width):
                    if random.random() < 0.05:
                        canvas[y][x] = random.choice(['·', ':', '·'])
                        
        elif pattern_type == 'waves':
            chars = ['~', '~', '-', '_', '']
            phase = random.uniform(0, math.pi * 2)
            frequency = random.uniform(0.05, 0.2)
            for y in range(self.height):
                for x in range(self.width):
                    offset = int(5 * math.sin(x * frequency + phase))
                    if 0 <= y + offset < self.height and random.random() < 0.3:
                        canvas[y + offset][x] = random.choice(chars[:-1])
                        
        elif pattern_type == 'gradient':
            char = random.choice(['#', '@', '*', '+', ':', '.', ' '])
            gradient = [c for c in '#@*+:. ']
            for y in range(self.height):
                intensity = y / self.height
                char = gradient[min(int(intensity * len(gradient)), len(gradient)-1)]
                for x in range(self.width):
                    if canvas[y][x] == ' ' and random.random() < 0.1:
                        canvas[y][x] = char

    def generate(self, num_shapes=10, num_patterns=5):
        """Generate a complete ASCII art piece"""
        canvas = self.clear_canvas()
        
        # Draw shapes
        for _ in range(num_shapes):
            self.random_shape(canvas)
            
        # Add patterns
        for _ in range(num_patterns):
            self.random_pattern(canvas)
            
        # Convert to string
        result = '\n'.join(''.join(row) for row in canvas)
        return result

def main():
    print("\n" + "="*80)
    print("🎨 ASCII ART GENERATOR")
    print("="*80)
    
    generator = ASCIIArtGenerator(width=80, height=40)
    
    # Generate 3 different art pieces
    for i in range(1, 4):
        print(f"\n--- Variation {i} ---\n")
        art = generator.generate(
            num_shapes=random.randint(5, 15),
            num_patterns=random.randint(2, 6)
        )
        print(art)
        
    print("\n" + "="*80)
    print(f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
