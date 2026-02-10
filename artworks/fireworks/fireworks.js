/**
 * Generative Fireworks
 * 自動的に打ち上がる花火アニメーション
 */

const canvas = document.getElementById('fireworksCanvas');
const ctx = canvas.getContext('2d');

let width, height;
let fireworks = [];
let particles = [];

function resize() {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
}

class Firework {
    constructor() {
        this.reset();
    }

    reset() {
        this.x = Math.random() * width;
        this.y = height;
        this.targetY = height * (0.2 + Math.random() * 0.4);
        this.vx = (Math.random() - 0.5) * 2;
        this.vy = -(8 + Math.random() * 6);
        this.hue = Math.random() * 360;
        this.trail = [];
        this.alive = true;
    }

    update() {
        this.trail.push({ x: this.x, y: this.y, alpha: 1 });
        if (this.trail.length > 10) this.trail.shift();

        this.x += this.vx;
        this.y += this.vy;
        this.vy += 0.15; // gravity

        // Explode at target height or when velocity reverses
        if (this.vy > 0 || this.y < this.targetY) {
            this.explode();
            this.alive = false;
        }

        // Fade trail
        this.trail.forEach(t => t.alpha *= 0.9);
    }

    explode() {
        const particleCount = 80 + Math.floor(Math.random() * 60);
        for (let i = 0; i < particleCount; i++) {
            particles.push(new Particle(this.x, this.y, this.hue));
        }
    }

    draw() {
        // Draw trail
        ctx.strokeStyle = `hsla(${this.hue}, 100%, 70%, 0.5)`;
        ctx.lineWidth = 2;
        ctx.beginPath();
        this.trail.forEach((t, i) => {
            if (i === 0) ctx.moveTo(t.x, t.y);
            else ctx.lineTo(t.x, t.y);
        });
        ctx.stroke();

        // Draw head
        ctx.fillStyle = `hsl(${this.hue}, 100%, 80%)`;
        ctx.beginPath();
        ctx.arc(this.x, this.y, 3, 0, Math.PI * 2);
        ctx.fill();
    }
}

class Particle {
    constructor(x, y, hue) {
        this.x = x;
        this.y = y;
        this.hue = hue + (Math.random() - 0.5) * 30;
        const angle = Math.random() * Math.PI * 2;
        const speed = 2 + Math.random() * 6;
        this.vx = Math.cos(angle) * speed;
        this.vy = Math.sin(angle) * speed;
        this.life = 1;
        this.decay = 0.01 + Math.random() * 0.02;
        this.gravity = 0.08;
    }

    update() {
        this.x += this.vx;
        this.y += this.vy;
        this.vy += this.gravity;
        this.vx *= 0.99;
        this.vy *= 0.99;
        this.life -= this.decay;
    }

    draw() {
        const alpha = Math.max(0, this.life);
        const size = 2 * alpha;
        ctx.fillStyle = `hsla(${this.hue}, 100%, ${50 + alpha * 30}%, ${alpha})`;
        ctx.beginPath();
        ctx.arc(this.x, this.y, size, 0, Math.PI * 2);
        ctx.fill();
    }
}

let lastLaunch = 0;
const launchInterval = 1500; // Launch every 1.5 seconds on average

function animate(timestamp) {
    // Fade effect for trails
    ctx.fillStyle = 'rgba(5, 5, 20, 0.15)';
    ctx.fillRect(0, 0, width, height);

    // Launch new fireworks
    if (timestamp - lastLaunch > launchInterval - Math.random() * 1000) {
        fireworks.push(new Firework());
        lastLaunch = timestamp;
    }

    // Update and draw fireworks
    fireworks = fireworks.filter(f => f.alive);
    fireworks.forEach(f => {
        f.update();
        f.draw();
    });

    // Update and draw particles
    particles = particles.filter(p => p.life > 0);
    particles.forEach(p => {
        p.update();
        p.draw();
    });

    requestAnimationFrame(animate);
}

// Initialize
resize();
window.addEventListener('resize', resize);

// Start animation
animate(0);
