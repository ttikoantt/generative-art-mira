#!/usr/bin/env node

/**
 * ジェネレーティブアート - 数式でASCIIパターン生成
 * 実行のたびに異なる美しいパターンが生まれる
 */

// パラメータをランダム生成
const params = {
  width: 80,
  height: 40,
  // パターンの複雑さを決める係数
  freqX: 0.1 + Math.random() * 0.3,
  freqY: 0.1 + Math.random() * 0.3,
  // 位相シフト
  phaseX: Math.random() * Math.PI * 2,
  phaseY: Math.random() * Math.PI * 2,
  // 振幅
  amplitude: 0.5 + Math.random() * 1.5,
  // 文字セット
  chars: [' ', '·', ':', '+', '*', '#', '@'],
  // カラフルモード
  colors: [
    '\x1b[34m', // 青
    '\x1b[36m', // シアン
    '\x1b[32m', // 緑
    '\x1b[33m', // 黄
    '\x1b[35m', // マゼンタ
    '\x1b[31m', // 赤
    '\x1b[37m', // 白
  ]
};

// 文字を選択
function getChar(value, min, max) {
  const normalized = (value - min) / (max - min);
  const index = Math.floor(normalized * (params.chars.length - 1));
  return params.chars[Math.min(index, params.chars.length - 1)];
}

// 色を選択
function getColor(value, min, max) {
  const normalized = (value - min) / (max - min);
  const index = Math.floor(normalized * (params.colors.length - 1));
  return params.colors[Math.min(index, params.colors.length - 1)];
}

// 数式で値を計算（三角関数の組み合わせ）
function calculateValue(x, y) {
  const nx = (x / params.width - 0.5) * params.freqX;
  const ny = (y / params.height - 0.5) * params.freqY;
  
  // 複雑な波形を組み合わせる
  const value =
    Math.sin(nx * 10 + params.phaseX) * Math.cos(ny * 10 + params.phaseY) +
    Math.sin(nx * 5 - ny * 5 + params.phaseX) * 0.5 +
    Math.cos(Math.sqrt(nx * nx + ny * ny) * 15 + params.phaseY) * 0.3;
  
  return value * params.amplitude;
}

// パターン生成
let output = [];
let minVal = Infinity, maxVal = -Infinity;

// まずは値を計算して範囲を決める
const values = [];
for (let y = 0; y < params.height; y++) {
  values[y] = [];
  for (let x = 0; x < params.width; x++) {
    const val = calculateValue(x, y);
    values[y][x] = val;
    if (val < minVal) minVal = val;
    if (val > maxVal) maxVal = val;
  }
}

// ASCIIアートを生成
const reset = '\x1b[0m';
for (let y = 0; y < params.height; y++) {
  let line = '';
  for (let x = 0; x < params.width; x++) {
    const val = values[y][x];
    const char = getChar(val, minVal, maxVal);
    const color = getColor(val, minVal, maxVal);
    line += color + char + reset;
  }
  output.push(line);
}

// タイトルとパラメータ表示
console.log('\n' + '═'.repeat(80));
console.log('\x1b[1m\x1b[35m' + '  ジェネレーティブ・アート v1.0'.padEnd(80) + '\x1b[0m');
console.log('═'.repeat(80));
console.log(`  パラメータ: Freq(${params.freqX.toFixed(3)}, ${params.freqY.toFixed(3)}) ` +
            `Phase(${params.phaseX.toFixed(2)}, ${params.phaseY.toFixed(2)}) ` +
            `Amp(${params.amplitude.toFixed(2)})`);
console.log('═'.repeat(80) + '\n');

// アートを出力
console.log(output.join('\n'));

// フッター
console.log('\n' + '═'.repeat(80));
console.log(`  Generated: ${new Date().toLocaleString('ja-JP')}`);
console.log('═'.repeat(80) + '\n');
