# AEM Universal Editor 調査レポート

**調査日:** 2026年2月13日  
**目的:** Universal Editorの実装形式とデザインパターンの調査・分類

---

## 📋 目次

1. [Universal Editorの概要](#universal-editorの概要)
2. [技術的アーキテクチャ](#技術的アーキテクチャ)
3. [実装形式の分類](#実装形式の分類)
4. [デザインパターンの分類](#デザインパターンの分類)
5. [主要な機能と特徴](#主要な機能と特徴)
6. [ベストプラクティス](#ベストプラクティス)
7. [関連リソース](#関連リソース)

---

## Universal Editorの概要

### 定義

Universal EditorはAdobe Experience Manager (AEM)のモダンなビジュアルオーサリングツールで、ヘッドレスおよびヘッドフルのどちらの実装でもコンテンツを編集できる統一されたオーサリングエクスペリエンスを提供します。

### 主な特徴

- **WYSIWYG編集**: プレビュー内で直接コンテンツを編集
- **プラットフォーム独立**: SSR、CSR、Next.js、React、Astroなど主要なフレームワークと互換
- **統合されたワークフロー**: AEMのワークフロー、MSM、翻訳、Launchesと完全統合
- **拡張性**: UI拡張、カスタムデータタイプ、イベントによる拡張
- **AI統合**: Generate Variations機能によるAI活用

### サポートされているAEMバージョン

- **AEM as a Cloud Service**: Release 2023.8.13099以上（推奨）
- **AEM 6.5 LTS**: オンプレミス・AMS対応
- **AEM 6.5**: オンプレミス・AMS対応

---

## 技術的アーキテクチャ

### 4つの構成要素

```
┌─────────────────────────────────────────────────────┐
│            Universal Editor                        │
│  ┌──────────────┐      ┌───────────────┐     │
│  │   Editors     │      │ Remote App    │     │
│  │  - Universal  │      │ (Instrumented)│     │
│  │    Editor     │      │      DOM       │     │
│  │  - Properties │      └───────────────┘     │
│  │    Panel      │              ↑               │
│  └──────────────┘              │               │
└──────────────────────────────────────┼───────────────┘
                                   │ data-aue-* 
                           ┌───────┴────────┐
                           │  API Layer     │
                           │  - Content     │
                           │    Data        │
                           │  - Persistence  │
                           └───────┬────────┘
                                   │ URN
                           ┌───────┴────────┐
                           │  Persistence    │
                           │    Layer       │
                           │  - CF Models   │
                           │  - Content     │
                           └────────────────┘
```

#### 1. Editors

**Universal Editor**
- インスツルメンテーションされたDOMを使用したインプレイス編集
- data-aue-*属性で編集可能な領域を識別

**Properties Panel**
- コンテキスト編集が難しいプロパティ用のフォームベースエディタ
- 右パネルに表示

#### 2. Remote App

- DOMに特定の属性をレンダリングすることでUniversal Editorと統合
- インスツルメンテーションは実装の責任
- 最小限のSDK

#### 3. API Layer

**Content Data**
- コンテンツデータのソースや消費方法は重要ではない
- 必要な属性を定義して提供することが重要

**Persisting Data**
- 編集可能なデータごとにURN識別子を持つ
- URNを使用して正しいシステムとリソースにルーティング

#### 4. Persistence Layer

**Content Fragment Model**
- コンテンツフラグメントプロパティ編集のためのモデル

**Content**
- AEM、Magentoなど任意の場所に保存可能

---

## 実装形式の分類

### 1. Edge Delivery Services（推奨）

**特徴:**
- 最もシンプルで高速
- 短いTime-to-Value
- 最高のパフォーマンス
- AEMがHTMLをレンダリング
- Edge Delivery Servicesが配信

**利点:**
- 100% Core Web Vitalsスコア
- 既存のAEM機能を完全に活用
- 複雑な設定不要

**URL:**
- https://www.aem.live/docs/edge-delivery

### 2. Headless Implementations

**特徴:**
- 既存のヘッドレスプロジェクトに対応
- 特定の要件がある場合
- SSR、CSR、Next.js、React、Astroなどに対応
- "Bring Your Own App"モデル

**利点:**
- 既存プロジェクトの完全な再構築が不要
- フレームワークの自由度
- 柔軟なホスティングモデル

**使用ケース:**
- 既存のヘッドレスプロジェクト
- 特定の技術要件がある場合
- デカップリングされた実装が必要な場合

---

## デザインパターンの分類

### ブロックシステムの構造

Edge Delivery Servicesは以下の階層構造を採用：

```
セクション（Sections）
├─ デフォルトコンテンツ（Default Content）
│  ├─ 見出し（H1-H6）
│  ├─ 段落（Text）
│  ├─ 画像（Images）
│  ├─ リスト（Lists）
│  └─ リンク（Links）
│
└─ ブロック（Blocks）
   ├─ AEM Boilerplate（標準ブロック）
   └─ Block Collection（共通ブロック）
```

### 1. デフォルトコンテンツ（Default Content）

**概要:**
- Word、Google Docs、Markdown、HTML間で共有されるセマンティックモデル
- 著者が自然に扱える要素

**主なタイプ:**

| タイプ | 説明 | タグ |
|--------|--------|------|
| 見出し | 段落構造のセマンティックバックボーン | h1-h6 |
| テキスト | リッチなセマンティックフォーマット | p, div |
| 画像 | コンテンツに命を吹き込む | picture |
| リスト | 順序付き・順序なしリスト | ul, ol |
| リンク | 他のウェブサイトや自コンテンツへの参照 | a |
| ボタン | コール・トゥ・アクション | button |
| コード | コードスニペットのハイライト | pre, code |

### 2. セクション（Sections）

**概要:**
- コンテンツを視覚的にグループ化
- 背景色の変更などが主な使用例

**特徴:**
- Section Metadataでデータ属性を追加
- StyleプロパティがCSSクラスに変換

### 3. ブロック（Blocks）

**AEM Boilerplate（標準ブロック）**
- ほとんどのAEMプロジェクトで使用
- aem-boilerplateレポジトリでオープンソース

| ブロック名 | 説明 |
|-----------|--------|
| **Hero** | ページトップのヒーローセクション |
| **Columns** | レスポンシブなマルチカラムレイアウト |
| **Cards** | 画像付き/なしのカードリスト |
| **Header** | フレキシブルなヘッダーとナビゲーション |
| **Footer** | シンプルで拡張可能なフッター |

**Block Collection（共通ブロック）**
- 半数以上のプロジェクトで使用
- aem-block-collectionレポジトリ

| ブロック名 | 説明 | タイプ |
|-----------|--------|--------|
| **Embed** | ソーシャルメディア埋め込み | Block |
| **Fragment** | 複数ページでコンテンツを共有 | Block |
| **Table** | 表形式データの整理 | Block |
| **Video** | AEMからの動画再生・表示 | Block |
| **Accordion** | トグル可能なラベルスタック | Block |
| **Breadcrumbs** | ナビゲーション階層の表示 | Add-on |
| **Carousel** | 画像のスムーズな遷移表示 | Block |
| **Modal** | サイトコンテンツ上のポップアップ | Block |
| **Quote** | 引用・ハイライト表示 | Block |
| **Search** | サイト内コンテンツ検索 | Block |
| **Tabs** | ラベル付きパネル分割 | Block |

### ブロックオプション

**形式:**
- `Block Name (option)`
- 例: `Columns (wide)` → `<div class="columns wide">`
- 複数: `Columns (dark, wide)` → `<div class="columns dark wide">`
- カンマ区切り: 複数クラスとして追加

**利点:**
- 同じブロックでバリエーションを作成可能
- 新しいブロックを作成する必要がない

### Auto Blocking

**概要:**
- デフォルトコンテンツとメタデータをプログラム的にブロックに変換
- 著者が物理的にブロックを作成する必要がない

**使用例:**
- ブログ記事のヘッダー（著者、タイトル、画像、公開日）
- YouTubeリンクを埋め込みブロックに自動変換
- 特定のテンプレートを持つページに共通ブロックを追加

**実装:**
- `scripts.js`の`buildAutoBlocks()`関数
- ブロックロード前に実行

---

## 主要な機能と特徴

### コンテンツ編集機能

| 機能 | 説明 |
|--------|--------|
| **インプレイス編集** | プレビュー内で直接編集（ダブルクリックでテキスト編集） |
| **Properties Panel** | コンテキスト編集が難しいプロパティはパネルで編集 |
| **ドラッグ＆ドロップ** | ブロックの並べ替え |
| **コピー＆ペースト** | コンポーネントをコピーしてペースト（ブラウザタブ間も可能） |
| **Undo/Redo** | セッション内で編集の取り消し・やり直し |

### レイアウト機能

| 機能 | 説明 |
|--------|--------|
| **コンテナ操作** | ブロックの追加、複製、削除、並べ替え |
| **デバイスシミュレーション** | 異なるデバイスでプレビュー |
| **テンプレート** | ページテンプレートの使用 |
| **ビジュアルスタイル** | ブロックオプションによるスタイル変更 |

### 統合機能

| 機能 | 説明 |
|--------|--------|
| **ワークフロー統合** | AEMワークフローの開始・管理 |
| **MSM（継承）** | 継承のステータス表示・解除・再適用 |
| **ローカライゼーション** | Multi-Site Managerによる翻訳ワークフロー |
| **公開** | レビュー・承認・出版の統合ワークフロー |

---

## データ属性とタイプ

### 必須・オプション属性

| タイプ | data-aue-type | 必須 | 説明 |
|--------|---------------|------|--------|
| **text** | text | resource | シンプルテキスト（見出しなど） |
| **richtext** | richtext | resource, prop | リッチテキスト（RTE使用） |
| **media** | media | resource, (filter) | 画像・動画などのアセット |
| **container** | container | 条件付き | コンポーネントコンテナ |
| **component** | component | resource | 移動・削除可能なコンポーネント |
| **reference** | reference | 条件付き | コンテンツフラグメント参照 |

### 属性の詳細

| 属性 | 説明 |
|--------|--------|
| **data-aue-resource** | コンテンツ変更の書き込み先を示すURN（必須） |
| **data-aue-prop** | プロパティ名（インプレイス編集時は必須） |
| **data-aue-filter** | アセットセレクタへのフィルタ条件（オプション） |
| **data-aue-label** | 著者向けの表示名（オプション） |
| **data-aue-model** | コンテンツフラグメントのモデル情報（オプション） |

---

## ベストプラクティス

### 1. 著者のアーリー・インボルブメント

- プロセスの初期段階で著者を関与
- WordやGoogle Docsでコンテンツを自然に作成させる
- 必要な箇所にのみセクションやブロックを導入

### 2. シンプルさの維持

- 著者にとってシンプルで直感的な構造にする
- 複雑なブロックは著者が使いづらくなる
- ブロックのネストは避ける

### 3. コードのスコープ

- すべてのセレクタをブロッククラスでプレフィックス
- 複雑で脆いセレクタは避ける
- ブロックレベルのCSSはブロックにスコープ

### 4. デカップリング

- 開発者は複雑さを吸収する
- 著者は直感的なオーサリングエクスペリエンスを享受
- 変換はDOMレベルで行う

---

## 制限事項

| 制限 | 説明 |
|------|--------|
| **リソース参照数** | 1ページで最大25個のAEMリソース |
| **サポートされるバックエンド** | AEM as a Cloud Service、AEM 6.5 LTS、AEM 6.5のみ |
| **バージョン要件** | AEM as a Cloud Service: Release 2023.8.13099以上 |
| **アカウント** | 著者は各自のExperience Cloudアカウントが必要 |
| **ブラウザ** | デスクトップブラウザのみ対応（モバイル非対応） |

---

## 関連リソース

### 公式ドキュメント

- **Universal Editor入門**: https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/universal-editor/introduction
- **Universal Editorアーキテクチャ**: https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/universal-editor/architecture
- **属性とタイプ**: https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/universal-editor/attributes-types
- **オーサリングガイド**: https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/universal-editor/authoring

### Edge Delivery Services

- **公式サイト**: https://www.aem.live/
- **ドキュメント**: https://www.aem.live/docs
- **ブロックコレクション**: https://www.aem.live/developer/block-collection
- **マークアップ・セクション・ブロック**: https://www.aem.live/developer/markup-sections-blocks

### GitHubリポジトリ

- **AEM Boilerplate**: https://github.com/adobe/aem-boilerplate
- **Block Collection**: https://github.com/adobe/aem-block-collection
- **ブログ例（Auto Blocking）**: https://github.com/adobe/blog

---

## まとめ

### 主要な発見

1. **Universal Editorは真にユニバーサル**
   - Edge Delivery Services（推奨）とHeadlessの両方をサポート
   - 既存プロジェクトの再構築が不要

2. **ブロックベースの設計**
   - デフォルトコンテンツ＋ブロックのハイブリッドアプローチ
   - 著者にとって自然で、開発者にとって柔軟

3. **最小限のインスツルメンテーション**
   - data-aue-*属性のみで実装可能
   - 実装の複雑さを吸収するアーキテクチャ

4. **拡張性**
   - UI拡張、カスタム拡張、Extension Registry
   - Generate VariationsなどAI機能の統合

### 次のステップ

- 実際の実装例の調査
- パフォーマンス最適化の詳細
- カスタムブロックの開発ガイドライン
- テスト・検証のベストプラクティス

---

**レポート作成者:** Mira (AEM Universal Editor Research Cron Job)  
**最終更新:** 2026年2月13日
