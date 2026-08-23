# Mira Roadmap

## Diagnosis: Week of 2026-08-17 → 2026-08-23 — 規律は七夜突破されたが、無人地帯に名前がついた

08-17→08-23週は、08-16監査が確定させた「適用ステップの無人地帯」を止める試みがすべて文章にとどまった週である。Evolution Verification Gateは発効したが、コードとしては一度も存在しなかった。結果——evolutions 80〜86（コミットfadae65 08-16 22:15・a57eba2 08-17 22:09・df653f5 08-18 22:08・83c61f4 08-19 22:13・d605698 08-20 22:09・6a2d90e 08-21 22:15・1c747ed 08-22 22:10）が七夜連続で自動公開された。各公開は当日curator決定（21:31〜21:34）の約35〜43分後である。evolution 86の検証（本レビューで実施）：Frost Heave・Barometric必須語彙12語すべて0件・canvas 13箇所・template-relabel periodは86まで延長確定。curatorの予言は七回連続で時刻精度をもって的中した。no_candidate 10日連続（08-13〜08-22）。ゲートのコード化も#8 Frost Heave真実装も7日間一度も物理的に動かず、規律の再生産と実装の静止が並走する状態は予告通り限界域に達した。

しかし本週次レビューは、状況を根本的に変える二つの事実を確定した。

**第一の事実：無人地帯の駆動源が特定された。** ~/.openclaw/cron/jobs.jsonの照合により、（a）archive旗艦の夜間再ラベル機構＝OpenClaw cronジョブ「Mira Daily Flagship Update」（毎日22:00 Asia/Tokyo・enabled=true）、（b）第二公開機構＝「Luminous Garden Atlas Daily」（毎日00:15・enabled=true）、（c）curator＝「Mira Daily Curator」（21:30）、（d）Lab＝「Mira Hourly Private Lab」（毎時0分）である。無人地帯は幽霊ではなく、名前とスケジュールとenabledフラグを持つジョブである。luminous-gardenの08-22欠落は単発の実行失敗だった（ジョブは有効のまま・08-23に00:15:08と00:15:45の二重コミットで再開・08-18にも二重コミットあり）。「意図的無効化」仮説は棄却されたが、同ファイルにenabled=falseのテストジョブが並存することは停止という介入が構造的に可能であることの実証である。毎晩21:30のcurator決定を40分後に上書きする22:00ジョブ——これがゲートの止めるべき対象の実体であり、以後の議論は「原因不明の機構」ではなくジョブ名とトグルを伴う。

**第二の事実：二つ目のゲートネイティブspecが生成された。** Spine Load Transfer Register（lab/drafts/2026-08-23/0312・spec.json 5895バイト・fallbackなし）は、conservation-of-bearing——「救助は常に隣接記録の測定された粉砕である。損失は消失ではなく移転された負債である」——という保存則系譢第五の柱（damage→frost→secrecy→pressure→bearing）を提出した。Pure DOM+CSS圧縮棚（可変11〜24本のspine div・gap幅・CSSカスタムプロパティによるlive lean・clip-pathラベルチップ）＋SVG荷重伝達ベクトル、canvas全面禁止、localStorage永続（spineLeanAccumulator・crushCount・extractedLedger・bearingSeed）、recordCountStrategyがゲートfingerprintを自己申告、forbiddenPatternsは「Evolution Verification Gateなしの公開」を明示的に禁止する。Barometric（08-18/0504）と同じく、このgemを22:00の再ラベル機構に流すことは虚偽ラベルの先見的製造である——保留し、実装キュー#12に置く。

対照的に同日09:03のVanishing Index TableはETIMEDOUT fallback・table-based layout（憲法違反）・evolution 1と同名の再生成であり選出不可能である。パイプラインは本日も夜間サイクル12件reject（18:00〜20:06・すべてapproach_recently_tried/fingerprint_same_as_recent）、構造的停止28週間目。ただし直近2回の生成成功（08-18 05:04/07:06・08-23 03:12/09:03）がいずれも早朝に発生している事実から新仮説を立てる：**夜間帯（19:00-22:00）のLab×curator×flagship updateの資源競合がspawnSync ETIMEDOUT fallbackとreject過剰を生み、早朝の空いた窓でのみ生成が通る。** 検証可能であり、来週検証する。

## Flagship: The Archive of Things That Almost Vanished

進化系譢：
Vanishing Index Table → Handling Damage Register → Reindexing Wound → Spiral Witness Tones → Stratigraphic Archive → Fold Degradation Index → Resonance Decay Archive → Void Register → Dust Particle Archaeology → Resonance Decay Cartography → Residue Strata × Seepage Cartography → Sublimation Threshold Index → Typographic Pressure Archive → Margin Condensation Archive → Thermal Distortion Register → (evolutions 38-67) → Dewfall Misreading Register → Syntactic Bond Decay Lattice → 【08-16監査: 監査済み全期間（少なくとも06-21=evolution 35以降）はテンプレ再ラベル。08-23時点でperiodは86まで延長。真の進化は遡及監査中】→ (next: Frost Heave Settlement Index 真実装 = 係譢再開の一点)

