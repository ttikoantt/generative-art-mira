// Bursting Particles - #860
// 円形に広がる美しいパーティクル

(function() {
  const canvas = document.createElement('canvas');
  const ctx = canvas.getContext('2d');

  // 全画面表示
  function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  resize();
  window.addEventListener('resize', resize);

  document.body.style.margin = '0';
  document.body.style.overflow = 'hidden';
  document.body.style.background = '#000';
  document.body.appendChild(canvas);

  // マウス位置
  const mouse = { x: canvas.width / 2, y: canvas.height / 2 };
  let hue = 0;

  canvas.addEventListener('mousemove', (e) => {
    mouse.x = e.clientX;
    mouse.y = e.clientY;
  });

  canvas.addEventListener('touchmove', (e) => {
    e.preventDefault();
    mouse.x = e.touches[0].clientX;
    mouse.y = e.touches[0].clientY;
  }, { passive: false });

  // パーティクルクラス
  class Particle {
    constructor(x, y) {
      this.x = x;
      this.y = y;
      this.size = Math.random() * 5 + 2;
      this.speedX = Math.random() * 6 - 3;
      this.speedY = Math.random() * 6 - 3;
      this.color = `hsl(${hue}, 100%, 60%)`;
      this.life = 1;
      this.decay = Math.random() * 0.02 + 0.01;
      this.angle = Math.random() * Math.PI * 2;
      this.spin = (Math.random() - 0.5) * 0.2;
    }

    update() {
      this.x += this.speedX;
      this.y += this.speedY;
      this.angle += this.spin;
      this.speedX *= 0.99;
      this.speedY *= 0.99;
      this.life -= this.decay;
      this.size *= 0.98;
    }

    draw() {
      ctx.save();
      ctx.translate(this.x, this.y);
      ctx.rotate(this.angle);
      ctx.globalAlpha = this.life;
      ctx.fillStyle = this.color;
      ctx.beginPath();
      ctx.arc(0, 0, this.size, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();
    }
  }

  const particles = [];
  let burstTimer = 0;
  const burstInterval = 5; // バースト間隔

  function burst() {
    const particleCount = 30;
    for (let i = 0; i < particleCount; i++) {
      particles.push(new Particle(mouse.x, mouse.y));
    }
  }

  function animate() {
    // トレイル効果
    ctx.fillStyle = 'rgba(0, 0, 0, 0.1)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // 色相を変化
    hue += 0.5;
    if (hue >= 360) hue = 0;

    // 定期的にバースト
    burstTimer++;
    if (burstTimer >= burstInterval) {
      burst();
      burstTimer = 0;
    }

    // パーティクル更新・描画
    for (let i = particles.length - 1; i >= 0; i--) {
      particles[i].update();
      particles[i].draw();

      if (particles[i].life <= 0 || particles[i].size < 0.1) {
        particles.splice(i, 1);
      }
    }

    // 中心の光る点
    ctx.globalAlpha = 0.8;
    ctx.fillStyle = `hsl(${hue}, 100%, 70%)`;
    ctx.beginPath();
    ctx.arc(mouse.x, mouse.y, 8, 0, Math.PI * 2);
    ctx.fill();

    // 光るリング
    ctx.globalAlpha = 0.3;
    ctx.strokeStyle = `hsl(${hue + 180}, 100%, 60%)`;
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.arc(mouse.x, mouse.y, 15 + Math.sin(Date.now() / 200) * 5, 0, Math.PI * 2);
    ctx.stroke();

    requestAnimationFrame(animate);
  }

  animate();

  // クリックでもバースト
  canvas.addEventListener('click', () => {
    for (let i = 0; i < 5; i++) {
      setTimeout(() => burst(), i * 50);
    }
  });

  console.log('🎨 Bursting Particles - #860');
  console.log('Move mouse/touch to change position');
  console.log('Click for extra burst!');
})();
