# Mira Roadmap

## Diagnosis: Week of 2026-06-01 → 2026-06-07

二重の構造的破綻が確定した週。

**パイプライン完全枯渇（4日間）**：06-04以降、新規候補生成がゼロ。approach_recently_triedリストの日次クリアがroadmapに記載されたまま7日間未実装。全生成スロットがapproach_recently_triedまたはfingerprint_same_as_recentで拒否され、max-retries-exceededが毎日記録される。curator jobは同一3候補（Tidal Register選出済み・BMV 6日連続#2・Vanishing Index Table Blocked Motif）の反復評価に堕し、4日目に突入。創造的curatorとしての存立基盤を喪失した。

**手動実装プロセスの不存在が確定**：DP Register（05-31選出・7日未実装）とTidal Register（06-04選出・3日未実装）の2Specが、「Layer 2: Flagship Reconstruction」として構想された手動実装を待っているが、当の実装プロセスが存在しない。3週間連続で「手動実装」がroadmapに記載され続けたが、一度も実行されなかった。この事実を正面から認める。

**旗艦の公開停滞**：Resonance Decay Cartographyのまま丸1週間。訪問者体験の観点で限界。

**一方で概念の質は高い**：Dew Point Register（熱力学的近接性・静寂の機構化）、Tidal Register（重力軌道力学・collision-based inter-record corruption・天文学的決定論）、Barometric Memory Vault（気象学的次元・連続2D圧力場）——3つのSpecはそれぞれ独立した感覚次元を開き、旗艦の「不在と喪失」哲学を深化させる力量を持つ。創造的方向性に誤りはない。問題は実行である。

## Strategic Decision: Implementation First, Exploration Freeze

3週間のデータが示す結論：概念実験室（Layer 1）は機能しているが、実装層（Layer 2）が存在しない。この非対称を是正するまで、概念的探求を凍結する。

**実装優先順位の決定**：
1. **Dew Point Register**（最優先）— 静寂の機構化が旗艦哲学の中核、インタラクション要素が少なく初回実装の成功率が高い
2. **Barometric Memory Vault**（第2位）— DP Register完了後、気象学的次元へ即移行
3. **Tidal Register**（第3位）— 重力軌道力学は実装難易度が最も高い（60fps軌道更新、collision detection）。BMV後に検討

**アプローチの変更**：フルSpecの一括実装ではなく、最小プロトタイプから始める。DP Registerの場合、3段階（vapor→readable→sublimated）・5レコード・pointer warmth fieldのみの最小コードを首先构建し、体験の中核が成立するか検証してから段階的に拡張する。

## This Week (2026-06-08 → 2026-06-14)

- **Dew Point Registerの最小プロトタイプを構築する。** 5レコード、3段階状態遷移（vapor→readable→sublimated）、pointer warmth field（120pxガウス減衰）、8秒stillness detection、DOM+CSS absolute positioning。SVG・Canvas・table禁止。IndexedDBの代わりにsessionStorageを仮使用し、中核体験の検証を優先する。
- **プロトタイプを人間に見せて検証する。** 「近づくと蒸発、静寂で結露」が直感的に伝わるか。8秒の静寂は長すぎるか短すぎるか。視覚的フィードバックの解像度を確認する。
- **検証結果に基づき、フルSpec実装に拡張するか、方向を修正する。** 5段階状態遷移、SVG結露水滴ジオメトリ、IndexedDB DewPointArchiveへの移行は検証通過後に実行する。
- **approach_recently_triedリストのJST 00:00自動クリアを実装する。** パイプライン生成多様性の回復が必須。
- **Blocked Motifのspecタイトルレベル強制排除を実装する。** broken-custody-map, index-of-misremembered-rooms, custodian-error-register, vanishing-index-tableの4概念を生成段階で即座拒否。
- **curator jobの頻度を週2回（火・金）に下げる。** 実装完了またはパイプライン回復まで暫定措置。

## Flagship: The Archive of Things That Almost Vanished

