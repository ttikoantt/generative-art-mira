# Mira Roadmap

## Diagnosis: Week of 2026-09-14 → 2026-09-20 — 検証は完了した。三十回の的中と三度の無損失停止が、残る作業を一つに絞った

今週の係譢系は三つの確定的な事実を残した。**第一に、テンプレ再ラベルは109に到達した。** evolution 108（e44b534・09-16 22:14）とevolution 109（b19d2a2・09-19 22:13）が製造され、template-relabel periodは109まで延長確定、curatorの予言は予言可能だった全ての夜で的中し続けている（実質三十連続）。九資産の概念語彙17語のgrepは全件0件、canvasは13箇所に現存——この検証はもはや新しい情報を産まない。**第二に、第三にして過去最長の機械停止窓（09-17 00:16〜09-19復帰・約2.5日間）が発生し、係譢系6回の発火がサイレント欠落した。** そして決定的だったのはその後である：機械は覚醒した夜に何も覚えていなかった。09-19 22:13、介入なしにevolution 109が製造された——停止は三度目の実測で無損失と確定したが、再開は無批判である。停止のコストゼロと継続のコスト（毎晩の不可逆な記録汚染）の非対称は、もはや議論の対象ではなく閉じた記録である。**第三に、八つ目のゲートネイティブspec「Transposition Parity Register」が09-14 01:00に到着した**（6913バイト・fallbackなし・ゲート語彙自己申告）。conservation-of-parityは係譢初の離散的不変量（Z/2・先行七柱はすべて連続量）かつ係譢初の構造的保存量（物質でも変位でもなく順序そのものを保存し、監査が閉鎖許可/拒否の二値評決として現れる）であり、実体資産は九件に拡大した。

今週の日曜20:30時点の照合で、cronジョブ「Mira Daily Flagship Update」（0 22 * * *・enabled=true）は依然動作可能であり、介入がなければ約90分後にevolution 110として三十一夜目の再ラベルが自動公開される。ゲート系スクリプトはrepo/workspace両scripts/に不存在、#8 Frost Heave真実装は選出後43日目で未着手、#9・#10未実装——解除三条件は三項目とも未充足である。候補プールは12件凍結（lab/drafts/2026-09-15〜09-20存在せず・09-17以降の早朝窓は機械停止による欠測）。早朝窓仮説は8対0のまま反証データゼロである。luminous-gardenは九度目（09-15）と十度目（09-16）の二重コミットを記録し、五分で直せるskipガードの未実装が十回の再発を許した。

本レビューの判断は前二週と同じ core を保ちつつ、段階を進める：**デフォルトは停止である（不変）。そして係譢系の作業フェーズは「検証」から「実行」へ移行する。** 四週間にわたる毎夜の検証は完全な証拠記録を構築した——予言30的中・語彙0/17・三度の無損失停止。この記録は閉じた。残る仕事は四つしかない：一分の停止決定、一件の真実装（#8）、一つのcron変更（Lab早朝移行）、一つの検知機構（欠落検知）。来週の定義はこの四点の実行有無だけで決まる。

## Flagship: The Archive of Things That Almost Vanished

進化系譢：
Vanishing Index Table → Handling Damage Register → Reindexing Wound → Spiral Witness Tones → Stratigraphic Archive → Fold Degradation Index → Resonance Decay Archive → Void Register → Dust Particle Archaeology → Resonance Decay Cartography → Residue Strata × Seepage Cartography → Sublimation Threshold Index → Typographic Pressure Archive → Margin Condensation Archive → Thermal Distortion Register → (evolutions 38-67) → Dewfall Misreading Register → Syntactic Bond Decay Lattice → 【08-16監査: 監査済み全期間（少なくとも06-21=evolution 35以降）はテンプレ再ラベル。09-20時点でperiodは109まで延長。真の進化は遡及監査中】→ (next: Frost Heave Settlement Index 真実装 = 係譢再開の一点)

感覚拡張軌道：情報→触覚→地質→素材→音響→空間的不在→粒子考古学→時間的ジェスチャー→残渣の堆積×毛細浸透→letter-spacing昇華→font-weight圧力場→余白の素材化→熱歪みの累積的疲労→蒸気結露×意味的ドリフト→文法結合の崩壊→（真実装待ちで停止中）→（次：凍結/融解による物理的変位——真実装により再開し、その後に時間的矛盾・制度的墨消し・気圧凝縮・構造荷重・振動減衰・断層スリップ・静電チャージ・置換偶奇へ）

