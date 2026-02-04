#!/usr/bin/env python3
"""
フィボナッチ音楽ジェネレーター
自然の数列を音楽に変換するアルゴリズム創作
"""

def fibonacci_sequence(n):
    """フィボナッチ数列を生成"""
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[1:n]  # 最初の0を除外

def number_to_note(num, scale='C'):
    """数字を音符に変換"""
    # Cメジャースケール: C, D, E, F, G, A, B
    scales = {
        'C': [0, 2, 4, 5, 7, 9, 11],
        'A': [9, 11, 0, 2, 4, 5, 7]  # Aマイナー
    }

    scale_degrees = scales[scale]
    octave = (num // 7) * 12
    degree = num % 7

    note = 60 + octave + scale_degrees[degree]  # 60 = 中央C
    return min(note, 127)  # MIDIノート番号は0-127

def create_fibonacci_melody(length=16, scale='C'):
    """フィボナッチ数列からメロディを生成"""
    fib = fibonacci_sequence(length * 2)  # 余分に生成

    melody = []
    for i, num in enumerate(fib[:length]):
        note = number_to_note(num % 28, scale)  # オクターブ範囲を制限
        duration = 0.5 + (num % 3) * 0.25  # リズムのバリエーション
        melody.append({
            'note': note,
            'duration': duration,
            'velocity': 80 + (num % 40)  # ヴェロシティの変化
        })

    return melody

def midi_to_frequency(midi_note):
    """MIDIノート番号を周波数に変換"""
    return 440 * (2 ** ((midi_note - 69) / 12))

def save_midi_simple(melody, filename='fibonacci_music.mid'):
    """簡易MIDIファイル出力（テキスト形式で保存）"""
    with open(filename.replace('.mid', '.txt'), 'w', encoding='utf-8') as f:
        f.write("# フィボナッチ音楽\n")
        f.write("# Note format: MIDI_Note (Frequency Hz) | Duration sec | Velocity\n\n")

        for i, note in enumerate(melody):
            freq = midi_to_frequency(note['note'])
            f.write(f"{i+1:3d}. Note {note['note']:3d} ({freq:7.2f} Hz) | "
                   f"Duration: {note['duration']:.2f}s | Velocity: {note['velocity']}\n")

    return filename.replace('.mid', '.txt')

def visualize_melody(melody):
    """メロディのASCIIビジュアライゼーション"""
    print("\n🎵 フィボナッチ・メロディ ビジュアライゼーション\n")
    print("=" * 70)

    for i, note in enumerate(melody):
        # 音高に応じた高さを表現
        height = (note['note'] - 48) // 2
        bar = "█" * max(1, int(note['duration'] * 4))
        spaces = " " * (20 - min(20, height))

        print(f"{i+1:2d} |{spaces}{'█' * max(1, height)} {bar} "
              f"(Note {note['note']}, {note['duration']:.2f}s)")

    print("=" * 70)

def main():
    print("🎼 フィボナッチ音楽ジェネレーター")
    print("=" * 50)

    # メロディ生成
    melody = create_fibonacci_melody(length=16, scale='C')

    print(f"\n✨ {len(melody)}音符のメロディを生成しました！\n")

    # ビジュアライゼーション
    visualize_melody(melody)

    # 保存
    output_file = save_midi_simple(melody)
    print(f"\n💾 メロディデータを保存: {output_file}")

    # 統計情報
    notes = [n['note'] for n in melody]
    durations = [n['duration'] for n in melody]

    print(f"\n📊 統計情報:")
    print(f"   音高範囲: {min(notes)} - {max(notes)} (MIDIノート番号)")
    print(f"   平均リズム: {sum(durations)/len(durations):.2f}秒")
    print(f"   総演奏時間: {sum(durations):.2f}秒")

    # フィボナッチ数列の表示
    fib = fibonacci_sequence(16)
    print(f"\n🔢 使用したフィボナッチ数列:")
    print(f"   {fib}")

    return melody

if __name__ == "__main__":
    main()
