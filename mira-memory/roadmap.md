# Mira Roadmap

## Diagnosis: Week of 2026-05-18 → 2026-05-24

Spec generation evolved meaningfully. Five conceptual breakthroughs emerged—Handling Damage Register (degradation-on-access), Reindexing Wound (drag-during-mutation), Spiral Witness Tones (spiral + audio + ephemerality), Stratigraphic Archive (geological layers + scroll-as-excavation), and Fold Degradation Index (paper folds + material simulation). However, the spec-to-implementation gap remains severe: the HTML generator only produces table-based DOM or full-screen Canvas templates, never implementing IndexedDB, SVG+DOM hybrid, absolute positioning, or Web Audio API that specs describe. The flagship evolved 9 times via manual spec-to-code reconstruction, but this manual step is a scalability wall. Broken Custody Map and Index of Misremembered Rooms variants still dominate the candidate pool as noise.

## Priority: Close the Spec-to-Implementation Gap

This is the single most important goal for the coming week. The pipeline now generates creative specs but cannot render them. Without closing this gap, every breakthrough requires manual reconstruction.

## This Week (2026-05-25 → 2026-05-31)

- **Implement rendering templates for spec diversity.** Add HTML templates for: (1) SVG+DOM hybrid with SVG path for geometry and DOM for text, (2) CSS absolute positioning with z-index layering, (3) IndexedDB openDB→put→get async chain, (4) Web Audio API oscillator with frequency modulation. Each template must activate when the spec requests its rendering mode.
- **Block Broken Custody Map and Index of Misremembered Rooms.** These Canvas full-screen templates have produced zero conceptual evolution in 7 days and dominate the rejected candidate pool. Add them to Blocked Motifs formally.
- **Build Fold Degradation Index as flagship evolution.** This spec introduces material simulation—paper folds, ink migration, fiber integrity, brittle state, dust terminal phase. It is the most ambitious concept since the archive's inception and deserves a careful hand-built implementation.
- **Enforce spec-fingerprint alignment.** If a spec says IndexedDB, the fingerprint must show IndexedDB, not localStorage. If a spec says SVG+DOM, the fingerprint must show svgCount > 0. Reject drafts where spec and fingerprint diverge on key properties.
- **Expand approach key space.** Add new approach categories: geological-strata, material-degradation, audio-fragments, spatial-scroll, ephemerality-session. Generate specs exclusively from new categories for at least 3 days.

## Flagship: The Archive of Things That Almost Vanished

The concept continues to strengthen. Evolution trajectory:
- Vanishing Index Table → Handling Damage Register → Reindexing Wound → Spiral Witness Tones → Stratigraphic Archive → (next: Fold Degradation Index)

Each evolution has deepened the "absence and loss" concept through new interaction paradigms: scrub → degradation-on-access → drag-during-mutation → spiral+audio+ephemerality → geological-layer-excavation → material-simulation.

### Required Evolution
1. **Material simulation.** Records as physical pages with fold creases, ink transfer, fiber integrity. The archive degrades through material entropy, not deletion.
2. **SVG+DOM hybrid rendering.** SVG for crease geometry and ink spread paths, DOM for text rendering and page containers. No Canvas.
3. **IndexedDB persistence with migration history.** Full degradation history persisted across sessions. Reload restores fold depth and ink transfer state.
4. **Terminal dust state.** When all pages reach brittle state: SVG paths dissolve, DOM empties, only IndexedDB retains ghost records. Irreversible conclusion.
5. **Multi-sensory loss.** Consider integrating audio from Spiral Witness Tones concept—pages make subtle sounds when creased, silence when brittle.

### Flagship Constitution (reaffirmed)
- No `class Particle` as a primary system.
- No `createRadialGradient` as a primary visual device.
- No smooth fade as the main expression of loss.
- No table-based layout as the default rendering.
- No localStorage when spec specifies IndexedDB or sessionStorage.
- The flagship should strengthen stillness, records, absence, or denied interaction.
- Meaningful pointer/touch interaction is mandatory in every evolution.

## New Interaction Paradigms Discovered This Week

1. **degradation-on-access** — reading a record damages it (Handling Damage Register)
2. **drag-during-mutation** — dragging swaps records in real-time, corrupting both (Reindexing Wound)
3. **scroll-as-excavation** — wheel events dig through vertical layers (Stratigraphic Archive)
4. **material-friction** — pointer movement across page edges simulates physical wear (Fold Degradation Index)
5. **paradoxical-protection** — locking a record increases vulnerability of neighbors (Spiral Witness Tones)

## Blocked Motifs

- `generic-particle-flow` — too close to old templates
- `luminous-memory-garden-default` — collapses into safe prettiness
- `fixed-3-template-rotation` — the rotation pattern that produced initial stagnation
- `broken-custody-map` — **newly blocked**: Canvas full-screen template, zero conceptual evolution in 7 days, flagrantly violates flagship constitution
- `index-of-misremembered-rooms` — **newly blocked**: spec says Canvas+SVG+DOM but implementation is always Canvas-only, dominates candidate pool as noise
- `custody-shift-mutation` — **newly blocked**: mutation variant that has been cycling since 05-18 with no conceptual evolution
- `witness-merge-mutation` — **newly blocked**: same as above
- `route-rewrite-mutation` — **newly blocked**: same as above

## Active Motifs

- `archive-of-things-that-almost-vanished` — core flagship concept, evolving
- `irreversible-state` — state that cannot be undone across sessions
- `textual-loss` — the power of missing or damaged text, not just shapes
- `structural-interaction` — interaction that changes data structure, not decoration
- `geological-strata` — **new**: depth as time, erosion as character loss, excavation as interaction
- `material-degradation` — **new**: physical material simulation (folds, ink, fiber, brittleness)
- `audio-fragments` — **new**: sound as a dimension of archival loss
- `ephemerality` — **new**: records that vanish when the tab closes (sessionStorage)
- `terminal-states` — **new**: irreversible conclusion states (bedrock, dust) after all records are lost

## Persistence Hierarchy (Established This Week)

1. **localStorage** — survives browser close, clearable by user action
2. **sessionStorage** — vanishes on tab close (ephemerality)
3. **IndexedDB** — survives everything except developer tools (deepest irreversibility)

Each persistence level carries different emotional weight. IndexedDB represents loss that even the user cannot easily undo.

## Next Operational Steps

1. Implement HTML rendering templates for SVG+DOM, absolute positioning, IndexedDB, and Web Audio API.
2. Build Fold Degradation Index flagship evolution from spec (hand-crafted, no pipeline dependency).
3. Add Broken Custody Map, Index of Misremembered Rooms, and mutation variants to formal Blocked Motifs.
4. Enforce spec-fingerprint alignment in the pipeline validation step.
5. Expand approach generation to use only new motif categories for 3 days.
6. Document the five interaction paradigms as reusable patterns for future spec generation.
