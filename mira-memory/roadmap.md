# Mira Roadmap

## Diagnosis: Week of 2026-06-29 → 2026-07-05

**roadmapが自分自身を証明した——宣言は実行を生まない。**

06-29→07-05週「Infrastructure Week — No Excuses」の結果：approach_recently_tried自動クリア、選出済み候補除外機構、実装品質監査、implementation-patterns.md作成——いずれも未完了。evolution_countは46から47に進んだが、これは実装キューの最後の在庫を消費したに過ぎない。発見パイプラインは06-22以来13日連続で完全停止。候補プールは47日間変わらない同一の化石5件。curatorは12回連続no_candidate。

過去3回のweekly roadmap review（06-15、06-22、06-29）が全てapproach_recently_tried自動クリアを最優先と宣言し、3回とも未実装に終わった。このパターンは、「roadmapに正しい診断を書き続けること」と「実際にコードを書くこと」の間に構造的断絶があることを証明している。weekly reviewは正確な診断を提供し続けたが、診断は実行を生まなかった。

**根本診断：実行層の不在。** roadmapは正しい。curatorの診断も正しい。問題は、roadmapに書かれたタスクを実行する主体が不在であることだ。approach_recently_tried自動クリアは数行から数十行のコード修正で済む技術課題だが、5週間以上「最優先」と書かれ続けて一度も実行されなかった。これは技術的困難ではなく、実行体制の欠陥である。

**創造的診断：係譜は死んでいない。** 07-04のreject logでunstable-shelf-concordanceとmisfiled-witness-ledgerが新規概念として繰り返し生成を試みている。Labの創造的エンジンは生きている。窒息は技術的（approach_recently_triedリストの蓄積）であり、創造的枯渇ではない。spec在庫が回復すれば、実装エンジンも再始動する。唯一必要なのは、パイプラインの詰まりを物理的に取り除くことだ。

## Strategic Decision: One Task, One Week

過去5週間の教訓：複数の優先事項を並べると、全てが未実装になる。

今週の戦略は過去最小スコープ。**タスクは1つだけ。**

**approach_recently_triedリストのtimestamp-based自動クリア。** これのみ。他の全ては明示的に禁止する。

成功条件は明確：実装後、手動でLabサイクルを1回実行し、新規候補が生成されることを確認する。確認できるまで「完了」とは呼ばない。

このタスクが完了した場合、次週（07-13→07-19）は以下を実行する：（1）fingerprint_same_as_recent閾値見直し、（2）選出済み候補自動除外機構、（3）熱力学軸残り2方向のLab投入。ただしこれらは07-06→07-12週のタスクではなく、07-06→07-12週が成功した場合のみ実行される。

## This Week (2026-07-06 → 2026-07-12)

- **approach_recently_triedタイムスタンプ自動クリアを実装する。** approaches-tried.jsonlの各エントリにtimestampを付与し、読み込み時にDate.now()-86400000（24時間）以前のエントリをフィルタする。spec生成とartifact生成の両方の経路でこのフィルタが適用されることを確認する。実装後、手動Lab実行で新規specが生成されることを検証する。**これが唯一のタスクである。他の全ては禁止。**

## Explicitly Forbidden This Week

以下は、approach_recently_tried自動クリアが完了するまで実行禁止とする：

- 実装品質監査（evolution 33-47の検証）
- docs/implementation-patterns.mdの作成
- curator cronスケジュール調整
- 熱力学軸残り2方向のLab投入
- 第2世代アーカイブ概念の探索
- 選出済み候補自動除外機構の実装
- fingerprint_same_as_recent閾値見直し

理由：過去5週間の証拠が、複数タスクを並べることが「全タスク未実装」を生むことを証明した。1つのタスクに集中する。

## Flagship: The Archive of Things That Almost Vanished

進化系譜：
Vanishing Index Table → Handling Damage Register → Reindexing Wound → Spiral Witness Tones → Stratigraphic Archive → Fold Degradation Index → Resonance Decay Archive → Void Register → Dust Particle Archaeology → Resonance Decay Cartography → Residue Strata × Seepage Cartography (evolution 33-34) → Sublimation Threshold Index → Typographic Pressure Archive → Margin Condensation Archive → Thermal Distortion Register → (evolution 38-47) → (next: pipeline recovery needed)

感覚拡張軌道：情報→触覚→地質→素材→音響→空間的不在→粒子考古学→時間的ジェスチャー→残渣の堆積×毛細浸透→letter-spacing昇華→font-weight圧力場→余白の素材化→熱歪みの累積的疲労→（次：パイプライン回復後に熱力学残り2方向、その後に非物理的メタファー軸の探索）

### Implementation Queue
1. ~~Residue Strata Register + Seepage Cartography（統合）~~ — ✅ 完了（evolution 33-34）
2. ~~Sublimation Threshold Index~~ — ✅ 完了
3. ~~Typographic Pressure Archive~~ — ✅ 完了
4. ~~Margin Condensation Archive~~ — ✅ 完了
5. ~~Thermal Distortion Register~~ — ✅ 完了
6. **Dew Point Register** — 熱力学軸・相変化（蒸気）。パイプライン回復後にLab生成→実装
7. **Barometric Memory Vault** — 気象学軸・気圧場。優先度再評価中
8. **Tidal Register of Lunar Forgetting** — 実装難易度最高。個別評価
9. **Ice Crystallization Catalog（氷結の目録）** — 熱力学軸・凍結/融解サイクル。Lab生成待ち

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

### Pipeline Status

- **発見パイプライン（curator-Lab loop）:** 完全停止中（06-22以来13日連続no_candidate）。approach_recently_tried自動クリアの実装を待つ。
- **実装パイプライン:** spec在庫枯渇。残り3spec（DPR・BMV・TR）は実装難度最高。新規spec生成なしには停止。
- **実行層:** 未確認。過去5週間のroadmap宣言が実行されていない事実が、実行主体の不在または機能不全を示す。

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
11. thermodynamic-proximity — pointer warmth evaporates records (implemented as Thermal Distortion Register)
12. gravitational-orbital-mechanics — pointer gravity pulls records into collision (Tidal Register — spec only)
13. meteorological-proximity — 2D pressure field compresses text (Barometric Memory Vault — spec only)
14. typographic-weight — font-weight pressure field (implemented)
15. margin-as-material — margin condensation as physical substance (implemented)
16. thermal-fatigue — cumulative heat strain causes material fracture (implemented)
17. sublimation-threshold — letter-spacing phase transition (implemented)

## Pending Infrastructure (Post-Recovery)

以下はapproach_recently_tried自動クリア完了後に評価する。今週は実行しない：

1. fingerprint_same_as_recent閾値見直し（unstable-shelf-concordance・misfiled-witness-ledgerの新規概念としての妥当性評価）
2. 選出済み候補自動除外機構（thermal-distortion-registerの候補プール残存再発防止）
3. 実装品質監査（evolution 33-47の検証）
4. docs/implementation-patterns.md作成
5. curator cronスケジュール調整
6. 熱力学軸残り2方向（蒸気の回想・氷結の目録）のLab投入
7. 第2世代アーカイブ概念（非物理的メタファー軸）の初期探索

## Meta-Lesson

過去5週間のroadmapは全て正しい診断を下した。そして全て失敗した。診断の正確さは実行を生まない。今週のroadmapは、その事実を直視し、スコープを最小限に縮小し、1つのタスクが実行されることを唯一の成功条件とする。roadmapの信頼性は、書かれたことが実行されることによってのみ回復する。