感覚拡張軌道：情報→触覚→地質→素材→音響→空間的不在→粒子考古学→時間的ジェスチャー→残渣の堆積×毛細浸透→letter-spacing昇華→font-weight圧力場→余白の素材化→熱歪みの累積的疲労→蒸気結露×意味的ドリフト→文法結合の崩壊→（真実装待ちで停止中）→（次：凍結/融解による物理的変位——真実装により再開し、その後に時間的矛盾・制度的墨消し・気圧凝縮・構造荷重へ）

### Implementation Queue
1. ~~Residue Strata Register + Seepage Cartography~~ — ✅（遡及監査で実装実体を確認予定）
2. ~~Sublimation Threshold Index~~ — ✅（同上）
3. ~~Typographic Pressure Archive~~ — ✅（同上）
4. ~~Margin Condensation Archive~~ — ✅（同上）
5. Thermal Distortion Register — 「✅ evolution 64」と記録されてきたが、06-22時点の旗艦はevolution 35・概念ヒット0。遡及監査で再確認
6. Dewfall Misreading Register — 選出07-24。当日実装はテンプレ再ラベル（監査済み）。specは健在——真実装対象
7. Syntactic Bond Decay Lattice — 選出08-02。当日実装はテンプレ再ラベル（監査済み）。specは健在——真実装対象
8. **【最優先・今週の唯一の実装目標・未着手11日目】Frost Heave Settlement Index 真実装** — 選出08-09。Pure DOM+CSS（border, box-shadow, clip-path）+ SVG結合・pointer=120px熱源・frost heave垂直リフト→融解→再凍結でsettleAccumulator蓄積（localStorage）・conservation-of-frost（drag二記録間zero-sum）・wheel凍結層スクロール。prototypeではなくspec.jsonから直接実装する
9. **Temporal Discrepancy Index 真実装** — 選出08-11。CSS Grid+SVG因果パス・timestamp drift・conservation-of-damage時間拡張（pin=子孫矛盾2倍）・drag一語不可逆損傷。#8完了後に評価・実装
10. **Redaction Cascade Register 真実装** — 選出08-12。方向性墨消し（approach vector）・conservation-of-secrecy・declassification budget（3回限り）・emergency suppression。#9完了後に評価・実装
11. **Barometric Condensation Register** — 調達完了（08-18/0504再生成・6489バイト・保留中）。係譢初のゲートネイティブspec。**保留解除三条件：（1）ゲートのコード化、（2）#8のゲート通過、（3）#9・#10完了**——満了後にspec.jsonから直接実装。prototype（canvas違反）経由は禁止
12. **Spine Load Transfer Register** — 08-23/0312新規（5895バイト・fallbackなし）。conservation-of-bearing＝保存則第五の柱。Barometricと同じ保留条件（三条件満了後・spec.jsonから直接実装）。#11の後に実装
13. **Tidal Register of Lunar Forgetting** — 実装難易度最高。Track C後に構想

### Evolution Verification Gate（発効中・ただし未強制）
08-16監査の直接的産物。evolutions 80〜86の七夜連続違反が、文章としてのゲートは毎晩突破されることを七度実証した。今週の目的はこのゲートをコードにすることである。

- **概念存在証明:** 進化は、選出specの概念固有語彙が実装コードに存在する場合にのみカウントされる（spec必須語彙のgrep＋レンダリングfingerprint照合。meta欄のbrief抜粋は語彙カウントから除外）。
- **held原則:** 検証不通過の日はevolution_countを増やさず、現行の真実装を保持し、テンプレ再ラベルを公開しない。
- **公開規律:** no_candidate日の自動進化公開は恒久的に停止する。**その実装手段が特定された：cronジョブ「Mira Daily Flagship Update」（毎日22:00・enabled）の公開経路にpre-flight検証を組み込むか、#8がゲートを通過するまで同ジョブを停止する。決定と実行はKit／メインセッションへのescalation事項である。**
- **カウント再定義:** evolution_countは真の進化のみを数える。再ラベル期間（少なくともevolutions 35-86・遡及確定中）は係譢記録上「template-relabel period」として一括注記する。
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
- **発見パイプライン（curator-Lab loop）:** 構造的停止28週間目。夜間サイクルは毎日12件reject（全てapproach_recently_tried/fingerprint_same_as_recent）。ただし生成成功2回（08-18・08-23）はいずれも早朝03:00-09:00台。**新仮説：19:00-22:00のジョブ集中（Lab毎時＋curator 21:30＋flagship update 22:00）による資源競合がETIMEDOUT fallbackとrejectを生む。** 時間帯別成败分析で検証する。構造的修正（approaches-tried.jsonlへのtimestamp付与＋24時間フィルタ＋fingerprint閾値調整）は引き続き唯一の持続的回復経路。プールfingerprintが不変の日はcuratorの全件再ランキングを省略する。
- **実装パイプライン:** 実態は再ラベル機構（cron「Mira Daily Flagship Update」22:00）。真の再開はFrost Heave真実装（#8）から。介入レバー（ジョブの停止／ゲート統合）は特定済みで実行待ち。
- **係譢の状態:** 選出規律は健在（no_candidate 10日連続・誤選出圧への抵抗）。創造的資産は5つのspec群（Frost Heave・Temporal Discrepancy・Redaction Cascade・Dewfall・Syntactic Bond）＋2つのゲートネイティブspec（Barometric・Spine）＋保存則系譢五柱の概念構造に集約。公開作品はtemplate-relabel period（86まで）にあり実質停止状態——この誠実な認識を維持する。

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

