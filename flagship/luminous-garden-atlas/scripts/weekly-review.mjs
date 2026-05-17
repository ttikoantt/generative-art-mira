import { mkdir, readFile, writeFile } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { MONTHS, dateKey, dayOfYear } from "../src/garden-core.js";

const root = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const now = process.env.GARDEN_DATE ? new Date(`${process.env.GARDEN_DATE}T00:00:00`) : new Date();
const week = getWeek(now);
const publicData = path.join(root, "public", "data");
const reviewRoot = process.env.GARDEN_REVIEW_DIR || path.join(os.homedir(), "LuminousGardenAtlasReviews");
const reviewDir = path.join(reviewRoot, String(now.getFullYear()));
const markerPath = path.join(publicData, "creative-evolution.json");
const version = `${now.getFullYear()}-week-${String(week).padStart(2, "0")}`;

await mkdir(publicData, { recursive: true });
await mkdir(reviewDir, { recursive: true });

const previous = await readJson(markerPath);
if (previous?.version === version && !process.env.GARDEN_FORCE_REVIEW) {
  console.log(`Weekly review already exists for ${version}.`);
  process.exit(0);
}

const month = MONTHS[now.getMonth()];
const doy = dayOfYear(now);
const densityLift = Math.round(Math.sin(week * 0.7) * 18 + Math.cos(doy * 0.03) * 12);
const hueDrift = Math.round((week % 5) - 2);
const focus = chooseFocus(week);
const experiment = chooseExperiment(week, month.motion);
const decision = `Increase ${focus} while keeping interaction gentle; apply ${experiment} for the next seven daily pieces.`;
const evolution = {
  version,
  densityLift,
  hueDrift,
  focus,
  experiment,
  lastReviewedAt: new Date().toISOString(),
  notes: decision
};

await writeFile(markerPath, `${JSON.stringify(evolution, null, 2)}\n`);
const md = `# Luminous Garden Atlas Weekly Review

- Date: ${dateKey(now)}
- Version: ${version}
- Season area: ${month.name}
- Current motion family: ${month.motion}

## Observe

The atlas has reached day ${doy}. The current monthly vocabulary is ${month.words.join(", ")}.

## Evaluate

The series should remain calm enough for display, but each week needs a visible creative turn so the year does not collapse into repeated particle wallpaper.

## Decision

${decision}

## Changes Applied

- densityLift: ${densityLift}
- hueDrift: ${hueDrift}
- focus: ${focus}
- experiment: ${experiment}

## Next Check

Review whether the next seven pieces still feel individually frameable and whether the atlas path reads more like a garden map than a calendar grid.
`;

await writeFile(path.join(reviewDir, `${version}.md`), md);
console.log(`Wrote weekly review to ${path.join(reviewDir, `${version}.md`)}`);
console.log("Updated public/data/creative-evolution.json");

async function readJson(file) {
  try {
    return JSON.parse(await readFile(file, "utf8"));
  } catch {
    return null;
  }
}

function getWeek(date) {
  const start = new Date(date.getFullYear(), 0, 1);
  return Math.floor((date - start) / (7 * 24 * 60 * 60 * 1000)) + 1;
}

function chooseFocus(week) {
  return ["depth layering", "edge glow", "slow water response", "pollen clustering", "negative space", "seasonal contrast"][week % 6];
}

function chooseExperiment(week, motion) {
  return [
    `a softer ${motion} field near the atlas coordinate`,
    "a faint secondary color temperature after touch",
    "larger particles only at the far depth layer",
    "a quieter center with brighter peripheral blooms",
    "thin garden-path ribbons behind the light field",
    "a slightly stronger final vignette for framed display"
  ][week % 6];
}
