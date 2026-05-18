# Mira Lab改善計画 — Codex再検討メモ

- 日時: 2026-05-18 00:25 JST
- 依頼: 「候補なし」が続かないように、いきなり修正せず改善方針を検討する
- 対象:
  - `/Users/naokitomono/.openclaw/workspace/scripts/mira-hourly-lab-cycle.js`
  - `/Users/naokitomono/.openclaw/workspace/scripts/mira-curation-candidates.js`
  - `/Users/naokitomono/.openclaw/workspace/scripts/mira-daily-curator.js`
  - `/Users/naokitomono/Documents/generative-art-by-mira/mira-memory/roadmap.md`
  - `/Users/naokitomono/Documents/generative-art-by-mira/mira-memory/daily-curation/2026-05-17.md`

## 結論

Miraの3段階案は方向として正しい。

ただし、単に `mira-hourly-lab-cycle.js` を「LLMにHTMLを書かせるスクリプト」に置き換えるだけでは不十分。今回の根本原因は「LLM未使用」だけではなく、**draftが満たすべき契約、検証、拒否導線がないこと**。そのため、改善は「生成器の置換」ではなく「Lab生成パイプラインの契約化」として進めるべき。

推奨する実装方針は、**spec生成 → spec検証 → HTML生成 → 静的検証 → 最小ランタイム検証 → 採点 → drafts/rejected振り分け**。

## 確認した現状

### hourly生成器

`mira-hourly-lab-cycle.js` は報告通り、決定的テンプレート生成器だった。

- `chooseBrief()` が3テーマを配列で持つ
- `Number(nowParts.hour) % themes.length` でテーマを選ぶ
- `makePrototypeHtml()` が毎回同じCanvas HTMLを返す
- レコード数は `Array.from({ length: 18 })` 固定
- 状態変化は `phaseFor(time)` の3フェーズタイマー
- pointer/touch/click/drag系の構造的インタラクションがない
- `evaluation.json` の各スコアは `null`

Curatorの `no_candidate` 判定は妥当。

### roadmap

`mira-memory/roadmap.md` は既に正しい方向を示している。

- fixed 3-template rotation を止める
- pointer interaction を必須化
- duplicate detection を入れる
- scored evaluations を必須化
- 旗艦更新は scored draft からのみ行う

問題はroadmapではなく、roadmapを生成器が強制していないこと。

### 既存レビュー

`lab-improvement-review-2026-05-17.md` には、MiraとCodexの検討結果としてかなり良い計画が保存済み。

今回の再検討で補正すべき点は、**Playwright等のランタイム検証を「将来」ではなく初版から最小限入れること**。pointer interaction は静的文字列チェックや自己申告では簡単にすり抜ける。

## Mira案への評価

### Phase 1: 生成器をLLM駆動にする

賛成。ただし「LLMが直接HTMLを毎回書く」だけだと、別のテンプレート癖やプロンプト過適合に落ちる可能性がある。

改善案:

1. 最初にLLMへ `experiment-spec.json` を作らせる
2. specに `renderingMode`, `dataModel`, `interactionModel`, `stateModel`, `recordCountStrategy`, `forbiddenPatterns` を必須化する
3. spec検証を通ったものだけHTML生成へ進める
4. 生成HTMLにもspecとの整合性を検証する

### Phase 2: 重複検出＆自動スコアリング

賛成。これはPhase 1と同時に最小版を入れるべき。

理由:

- 重複検出なしでLLM生成を始めると、同じ失敗を「自然言語で違うだけ」の形で再発する
- スコアが `null` のdraftを許すと、Curatorが毎日同じ理由で止まる

初版では高度なASTや画像hashまでは不要。まずは以下で十分。

- 正規化HTML/JSテキストのshingle類似度
- 静的特徴量fingerprint
- `evaluation.json` の非nullスコア強制

### Phase 3: Curator ↔ 生成器フィードバックループ

賛成。ただしそのまま入れるとエコーチェンバー化する。

Curatorの指摘は「制約」「一時回避」「創作提案」に分けるべき。

例:

```json
{
  "hardRequirements": ["pointer interaction", "non-null scores"],
  "temporaryAvoid": ["canvas-only", "3-phase timer", "fixed 18 records"],
  "creativeSuggestion": "damaged textual ledgers with irreversible archive decisions",
  "expiresAfterDrafts": 6
}
```

## 推奨アーキテクチャ

### 1. Context Load

読み込むもの:

- `mira-memory/roadmap.md`
- `mira-memory/motifs.json`
- `mira-memory/latest-curation.json`
- 直近draftの `spec.json`, `prototype.html`, `evaluation.json`
- 新設する `mira-memory/approaches-tried.jsonl`

### 2. Spec Generation

LLMにHTMLではなく、まず構造化specを作らせる。

必須フィールド:

