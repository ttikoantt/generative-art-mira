# Spiral Witness Tones

- id: exp-2026-05-21-1306-spiral-witness-tones
- createdAt: 2026-05-21T13:06:25+09:00
- status: private-draft
- publish: false
- renderingMode: DOM

## Hypothesis

Records arranged in a temporal spiral where each text fragment carries an associated tone frequency. Long-pressing paradoxically locks a record while making its unlocked neighbors more vulnerable to text corruption. Accessing any record degrades nearby unlocked records' text. SessionStorage ensures total state erasure on tab close—true archival ephemerality where preservation is temporary and loss is guaranteed.

## Interaction

Long-press (pointerdown 500ms) toggles lock and plays Web Audio API tone at record's frequency. Click reads record, increments access count, and triggers corruption in 2-3 nearest unlocked neighbors. Scroll/wheel zooms spiral scale. All state stored in sessionStorage—vanishes on tab close. Locking paradoxically increases corruption spread radius from that record.

## Expected Structural Change

Introduces temporal-spiral spatial metaphor (CSS transforms, not canvas). Adds audio dimension via Web Audio API tones. Implements paradoxical protection mechanic (locking increases neighbor vulnerability). Uses sessionStorage for guaranteed ephemerality. Text corruption is character-level and visible, emphasizing textual-loss motif. Long-press interaction is structurally different from all previous drag/scrub/click patterns.