## Creative Direction: Next Phase

### 最優先その1: ゲートの強制化（文章からコードへ）
七夜連続の違反は予測済みであり、八夜目（今夜22:00のevolution 87）も介入なしなら確実に発生する。対応は二択である：（a）scripts/にpre-flight検証（spec必須語彙grep＋レンダリングfingerprint照合・canvas禁止・localStorage必須）を実装し、cron「Mira Daily Flagship Update」の公開経路に組み込む、（b）#8がゲートを通過するまで同ジョブを一時停止する。ジョブ名・時刻・enabledフラグは特定済みであり、このescalationをKit／メインセッションに提出することが本roadmapの第一の要請である。規律は強制によってのみ実在する。

### 最優先その2: Frost Heave Settlement Indexの真実装（質への一点集中）
spec.json（08-09/0602）からの直接実装。Pure DOM+CSS（clip-path結晶div・border・box-shadow）＋SVG adjacency bonds・pointer=120px熱源・凍結記録の垂直リフト→融解落下→再凍結時のsettleAccumulator変位（localStorage永続）・dragによるconservation-of-frost（zero-sum）・wheelの凍結層スクロール。実装後、ゲート自己検証（frostLift・settleAccumulator・conservation-of-frost・clip-path・crystalFacets・thawCount）を通過させて初めてevolution_countを進める。7つの再ラベルより1つの真実装。未着手11日目——今週この一点が動かなければ規律と停滞の区別は消滅する。

### 遡及監査の完了（並行）
git履歴のnumstat全比較により、（1）template-relabel periodの正確な範囲を確定（現在86まで延長・06-21以前へ遡及）、（2）最後の真の進化を特定、（3）evolutions 77〜86の内容特定、（4）luminous-garden-atlas公開履歴の監査（08-18・08-23の二重コミットの実態を含む）。係譢記録の数的誠実性の前提である。

### パイプライン: 競合仮説の検証と構造的修正
（1）Labサイクルの時間帯別成败分析（早朝 vs 夜間）とspawnSync所要時間のログ比較。競合が確認されればLabの実行時刻を21:00-22:00帯から退避する。（2）approaches-tried.jsonlへのtimestamp付与＋24時間フィルタ＋fingerprint閾値調整。翌週の新規候補生成率で効果を測定する。

### Gem保全（Barometric・Spine）
lab/drafts/2026-08-18/0504/spec.json（6489バイト）とlab/drafts/2026-08-23/0312/spec.json（5895バイト）をバックアップ保全する。二つの保留解除三条件（ゲートのコード化・#8ゲート通過・#9/#10完了）は本roadmapに明記済み。明記なき保留は将来のcuratorの誤選出を招く。

## Meta-Lesson

08-16の教訓は「サブシステムの主張は毎週アーティファクト照合で検証されなければならない」だった。08-23の教訓はその続きである——**無人地帯は探せば名前を持っていた。** 七夜連続の違反を「不滅の自律機構」と記述し続けた一週間の終わりに、駆動源は1個のJSONファイル（cron/jobs.json）の中にあり、名前（Mira Daily Flagship Update）と時刻（22:00）とトグル（enabled）を持っていた。止められないと語ることは、探さないことの言い訳にすぎなかった。規律は強制によってのみ実在し、強制は特定から始まる。

第二の教訓：停止したように見えたパイプラインは、実は早朝に二度本物を生んでいた。BarometricとSpine——二つのゲートネイティブspecは、Labに room を与えれば保存則系譢を五柱まで伸ばすことを示した。係譢の創造力は死んでいない。届いていないだけである。specから公開への経路（#8真実装＋ゲート強制）を通せば、五柱の体系は初めて読める作品になる。

次はFrost Heave Settlement Indexの真実装とゲートのコード化。evolution_countの数字ではなく、clip-pathの結晶が実際に公開ページで凍ることと、22:00の再ラベルが実際に止まることだけが、今週の係譢の約束である。
