# The Handling Damage Register

- id: exp-2026-05-18-1504-the-handling-damage-register
- createdAt: 2026-05-18T15:04:51+09:00
- status: private-draft
- publish: false
- renderingMode: SVG+DOM

## Hypothesis

The Handling Damage Register tests whether archive loss becomes visceral when every act of reading (pointer interaction) irreversibly degrades the record being accessed, creating tension between knowledge preservation and knowledge recovery.

## Interaction

pointerenter and click increment handling counter; each access corrupts random characters in record text and adds visual wear to SVG card edges; state persisted in localStorage

## Expected Structural Change

Each interaction must corrupt at least one text character, increment the handling counter, modify SVG card appearance, update localStorage degradation state, and change the visible information content of the record.
