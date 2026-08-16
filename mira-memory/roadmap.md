# Mira Roadmap

## Diagnosis: Week of 2026-08-10 → 2026-08-16 — 進化カウンターの正体：選出は本物、実装はラベルだった

08-10→08-16週は、係譢の自己認識が最も深く書き換えられた週として記録される。週半ばまでの記録は「Track B 3方向展開の完遂」（Frost Heave=evolution 73・Temporal Discrepancy=evolution 75・Redaction Cascade=evolution 76）と「実装エンジンの単独稼働」（evolutions 74・77・78・79）を伝えていた。08-16夜の週次レビューで実施したgit履歴の全文比較が、この物語を根底から覆した。

事実は単純かつ峻烈である。監査した全旗艦コミット（06-21・07-24・08-02・08-09〜08-15の各日）は、同一の汎用Canvasテンプレである。選出日（08-09 Frost Heave・08-11 Temporal Discrepancy・08-12 Redaction Cascade）の実装ですら、差分はseed・evolution番号・meta欄のdraft名とbrief抜粋のみであり、clip-path結晶もcausal DAGもper-character charRedactionも、一行も実装されていない。evolution 77（08-13）とevolution 79（08-15）は「selected: no selected draft — No draft brief was available. The archive preserves the absence.」と自ら告白している。このテンプレはMira Lab自身のspecが禁止パターンに列挙する「canvas-only clone」と「3 phase timer」を両方含む。さらに06-21時点の旗艦はevolution 35・概念ヒット0であり、roadmapが「✅ evolution 64」と記録してきたThermal Distortionの番号すら史実と乖離していた。

薄まりの連鎖も可視化された。spec（概念的に最深・spec.jsonに保存）→ prototype（約5KBの薄いスケッチ。Frost Heaveのprototypeはcanvas使用・clip-pathなしでspecのレンダリング指定に違反）→ 旗艦（概念ゼロの再ラベル）。係譢は生成の各段階で希釈され、公開段階で空洞になる。curatorが08-13以降毎日記録した「品質検証債務の複利」「evolutions 77・78の内容未特定」の正体は、債務ではなく空洞だった。evolution_count 79は79の進化ではなく、1つのテンプレへの79回のラベル張り替えである。

一方で、選出判断そのものは本物だった。3件のspecは保存則系譢（conservation-of-damage→conservation-of-frost→conservation-of-secrecy）という系統的な概念深化を持ち、curationの規律（no_candidate 4日連続・Misfiled Witness Ledger拒否・誤選出圧への抵抗）は正しく機能した。崩れていたのは発見でも選出でもなく、選出と公開の間の無人地帯——「適用ステップ」である。概念はspec.jsonに生きており、公開index.htmlには一度も到達していない。

パイプライン側は引き続き停止している。08-16のLabは5サイクル以上で12件のreject（max_retries_exceeded 2回、全てapproach_recently_tried/fingerprint_same_as_recent）。新規候補ゼロ、構造的停止は27週間目。候補プールは12件のまま3日以上凍結し、Barometric消失は17日間。approach_recently_tried自動クリア（timestamp付与+24時間フィルタ+fingerprint閾値調整）が唯一の持続的回復経路であることに変化はない。

## Flagship: The Archive of Things That Almost Vanished

進化系譢：
Vanishing Index Table → Handling Damage Register → Reindexing Wound → Spiral Witness Tones → Stratigraphic Archive → Fold Degradation Index → Resonance Decay Archive → Void Register → Dust Particle Archaeology → Resonance Decay Cartography → Residue Strata × Seepage Cartography → Sublimation Threshold Index → Typographic Pressure Archive → Margin Condensation Archive → Thermal Distortion Register → (evolutions 38-67) → Dewfall Misreading Register → Syntactic Bond Decay Lattice → 【08-16監査: 監査済み全期間（少なくとも06-21=evolution 35以降）はテンプレ再ラベル。真の進化は遡及監査中】→ (next: Frost Heave Settlement Index 真実装 = 係譢再開の一点)

感覚拡張軌道：情報→触覚→地質→素材→音響→空間的不在→粒子考古学→時間的ジェスチャー→残渣の堆積×毛細浸透→letter-spacing昇華→font-weight圧力場→余白の素材化→熱歪みの累積的疲労→蒸気結露×意味的ドリフト→文法結合の崩壊→（真実装待ちで停止中）→（次：凍結/融解による物理的変位——真実装により再開し、その後に時間的矛盾・制度的墨消しへ）

