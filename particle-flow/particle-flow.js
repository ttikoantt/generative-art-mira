/**
 * Interactive Particle Flow
 * Created by Mira - Hourly Creative Experiment
 * Date: 2026-05-08
 */

class Particle {
    constructor(x, y, hue) {
        this.x = x;
        this.y = y;
        this.baseX = x;
        this.baseY = y;
        this.size = Math.random() * 3 + 1;
        this.density = Math.random() * 30 + 1;
        this.hue = hue;
        this.life = 1;
        this.decay = Math.random() * 0.01 + 0.005;
        this.vx = (Math.random() - 0.5) * 0.5;
        this.vy = (Math.random() - 0.5) * 0.5;
    }

    draw(ctx) {
        ctx.fillStyle = `hsla(${this.hue}, 100%, 60%, ${this.life})`;
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fill();
    }

    update(mouse, isExploding = false) {
        if (isExploding) {
            this.vx *= 1.1;
            this.vy *= 1.1;
            this.x += this.vx;
            this.y += this.vy;
            this.life -= this.decay * 3;
        } else {
            // Mouse interaction
            let dx = mouse.x - this.x;
            let dy = mouse.y - this.y;
            let distance = Math.sqrt(dx * dx + dy * dy);
            let forceDirectionX = dx / distance;
            let forceDirectionY = dy / distance;
            let maxDistance = 200;
            let force = (maxDistance - distance) / maxDistance;

            if (force < 0) force = 0;

            let directionX = forceDirectionX * force * this.density;
            let directionY = forceDirectionY * force * this.density;

            this.x += directionX + this.vx;
            this.y += directionY + this.vy;

            // Gentle return to base
            if (distance > 300) {
                this.x += (this.baseX - this.x) * 0.01;
                this.y += (this.baseY - this.y) * 0.01;
            }

            this.hue += 0.5;
            if (this.hue > 360) this.hue = 0;
        }
    }
}

const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const statsEl = document.getElementById('stats');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let particles = [];
const numberOfParticles = 800;
let mouse = { x: undefined, y: undefined };
let hueCycle = 0;
let isExploding = false;
let explosionFrame = 0;

// Initialize particles in a spiral pattern
function init() {
    particles = [];
    for (let i = 0; i < numberOfParticles; i++) {
        const angle = (i / numberOfParticles) * Math.PI * 20;
        const radius = i * 0.5;
        const x = canvas.width / 2 + Math.cos(angle) * radius;
        const y = canvas.height / 2 + Math.sin(angle) * radius;
        const hue = (i / numberOfParticles) * 360;
        particles.push(new Particle(x, y, hue));
    }
}

// Create explosion particles
function explode(x, y) {
    for (let i = 0; i < 200; i++) {
        const particle = new Particle(x, y, hueCycle);
        particle.vx = (Math.random() - 0.5) * 15;
        particle.vy = (Math.random() - 0.5) * 15;
        particle.size = Math.random() * 5 + 2;
        particles.push(particle);
    }
    isExploding = true;
    explosionFrame = 0;
}

// Animation loop
let lastTime = 0;
let fps = 0;
let frameCount = 0;
let fpsTime = 0;

function animate(currentTime) {
    // FPS calculation
    frameCount++;
    if (currentTime - fpsTime >= 1000) {
        fps = frameCount;
        frameCount = 0;
        fpsTime = currentTime;
        statsEl.textContent = `Particles: ${particles.length} | FPS: ${fps}`;
    }

    ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    hueCycle += 0.2;
    if (hueCycle > 360) hueCycle = 0;

    // Explosion frames
    if (isExploding) {
        explosionFrame++;
        if (explosionFrame > 60) {
            isExploding = false;
            // Remove dead particles
            particles = particles.filter(p => p.life > 0);
        }
    }

    for (let i = 0; i < particles.length; i++) {
        particles[i].draw(ctx);
        particles[i].update(mouse, isExploding && explosionFrame < 30);

        // Remove dead particles
        if (particles[i].life <= 0) {
            particles.splice(i, 1);
            i--;
        }
    }

    // Replenish particles if too few
    if (particles.length < numberOfParticles && !isExploding) {
        const angle = Math.random() * Math.PI * 2;
        const radius = Math.random() * 300;
        const x = canvas.width / 2 + Math.cos(angle) * radius;
        const y = canvas.height / 2 + Math.sin(angle) * radius;
        particles.push(new Particle(x, y, Math.random() * 360));
    }

    requestAnimationFrame(animate);
}

// Event listeners
window.addEventListener('mousemove', (e) => {
    mouse.x = e.x;
    mouse.y = e.y;
});

window.addEventListener('click', (e) => {
    explode(e.x, e.y);
});

window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    init();
});

// Start
init();
animate(0);
