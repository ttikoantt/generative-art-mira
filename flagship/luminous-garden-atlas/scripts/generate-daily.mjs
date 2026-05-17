import { mkdir, writeFile, readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { makeYearPieces, dateKey } from "../src/garden-core.js";

const root = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const outDir = path.join(root, "public", "data");
const now = process.env.GARDEN_DATE ? new Date(`${process.env.GARDEN_DATE}T00:00:00`) : new Date();
const year = Number(process.env.GARDEN_YEAR) || now.getFullYear();
const evolution = await readEvolution(outDir);
const pieces = makeYearPieces(year, now).map((piece) => ({
  ...piece,
  evolutionVersion: evolution.version,
  generatedAt: new Date().toISOString()
}));

await mkdir(outDir, { recursive: true });
await writeFile(path.join(outDir, `${year}.json`), `${JSON.stringify({
  series: "Luminous Garden Atlas",
  year,
  through: dateKey(now),
  count: pieces.length,
  evolution,
  pieces
}, null, 2)}\n`);

console.log(`Generated ${pieces.length} pieces through ${dateKey(now)} at public/data/${year}.json`);

async function readEvolution(dir) {
  try {
    return JSON.parse(await readFile(path.join(dir, "creative-evolution.json"), "utf8"));
  } catch {
    return {
      version: "week-00",
      densityLift: 0,
      hueDrift: 0,
      lastReviewedAt: null,
      notes: "Initial deterministic garden rules."
    };
  }
}
