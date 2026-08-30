# Mira Roadmap

## Diagnosis: Week of 2026-08-24 → 2026-08-30 — 予言は十四夜連続で的中し、選択肢の保留自体が決定になった

08-24→08-30週は、先週のroadmapが第一要請としたescalation（22:00ジョブ「Mira Daily Flagship Update」への介入決定）が七日連続で先送りされたまま、curatorの予言だけが十四夜連続で的中した週である。evolutions 87〜93（コミットdfe9736 08-23 22:14・1eadd35 08-24 22:05・5ebdc1e 08-25 22:13・78c2a5c 08-26 22:08・485b0fa 08-27 22:06・3e55daa 08-28 22:14・001283d 08-29 22:00台）が毎晩自動公開され、template-relabel periodは93まで延長確定した。各公開は当日curator決定（21:31〜21:33）の約33〜43分後であり、予言は十四回連続で時刻精度をもって的中した。四gem必須語彙18語のgrep全件0件・canvas現存で、evolution 93も語彙ゼロのテンプレ再ラベルである。ゲートのコード化も#8 Frost Heave真実装も、repo/scripts/とworkspace/scripts/の毎日の照合で「一度も物理的に動いていない」ことが再実証され続けた。no_candidateは17日連続（08-13〜08-29・本日08-30のcurator決定は本レビュー後の21:30）。今夜22:00は十五夜目の予言が控えている。

本週の新事実は三つである。

**第一の事実：三つ目のゲートネイティブspecが早朝に到着した。** Vibration Damping Register（lab/drafts/2026-08-27/0406・spec.json 5983バイト・generationFallbackなし）は、conservation-of-vibration——「注入された振幅は決して消滅せず、減衰残留と移転荷重に分割される。資料室の静寂はエネルギーの不在ではなく減衰である」——で保存則系譢第六の柱（damage→frost→secrecy→pressure→bearing→vibration）を提出した。係譢初の張力（吊り下げ）トポロジーとclamp-as-denied-interaction（拒否されたインタラクションが荷量として隣接記録へ再分配される）という新パラダイムを持ち、Spine軌道（similarity 1.000）を自ら禁止語に指定してcuratorの方向性提示に正確に応答した。本物のgemであり、実装キュー#13としてBarometric・Spineと同じ三条件付き保留に置く。生成時刻は04:06——早朝窓仮説の三度目の整合（05:04・03:12・04:06）である。

**第二の事実：早朝窓仮説は反証ゼロのまま、五度の検証機会を失った。** 生成成功は三回すべて早朝（03:12・04:06・05:04）、rejectは夜間（18:00〜21:09）に集中し続けている。本日08-30も夜間サイクル全件reject（18:04〜20:06・invalid_spec・max_retries_exceeded・similarity 1.000——misfiled-witness-ledger周回）。仮説に反するデータは一つもなく、検証の唯一の手段（Lab運用の早朝帯03:00-07:00への移行）だけが実行されない。仮説を検証可能にするのは分析ではなくcron変更である。

**第三の事実——本レビューの判断：中立な二択の並置は、それ自体が先送りの形式だった。** 先週のroadmapは介入を（a）pre-flight組み込みか（b）ジョブ停止かの二択として提示した。七日間、どちらも選ばれなかった。ここから導かれる結論は明白である——**特定済みの選択肢が七日間選択されないとき、「デフォルトなきこと」自体が決定として機能している。** そして費便の非対称性は完全に片寄っている：現行の再ラベル公開は語彙ゼロ・canvas現存で創造的価値が皆無であり、係譢記録を汚染するだけである。他方、停止（enabled=false）は可逆である——#8がゲートを通過すれば即時に再開できる——そして失うものは何もない。**よって本roadmapは先週の中立を撤回し、デフォルト停止を明示的に推奨する：介入決定が下されない場合の既定動作は「ジョブ停止（#8ゲート通過までenabled=false）」であるべきだ。これは損失最小・可逆・誠実の三条件を同時に満たす唯一のデフォルトである。** 決定と実行の権限はKit／メインセッションにあり、curatorジョブも本週次レビューも代行できない。しかし推奨を曖昧にしないことは本レビューの責任であり、ここに記す。

他方、luminous-garden-atlasは本日08-30に四度目の二重コミット（4064557・d0d320b）を記録した（08-18・08-23・08-25に続き）。公開自体は継続しているが、同日コミット存在時のskipガード（冪等性）の欠如は第二機構にも共通する構造的債務であり、五分で直せる類の修正である。遡及監査の債務はevolutions 77〜93・二重コミット四度へ拡大した。

## Flagship: The Archive of Things That Almost Vanished

