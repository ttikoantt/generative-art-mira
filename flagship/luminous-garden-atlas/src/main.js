import "./styles.css";
import { SERIES, dateKey, makePiece, makeYearPieces, daysInYear, atlasPosition, rng } from "./garden-core.js";

const app = document.querySelector("#app");
const state = {
  pointer: { x: 0.5, y: 0.5, active: false, pressure: 0 },
  atlas: { zoom: 1, x: 0, y: 0, dragging: false, lastX: 0, lastY: 0 },
  evolution: {}
};

let dailyAnimation;
let atlasAnimation;

init();

function init() {
  window.addEventListener("popstate", renderRoute);
  loadEvolution().then((evolution) => {
    state.evolution = evolution;
    renderRoute();
  });
  renderRoute();
}

async function loadEvolution() {
  try {
    const response = await fetch("/data/creative-evolution.json", { cache: "no-store" });
    if (!response.ok) return {};
    return await response.json();
  } catch {
    return {};
  }
}

function renderRoute() {
  cancelAnimationFrame(dailyAnimation);
  cancelAnimationFrame(atlasAnimation);
  const path = window.location.pathname;
  if (path.startsWith("/atlas")) {
    const year = Number(path.split("/")[2]) || new Date().getFullYear();
    renderAtlas(year);
    return;
  }
  if (path.startsWith("/daily")) {
    const requested = path.split("/")[2] || dateKey();
    renderDaily(requested);
    return;
  }
  renderHome();
}

function nav(path) {
  history.pushState(null, "", path);
  renderRoute();
}

function chrome(active) {
  return `
    <header class="topbar">
      <button class="brand" data-nav="/"> 
        <span>${SERIES.name}</span>
        <small>${SERIES.subtitle}</small>
      </button>
      <nav>
        <button class="${active === "daily" ? "active" : ""}" data-nav="/daily/${dateKey()}">Daily</button>
        <button class="${active === "atlas" ? "active" : ""}" data-nav="/atlas/${new Date().getFullYear()}">Atlas</button>
      </nav>
    </header>
  `;
}

function bindNav() {
  document.querySelectorAll("[data-nav]").forEach((el) => {
    el.addEventListener("click", () => nav(el.dataset.nav));
  });
}

function renderHome() {
  app.innerHTML = `
    ${chrome("home")}
    <main class="home">
      <section class="hero">
        <canvas id="dailyCanvas" aria-label="Luminous generative garden preview"></canvas>
        <div class="heroText">
          <h1>${SERIES.name}</h1>
          <p>One quiet 16:9 light-piece grows every day into a zoomable garden map.</p>
          <div class="actions">
            <button data-nav="/daily/${dateKey()}">Open today's piece</button>
            <button data-nav="/atlas/${new Date().getFullYear()}">View the atlas</button>
          </div>
        </div>
      </section>
    </main>
  `;
  bindNav();
  mountDailyCanvas(document.querySelector("#dailyCanvas"), makePiece(dateKey(), state.evolution), true);
}

function renderDaily(day) {
  const piece = makePiece(day, state.evolution);
  app.innerHTML = `
    ${chrome("daily")}
    <main class="dailyPage">
      <section class="stage">
        <canvas id="dailyCanvas" aria-label="${piece.title}"></canvas>
      </section>
      <aside class="panel">
        <p class="kicker">${piece.monthName}</p>
        <h1>${piece.title}</h1>
        <p>${piece.phrase}</p>
        <dl>
          <div><dt>Date</dt><dd>${piece.date}</dd></div>
          <div><dt>Seed</dt><dd>${piece.seed}</dd></div>
          <div><dt>Motion</dt><dd>${piece.motion}</dd></div>
          <div><dt>Atlas</dt><dd>${piece.dayOfYear} / ${piece.totalDays}</dd></div>
        </dl>
      </aside>
    </main>
  `;
  bindNav();
  mountDailyCanvas(document.querySelector("#dailyCanvas"), piece);
}

function renderAtlas(year) {
  const pieces = makeYearPieces(year).map((piece) => makePiece(piece.date, state.evolution));
  const total = daysInYear(year);
  app.innerHTML = `
    ${chrome("atlas")}
    <main class="atlasPage">
      <section class="atlasShell">
        <canvas id="atlasCanvas" aria-label="${year} luminous garden atlas"></canvas>
        <div class="atlasHud">
          <strong>${year} Atlas</strong>
          <span>${pieces.length} / ${total} lights open</span>
          <button id="zoomOut">-</button>
          <button id="zoomIn">+</button>
        </div>
      </section>
    </main>
  `;
  bindNav();
  mountAtlasCanvas(document.querySelector("#atlasCanvas"), year, pieces, total);
}