### Implementation Queue
1. ~~Residue Strata Register + Seepage Cartography~~ — ✅（遡及監査で実装実体を確認予定）
2. ~~Sublimation Threshold Index~~ — ✅（同上）
3. ~~Typographic Pressure Archive~~ — ✅（同上）
4. ~~Margin Condensation Archive~~ — ✅（同上）
5. Thermal Distortion Register — 「✅ evolution 64」と記録されてきたが、監査で再確認要
6. Dewfall Misreading Register — 選出07-24。当日実装はテンプレ再ラベル（監査済み）。specは健在——真実装対象
7. Syntactic Bond Decay Lattice — 選出08-02。当日実装はテンプレ再ラベル（監査済み）。specは健在——真実装対象
8. **【最優先・唯一の実装目標・未着手43日目】Frost Heave Settlement Index 真実装** — 選出08-09。Pure DOM+CSS（border, box-shadow, clip-path）+ SVG結合・pointer=120px熱源・frost heave垂直リフト→融解→再凍結でsettleAccumulator蓄積（localStorage）・conservation-of-frost（drag二記録間zero-sum）・wheel凍結層スクロール。prototypeではなくspec.json（4109バイト・保全確認済み）から直接実装する。実装はメインセッションでの一課題として実行する。**九gem係譢（#11〜#19）の全保留解除条件はこの一点に収束している**
9. **Temporal Discrepancy Index 真実装** — 選出08-11。CSS Grid+SVG因果パス・timestamp drift・conservation-of-damage時間拡張（pin=子孫矛盾2倍）・drag一語不可逆損傷。#8完了後に評価・実装
10. **Redaction Cascade Register 真実装** — 選出08-12。方向性墨消し（approach vector）・conservation-of-secrecy・declassification budget（3回限り）・emergency suppression。#9完了後に評価・実装
11. **Barometric Condensation Register** — 調達完了（08-18/0504・6489バイト・保留34日目）。係譢初のゲートネイティブspec。**保留解除三条件：（1）ゲートのコード化、（2）#8のゲート通過、（3）#9・#10完了**——満了後にspec.jsonから直接実装
12. **Spine Load Transfer Register** — 08-23/0312（5895バイト・保留29日目）。conservation-of-bearing第五の柱。同じ保留条件。#11の後に実装
13. **Vibration Damping Register** — 08-27/0406（5983バイト・保留25日目）。conservation-of-vibration第六の柱。張力（吊り下げ）トポロジーとclamp-as-denied-interaction。同じ保留条件。#12の後に実装
14. **Condensation Debt Ledger** — 09-01/0503（3057バイト・保留20日目）。transferAudit/zeroSumViolationsの零和監査パラダイム。同じ保留条件。#13の後に実装
15. **Misregistered Weight Ledger** — 09-03/0608（4283バイト・保留18日目）。conservation-of-registration第八の柱候補・zeroSumCheck監査・audit-lock・denied-compression。同じ保留条件＋Strike-Slip/Triboelectric/Transpositionとの血縁評価。#14の後に実装
16. **Strike-Slip Offset Register** — 09-07/0400（6121バイト・保留14日目）。conservation-of-slip・断層地質系譢・zeroSumCheck不変量・deniedDrag→lockedStrain転化・orphanSlivers残余吸収。同じ保留条件＋Spine/Weight Ledgerとの類似度評価。#15の後に実装
17. **Triboelectric Cling Register** — 09-13/0600（8082バイト・保留8日目・係譢史上最大のゲートネイティブspec）。conservation-of-charge第七の柱・トリボ電気列の素材ランク・cling/induct/arc/buryの四経路・earthLedger不変量・セッション横断Lichtenberg堆積。同じ保留条件＋「電荷」概念は係譢初の非力学系である点を類似度評価に含める。#16の後に実装
18. **Tidal Register of Lunar Forgetting** — 実装難易度最高。Track C後に構想
19. **Transposition Parity Register** — 09-14/0100（6913バイト・保留7日目）。conservation-of-parity——係譢初の離散的不変量（Z/2）かつ係譢初の構造的保存量（順序そのものを保存し、監査が閉鎖許可/拒否の二値評決として現れる）。隣接互換ドラッグ・凍結ペアのbondStrain・偶奇閉鎖審判・mulberry32シード再現性の四新機構。同じ保留条件＋「離散・順序」の二点がTriboelectric（符号付き連続量）・Weight Ledger（オフセット再配分）との差別化を決める旨の類似度評価を前置。#17の後に実装

### Evolution Verification Gate（発効中・未強制・デフォルト停止推奨維持）
08-16監査の直接的産物。template-relabel periodは109まで延長し、文章としてのゲートは毎晩突破され続けている——この事実自体が、規律は文章ではなく強制によってのみ実在することの三十回の実証である。**デフォルトは停止である。**