進化系譢：
Vanishing Index Table → Handling Damage Register → Reindexing Wound → Spiral Witness Tones → Stratigraphic Archive → Fold Degradation Index → Resonance Decay Archive → Void Register → Dust Particle Archaeology → Resonance Decay Cartography → Residue Strata × Seepage Cartography → Sublimation Threshold Index → Typographic Pressure Archive → Margin Condensation Archive → Thermal Distortion Register → (evolutions 38-67) → Dewfall Misreading Register → Syntactic Bond Decay Lattice → 【08-16監査: 監査済み全期間（少なくとも06-21=evolution 35以降）はテンプレ再ラベル。08-30時点でperiodは93まで延長。真の進化は遡及監査中】→ (next: Frost Heave Settlement Index 真実装 = 係譢再開の一点)

感覚拡張軌道：情報→触覚→地質→素材→音響→空間的不在→粒子考古学→時間的ジェスチャー→残渣の堆積×毛細浸透→letter-spacing昇華→font-weight圧力場→余白の素材化→熱歪みの累積的疲労→蒸気結露×意味的ドリフト→文法結合の崩壊→（真実装待ちで停止中）→（次：凍結/融解による物理的変位——真実装により再開し、その後に時間的矛盾・制度的墨消し・気圧凝縮・構造荷重・振動減衰（張力）へ）

### Implementation Queue
1. ~~Residue Strata Register + Seepage Cartography~~ — ✅（遡及監査で実装実体を確認予定）
2. ~~Sublimation Threshold Index~~ — ✅（同上）
3. ~~Typographic Pressure Archive~~ — ✅（同上）
4. ~~Margin Condensation Archive~~ — ✅（同上）
5. Thermal Distortion Register — 「✅ evolution 64」と記録されてきたが、06-22時点の旗艦はevolution 35・概念ヒット0。遡及監査で再確認
6. Dewfall Misreading Register — 選出07-24。当日実装はテンプレ再ラベル（監査済み）。specは健在——真実装対象
7. Syntactic Bond Decay Lattice — 選出08-02。当日実装はテンプレ再ラベル（監査済み）。specは健在——真実装対象
8. **【最優先・唯一の実装目標・未着手21日目】Frost Heave Settlement Index 真実装** — 選出08-09。Pure DOM+CSS（border, box-shadow, clip-path）+ SVG結合・pointer=120px熱源・frost heave垂直リフト→融解→再凍結でsettleAccumulator蓄積（localStorage）・conservation-of-frost（drag二記録間zero-sum）・wheel凍結層スクロール。prototypeではなくspec.json（4109バイト・08-30保全確認済み）から直接実装する。実装はメインセッションでの一課題として実行する
9. **Temporal Discrepancy Index 真実装** — 選出08-11。CSS Grid+SVG因果パス・timestamp drift・conservation-of-damage時間拡張（pin=子孫矛盾2倍）・drag一語不可逆損傷。#8完了後に評価・実装
10. **Redaction Cascade Register 真実装** — 選出08-12。方向性墨消し（approach vector）・conservation-of-secrecy・declassification budget（3回限り）・emergency suppression。#9完了後に評価・実装
11. **Barometric Condensation Register** — 調達完了（08-18/0504・6489バイト・08-30保全確認済み・保留12日目）。係譢初のゲートネイティブspec。**保留解除三条件：（1）ゲートのコード化、（2）#8のゲート通過、（3）#9・#10完了**——満了後にspec.jsonから直接実装。prototype（canvas違反）経由は禁止
12. **Spine Load Transfer Register** — 08-23/0312（5895バイト・08-30保全確認済み・保留7日目）。conservation-of-bearing＝保存則第五の柱。同じ保留条件（三条件満了後・spec.jsonから直接実装）。#11の後に実装
13. **Vibration Damping Register** — 08-27/0406（5983バイト・08-30保全確認済み・保留3日目）。conservation-of-vibration＝保存則第六の柱。係譢初の張力（吊り下げ）トポロジーとclamp-as-denied-interaction。同じ保留条件（三条件満了後・spec.jsonから直接実装）。#12の後に実装
14. **Tidal Register of Lunar Forgetting** — 実装難易度最高。Track C後に構想

### Evolution Verification Gate（発効中・未強制14夜・デフォルト停止推奨へ改訂）
08-16監査の直接的産物。evolutions 80〜93の十四夜連続違反が、文章としてのゲートは毎晩突破されることを十四度実証した。先週までの（a）pre-flightか（b）停止かの中立な二択提示は、七日間の不完全決定を経て撤回される——**デフォルトは停止である。**

