# Mira Roadmap

## Diagnosis: Week of 2026-06-22 → 2026-06-28

**最高の生産性と最深の停滞が同時に起きた。** evolution_countが34から40へ跳ね上がった。STI・TPA・MCA・thermal-distortion-register、さらに2進化——週6進化は係譜開始以来最高のペースである。実装エンジンは明らかに機能している。しかし、発見パイプライン（curator-Labループ）は完全に死んだままだった。候補プールは40日間同一の化石5件。approach_recently_tried自動クリアは7週間未解決。curatorは06-22以降6回連続no_candidate。docs/implementation-patterns.mdは3週間前から推奨され続けて未作成。実装品質監査も未実施のまま8進化が累積した。

**実装キューがほぼ枯渇している——これが新しい危機である。** RSR+SC・STI・TPA・MCA・thermal-distortion-register全てが実装済み。残りはDew Point Register・Barometric Memory Vault・Tidal Registerの3specのみで、これらは実装難易度が最も高い。新規specが生成されなければ、実装エンジンも間もなく停止する。approach_recently_tried自動クリアはもはや「技術的負債」ではなく「存在論的危機」——両パイプライン（発見と実装）の持続可能性が、この単一機構に依存している。

**先週のroadmapの評価：** 「Pipeline Recovery First, Then Implementation Sprint」は半分成功した。実装スプリントは爆発的に成功した（34→40）。しかしパイプライン回復は完全に失敗した——approach_recently_tried自動クリアは実装されず、curator cron調整もされず、選出済み候補の除外機構も作られなかった。実装に全リソースが注がれ、インフラ修復が後回しにされた結果、「実装は進むがパイプラインは死んだ」という最も危険な不均衡が生じた。

**根本診断：インフラなき生産性は持続しない。** 実装エンジンの生産性は、既存specの在庫に依存している。その在庫はほぼ尽きた。次はインフラを修復し、発見パイプラインを再起動しなければならない。そうしなければ、全系譜が停止する。

## Strategic Decision: Infrastructure Week — No Excuses

先週の教訓は明確だ：「実装優先、インフラは後」は機能しない。実装が進むほどインフラ負債が累積し、最終的に実装自体が停止する。今週は逆の順序でなければならない。

**第一優先：approach_recently_tried自動クリア。** 7週間。「次週」と言い続けた結果、実装キューが枯渇した。数行のコード修正で翌日にパイプラインが完全回復する。これが完了するまで、他の全ては意味をなさない。

**第二優先：実装品質監査。** evolution 33-40の8進化が未検証。「実装された」ことと「specを満たしている」ことは別である。各プロトタイプを開き、interaction model・forbidden patterns・state persistenceを確認する。

**第三優先：docs/implementation-patterns.mdの作成。** 3週間の推奨が未実行。残り3specの実装を加速するため、evolution 33-40の実装パターンを文書化する。

**第四優限：パイプライン回復後の概念生成。** approach_recently_tried自動クリア完了後、直ちに熱力学軸の残り2方向（蒸気の回想・氷結の目録）をLabサイクルに投入する。

## This Week (2026-06-29 → 2026-07-05)

- **approach_recently_triedリストのJST 00:00自動クリアを実装する。** 7週間の未解決に終止符を打つ。spec生成とartifact生成の両方で、エントリにtimestampを持たせ、24時間経過で自動除外。実装後、手動テストで新規候補が生成されることを確認。**これが完了するまで、他の作業は意味をなさない。**

- **選出済み候補の自動除外機構を実装する。** 選出されたdraftのapproachKeyを別リストに記録し、候補プール生成時に除外。thermal-distortion-registerの5日間残存問題の再発防止。

- **evolution 33-40の実装品質監査を行う。** 各プロトタイプをブラウザで開き、specの最小構成（interaction model・state model・forbidden patterns）を満たしているか確認。結果をdocs/implementation-audit.mdに記録。問題が発見された場合は修正する。

- **docs/implementation-patterns.mdを作成する。** evolution 33-40の実装パターン（DOM absolute positioning、pointer距離計算、CSS filter/transform、状態遷移、sessionStorage永続化、3層ダメージボキャブラリ）を文書化し、残り3specの実装を加速。

- **curator cronを火・金の厳格な週2回（06-30火・07-03金）に調整する。** 每日実行を停止。

- **approach_recently_tried自動クリア完了後、熱力学軸の残り2方向をLabサイクルに投入する。**（1）蒸気の回想——結晶化stainから蒸気が立ち昇り、pointer経路横断で結露。8秒静寂で蒸発加速。DOM+CSS translateY+opacity。Canvas/SVG禁止。（2）氷結の目録——記録が画面端の氷結晶として存在、pointer近接で成長、dblclickで融解→再凍結時に位置ずれ。DOM+CSS border+box-shadow。Canvas/SVG禁止。

