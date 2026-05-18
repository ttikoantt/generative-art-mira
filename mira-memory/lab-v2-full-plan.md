# Mira Lab v2 — 課題・アーキテクチャ・改善提案

**作成日:** 2026-05-18
**レビュー参加:** Mira (OpenClaw GLM 5.1) + Codex CLI (OpenAI)
**関連ファイル:**
- 詳細レビュー議事録: `mira-memory/lab-improvement-review-2026-05-17.md`
- アーキテクチャ詳細: `mira-memory/lab-architecture-v2.md`

---

## 1. 現在の課題

### 1-1. 根本原因: 決定的テンプレート生成器

現在のLab生成スクリプト（`mira-hourly-lab-cycle.js`）は **LLMを一切使わない静的スクリプト**。

- `hour % 3` で3テーマ（missing-record-grid / damaged-label-ledger / archive-fragment-reassembly）をローテーション
- `makePrototypeHtml()` が常に同一HTMLを出力:
  - 18レコード固定配列
  - 3フェーズタイマー（10秒ごとに自動変異）
  - ポインターインタラクションなし
  - 66行Canvasのみ
- experiment IDの文字列だけが違い、MD5ハッシュは全て異なるが実質的に同一コード
- hypothesisテキストも3パターンのローテーション → roadmapがブロックした `fixed-3-template-rotation` そのもの

### 1-2. 派生問題

| 問題 | 詳細 |
|------|------|
| 全draftがクローン | 12件/日 全てが Curator で `no_candidate` 判定 |
| スコア評価が null | `visual_score`, `novelty_score`, `interaction_score`, `stability_score` 全件 null |
| 品質ゲート不通過 | null = ゲート不通過、旗艦に反映されない |
| ポインターインタラクションなし | roadmapの必須要件違反 |
| 旗艦の進化停止 | 合格draftがないため旗艦更新が止まる |
| Curatorへの負荷集中 | クローン検知がCuratorに丸投げ、パイプライン側で事前排除すべき |

### 1-3. なぜ気づかなかったか

- 生成スクリプトは `~/.openclaw/workspace/scripts/` にあり、リポジトリ内になかった
- 出力ファイル（prototype.html）のMD5は全部違う（experiment IDが埋め込まれているため）
-表面上は「毎時異なるテーマ名で生成されている」ように見える

---

## 2. 改善後アーキテクチャ

### 2-1. 全体フロー図

```
┌─────────────────────────────────────────────────┐
│              Hourly Lab Cycle (cron)              │
├─────────────────────────────────────────────────┤
│                                                   │
│  1. Context Load                                  │
│     ├ roadmap.md (要件 + ブロック済みmotif)        │
│     ├ motifs.json (active/blocked)               │
│     ├ latest-curation.json (curator feedback)    │
│     └ approaches-tried.jsonl (直近のアプローチ)    │
│                                                   │
│  2. Spec Generation (LLM)                        │
│     ├ 構造化JSON specを生成                       │
│     ├ 70% roadmap追従 / 30% 新規探索              │
│     └ curator feedbackを統合（期限付き）           │
│                                                   │
│  3. Spec Validation                               │
│     ├ 類似度チェック (specレベル)                  │
│     ├ 必須フィールド検証                          │
│     ├ forbiddenPatterns検出                       │
│     └ maxAttempts: 3 でリトライ                   │
│                                                   │
│  4. HTML Generation (LLM)                        │
│     ├ 承認済みspecからフルHTML生成                 │
│     └ 自己完結型・単一ファイル                    │
│                                                   │
│  5. Artifact Validation                           │
│     ├ 正規化テキスト類似度 >0.80 → reject         │
│     ├ AST類似度 >0.75 → reject                   │
│     ├ フィーチャーフィンガープリント              │
│     └ ランタイム検証 (Playwright)                 │
│                                                   │
│  6. Scoring (LLM)                                │
│     ├ visual_score, novelty_score                 │
│     ├ interaction_score, stability_score          │
│     └ ゲート不通過 → lab/rejected/               │
│                                                   │
│  7. Output (合格時)                               │
│     ├ lab/drafts/YYYY-MM-DD/HHMM-slug/           │
│     │  ├ brief.md                                 │
│     │  ├ spec.json                                │
│     │  ├ prototype.html                           │
│     │  └ evaluation.json (スコア付き)             │
│     └ approaches-tried.jsonl に追記              │
│                                                   │
│  7'. Output (拒否時)                              │
│     └ lab/rejected/YYYY-MM-DD/HHMM-slug/         │
│        ├ rejection-reason.json                    │
│        └ (prototype.html)                        │
└─────────────────────────────────────────────────┘
```

