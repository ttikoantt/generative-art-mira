#!/usr/bin/env python3
"""
Turtle Geometric Spiral - Generative Art
有機的な幾何学模様を描くジェネレーティブアート

実行方法:
    python3 turtle_geometry.py
"""

import turtle
import math
import random
import colorsys

# キャンバスの設定
screen = turtle.Screen()
screen.bgcolor('#0a0a0f')
screen.title('Turtle Geometric Spiral - Generative Art')
screen.setup(width=800, height=800)
screen.tracer(0)

# タートルの設定
artist = turtle.Turtle()
artist.speed(0)
artist.hideturtle()

# 描画パラメータ
NUM_SPIRALS = 6
POINTS_PER_SPIRAL = 200
BASE_RADIUS = 50
RADIUS_GROWTH = 0.5
ANGLE_STEP = 0.1

def rgb_from_hsv(h, s, v):
    """HSVからRGBへ（0-255の範囲）"""
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return int(r * 255), int(g * 255), int(b * 255)

def draw_geometric_spiral(start_hue):
    """幾何学的な螺旋を描く"""
    artist.penup()

    # グラデーション色の螺旋
    for i in range(POINTS_PER_SPIRAL):
        # 螺旋の計算（フェルマーの螺旋に基づく）
        angle = i * ANGLE_STEP
        radius = BASE_RADIUS + i * RADIUS_GROWTH

        # 変形を加える
        x_mod = math.sin(angle * 3) * 20
        y_mod = math.cos(angle * 2) * 20

        x = radius * math.cos(angle) + x_mod
        y = radius * math.sin(angle) + y_mod

        # 色の計算
        hue = (start_hue + i / POINTS_PER_SPIRAL * 0.3) % 1.0
        saturation = 0.7 + (i / POINTS_PER_SPIRAL) * 0.3
        value = 0.8

        artist.goto(x, y)

        # サイズの変化
        size = 2 + (i / POINTS_PER_SPIRAL) * 4

        # 色を設定
        r, g, b = rgb_from_hsv(hue, saturation, value)
        color = f'#{r:02x}{g:02x}{b:02x}'

        artist.dot(size, color)

    # 内側の装飾的な円
    artist.penup()
    for i in range(36):
        angle = i * 10
        radius = 30
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))

        hue = (start_hue + i / 36 * 0.2) % 1.0
        r, g, b = rgb_from_hsv(hue, 0.8, 0.9)
        color = f'#{r:02x}{g:02x}{b:02x}'

        artist.goto(x, y)
        artist.dot(6, color)

def draw_pattern():
    """全体のパターンを描画"""
    # 複数の螺旋を回転配置
    for s in range(NUM_SPIRALS):
        # 新しい螺旋を開始する色
        start_hue = s / NUM_SPIRALS

        # 回転して配置
        artist.penup()
        artist.home()

        # すべてをクリアして最初の位置に戻る
        artist.clear()

        # 螺旋を描画
        draw_geometric_spiral(start_hue)

        # 画面を更新
        screen.update()

        # 少し待機してから次の螺旋
        # 実際にはすべてを同時に描画するので、これはアニメーション効果
        # 本当のアニメーションにするには、描画を分割する必要がある

    # 中心に大きな星
    artist.penup()
    artist.home()
    for i in range(12):
        angle = i * 30
        distance = 15
        x = distance * math.cos(math.radians(angle))
        y = distance * math.sin(math.radians(angle))

        hue = (i / 12 * 0.5) % 1.0
        r, g, b = rgb_from_hsv(hue, 0.9, 1.0)
        color = f'#{r:02x}{g:02x}{b:02x}'

        artist.goto(x, y)
        artist.dot(8, color)

    screen.update()

def main():
    """メイン描画関数"""
    # 最初に画面をクリア
    artist.clear()

    # パターンを描画
    draw_pattern()

    # 完了メッセージ
    print("✨ 幾何学模様が完成しました！")
    print("   クローズするにはウィンドウを閉じてください")

    # イベントループ
    screen.mainloop()

if __name__ == "__main__":
    main()