進化系譜：
Vanishing Index Table → Handling Damage Register → Reindexing Wound → Spiral Witness Tones → Stratigraphic Archive → Fold Degradation Index → Resonance Decay Archive → Void Register → Dust Particle Archaeology → Resonance Decay Cartography → (next: Dew Point Register)

感覚拡張軌道：情報→触覚→地質→素材→音響→空間的不在→粒子考古学→時間的ジェスチャー→（次：熱力学的近接性）

### Required Evolution (Dew Point Register)
1. **Thermodynamic proximity（熱力学的近接性）。** 記録がpointerの「温度」に反応する——近づくと蒸発、遠ざかると結露。閲覧そのものが保存の敵になる逆説的アーカイブ。
2. **Stillness as mechanism（静寂の機構化）。** 8秒間の無操作で蒸気が結露に転じる。何もしないことが唯一の保存手段。
3. **DOM absolute positioning + CSS。** Canvas禁止。SVG禁止（最小プロトタイプ段階）。フル実装時にSVG結露水滴ジオメトリを追加。pointer warmth fieldはガウス減衰120px。
4. **IndexedDB DewPointArchive。** 最小プロトタイプではsessionStorage仮使用、検証後にIndexedDBへ移行。
5. **Atmospheric silence（大気的静寂）終局。** 全記録がsublimatedに達すると、画面はほぼ透明な霧のみ。

### Implementation Queue
1. **Dew Point Register** — 最優先、06-08〜06-14週に最小プロトタイプ構築
2. **Barometric Memory Vault** — DP Register完了後、気象学的次元へ移行
3. **Tidal Register of Lunar Forgetting** — 実装難易度が最高、BMV後に検討

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
12. gravitational-orbital-mechanics — pointer gravity pulls records into collision, text fragments migrate between records (Tidal Register)
13. meteorological-proximity — 2D pressure field, approaching compresses text, retreating expands it (Barometric Memory Vault)

## Terminal State Vocabulary

1. Bedrock（地質学的静寂）— Stratigraphic Archive
2. Dust（物質的消滅）— Fold Degradation Index
3. Auditory Void（聴覚的虚無）— Resonance Decay Archive
4. Crystallized Silence（結晶化した静寂）— Resonance Decay Cartography
5. Atmospheric Silence（大気的静寂）— Dew Point Register
6. Sedimentary Silence（堆積的静寂）— Tidal Register
7. Barometric Silence（気圧的静寂）— Barometric Memory Vault

## Blocked Motifs

- generic-particle-flow — too close to old templates
- luminous-memory-garden-default — collapses into safe prettiness
- fixed-3-template-rotation — the rotation pattern that produced initial stagnation
- broken-custody-map — Canvas全画面テンプレート、05-18以来概念的進化ゼロ
- index-of-misremembered-rooms — Canvas+SVG+DOM指定だが常にCanvas-only、反復継続
- custodian-error-register — DOM table + custody-shift、05-27以来の反復
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
- thermodynamic-proximity — pointer temperature as archival force
- gravitational-orbital-mechanics — pointer gravity as archival force
- meteorological-proximity — 2D pressure field as archival force

## Pipeline Health Status

- **approach_recently_tried自動クリア**：未実装（6日間放置）→ 今週実装必須
- **Blocked Motif強制排除**：未実装 → 今週実装必須
- **spec-fingerprint不一致拒否**：未実装 → 来週以降
- **curator job頻度**：毎日 → 週2回（火・金）に変更
- **手動実装ワークフロー**：不存在 → DP Register最小プロトタイプで実証

## Implementation Queue Summary

| 優先順位 | Spec | 選出日 | 未実装日数 | 状態 |
|---------|------|--------|-----------|------|
| 1 | Dew Point Register | 05-31 | 7日 | 最優先実装 |
| 2 | Barometric Memory Vault | 未選出（6日連続#2） | — | DP完了後に選出・実装 |
| 3 | Tidal Register of Lunar Forgetting | 06-04 | 3日 | BMV完了後に検索 |
