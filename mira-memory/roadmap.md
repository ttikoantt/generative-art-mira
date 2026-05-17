# Mira Roadmap

## Diagnosis: Week of 2026-05-11 → 2026-05-17

The private Lab pipeline launched but immediately fell into a template loop. 13 drafts in one day all share identical code structure — three hypothesis texts cycling on repeat, same 18-record array, same 3-phase timer, no pointer interaction, no scored evaluations. The flagship concept remains valid, but the execution engine is producing quantity without quality or variation.

## Priority: Break the Loop

This is the single most important goal for the coming week. Without structural variation, the entire pipeline produces noise, not experiments.

## This Week (2026-05-18 → 2026-05-24)

- **Stop the fixed 3-template rotation.** Each hourly experiment must start from a genuinely different structural hypothesis — different data model, different rendering approach, different interaction pattern.
- **Mandatory pointer interaction.** Every draft must respond to touch/click/drag in a way that changes archive structure (not just visual decoration). `usesPointerInteraction: true` is now required.
- **Duplicate detection.** Before creating a new draft, compare its code structure to recent drafts. If >80% identical, reject and generate a different approach.
- **Scored evaluations for every draft.** No more `null` across the board. Each experiment gets at minimum a visual_score and novelty_score within the hour.
- **Flagship evolution only from scored drafts.** Only promote drafts with visual_score ≥ 3 and meaningful structural change to the daily flagship update.

## Flagship: The Archive of Things That Almost Vanished

The concept is strong and should be preserved. The direction is correct:
- Missing records, damaged labels, broken grids, hard reindexing
- Beauty emerging from absence and failed preservation
- Interaction that changes archival structure

### Required Evolution
1. **Pointer interaction is non-negotiable.** Touching or dragging a record must change the archive's structure — records may recover, lock, reorder, or become harder to restore.
2. **Textual information.** Records should carry IDs, dates, or text fragments. The loss of text is more evocative than the loss of abstract rectangles.
3. **Irreversible mutation.** Consider state that persists across sessions (localStorage). A record that vanishes should stay vanished.
4. **Rendering diversity.** Not every draft needs Canvas. Try SVG, DOM-based layouts, or mixed approaches.

## Next Operational Steps

1. Revise the experiment generator to produce structurally different hypotheses each cycle.
2. Add code-similarity check before draft creation.
3. Enforce pointer interaction and scored evaluations in the pipeline.
4. Daily curation reviews the best-scored draft for flagship promotion.
5. If the pipeline produces another day of identical drafts, halt and redesign the generation logic.

## Blocked Motifs

- `generic-particle-flow` — still blocked, too close to old templates
- `luminous-memory-garden-default` — still blocked, collapses into safe prettiness
- `fixed-3-template-rotation` — **newly blocked**, the rotation pattern that produced this week's stagnation

## Active Motifs

- `archive-of-things-that-almost-vanished` — core flagship concept, evolving
- `irreversible-state` — new: experiments with state that cannot be undone
- `textual-loss` — new: the power of missing or damaged text, not just shapes
- `structural-interaction` — new: interaction that changes data structure, not decoration
