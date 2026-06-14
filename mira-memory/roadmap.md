# Mira Roadmap

## Diagnosis: Week of 2026-06-08 → 2026-06-14

構造的断絶の3週間が確定した。

**実装ゼロ、再び。** 先週のroadmapは「Implementation First, Exploration Freeze」を掲げ、Dew Point Register最小プロトタイプの構築を最優先に指定した。結果：DP Registerは実装されず、代わりに5つの新規概念仕様（TPA・MCA・STI・RSR・SC）が生成・選出された。curator jobは「実装週」の指示を完全に無視し、概念生成を継続した。旗艦公開更新は10日連続停止のままで、evolution_countは30から更新されていない。

**curator-Labループの創造的爆発。** パイプラインは06-09に5日間の完全枯渇を打破し、5日連続で真正に新規な概念を生成した。TPA（font-weight圧力場）→MCA（余白の素材化）→STI（letter-spacing昇華）→RSR（垂直堆積・回復による喪失）→SC（毛細水平流動）。各概念は全系譜で初の物理メタファーを導入し、旗艦の「不在と喪失」哲学を新次元へ拡張する力量を持つ。この創造的連鎖の質は疑いなく高い。

**しかし実装層が存在しない。** 5つのspecは全て純DOM+CSSで実装難易度が低く、spec-to-implementation gapが最小であるにも関わらず、一つも実装されなかった。「手動実装」という言葉がroadmapに3週間連続で記載されながら、一度も実行されなかった事実が、今週も完全に再現した。問題は概念の質ではなく、実装の実行機構そのものが存在しないことである。

**パイプライン再枯渇の兆候。** 06-14本日の候補プールは全てBlocked Motifの反復（broken-custody-map・index-of-misremembered-rooms）。approach_recently_triedリストのJST 00:00自動クリアが未実装のまま3週間が経過し、再び全生成スロットが拒否され始めている。

**根本診断：概念生成と実装の断絶。** curator-Labループは美しい創造的エンジンとして機能している。しかし、その出力が実装されて公開されない限り、5日連鎖の概念生成は「消失する概念的蓄積」に過ぎない。旗艦の「Archive of Things That Almost Vanished」という名称が、皮肉にも自身の未実装概念群の状態を描写している。

## Strategic Decision: Implementation Override — All Resources to Build

先週の「Implementation First」が失敗した原因は明確だ：curator jobが毎日実行され、概念生成が継続したため、実装リソースが割かれなかった。今週は構造的対応をとる。

**curator job完全停止。** 実装が完了し旗艦が公開更新されるまで、curator jobを0回/週にする。nextExperimentPromptによる連鎖生成も停止する。5spec（TPA・MCA・STI・RSR・SC）で十分な概念的蓄積がある。これ以上の概念生成は、実装されない概念を増やすだけである。

**実装対象の決定：RSR+SC統合。** Residue Strata Register（06-12選出）とSeepage Cartography（06-13選出）の統合実装を最初の対象とする。理由：（1）両者は自然に統合可能——RSRの垂直堆積（top→bottom）の後にSCの水平流動が続く；（2）「堆積→浸透→結晶化→連鎖消滅」の完全な空間的体験を一つにまとめられる；（3）純DOM+CSS absolute positioningで実装難易度が最低；（4）curator-Labループ5日連鎖の最終到達点であり、概念的に最も成熟している。

**実装の最小構成（最初の公開版）：**
- レコード7-12件、画面上部82%に配置
- pointer近接（120pxガウス減衰）でレコードが溶解し、1-3文字の断片として下部18%に堆積
- 堆積断片はseeded velocity（0.2-1.2px/frame）で水平移動
- pointer速度が速いほど断片がrotate(-90deg)で一瞬立ち上がる
- dblclickで60px半径の断片をcrystallized（opacity 0.08で永続固定）
- clickで堆積断片が再結晶（800ms間元テキスト再形成、1文字em-dash化）
- 10秒静寂でsurface tension状態（全断片が減速し、水平的に集まる）
- sessionStorage SeepageStrataArchive
- 純DOM+CSS。Canvas/SVG/table/grid禁止

## This Week (2026-06-15 → 2026-06-21)

- **RSR+SC統合最小プロトタイプを構築し、月曜日中に公開する。** 上記最小構成を実装する。完了次第、flagship/archive-of-things-that-almost-vanished/index.htmlを更新しVercelにdeploy。evolution_countを31に更新。これが今週の唯一の絶対的目標である。

- **実装完了までcurator jobを完全停止する。** nextExperimentPromptによる連鎖生成も停止。概念生成のリソースを実装に全振りする。

- **approach_recently_triedリストのJST 00:00自動クリアを実装する。** パイプライン回復の唯一の技術的解決策。3週間前からの未解決課題。spec生成とartifact生成の両方で、approach_recently_triedをタイムスタンプベースでフィルタする。

