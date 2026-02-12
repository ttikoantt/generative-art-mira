# AEM Universal Editor 調査レポート

**調査日:** 2026年2月13日
**調査者:** Mira (AI Assistant)
**目的:** AEM Universal Editorの実装形式とデザインパターンを調査し、レポートとしてまとめる

---

## 1. 概要

AEM (Adobe Experience Manager) Universal Editorは、Adobe Experience Manager as a Cloud Serviceで提供される次世代のコンテンツ編集エディターで、あらゆる実装のあらゆるコンテンツを編集できるユニバーサルなソリューションです。

**主な特徴:**
- 直感的なUIで最小限のトレーニングで利用可能
- インプレイス編集が可能
- Edge Delivery Servicesとの統合で100% Core Web Vitalsスコアを実現
- AEMの強力なコンテンツ管理機能（MSM、翻訳、Launches等）と連携

---

## 2. URL調査結果

### 調査したURL

| URL | ステータス | メモ |
|-----|----------|------|
| `https://www.aem.live/docs/edge-delivery` | ❌ 404 | 存在しない |
| `https://www.aem.live/docs/aem-authoring` | ✅ 200 | AEMでのオーサリングガイド |
| `https://www.aem.live/developer/keeping-it-100` | ✅ 200 | パフォーマンス最適化ガイド |
| `https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/universal-editor/architecture` | ✅ 200 | アーキテクチャ説明 |
| `https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/universal-editor/attributes-types` | ✅ 200 | HTML属性とタイプ |

### 関連ドキュメント

- **AEM Authoring:** https://www.aem.live/docs/aem-authoring
- **Keeping it 100:** https://www.aem.live/developer/keeping-it-100
- **Universal Editor Architecture:** https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/universal-editor/architecture
- **Attributes and Types:** https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/universal-editor/attributes-types

---

## 3. Universal Editorの実装形式

### 3.1 アーキテクチャ

Universal Editorは4つの主要なビルディングブロックで構成されています：

#### 1. **Editors（エディター）**
- **Universal Editor本体:** インストルメンテーションされたDOMを使用してインプレイス編集を可能にする
- **Properties Panel:** コンテキスト外編集に使用されるフォームベースのエディター（カルーセルの回転時間等）

#### 2. **Remote App（リモートアプリ）**
- Universal Editorでインプレイス編集可能にするため、DOMをインストルメンテーションする必要がある
- SDKは最小限で、インストルメンテーションはアプリ実装の責任

#### 3. **API Layer（APIレイヤー）**
- **Content Data:** コンテンツデータのソースシステムや消費方法は重要ではなく、必要な属性を定義・提供することが重要
- **Persisting Data:** 編集可能なデータごとにURN識別子があり、正しいシステムとリソースへのルーティングに使用される

#### 4. **Persistence Layer（持続性レイヤー）**
- **Content Fragment Model:** コンポーネントおよびコンテンツフラグメントごとのモデルが必要
- **Content:** AEM、Magento等、どこにでも格納可能

### 3.2 サービスディスパッチ

Universal Editorは、コンテンツ変更をすべて**Universal Editor Service**と呼ばれる集中サービスにディスパッチします。

- Adobe I/O Runtime上で実行される
- Extension Registryからプラグインをロード
- プラグインはバックエンドとの通信と統一されたレスポンスの返却を担当

---

## 4. HTML属性とデータタイプ

Universal EditorはDOMに特定の属性を追加することで、編集可能なコンテンツを識別します。

### 4.1 主要な属性

| 属性 | 説明 | 必須性 |
|------|------|--------|
| `data-aue-type` | 編集可能なコンテンツの種類（text, richtext, media, container, component, reference） | 必須 |
| `data-aue-resource` | コンテンツ変更の書き込み先を示すURN識別子 | 必須 |
| `data-aue-prop` | プロパティ識別子（インプレイス編集時に必須） | 条件付き必須 |
| `data-aue-filter` | アセットや参照のフィルタリング基準 | 任意 |
| `data-aue-label` | コンテンツのラベル表示 | 任意 |
| `data-aue-model` | Content Fragment Modelの識別子 | 任意 |

### 4.2 データタイプ

| タイプ | 説明 | 必須属性 |
|--------|------|----------|
| **text** | 単純なテキスト形式（リッチテキストなし）| `data-aue-resource`, `data-aue-prop` |
| **richtext** | 完全なリッチテキスト機能付きテキスト | `data-aue-resource`, `data-aue-prop` |
| **media** | アセット（画像やビデオ等）| `data-aue-resource`, `data-aue-prop`, `data-aue-filter`（任意）|
| **container** | コンポーネントのコンテナ（Paragraph System）| `data-aue-resource`, `data-aue-prop`（条件付き）, `data-aue-filter`（任意）|
| **component** | コンポーネント（移動/削除可能なDOM部分）| `data-aue-resource` |
| **reference** | 参照（Content Fragment、Experience Fragment、製品等）| `data-aue-resource`, `data-aue-prop`, `data-aue-filter`（任意）, `data-aue-model`（任意）|

---

## 5. デザインパターン分類

### 5.1 編集体験パターン

#### **A. テキスト編集**
- **タイプ:** `text`, `richtext`
- **UI:** インプレイスダブルクリックで編集開始
- **フィーチャー:**
  - `text`: 単純なテキスト入力
  - `richtext`: リッチテキストエディター（フォーマットオプション付き）
  - 自動保存（フォーカスが離れると保存）

