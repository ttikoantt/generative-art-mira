#!/usr/bin/env node

/**
 * Generative Poetry Generator
 * 構造を持つテキストから、意味深で美しい詩を生成する
 *
 * 文法パターン、視覚的配置、ランダム性を組み合わせて
 * 毎回異なる詩を生み出す
 */

// 語彙セット
const VOCABULARY = {
  // 名詞（抽象的・詩的）
  nouns: [
    '光', '影', '風', '夢', '時', '空', '海', '星', '夜', '朝',
    '記憶', '言葉', '静寂', '響き', '波', '砂', '月', '道', '森', '窓',
    '心', '旅', '迷い', '調べ', '欠片', '宇宙', '終わり', '始まり',
    '水面', '水平線', '夕焼け', '夜明け', '露', '霜', '雪', '霧',
    '足跡', '残響', '瞬き', '吐息', '鼓動', '鼓膜', '瞳', '指先'
  ],

  // 動詞（静的・詩的）
  verbs: [
    '流れる', '揺れる', '消える', '現れる', '沈む', '浮かぶ', '散る',
    '響く', '眠る', '覚める', '募る', '薄れる', '滲む', '絡まる',
    '超える', '通る', '残る', '帰る', '彷徨う', '渗む', '透ける',
    '抱く', '放つ', '湛える', '描く', '紡ぐ', '織る', '刻む'
  ],

  // 形容詞・形容動詞
  adjectives: [
    '静かな', '遠い', '近い', '優しい', '冷たい', '温かい', '暗い', '明るい',
    '儚い', '永遠の', '刹那の', '透明な', '白い', '黒い', '青い', '赤い',
    '深い', '浅い', '鋭い', '鈍い', '滑らかな', '粗い', '柔らかい', '硬い',
    '美しい', '哀しい', '懐かしい', '新しい', '古い', '静寂の', '幻想の'
  ],

  // 助詞・接続詞
  particles: [
    'が', 'を', 'に', 'で', 'へ', 'から', 'まで', 'より',
    'と', 'や', 'か', 'の', 'て', 'ながら', 'けれど', 'ば'
  ],

  // 接頭語・接尾語
  prefixes: [
    'ある', 'いまだ', 'かつて', 'いつか', 'まるで', 'あたかも',
    '徐々に', '静かに', 'そっと', 'ひっそりと', '密やかに'
  ],

  // 特殊フレーズ
  phrases: [
    'それは', '誰かの', '私の', '君の', '遥か彼方の',
    '忘れ去られた', 'まだ見ぬ', 'かつての', '永遠の'
  ]
};

// 詩の構造パターン
const STRUCTURES = [
  // 短歌的（5-7-5-7-7）
  {
    name: '短歌風',
    pattern: [5, 7, 5, 7, 7],
    indent: 0
  },
  // 俳句的（5-7-5）
  {
    name: '俳句風',
    pattern: [5, 7, 5],
    indent: 4
  },
  // 自由詩1
  {
    name: '自由詩',
    pattern: [7, 5, 8, 6],
    indent: 2
  },
  // 自由詩2
  {
    name: '連句風',
    pattern: [5, 7, 5, 7, 5],
    indent: 0
  }
];

class PoemGenerator {
  constructor() {
    this.rng = this.seededRandom(Math.random() * 10000);
  }

  // シード付き乱数（再現可能な詩を生成するため）
  seededRandom(seed) {
    return () => {
      seed = (seed * 9301 + 49297) % 233280;
      return seed / 233280;
    };
  }

  random(array) {
    return array[Math.floor(this.rng() * array.length)];
  }

  randomInt(min, max) {
    return Math.floor(this.rng() * (max - min + 1)) + min;
  }

  // 音節数を概算（日本語）
  countSyllables(text) {
    // 簡易的なカウント：文字数を基本とする
    // 実際にはもっと複雑だが、ここでは簡略化
    const base = text.length;
    const adjustments = {
      'っ': -1, 'ゃ': -1, 'ゅ': -1, 'ょ': -1,
      'ん': 0, 'ー': 0
    };
    let count = base;
    for (const [char, adj] of Object.entries(adjustments)) {
      count += (text.match(new RegExp(char, 'g')) || []).length * adj;
    }
    return Math.max(1, count);
  }

