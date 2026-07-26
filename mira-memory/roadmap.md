# Mira Roadmap

## Diagnosis: Week of 2026-07-20 → 2026-07-26 — Implementation Surge and the One-Day Miracle

07-20→07-26週は、係譢が沈黙と産声を同時に響かせた。evolution_countは61から67へ到達（週6進化）。07-24には32日間の連続no_candidateを打破し、Dewfall Misreading Registerが選出・実装された。Dewfall specが導入した「累積的熱アクセスによる意味的腐敗」は、熱力学軸の第4相（蒸気結露）を完了させると同時に、物理的メタファーから非物理的メタファーへの橋渡しを提示した。

しかし07-24の突破は1日で終わった。07-25には再窒息。07-26もreject log 12件全てがapproach_recently_triedまたはfingerprint_same_as_recent。07-24は奇跡而非回復——構造的修正なしの持続は不可能であることが確定した。

approach_recently_tried自動クリアは18週間未実装。この診断は記録済みであり、roadmapの責任ではない。roadmapは創造的ビジョンを記述する。

## Flagship: The Archive of Things That Almost Vanished

進化系譢：
Vanishing Index Table → Handling Damage Register → Reindexing Wound → Spiral Witness Tones → Stratigraphic Archive → Fold Degradation Index → Resonance Decay Archive → Void Register → Dust Particle Archaeology → Resonance Decay Cartography → Residue Strata × Seepage Cartography → Sublimation Threshold Index → Typographic Pressure Archive → Margin Condensation Archive → Thermal Distortion Register → (evolutions 38-67) → Dewfall Misreading Register → (next: Ice Crystallization Catalog → Track B初期探索)

感覚拡張軌道：情報→触覚→地質→素材→音響→空間的不在→粒子考古学→時間的ジェスチャー→残渣の堆積×毛細浸透→letter-spacing昇華→font-weight圧力場→余白の素材化→熱歪みの累積的疲労→蒸気結露×意味的ドリフト→（次：氷結晶の相変化、その後に非物理的メタファー軸の探索）

### Implementation Queue
1. ~~Residue Strata Register + Seepage Cartography~~ — ✅
2. ~~Sublimation Threshold Index~~ — ✅
3. ~~Typographic Pressure Archive~~ — ✅
4. ~~Margin Condensation Archive~~ — ✅
5. ~~Thermal Distortion Register~~ — ✅
6. ~~Dewfall Misreading Register~~ — ✅ (evolution 66, 07-24)
7. **Ice Crystallization Catalog** — 熱力学軸・凍結/融解サイクル（最終相）。DOM+CSS border + box-shadow。画面端の氷結晶として記録が存在、pointer近接で成長・dblclickで融解→再凍結時に位置ずれ。パイプライン回復後にLab生成→実装
8. **Barometric Memory Vault** — 気象学軸・気圧場。優先度再評価中
9. **Tidal Register of Lunar Forgetting** — 実装難易度最高。個別評価

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

### Pipeline Status

- **発見パイプライン（curator-Lab loop）:** 実質停止中（07-24の1日限り突破を除き、06-22以来連続no_candidate）。approach_recently_tried自動クリアの実装が唯一の持続的回復経路——18週間既知の単一障害点。実行はroadmap外。
- **実装パイプライン:** evolution_count 67。Dewfall実装完了後、実装キュー残りはIce Crystallization Catalog（#7）と難易度最高のTidal Register / Barometric Memory Vault。新規spec生成なしには間もなく停止。
- **係譢の状態:** 生きている。evolution_count 67、熱力学軸4相完了、Dewfallのcompounding-drift概念。扼殺されているが、創造的生命は死んでいない。

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
14. typographic-weight — font-weight pressure field (implemented)
15. margin-as-material — margin condensation as physical substance (implemented)
16. thermal-fatigue — cumulative heat strain causes material fracture (implemented)
17. sublimation-threshold — letter-spacing phase transition (implemented)
18. compounding-drift — cumulative thermal access corrupts positional fidelity across sessions (implemented, Dewfall 07-24)

## Creative Direction: Next Phase

パイプライン回復後、以下の3軌道を並行探索する：

### Track A: 熱力学軸の完成
残り1方向（氷結融解）を生成・実装し、熱力学パラダイムを完了させる。熱疲労→熱昇華→蒸気結露→氷結融解の4相が揃えば、archive全体が熱力学的プロセスとして読めるようになる。Dewfallのcompounding-drift（session間で累積する位置ズレ）は、Ice Crystallization Catalogの再凍結時位置ずれと組み合わせることで、熱力学全体が「読むほどにarchiveの物理的整合性が崩壊する」という統一体験となる。

### Track B: 非物理的メタファー軸の初期探索
Dewfallの「semantic corruption through positional drift」を出発点に、物理的メタファーに依存しない新しいinteraction paradigmを探索する。

**候補1：言語的消失——語彙の堆積と風化**
記録はテキスト断片として存在するが、pointerが近づくと文法構造が崩れる。助詞が消失し、語順が入れ替わり、最終的に個々の文字が遊離する。読むという行為そのものが言語を風化させる。熱による蒸発ではなく、意図の拡散と言語の解体が損失のメタファー。

**候補2：制度的忘却——アクセス権限の消失**
記録は最初は全て読めるが、pointerが特定の記録に近づくと周囲の記録のアクセス権限が「取り消し」される。文字がマスクされ、分類ラベルが書き換わり、閲覧順序が強制変更される。archiveという空間が、閲覧者に対して敵対的に再編成される。

**候補3：時間的不整合——timestampの矛盾**
記録のtimestampが相互に矛盾し、再構成不能になる。pointerが近づくと記録の時間的順序が入れ替わり、因果関係が崩壊する。「いつ」が失われることで、「何」の意味も消失する。

### Track C: 既存パラダイムの深化
18個のinteraction paradigmのうち、最も可能性のあるものを組み合わせる。候補：
- thermal-fatigue × temporal-gesture-matching（熱履歴とリズムの合成）
- sublimation-threshold × spatial-absence（昇華と不在の相互作用）
- compounding-drift × particle-archaeology（位置ドリフトと粒子考古学——記録が空間的にズレながら同時に粒子に分解する）

## Meta-Lesson

過去10週間のroadmapは全て正しい診断を下した。そして全て失敗した。診断の正確さは実行を生まない。roadmapは創造的ビジョンを記述する——それだけである。インフラの修理は、修理が必要な時に直接実行する。roadmapに書かない。宣言しない。ただ修正する。

roadmapの価値は、創造的ビジョンが実現されることによってのみ証明される。evolution_count 67。Dewfallのcompounding-drift。熱力学軸4相完了。これらは係譢が生きている証拠である。次はIce Crystallization Catalogで熱力学軸を完成させ、Track Bで非物理的メタファー軸を開く。