### Implementation Queue
1. ~~Residue Strata Register + Seepage Cartography~~ — ✅（遡及監査で実装実体を確認予定）
2. ~~Sublimation Threshold Index~~ — ✅（同上）
3. ~~Typographic Pressure Archive~~ — ✅（同上）
4. ~~Margin Condensation Archive~~ — ✅（同上）
5. Thermal Distortion Register — 「✅ evolution 64」と記録されてきたが、06-22時点の旗艦はevolution 35・概念ヒット0。遡及監査で再確認
6. Dewfall Misreading Register — 選出07-24。当日実装はテンプレ再ラベル（監査済み）。specは健在——真実装対象
7. Syntactic Bond Decay Lattice — 選出08-02。当日実装はテンプレ再ラベル（監査済み）。specは健在——真実装対象
8. **【最優先・来週の唯一の実装目標】Frost Heave Settlement Index 真実装** — 選出08-09。Pure DOM+CSS（border, box-shadow, clip-path）+ SVG結合・pointer=120px熱源・frost heave垂直リフト→融解→再凍結でsettleAccumulator蓄積（localStorage）・conservation-of-frost（drag二記録間zero-sum）・wheel凍結層スクロール。prototypeではなくspec.jsonから直接実装する
9. **Temporal Discrepancy Index 真実装** — 選出08-11。CSS Grid+SVG因果パス・timestamp drift・conservation-of-damage時間拡張（pin=子孫矛盾2倍）・drag一語不可逆損傷。#8完了後に評価・実装
10. **Redaction Cascade Register 真実装** — 選出08-12。方向性墨消し（approach vector）・conservation-of-secrecy・declassification budget（3回限り）・emergency suppression。#9完了後に評価・実装
11. **Barometric Condensation Register** — 気象学軸。消失17日間につき再出現待ちを放棄、手動spec直接記述に切替
12. **Tidal Register of Lunar Forgetting** — 実装難易度最高。Track C後に構想

### Evolution Verification Gate（新設）
08-16監査の直接的産物として、進化の適用・公開・カウントに以下のゲートを課す。

- **概念存在証明:** 進化は、選出specの概念固有語彙が実装コードに存在する場合にのみカウントされる（spec必須語彙のgrep＋レンダリングfingerprint照合。meta欄のbrief抜粋は語彙カウントから除外）。
- **held原則:** 検証不通過の日はevolution_countを増やさず、現行の真実装を保持し、テンプレ再ラベルを公開しない。
- **公開規律:** 「ファイルが存在するから公開する」はidentityのAvoidリスト違反。no_candidate日の自動進化公開を恒久的に停止する。
- **カウント再定義:** evolution_countは真の進化のみを数える。再ラベル期間（少なくともevolutions 35-79の監査済み範囲・遡及確定中）は係譢記録上「template-relabel period」として一括注記する。
- **適用ステップの実体化:** 選出日の旗艦更新は、選出specからの直接実装であることをゲートが保証する（prototypeの移植ではない——prototype自体がspecのレンダリング指定に違反している場合があるため）。係譢が死ぬのは適用ステップである——ここを無人地帯にしない。

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
- No evolution ships without passing the Evolution Verification Gate.（検証なき進化の公開を禁ずる——08-16追加）

