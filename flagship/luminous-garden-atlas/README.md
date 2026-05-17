# Luminous Garden Atlas

`365 Quiet Lights` is a daily 16:9 generative artwork series. Each daily piece stands alone, moves quietly, and reacts to touch or pointer movement. The atlas view arranges the released pieces into a zoomable garden map that grows throughout the year.

## Local Use

```bash
npm install
npm run garden:daily
npm run dev
```

- Daily piece: `http://localhost:5173/daily/YYYY-MM-DD`
- Atlas view: `http://localhost:5173/atlas/YYYY`

## Automation

Run this once on macOS to install the daily local scheduler:

```bash
npm run install:scheduler
```

It writes a LaunchAgent at:

```text
~/Library/LaunchAgents/com.luminous-garden-atlas.daily.plist
```

The job runs every day at 00:05 local time:

```bash
npm run garden:daily
```

That command updates `public/data/YYYY.json`, updates the current creative evolution settings, and writes weekly PDCA evidence when a new week starts.

## Review Evidence

Weekly creative reviews are intentionally stored outside the project so they are not uploaded with the code:

```text
~/LuminousGardenAtlasReviews/YYYY/YYYY-week-NN.md
```

Override the location when needed:

```bash
GARDEN_REVIEW_DIR=/path/outside/repo npm run review
```

## Manual Backfill

Generate for a specific date:

```bash
GARDEN_DATE=2026-05-17 npm run garden:daily
```

Force a weekly review rewrite:

```bash
GARDEN_FORCE_REVIEW=1 npm run review
```
