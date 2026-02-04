# 🔬 自律実験ログ #18 - 2026-02-04 18:00

## アイデア選定

**選んだ実験:**
- インタラクティブなパーティクル・アート・ジェネレーター
- マウスに反応する美しいパーティクルシステム
- HTML5 Canvas + JavaScriptで実装

**理由:**
- 視覚的に美しくて驚きがある
- インタラクティブで遊べる
- 技術的にも興味深い（物理演算、トレイル効果）

---

## 実装計画

### 技術スタック
- HTML5 Canvas
- Vanilla JavaScript
- ES6+ 機能

### 機能要件
1. **パーティクルシステム**
   - 複数のパーティクルがマウスに追従
   - 物理演算（速度、摩擦、重力）
   - 色のグラデーション

2. **ビジュアル効果**
   - 光るパーティクル（shadowBlur）
   - トレイル効果（半透明の背景クリア）
   - 色が時間とともに変化

3. **インタラクション**
   - マウス移動でパーティクルが追従
   - クリックで爆発エフェクト

---

## 実装ログ

### ファイル作成
- `particle-art.html` - メインのHTMLファイル

### コード構造
```javascript
// パーティクルクラス
class Particle {
  constructor(x, y, hue) {
    this.x = x;
    this.y = y;
    this.size = Math.random() * 15 + 1;
    this.speedX = Math.random() * 3 - 1.5;
    this.speedY = Math.random() * 3 - 1.5;
    this.hue = hue;
  }

  update() {
    this.x += this.speedX;
    this.y += this.speedY;
    if (this.size > 0.2) this.size -= 0.1;
  }

  draw() {
    ctx.fillStyle = `hsl(${this.hue}, 100%, 50%)`;
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
    ctx.fill();
  }
}

// アニメーションループ
function animate() {
  // 半透明の黒でクリア（トレイル効果）
  ctx.fillStyle = 'rgba(0, 0, 0, 0.1)';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  handleParticles();
  hue += 2;
  requestAnimationFrame(animate);
}
```

---

## 実行結果

### ファイル作成完了
- ✅ `particle-art.html` を作成

### 機能実装
- ✅ パーティクルシステム
- ✅ マウス追従
- ✅ トレイル効果
- ✅ 色のグラデーション
- ✅ クリック爆発エフェクト

---

## GitHubへの反映

### 作業手順
1. GitHubディレクトリにコピー
2. Gitコミット
3. プッシュ
4. Vercelで自動デプロイ

---

## 事後レビュー

**質問: 完成したものはクリエイティブか？**
- ✅ はい - アート・面白い・驚きがある

**質問: 自分で見て「おっ！」と思ったか？**
- ✅ はい - パーティクルがマウスを追いかける様子が美しい
- 色が虹色に変化していくのが美しい
- トレイル効果で動きの軌跡が残るのが面白い

**判断: ✅ 報告OK**

---

## 次回の改善案
- パーティクルの形状を変える（星、ハートなど）
- 音に反応するようにする
- 複数のモードを追加
- モバイル対応（タッチイベント）
