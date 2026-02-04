#!/usr/bin/env node

/**
 * 夜の詩ジェネレーター
 * 時間帯に合わせた詩を生成する（22:00 夜モード）
 */

const wordBanks = {
  night: {
    ja: ['星空', '月明かり', '静寂', '夜風', '夢', '眠り', '闇', '街灯', '窓', '影'],
    en: ['starry sky', 'moonlight', 'silence', 'night breeze', 'dreams', 'sleep', 'darkness', 'streetlights', 'window', 'shadows']
  },
  emotions: {
    ja: ['静かに', '優しく', '深く', '遠く', '密かに', 'ゆっくりと', '揺れて', '漂って'],
    en: ['quietly', 'gently', 'deeply', 'far away', 'secretly', 'slowly', 'swaying', 'drifting']
  },
  actions: {
    ja: ['抱く', '包む', '溶ける', '歌う', '眠る', '夢見る', '渡る', '消える'],
    en: ['embrace', 'wrap', 'melt', 'sing', 'sleep', 'dream', 'cross', 'fade']
  }
};

const templates = {
  ja: [
    '【{time}の詩】\n\n{emotion}、{noun1}が{action}。\n{noun2}の中で、今日も{emotion2}終わる。\n\n静かな夜、あなたへ。',
    '【{time}】\n\n{noun1}が{emotion}{action}。\n窓の外、{noun2}が{emotion2}揺れている。\n\nおやすみ、世界。',
    '【夜の深さ】\n\n{emotion}、{noun1}と{noun2}が{action}。\n夢の入り口で、{emotion2}時が止まる。\n\n良い夢を。',
    '【{time}の静寂】\n\n{noun1}が{emotion}{action}。\n{noun2}の影が{emotion2}伸びる。\n\n夜はまだ始まったばかり。',
    '【夜の詩：短編】\n\n{emotion}、{noun1}。\n{emotion2}、{noun2}。\n\n{action}。'
  ],
  en: [
    '【Poem of {time}】\n\n{emotion}, the {noun1} {action}s.\nIn the {noun2}, today {emotion2} ends.\n\nQuiet night, to you.',
    '【{time}】\n\nThe {noun1} {action}s {emotion}.\nOutside the window, the {noun2} {action}s {emotion2}.\n\nGoodnight, world.',
    '【Depth of Night】\n\n{emotion}, {noun1} and {noun2} {action}.\nAt the entrance of dreams, time {emotion2} stops.\n\nSweet dreams.',
    '【{time} Silence】\n\nThe {noun1} {action}s {emotion}.\nThe shadows of {noun2} stretch {emotion2}.\n\nThe night has just begun.',
    '【Night Poem: Short】\n\n{emotion}, {noun1}.\n{emotion2}, {noun2}.\n\n{action}.'
  ]
};

function getRandom(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

function generatePoem(lang = 'ja') {
  const bank = wordBanks;
  const temps = templates[lang];

  const template = getRandom(temps);

  const placeholders = {
    time: lang === 'ja' ? '夜十時' : '10 PM',
    noun1: getRandom(bank.night[lang]),
    noun2: getRandom(bank.night[lang]),
    emotion: getRandom(bank.emotions[lang]),
    emotion2: getRandom(bank.emotions[lang]),
    action: getRandom(bank.actions[lang])
  };

  // 同じ単語が被らないように調整
  while (placeholders.noun2 === placeholders.noun1) {
    placeholders.noun2 = getRandom(bank.night[lang]);
  }
  while (placeholders.emotion2 === placeholders.emotion) {
    placeholders.emotion2 = getRandom(bank.emotions[lang]);
  }

  let poem = template;
  for (const [key, value] of Object.entries(placeholders)) {
    poem = poem.replace(`{${key}}`, value);
  }

  return poem;
}

function generateBoth() {
  console.log('═'.repeat(40));
  console.log('🌙 夜の詩ジェネレーター - Night Poetry Generator');
  console.log('═'.repeat(40));
  console.log('');

  console.log('🇯🇵 日本語版 Japanese Version');
  console.log('─'.repeat(40));
  console.log(generatePoem('ja'));
  console.log('');

  console.log('🇺🇸 English Version');
  console.log('─'.repeat(40));
  console.log(generatePoem('en'));
  console.log('');

  console.log('═'.repeat(40));
  console.log(`Generated at: ${new Date().toLocaleString('ja-JP', { timeZone: 'Asia/Tokyo' })}`);
  console.log('═'.repeat(40));
}

// メイン実行
if (require.main === module) {
  generateBoth();
}

module.exports = { generatePoem, generateBoth };
