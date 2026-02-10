/**
 * Catch the Stars
 * 落ちてくる星をキャッチするゲーム
 */

const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

let width, height;
let player;
let stars = [];
let score = 0;
let timeLeft = 60;
let gameOver = false;
let lastTime = 0;
let starSpawnTimer = 0;
let starSpawnInterval = 1000;
let difficultyMultiplier = 1;

const keys = {};

function resize() {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;

    // Re-center player if exists
    if (player) {
        player.y = height - 80;
    }
}

class Player {
    constructor() {
        this.width = 80;
        this.height = 15;
        this.x = width / 2 - this.width / 2;
        this.y = height - 80;
        this.speed = 8;
        this.color = '#FFD700';
    }

    update() {
        if (keys['ArrowLeft'] || keys['a']) {
            this.x -= this.speed;
        }
        if (keys['ArrowRight'] || keys['d']) {
            this.x += this.speed;
        }

        // Keep in bounds
        this.x = Math.max(0, Math.min(width - this.width, this.x));
    }

    draw() {
        // Draw basket
        ctx.fillStyle = this.color;
        ctx.beginPath();
        ctx.moveTo(this.x, this.y);
        ctx.lineTo(this.x + this.width, this.y);
        ctx.lineTo(this.x + this.width - 10, this.y + this.height);
        ctx.lineTo(this.x + 10, this.y + this.height);
        ctx.closePath();
        ctx.fill();

        // Glow effect
        ctx.shadowColor = this.color;
        ctx.shadowBlur = 20;
        ctx.fill();
        ctx.shadowBlur = 0;
    }
}

class Star {
    constructor() {
        this.size = 15 + Math.random() * 10;
        this.x = Math.random() * (width - this.size * 2) + this.size;
        this.y = -this.size;
        this.speed = (2 + Math.random() * 2) * difficultyMultiplier;
        this.rotation = Math.random() * Math.PI * 2;
        this.rotationSpeed = (Math.random() - 0.5) * 0.1;
        this.hue = Math.random() * 60 + 40; // Gold to yellow
    }

    update() {
        this.y += this.speed;
        this.rotation += this.rotationSpeed;
    }

    draw() {
        ctx.save();
        ctx.translate(this.x, this.y);
        ctx.rotate(this.rotation);

        // Draw star shape
        ctx.fillStyle = `hsl(${this.hue}, 100%, 60%)`;
        ctx.beginPath();
        for (let i = 0; i < 5; i++) {
            const angle = (i * 4 * Math.PI) / 5 - Math.PI / 2;
            const x = Math.cos(angle) * this.size;
            const y = Math.sin(angle) * this.size;
            if (i === 0) ctx.moveTo(x, y);
            else ctx.lineTo(x, y);
        }
        ctx.closePath();
        ctx.fill();

        // Glow
        ctx.shadowColor = `hsl(${this.hue}, 100%, 60%)`;
        ctx.shadowBlur = 15;
        ctx.fill();

        ctx.restore();
    }

    isOffScreen() {
        return this.y > height + this.size;
    }

    collidesWith(player) {
        return (
            this.x > player.x &&
            this.x < player.x + player.width &&
            this.y + this.size > player.y &&
            this.y - this.size < player.y + player.height
        );
    }
}

function spawnStar() {
    stars.push(new Star());
}

function resetGame() {
    player = new Player();
    stars = [];
    score = 0;
    timeLeft = 60;
    gameOver = false;
    difficultyMultiplier = 1;
    starSpawnInterval = 1000;
}

function update(timestamp) {
    if (gameOver) return;

    const deltaTime = timestamp - lastTime;
    lastTime = timestamp;

    // Update timer
    timeLeft -= deltaTime / 1000;
    if (timeLeft <= 0) {
        timeLeft = 0;
        gameOver = true;
    }

    // Increase difficulty over time
    difficultyMultiplier = 1 + (60 - timeLeft) / 120;
    starSpawnInterval = Math.max(300, 1000 - (60 - timeLeft) * 10);

    // Spawn stars
    starSpawnTimer += deltaTime;
    if (starSpawnTimer > starSpawnInterval) {
        spawnStar();
        starSpawnTimer = 0;
    }

    // Update player
    player.update();

    // Update stars
    stars.forEach(star => star.update());

    // Check collisions
    stars = stars.filter(star => {
        if (star.collidesWith(player)) {
            score += 10;
            return false;
        }
        return !star.isOffScreen();
    });
}

function draw() {
    // Clear canvas
    ctx.fillStyle = '#0a0a20';
    ctx.fillRect(0, 0, width, height);

    // Draw stars
    stars.forEach(star => star.draw());

    // Draw player
    player.draw();

    // Draw UI
    ctx.fillStyle = 'white';
    ctx.font = 'bold 24px Courier New';
    ctx.fillText(`Score: ${score}`, 20, 40);
    ctx.fillText(`Time: ${Math.ceil(timeLeft)}s`, 20, 80);

    // Draw game over screen
    if (gameOver) {
        ctx.fillStyle = 'rgba(0, 0, 0, 0.7)';
        ctx.fillRect(0, 0, width, height);

        ctx.fillStyle = '#FFD700';
        ctx.font = 'bold 48px Courier New';
        ctx.textAlign = 'center';
        ctx.fillText('Game Over!', width / 2, height / 2 - 40);

        ctx.fillStyle = 'white';
        ctx.font = 'bold 32px Courier New';
        ctx.fillText(`Final Score: ${score}`, width / 2, height / 2 + 20);

        ctx.font = '20px Courier New';
        ctx.fillText('Click or tap to play again', width / 2, height / 2 + 70);
        ctx.textAlign = 'left';
    }
}

function gameLoop(timestamp) {
    update(timestamp);
    draw();
    requestAnimationFrame(gameLoop);
}

// Input handling
window.addEventListener('keydown', e => {
    keys[e.key] = true;
});

window.addEventListener('keyup', e => {
    keys[e.key] = false;
});

// Touch handling
let touchStartX = 0;
canvas.addEventListener('touchstart', e => {
    e.preventDefault();
    touchStartX = e.touches[0].clientX;
    if (gameOver) {
        resetGame();
    }
});

canvas.addEventListener('touchmove', e => {
    e.preventDefault();
    const touchX = e.touches[0].clientX;
    const diff = touchX - touchStartX;
    if (player) {
        player.x += diff * 0.5;
        player.x = Math.max(0, Math.min(width - player.width, player.x));
    }
    touchStartX = touchX;
});

canvas.addEventListener('click', () => {
    if (gameOver) {
        resetGame();
    }
});

// Initialize
resize();
window.addEventListener('resize', resize);
resetGame();
gameLoop(0);
