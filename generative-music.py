#!/usr/bin/env python3
"""
Generative Music Generator
~~~~~~~~~~~~~~~~~~~~~~~~~~
Creates algorithmic music using pentatonic scales and probability patterns.

Algorithm:
1. Uses C Major Pentatonic scale (C, D, E, G, A)
2. Each note has probability based on position (root more stable)
3. Creates phrases with rhythm patterns
4. Generates WAV output
"""

import random
import wave
import struct
import math
from pathlib import Path

# Musical parameters
SAMPLE_RATE = 44100
BIT_DEPTH = 16
CHANNELS = 1
DURATION = 30  # seconds
TEMPO = 120  # BPM

# C Major Pentatonic scale (spanning multiple octaves)
# C4=261.63Hz, D4=293.66Hz, E4=329.63Hz, G4=392.00Hz, A4=440.00Hz
PENTATONIC_SCALE = [
    130.81,  # C3
    146.83,  # D3
    164.81,  # E3
    196.00,  # G3
    220.00,  # A3
    261.63,  # C4
    293.66,  # D4
    329.63,  # E4
    392.00,  # G4
    440.00,  # A4
    523.25,  # C5
    587.33,  # D5
    659.25,  # E5
]

# Note probabilities (root and 5th more stable)
NOTE_PROBABILITIES = [
    0.08,  # C3 (root)
    0.12,  # D3
    0.10,  # E3
    0.15,  # G3 (5th)
    0.12,  # A3
    0.08,  # C4 (root)
    0.10,  # D4
    0.08,  # E4
    0.10,  # G4 (5th)
    0.05,  # A4
    0.01,  # C5
    0.01,  # D5
    0.00,  # E5 (rare)
]

def generate_sine_wave(frequency, duration, volume=0.3):
    """Generate a sine wave with envelope for natural decay."""
    num_samples = int(SAMPLE_RATE * duration)
    data = []

    # ADSR-like envelope
    attack = int(num_samples * 0.1)
    decay = int(num_samples * 0.2)
    sustain = int(num_samples * 0.5)
    release = int(num_samples * 0.2)

    for i in range(num_samples):
        t = i / SAMPLE_RATE
        sample = math.sin(2 * math.pi * frequency * t)

        # Apply envelope
        if i < attack:
            envelope = i / attack  # Attack
        elif i < attack + decay:
            envelope = 1.0 - (i - attack) / decay * 0.3  # Decay to 0.7
        elif i < attack + decay + sustain:
            envelope = 0.7  # Sustain
        else:
            envelope = 0.7 * (1 - (i - attack - decay - sustain) / release)  # Release

        sample *= envelope * volume
        data.append(sample)

    return data

def weighted_choice(items, weights):
    """Choose an item based on weights."""
    total = sum(weights)
    r = random.uniform(0, total)
    upto = 0
    for item, weight in zip(items, weights):
        if upto + weight >= r:
            return item
        upto += weight
    return items[-1]

def generate_music():
    """Generate the complete music piece."""
    total_samples = int(SAMPLE_RATE * DURATION)
    music_data = [0.0] * total_samples

    # Beat subdivision (16th notes)
    beat_duration = 60 / TEMPO  # quarter note
    subdivision = beat_duration / 4  # 16th note

    current_sample = 0
    phrase_length = 8  # beats per phrase
    beat_count = 0

    print(f"🎵 Generating {DURATION}s of generative music...")
    print(f"   Tempo: {TEMPO} BPM")
    print(f"   Scale: C Major Pentatonic")

    # Generate patterns
    pattern_history = []

    while current_sample < total_samples:
        # Create rhythmic patterns
        if beat_count % phrase_length == 0:
            # New phrase - decide density
            density = random.choice([0.3, 0.5, 0.7])
            note_count = 0

        # Decide whether to play a note
        if random.random() < density and note_count < 4:
            # Choose note from pentatonic scale
            note_idx = weighted_choice(
                list(range(len(PENTATONIC_SCALE))),
                NOTE_PROBABILITIES
            )
            frequency = PENTATONIC_SCALE[note_idx]

            # Random duration (16th, 8th, or quarter note)
            duration_multiplier = random.choice([1, 2, 4])
            note_duration = subdivision * duration_multiplier

            # Generate the note
            note_data = generate_sine_wave(frequency, note_duration, volume=0.25)

            # Mix into music data
            note_samples = len(note_data)
            end_sample = min(current_sample + note_samples, total_samples)

            for i in range(end_sample - current_sample):
                if current_sample + i < total_samples:
                    music_data[current_sample + i] += note_data[i]

            current_sample = end_sample
            note_count += 1
        else:
            # Rest
            current_sample += int(SAMPLE_RATE * subdivision)

        beat_count += 1

    # Normalize to prevent clipping
    max_value = max(abs(x) for x in music_data)
    if max_value > 0:
        music_data = [x / max_value * 0.8 for x in music_data]

    return music_data

def save_wav(data, filename):
    """Save audio data to WAV file."""
    wav_file = wave.open(str(filename), 'w')
    wav_file.setparams((CHANNELS, 2, SAMPLE_RATE, len(data), 'NONE', 'not compressed'))

    for sample in data:
        # Convert to 16-bit integer
        value = int(sample * 32767)
        wav_file.writeframes(struct.pack('<h', value))

    wav_file.close()

def main():
    """Main generation process."""
    print("\n🎵 Generative Music Generator")
    print("=" * 40)

    # Generate music
    music_data = generate_music()

    # Save to file
    output_path = Path("generated-music.wav")
    save_wav(music_data, output_path)

    print(f"\n✅ Music saved to: {output_path}")
    print(f"   Duration: {DURATION}s")
    print(f"   Size: {output_path.stat().st_size / 1024:.1f} KB")
    print("\n🎶 Play it: afplay generated-music.wav")

if __name__ == "__main__":
    main()
