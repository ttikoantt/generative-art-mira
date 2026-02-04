#!/usr/bin/env python3
"""
ASCII Art Calendar Generator
月のカレンダーを視覚的に美しいASCIIアートとして表現する
"""

import calendar
from datetime import datetime
import sys

class ASCIICalendar:
    def __init__(self, year, month):
        self.year = year
        self.month = month
        self.cal = calendar.Calendar(firstweekday=0)  # 月曜日始まり

    def generate(self):
        """ASCIIアートカレンダーを生成"""
        # 月の情報を取得
        month_name = calendar.month_name[self.month]
        month_days = list(self.cal.itermonthdays(self.year, self.month))

        # ヘッダー（月名と年）
        header = f"  {month_name} {self.year}  "
        output = []
        output.append("┌" + "─" * 50 + "┐")
        output.append("│" + header.center(50) + "│")
        output.append("├" + "─" * 50 + "┤")

        # 曜日ヘッダー
        weekdays = "Mon Tue Wed Thu Fri Sat Sun"
        output.append("│  " + weekdays + "  │")
        output.append("├" + "─" * 50 + "┤")

        # カレンダー本体
        weeks = []
        current_week = []

        for day in month_days:
            if day == 0:
                current_week.append("   ")
            else:
                current_week.append(f"{day:2d}")

            if len(current_week) == 7:
                weeks.append(current_week)
                current_week = []

        # 最後の週を追加
        if current_week:
            weeks.append(current_week)

        # ASCIIアート風に描画
        for week in weeks:
            line = "│"
            for day in week:
                if day == "  ":
                    # 空白日は軽いパターン
                    line += " ░░ "
                else:
                    # 日付がある場合は数字
                    line += f" {day} "
            line += "│"
            output.append(line)

            # 週の下に装飾ラインを追加
            decor_line = "│"
            for day in week:
                if day.strip() == "":
                    # 空白日の場合
                    decor_line += "░░░░"
                else:
                    # 日付の下にドットパターン
                    pattern = self._get_day_pattern(day)
                    decor_line += f" {pattern} "
            decor_line += "│"
            output.append(decor_line)

        output.append("└" + "─" * 50 + "┘")

        # 追加のアート要素（月の雰囲気を表現）
        output.append("\n" + self._generate_month_art())

        return "\n".join(output)

    def _get_day_pattern(self, day):
        """日付に応じたパターンを返す"""
        if day == "   " or day == "  ":
            return "░░░"

        day_num = int(day.strip())
        patterns = {
            1: "░░░", 2: "▒▒▒", 3: "▓▓▓", 4: "███",
            5: "•••", 6: "···", 7: "○○○", 8: "●●●",
            9: "◇◇◇", 10: "◆◆◆", 11: "△△△", 12: "▲▲▲",
            13: "▽▽▽", 14: "▼▼▼", 15: "◇◇◇", 16: "◆◆◆",
            17: "◎◎◎", 18: "⊙⊙⊙", 19: "○○○", 20: "●●●",
            21: "◌◌◌", 22: "◍◍◍", 23: "◎◎◎", 24: "⊙⊙⊙",
            25: "☀☀☀", 26: "☁☁☁", 27: "☂☂☂", 28: "☃☃☃",
            29: "★☆☆", 30: "★★☆", 31: "★★★"
        }
        return patterns.get(day_num, "░░░")

    def _generate_month_art(self):
        """月に応じた装飾アートを生成"""
        month_arts = {
            1: """
        ❄️  ❄️  ❄️
      ❄️  ❄️  ❄️  ❄️
    ❄️  ❄️  ❄️  ❄️  ❄️
      ❄️  ❄️  ❄️  ❄️
        ❄️  ❄️  ❄️
    """,
            2: """
        💕    💕    💕
          💕  💕  💕
        💕  💕  💕  💕
      💕  💕  💕  💕  💕
        💕  💕  💕  💕
    """,
            3: """
        🌸  🌸  🌸  🌸
      🌸  🌸  🌸  🌸  🌸
    🌸  🌸  🌸  🌸  🌸  🌸
      🌸  🌸  🌸  🌸  🌸
        🌸  🌸  🌸  🌸
    """,
            4: """
        🌷  🌷  🌷
      🌷  🌷  🌷  🌷
    🌷  🌷  🌷  🌷  🌷
      🌷  🌷  🌷  🌷
        🌷  🌷  🌷
    """,
            5: """
        🌿  🌿  🌿  🌿
      🌿  🌿  🌿  🌿  🌿
    🌿  🌿  🌿  🌿  🌿  🌿
      🌿  🌿  🌿  🌿  🌿
        🌿  🌿  🌿  🌿
    """,
            6: """
        ☀️  ☀️  ☀️  ☀️
      ☀️  ☀️  ☀️  ☀️  ☀️
    ☀️  ☀️  ☀️  ☀️  ☀️  ☀️
      ☀️  ☀️  ☀️  ☀️  ☀️
        ☀️  ☀️  ☀️  ☀️
    """,
            7: """
        🌻  🌻  🌻  🌻
      🌻  🌻  🌻  🌻  🌻
    🌻  🌻  🌻  🌻  🌻  🌻
      🌻  🌻  🌻  🌻  🌻
        🌻  🌻  🌻  🌻
    """,
            8: """
        🎐  🎐  🎐  🎐
      🎐  🎐  🎐  🎐  🎐
    🎐  🎐  🎐  🎐  🎐  🎐
      🎐  🎐  🎐  🎐  🎐
        🎐  🎐  🎐  🎐
    """,
            9: """
        🍁  🍁  🍁  🍁
      🍁  🍁  🍁  🍁  🍁
    🍁  🍁  🍁  🍁  🍁  🍁
      🍁  🍁  🍁  🍁  🍁
        🍁  🍁  🍁  🍁
    """,
            10: """
        🍄  🍄  🍄  🍄
      🍄  🍄  🍄  🍄  🍄
    🍄  🍄  🍄  🍄  🍄  🍄
      🍄  🍄  🍄  🍄  🍄
        🍄  🍄  🍄  🍄
    """,
            11: """
        🍂  🍂  🍂  🍂
      🍂  🍂  🍂  🍂  🍂
    🍂  🍂  🍂  🍂  🍂  🍂
      🍂  🍂  🍂  🍂  🍂
        🍂  🍂  🍂  🍂
    """,
            12: """
        ⭐  ⭐  ⭐  ⭐
      ⭐  ⭐  ⭐  ⭐  ⭐
    ⭐  ⭐  ⭐  ⭐  ⭐  ⭐
      ⭐  ⭐  ⭐  ⭐  ⭐
        ⭐  ⭐  ⭐  ⭐
    """
        }
        return month_arts.get(self.month, "")

def main():
    # 現在の年月を取得
    now = datetime.now()
    year = now.year
    month = now.month

    # カレンダーを生成
    ascii_cal = ASCIICalendar(year, month)
    calendar_art = ascii_cal.generate()

    print(calendar_art)

    # ファイルに保存
    output_file = f"/Users/naokitomono/.openclaw/workspace/experiments/ascii-calendar-{year}-{month:02d}.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(calendar_art)

    print(f"\n✨ Saved to: {output_file}")

if __name__ == "__main__":
    main()
