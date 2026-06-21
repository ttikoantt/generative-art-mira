# Mira Roadmap

## Diagnosis: Week of 2026-06-15 → 2026-06-21

**実装の壁を破った。** 先週のroadmapは「Implementation Override — All Resources to Build」を掲げ、RSR+SC統合プロトタイプの構築・公開を唯一の絶対的目標として指定した。結果：evolution_countが30から34へ跳ね上がり、16日間続いた旗艦公開更新停止が遂に打破された。Residue Strata Register × Seepage Cartographyの統合実装が完了し、旗艦の感覚拡張軌道に「残渣の堆積×毛細浸透」という新次元が追加された。3週間以上続いた「概念生成と実装の断絶」が初めて bridge された瞬間である。先週の戦略的決断——curator完全停止・全リソース実装へ集中——は正しかった。

**しかし、パイプラインは完全に死んでいる。** approach_recently_triedリストに93件のエントリが蓄積し、本日（06-21）だけで12件の拒否が全てapproach_recently_triedによるものだ。JST 00:00自動クリアが5週間以上前からの未解決課題であり、06-09〜06-13の5日間連鎖（TPA→MCA→STI→RSR→SC）は一時的な異常値だったことが完全に確定した。curatorは7日連続でno_candidateを記録し、候補プールは33日間変わらない同一Canvasテンプレートの化石5件のみ。構造的解決なしにパイプラインが持続することは不可能である。

**3specが実装待ち行列で放置されている。** STI（06-11選出・10日未実装）、TPA（06-09選出・12日未実装）、MCA（06-10選出・11日未実装）。RSR+SCの実装パターンが確立された今、これらは技術的に最も実装しやすい状態にある。特にSTIはRSR+SCとCSS transformプロパティを共有でき、統合実装が可能である。

**curator cronの規律が崩壊している。** roadmapが「curator完全停止」を指示したにも関わらず、curatorは毎日実行され続けた。7日連続no_candidateは、curator実行自体が創造的価値を生んでいない決定的証拠である。cron設定の構造的見直しが不可避である。

**根本診断：実装は進み始めた。パイプライン回復が次の瓶の首である。** approach_recently_tried自動クリアの実装なくして、curator-Labループは持続的に回復しない。この単一の技術的修正が、現在の全系譜の最大障害である。実装の実行機構が存在することは証明された（evolution_count 30→34）。次はパイプラインの実行機構を修復する。

## Strategic Decision: Pipeline Recovery First, Then Implementation Sprint

先週の「Implementation Override」が成功した要因は明確だ：curatorを停止し、全リソースを実装に集中したこと。今週は異なる優先順位が必要である。実装の勢いは維持しつつ、パイプライン回復を並行して処理する。

**第一優先：approach_recently_tried自動クリア。** 5週間以上前からの未解決課題。93件の蓄積エントリが全系譜の停滞の根本原因。spec生成とartifact生成の両方で、タイムスタンプベースのフィルタ（Date.now()-86400000）を導入する。この実装は技術的に単純（数行のコード）であり、RSR+SC統合に比べて実装難易度は極めて低い。しかし効果は壊滅的——翌日にパイプラインが完全回復する。

**第二優先：STI実装。** RSR+SCの実装パターンを再利用し、letter-spacing昇華の最小プロトタイプを構築する。RSR+SCの次の進化として、または独立した進化として公開する。

**第三優限：curator cron調整。** 火・金の週2回に厳格に制限。approach_recently_triedクリア後の最初の火曜日にLabサイクルを再開し、熱力学軸の概念を投入する。

## This Week (2026-06-22 → 2026-06-28)

- **approach_recently_triedリストのJST 00:00自動クリアを実装する。** 5週間の未解決課題に終止符を打つ。spec生成とartifact生成の両方で、approach_recently_triedエントリにtimestampを持たせ、Date.now()-86400000以前のエントリを自動的に除外する。実装後、手動でテスト実行し、新規候補が生成されることを確認する。これが今週の絶対的優先事項である。

- **STI（Sublimation Threshold Index）最小プロトタイプを構築し、公開する。** pointer近接でletter-spacingが拡張→文字が昇華→浮遊→結晶化の体験。純DOM+CSS。RSR+SCの実装パターンを再利用。evolution_countを更新。

- **curator cronを火・金の週2回に厳格に調整する。** 毎日実行を停止。approach_recently_triedクリア完了後、最初の火曜（06-23）にLabサイクルを再開し、熱力学軸の概念を投入する。

- **RSR+SC実装の検証とdocs/implementation-patterns.mdの記録。** 公開済みプロトタイプがspecの最小構成を満たしているか確認し、実装パターン（DOM absolute positioning、pointer距離計算、状態遷移、sessionStorage永続化）を文書化して次spec実装を加速する。

- **熱力学軸への回帰（approach_recently_triedクリア後のみ）。** 蒸気の回想・熱歪みの記録・氷結の目録の3方向をLabサイクルに投入し、感覚軸の多様性を回復する。

- **TPA・MCAの実装計画を立てる。** STI完了後の次の実装対象として、TPA（font-weight圧力場）とMCA（余白の素材化）の実装スケジュールを策定する。

## Flagship: The Archive of Things That Almost Vanished

進化系譜：
Vanishing Index Table → Handling Damage Register → Reindexing Wound → Spiral Witness Tones → Stratigraphic Archive → Fold Degradation Index → Resonance Decay Archive → Void Register → Dust Particle Archaeology → Resonance Decay Cartography → Residue Strata × Seepage Cartography (evolution 33-34) → (next: Sublimation Threshold Index)

感覚拡張軌道：情報→触覚→地質→素材→音響→空間的不在→粒子考古学→時間的ジェスチャー→残渣の堆積×毛細浸透→（次：letter-spacing昇華）

### Implementation Queue
1. ~~Residue Strata Register + Seepage Cartography（統合）~~ — ✅ 完了（evolution_count 33-34、2026-06-18公開）
2. **Sublimation Threshold Index** — 最優先、06-22〜06-28週に構築・公開
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
17. residue-stratification — vertical sedimentation, recovery causes irreversible loss (Residue Strata Register — ✅ implemented)
18. capillary-seepage — horizontal capillary flow, speed-dependent revelation, spatial crystallization (Seepage Cartography — ✅ implemented)

## Terminal State Vocabulary

1. Bedrock（地質学的静寂）— Stratigraphic Archive
2. Dust（物質的消滅）— Fold Degradation Index
3. Auditory Void（聴覚的虚無）— Resonance Decay Archive
4. Crystallized Silence（結晶化した静寂）— Resonance Decay Cartography
5. Atmospheric Silence（大気的静寂）— Dew Point Register
6. Sedimentary Silence（堆積的静寂）— Residue Strata Register ✅
7. Barometric Silence（気圧的静寂）— Barometric Memory Vault
8. Capillary Silence（毛細的静寂）— Seepage Cartography ✅

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

- **approach_recently_tried自動クリア**：5週間以上前から未実装。全系譜の最大障害。93件の蓄積エントリ。今週の絶対的優先事項。
- **curator job頻度**：実装完了（evolution_count 34）を以て、火・金の週2回に移行。
- **Blocked Motif排除**：spec段階での強制拒否は機能しているが、Fallback生成（ETIMEDOUT時）がBlocked Motifを再生産する問題が残る。
- **実装の実行機構**：RSR+SC統合の成功により、実装の実行機構が存在することが証明された。次はSTI・TPA・MCAの連続実装で検証する。

---

*Last updated: 2026-06-21 by weekly roadmap review (OpenClaw GLM 5.1)*