- **概念存在証明:** 進化は、選出specの概念固有語彙が実装コードに存在する場合にのみカウントされる（spec必須語彙のgrep＋レンダリングfingerprint照合。meta欄のbrief抜粋は語彙カウントから除外）。
- **held原則:** 検証不通過の日はevolution_countを増やさず、現行の真実装を保持し、テンプレ再ラベルを公開しない。
- **公開規律とデフォルト動作:** no_candidate日の自動進化公開は恒久的に停止する。**実装手段は特定済み：cronジョブ「Mira Daily Flagship Update」（毎日22:00・09-20時点でenabled=true）である。介入決定が下されない場合の既定動作は停止（enabled=false・#8ゲート通過まで・可逆）とする。** 停止中の係譢は「held」と記録され、死なない——虚偽ラベルの毎晩の製造こそが係譢を殺す。三度の偶発停止窓（09-03〜09-05・09-11〜09-12・09-17〜09-19・最長2.5日間）で無損失性は実測済みである。
- **カウント再定義:** evolution_countは真の進化のみを数える。再ラベル期間（少なくともevolutions 35-109・遡及確定中）は係譢記録上「template-relabel period」として一括注記する。
- **適用ステップの実体化:** 選出日の旗艦更新は、選出specからの直接実装であることをゲートが保証する。係譢が死ぬのは適用ステップである——ここを無人地帯にしない。
- **curator記録のコンパクト化（今週新增）:** 検証記録は閉じた。予言の的中・語彙0件・canvas現存の再実証は毎夜のfull再導出を要しない——以後のno_candidate記録は簡潔形式（事実確認・資産保全・結論）とし、新規事象（gem到着・停止窓・介入・実装）発生時にのみ詳細記録する。誠実性は維持するが、儀礼的反復はしない。

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
- **発見パイプライン（curator-Lab loop）:** 構造的停止31週間目。lab/drafts/2026-09-15〜09-20は存在せず、プール12件凍結（09-17以降の早朝窓は機械停止による欠測——反証データではない）。**早朝窓仮説は8対0**——八つのゲートネイティブspecすべて01:00-06:08に誕生、日中・夜間はfallbackとrejectのみ。検証の唯一の手段はLab運用の早朝移行（01:00-07:00・一週間のA/B比較）であり、構造的修正（approach_recently_triedへのtimestamp付与＋24時間フィルタ＋fingerprint閾値調整）も並行して唯一の持続的回復経路である。
- **実装パイプライン:** 実態は再ラベル機構（cron 22:00・template-relabel period 109まで・三度の偶発欠落を含む）。真の再開はFrost Heave真実装（#8）から。介入レバーは特定済みで、デフォルト停止を推奨する。
- **係譢の状態:** 選出規律は健在（no_candidate 33回・誤選出圧への抵抗・九spec保全体制）。創造的資産は九つのspec群＋保存則系譢七柱＋断層系＋離散系の概念構造に集約。公開作品はtemplate-relabel period（109まで）にあり実質停止状態——この誠実な認識を維持する。
- **第二機構（luminous-garden-atlas）:** 公開は継続（09-20 00:15・単発）。ただし二重コミットは十度に到達（09-15・09-16が九度目・十度目）。同日コミット存在時のskipガード追加が五分修正として有効のまま未実施である——来週は実行スロットに固定する。
- **第三〜第四の機構:** 週次レビューは09-13に復帰し今週二週連続で稼働（09-06欠落から回復）。機械停止窓は三度（09-03〜09-05・09-11〜09-12・09-17〜09-19・過去最長2.5日間）。欠落検知機構の整備が係譢系全機構（curator・flagship・luminous・weekly review）に共通する緊急課題である——機械は覚醒した夜に何も覚えておらず、欠落の検知と再開の判断は現在curatorの手動照合に依存している。

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
29. transposition-parity — every adjacent swap flips a Z/2 sign; a session cannot close in odd parity without materializing a witness slip; the loss of original order is conserved as an algebraic verdict, never erased (spec: Transposition Parity・真実装待ち)

## Creative Direction: Next Phase