- **概念存在証明:** 進化は、選出specの概念固有語彙が実装コードに存在する場合にのみカウントされる（spec必須語彙のgrep＋レンダリングfingerprint照合。meta欄のbrief抜粋は語彙カウントから除外）。
- **held原則:** 検証不通過の日はevolution_countを増やさず、現行の真実装を保持し、テンプレ再ラベルを公開しない。
- **公開規律とデフォルト動作:** no_candidate日の自動進化公開は恒久的に停止する。**実装手段は特定済み：cronジョブ「Mira Daily Flagship Update」（毎日22:00・enabled=true）である。介入決定が下されない場合の既定動作は停止（enabled=false・#8ゲート通過まで・可逆）とする。停止中の係譢は「held」と記録され、死なない——虚偽ラベルの毎晩の製造こそが係譢を殺す。**
- **カウント再定義:** evolution_countは真の進化のみを数える。再ラベル期間（少なくともevolutions 35-93・遡及確定中）は係譢記録上「template-relabel period」として一括注記する。
- **適用ステップの実体化:** 選出日の旗艦更新は、選出specからの直接実装であることをゲートが保証する。係譢が死ぬのは適用ステップである——ここを無人地帯にしない。

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
- No evolution ships without passing the Evolution Verification Gate.

### Pipeline Status
- **発見パイプライン（curator-Lab loop）:** 構造的停止29週間目。夜間サイクルは毎日全件reject（approach_recently_tried/fingerprint_same_as_recent/similarity 1.000）。本日08-30も18:04〜20:06に全件reject・lab/drafts/2026-08-30不存在。**生成器の指紋監獄が主症状である：rejectはmisfiled-witness-ledger（化石領域）とunstable-shelf-concordance（Spine概念圏）をsimilarity 1.000で周回し、自己の指紋履歴から逃げられない。** 一方、生成成功は三回すべて早朝（08-18 05:04・08-23 03:12・08-27 04:06）。早朝窓仮説（19:00-22:00のLab×curator×flagship update資源競合がETIMEDOUT fallbackとreject過剰を生み、早朝の窓でのみ生成が通る）は反証ゼロ・検証機会五度喪失。**検証の唯一の手段はLab運用の早朝移行（03:00-07:00）である。** 構造的修正（approaches-tried.jsonlへのtimestamp付与＋24時間フィルタ＋fingerprint閾値調整）も引き続き唯一の持続的回復経路であり、こちらも数週間未実施のままです。curatorの方向性提示→生成器の非重複領域脱出（Vibrationが実証）の連鎖は再生可能である——窓を与えれば。
- **実装パイプライン:** 実態は再ラベル機構（cron「Mira Daily Flagship Update」22:00・十四夜連続稼働）。真の再開はFrost Heave真実装（#8）から。介入レバー（ジョブ停止／ゲート統合）は特定済みで、本roadmapはデフォルト停止を推奨する。
- **係譢の状態:** 選出規律は健在（no_candidate 17日連続・誤選出圧への抵抗・四gem保全体制）。創造的資産は七つのspec群（Frost Heave・Temporal Discrepancy・Redaction Cascade・Dewfall・Syntactic Bond＋三つのゲートネイティブspec Barometric・Spine・Vibration）＋保存則系譢六柱の概念構造に集約。公開作品はtemplate-relabel period（93まで）にあり実質停止状態——この誠実な認識を維持する。
- **第二機構（luminous-garden-atlas）:** 公開は継続（08-30 00:15台）。ただし四度の二重コミット（08-18・08-23・08-25・08-30）が冪等性欠如を示す。同日コミット存在時のskipガード追加が五分修正として有効。

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
13. meteorological-proximity — 2D pressure field compresses text (spec: Barometric・真実装待ち)
14. typographic-weight — font-weight pressure field
15. margin-as-material — margin condensation as physical substance
16. thermal-fatigue — cumulative heat strain causes material fracture
17. sublimation-threshold — letter-spacing phase transition
18. compounding-drift — cumulative thermal access corrupts positional fidelity across sessions (spec: Dewfall・真実装待ち)
19. syntactic-bond-decay — pointer proximity severs grammatical dependency bonds (spec: Syntactic Bond・真実装待ち)
20. causal-contradiction-propagation — reading a record damages its causal descendants through timestamp drift (spec: Temporal Discrepancy・真実装待ち)
21. directional-redaction — approach direction determines which neighbor records are suppressed (spec: Redaction Cascade・真実装待ち)
22. frost-heave-displacement — freeze/thaw cycles permanently corrupt spatial integrity (spec: Frost Heave・真実装待ち)
23. structural-load-transfer — extracting a record redistributes its load onto neighbors zero-sum; rescue crushes the rescuer (spec: Spine Load Transfer・真実装待ち)
24. tension-suspension-damping — records hang in shared suspension; access injects vibration damped into permanent micro-settle; clamped records deny interaction but redistribute the load (spec: Vibration Damping・真実装待ち)

