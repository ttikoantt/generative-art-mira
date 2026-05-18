# Mira Lab v2 — 改善アーキテクチャ

**作成日:** 2026-05-18
**レビュー:** Mira + Codex CLI

---

## 全体フロー

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

---

## 各ステップの詳細

### 1. Context Load

毎時のサイクル開始時に以下を読み込む:

| ファイル | 用途 |
|----------|------|
| `roadmap.md` | 週次の方向性、必須要件、ブロック済みmotif |
| `motifs.json` | active/blocked motif一覧 |
| `latest-curation.json` | Curatorの最新フィードバック |
| `approaches-tried.jsonl` | 直近N件の試行アプローチ記録 |

---

### 2. Spec Generation (LLM)

LLMが構造化JSON specを生成する。フルHTMLではなく、まず「何を作るか」を定義。

**生成ルール:**
- 70% は roadmap + curator feedback に従う
- 30% は新しい構造的アプローチを探索
- curator feedback は期限付き（N drafts後に減衰）

**specの例:**
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

---

### 3. Spec Validation

LLMが生成したspecを、コードが存在する前に検証する。

**チェック項目:**
- 必須フィールドの存在確認
- `forbiddenPatterns` との一致チェック
- 直近specとの類似度チェック
- `approaches-tried` との重複確認

**リトライ:**
- max 3回まで再生成可能
- 3回失敗 → rejection reportを書いて終了

---

### 4. HTML Generation (LLM)

承認済みspecからフルHTMLを生成。

**要件:**
- 自己完結型の単一HTMLファイル
- specで定義されたrenderingMode/interactionModel/stateModelを忠実に実装
- forbiddenPatternsを含まない

---

### 5. Artifact Validation

生成されたHTMLを多層で検証。

**レイヤー:**

| レイヤー | 手法 | しきい値 |
|----------|------|----------|
| 正規化テキスト類似度 | ID/タイムスタンプ/空白/コメント除去後のshingle比較 | >0.80 → reject |
| AST類似度 | Babel/Acornでパース、識別子/リテラル正規化後のノード比較 | >0.75 → reject |
| フィーチャーフィンガープリント | canvasCount, svgCount, eventListenerTypes等の比較 | 同一→reject |
| ランタイム検証 | Playwrightでロード確認、pointer event発火で状態変化確認 | エラー→reject |

---

### 6. Scoring (LLM)

合格したHTMLに対してLLMがスコアリング。

**スコア項目:**
- `visual_score` (1-5): 視覚的品質
- `novelty_score` (1-5): 新規性
- `interaction_score` (1-5): インタラクションの質
- `stability_score` (1-5): 安定性

**品質ゲート:**
- visual_score ≥ 3 かつ novelty_score ≥ 3 で合格
- 不通過 → `lab/rejected/` に移動

---

### 7. Output

**合格時のディレクトリ構造:**
```
lab/drafts/YYYY-MM-DD/HHMM-slug/
├── brief.md          # 実験の説明
├── spec.json         # 構造化spec
├── prototype.html    # 生成されたHTML
└── evaluation.json   # スコア付き評価
```

**拒否時のディレクトリ構造:**
```
lab/rejected/YYYY-MM-DD/HHMM-slug/
├── rejection-reason.json  # 拒否理由（分類付き）
└── prototype.html         # 参考用に保持
```

**拒否理由の分類:**
- `similarity_too_high` — 直近draftとの類似度超标
- `missing_interaction` — ポインターインタラクション欠落
- `invalid_html` — HTMLパースエラー
- `runtime_error` — Playwright検証失敗
- `low_scores` — スコアリング不合格
- `max_retries_exceeded` — リトライ予算枯渇

---

## フィードバックループ（セーフガード付き）

```
┌──────────────┐     nextExperimentPrompt     ┌──────────────┐
│   Curator    │ ─────────────────────────────→│  Generator   │
│  (Daily)     │                               │  (Hourly)    │
└──────────────┘                               └──────┬───────┘
       ↑                                              │
       │              scores + approach log            │
       └──────────────────────────────────────────────┘
```

**エコーチェンバー防止:**
- curator feedbackは「一つの入力」として扱い、プロンプト全体にしない
- 70% roadmap追従 / 30% 新規探索の予算配分
- feedbackに期限を設定（6 drafts後に減衰）
- 時折「逆説的brief」を挿入（同じ旗艦だが異なるrendering/data family）

**feedbackオブジェクトの例:**
```json
{
  "hardRequirements": ["pointer interaction", "non-null scores"],
  "temporaryAvoid": ["canvas-only", "3-phase timer"],
  "creativeSuggestion": "try damaged text ledgers with irreversible filing decisions",
  "expiresAfterDrafts": 6
}
```

---

## 現行との比較

| 項目 | 現行 (v1) | 改善後 (v2) |
|------|-----------|-------------|
| 生成方式 | 静的JS `hour % 3` | LLM駆動（spec → HTML） |
| テンプレート | 常に同一HTML | 毎回異なる構造的アプローチ |
| インタラクション | なし（必須違反） | ポインター必須 + ランタイム検証 |
| スコアリング | 全件 `null` | LLMが4軸スコアリング |
| 重複検出 | なし | テキスト/AST/フィンガープリントの3層 |
| Curator負担 | クローン検知が最初の壁 | パイプライン側で事前拒否 |
| 拒否追跡 | なし | 理由分類付きで `lab/rejected/` に保存 |
| リトライ | なし | max 3回 |
| 記憶 | blocked motifsのみ | approaches-tried log |

---

## 実装優先順位

1. **最優先:** 現在のcron停止 → LLM駆動生成器（spec → HTML + spec validation）
2. **次:** 類似度チェック + 自動スコアリング
3. **その後:** フィードバックループ + approaches-tried log
4. **将来:** ランタイムバリデーション（Playwright）