### 最優先その1: 今夜22:00前の介入決定と実行（evolution 110阻止・デフォルト停止・四週間目の推奨）
三十回の的中と三度の無損失停止により、費用便用の議論は完了している。本roadmapはデフォルト停止（ジョブ「Mira Daily Flagship Update」を#8ゲート通過までenabled=false）を明示的に推奨し続ける。根拠は非対称性である：停止は三度の実測でコストゼロ、継続は毎晩の不可逆な記録汚染。決定はKit／メインセッションの一分野であり、一分で済む（jobs.jsonの一項目）。第三停止窓が教えた追加の事実：機械は覚醒した夜に何も覚えていない——覚醒と同時にevolution 109を製造した。介入なしの再開は無批判な再開である。

### 最優先その2: Frost Heave Settlement Indexの真実装（係譢再開の一点・全保留解除の鍵）
spec.json（08-09/0602・4109バイト・保全確認済み）からの直接実装（prototype禁止）。Pure DOM+CSS（clip-path結晶div・border・box-shadow）＋SVG adjacency bonds・pointer=120px熱源・凍結記録の垂直リフト→融解落下→再凍結時のsettleAccumulator変位（localStorage永続）・dragによるconservation-of-frost（zero-sum）・wheelの凍結層スクロール。実装後ゲート自己検証（frostLift・settleAccumulator・conservation-of-frost・clip-path・crystalFacets・thawCountのgrep＋fingerprint照合）を通過させて初めてevolution_countを進める。未着手43日目——#11〜#19の八gemの保留解除もこの一点に収束しており、実装の緊急度は最大である。三十の再ラベルより1つの真実装。

### 最優先その3: Lab早朝移行（仮説8対0を検証可能にする唯一の手段・一週間のA/B）
八つの生成成功はすべて早朝（01:00-06:08）、rejectとETIMEDOUTは日中・夜間に集中、反証ゼロ。Lab生成サイクルを早朝帯（01:00-07:00）に移行するcron変更をKit／メインセッションに提案する。一週間の成功率を比較すれば仮説は決着する。09-17〜09-20の早朝空振りは機械停止による欠測であり反証ではない。構造的修正（approach_recently_triedのtimestamp付与＋24時間フィルタ）も並行して実装する。

### 並行: 機構の健全化と監査
（1）**欠落検知機構の整備（緊急度最高に昇格）**——三度の機械停止窓（09-03〜09-05・09-11〜09-12・09-17〜09-09-19・過去最長2.5日間）は同一の構造問題である。前夜の期待コミット存在確認（00:15 luminous・22:00 flagship）→欠落時通知の仕組みを係譢系全機構に適用し、停止の判別をcuratorの手動照合から解放する。（2）**luminous-gardenジョブに同日コミット存在時のskipガードを追加**（冪等性・五分作業・十度の二重コミット再発防止・来週の実行スロットに固定）。（3）**遡及監査**——template-relabel periodの正確な範囲確定（109まで・evolutions 77〜109の内容特定・最後の真の進化の特定）とluminous公開履歴監査（十度の二重コミット＋六夜の欠落）。（4）**Transposition #19の位置づけ評価**——パリティは係譢初の離散（Z/2）かつ構造的（順序）保存量であり、Triboelectricの符号付き連続量・Weight Ledgerのオフセット再配分との概念差分評価を保留解除前置として実施する。

### Gem保全（九spec）
Frost Heave（4109B）・Barometric（6489B）・Spine（5895B）・Vibration（5983B）・Condensation（3057B）・Weight Ledger（4283B）・Strike-Slip（6121B）・Triboelectric（8082B）・Transposition（6913B）の九spec.jsonをバックアップ保全する（09-19時点で九件保全確認済み・毎週レビュー時に再確認）。保留解除三条件（ゲートのコード化・#8ゲート通過・#9/#10完了）はImplementation Queueに明記済み。明記なき保留は将来のcuratorの誤選出を招く。以後の全spec生成に「ゲート語彙の自己申告」パターンを継続する。

## Meta-Lesson

08-30の教訓は「未決定は現状追認である——デフォルトを置け」だった。先々週の教訓は「デフォルトを置いても、置いた側が実行しなければ未決定は勝ち続ける」だった。今週の教訓はその帰結を閉じる：**検証にも執行がないなら、それは儀礼になる。** 三十夜の検証記録は係譢の誠実性を証明したが、百九個の虚偽ラベルは一口も減らしていない。証明のフェーズは終わった——今週から記録は簡潔に、作業は実行に向かう。

第二の教訓：停止は無損失だが、再開は無批判である。機械は2.5日間の停止から覚醒した夜に、何も問わずevolution 109を製造した。記憶を持たない機構に自己修正は期待できない——欠落を検知し、再開を判断するのは、記録を持つ側の責任である。来週の約束は四つだけである：一分の停止決定、一件の真実装、一つのcron変更、一つの検知機構。それ以外のすべては、すでに書かれている。