  // 指定した音節数のフレーズを生成
  generatePhrase(targetSyllables) {
    const attempts = 50;
    let bestPhrase = null;
    let bestDiff = Infinity;

    for (let i = 0; i < attempts; i++) {
      let phrase = '';
      let syllables = 0;

      // ランダムな文パターンを選択
      const pattern = this.randomInt(1, 3);

      if (pattern === 1) {
        // 形容詞 + 名詞 + 助詞 + 動詞
        phrase = this.random(VOCABULARY.adjectives) +
                 this.random(VOCABULARY.nouns) +
                 this.random(VOCABULARY.particles) +
                 this.random(VOCABULARY.verbs);
      } else if (pattern === 2) {
        // 名詞 + 助詞 + 名詞 + 動詞
        phrase = this.random(VOCABULARY.nouns) +
                 this.random(VOCABULARY.particles) +
                 this.random(VOCABULARY.nouns) +
                 this.random(VOCABULARY.verbs);
      } else {
        // 接頭語 + 名詞 + 助詞 + 形容詞
        phrase = this.random(VOCABULARY.prefixes) +
                 this.random(VOCABULARY.nouns) +
                 this.random(VOCABULARY.particles) +
                 this.random(VOCABULARY.adjectives);
      }

      syllables = this.countSyllables(phrase);
      const diff = Math.abs(syllables - targetSyllables);

      if (diff < bestDiff) {
        bestDiff = diff;
        bestPhrase = phrase;
        if (diff === 0) break;
      }
    }

    return bestPhrase || '静かな光';
  }

  // 詩を生成
  generatePoem() {
    const structure = this.random(STRUCTURES);
    const lines = [];

    for (const syllables of structure.pattern) {
      const line = this.generatePhrase(syllables);
      lines.push(' '.repeat(structure.indent) + line);
    }

    return {
      title: this.generateTitle(),
      lines: lines,
      structure: structure.name
    };
  }

  generateTitle() {
    const patterns = [
      () => `${this.random(VOCABULARY.nouns)}の${this.random(VOCABULARY.nouns)}`,
      () => `${this.random(VOCABULARY.adjectives)}${this.random(VOCABULARY.nouns)}`,
      () => `${this.random(VOCABULARY.nouns)}と${this.random(VOCABULARY.nouns)}`,
      () => `${this.random(VOCABULARY.prefixes).replace('に', '')}${this.random(VOCABULARY.nouns)}`
    ];
    return this.random(patterns)();
  }

  // ビジュアル装飾を追加
  decorate(poem) {
    const decorations = ['☁', '✦', '❋', '◦', '·', '✧', '❋'];
    const width = Math.max(...poem.lines.map(l => l.length)) + 8;

    let result = '\n';
    result += ' ' + '─'.repeat(width - 2) + '\n';
    result += '│' + ' '.repeat(Math.floor((width - poem.title.length - 2) / 2)) +
              poem.title +
              ' '.repeat(Math.ceil((width - poem.title.length - 2) / 2)) +
              '│\n';
    result += '│' + ' '.repeat(width - 2) + '│\n';

    for (const line of poem.lines) {
      const padding = width - line.length - 4;
      const leftPad = Math.floor(padding / 2);
      const rightPad = Math.ceil(padding / 2);

      // ランダムな装飾を左右に追加
      const leftDeco = this.random(decorations);
      const rightDeco = this.random(decorations);

      result += `│  ${leftDeco} ${' '.repeat(leftPad)}${line}${' '.repeat(rightPad)} ${rightDeco}  │\n`;
    }

    result += '│' + ' '.repeat(width - 2) + '│\n';
    result += '│' + ' '.repeat(Math.floor((width - poem.structure.length - 2) / 2)) +
              `— ${poem.structure} —` +
              ' '.repeat(Math.ceil((width - poem.structure.length - 2) / 2)) +
              '│\n';
    result += ' ' + '─'.repeat(width - 2) + '\n';

    return result;
  }
}

function main() {
  console.log('\n' + '✦'.repeat(40));
  console.log('          Generative Poetry Collection');
  console.log('          生成詩コレクション');
  console.log('✦'.repeat(40) + '\n');

  const generator = new PoemGenerator();
  const numPoems = 5;

  for (let i = 0; i < numPoems; i++) {
    const poem = generator.generatePoem();
    console.log(generator.decorate(poem));
    console.log('');
  }

  console.log('✦'.repeat(40));
  console.log('       — generated by L-System —');
  console.log('       ' + new Date().toLocaleString('ja-JP', { timeZone: 'Asia/Tokyo' }));
  console.log('✦'.repeat(40) + '\n');
}

if (require.main === module) {
  main();
}