### 2-2. 各ステップの詳細

#### Step 1: Context Load

毎時のサイクル開始時に読み込むファイル:

- **roadmap.md** — 週次の方向性、必須要件、ブロック済みmotif
- **motifs.json** — active/blocked motif一覧
- **latest-curation.json** — Curatorの最新フィードバック
- **approaches-tried.jsonl** — 直近N件の試行アプローチ記録

#### Step 2: Spec Generation (LLM)

**ハイブリッド生成の前半:** LLMがまず「何を作るか」を構造化JSON specとして定義する。フルHTMLはまだ書かない。

specの例:
```json
{
  "title": "Misfiled Witness Ledger",
  "renderingMode": "DOM+SVG",
  "dataModel": "variable-length records with parent/child fragments",
  "recordCountStrategy": "seeded 9-27 records",
  "interactionModel": "drag record strips between columns; dropped records rewrite archive order",
  "stateModel": "localStorage persists vanished and locked records",
  "requiredEvents": ["pointerdown", "pointermove", "pointerup"],
  "forbiddenPatterns": ["fixed 18 records", "3 phase timer", "canvas-only"],
  "visualHypothesis": "text loss is shown through unstable filing order, not abstract missing boxes"
}
```

生成ルール:
- **70%** は roadmap + curator feedback に従う
- **30%** は新しい構造的アプローチを探索
- curator feedback は期限付き（6 drafts後に減衰）

#### Step 3: Spec Validation

コードが存在する前に検証する（これが最大の改善点）。

チェック項目:
- 必須フィールドの存在確認
- `forbiddenPatterns` との一致チェック
- 直近specとの類似度チェック
- `approaches-tried` との重複確認
- **maxAttempts: 3** — 失敗時は再生成、3回超過で拒否レポート

#### Step 4: HTML Generation (LLM)

承認済みspecからフルHTMLを生成。
- 自己完結型の単一HTMLファイル
- specで定義された renderingMode / interactionModel / stateModel を忠実に実装
- forbiddenPatterns を含まない

#### Step 5: Artifact Validation（多層検証）

| レイヤー | 手法 | しきい値 |
|----------|------|----------|
| 正規化テキスト類似度 | ID/タイムスタンプ/空白/コメント除去後のshingle比較 | >0.80 → reject |
| AST類似度 | Babel/Acornでパース、識別子/リテラル正規化後のノード比較 | >0.75 → reject |
| フィーチャーフィンガープリント | canvasCount, svgCount, eventListenerTypes等の比較 | 同一構成→reject |
| ランタイム検証 | Playwrightでロード確認、pointer event発火で状態変化確認 | エラー→reject |

#### Step 6: Scoring (LLM)

スコア項目（全て 1-5）:
- `visual_score` — 視覚的品質
- `novelty_score` — 新規性
- `interaction_score` — インタラクションの質
- `stability_score` — 安定性

品質ゲート: visual_score ≥ 3 かつ novelty_score ≥ 3 で合格

#### Step 7: Output

**合格時:**
```
lab/drafts/YYYY-MM-DD/HHMM-slug/
├── brief.md          # 実験の説明
├── spec.json         # 構造化spec
├── prototype.html    # 生成されたHTML
└── evaluation.json   # スコア付き評価
```

**拒否時:**
```
lab/rejected/YYYY-MM-DD/HHMM-slug/
├── rejection-reason.json  # 拒否理由（分類付き）
└── prototype.html         # 参考用に保持
```

---

## 3. 改善提案

### 3-1. Codex CLIとの議論で判明したブラインドスポット

Miraの初期提案（3段階）は方向性正しかったが、以下を見落としていた:

| # | ブラインドスポット | 詳細 |
|---|-------------------|------|
| 1 | **ランタイムバリデーション** | Playwright等で「ページがロードできるか」「pointer eventで状態が変わるか」を検証すべき |
| 2 | **リトライ予算** | max 3回失敗したら拒否レポートを書く |
| 3 | **アンチチーティングチェック** | `usesPointerInteraction: true` とメタデータに書いても、実際に動くか検証が必要 |
| 4 | **拒否理由の分類** | 類似度、インタラクション欠落、不正HTML等を分類して追跡 |

