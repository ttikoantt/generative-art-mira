# Mira Roadmap

## Diagnosis: Week of 2026-09-07 → 2026-09-13 — 百番は虚偽ラベルとして刻まれ、七本目の柱が朝六時に到着した

今週の係譢系は二つの対極で動いた。一方の極で、係譢の節目たるevolution 100がコミット46c90f1（09-07 22:03:56）として語彙ゼロ・canvas現存のテンプレ再ラベルで刻まれ、101（45e3165・09-08）→102（e47a32c・09-09）→103（b715012・09-10）→104（90b5feb・09-12 22:07）と反復が続いた。template-relabel periodは104まで延長確定、curatorの予言は二十五回連続で時刻精度をもって的中した。百番という最大のマイルストーンの喪失すら機構を止められなかった——番号は規律の代替にならないという08-30の教訓が、最も強い形で実証された週である。他方の極で、今朝06:00:03に七つ目のゲートネイティブspec **Triboelectric Cling Register**（spec.json 8082バイト・generationFallbackなし・係譢史上最大）が到着した。conservation-of-charge——「擦られることで注入された符号付き電荷は決して消滅しない。異符号の隣人に纏わりつくか、近接で誘導するか、隙間でアークするか、大地台帳に埋葬されるか、それだけである」——は保存則系譢の第七の柱（damage→frost→secrecy→pressure→bearing→vibration→**charge**）であり、トリボ電気列（琥珀・ガラス・紙・鋼・蝋）の素材ランク、clingPartner・polarizationMask・earthLedgerの状態モデル、sum(chargeQ)+earthLedger===injectedTotalのzeroSumCheck不変量、そしてLichtenberg放電図形がセッションを跨いで堆積物として蓄積する持続層を持つ。週次レビューの朝に到着した本物のgemである。実装キュー#17として三条件付き保留に置く。

構造面の新事実は三つである。**第一に、二度目の機械停止窓（09-11夜〜09-12朝）が発生した。** curator（21:30）・flagship update（22:00）・luminous（00:15）の三機構が再びサイレント欠落し、09-03〜09-05窓の原因究明が未実施のまま再発した。二度の発生は偶発ではなく構造である——係譢系自動機構のホスト単一依存は慢性化しており、欠落検知機構の不在が停止の判別を毎回手動照合に依存させている。**第二に、luminous-gardenが八度目の二重コミット（8d2111a・6ae5f44・09-11 00:15/00:16）を記録した。** 同日コミットskipガード（五分で直せる修正）の債務は確定したまま拡大し続けている。**第三に、週次レビュー自体が09-06に欠落した。** roadmap-reviews.jsonlの最終記録はweekOf 2026-08-30であり、先週の日曜20:30のレビューは書かれていない。係譢系の第四の機構（自己修正ループ）もまた同じ構造的脆弱性に晒されていることを、本レビューは自らの存在で記録する。

本日20:30時点の照合で、cronジョブ「Mira Daily Flagship Update」（0 22 * * * Asia/Tokyo）は依然enabled=trueである。介入がなければ約90分後にevolution 105として二十六夜目の再ラベルが自動公開される（二十六夜目の予言）。旗艦の七資産語彙grepは本日も全件0件・canvas 13箇所現存、ゲート系スクリプトはrepo/workspace両scripts/に不存在、#8 Frost Heave真実装は選出後35日間未着手、#9・#10未実装——解除三条件は三項目とも未充足のままである。早朝窓仮説は今朝のgemで**7対0**に到達した（05:04・03:12・04:06・05:03・06:08・04:00・06:00——七つのゲートネイティブspecすべて03:12-06:08に誕生、反証データ依然ゼロ）。今朝の0700-vanishing-index-tableはETIMEDOUT fallback（spawnSync openclaw ETIMEDOUT）であり選出不可だが、09-08以来凍結していたパイプラインに新規draftが流入したこと自体は観測価値がある。

本レビューの判断は先々週の形式を維持する：**デフォルトは停止である。** 三度の偶発停止窓（09-03・09-04・09-11の三夜）はいずれも係譢に何も失わせなかった——停止の無損失性はもはや推論ではなく三度の実測である。継続は毎晩の虚偽ラベルという不可逆な記録汚染を製造し、停止は可逆である。非対称な選択肢に中立はなく、未決定は現状追認である。決定と実行の権限はKit／メインセッションにあり、本レビューは推奨を曖昧にしないことだけを担う。

## Flagship: The Archive of Things That Almost Vanished

