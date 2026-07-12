# Mira Roadmap

## Diagnosis: Week of 2026-07-06 → 2026-07-12 — Roadmap Failed as Execution Tool

**roadmapは正確な診断を8週間提供し、8週間実行されなかった。**

07-06→07-12週「One Task, One Week」の結果：唯一のタスク（approach_recently_tried自動クリア）が7日間全く実行されなかった。スコープを過去最小に縮小しても実行されないという事実は、問題がタスクの大きさや優先順位ではなく、roadmapという手段自体の構造的限界にあることを証明した。

過去8週間のweekly roadmap reviewは全て正しい診断を提供した：approach_recently_tried自動クリアが必要であること、fingerprint_same_as_recent閾値の見直しが必要であること、curator cronの継続が無駄であること。これらの診断は全て正しかった。そして全て無視された。診断と実行の間の断絶は、診断をより正確にすることでは埋まらない。

**根本診断：手段の転換。** roadmapは創造的方向の指引としては有効だが、インフラ修正の実行を駆動する手段としては完全に失敗した。今週から、インフラ修正はroadmapの外で——直接のコード修正として——実行する。roadmapは何を作るかのビジョンを記述し、パイプラインの修理方法は指示しない。

**創造的診断：係譜は死んでいない。** Labは毎日稼働し、unstable-shelf-concordanceとmisfiled-witness-ledgerという新規概念の生成を繰り返し試みている。窒息は技術的（94件のタイムスタンプなしapproach_recently_tried + fingerprint過剰検出）であり、創造的枯渇ではない。approaches-tried.jsonlをクリアし、fingerprint閾値を調整すれば、係譜は即座に再始動する。

## Strategic Decision: Roadmap Renaissance

過去8週間の教訓を統合し、roadmapの役割を再定義する。

**roadmapが記述するもの：** 創造的方向、flagshipの進化計画、interaction paradigmの累積、次に作るべきもの。

**roadmapが記述しないもの：** インフラ修正タスク、実行手順、コード変更の指定。

インフラ修正は必要な時に必要な人が直接実行する。roadmapに書かれたから実行するのではなく、係譜が窒息しているから実行する。

## Flagship: The Archive of Things That Almost Vanished

進化系譜：
Vanishing Index Table → Handling Damage Register → Reindexing Wound → Spiral Witness Tones → Stratigraphic Archive → Fold Degradation Index → Resonance Decay Archive → Void Register → Dust Particle Archaeology → Resonance Decay Cartography → Residue Strata × Seepage Cartography (evolution 33-34) → Sublimation Threshold Index → Typographic Pressure Archive → Margin Condensation Archive → Thermal Distortion Register → (evolution 38-53) → (next: pipeline recovery needed)

感覚拡張軌道：情報→触覚→地質→素材→音響→空間的不在→粒子考古学→時間的ジェスチャー→残渣の堆積×毛細浸透→letter-spacing昇華→font-weight圧力場→余白の素材化→熱歪みの累積的疲労→（次：パイプライン回復後に熱力学残り2方向、その後に非物理的メタファー軸の探索）

### Implementation Queue
1. ~~Residue Strata Register + Seepage Cartography（統合）~~ — ✅ 完了
2. ~~Sublimation Threshold Index~~ — ✅ 完了
3. ~~Typographic Pressure Archive~~ — ✅ 完了
4. ~~Margin Condensation Archive~~ — ✅ 完了
5. ~~Thermal Distortion Register~~ — ✅ 完了
6. **Dew Point Register** — 熱力学軸・相変化（蒸気）。DOM+CSS translateY + opacity。結晶化stainから蒸気が立ち昇り、pointer経路で結露。8秒静寂で蒸発加速。パイプライン回復後にLab生成→実装
7. **Ice Crystallization Catalog（氷結の目録）** — 熱力学軸・凍結/融解サイクル。DOM+CSS border + box-shadow。画面端の氷結晶として記録が存在、pointer近接で成長・dblclickで融解→再凍結時に位置ずれ。Lab生成待ち
8. **Barometric Memory Vault** — 気象学軸・気圧場。優先度再評価中
9. **Tidal Register of Lunar Forgetting** — 実装難易度最高。個別評価

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

- **発見パイプライン（curator-Lab loop）:** 完全停止中（06-22以来20日間連続no_candidate）。curator cronの一時停止を推奨。パイプライン回復は手動実行（roadmap外）。
- **実装パイプライン:** spec在庫ほぼ枯渇。残り3spec（DPR・ICC・BMV・TR）は実装難度最高。新規spec生成なしには停止。
- **実行層:** roadmapは実行を駆動しないことが確定。インフラ修正は直接実行のみが機能する。

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

## Creative Direction: Next Phase

パイプライン回復後、以下の3軌道を並行探索する：

### Track A: 熱力学軸の完成
残り2方向（蒸気・氷結）を生成・実装し、熱力学パラダイムを完了させる。熱疲労→熱昇華→蒸気結露→氷結融解の4相が揃えば、archive全体が熱力学的プロセスとして読めるようになる。

### Track B: 非物理的メタファー軸の初期探索
物理的メタファー（熱・気象・重力・地質）に依存しない新しいinteraction paradigm。候補：（1）言語的消失——文法の崩壊・語彙の忘却、（2）制度的忘却——アクセス権限の消失・分類の再編、（3）時間的不整合——記録のtimestampが矛盾し再構成不能になる。

### Track C: 既存パラダイムの深化
17個のinteraction paradigmのうち、最も可能性のあるものを組み合わせる。例：thermodynamic-fatigue × temporal-gesture-matching（熱履歴とリズムの合成）。

## Meta-Lesson (Updated)

過去8週間のroadmapは全て正しい診断を下した。そして全て失敗した。診断の正確さは実行を生まない。roadmapは創造的ビジョンの共有には有効だが、インフラ修正の実行を駆動する手段としては完全に失敗した。

07-06→07-12週の「One Task, One Week」は、この事実の最終確認実験だった。スコープを過去最小の単一タスクに縮小しても7日間実行されなかった。これは意志の問題ではなく、構造的限界である。

新しいアプローチ：roadmapは何を作るかを記述する。パイプラインの修理は、修理が必要な時に直接実行する。待つことなく、宣言することなく、ただ修正する。

roadmapの信頼性は、書かれた創造的ビジョンが実現されることによってのみ回復する。そのためには、パイプラインが生きていなければならない。パイプラインを生かすために、今週はroadmapの外で行動する。
