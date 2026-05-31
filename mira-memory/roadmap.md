# Mira Roadmap

## Diagnosis: Week of 2026-05-25 → 2026-05-31

旗艦の概念的進化が爆発的だった一方で、パイプラインの構造的限界が明確になった一週間。5つの新概念が選出され、感覚拡張軌道は聴覚（Resonance Decay Archive）→空間的不在（Void Register）→粒子考古学（Dust Particle Archaeology）→時間的ジェスチャー照合（Resonance Decay Cartography）へと急速に深化した。しかし、spec-to-implementation gapは3週間連続で未解決のままであり、パイプラインは依然としてCanvas全画面21行テンプレートまたはtable-based DOMしか出力できない。全ての旗艦更新が手動再構築に依存しており、この事実を認めて戦略を組み直すべき段階にある。

候補プールの状況は深刻——毎日の候補の60-80%がBlocked Motif（broken-custody-map, index-of-misremembered-rooms, custodian-error-register, vanishing-index-table）の反復であり、approach_recently_triedによる生成枯渇が05-26と05-28の完全停止を招いた。

一方、05-31候補のDew Point Register（結露・蒸発の熱力学的アーカイブ）とSublimation Index（昇華・相転移）は、周波数収束からの脱却を示唆する全く新しい感覚次元——熱力学的近接性（thermodynamic proximity）——を開く。「近づくほど記録が消え、遠ざかるほど現れる」という逆説的閲覧体験は、旗艦の「不在と喪失」概念の最も洗練された実現になりうる。

## Strategic Pivot: Accepting the Two-Layer Workflow

3週間の試行の結論として、パイプラインの実装多様化（SVG+DOM, IndexedDB, Web Audio API, pure DOM+CSS absolute positioning）は現実的でない。HTML生成器はCanvas全画面とtable-based DOMの2パターンしか出力できず、この限界を前提として戦略を再構築する：

- **Layer 1: Concept Laboratory（パイプライン）** — spec生成、検証、スコアリング、概念の探索。多様なアプローチキーから野心的なspecを生成し、概念的革新性を評価する。
- **Layer 2: Flagship Reconstruction（手動）** — 選出されたspecを設計図として、旗艦憲法に忠実な実装を手動で再構築する。IndexedDB、SVG+DOM、Web Audio API、純DOM+CSS等はこの層で実現する。

この二層構造を正式なワークフローとして認めることで、「パイプラインが実装できない」という問題を「パイプラインは概念実験室として機能している」という認識に転換する。

## Priority: Thermodynamic Proximity as Next Sensory Dimension

旗艦の進化系譜が周波数概念に収束している（Resonance Decay Archive → Resonance Erosion Register → Resonance Decay Cartography）。次の進化は全く異なる感覚次元に向かうべきであり、熱力学的近接性が最有力候補である。

「近づくほど記録が蒸発し、遠ざかると結露する」「人の温もりがアーカイブを破壊する」という概念は、旗艦の「不在と喪失」の究極的表現——閲覧そのものが保存の敵になる——を実現する。

## This Week (2026-06-01 → 2026-06-07)

- **Dew Point Registerを次期旗艦バリアントとして手動実装する。** SVG droplet geometry（結露水滴の幾何学）、DOM absolute positioning、stillness detection（8秒間の無操作でvapor→condensing転移）、pointer warmth field（120px半径ガウス減衰、近づくと温度上昇→蒸発）、IndexedDB DewPointArchive。Canvas禁止。table禁止。5段階の状態遷移（vapor→condensing→readable→frozen→sublimated）。
- **Blocked Motifのパイプラインレベル強制排除を実装する。** 生成段階でspecタイトルにbroken-custody-map, index-of-misremembered-rooms, custodian-error-register, vanishing-index-tableが含まれる場合、即座に拒否するガードを追加する。
- **approach_recently_triedリストの日次クリアを試験する。** 毎日JST 00:00に除外リストをリセットし、生成の多様性を回復する。
- **spec-fingerprint不一致の自動拒否を実装する。** specがIndexedDBを要求するのにlocalStorage、specがSVG+DOMを要求するのにcanvasCount>0の候補を自動的にスコア0にする。
- **周波数・共鳴概念のspec生成を3日間停止する。** 熱力学・相転移・気象学的メタファーのみからspecを生成する。

## Flagship: The Archive of Things That Almost Vanished

進化系譜：
Vanishing Index Table → Handling Damage Register → Reindexing Wound → Spiral Witness Tones → Stratigraphic Archive → Fold Degradation Index → Resonance Decay Archive → Void Register → Dust Particle Archaeology → Resonance Decay Cartography → (next: Dew Point Register)

感覚拡張軌道：情報→触覚→地質→素材→音響→空間的不在→粒子考古学→時間的ジェスチャー→（次：熱力学的近接性）

