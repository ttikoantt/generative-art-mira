// Gravitational Waves - 重力波シミュレーション
// 複数の重力源が相互作用して、粒子が美しい軌道を描く

const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

// キャンバスサイズを設定
function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}
resizeCanvas();
window.addEventListener('resize', resizeCanvas);

// 重力源のクラス
class GravitySource {
    constructor(x, y, mass) {
        this.x = x;
        this.y = y;
        this.mass = mass;
        this.radius = Math.sqrt(mass) * 3;
        this.hue = Math.random() * 360;
        
        // パルスアニメーション
        this.pulsePhase = Math.random() * Math.PI * 2;
    }
    
    update() {
        this.pulsePhase += 0.02;
    }
    
    draw() {
        // パルス効果
        const pulseRadius = this.radius + Math.sin(this.pulsePhase) * 5;
        
        // 光る効果
        const gradient = ctx.createRadialGradient(
            this.x, this.y, 0,
            this.x, this.y, pulseRadius * 3
        );
        gradient.addColorStop(0, `hsla(${this.hue}, 100%, 70%, 1)`);
        gradient.addColorStop(0.5, `hsla(${this.hue}, 100%, 50%, 0.3)`);
        gradient.addColorStop(1, `hsla(${this.hue}, 100%, 50%, 0)`);
        
        ctx.beginPath();
        ctx.arc(this.x, this.y, pulseRadius * 3, 0, Math.PI * 2);
        ctx.fillStyle = gradient;
        ctx.fill();
        
        // 中心
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        ctx.fillStyle = `hsl(${this.hue}, 100%, 70%)`;
        ctx.fill();
        
        // 重力波の輪
        ctx.beginPath();
        ctx.arc(this.x, this.y, pulseRadius * 2, 0, Math.PI * 2);
        ctx.strokeStyle = `hsla(${this.hue}, 100%, 60%, ${0.3 + Math.sin(this.pulsePhase) * 0.2})`;
        ctx.lineWidth = 2;
        ctx.stroke();
    }
}

// 粒子のクラス
class Particle {
    constructor() {
        this.reset();
    }
    
    reset() {
        this.x = Math.random() * canvas.width;
        this.y = Math.random() * canvas.height;
        this.vx = (Math.random() - 0.5) * 2;
        this.vy = (Math.random() - 0.5) * 2;
        this.radius = Math.random() * 2 + 1;
        this.trail = [];
        this.maxTrailLength = 20;
        this.hue = Math.random() * 360;
    }
    
    update(gravitySources) {
        // 全ての重力源からの引力を計算
        gravitySources.forEach(source => {
            const dx = source.x - this.x;
            const dy = source.y - this.y;
            const distance = Math.sqrt(dx * dx + dy * dy);
            
            // 距離が近すぎると発散するので最小距離を設定
            const minDistance = 50;
            const effectiveDistance = Math.max(distance, minDistance);
            
            // 重力の計算（逆二乗則）
            const force = (source.mass * 100) / (effectiveDistance * effectiveDistance);
            const angle = Math.atan2(dy, dx);
            
            this.vx += Math.cos(angle) * force * 0.01;
            this.vy += Math.sin(angle) * force * 0.01;
        });
        
        // 速度を制限
        const maxSpeed = 8;
        const speed = Math.sqrt(this.vx * this.vx + this.vy * this.vy);
        if (speed > maxSpeed) {
            this.vx = (this.vx / speed) * maxSpeed;
            this.vy = (this.vy / speed) * maxSpeed;
        }
        
        // 位置を更新
        this.x += this.vx;
        this.y += this.vy;
        
        // 軌跡を記録
        this.trail.push({ x: this.x, y: this.y });
        if (this.trail.length > this.maxTrailLength) {
            this.trail.shift();
        }
        
        // 画面外に出たらリセット
        if (this.x < -100 || this.x > canvas.width + 100 ||
            this.y < -100 || this.y > canvas.height + 100) {
            this.reset();
        }
        
        // 速度に応じて色を変化
        this.hue = (speed * 20 + this.hue * 0.95) % 360;
    }
    
    draw() {
        // 軌跡を描画
        if (this.trail.length > 1) {
            ctx.beginPath();
            ctx.moveTo(this.trail[0].x, this.trail[0].y);
            
            for (let i = 1; i < this.trail.length; i++) {
                ctx.lineTo(this.trail[i].x, this.trail[i].y);
            }
            
            const speed = Math.sqrt(this.vx * this.vx + this.vy * this.vy);
            const alpha = 0.6 - (speed / 10) * 0.4;
            
            ctx.strokeStyle = `hsla(${this.hue}, 80%, 60%, ${alpha})`;
            ctx.lineWidth = this.radius * 0.5;
            ctx.stroke();
        }
        
        // 粒子を描画
        const speed = Math.sqrt(this.vx * this.vx + this.vy * this.vy);
        const brightness = 50 + speed * 5;
        
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        ctx.fillStyle = `hsl(${this.hue}, 80%, ${Math.min(brightness, 80)}%)`;
        ctx.fill();
    }
}

// 初期化
const particleCount = 1000;
const particles = [];
const gravitySources = [];

// 初期の重力源を追加
gravitySources.push(new GravitySource(
    canvas.width * 0.3,
    canvas.height * 0.5,
    500
));
gravitySources.push(new GravitySource(
    canvas.width * 0.7,
    canvas.height * 0.5,
    500
));

// 粒子を生成
for (let i = 0; i < particleCount; i++) {
    particles.push(new Particle());
}

// クリックで新しい重力源を追加
canvas.addEventListener('click', (e) => {
    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    const mass = Math.random() * 500 + 300;
    
    gravitySources.push(new GravitySource(x, y, mass));
    document.getElementById('gravity-count').textContent = gravitySources.length;
});

// アニメーションループ
function animate() {
    // 残像効果
    ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    // 重力源を更新・描画
    gravitySources.forEach(source => {
        source.update();
        source.draw();
    });
    
    // 粒子を更新・描画
    particles.forEach(particle => {
        particle.update(gravitySources);
        particle.draw();
    });
    
    requestAnimationFrame(animate);
}

// 全画面切り替え
function toggleFullscreen() {
    if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen();
    } else {
        document.exitFullscreen();
    }
}

// 初期表示
document.getElementById('gravity-count').textContent = gravitySources.length;

// アニメーション開始
animate();
