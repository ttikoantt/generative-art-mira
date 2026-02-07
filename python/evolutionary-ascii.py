#!/usr/bin/env python3
"""
進化的ASCIIアートジェネレーター
シミュレーテッド・アニーリングで美しいパターンを進化させる
"""

import random
import math
import copy
from typing import List, Tuple

# ASCII文字セット（視覚的に面白い文字）
ASCII_CHARS = " .:-=+*#%@XO"

class EvolutionaryASCII:
    def __init__(self, width=40, height=20):
        self.width = width
        self.height = height
        self.grid = []
        self.best_score = float('-inf')
        self.best_grid = []
        self.temperature = 1.0
        self.cooling_rate = 0.995

    def random_char(self):
        """ランダムなASCII文字を選択"""
        return random.choice(ASCII_CHARS)

    def initialize(self):
        """ランダムなグリッドで初期化"""
        self.grid = [[self.random_char() for _ in range(self.width)] for _ in range(self.height)]
        self.best_grid = copy.deepcopy(self.grid)

    def score_symmetry(self, grid: List[List[str]]) -> float:
        """対称性をスコア化（縦・横・斜め）"""
        score = 0.0

        # 縦対称
        for y in range(self.height):
            for x in range(self.width // 2):
                if grid[y][x] == grid[y][self.width - 1 - x]:
                    score += 1

        # 横対称
        for y in range(self.height // 2):
            for x in range(self.width):
                if grid[y][x] == grid[self.height - 1 - y][x]:
                    score += 1

        # 斜め対称
        for i in range(min(self.width, self.height) // 2):
            if grid[i][i] == grid[self.height - 1 - i][self.width - 1 - i]:
                score += 2

        return score / (self.width * self.height)

    def score_repetition(self, grid: List[List[str]]) -> float:
        """パターンの反復をスコア化"""
        score = 0.0

        # 横方向の反復
        for y in range(self.height):
            for x in range(self.width - 4):
                pattern = grid[y][x:x+4]
                # グリッド内で同じパターンを探す
                for x2 in range(x + 4, self.width - 4):
                    if grid[y][x2:x2+4] == pattern:
                        score += 1

        # 縦方向の反復
        for x in range(self.width):
            for y in range(self.height - 4):
                pattern = [grid[y+i][x] for i in range(4)]
                for y2 in range(y + 4, self.height - 4):
                    pattern2 = [grid[y2+i][x] for i in range(4)]
                    if pattern == pattern2:
                        score += 1

        return score / 10.0

    def score_contrast(self, grid: List[List[str]]) -> float:
        """コントラストと文字の分布をスコア化"""
        char_counts = {}
        for row in grid:
            for char in row:
                char_counts[char] = char_counts.get(char, 0) + 1

        # シャノンエントロピー（多様性）
        total = self.width * self.height
        entropy = 0.0
        for count in char_counts.values():
            p = count / total
            entropy -= p * math.log2(p) if p > 0 else 0

        return entropy

    def evaluate(self, grid: List[List[str]]) -> float:
        """総合スコア計算"""
        symmetry = self.score_symmetry(grid)
        repetition = self.score_repetition(grid)
        contrast = self.score_contrast(grid)

        # 重み付き合計
        return (symmetry * 3.0 + repetition * 1.5 + contrast * 0.5)

    def mutate(self, grid: List[List[str]]) -> List[List[str]]:
        """グリッドを変異させる（ランダムな位置の文字を変更）"""
        new_grid = copy.deepcopy(grid)
        num_mutations = random.randint(1, 5)

        for _ in range(num_mutations):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            new_grid[y][x] = self.random_char()

        return new_grid

    def should_accept(self, old_score: float, new_score: float) -> bool:
        """シミュレーテッド・アニーリングの採択判定"""
        if new_score > old_score:
            return True

        # 悪化も確率的に許容
        delta = old_score - new_score
        probability = math.exp(-delta / max(self.temperature, 0.01))
        return random.random() < probability

    def evolve(self, generations: int = 1000) -> List[List[str]]:
        """進化を実行"""
        current_grid = copy.deepcopy(self.grid)
        current_score = self.evaluate(current_grid)

        for gen in range(generations):
            # 変異
            new_grid = self.mutate(current_grid)
            new_score = self.evaluate(new_grid)

            # 採択判定
            if self.should_accept(current_score, new_score):
                current_grid = new_grid
                current_score = new_score

                # ベスト記録更新
                if current_score > self.best_score:
                    self.best_score = current_score
                    self.best_grid = copy.deepcopy(current_grid)

            # 温度を下げる（アニーリング）
            self.temperature *= self.cooling_rate

            # 進捗表示（100世代ごと）
            if gen % 100 == 0:
                print(f"Generation {gen}: Score={current_score:.3f}, Temp={self.temperature:.4f}, Best={self.best_score:.3f}")

        return self.best_grid

    def render(self, grid: List[List[str]]) -> str:
        """グリッドを文字列としてレンダリング"""
        return '\n'.join(''.join(row) for row in grid)

    def generate(self, generations: int = 1000) -> str:
        """ASCIIアートを生成"""
        self.initialize()
        best_grid = self.evolve(generations)
        return self.render(best_grid)


def main():
    print("🧬 進化的ASCIIアートジェネレーター")
    print("=" * 50)

    # パラメータ設定
    WIDTH = 40
    HEIGHT = 20
    GENERATIONS = 1500

    # ジェネレーター作成
    gen = EvolutionaryASCII(WIDTH, HEIGHT)

    # 進化実行
    print(f"\nサイズ: {WIDTH}x{HEIGHT}, 世代数: {GENERATIONS}")
    print("進化中...\n")

    art = gen.generate(GENERATIONS)

    # 結果表示
    print("\n" + "=" * 50)
    print("🎨 生成されたASCIIアート:")
    print("=" * 50)
    print(art)
    print("=" * 50)
    print(f"\n最終スコア: {gen.best_score:.3f}")
    print(f"最終温度: {gen.temperature:.6f}")


if __name__ == "__main__":
    main()