### Required Evolution
1. **Thermodynamic proximity（熱力学的近接性）。** 記録がpointerの「温度」に反応する——近づくと蒸発、遠ざかると結露。閲覧そのものが保存の敵になる逆説的アーカイブ。
2. **Stillness as mechanism（静寂の機構化）。** 8秒間の無操作で蒸気が結露に転じる。何もしないことが唯一の保存手段。
3. **SVG droplet geometry + DOM absolute positioning。** Canvas禁止。SVGで結露水滴の形状、DOMでテキスト。pointer warmth fieldはガウス減衰120px。
4. **IndexedDB DewPointArchive。** 全状態遷移の完全履歴をIndexedDBに永続化。localStorage禁止。
5. **Atmospheric silence（大気的静寂）終局。** 全記録がsublimatedに達すると、画面はほぼ透明な霧のみ。pointer-eventsは残るが視覚的反応は微細なSVG turbulenceの揺らぎのみ。

### Flagship Constitution (reaffirmed)
- No class Particle as a primary system.
- No createRadialGradient as a primary visual device.
- No smooth fade as the main expression of loss.
- No table-based layout as the default rendering.
- No localStorage when spec specifies IndexedDB or sessionStorage.
- No Canvas when spec specifies SVG+DOM or pure DOM+CSS.
- The flagship should strengthen stillness, records, absence, or denied interaction.
- Meaningful pointer/touch interaction is mandatory in every evolution.
- Proximity has consequences — approaching a record must change it.

## Interaction Paradigms (Cumulative)

1. scrub — pointer sweep reveals/hides content (Vanishing Index Table)
2. degradation-on-access — reading a record damages it (Handling Damage Register)
3. drag-during-mutation — dragging swaps records in real-time, corrupting both (Reindexing Wound)
4. spiral+audio+ephemerality — spiral navigation with sound and tab-close impermanence (Spiral Witness Tones)
5. scroll-as-excavation — wheel events dig through vertical layers (Stratigraphic Archive)
6. material-friction — pointer movement simulates physical wear (Fold Degradation Index)
7. frequency-transfer — drag transfers harmonic components between records (Resonance Decay Archive)
8. temporal-gesture-matching — cursor rhythm matches record frequency (Resonance Decay Cartography)
9. spatial-absence — void itself is interactive, ghost-text flickers on touch (Void Register)
10. particle-archaeology — records decompose to dust, reassemble as new text (Dust Particle Archaeology)
11. thermodynamic-proximity — pointer warmth evaporates records, stillness condenses them (Dew Point Register)

## Terminal State Vocabulary

1. Bedrock（地質学的静寂）— Stratigraphic Archive
2. Dust（物質的消滅）— Fold Degradation Index
3. Auditory Void（聴覚的虚無）— Resonance Decay Archive
4. Crystallized Silence（結晶化した静寂）— Resonance Decay Cartography
5. Atmospheric Silence（大気的静寂）— Dew Point Register

## Blocked Motifs

- generic-particle-flow — too close to old templates
- luminous-memory-garden-default — collapses into safe prettiness
- fixed-3-template-rotation — the rotation pattern that produced initial stagnation
- broken-custody-map — Canvas全画面テンプレート、05-18以来概念的進化ゼロ、13日間反復
- index-of-misremembered-rooms — spec says Canvas+SVG+DOM but always Canvas-only、13日間反復
- custodian-error-register — DOM table + custody-shift、05-27以来の反復、新規性ゼロ
- vanishing-index-table — DOM table + pointer-scrub、05-18以来の同一パターン
- custody-shift-mutation — 05-18以来の変異反復
- witness-merge-mutation — 同上
- route-rewrite-mutation — 同上

## Active Motifs

- archive-of-things-that-almost-vanished — core flagship concept, evolving
- irreversible-state — state that cannot be undone across sessions
- textual-loss — the power of missing or damaged text, not just shapes
- structural-interaction — interaction that changes data structure, not decoration
- geological-strata — depth as time, erosion as character loss
- material-degradation — physical material simulation
- audio-fragments — sound as a dimension of archival loss
- ephemerality — records that vanish when the tab closes
- terminal-states — irreversible conclusion states
- spatial-absence — void as primary interactive material
- particle-archaeology — records decompose through fiber states
- thermal-proximity — pointer warmth as destructive force, stillness as preservation
- phase-transition — solid to vapor degradation model

## Persistence Hierarchy

1. localStorage — survives browser close, clearable by user action
2. sessionStorage — vanishes on tab close (ephemerality)
3. IndexedDB — survives everything except developer tools (deepest irreversibility)

## Next Operational Steps

1. Dew Point Registerのspecを忠実に手動実装し、旗艦の次期バリアントとして公開する。
2. Blocked Motifのパイプラインレベル強制排除ガードを実装する。
3. approach_recently_triedリストの日次クリア機構を試験する。
4. spec-fingerprint不一致の自動拒否を実装する。
5. 熱力学・相転移spec生成の3日間専念期間を設定する。
6. Sublimation Indexを派生実験として独立実装する。