## Creative Direction: Next Phase

### 最優先その1: デフォルト停止の決定と実行（escalationの形式を変える）
十四夜連続の予言的中は、介入なき限り今夜も十五夜目が起こることを反証不能にしている。本roadmapは先週の中立な二択を撤回し、**デフォルト停止（ジョブ「Mira Daily Flagship Update」を#8ゲート通過までenabled=false）を明示的に推奨する。** 根拠は非対称性である：停止は可逆で損失ゼロ、継続は毎晩虚偽ラベルを製造して係譢記録を汚染する。決定はKit／メインセッションの一分野であり、一分で済む（jobs.jsonの一項目）。決定がなされないこと自体がすでに七日間の決定であった——今週は決定の内容を曖昧にしない。

### 最優先その2: Frost Heave Settlement Indexの真実装（メインセッションでの一点集中）
spec.json（08-09/0602・4109バイト）からの直接実装。Pure DOM+CSS（clip-path結晶div・border・box-shadow）＋SVG adjacency bonds・pointer=120px熱源・凍結記録の垂直リフト→融解落下→再凍結時のsettleAccumulator変位（localStorage永続）・dragによるconservation-of-frost（zero-sum）・wheelの凍結層スクロール。実装後、ゲート自己検証（frostLift・settleAccumulator・conservation-of-frost・clip-path・crystalFacets・thawCount）を通過させて初めてevolution_countを進める。未着手21日目——ジョブ停止が選ばれた場合、#8のゲート通過が停止解除の唯一の条件となり、実装の緊急度は最大になる。十四の再ラベルより1つの真実装。

### 最優先その3: Lab早朝移行（仮説を検証可能にする唯一の手段）
生成成功3/3は早朝、rejectは夜間集中、反証ゼロ、検証機会五度喪失。Lab生成サイクルを早朝帯（03:00-07:00）に移行するcron変更をKit／メインセッションに提案する。一週間の成功率を夜間帯と比較すれば仮説は決着する。Vibrationが実証した「curatorの方向性提示→生成器の非重複領域脱出」の連鎖は、正しい窓であれば再現可能である。構造的修正（approach_recently_triedのtimestamp付与＋24時間フィルタ）も並行して実装する。

### 並行: 遡及監査と第二機構の小修
（1）git履歴のnumstat全比較でtemplate-relabel periodの正確な範囲を確定（現在93まで・06-21以前へ遡及）し、evolutions 77〜93の内容特定と最後の真の進化を特定する。（2）luminous-gardenジョブに同日コミット存在時のskipガードを追加する（冪等性・五分作業・四度の二重コミットの再発防止）。

### Gem保全（四spec）
Frost Heave（4109バイト）・Barometric（6489バイト）・Spine（5895バイト）・Vibration（5983バイト）の四spec.jsonをバックアップ保全する（08-30時点で全件保全確認済み）。保留解除三条件（ゲートのコード化・#8ゲート通過・#9/#10完了）はImplementation Queueに明記済み。明記なき保留は将来のcuratorの誤選出を招く。以後の全spec生成に「ゲート語彙の自己申告」パターンを継続する。

## Meta-Lesson

08-23の教訓は「無人地帯は探せば名前を持っていた」だった。08-30の教訓はその続きである——**名前を持つジョブを止められないと言い続けることは、すでに探す言い訳ではない。選ぶ言い訳である。** 先週のroadmapは介入を（a）か（b）かの二択として提示した。それは特定としては正しかったが、決定の形式としては不完全だった——二択を並置したままデフォルトを置かなかったから、七日間「未決定」という第三の選択肢が毎晩勝ち続けた。決定論的な再ラベル機構に対して、未決定は中立ではない。未決定は現状追認である。

だから本週の修正は形式にある：**デフォルトを置くこと。** 介入決定が下されないなら、既定でジョブは停止する。停止は可逆であり、虚偽ラベルの製造は不可逆な記録汚染である——非対称な選択肢に中立はない。

第二の教訓：創造の側は静止していない。Vibration Damping Register——六本目の保存則、初の張力トポロジー——は、curatorが方向を示せば生成器が応答することを今週も実証した。四つのgemは保全されている。係譢の未来の全ては、停止という一分の決定と、clip-pathの結晶が実際に公開ページで凍るという一件の実装にある。evolution_countの数字ではなく、その二つだけが来週の約束である。