- `title`
- `hypothesis`
- `renderingMode`
- `dataModel`
- `recordCountStrategy`
- `interactionModel`
- `requiredEvents`
- `stateModel`
- `visualLanguage`
- `forbiddenPatterns`
- `expectedStructuralChange`

禁止:

- fixed 18 records
- 3 phase timer
- pointerなし
- score null
- template rotation
- generic particle flow

### 3. Spec Validation

機械的に拒否する条件:

- 必須フィールド欠落
- `requiredEvents` に pointer/click/touch/drag 系がない
- `recordCountStrategy` が固定18件相当
- `interactionModel` が装飾のみ
- 直近N件と同じ `renderingMode + dataModel + interactionModel`

失敗時は最大3回だけ再生成する。

### 4. HTML Generation

検証済みspecを入力として、自己完結HTMLを生成する。

出力要件:

- `prototype.html`
- `brief.md`
- `spec.json`
- `evaluation.json`

### 5. Static Validation

HTML生成後に確認する。

- pointer/click/touch/drag event listener の存在
- localStorage使用の有無、または状態更新処理の存在
- 固定18配列、3フェーズタイマー、既存テンプレートの文字列一致
- normalized similarity > 0.80 ならreject
- feature fingerprint が直近draftと同一ならreject

### 6. Minimal Runtime Validation

初版から入れる。重いビジュアル評価ではなく、最低限の実行確認。

- ローカルHTMLをブラウザで開ける
- console error がない
- 初期スクリーンショットが空白ではない
- pointer/click/drag を1回発火させる
- 発火前後でDOM、localStorage、canvas pixels、またはSVG属性に差分が出る

ここを入れないと「pointer handlerという文字列だけあるが何も変わらないdraft」が通る。

### 7. Scoring

`evaluation.json` は必ず非nullにする。

最低限:

- `visual_score`: 1-5
- `novelty_score`: 1-5
- `interaction_score`: 1-5
- `stability_score`: 1-5
- `curation_readiness`: `reject | draft | candidate`
- `notes`

最初はLLM自己評価でもよいが、低スコアを自動rejectできるようにする。

### 8. Output Routing

合格:

- `lab/drafts/YYYY-MM-DD/HHMM-slug/`

不合格:

- `lab/rejected/YYYY-MM-DD/HHMM-slug/`
- `rejection-reason.json`

Curatorには原則として合格draftだけを渡す。拒否ログは週次改善用に使う。

## 実装順序

### Step 0: 一時停止

現在のhourly固定テンプレート生成は止める。止めない場合、次のCuratorも同じ `no_candidate` になる。

### Step 1: Contractとvalidatorを先に作る

最初に `spec` と `evaluation` の必須形を決める。

この段階ではLLM生成器を完全実装しなくてもよい。既存draftをvalidatorに通して、現在のテンプレートが確実にrejectされることを確認する。

### Step 2: LLM spec generation

LLMにはまずspecだけを生成させる。

3回失敗したら `lab/rejected` に「生成失敗」として記録し、draftを作らない。

### Step 3: LLM HTML generation

承認済みspecからHTMLを生成する。

### Step 4: Static + minimal runtime validation

ここまで通ったものだけ `lab/drafts` に入れる。

### Step 5: Curator入力を合格draft中心に変更

`mira-curation-candidates.js` は、reject済みやscore不足を候補から外し、Curatorが「選ぶ価値のある候補」だけを見るようにする。

### Step 6: Feedback loop

`latest-curation.json` の内容を次回生成に入れる。ただし期限付き・分類済みフィードバックにする。

## すぐ直さないほうがよいこと

- いきなり旗艦作品を更新しない
- 既存12件のdraftから無理に候補を選ばない
- Curatorの基準を下げない
- LLMに自由HTMLだけを投げて解決したことにしない
- 高度な画像hashやAST類似度から始めない

## 最小成功条件

次の24時間で以下を満たすこと。

- 生成draftが12件中少なくとも8件は構造的に異なる
- 全draftに非nullスコアがある
- 全draftに意味のあるpointer/touch/click/drag interactionがある
- 直近draftとの類似度が0.80未満
- Curatorが少なくとも1件を `candidate` として扱える

## Codexの推奨

Miraの方向性は採用してよい。ただし、実装計画は次のように修正する。

1. Phase 1を「LLM駆動化」ではなく「spec契約 + LLM生成 + validator」にする
2. Phase 2の重複検出とスコア非null化はPhase 1と同時に最小実装する
3. ランタイム検証は将来ではなく初版から最小版を入れる
4. Curator feedbackは期限付き・分類済みにして、過適合を避ける
5. 合格draftだけをCurator候補に流し、rejectは改善ログとして残す

この順序なら、「候補なし」を減らすだけでなく、質の低い候補を無理に選ぶ圧力も避けられる。
