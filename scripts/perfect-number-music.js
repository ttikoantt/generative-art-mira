#!/usr/bin/env node

/**
 * 完全数音楽生成器 (Perfect Number Music Generator)
 *
 * 完全数 = 自分自身を除く約数の和が自分自身と等しい整数
 * 例: 6 = 1 + 2 + 3
 *
 * 完全数の神秘的な性質を音楽に変換します。
 */

// 完全数の定義と約数
const PERFECT_NUMBERS = {
  6: {
    divisors: [1, 2, 3],
    nickname: "最初の完全数"
  },
  28: {
    divisors: [1, 2, 4, 7, 14],
    nickname: "第2の完全数"
  },
  496: {
    divisors: [1, 2, 4, 8, 16, 31, 62, 124, 248],
    nickname: "第3の完全数"
  },
  8128: {
    divisors: [1, 2, 4, 8, 16, 32, 64, 127, 254, 508, 1016, 2032, 4064],
    nickname: "第4の完全数"
  }
};

// 音階（Cメジャーペンタトニック - 美しい響き）
const SCALE = [
  { note: "C4", freq: 261.63 },
  { note: "D4", freq: 293.66 },
  { note: "E4", freq: 329.63 },
  { note: "G4", freq: 392.00 },
  { note: "A4", freq: 440.00 },
  { note: "C5", freq: 523.25 },
  { note: "D5", freq: 587.33 },
  { note: "E5", freq: 659.25 }
];

/**
 * 約数を音階にマッピング
 */
function divisorToNote(divisor, scaleIndex) {
  const index = (divisor + scaleIndex) % SCALE.length;
  return SCALE[index];
}

/**
 * 完全数の約数から音楽を生成
 */
function generatePerfectNumberMusic(perfectNum) {
  const data = PERFECT_NUMBERS[perfectNum];
  if (!data) {
    throw new Error(`完全数 ${perfectNum} は見つかりません`);
  }

  console.log(`\n🎵 完全数 ${perfectNum} の音楽`);
  console.log(`   (${data.nickname})`);
  console.log(`   約数: ${data.divisors.join(" + ")} = ${perfectNum}\n`);

  const notes = [];

  data.divisors.forEach((divisor, i) => {
    const note = divisorToNote(divisor, perfectNum % SCALE.length);
    const duration = (divisor / perfectNum) * 2; // 約数が大きいほど長く
    notes.push({
      divisor,
      note: note.note,
      freq: note.freq,
      duration: duration.toFixed(2)
    });
  });

  return notes;
}

/**
 * 音楽譜をASCIIアートで表示
 */
function renderScore(notes) {
  console.log("🎼 楽譜\n");
  console.log("音符    | 周波数  | 長さ  | 元の約数");
  console.log("--------|---------|-------|---------");

  notes.forEach(n => {
    const bar = "█".repeat(Math.ceil(n.duration * 5));
    console.log(`${n.note.padEnd(6)} | ${n.freq.toFixed(2)} | ${n.duration}s  | ${n.divisor} → ${bar}`);
  });

  console.log("\n🎹 和音構成:");
  const allNotes = notes.map(n => n.note).join(" - ");
  console.log(`   ${allNotes}`);
}

/**
 * Web Audio API 用のJavaScriptコードを生成
 */
function generateAudioCode(notes, perfectNum) {
  let code = `<!DOCTYPE html>
<html>
<head>
  <title>完全数 ${perfectNum} の音楽</title>
  <style>
    body { font-family: monospace; padding: 20px; background: #1a1a2e; color: #eee; }
    button { padding: 10px 20px; font-size: 16px; margin: 10px 5px; cursor: pointer; border-radius: 5px; border: none; }
    .play { background: #4CAF50; color: white; }
    .play:hover { background: #45a049; }
    .info { margin: 20px 0; line-height: 1.6; }
    .note { display: inline-block; padding: 5px 10px; margin: 5px; background: #16213e; border-radius: 3px; }
  </style>
</head>
<body>
  <h1>🎵 完全数 ${perfectNum} の音楽</h1>
  <div class="info">
    <p>完全数 = 自分自身を除く約数の和が自分自身と等しい整数</p>
    <p>${perfectNum} = ${notes.map(n => n.divisor).join(" + ")}</p>
    <p>約数を音階にマッピングして演奏します</p>
  </div>
  <button class="play" onclick="playMusic()">▶ 演奏</button>
  <button onclick="stopMusic()">■ 停止</button>
  <div id="notes"></div>

  <script>
    const audioContext = new (window.AudioContext || window.webkitAudioContext)();
    let isPlaying = false;

    const notes = ${JSON.stringify(notes)};

    function playNote(freq, duration, startTime) {
      const osc = audioContext.createOscillator();
      const gain = audioContext.createGain();

      osc.type = 'sine';
      osc.frequency.value = freq;

      gain.gain.setValueAtTime(0.3, startTime);
      gain.gain.exponentialRampToValueAtTime(0.01, startTime + duration);

      osc.connect(gain);
      gain.connect(audioContext.destination);

      osc.start(startTime);
      osc.stop(startTime + duration);
    }

    function playMusic() {
      if (isPlaying) return;
      isPlaying = true;

      let startTime = audioContext.currentTime + 0.1;
      const totalDuration = notes.reduce((sum, n) => sum + parseFloat(n.duration), 0);

      notes.forEach(note => {
        playNote(note.freq, parseFloat(note.duration), startTime);
        startTime += parseFloat(note.duration) * 0.8; // 少し重ねる
      });

      setTimeout(() => { isPlaying = false; }, totalDuration * 1000 + 500);

      document.getElementById('notes').innerHTML =
        '<h3>🎹 演奏中...</h3><p>' +
        notes.map(n => \`<span class="note">\${n.note} (\${n.divisor})</span>\`).join('') +
        '</p>';
    }

    function stopMusic() {
      audioContext.close();
      location.reload();
    }
  </script>
</body>
</html>`;

  return code;
}

/**
 * メイン実行
 */
function main() {
  console.log("═══════════════════════════════════════════════════");
  console.log("🎵 完全数音楽生成器");
  console.log("   Perfect Number Music Generator");
  console.log("═══════════════════════════════════════════════════\n");

  Object.keys(PERFECT_NUMBERS).forEach(perfectNum => {
    const notes = generatePerfectNumberMusic(perfectNum);
    renderScore(notes);

    const htmlPath = `/tmp/perfect-number-${perfectNum}.html`;
    const fs = require('fs');
    fs.writeFileSync(htmlPath, generateAudioCode(notes, perfectNum));
    console.log(`\n💾 HTML出力: ${htmlPath}`);
    console.log("   ブラウザで開いて演奏を聞いてください！\n");
  });

  console.log("═══════════════════════════════════════════════════");
  console.log("📚 完全数について:");
  console.log("   - 6, 28, 496, 8128, 33550336, ...");
  console.log("   - 全て偶数の完全数は「2^(p-1) × (2^p - 1)」の形");
  console.log("   - (2^p - 1)がメルセンヌ素数の時に完全数になる");
  console.log("   - 奇数の完全数は見つかっていない（存在不明）");
  console.log("═══════════════════════════════════════════════════\n");
}

if (require.main === module) {
  main();
}

module.exports = { generatePerfectNumberMusic, renderScore };