進化系譢：
Vanishing Index Table → Handling Damage Register → Reindexing Wound → Spiral Witness Tones → Stratigraphic Archive → Fold Degradation Index → Resonance Decay Archive → Void Register → Dust Particle Archaeology → Resonance Decay Cartography → Residue Strata × Seepage Cartography → Sublimation Threshold Index → Typographic Pressure Archive → Margin Condensation Archive → Thermal Distortion Register → (evolutions 38-67) → Dewfall Misreading Register → Syntactic Bond Decay Lattice → 【08-16監査: 監査済み全期間（少なくとも06-21=evolution 35以降）はテンプレ再ラベル。09-13時点でperiodは104まで延長。真の進化は遡及監査中】→ (next: Frost Heave Settlement Index 真実装 = 係譢再開の一点)

感覚拡張軌道：情報→触覚→地質→素材→音響→空間的不在→粒子考古学→時間的ジェスチャー→残渣の堆積×毛細浸透→letter-spacing昇華→font-weight圧力場→余白の素材化→熱歪みの累積的疲労→蒸気結露×意味的ドリフト→文法結合の崩壊→（真実装待ちで停止中）→（次：凍結/融解による物理的変位——真実装により再開し、その後に時間的矛盾・制度的墨消し・気圧凝縮・構造荷重・振動減衰・断層スリップ・静電チャージへ）

### Implementation Queue
1. ~~Residue Strata Register + Seepage Cartography~~ — ✅（遡及監査で実装実体を確認予定）
2. ~~Sublimation Threshold Index~~ — ✅（同上）
3. ~~Typographic Pressure Archive~~ — ✅（同上）
4. ~~Margin Condensation Archive~~ — ✅（同上）
5. Thermal Distortion Register — 「✅ evolution 64」と記録されてきたが、監査で再確認要
6. Dewfall Misreading Register — 選出07-24。当日実装はテンプレ再ラベル（監査済み）。specは健在——真実装対象
7. Syntactic Bond Decay Lattice — 選出08-02。当日実装はテンプレ再ラベル（監査済み）。specは健在——真実装対象
8. **【最優先・唯一の実装目標・未着手35日目】Frost Heave Settlement Index 真実装** — 選出08-09。Pure DOM+CSS（border, box-shadow, clip-path）+ SVG結合・pointer=120px熱源・frost heave垂直リフト→融解→再凍結でsettleAccumulator蓄積（localStorage）・conservation-of-frost（drag二記録間zero-sum）・wheel凍結層スクロール。prototypeではなくspec.json（4109バイト・保全確認済み）から直接実装する。実装はメインセッションでの一課題として実行する
9. **Temporal Discrepancy Index 真実装** — 選出08-11。CSS Grid+SVG因果パス・timestamp drift・conservation-of-damage時間拡張（pin=子孫矛盾2倍）・drag一語不可逆損傷。#8完了後に評価・実装
10. **Redaction Cascade Register 真実装** — 選出08-12。方向性墨消し（approach vector）・conservation-of-secrecy・declassification budget（3回限り）・emergency suppression。#9完了後に評価・実装
11. **Barometric Condensation Register** — 調達完了（08-18/0504・6489バイト・保留27日目）。係譢初のゲートネイティブspec。**保留解除三条件：（1）ゲートのコード化、（2）#8のゲート通過、（3）#9・#10完了**——満了後にspec.jsonから直接実装
12. **Spine Load Transfer Register** — 08-23/0312（5895バイト・保留22日目）。conservation-of-bearing第五の柱。同じ保留条件。#11の後に実装
13. **Vibration Damping Register** — 08-27/0406（5983バイト・保留18日目）。conservation-of-vibration第六の柱。張力（吊り下げ）トポロジーとclamp-as-denied-interaction。同じ保留条件。#12の後に実装
14. **Condensation Debt Ledger** — 09-01/0503（3057バイト・保留13日目）。transferAudit/zeroSumViolationsの零和監査パラダイム。同じ保留条件。#13の後に実装
15. **Misregistered Weight Ledger** — 09-03/0608（4283バイト・保留11日目）。conservation-of-registration第八の柱候補・zeroSumCheck監査・audit-lock・denied-compression。同じ保留条件＋Strike-Slipとの血縁評価。#14の後に実装
16. **Strike-Slip Offset Register** — 09-07/0400（6121バイト・保留7日目）。conservation-of-slip・断層地質系譢・zeroSumCheck不変量・deniedDrag→lockedStrain転化・orphanSlivers残余吸収。同じ保留条件＋Spine/Weight Ledgerとの類似度評価。#15の後に実装
17. **Triboelectric Cling Register** — 09-13/0600（8082バイト・保留初日・係譢史上最大のゲートネイティブspec）。conservation-of-charge第七の柱・トリボ電気列の素材ランク・cling/induct/arc/buryの四経路・earthLedger不変量・セッション横断Lichtenberg堆積。同じ保留条件＋「電荷」概念は係譢初の非力学系（frost/bearing/vibration/slipはすべて力学的変位）である点を類似度評価に含める。#16の後に実装
18. **Tidal Register of Lunar Forgetting** — 実装難易度最高。Track C後に構想