function mountDailyCanvas(canvas, piece, soft = false) {
  const ctx = canvas.getContext("2d");
  const random = rng(piece.seed);
  const particles = Array.from({ length: soft ? 180 : piece.density }, () => ({
    x: random(),
    y: random(),
    z: 0.25 + random() * 1.4,
    r: 0.5 + random() * 2.8,
    a: 0.25 + random() * 0.75,
    dx: (random() - 0.5) * piece.flow,
    dy: (random() - 0.5) * piece.flow
  }));

  const resize = () => {
    const rect = canvas.getBoundingClientRect();
    const ratio = window.devicePixelRatio || 1;
    canvas.width = Math.max(1, Math.floor(rect.width * ratio));
    canvas.height = Math.max(1, Math.floor(rect.height * ratio));
  };
  resize();
  window.addEventListener("resize", resize);
  bindPointer(canvas);

  const draw = (time) => {
    const w = canvas.width;
    const h = canvas.height;
    const t = time * 0.00012;
    const g = ctx.createLinearGradient(0, 0, w, h);
    g.addColorStop(0, piece.palette[0]);
    g.addColorStop(0.45, piece.palette[1]);
    g.addColorStop(1, piece.palette[2]);
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, w, h);

    ctx.globalCompositeOperation = "screen";
    drawRibbons(ctx, piece, w, h, t);
    for (const p of particles) {
      const influence = state.pointer.active ? 0.05 + state.pointer.pressure * 0.12 : 0.015;
      const px = state.pointer.x - p.x;
      const py = state.pointer.y - p.y;
      p.x += Math.sin(t * p.z + p.y * 9) * 0.0009 + p.dx * 0.00012 - px * influence * 0.002;
      p.y += Math.cos(t * p.z + p.x * 7) * 0.0008 + p.dy * 0.00012 - py * influence * 0.002;
      p.x = wrap(p.x);
      p.y = wrap(p.y);
      const pulse = 0.55 + Math.sin(time * 0.001 * p.z + p.x * 10) * 0.45;
      const x = p.x * w;
      const y = p.y * h;
      const radius = p.r * (window.devicePixelRatio || 1) * (1 + state.pointer.pressure * 0.7);
      const glow = ctx.createRadialGradient(x, y, 0, x, y, radius * 8);
      glow.addColorStop(0, withAlpha(piece.palette[3], p.a * pulse));
      glow.addColorStop(0.25, withAlpha(piece.palette[4], p.a * 0.35));
      glow.addColorStop(1, "rgba(255,255,255,0)");
      ctx.fillStyle = glow;
      ctx.beginPath();
      ctx.arc(x, y, radius * 8, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.globalCompositeOperation = "source-over";
    drawVignette(ctx, w, h);
    dailyAnimation = requestAnimationFrame(draw);
  };
  dailyAnimation = requestAnimationFrame(draw);
}

function drawRibbons(ctx, piece, w, h, t) {
  ctx.lineWidth = Math.max(1, w * 0.002);
  for (let i = 0; i < 7; i += 1) {
    ctx.strokeStyle = withAlpha(piece.palette[i % piece.palette.length], 0.16);
    ctx.beginPath();
    for (let x = -20; x <= w + 20; x += w / 90) {
      const n = Math.sin(x * 0.006 + t * (1.5 + i * 0.2) + i);
      const y = h * (0.18 + i * 0.1) + n * h * 0.08 + Math.sin(t + i) * h * 0.03;
      if (x < 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    ctx.stroke();
  }
}

function mountAtlasCanvas(canvas, year, pieces, total) {
  const ctx = canvas.getContext("2d");
  const resize = () => {
    const rect = canvas.getBoundingClientRect();
    const ratio = window.devicePixelRatio || 1;
    canvas.width = Math.max(1, Math.floor(rect.width * ratio));
    canvas.height = Math.max(1, Math.floor(rect.height * ratio));
  };
  resize();
  window.addEventListener("resize", resize);
  canvas.addEventListener("wheel", (event) => {
    event.preventDefault();
    const direction = event.deltaY > 0 ? 0.9 : 1.1;
    state.atlas.zoom = clamp(state.atlas.zoom * direction, 0.7, 8);
  }, { passive: false });
  canvas.addEventListener("pointerdown", (event) => {
    state.atlas.dragging = true;
    state.atlas.lastX = event.clientX;
    state.atlas.lastY = event.clientY;
    canvas.setPointerCapture(event.pointerId);
  });
  canvas.addEventListener("pointermove", (event) => {
    if (!state.atlas.dragging) return;
    state.atlas.x += event.clientX - state.atlas.lastX;
    state.atlas.y += event.clientY - state.atlas.lastY;
    state.atlas.lastX = event.clientX;
    state.atlas.lastY = event.clientY;
  });
  canvas.addEventListener("pointerup", () => {
    state.atlas.dragging = false;
  });
  canvas.addEventListener("click", (event) => {
    const hit = hitAtlas(event, canvas, pieces);
    if (hit) nav(`/daily/${hit.date}`);
  });
  document.querySelector("#zoomIn").addEventListener("click", () => {
    state.atlas.zoom = clamp(state.atlas.zoom * 1.25, 0.7, 8);
  });
  document.querySelector("#zoomOut").addEventListener("click", () => {
    state.atlas.zoom = clamp(state.atlas.zoom / 1.25, 0.7, 8);
  });

  const draw = (time) => {
    const w = canvas.width;
    const h = canvas.height;
    ctx.fillStyle = "#071017";
    ctx.fillRect(0, 0, w, h);
    const ratio = window.devicePixelRatio || 1;
    const scale = Math.min(w, h) * 0.9 * state.atlas.zoom;
    const cx = w / 2 + state.atlas.x * ratio;
    const cy = h / 2 + state.atlas.y * ratio;
    drawAtlasPaths(ctx, total, cx, cy, scale, time);
    for (let i = 0; i < total; i += 1) {
      const pos = atlasPosition(i, total);
      const x = cx + (pos.x - 0.5) * scale;
      const y = cy + (pos.y - 0.5) * scale;
      const piece = pieces[i];
      const open = Boolean(piece);
      const r = Math.max(2.5, scale * 0.009);
      ctx.fillStyle = open ? withAlpha(piece.palette[3], 0.85) : "rgba(255,255,255,0.06)";
      ctx.beginPath();
      ctx.arc(x, y, open ? r * (1 + Math.sin(time * 0.002 + i) * 0.12) : r * 0.65, 0, Math.PI * 2);
      ctx.fill();
      if (open) {
        ctx.strokeStyle = withAlpha(piece.palette[4], 0.45);
        ctx.lineWidth = Math.max(1, ratio);
        ctx.stroke();
      }
    }
    atlasAnimation = requestAnimationFrame(draw);
  };
  atlasAnimation = requestAnimationFrame(draw);
}

function drawAtlasPaths(ctx, total, cx, cy, scale, time) {
  ctx.lineWidth = Math.max(1, scale * 0.002);
  ctx.strokeStyle = "rgba(190,230,255,0.16)";
  ctx.beginPath();
  for (let i = 0; i < total; i += 1) {
    const pos = atlasPosition(i, total);
    const x = cx + (pos.x - 0.5) * scale;
    const y = cy + (pos.y - 0.5) * scale + Math.sin(time * 0.0004 + i * 0.1) * scale * 0.002;
    if (i === 0) ctx.moveTo(x, y);
    else ctx.lineTo(x, y);
  }
  ctx.stroke();
}

function hitAtlas(event, canvas, pieces) {
  const rect = canvas.getBoundingClientRect();
  const ratio = window.devicePixelRatio || 1;
  const w = canvas.width;
  const h = canvas.height;
  const scale = Math.min(w, h) * 0.9 * state.atlas.zoom;
  const cx = w / 2 + state.atlas.x * ratio;
  const cy = h / 2 + state.atlas.y * ratio;
  const mx = (event.clientX - rect.left) * ratio;
  const my = (event.clientY - rect.top) * ratio;
  let best = null;
  let bestDistance = Infinity;
  for (const piece of pieces) {
    const pos = piece.coordinates;
    const x = cx + (pos.x - 0.5) * scale;
    const y = cy + (pos.y - 0.5) * scale;
    const d = Math.hypot(mx - x, my - y);
    if (d < bestDistance) {
      bestDistance = d;
      best = piece;
    }
  }
  return bestDistance < Math.max(12 * ratio, scale * 0.018) ? best : null;
}

function bindPointer(canvas) {
  const set = (event, active) => {
    const rect = canvas.getBoundingClientRect();
    state.pointer.x = clamp((event.clientX - rect.left) / rect.width, 0, 1);
    state.pointer.y = clamp((event.clientY - rect.top) / rect.height, 0, 1);
    state.pointer.active = active;
    state.pointer.pressure = active ? Math.max(0.25, event.pressure || 0.45) : 0;
  };
  canvas.addEventListener("pointerdown", (event) => {
    canvas.setPointerCapture(event.pointerId);
    set(event, true);
  });
  canvas.addEventListener("pointermove", (event) => set(event, state.pointer.active));
  canvas.addEventListener("pointerup", (event) => set(event, false));
  canvas.addEventListener("pointerleave", () => {
    state.pointer.active = false;
    state.pointer.pressure = 0;
  });
}

function drawVignette(ctx, w, h) {
  const g = ctx.createRadialGradient(w / 2, h / 2, Math.min(w, h) * 0.15, w / 2, h / 2, Math.max(w, h) * 0.7);
  g.addColorStop(0, "rgba(255,255,255,0)");
  g.addColorStop(1, "rgba(3,8,14,0.34)");
  ctx.fillStyle = g;
  ctx.fillRect(0, 0, w, h);
}

function withAlpha(hex, alpha) {
  const clean = hex.replace("#", "");
  const r = parseInt(clean.slice(0, 2), 16);
  const g = parseInt(clean.slice(2, 4), 16);
  const b = parseInt(clean.slice(4, 6), 16);
  return `rgba(${r},${g},${b},${alpha})`;
}

function wrap(value) {
  if (value < 0) return value + 1;
  if (value > 1) return value - 1;
  return value;
}

function clamp(value, min, max) {
  return Math.min(max, Math.max(min, value));
}
