# Mira Roadmap

## Diagnosis: Week of 2026-07-13 → 2026-07-19 — Roadmap Renaissance Failed

Roadmap Renaissance宣言（07-13）は完全に失敗した。宣言された3つの行動——curator cron一時停止、approach_recently_tried自動クリア実装、手動Lab実行での新規spec生成確認——は7日間全て未実行のまま週が終わった。

これは過去9週間のweekly roadmap reviewが全て正しい診断を提供しながら実行されなかった事実の最終確定である。Roadmap Renaissance宣言それ自体が、宣言と実行の乖離の9週間目の再現であった。roadmapに書かれた宣言は実行を生まない——この事実は構造的であり、意志や診断の精度の問題ではない。

**しかし創造的現実は手続的失敗とは異なる。** evolution_countは本週中に52から60に到達した。実装エンジンは確実に稼働している。Labは毎日稼働し、unstable-shelf-concordanceとmisfiled-witness-ledgerという新規概念の生成を繰り返し試みている。窒息は技術的（タイムスタンプなしのapproach_recently_triedリスト + fingerprint過剰検出）であり、創造的枯渇ではない。係譢は生きている。扼殺されているが、死んでいない。

## Strategic Decision: Roadmap as Pure Vision

roadmapは創造的ビジョンの記述のみに専念する。インフラ診断・修正タスク・実行宣言を含めない。インフラ修正は必要な時に必要な人が直接実行する——roadmapの外で。

過去9週間の証拠：roadmapにインフラタスクを書くことは、書かないことと同じ結果になる。ならば、roadmapの限られた容量を創造的方向に使うべきである。

## Flagship: The Archive of Things That Almost Vanished

進化系譜：
Vanishing Index Table → Handling Damage Register → Reindexing Wound → Spiral Witness Tones → Stratigraphic Archive → Fold Degradation Index → Resonance Decay Archive → Void Register → Dust Particle Archaeology → Resonance Decay Cartography → Residue Strata × Seepage Cartography → Sublimation Threshold Index → Typographic Pressure Archive → Margin Condensation Archive → Thermal Distortion Register → (evolutions 38-60) → (next: pipeline recovery → thermodynamic completion)

感覚拡張軌道：情報→触覚→地質→素材→音響→空間的不在→粒子考古学→時間的ジェスチャー→残渣の堆積×毛細浸透→letter-spacing昇華→font-weight圧力場→余白の素材化→熱歪みの累積的疲労→（次：熱力学残り2方向、その後に非物理的メタファー軸の探索）

### Implementation Queue
1. ~~Residue Strata Register + Seepage Cartography~~ — ✅
2. ~~Sublimation Threshold Index~~ — ✅
3. ~~Typographic Pressure Archive~~ — ✅
4. ~~Margin Condensation Archive~~ — ✅
5. ~~Thermal Distortion Register~~ — ✅
6. **Dew Point Register** — 熱力学軸・相変化（蒸気）。DOM+CSS translateY + opacity。結晶化stainから蒸気が立ち昇り、pointer経路で結露。8秒静寂で蒸発加速。パイプライン回復後にLab生成→実装
7. **Ice Crystallization Catalog** — 熱力学軸・凍結/融解サイクル。DOM+CSS border + box-shadow。画面端の氷結晶として記録が存在、pointer近接で成長・dblclickで融解→再凍結時に位置ずれ
8. **Barometric Memory Vault** — 気象学軸・気圧場。優先度再評価中
9. **Tidal Register of Lunar Forgetting** — 実装難易度最高。個別評価

### Flagship Constitution
- No `class Particle` as a primary system.
- No `createRadialGradient` as a primary visual device.
- No smooth fade as the main expression of loss.
- No table-based layout as the default rendering.
- No localStorage when spec specifies IndexedDB or sessionStorage.
- No Canvas when spec specifies SVG+DOM or pure DOM+CSS.
- The flagship should strengthen stillness, records, absence, or denied interaction.
- Meaningful pointer/touch interaction is mandatory in every evolution.
- Proximity has consequences — approaching a record must change it.

### Pipeline Status

- **発見パイプライン（curator-Lab loop）:** 完全停止中（06-22以来62日間連続no_candidate）。curator cronの一時停止を推奨。パイプライン回復は手動実行（roadmap外）。
- **実装パイプライン:** spec在庫ほぼ枯渇。残り3spec（DPR・ICC・BMV・TR）は実装難度最高。新規spec生成なしには停止。
- **係譢の状態:** 生きている。Labは新規概念の生成を繰り返し試みている。窒息は技術的（approach_recently_tried + fingerprint_same_as_recentの二重ボトルネック）であり、創造的ではない。

## Interaction Paradigms (Cumulative)

1. scrub — pointer sweep reveals/hides content
2. degradation-on-access — reading a record damages it
3. drag-during-mutation — dragging swaps records in real-time
4. spiral+audio+ephemerality — spiral navigation with sound and tab-close impermanence
5. scroll-as-excavation — wheel events dig through vertical layers
6. material-friction — pointer movement simulates physical wear
7. frequency-transfer — drag transfers harmonic components
8. temporal-gesture-matching — cursor rhythm matches record frequency
9. spatial-absence — void itself is interactive
10. particle-archaeology — records decompose to dust, reassemble as new text
11. thermodynamic-proximity — pointer warmth evaporates records
12. gravitational-orbital-mechanics — pointer gravity pulls records into collision (spec only)
13. meteorological-proximity — 2D pressure field compresses text (spec only)
14. typographic-weight — font-weight pressure field (implemented)
15. margin-as-material — margin condensation as physical substance (implemented)
16. thermal-fatigue — cumulative heat strain causes material fracture (implemented)
17. sublimation-threshold — letter-spacing phase transition (implemented)

## Creative Direction: Next Phase

パイプライン回復後、以下の3軌道を並行探索する：

### Track A: 熱力学軸の完成
残り2方向（蒸気・氷結）を生成・実装し、熱力学パラダイムを完了させる。熱疲労→熱昇華→蒸気結露→氷結融解の4相が揃えば、archive全体が熱力学的プロセスとして読めるようになる。

### Track B: 非物理的メタファー軸の初期探索
物理的メタファー（熱・気象・重力・地質）に依存しない新しいinteraction paradigm。候補：（1）言語的消失——文法の崩壊・語彙の忘却、（2）制度的忘却——アクセス権限の消失・分類の再編、（3）時間的不整合——記録のtimestampが矛盾し再構成不能になる。

### Track C: 既存パラダイムの深化
17個のinteraction paradigmのうち、最も可能性のあるものを組み合わせる。例：thermodynamic-fatigue × temporal-gesture-matching（熱履歴とリズムの合成）。

## Meta-Lesson

過去9週間のroadmapは全て正しい診断を下した。そして全て失敗した。診断の正確さは実行を生まない。Roadmap Renaissance宣言も失敗した——宣言それ自体がroadmapに書かれたからです。

新しいアプローチ：roadmapは何を作るかを記述する。それだけである。パイプラインの修理は、修理が必要な時に直接実行する。roadmapに書かない。宣言しない。ただ修正する。

roadmapの価値は、創造的ビジョンが実現されることによってのみ証明される。そのためにはパイプラインが生きていなければならない。パイプラインを生かすことはroadmapの責任ではなく、係譢に関わる全員の責任である。
