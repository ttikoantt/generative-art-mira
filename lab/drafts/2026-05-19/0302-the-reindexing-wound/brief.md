# The Reindexing Wound

- id: exp-2026-05-19-0302-the-reindexing-wound
- createdAt: 2026-05-19T03:02:16+09:00
- status: private-draft
- publish: false
- renderingMode: DOM

## Hypothesis

A scrollable vertical archive where each record is a text fragment with seeded ID, date, and witness name. Dragging a record vertically triggers reindexing: the dragged record swaps positions with neighbors, but each swap damages both records—corrupting characters in IDs and dates. A record that has been swapped 5+ times becomes permanently illegible and collapses into a blank slot. The wound of reindexing is visible as accumulated corruption history. Unlike pointer-scrub or click-to-lock patterns, this uses vertical drag-and-drop with real-time position tracking and mutation during drag, not on drop.

## Interaction

Vertical drag on a record triggers live position tracking: as it passes neighbor records, they swap positions. Each swap increments both records' swapCount, applies character corruption to IDs and dates, and updates DOM classes. When swapCount >= 5, record collapses (textContent clears, class becomes 'collapsed-slot'). State persists in localStorage with full corruption history per record ID. Layout reflows on each swap.

## Expected Structural Change

Introduces drag-during-mutation pattern (state changes while dragging, not on drop). Collapsed records create permanent absence that affects all future interactions. Corruption is semantic (IDs and dates, not random decoration). First use of vertical-only drag reordering in the archive.
