#!/usr/bin/env python3
"""
数字の花園 - Fibonacci Number Garden
フィボナッチ数列を美しく視覚化する
"""

import sys

# ANSI color codes
COLORS = [
    '\033[91m',  # Red
    '\033[92m',  # Green
    '\033[93m',  # Yellow
    '\033[94m',  # Blue
    '\033[95m',  # Magenta
    '\033[96m',  # Cyan
    '\033[38;5;214m',  # Orange
    '\033[38;5;13m',   # Purple
    '\033[38;5;11m',   # Bright Yellow
    '\033[38;5;9m',    # Bright Red
]
RESET = '\033[0m'

def fibonacci_sequence(n):
    """Generate fibonacci sequence"""
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq

def format_number(num, color_idx):
    """Format a number with color and artistic representation"""
    color = COLORS[color_idx % len(COLORS)]
    digits = str(num)

    # Create artistic representation based on number
    if num < 10:
        return f"{color}✿ {digits}{RESET}"
    elif num < 100:
        return f"{color}❀ {digits} ✿{RESET}"
    elif num < 1000:
        return f"{color}✾ {digits} ✾{RESET}"
    else:
        # For larger numbers, show as flower with petals
        petals = '✿' * min(len(digits), 8)
        return f"{color}{petals} {digits[-3:]} {petals}{RESET}"

def create_garden(n=15):
    """Create the number garden"""
    fib = fibonacci_sequence(n)

    print("\n" + "🌸 " * 20)
    print(f"\n{COLORS[0]}    ✿ 数字の花園 - Fibonacci Garden ✿{RESET}\n")

    # Display the sequence artistically
    for i, num in enumerate(fib[1:]):  # Skip the first 0
        color_idx = i % len(COLORS)
        indent = "  " * (i // 3)
        line = format_number(num, color_idx)

        print(f"{indent}{line}")

        # Add decorative elements periodically
        if i % 4 == 3 and i > 0:
            print(f"{indent}  {COLORS[(i+1) % len(COLORS)]}~|~{RESET}")

    # Display golden ratio approximation
    print("\n" + "─" * 50)
    if len(fib) >= 4:
        ratio = fib[-1] / fib[-2]
        print(f"\n{COLORS[3]}黄金比の近似値: {ratio:.8f}{RESET}")
        print(f"{COLORS[5]}φ = 1.618033988749...{RESET}")

    print(f"\n{COLORS[1]}🌱 自然界の美しさは数字に隠れている... 🌱{RESET}\n")
    print("🌸 " * 20 + "\n")

if __name__ == "__main__":
    create_garden(15)
