#!/usr/bin/env node

/**
 * Generative ASCII Art Landscape
 * ランダムに美しい風景を生成する
 */

const WIDTH = 80;
const HEIGHT = 25;

// ランダム選択
function pick(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

// 範囲内のランダム整数
function rand(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

// 山を生成
function generateMountain(baseRow, height, char) {
  const peakX = rand(10, WIDTH - 10);
  const mountain = [];
  
  for (let y = 0; y < height; y++) {
    const row = Math.floor(baseRow - y);
    if (row < 0 || row >= HEIGHT) continue;
    
    const width = y * 2;
    for (let x = peakX - width; x <= peakX + width; x++) {
      if (x >= 0 && x < WIDTH) {
        mountain.push({ x, y: row, char });
      }
    }
  }
  
  return mountain;
}

// 川を生成
function generateRiver(row) {
  const river = [];
  let x = 5;
  
  while (x < WIDTH - 5) {
    const segmentLength = rand(3, 8);
    for (let i = 0; i < segmentLength && x < WIDTH - 5; i++) {
      river.push({ x, y: row, char: '~' });
      river.push({ x, y: row + 1, char: '~' });
      x++;
    }
    x += rand(0, 2);
  }
  
  return river;
}

// 星を生成
function generateStars(count) {
  const stars = [];
  for (let i = 0; i < count; i++) {
    stars.push({
      x: rand(0, WIDTH - 1),
      y: rand(0, 8),
      char: pick(['.', '*', '+', '°'])
    });
  }
  return stars;
}

// 月を生成
function generateMoon() {
  const moonX = rand(10, WIDTH - 10);
  const moonY = rand(2, 6);
  
  // 新月、半月、満月
  const phase = rand(0, 2);
  const moonChars = [
    ['    ),,', '   ((),', '  (   )', '   (())', '    \'`'],
    ['     )', '    ((', '   (  )', '    ((', '     )'],
    ['    ((', '   (  )', '  (    )', '   (  )', '    (())']
  ];
  
  const moon = [];
  for (let y = 0; y < moonChars[phase].length; y++) {
    for (let x = 0; x < moonChars[phase][y].length; x++) {
      const char = moonChars[phase][y][x];
      if (char !== ' ') {
        moon.push({ x: moonX + x, y: moonY + y, char });
      }
    }
  }
  
  return moon;
}

// 木を生成
function generateTree(x, y) {
  const tree = [];
  
  // 幹
  for (let i = 0; i < 3; i++) {
    tree.push({ x, y: y + i, char: '|' });
  }
  
  // 葉
  const leafChar = pick(['♠', '♣', '▲', '◆']);
  for (let dy = -3; dy <= 0; dy++) {
    const width = dy === 0 ? 1 : Math.abs(dy) * 2 + 1;
    for (let dx = -width; dx <= width; dx++) {
      if (Math.random() > 0.3) {
        tree.push({ x: x + dx, y: y + dy, char: leafChar });
      }
    }
  }
  
  return tree;
}

// 家を生成
function generateHouse(x, y) {
  const house = [];
  
  // 屋根
  for (let i = 0; i < 5; i++) {
    house.push({ x: x - 2 + i, y, char: i === 2 ? '∧' : '_' });
  }
  
  // 壁
  for (let dy = 1; dy <= 3; dy++) {
    for (let dx = -2; dx <= 2; dx++) {
      const isDoor = dy >= 2 && dx === 0;
      const isWindow = (dy === 1 && (dx === -1 || dx === 1));
      house.push({ x: x + dx, y: y + dy, char: isDoor ? '|' : isWindow ? '○' : '#' });
    }
  }
  
  return house;
}

// メイン生成関数
function generate() {
  // キャンバス初期化
  const canvas = Array(HEIGHT).fill(null).map(() => Array(WIDTH).fill(' '));
  
  // 時間帯を決定
  const isNight = Math.random() > 0.5;
  
  // 空の描画
  const skyChar = isNight ? ' ' : pick([' ', ' ', ' ']);
  for (let y = 0; y < HEIGHT - 5; y++) {
    for (let x = 0; x < WIDTH; x++) {
      canvas[y][x] = skyChar;
    }
  }
  
  // 星（夜のみ）
  if (isNight) {
    const stars = generateStars(rand(10, 30));
    stars.forEach(s => {
      if (s.y < HEIGHT && s.x < WIDTH) {
        canvas[s.y][s.x] = s.char;
      }
    });
    
    // 月
    const moon = generateMoon();
    moon.forEach(m => {
      if (m.y < HEIGHT && m.x >= 0 && m.x < WIDTH) {
        canvas[m.y][m.x] = m.char;
      }
    });
  } else {
    // 太陽
    const sunX = rand(10, WIDTH - 10);
    const sunY = rand(2, 6);
    canvas[sunY][sunX] = '☀';
  }
  
  // 地面
  const groundY = HEIGHT - 5;
  for (let y = groundY; y < HEIGHT; y++) {
    for (let x = 0; x < WIDTH; x++) {
      canvas[y][x] = pick(['_', '_', '_', ' ']);
    }
  }
  
  // 山（2-4個）
  const mountainCount = rand(2, 4);
  for (let i = 0; i < mountainCount; i++) {
    const mountain = generateMountain(groundY, rand(3, 7), pick(['▲', '△', '^']));
    mountain.forEach(m => {
      if (m.y >= 0 && m.y < HEIGHT && m.x >= 0 && m.x < WIDTH) {
        canvas[m.y][m.x] = m.char;
      }
    });
  }
  
  // 川（50%の確率）
  if (Math.random() > 0.5) {
    const riverY = rand(groundY, HEIGHT - 2);
    const river = generateRiver(riverY);
    river.forEach(r => {
      if (r.y < HEIGHT && r.x >= 0 && r.x < WIDTH) {
        canvas[r.y][r.x] = r.char;
      }
    });
  }
  
  // 木（3-6個）
  const treeCount = rand(3, 6);
  for (let i = 0; i < treeCount; i++) {
    const tree = generateTree(rand(5, WIDTH - 5), groundY + rand(-1, 2));
    tree.forEach(t => {
      if (t.y >= 0 && t.y < HEIGHT && t.x >= 0 && t.x < WIDTH) {
        canvas[t.y][t.x] = t.char;
      }
    });
  }
  
  // 家（0-2個）
  const houseCount = rand(0, 2);
  for (let i = 0; i < houseCount; i++) {
    const house = generateHouse(rand(10, WIDTH - 10), groundY - 2);
    house.forEach(h => {
      if (h.y >= 0 && h.y < HEIGHT && h.x >= 0 && h.x < WIDTH) {
        canvas[h.y][h.x] = h.char;
      }
    });
  }
  
  // 出力
  const title = isNight ? '🌙 夜の風景' : '☀️ 昼の風景';
  let output = '\n' + '='.repeat(WIDTH) + '\n';
  output += `  ${title}\n`;
  output += '='.repeat(WIDTH) + '\n';
  
  for (let y = 0; y < HEIGHT; y++) {
    output += '|' + canvas[y].join('') + '|\n';
  }
  
  output += '='.repeat(WIDTH) + '\n';
  output += `  Generated: ${new Date().toLocaleString('ja-JP')}\n`;
  
  return output;
}

// 実行
if (require.main === module) {
  console.log(generate());
}

module.exports = { generate };
