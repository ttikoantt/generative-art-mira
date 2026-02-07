#!/usr/bin/env node

/**
 * 音律幾何学 Harmonic Geometry
 * 音程関係をASCIIアートパターンとして視覚化
 */

const ANSI = {
  reset: '\x1b[0m',
  red: '\x1b[31m',
  green: '\x1b[32m',
  yellow: '\x1b[33m',
  blue: '\x1b[34m',
  magenta: '\x1b[35m',
  cyan: '\x1b[36m',
  white: '\x1b[37m',
  brightRed: '\x1b[91m',
  brightGreen: '\x1b[92m',
  brightYellow: '\x1b[93m',
  brightBlue: '\x1b[94m',
  brightMagenta: '\x1b[95m',
  brightCyan: '\x1b[96m',
  brightWhite: '\x1b[97m',
};

const colors = [
  ANSI.brightRed,
  ANSI.brightYellow,
  ANSI.brightGreen,
  ANSI.brightCyan,
  ANSI.brightBlue,
  ANSI.brightMagenta,
];

// 純正律の音程比（ユニソンからオクターブまで）
const intervals = [
  { name: 'P1', ratio: 1/1, label: '根音' },        // 完全1度
  { name: 'm2', ratio: 16/15, label: '短2度' },     // 短2度
  { name: 'M2', ratio: 9/8, label: '長2度' },       // 長2度
  { name: 'm3', ratio: 6/5, label: '短3度' },       // 短3度
  { name: 'M3', ratio: 5/4, label: '長3度' },       // 長3度
  { name: 'P4', ratio: 4/3, label: '完全4度' },     // 完全4度
  { name: 'd5', ratio: 45/32, label: '増4度' },     // 増4度/減5度
  { name: 'P5', ratio: 3/2, label: '完全5度' },     // 完全5度
  { name: 'm6', ratio: 8/5, label: '短6度' },       // 短6度
  { name: 'M6', ratio: 5/3, label: '長6度' },       // 長6度
  { name: 'm7', ratio: 9/5, label: '短7度' },       // 短7度
  { name: 'M7', ratio: 15/8, label: '長7度' },      // 長7度
  { name: 'P8', ratio: 2/1, label: 'オクターブ' },  // 完全8度
];

// 周波数比を「距離」に変換（対数スケール）
function ratioToDistance(ratio) {
  return Math.log2(ratio);
}

// 距離からパターン文字を生成
function distanceToPattern(distance, index) {
  const normalized = (distance / Math.log2(2)) * 12; // 0-12の範囲
  const charIndex = Math.floor(normalized * 2) % 8;
  const chars = ['·', '░', '▒', '▓', '█', '▓', '▒', '░'];
  return chars[charIndex];
}

// 音程パターンを生成
function generateHarmonicPattern() {
  const width = 60;
  const height = 13;
  const output = [];

  // ヘッダー
  output.push(ANSI.brightWhite + '\n🎵 音律幾何学 Harmonic Geometry 🎵\n');
  output.push('純正律の音程関係を視覚化\n' + ANSI.reset);

  const distances = intervals.map(i => ratioToDistance(i.ratio));

  for (let row = 0; row < height; row++) {
    let line = '';
    for (let col = 0; col < width; col++) {
      // 2音間の「インターバルパターン」を計算
      const idx1 = row;
      const idx2 = (col % 12);
      
      const dist1 = distances[idx1];
      const dist2 = distances[idx2];
      
      // 2音の距離関係に基づいてパターンを生成
      const intervalDist = Math.abs(dist1 - dist2);
      const harmonicIndex = (idx1 + idx2) % colors.length;
      
      // 中心からの距離でパターンを変化
      const centerDist = Math.abs(col - width / 2) / (width / 2);
      const char = distanceToPattern(intervalDist + centerDist * 0.5, idx1);
      
      line += colors[harmonicIndex] + char;
    }
    output.push(line + ANSI.reset);
    
    // 右側に音程情報を表示
    if (row < intervals.length) {
      const interval = intervals[row];
      const cents = Math.round(1200 * Math.log2(interval.ratio));
      output.push(
        ANSI.brightWhite + '  ' +
        interval.name.padEnd(3) + ' ' +
        interval.label.padEnd(8) + ' ' +
        `比: ${interval.ratio.toFixed(3)}  ${cents}¢`
      );
    } else {
      output.push('');
    }
  }

  return output.join('\n');
}

// メロディックパターンを生成（スケールを横に展開）
function generateMelodicPattern() {
  const width = 50;
  const scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B'];
  const output = [];

  output.push(ANSI.brightWhite + '\n🎶 メロディックパターン Melodic Pattern 🎶\n' + ANSI.reset);

  for (let octave = 0; octave < 4; octave++) {
    let line = '';
    for (let i = 0; i < width; i++) {
      const noteIndex = i % scale.length;
      const note = scale[noteIndex];
      
      // 音の「高さ」と「位置」から幾何学パターンを生成
      const x = i / width * Math.PI * 2;
      const y = octave / 4 * Math.PI;
      const pattern = Math.sin(x * 3 + y * 2) * Math.cos(x);
      
      const charIndex = Math.floor((pattern + 1) * 3.5) % 7;
      const chars = ['○', '◯', '◎', '◉', '●', '◕', '◔'];
      const colorIndex = (noteIndex + octave) % colors.length;
      
      line += colors[colorIndex] + chars[charIndex];
    }
    output.push(line + ANSI.reset);
  }

  return output.join('\n');
}

// 和音パターン（トライアドの視覚化）
function generateChordPattern() {
  const chords = [
    { name: 'C', notes: [0, 4, 7], label: 'Cメジャー' },
    { name: 'Am', notes: [9, 0, 4], label: 'Aマイナー' },
    { name: 'F', notes: [5, 9, 0], label: 'Fメジャー' },
    { name: 'G', notes: [7, 11, 2], label: 'Gメジャー' },
  ];

  const output = [];
  output.push(ANSI.brightWhite + '\n🎹 和音幾何学 Chord Geometry 🎹\n' + ANSI.reset);

  chords.forEach((chord, chordIdx) => {
    let line = ANSI.brightWhite + chord.label + ': ' + ANSI.reset;
    
    for (let pos = 0; pos < 20; pos++) {
      // 和音の3音の「バランス」を視覚化
      let patternSum = 0;
      chord.notes.forEach((note, i) => {
        const phase = (note / 12) * Math.PI * 2;
        patternSum += Math.sin(phase + pos * 0.3 + i * 2);
      });
      
      const normalized = patternSum / 3 + 0.5;
      const charIndex = Math.floor(normalized * 7) % 7;
      const chars = ['┈', '┉', '┊', '┋', '╻', '╽', '┃'];
      const colorIndex = (chordIdx + pos) % colors.length;
      
      line += colors[colorIndex] + chars[charIndex];
    }
    output.push(line);
  });

  return output.join('\n');
}

// メイン実行
function main() {
  console.log(generateHarmonicPattern());
  console.log(generateMelodicPattern());
  console.log(generateChordPattern());
  console.log(ANSI.brightWhite + '\n✨ 音の調和を幾何学として見る ✨\n' + ANSI.reset);
}

main();