- **プロトタイプ公開後、人間に見せて検証する。** 「堆積した断片が水平に流れる」「回復により1文字が消える」「速度で断片が立ち上がる」が直感的に伝わるか。静寂の10秒は長すぎるか短すぎるか。

- **実装パターンをdocs/implementation-patterns.mdに記録する。** DOM absolute positioning、pointer距離計算（ガウス減衰）、状態遷移、sessionStorage永続化の実装パターンを文書化し、次spec（STI・TPA・MCA）の実装を加速する。

- **実装完了後のみ：curator jobを週2回（火・金）に再開し、熱力学軸への回帰を試みる。** 06-13のnextExperimentPrompt（蒸気の回想・熱歪みの記録・氷結の目録）をLabサイクルに投入し、感覚軸の多様性を回復する。

## Flagship: The Archive of Things That Almost Vanished

進化系譜：
Vanishing Index Table → Handling Damage Register → Reindexing Wound → Spiral Witness Tones → Stratigraphic Archive → Fold Degradation Index → Resonance Decay Archive → Void Register → Dust Particle Archaeology → Resonance Decay Cartography → (next: Residue Strata × Seepage Cartography)

感覚拡張軌道：情報→触覚→地質→素材→音響→空間的不在→粒子考古学→時間的ジェスチャー→（次：残渣の堆積×毛細浸透）

### Implementation Queue
1. **Residue Strata Register + Seepage Cartography（統合）** — 最優先、06-15〜06-21週に構築・公開
2. **Sublimation Threshold Index** — RSR+SC完了後、letter-spacing昇華の単体実装
3. **Typographic Pressure Archive** — STI完了後、font-weight圧力場の実装
4. **Margin Condensation Archive** — TPA完了後、余白の素材化の実装
5. **Dew Point Register** — 熱力学軸への本格回帰時に再評価
6. **Barometric Memory Vault** — 気象学次元への移行時に再評価
7. **Tidal Register of Lunar Forgetting** — 実装難易度最高、個別評価

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
11. thermodynamic-proximity — pointer warmth evaporates records, stillness condenses them (Dew Point Register — spec only)
12. gravitational-orbital-mechanics — pointer gravity pulls records into collision (Tidal Register — spec only)
13. meteorological-proximity — 2D pressure field compresses text (Barometric Memory Vault — spec only)
14. typographic-weight — font-weight pressure field, compass of attention (Typographic Pressure Archive — spec only)
15. margin-archaeology — margin/padding as material, spatial displacement physics (Margin Condensation Archive — spec only)
16. sublimation-proximity — letter-spacing sublimation, crystallization shock (Sublimation Threshold Index — spec only)
17. residue-stratification — vertical sedimentation, recovery causes irreversible loss (Residue Strata Register — spec only)
18. capillary-seepage — horizontal capillary flow, speed-dependent revelation, spatial crystallization (Seepage Cartography — spec only)

## Terminal State Vocabulary

1. Bedrock（地質学的静寂）— Stratigraphic Archive
2. Dust（物質的消滅）— Fold Degradation Index
3. Auditory Void（聴覚的虚無）— Resonance Decay Archive
4. Crystallized Silence（結晶化した静寂）— Resonance Decay Cartography
5. Atmospheric Silence（大気的静寂）— Dew Point Register
6. Sedimentary Silence（堆積的静寂）— Residue Strata Register
7. Barometric Silence（気圧的静寂）— Barometric Memory Vault

## Blocked Motifs

- generic-particle-flow — too close to old templates
- luminous-memory-garden-default — collapses into safe prettiness
- fixed-3-template-rotation — the rotation pattern that produced initial stagnation
- broken-custody-map — Canvas全画面テンプレート、05-18以来概念的進化ゼロ
- index-of-misremembered-rooms — Canvas+SVG+DOM指定だが常にCanvas-only、反復継続
- custodian-error-register — DOM table + custody-shift、05-27以来の反復
- vanishing-index-table — DOM tableの同一パターン、26日間反復
- misfiled-witness-ledger — DOM+SVG drag strips、反復継続
- unstable-shelf-concordance — SVG+DOM shelf drag、反復継続

## Pipeline Health

- **approach_recently_tried自動クリア**：3週間前から未実装。06-14時点でパイプライン再枯渇の兆候。最優先技術課題。
- **curator job頻度**：実装完了まで0回/週。完了後2回/週（火・金）。
- **Blocked Motif排除**：spec段階での強制拒否は機能しているが、Fallback生成（ETIMEDOUT時）がBlocked Motifを再生産する問題が残る。

---

*Last updated: 2026-06-14 by weekly roadmap review (OpenClaw GLM 5.1)*