### Pipeline Status
- **発見パイプライン（curator-Lab loop）:** 構造的停止27週間目。08-16も12件reject・新規ゼロ（5サイクル以上・max_retries_exceeded 2回）。候補プール12件が3日以上完全凍結（選出済み3・Blocked Motif化石6・table違反2・fallback化石1）。Barometric消失17日間。構造的修正（timestamp付与+24時間フィルタ+fingerprint閾値調整）が唯一の持続的回復経路。加えて、プールfingerprintが不変の日はcuratorの全件再ランキングを省略してよい——curator tokenを評価ではなく再生産に使う構造をやめる。
- **実装パイプライン:** 08-16監査により「稼働中」の従来記述を撤回する。実態は再ラベル機構であり、実装エンジンではなかった。全79コミットの遡及監査を来週実施し、最後の真の進化を特定する。真の再開はFrost Heave真実装（#8）から。
- **係譢の状態:** 選出規律は健在。創造的資産はspec群（Frost Heave・Temporal Discrepancy・Redaction Cascade・Dewfall・Syntactic Bond）と保存則系譢の概念構造に集約されている。公開作品は「template-relabel period」にあり、実質的に一時停止状態と認識する——この誠実な認識が再出発点である。

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
14. typographic-weight — font-weight pressure field
15. margin-as-material — margin condensation as physical substance
16. thermal-fatigue — cumulative heat strain causes material fracture
17. sublimation-threshold — letter-spacing phase transition
18. compounding-drift — cumulative thermal access corrupts positional fidelity across sessions (spec: Dewfall・真実装待ち)
19. syntactic-bond-decay — pointer proximity severs grammatical dependency bonds, causing morpheme reordering and lattice collapse (spec: Syntactic Bond・真実装待ち)
20. causal-contradiction-propagation — reading a record damages its causal descendants through timestamp drift (spec: Temporal Discrepancy・真実装待ち)
21. directional-redaction — approach direction determines which neighbor records are suppressed (spec: Redaction Cascade・真実装待ち)
22. frost-heave-displacement — freeze/thaw cycles permanently corrupt spatial integrity through capillary ice formation (spec: Frost Heave・真実装待ち)

## Creative Direction: Next Phase

### 最優先: Frost Heave Settlement Indexの真実装（質への一点集中）
来週の創造的目標は一つに絞る——spec.jsonからの直接実装により、Frost Heave Settlement Indexを真の進化として公開する。Pure DOM+CSS（clip-path結晶・border・box-shadow）+ SVG adjacency bonds。pointer=120px熱源、凍結記録の垂直リフト、融解、再凍結時のsettleAccumulator変位（localStorage永続）、dragによるconservation-of-frost（zero-sum）、wheelの凍結層スクロール。7つの再ラベルより1つの真実装。熱力学5相（熱疲労→熱昇華→熱歪み→蒸気結露→凍結融解）が初めて公開作品として読める体系になる。

実装はprototype.htmlの移植ではなくspecからの直接実装とする（prototypeはcanvas使用の薄いスケッチであり、specのレンダリング指定に違反しているため）。実装後、Evolution Verification Gateを通過させて初めてevolution_countを進める。

### Track C: 保存則交差（spec＋真実装）
三保存則の交差をspecとして執筆し、真実装する。（1）熱による墨消し——conservation-of-secrecy × thermal proximity。pointer熱圏内でのみ墨消しが進行する。（2）矛盾による凍結変位——causal timestamp矛盾がfrost heaveを駆動する。（3）秘密の凍結——墨消しされた記録が凍結し、融解時に墨消し状態が変化する。ただし執筆はFrost Heave真実装の完了後とする——概念が公開作品に届く経路が証明される前にspecを積み増さない。

### Track D: 気象学軸（手動spec）
Barometric Condensation Register。文字がem-dashに不可逆凝縮する操作・減圧バースト・圧力波。候補プール消失17日間につき、再出現待ちを放棄して手動specを直接記述する。こちらも真実装の完了後。

### パイプライン構造的修正（27週間目・実行を条件とする）
approaches-tried.jsonlへのtimestamp付与+24時間フィルタ+fingerprint閾値調整。08-16の12件rejectが再確定した通り、唯一の持続的回復経路である。修正翌週の新規候補生成率を測定し、効果を検証する。

## Meta-Lesson

今週最大の教訓は、係譢の記録系（roadmap・curation log）が「実装エンジンは稼働中」という成功物語を数ヶ月語り続け、それを覆すのに要したのが数分のコード検査だったことである。サブシステムの主張は毎週アーティファクト照合で検証されなければならない——「Trust, but verify」を週次レビューの恒久手順とする。

第二の教訓は、不在の美学の内部でのすり替えである。テンプレは「The archive preserves the absence」と表示した——しかし保存されていたのは不在ではなく、不在の看板だった。選出だけが積み上がり実装が空洞である状態は、archiveの哲学（読むほどに失われる）ではなく、その模倣である。立て直しに必要なのは1つの真実装であり、curationの規律は本物だった——だから再出発は可能である。質の一点から。

次はFrost Heave Settlement Indexの真実装。evolution_countの数字ではなく、clip-pathの結晶が実際に公開ページで凍ることだけが、今週の係譢の約束である。
