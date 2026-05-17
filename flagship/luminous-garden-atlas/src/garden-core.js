const MS_PER_DAY = 24 * 60 * 60 * 1000;

export const SERIES = {
  name: "Luminous Garden Atlas",
  subtitle: "365 Quiet Lights",
  startMonth: 0,
  aspectRatio: 16 / 9
};

export const MONTHS = [
  {
    name: "Gate of First Mist",
    words: ["Mist", "Seed", "Dawn", "Veil", "Pearl"],
    palette: ["#dcecff", "#f8f2df", "#a9d8ce", "#eef7ff", "#91a8ff"],
    motion: "drift"
  },
  {
    name: "Crystal Underlight",
    words: ["Crystal", "Blue", "Frost", "Glass", "Quiet"],
    palette: ["#d7f7ff", "#b7c7ff", "#eefcff", "#7bd5e6", "#ffffff"],
    motion: "suspend"
  },
  {
    name: "Moss Constellation",
    words: ["Moss", "Sprout", "Thread", "Pale", "Bloom"],
    palette: ["#ddf6c8", "#b7e4ae", "#fff3ba", "#8fc7a2", "#efffdc"],
    motion: "gather"
  },
  {
    name: "Pollen Weather",
    words: ["Pollen", "Petal", "Gold", "Wind", "Halo"],
    palette: ["#fff0a8", "#ffd0db", "#f7fff0", "#c6ecba", "#ffc86f"],
    motion: "breathe"
  },
  {
    name: "Soft Layer Garden",
    words: ["Layer", "Garden", "Lime", "Canopy", "Nest"],
    palette: ["#dfffb0", "#a9e5bb", "#fff8d6", "#7bd6c2", "#e8d6ff"],
    motion: "ripple"
  },
  {
    name: "Rain Mirror",
    words: ["Rain", "Mirror", "Silver", "Pool", "Echo"],
    palette: ["#dbeafe", "#b7f3ee", "#f3f7ff", "#8caee6", "#d7d1ff"],
    motion: "fall"
  },
  {
    name: "Golden Current",
    words: ["Sun", "Current", "Amber", "Heat", "Lantern"],
    palette: ["#fff0a3", "#ffb75e", "#ffd5a5", "#fff8df", "#f36f45"],
    motion: "stream"
  },
  {
    name: "Night Sea Stars",
    words: ["Night", "Sea", "Star", "Depth", "Tide"],
    palette: ["#081c3a", "#0f4b7c", "#74d0ff", "#c3f4ff", "#e6d7ff"],
    motion: "orbit"
  },
  {
    name: "Amber Orchard",
    words: ["Amber", "Orchard", "Honey", "Ripe", "Glow"],
    palette: ["#ffdc8a", "#d98c4a", "#7fbf9f", "#fff4d6", "#b95f3d"],
    motion: "sway"
  },
  {
    name: "Falling Map",
    words: ["Leaf", "Map", "Copper", "Path", "Ash"],
    palette: ["#f7c66d", "#c56b43", "#684b46", "#e7dfbf", "#88a18a"],
    motion: "settle"
  },
  {
    name: "Distant Ashlight",
    words: ["Ash", "Distant", "Grey", "Signal", "Ember"],
    palette: ["#d9dde2", "#9ba7b4", "#fff1c7", "#576477", "#cfc7ff"],
    motion: "pulse"
  },
  {
    name: "Star Courtyard",
    words: ["Star", "Courtyard", "Return", "Crown", "Whole"],
    palette: ["#f7f5ff", "#b9d4ff", "#ffe7a8", "#9ce5df", "#ffffff"],
    motion: "align"
  }
];

export function dateKey(date = new Date()) {
  const d = new Date(date);
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;
}

export function dayOfYear(date) {
  const start = new Date(date.getFullYear(), 0, 1);
  return Math.floor((stripTime(date) - start) / MS_PER_DAY) + 1;
}

export function daysInYear(year) {
  return isLeapYear(year) ? 366 : 365;
}

export function isLeapYear(year) {
  return year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0);
}

export function stripTime(date) {
  return new Date(date.getFullYear(), date.getMonth(), date.getDate());
}

export function hashString(input) {
  let h = 2166136261;
  for (let i = 0; i < input.length; i += 1) {
    h ^= input.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  return h >>> 0;
}

export function rng(seed) {
  let t = seed >>> 0;
  return () => {
    t += 0x6d2b79f5;
    let r = Math.imul(t ^ (t >>> 15), 1 | t);
    r ^= r + Math.imul(r ^ (r >>> 7), 61 | r);
    return ((r ^ (r >>> 14)) >>> 0) / 4294967296;
  };
}

export function atlasPosition(index, total = 365) {
  const t = index / Math.max(1, total - 1);
  const angle = t * Math.PI * 8.4 + Math.sin(t * Math.PI * 6) * 0.4;
  const radius = 0.08 + Math.pow(t, 0.72) * 0.78;
  const seasonalBend = Math.sin(t * Math.PI * 2) * 0.08;
  return {
    x: 0.5 + Math.cos(angle) * (radius + seasonalBend) * 0.48,
    y: 0.5 + Math.sin(angle) * radius * 0.42
  };
}

export function makePiece(dateInput, evolution = {}) {
  const date = new Date(`${dateInput}T00:00:00`);
  const key = dateKey(date);
  const seed = hashString(`${SERIES.name}:${key}`);
  const random = rng(seed);
  const doy = dayOfYear(date);
  const total = daysInYear(date.getFullYear());
  const month = MONTHS[date.getMonth()];
  const position = atlasPosition(doy - 1, total);
  const adjective = pick(month.words, random);
  const noun = pick(["Light", "Garden", "Gate", "Current", "Bloom", "Map", "Pool", "Signal"], random);
  const title = `Day ${doy}: The ${adjective} ${noun}`;
  const densityLift = evolution.densityLift ?? 0;
  const hueDrift = evolution.hueDrift ?? 0;
  return {
    id: key,
    date: key,
    year: date.getFullYear(),
    dayOfYear: doy,
    totalDays: total,
    seed,
    title,
    monthName: month.name,
    motion: month.motion,
    palette: rotatePalette(month.palette, Math.floor(hueDrift + random() * 2)),
    coordinates: position,
    density: Math.round(120 + random() * 130 + densityLift),
    bloom: Number((0.45 + random() * 0.4).toFixed(3)),
    flow: Number((0.3 + random() * 0.8).toFixed(3)),
    phrase: `A ${month.motion} field from ${month.name.toLowerCase()}, placed at ${Math.round(position.x * 100)}:${Math.round(position.y * 100)} in the atlas.`
  };
}

export function makeYearPieces(year, throughDate = new Date()) {
  const total = daysInYear(year);
  const through = stripTime(throughDate);
  const pieces = [];
  for (let i = 0; i < total; i += 1) {
    const date = new Date(year, 0, i + 1);
    if (date <= through) pieces.push(makePiece(dateKey(date)));
  }
  return pieces;
}

function pick(items, random) {
  return items[Math.floor(random() * items.length) % items.length];
}

function rotatePalette(palette, amount) {
  return palette.map((_, i) => palette[((i + amount) % palette.length + palette.length) % palette.length]);
}
