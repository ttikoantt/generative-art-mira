#!/usr/bin/env python3
"""
🎨 Colorful ASCII Pattern Generator
Creates beautiful animated patterns in the terminal
"""

import math
import time
import sys
import signal

# ANSI color codes
COLORS = [
    '\033[91m', # Red
    '\033[92m', # Green
    '\033[93m', # Yellow
    '\033[94m', # Blue
    '\033[95m', # Magenta
    '\033[96m', # Cyan
    '\033[97m', # White
    '\033[38;5;206m', # Hot Pink
    '\033[38;5;214m', # Orange
    '\033[38;5;82m', # Bright Green
    '\033[38;5;141m', # Purple
    '\033[38;5;226m', # Gold
]
RESET = '\033[0m'
CLEAR = '\033[2J\033[H'

# Pattern characters
CHARS = '█▓▒░●○◌✦✧★☆❋❊'

running = True

def signal_handler(sig, frame):
    global running
    running = False
    print(f"\n{RESET}Pattern generation stopped! ✨")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def generate_pattern(time_step, width, height):
    """Generate a colorful ASCII pattern based on mathematical functions"""
    pattern = []
    
    for y in range(height):
        line = ""
        for x in range(width):
            # Create mathematical patterns using sine/cosine
            # Multiple overlapping waves create interesting effects
            value1 = math.sin(x * 0.1 + time_step) * math.cos(y * 0.1 + time_step * 0.5)
            value2 = math.sin((x + y) * 0.05 + time_step * 0.7)
            value3 = math.cos(math.sqrt(x*x + y*y) * 0.1 - time_step * 0.3)
            
            # Combine values
            combined = (value1 + value2 + value3) / 3
            
            # Select character based on value
            char_idx = int((combined + 1) * 0.5 * (len(CHARS) - 1))
            char_idx = max(0, min(char_idx, len(CHARS) - 1))
            char = CHARS[char_idx]
            
            # Select color based on position and time
            color_idx = int((combined + math.sin(time_step * 0.5) + 2) * 0.25 * len(COLORS))
            color_idx = color_idx % len(COLORS)
            
            line += COLORS[color_idx] + char
        pattern.append(line)
    
    return pattern

def main():
    """Main animation loop"""
    width, height = 80, 24
    time_step = 0
    frame_count = 0
    
    print(f"{CLEAR}🎨 Colorful ASCII Pattern Generator 🎨")
    print(f"Press Ctrl+C to stop\n")
    time.sleep(1)
    
    while running:
        print(CLEAR, end='')
        
        # Generate and display pattern
        pattern = generate_pattern(time_step, width, height)
        for line in pattern:
            print(line + RESET)
        
        # Display info
        print(f"{RESET}\n{'─' * width}")
        print(f"  Frame: {frame_count} | Time: {time_step:.2f} | Pattern: Sine Wave Flow")
        print(f"  Press Ctrl+C to stop  ")
        
        time_step += 0.15
        frame_count += 1
        time.sleep(0.05)  # ~20 FPS

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RESET}Pattern generation stopped! ✨")