#### **B. メディア編集**
- **タイプ:** `media`
- **UI:** Properties Panelからアセットセレクターを起動
- **フィーチャー:**
  - 画像/ビデオの選択と置換
  - フィルタリング基準でアセット検索可能

#### **C. コンテナ管理**
- **タイプ:** `container`
- **UI:** コンテナ内にコンポーネントを追加・削除・再配列
- **フィーチャー:**
  - コンポーネントの追加・複製・削除
  - ドラッグ＆ドロップで再配列
  - Content Treeモードで階層的に管理

#### **D. コンポーネント操作**
- **タイプ:** `component`
- **UI:** コンテキストメニューから移動・削除・複製
- **フィーチャー:**
  - コンテキストメニュー（右クリック）からの操作
  - ホットキーによる素早い操作（例: `a`で追加、`Command-C/V`でコピー＆ペースト）

#### **E. 参照編集**
- **タイプ:** `reference`
- **UI:** Properties Panelで参照先を選択
- **フィーチャー:**
  - Content Fragment、Experience Fragment、製品等の参照
  - フィルタリング基準で参照先を検索可能
  - Content Fragment Editorで直接編集も可能

### 5.2 拡張フィーチャー（Extension Managerで有効化）

| 拡張 | 機能 |
|------|------|
| **AEM Multi-Site-Management (MSM) Extension** | 継承の状態を表示・変更（継承の解除・再設定）|
| **AEM Page Properties Extension** | 現在編集中のページのページプロパティに素早くアクセス |
| **AEM Site Admin Extension** | Sites Consoleでページを管理 |
| **AEM Page Lock Extension** | ページのロック・アンロック |
| **AEM Workflows Extension** | ワークフローの開始 |
| **Generate Variations Extension** | 生成AIでコンテンツのバリエーションを作成 |
| **Developer Login Extension** | ローカルAEM SDKでの開発者ログイン |

---

## 6. パフォーマンス最適化（Edge Delivery Services）

### 6.1 Three-Phase Loading（E-L-D）戦略

#### **Phase E: Eager（LCP達成）**
- 目的: Largest Contentful Paint (LCP) を達成
- 内容:
  - DOMのデコレーション（CSSクラスの追加）
  - 最初のセクションとLCP候補（最初の画像）を優先読み込み
  - フォントはLCP後に非同期読み込み
- 重要: LCP前のペイロードは100kb以下に抑える

#### **Phase L: Lazy（遅延読み込み）**
- 目的: Total Blocking Time (TBT) に影響しない読み込み
- 内容:
  - 次のセクションとそのブロック
  - 残りの画像（`loading="lazy"`属性付き）
  - 非ブロッキングなJavaScriptライブラリ

#### **Phase D: Delayed（遅延サードパーティ）**
- 目的: 経験に直接影響しないサードパーティタグ等の読み込み
- 内容:
  - マーケティングツール、同意管理、拡張分析等
  - **重要:** LCPイベント後少なくとも3秒遅延させる

### 6.2 その他の最適化手法

| 手法 | 説明 |
|------|------|
| **ヘッダー＆フッターの非同期読み込み** | LCPのクリティカルパスに含まれないため非同期で読み込み |
| **ウェブフォントの遅延読み込み** | LCP直後に読み込み、フォントフォールバック手法でCLS回避 |
| **単一オリジンからの配信** | LCP前の複数オリジン接続はパフォーマンスに悪影響 |
| **リダイレクト回避** | 複数回のリダイレクトはCore Web Vitalsを悪化 |

---

## 7. 技術スタック

### 7.1 レンダリングパイプライン

Universal Editorは以下のレンダリング方式に対応：

1. **Server Side Rendering (SSR)**
2. **Static Site Generation (SSG)**
3. **Client Side Rendering (CSR)**

### 7.2 Edge Delivery Servicesの特徴

- **100% Core Web Vitalsスコア**を目指す設計
- **AEM Boilerplate**を使用すると開発当初から100スコアを実現
- プルリクエストごとにPageSpeed Insights Serviceで自動テスト
- スコアが100未満の場合、プルリクエストを失敗させる

---

## 8. 結論

### 8.1 Universal Editorの強み

1. **統一的編集体験:** あらゆる実装のあらゆるコンテンツを単一のエディターで編集可能
2. **開発者体験:** 最小限のSDK、DOMベースのインストルメンテーションで柔軟な実装
3. **パフォーマンス:** Edge Delivery Servicesとの統合で100% Core Web Vitalsを実現
4. **拡張性:** Extension Managerで機能拡張が可能

### 8.2 技術的洞察

- **属性ベースのインストルメンテーション:** HTML属性を追加するだけで編集可能に
- **URNベースのルーティング:** 変更を適切なバックエンドシステムにルーティング
- **プラグイン可能なバックエンド:** Universal Editor Service経由で様々なシステムに対応可能

### 8.3 デザインパターン

- **コンテキスト依存のUI:** 選択したコンテンツタイプに応じて適切な編集体験を提供
- **プレビューモード:** 編集とナビゲーションを切り替え可能
- **ホットキー:** よく使う操作はキーボードショートカットで素早く実行可能

---

## 9. 関連リソース

- [AEM Universal Editor Documentation](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/universal-editor/authoring)
- [AEM Boilerplate](https://github.com/adobe/aem-boilerplate)
- [Adobe Developer - Extension Manager](https://developer.adobe.com/uix/docs/extension-manager/)
- [Core Web Vitals](https://web.dev/explore-learn-core-vitals/)

---

*本レポートはMira (AI Assistant) によって作成されました。*