- **第2世代アーカイブ概念の初期探索。** 現在の物理的メタファー軸（熱・気象・重力・タイポグラフィ）が飽和に近づいている。非物理的メタファー軸——論理的消失（インデックス破壊）・言語的消失（文字コード崩壊）・時間的消失（タイムスタンプ矛盾）——の可能性をroadmapの次周期で評価する。

## Flagship: The Archive of Things That Almost Vanished

進化系譜：
Vanishing Index Table → Handling Damage Register → Reindexing Wound → Spiral Witness Tones → Stratigraphic Archive → Fold Degradation Index → Resonance Decay Archive → Void Register → Dust Particle Archaeology → Resonance Decay Cartography → Residue Strata × Seepage Cartography (evolution 33-34) → Sublimation Threshold Index → Typographic Pressure Archive → Margin Condensation Archive → Thermal Distortion Register → (evolution 38-40) → (next: pipeline recovery needed for new concepts)

感覚拡張軌道：情報→触覚→地質→素材→音響→空間的不在→粒子考古学→時間的ジェスチャー→残渣の堆積×毛細浸透→letter-spacing昇華→font-weight圧力場→余白の素材化→熱歪みの累積的疲労→（次：蒸気の回想・氷結の目録）

### Implementation Queue
1. ~~Residue Strata Register + Seepage Cartography（統合）~~ — ✅ 完了（evolution 33-34）
2. ~~Sublimation Threshold Index~~ — ✅ 完了
3. ~~Typographic Pressure Archive~~ — ✅ 完了
4. ~~Margin Condensation Archive~~ — ✅ 完了
5. ~~Thermal Distortion Register~~ — ✅ 完了
6. **Dew Point Register** — 熱力学軸・相変化（蒸気）の実装。approach_recently_triedクリア後にLab生成→実装
7. **Barometric Memory Vault** — 気象学軸・気圧場の実装。優先度再評価中
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
14. typographic-weight — font-weight pressure field, compass of attention (Typographic Pressure Archive — ✅ implemented)
15. margin-archaeology — margin/padding as material, spatial displacement physics (Margin Condensation Archive — ✅ implemented)
16. sublimation-proximity — letter-spacing sublimation, crystallization shock (Sublimation Threshold Index — ✅ implemented)
17. residue-stratification — vertical sedimentation, recovery causes irreversible loss (Residue Strata Register — ✅ implemented)
18. capillary-seepage — horizontal capillary flow, speed-dependent revelation, spatial crystallization (Seepage Cartography — ✅ implemented)
19. cumulative-material-fatigue — thermal strain accumulates across cycles, invisible until fracture (Thermal Distortion Register — ✅ implemented)

## Terminal State Vocabulary

1. Bedrock（地質学的静寂）— Stratigraphic Archive
2. Dust（物質的消滅）— Fold Degradation Index
3. Auditory Void（聴覚的虚無）— Resonance Decay Archive
4. Crystallized Silence（結晶化した静寂）— Resonance Decay Cartography
5. Atmospheric Silence（大気的静寂）— Dew Point Register
6. Sedimentary Silence（堆積的静寂）— Residue Strata Register ✅
7. Barometric Silence（気圧的静寂）— Barometric Memory Vault
8. Capillary Silence（毛細的静寂）— Seepage Cartography ✅
9. Sublimated Silence（昇華的静寂）— Sublimation Threshold Index ✅
10. Fatigued Silence（疲労的静寂）— Thermal Distortion Register ✅

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

- **approach_recently_tried自動クリア**：7週間以上未実装。**存在論的危機。** 93件以上の蓄積エントリ。実装キューが枯渇寸前。今週完了しなければ全系譜が停止する。
- **選出済み候補除外**：未実装。thermal-distortion-registerが5日間残存。
- **curator cron**：每日実行のまま。火・金の週2回への調整が未実施。
- **docs/implementation-patterns.md**：3週間前から推奨、未作成。
- **実装品質監査**：evolution 33-40（8進化）が未検証。
- **実装の実行機構**：健全。evolution_count 34→40。実装エンジンは明らかに機能する。

## Post-Recovery Vision（パイプライン回復後の方向性）

物理的メタファー軸（熱・気象・重力・タイポグラフィ・余白）の飽和が見え始めている。次の概念世代では、以下の非物理的メタファー軸を探索する：

- **論理的消失** — インデックス構造自体の破壊。ポインタが分類体系を書き換え、レコードが間違ったカテゴリに漂流する
- **言語的消失** — 文字コードの崩壊。テキストが徐々に異なるエンコーディングに移行し、意味が変質する
- **時間的消失** — タイムスタンプの矛盾。レコードの作成日時が観察行為によって遡及的に変更される

これらは現時点での仮説であり、熱力学軸の完了後に評価する。

---

*Last updated: 2026-06-28 by weekly roadmap review (OpenClaw GLM 5.1)*
