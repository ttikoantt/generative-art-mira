// 迷路の中を漂う粒子のアニメーション
// 迷路を自動生成し、粒子が迷路の通路に沿って動く

class Maze {
  constructor(width, height, cellSize) {
    this.width = width;
    this.height = height;
    this.cellSize = cellSize;
    this.cols = Math.floor(width / cellSize);
    this.rows = Math.floor(height / cellSize);
    this.grid = [];
    this.generate();
  }

  generate() {
    // 深さ優先探索で迷路を生成
    this.grid = Array(this.rows).fill(null).map(() => Array(this.cols).fill(true));

    const stack = [];
    const start = { x: 1, y: 1 };
    this.grid[start.y][start.x] = false;
    stack.push(start);

    const directions = [
      { dx: 2, dy: 0 },
      { dx: -2, dy: 0 },
      { dx: 0, dy: 2 },
      { dx: 0, dy: -2 }
    ];

    while (stack.length > 0) {
      const current = stack[stack.length - 1];
      const neighbors = [];

      for (const dir of directions) {
        const nx = current.x + dir.dx;
        const ny = current.y + dir.dy;

        if (nx > 0 && nx < this.cols - 1 && ny > 0 && ny < this.rows - 1 && this.grid[ny][nx]) {
          neighbors.push({ x: nx, y: ny, wx: current.x + dir.dx / 2, wy: current.y + dir.dy / 2 });
        }
      }

      if (neighbors.length > 0) {
        const next = neighbors[Math.floor(Math.random() * neighbors.length)];
        this.grid[next.wy][next.wx] = false;
        this.grid[next.y][next.x] = false;
        stack.push({ x: next.x, y: next.y });
      } else {
        stack.pop();
      }
    }
  }

  isWall(x, y) {
    const col = Math.floor(x / this.cellSize);
    const row = Math.floor(y / this.cellSize);
    if (col < 0 || col >= this.cols || row < 0 || row >= this.rows) return true;
    return this.grid[row][col];
  }
}

class Particle {
  constructor(x, y, maze) {
    this.x = x;
    this.y = y;
    this.vx = (Math.random() - 0.5) * 4;
    this.vy = (Math.random() - 0.5) * 4;
    this.radius = 3 + Math.random() * 3;
    this.hue = Math.random() * 360;
    this.maze = maze;
    this.trail = [];
    this.maxTrail = 15;
    this.speed = 1.5 + Math.random() * 1.5;
  }

  update() {
    // 現在の方向に移動を試みる
    let nextX = this.x + this.vx * this.speed;
    let nextY = this.y + this.vy * this.speed;

    // 壁にぶつかったら方向を変える
    if (this.maze.isWall(nextX, nextY)) {
      // 新しい方向を探す
      const angles = [];
      for (let a = 0; a < Math.PI * 2; a += Math.PI / 8) {
        const testX = this.x + Math.cos(a) * this.maze.cellSize * 0.5;
        const testY = this.y + Math.sin(a) * this.maze.cellSize * 0.5;
        if (!this.maze.isWall(testX, testY)) {
          angles.push(a);
        }
      }

      if (angles.length > 0) {
        const bestAngle = angles[Math.floor(Math.random() * angles.length)];
        this.vx = Math.cos(bestAngle) * (1 + Math.random());
        this.vy = Math.sin(bestAngle) * (1 + Math.random());
      } else {
        // 行き詰まった場合、ランダムに反転
        this.vx = -this.vx + (Math.random() - 0.5) * 2;
        this.vy = -this.vy + (Math.random() - 0.5) * 2;
      }
    } else {
      this.x = nextX;
      this.y = nextY;
    }

    // 軌跡を記録
    this.trail.push({ x: this.x, y: this.y });
    if (this.trail.length > this.maxTrail) {
      this.trail.shift();
    }

    // 徐々に色相を変化
    this.hue = (this.hue + 0.5) % 360;
  }

  draw(ctx) {
    // 軌跡を描画
    ctx.beginPath();
    for (let i = 0; i < this.trail.length; i++) {
      const alpha = i / this.trail.length;
      ctx.strokeStyle = `hsla(${this.hue}, 80%, 60%, ${alpha * 0.5})`;
      ctx.lineWidth = this.radius * alpha;
      if (i === 0) {
        ctx.moveTo(this.trail[i].x, this.trail[i].y);
      } else {
        ctx.lineTo(this.trail[i].x, this.trail[i].y);
      }
    }
    ctx.stroke();

    // 粒子を描画
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
    ctx.fillStyle = `hsl(${this.hue}, 80%, 60%)`;
    ctx.fill();

    // グロー効果
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.radius * 2, 0, Math.PI * 2);
    ctx.fillStyle = `hsla(${this.hue}, 80%, 60%, 0.3)`;
    ctx.fill();
  }
}

// アニメーション設定
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

let width, height, maze, particles;

function resize() {
  width = canvas.width = window.innerWidth;
  height = canvas.height = window.innerHeight;
  maze = new Maze(width, height, 40);
  particles = Array(50).fill(null).map(() => {
    let x, y;
    do {
      x = Math.random() * width;
      y = Math.random() * height;
    } while (maze.isWall(x, y));
    return new Particle(x, y, maze);
  });
}

resize();
window.addEventListener('resize', resize);

function drawMaze() {
  ctx.fillStyle = 'rgba(10, 10, 30, 0.3)';
  ctx.fillRect(0, 0, width, height);

  // 迷路の壁を描画
  ctx.fillStyle = 'rgba(40, 40, 80, 0.8)';
  for (let row = 0; row < maze.rows; row++) {
    for (let col = 0; col < maze.cols; col++) {
      if (maze.grid[row][col]) {
        ctx.fillRect(
          col * maze.cellSize,
          row * maze.cellSize,
          maze.cellSize + 1,
          maze.cellSize + 1
        );
      }
    }
  }
}

function animate() {
  drawMaze();

  // 粒子を更新・描画
  particles.forEach(p => {
    p.update();
    p.draw(ctx);
  });

  requestAnimationFrame(animate);
}

animate();
