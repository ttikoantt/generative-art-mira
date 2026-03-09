// Particle Flow Field - パーティクルがフロー場に沿って動くジェネレーティブアート

class Particle {
  constructor(width, height) {
    this.x = Math.random() * width;
    this.y = Math.random() * height;
    this.vx = 0;
    this.vy = 0;
    this.life = Math.random() * 200 + 100;
    this.maxLife = this.life;
    this.size = Math.random() * 2 + 1;
  }

  update(flowField, width, height) {
    // フロー場から角度を取得
    const col = Math.floor(this.x / 20);
    const row = Math.floor(this.y / 20);
    const index = col + row * Math.ceil(width / 20);

    if (flowField[index]) {
      const angle = flowField[index];
      this.vx += Math.cos(angle) * 0.1;
      this.vy += Math.sin(angle) * 0.1;
    }

    // 速度制限
    const speed = Math.sqrt(this.vx * this.vx + this.vy * this.vy);
    if (speed > 3) {
      this.vx = (this.vx / speed) * 3;
      this.vy = (this.vy / speed) * 3;
    }

    this.x += this.vx;
    this.y += this.vy;
    this.life--;
  }

  draw(ctx) {
    const alpha = this.life / this.maxLife;
    const speed = Math.sqrt(this.vx * this.vx + this.vy * this.vy);

    // 速度に応じて色を変える
    const hue = (speed * 30 + 180) % 360;

    ctx.fillStyle = `hsla(${hue}, 80%, 60%, ${alpha})`;
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
    ctx.fill();
  }

  isDead(width, height) {
    return this.life <= 0 ||
           this.x < 0 || this.x > width ||
           this.y < 0 || this.y > height;
  }
}

class FlowFieldAnimation {
  constructor(canvas) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.particles = [];
    this.flowField = [];
    this.time = 0;
    this.resize();

    window.addEventListener('resize', () => this.resize());
  }

  resize() {
    this.canvas.width = window.innerWidth;
    this.canvas.height = window.innerHeight;
    this.initFlowField();
  }

  initFlowField() {
    this.flowField = [];
    const cols = Math.ceil(this.canvas.width / 20);
    const rows = Math.ceil(this.canvas.height / 20);

    for (let i = 0; i < cols * rows; i++) {
      const x = (i % cols) * 20;
      const y = Math.floor(i / cols) * 20;
      const angle = Math.sin(x * 0.01) + Math.cos(y * 0.01);
      this.flowField.push(angle * Math.PI);
    }
  }

  updateFlowField() {
    const timeScale = 0.001;
    this.time++;

    const cols = Math.ceil(this.canvas.width / 20);
    const rows = Math.ceil(this.canvas.height / 20);

    for (let i = 0; i < cols * rows; i++) {
      const x = (i % cols) * 20;
      const y = Math.floor(i / cols) * 20;

      // パーリンノイズ風のパターン
      const angle = Math.sin(x * 0.01 + this.time * timeScale) +
                    Math.cos(y * 0.01 + this.time * timeScale) +
                    Math.sin((x + y) * 0.005 + this.time * timeScale * 0.5);

      this.flowField[i] = angle;
    }
  }

  addParticle() {
    if (this.particles.length < 500) {
      this.particles.push(new Particle(this.canvas.width, this.canvas.height));
    }
  }

  animate() {
    // 半透明の背景でトレイル効果
    this.ctx.fillStyle = 'rgba(10, 10, 20, 0.05)';
    this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

    this.updateFlowField();

    // 新しいパーティクルを追加
    for (let i = 0; i < 3; i++) {
      this.addParticle();
    }

    // パーティクルを更新・描画
    this.particles = this.particles.filter(p => {
      p.update(this.flowField, this.canvas.width, this.canvas.height);
      p.draw(this.ctx);
      return !p.isDead(this.canvas.width, this.canvas.height);
    });

    requestAnimationFrame(() => this.animate());
  }

  start() {
    this.animate();
  }
}

// 初期化
const canvas = document.getElementById('canvas');
const animation = new FlowFieldAnimation(canvas);
animation.start();

// 全画面表示ボタン
document.getElementById('fullscreenBtn').addEventListener('click', () => {
  if (document.fullscreenElement) {
    document.exitFullscreen();
  } else {
    document.documentElement.requestFullscreen();
  }
});