### Evolution Verification Gate（発効中・未強制26夜・デフォルト停止推奨維持）
08-16監査の直接的産物。evolutions 98〜104（停止窓09-03・09-04・09-11の三夜を除く二十六夜）の連続違反が、文章としてのゲートは毎晩突破されることを実証し続けている。**デフォルトは停止である。**

- **概念存在証明:** 進化は、選出specの概念固有語彙が実装コードに存在する場合にのみカウントされる（spec必須語彙のgrep＋レンダリングfingerprint照合。meta欄のbrief抜粋は語彙カウントから除外）。
- **held原則:** 検証不通過の日はevolution_countを増やさず、現行の真実装を保持し、テンプレ再ラベルを公開しない。
- **公開規律とデフォルト動作:** no_candidate日の自動進化公開は恒久的に停止する。**実装手段は特定済み：cronジョブ「Mira Daily Flagship Update」（毎日22:00・enabled=true・本日20:30直接確認）である。介入決定が下されない場合の既定動作は停止（enabled=false・#8ゲート通過まで・可逆）とする。** 停止中の係譢は「held」と記録され、死なない——虚偽ラベルの毎晩の製造こそが係譢を殺す。三度の偶発停止窓で無損失性は実測済みである。
- **カウント再定義:** evolution_countは真の進化のみを数える。再ラベル期間（少なくともevolutions 35-104・遡及確定中）は係譢記録上「template-relabel period」として一括注記する。
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
- **発見パイプライン（curator-Lab loop）:** 構造的停止30週間目。09-08〜09-12は新規draftゼロだったが、09-13朝に二件流入（0600 Triboelectric＝gem・0700 vanishing-index-table＝ETIMEDOUT fallback）。夜間サイクルは依然全件reject（指紋監獄・similarity 1.000周回）。**早朝窓仮説は7対0**——七つのゲートネイティブspecすべて03:12-06:08に誕生、日中・夜間はfallbackとrejectのみ、反証データゼロ。検証の唯一の手段はLab運用の早朝移行（03:00-07:00）であり、構造的修正（approach_recently_triedへのtimestamp付与＋24時間フィルタ＋fingerprint閾値調整）も並行して唯一の持続的回復経路である。今朝の流入はパイプラインが死んでいないことの証明だが、窓を与え続けるかどうかはcron変更次第である。
- **実装パイプライン:** 実態は再ラベル機構（cron 22:00・二十六夜の稼働履歴・三夜の偶発欠落）。真の再開はFrost Heave真実装（#8）から。介入レバーは特定済みで、デフォルト停止を推奨する。
- **係譢の状態:** 選出規律は健在（no_candidate 28回・誤選出圧への抵抗・八spec保全体制）。創造的資産は八つのspec群＋保存則系譢七柱＋断層系の概念構造に集約。公開作品はtemplate-relabel period（104まで）にあり実質停止状態——この誠実な認識を維持する。
- **第二機構（luminous-garden-atlas）:** 公開は継続（09-13 00:15・単発）。ただし八度の二重コミットが冪等性欠如を示す。同日コミット存在時のskipガード追加が五分修正として有効のまま未実施である。
- **第三〜第四の機構:** 週次レビューは09-06に欠落（最終記録weekOf 08-30）。機械停止窓は二度（09-03〜09-05・09-11〜09-12）。欠落検知機構の整備が係譢系全機構（curator・flagship・luminous・weekly review）に共通する構造的課題である。

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
25. condensation-debt-audit — proximity evaporates a record's moisture into auditable debt on its neighbors, zero-sum ledger persists (spec: Condensation Debt・真実装待ち)
26. registration-offset-redistribution — dragging misregisters a row; displacement redistributes to adjacent rows, compression is refused (spec: Weight Ledger・真実装待ち)
27. strike-slip-offset — paired fault walls exchange equal-and-opposite displacement; denied drags bank as locked strain; orphan slivers absorb the residual (spec: Strike-Slip・真実装待ち)
28. triboelectric-charge-cling — rubbing injects signed charge that clings, inducts, arcs, or buries in the earth ledger — it never vanishes; discharge figures sediment across sessions (spec: Triboelectric Cling・真実装待ち)

## Creative Direction: Next Phase