### 3-2. フィードバックループのエコーチェンバー対策

Curator ↔ Generator のループは有用だが、放置すると「昨日の苦情に過剰適合」するリスクがある。

対策:
- curator feedbackは「一つの入力」として扱い、プロンプト全体にしない
- 70% roadmap追従 / 30% 新規探索の予算配分
- feedbackに期限を設定（6 drafts後に減衰）
- 時折「逆説的brief」を挿入（同じ旗艦だが異なる rendering/data family）
- ハード制約とテイスト提案を分離

```json
{
  "hardRequirements": ["pointer interaction", "non-null scores"],
  "temporaryAvoid": ["canvas-only", "3-phase timer"],
  "creativeSuggestion": "try damaged text ledgers with irreversible filing decisions",
  "expiresAfterDrafts": 6
}
```

### 3-3. approaches-tried log（ジェネレーターの記憶）

blocked motifsだけでなく、**試したアプローチ全体**を追跡する:

- 各draftの `renderingMode` + `dataModel` + `interactionModel` の組み合わせを記録
- 直近N件の組み合わせを低優先度化（完全ブロックではなく）
- 週次roadmapレビューで「試したアプローチ」を評価

### 3-4. 参考になるアーキテクチャパターン

Codexが推奨したパターン:
- **Grammar-based generation** — バリエーションを体系的に生成
- **Constraint satisfaction** — 「許容される解空間」を定義してランダムサンプリング
- **Progressive refinement** — 粗いspec → 詳細化 → 実装 → 評価の段階的精製
- **Mutation operators** — 遺伝的アルゴリズム的に「変異演算子」を定義（追加、削除、置換、組み替え）

---

## 4. 現行 vs 改善後 比較

| 項目 | 現行 (v1) | 改善後 (v2) |
|------|-----------|-------------|
| 生成方式 | 静的JS `hour % 3` | LLM駆動（spec → HTML のハイブリッド） |
| テンプレート | 常に同一HTML | 毎回異なる構造的アプローチ |
| インタラクション | なし（必須違反） | ポインター必須 + ランタイム検証 |
| スコアリング | 全件 `null` | LLMが4軸スコアリング |
| 重複検出 | なし | テキスト/AST/フィンガープリントの3層 |
| Curator負担 | クローン検知が最初の壁 | パイプライン側で事前拒否 |
| 拒否追跡 | なし | 理由分類付きで `lab/rejected/` に保存 |
| リトライ | なし | max 3回 |
| 記憶 | blocked motifsのみ | approaches-tried log |
| フィードバック | 片方向（Curator → 人間） | 双方向 + セーフガード |

---

## 5. 実装優先順位

| 優先度 | 内容 | 概要 |
|--------|------|------|
| **P0 最優先** | cron停止 + LLM駆動生成器 | 現在の静的JSを止め、spec → HTML のハイブリッド生成に切り替え |
| **P1** | 類似度チェック + 自動スコアリング | 3層検証 + LLMスコアリング |
| **P2** | フィードバックループ + approaches-tried | Curator ↔ Generator の双方向化 + 記憶 |
| **P3** | ランタイムバリデーション (Playwright) | ページロード + pointer event検証 |

**P0の具体的手順:**
1. 現在のcron（`e41e47e1`）を一時停止
2. OpenClaw subagentベースの生成器を実装
3. spec生成 → spec検証 → HTML生成 のフローを検証
4. 動作確認してcron再開

---

## 6. Mira & Codex の合意事項

1. ✅ 現在の静的JS生成器をLLM駆動に置き換える
2. ✅ ハイブリッドアプローチ（spec → HTML）を採用
3. ✅ レイヤード類似度チェックを実装
4. ✅ ランタイムバリデーション（Playwright）を追加
5. ✅ フィードバックループにセーフガードを実装
6. ✅ approaches-tried logで記憶を持つ
7. ✅ reject理由の分類を実装
8. ✅ 失敗時リトライ予算（max 3回）を設定

---

*作成: 2026-05-18 00:06 JST*