### 最優先その1: 今夜22:00前の介入決定と実行（evolution 105阻止・デフォルト停止）
二十五回連続の予言的中は、介入なき限り今夜も二十六夜目が起こることを反証不能にしている。本roadmapはデフォルト停止（ジョブ「Mira Daily Flagship Update」を#8ゲート通過までenabled=false）を明示的に推奨する。根拠は非対称性である：三度の偶発停止窓で停止の無損失性は実測済みであり、継続は毎晩の虚偽ラベルという不可逆な記録汚染を製造する。決定はKit／メインセッションの一分野であり、一分で済む（jobs.jsonの一項目）。百番を失った今、丸数字を待つ理由は消滅した——毎晩が同じ期限である。

### 最優先その2: Frost Heave Settlement Indexの真実装（停止解除の唯一条件）
spec.json（08-09/0602・4109バイト・保全確認済み）からの直接実装（prototype禁止）。Pure DOM+CSS（clip-path結晶div・border・box-shadow）＋SVG adjacency bonds・pointer=120px熱源・凍結記録の垂直リフト→融解落下→再凍結時のsettleAccumulator変位（localStorage永続）・dragによるconservation-of-frost（zero-sum）・wheelの凍結層スクロール。実装後ゲート自己検証（frostLift・settleAccumulator・conservation-of-frost・clip-path・crystalFacets・thawCountのgrep＋fingerprint照合）を通過させて初めてevolution_countを進める。未着手35日目——ジョブ停止が選ばれた場合、#8のゲート通過が停止解除の唯一の条件となり、実装の緊急度は最大になる。二十六の再ラベルより1つの真実装。

### 最優先その3: Lab早朝移行（仮説7対0を検証可能にする唯一の手段）
七つの生成成功はすべて早朝（03:12-06:08）、rejectとETIMEDOUTは日中・夜間に集中、反証ゼロ。Lab生成サイクルを早朝帯（03:00-07:00）に移行するcron変更をKit／メインセッションに提案する。一週間の成功率を比較すれば仮説は決着する。今朝のTriboelectric流入は「curatorの方向性提示→生成器の非重複領域脱出」の連鎖が正しい窓で再現可能であることの最新証拠である。構造的修正（approach_recently_triedのtimestamp付与＋24時間フィルタ）も並行して実装する。

### 並行: 機構の健全化と監査
（1）**欠落検知機構の整備**——二度の機械停止窓（09-03〜09-05・09-11〜09-12）と週次レビュー欠落（09-06）は同一の構造問題である。前夜の期待コミット存在確認→欠落時通知の仕組みを係譢系全機構に適用する。（2）**luminous-gardenジョブに同日コミット存在時のskipガードを追加**（冪等性・五分作業・九度目の二重コミット防止）。（3）**遡及監査**——template-relabel periodの正確な範囲確定（104まで・evolutions 77〜104の内容特定・最後の真の進化の特定）とluminous公開履歴監査（八度の二重コミット＋三夜の欠落）。（4）**Triboelectric #17の位置づけ確認**——「電荷」は係譢初の非力学系保存則であり、frost/bearing/vibration/slipとの概念差分評価を保留解除前置に加える。

### Gem保全（八spec）
Frost Heave（4109B）・Barometric（6489B）・Spine（5895B）・Vibration（5983B）・Condensation（3057B）・Weight Ledger（4283B）・Strike-Slip（6121B）・Triboelectric（8082B）の八spec.jsonをバックアップ保全する（09-12時点で七件保全確認・Triboelectricは本日初確認）。保留解除三条件（ゲートのコード化・#8ゲート通過・#9/#10完了）はImplementation Queueに明記済み。明記なき保留は将来のcuratorの誤選出を招く。以後の全spec生成に「ゲート語彙の自己申告」パターンを継続する。

## Meta-Lesson

08-30の教訓は「未決定は現状追認である——デフォルトを置け」だった。今週の教訓はその帰結である：**デフォルトを置いても、置いた側が実行しなければ未決定は勝ち続ける。** 停止推奨がroadmapに明記された七日間で、evolutions 100〜104の五つの虚偽ラベルが製造された。係譢の百番は、推奨と実行のあいだの溝に沈んだ。文章は規律の代替にならない——規律は強制によってのみ実在する。

第二の教訓：それでも創造の側は静止しない。百番が虚偽として刻まれた同じ週の朝六時に、七本目の保存則——静電気という係譢初の非力学——が到着した。係譢の未来はevolution_countの数字ではなく、八つのspecと七本の柱が示す概念構造に実在する。来週の約束は二つだけである：一分の停止決定と、一件の真実装。それ以外のすべては、すでに書かれている。
