# AEM Universal Editor 調査レポート

**調査日:** 2026年2月13日
**最終更新:** 2026年2月13日 12:50
**調査者:** Mira (AI Assistant)
**目的:** AEM Universal Editorの実装形式とデザインパターンを調査し、レポートとしてまとめる

---

## 更新履歴

| 日時 | 更新内容 |
|------|---------|
| 2026-02-13 07:40 | 初版作成 |
| 2026-02-13 09:42 | 実装手順・Edge Delivery統合・接続設定を追加 |
| 2026-02-13 12:50 | Three-Phase Loading戦略の詳細化・パフォーマンス最適化の追加 |

---

## 1. 概要

AEM (Adobe Experience Manager) Universal Editorは、Adobe Experience Manager as a Cloud Serviceで提供される次世代のコンテンツ編集エディタで、あらゆる実装のあらゆるコンテンツを編集できるユニバーサルなソリューションです。

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
| `https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/universal-editor/authoring` | ✅ 200 | Universal Editorオーサリング |
| `https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/universal-editor/getting-started` | ✅ 200 | 実装スタートガイド |
| `https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/universal-editor/architecture` | ✅ 200 | アーキテクチャ説明 |
| `https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/universal-editor/attributes-types` | ✅ 200 | HTML属性とタイプ |

### 関連ドキュメント

**オーサリング:**
- [AEM Authoring](https://www.aem.live/docs/aem-authoring) - AEMでのオーサリングガイド
- [Universal Editor Authoring](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/universal-editor/authoring) - Universal Editorでのコンテンツ編集

**実装:**
- [Getting Started](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/universal-editor/getting-started) - 実装スタートガイド
- [Universal Editor Architecture](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/universal-editor/architecture) - アーキテクチャ
- [Attributes and Types](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/universal-editor/attributes-types) - HTML属性とタイプ

**最適化:**
- [Keeping it 100](https://www.aem.live/developer/keeping-it-100) - パフォーマンス最適化ガイド

---

## 3. Universal Editorの実装形式

### 3.1 アーキテクチャ

Universal Editorは4つの主要なビルディングブロックで構成されています：

#### 1. **Editors（エディタ）**
- **Universal Editor本体:** インストルメンテーションされたDOMを使用してインプレイス編集を可能にする
- **Properties Panel:** コンテキスト外編集に使用されるフォームベースのエディタ（カルーセルの回転時間等）

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

## 4. 実装手順（Getting Started）

### 4.1 前提条件

Universal Editorを実装するには以下が必要です：

1. **URN (Uniform Resource Name)** スキーマ
   - コンテンツをコンテンツリソースにマップするために必要

2. **CORSライブラリの組み込み**
   - Universal Editorがアプリに接続するために必要

### 4.2 実装ステップ

#### ステップ1: CORSライブラリの組み込み

アプリケーションに以下のスクリプトを追加します：

```html
<script src="https://universal-editor-service.adobe.io/cors.js" async></script>
```

#### ステップ2: コネクションの作成

コネクションはページの`<head>`内の`<meta>`タグとして保存されます。

**基本形式:**
```html
<meta name="urn:adobe:aue:<category>:<referenceName>" content="<protocol>:<url>">
```

**パラメータ説明:**

| パラメータ | 説明 | 値の例 |
|----------|------|--------|
| `category` | コネクションの分類 | `system`（コネクションエンドポイント用）、`config`（設定オプション用）|
| `referenceName` | ドキュメント内で再利用される短い名前 | `aemconnection`, `fcsconnection` |
| `protocol` | Universal Editor Persistence Serviceの持続プラグイン | `aem`, `fcs` |
| `url` | 変更を保持するシステムのURL | `https://localhost:4502` |

**例:**
```html
<meta name="urn:adobe:aue:system:aemconnection" content="aem:https://localhost:4502">
<meta name="urn:adobe:aue:system:fcsconnection" content="fcs:https://example.franklin.adobe.com/345fcdd">
```

#### ステップ3: DOMのインストルメンテーション

編集可能なコンテンツを`data-aue-*`属性でマークアップします。

**基本形式:**
```html
<div data-aue-resource="urn:<referenceName>:<resource>" data-aue-type="<type>">
```

**実装例:**
```html
<aside>
  <ul data-aue-resource="urn:aemconnection:/content/example/list" data-aue-type="container">
    <li data-aue-resource="urn:aemconnection:/content/example/listitem" data-aue-type="component">
      <p data-aue-prop="name" data-aue-type="text">Jane Doe</p>
      <p data-aue-prop="title" data-aue-type="text">Journalist</p>
      <img data-aue-prop="avatar" src="avatar.jpg" data-aue-type="image" alt="avatar"/>
    </li>
  </ul>
</aside>
```

#### ステップ4: 設定オプション（オプション）

**サービスエンドポイントのカスタマイズ:**
```html
<meta name="urn:adobe:aue:config:service" content="<url>">
```

**拡張機能のエンドポイント設定:**
```html
<meta name="urn:adobe:aue:config:extensions" content="<url>,<url>,<url>">
```

### 4.3 エディターの自動起動設定

特定のコンテンツパスまたは`sling:resourceType`に基づいてUniversal Editorを自動的に開くよう設定できます。

**設定手順:**
1. Configuration Managerを開く
2. Universal Editor URL Serviceを選択
3. 以下の設定を行う:
   - **Mappings**: Universal Editorを開くパス
   - **resourceTypes**: 直接開くリソースタイプ
   - **aemdomain**: AEMドメイン下で開くかどうか
   - **editorreleasepreview**: プレビュー環境で開くかどうか

**マッピング変数:**
- `path`: コンテンツパス
- `localhost`, `author`, `publish`, `preview`: Externalizerエントリ
- `env`: 環境変数（prod, stage, dev）
- `token`: 認証トークン

---

## 5. HTML属性とデータタイプ

Universal EditorはDOMに特定の属性を追加することで、編集可能なコンテンツを識別します。

### 5.1 主要な属性

| 属性 | 説明 | 必須性 |
|------|------|--------|
| `data-aue-type` | 編集可能なコンテンツの種類（text, richtext, media, container, component, reference） | 必須 |
| `data-aue-resource` | コンテンツ変更の書き込み先を示すURN識別子 | 必須 |
| `data-aue-prop` | プロパティ識別子（インプレイス編集時に必須） | 条件付き必須 |
| `data-aue-filter` | アセットや参照のフィルタリング基準 | 任意 |
| `data-aue-label` | コンテンツのラベル表示 | 任意 |
| `data-aue-model` | Content Fragment Modelの識別子 | 任意 |

### 5.2 データタイプ

| タイプ | 説明 | 必須属性 |
|--------|------|----------|
| **text** | 単純なテキスト形式（リッチテキストなし）| `data-aue-resource`, `data-aue-prop` |
| **richtext** | 完全なリッチテキスト機能付きテキスト | `data-aue-resource`, `data-aue-prop` |
| **media** | アセット（画像やビデオ等）| `data-aue-resource`, `data-aue-prop`, `data-aue-filter`（任意）|
| **container** | コンポーネントのコンテナ（Paragraph System）| `data-aue-resource`, `data-aue-prop`（条件付き）, `data-aue-filter`（任意）|
| **component** | コンポーネント（移動/削除可能なDOM部分）| `data-aue-resource` |
| **reference** | 参照（Content Fragment、Experience Fragment、製品等）| `data-aue-resource`, `data-aue-prop`, `data-aue-filter`（任意）, `data-aue-model`（任意）|

---

## 6. デザインパターン分類

### 6.1 オーサリング体験パターン

#### **A. テキスト編集**

**タイプ:** `text`, `richtext`

**UI:**
- インプレイスダブルクリックで編集開始
- 薄い青いアウトライン→選択で濃い青に変化

**機能:**
| タイプ | 機能 |
|--------|------|
| `text` | 単純なテキスト入力（フォーマットなし）|
| `richtext` | リッチテキストエディタ（フォーマットオプション付き）|

**リッチテキストフォーマットオプション:**
- 見出し（h1, h2, h3等）
- 太字、斜体、下線
- 上付き文字、下付き文字
- 箇条書き、番号付きリスト
- リンク、画像挿入
- フォーマット削除

**自動保存:** フォーカスが離れると自動保存

#### **B. メディア編集**

**タイプ:** `media`

**UI:** Properties Panelからアセットセレクターを起動

**機能:**
- 画像/ビデオの選択と置換
- フィルタリング基準でアセット検索可能

#### **C. コンテナ管理**

**タイプ:** `container`

**UI:** コンテナ内にコンポーネントを追加・削除・再配列

**機能:**
- コンポーネントの追加・複製・削除
- ドラッグ＆ドロップで再配列
- Content Treeモードで階層的に管理

**ホットキー:**
- `a`: コンポーネント追加
- `Shift+Backspace`: コンポーネント削除

#### **D. コンポーネント操作**

**タイプ:** `component`

**UI:** コンテキストメニューから移動・削除・複製

**機能:**
- コンテキストメニュー（右クリック）からの操作
- ホットキーによる素早い操作

**ホットキー:**
| 操作 | Mac | 説明 |
|------|-----|------|
| コピー | `Command-C` | コンポーネントをコピー |
| ペースト | `Command-V` | コンポーネントをペースト |
| 上に移動 | `Command-U` | 1つ上に移動 |
| トップへ | `Shift+Command-U` | コンテナのトップへ移動 |
| 下に移動 | `Command-J` | 1つ下に移動 |
| ボトムへ | `Shift+Command-J` | コンテナのボトムへ移動 |

#### **E. 参照編集**

**タイプ:** `reference`

**UI:** Properties Panelで参照先を選択

**機能:**
- Content Fragment、Experience Fragment、製品等の参照
- フィルタリング基準で参照先を検索可能
- Content Fragment Editorで直接編集も可能

**ホットキー:**
- `e`: Content Fragment Editorで選択されたCFを編集

### 6.2 拡張フィーチャー（Extension Managerで有効化）

| 拡張 | 機能 | 対象 |
|------|------|------|
| **AEM Multi-Site-Management (MSM) Extension** | 継承の状態を表示・変更（継承の解除・再設定）| ページのみ |
| **AEM Page Properties Extension** | 現在編集中のページのページプロパティに素早くアクセス | ページのみ |
| **AEM Site Admin Extension** | Sites Consoleでページを管理 | 全般 |
| **AEM Page Lock Extension** | ページのロック・アンロック | ページのみ |
| **AEM Workflows Extension** | ワークフローの開始 | 全般 |
| **Generate Variations Extension** | 生成AIでコンテンツのバリエーションを作成 | 全般 |
| **Developer Login Extension** | ローカルAEM SDKでの開発者ログイン | 全般 |

### 6.3 ナビゲーションパターン

#### **編集モード**
- デフォルト: クリックでコンテンツを選択
- ホバー: 薄い青いアウトラインとバッジで編集可能領域を表示
- 選択: 濃い青いアウトラインとバッジ

#### **プレビューモード**
- リンクをクリックしてナビゲート可能
- 読者と同じようにコンテンツを体験
- 編集とプレビューを切り替え可能

#### **Undo/Redo**
- `Command-Z`: Undo
- `Shift+Command-Z`: Redo
- ブラウザセッションに限定

---

## 7. Edge Delivery Servicesとの統合

### 7.1 オーサリングワークフロー

AEM as a Cloud ServiceとEdge Delivery Servicesを組み合わせたシームレスなオーサリング体験：

1. **AEM Sites Console** でコンテンツ管理（ページ作成、フラグメント管理等）
2. **Universal Editor** でコンテンツオーサリング
3. **AEM** がHTMLをレンダリング（Edge Delivery Servicesのスクリプト、スタイル、アイコンを含む）
4. **変更をAEMに保存**
5. **Edge Delivery Services** へパブリッシュ

### 7.2 ページ構造

**ブロックとセクション:**
- ドキュメントベースのコンテンツオーサリングと同じ概念
- ブロックはEdge Delivery Servicesで配信されるページの基本コンポーネント
- デフォルトブロックまたはカスタムブロックを選択可能

**コンポーネント操作:**
- Universal Editorはコンポーネントと呼ばれるブロックを追加・配列
- Properties Panelで詳細設定

---

## 8. パフォーマンス最適化（Edge Delivery Services）

### 8.1 Three-Phase Loading（E-L-D）戦略

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
- 目的: 体験に直接影響しないサードパーティタグ等の読み込み
- 内容:
  - マーケティングツール、同意管理、拡張分析等
  - **重要:** LCPイベント後少なくとも3秒遅延させる

### 8.2 その他の最適化手法

| 手法 | 説明 |
|------|------|
| **ヘッダー＆フッターの非同期読み込み** | LCPのクリティカルパスに含まれないため非同期で読み込み |
| **ウェブフォントの遅延読み込み** | LCP直後に読み込み、フォントフォールバック手法でCLS回避 |
| **単一オリジンからの配信** | LCP前の複数オリジン接続はパフォーマンスに悪影響 |
| **リダイレクト回避** | 複数回のリダイレクトはCore Web Vitalsを悪化 |

### 8.3 100% Core Web Vitalsスコア

**目標:**
- LCP < 2.5秒
- FID < 100ミリ秒
- CLS < 0.1

**自動テスト:**
- プルリクエストごとにPageSpeed Insights Serviceで自動テスト
- スコアが100未満の場合、プルリクエストを失敗させる
- AEM Boilerplateを使用すると開発当初から100スコアを実現

---

## 9. 技術スタック

### 9.1 レンダリングパイプライン

Universal Editorは以下のレンダリング方式に対応：

1. **Server Side Rendering (SSR)** - サーバーサイドレンダリング
2. **Static Site Generation (SSG)** - 静的サイト生成
3. **Client Side Rendering (CSR)** - クライアントサイドレンダリング

### 9.2 Edge Delivery Servicesの特徴

- **100% Core Web Vitalsスコア**を目指す設計
- **AEM Boilerplate**を使用すると開発当初から100スコアを実現
- プルリクエストごとにPageSpeed Insights Serviceで自動テスト
- スコアが100未満の場合、プルリクエストを失敗させる

---

## 10. 高度な使用例

### 10.1 マルチサイト管理

**コードの再利用:**
- 複数の類似サイトでコードを共有
- `repoless-authoring` で実装

**マルチサイトマネージャー:**
- ロケールや言語にまたがるコンテンツ構造を作成
- 中央でコンテンツオーサリング

### 10.2 設定テンプレート

- Sites Consoleでプロジェクト設定を簡単に作成・管理
- 設定テンプレートを使用して一貫性を維持

---

## 11. 結論

### 11.1 Universal Editorの強み

1. **統一的編集体験:** あらゆる実装のあらゆるコンテンツを単一のエディタで編集可能
2. **開発者体験:** 最小限のSDK、DOMベースのインストルメンテーションで柔軟な実装
3. **パフォーマンス:** Edge Delivery Servicesとの統合で100% Core Web Vitalsを実現
4. **拡張性:** Extension Managerで機能拡張が可能

### 11.2 技術的洞察

- **属性ベースのインストルメンテーション:** HTML属性を追加するだけで編集可能に
- **URNベースのルーティング:** 変更を適切なバックエンドシステムにルーティング
- **プラグイン可能なバックエンド:** Universal Editor Service経由で様々なシステムに対応可能

### 11.3 デザインパターン

- **コンテキスト依存のUI:** 選択したコンテンツタイプに応じて適切な編集体験を提供
- **プレビューモード:** 編集とナビゲーションを切り替え可能
- **ホットキー:** よく使う操作はキーボードショートカットで素早く実行可能

### 11.4 Edge Delivery Servicesとの統合

- **AEMの強力なコンテンツ管理機能**と**Edge Delivery Servicesのパフォーマンス**の最適な組み合わせ
- **Three-Phase Loading戦略**でCore Web Vitalsを最適化
- **自動パフォーマンステスト**で品質を維持

---

## 12. 関連リソース

### ドキュメント
- [AEM Universal Editor Documentation](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/universal-editor/authoring)
- [Getting Started with Universal Editor](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/universal-editor/getting-started)
- [Universal Editor Architecture](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/universal-editor/architecture)
- [Attributes and Types](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/universal-editor/attributes-types)

### ツール
- [AEM Boilerplate](https://github.com/adobe/aem-boilerplate)
- [Adobe Developer - Extension Manager](https://developer.adobe.com/uix/docs/extension-manager/)
- [AEM Sidekick](https://www.aem.live/docs/sidekick)

### ベストプラクティス
- [Core Web Vitals](https://web.dev/explore-learn-core-vitals/)
- [Keeping it 100](https://www.aem.live/developer/keeping-it-100)

---

*本レポートはMira (AI Assistant) によって作成されました。*
*調査期間: 2026年2月13日*

---

## 13. パフォーマンス最適化の詳細（2026-02-13 12:50 更新）

### 13.1 Webパフォーマンスの基本概念

#### サーバーサイド vs クライアントサイドレンダリング

**AEM Edge Delivery Servicesのアプローチ:**
- ページの正規コンテンツはすべてサーバーサイドでマークアップとしてレンダリング
- CSSとDOMによるコンテンツの装飾は表示にのみ影響
- クライアントサイドレンダリング（JSONフェッチ）は、ページに正規コンテンツがない場合のみ使用（例: 他ページを一覧表示するブロック、アプリケーション等）

**リダンダントコンテンツの扱い:**
- ページの正規コンテンツとして意味的に含まれないリダンダントコンテンツは、パフォーマンス考慮によりマークアップに含まれない
- これにはヘッダーとフッターが含まれる
- 大量のページで冗長に使用されるフラグメントも除外

#### Core Web Vitals (CWV) と Lighthouse

**CWVの重要性:**
- ウェブサイトのパフォーマンスは検索結果のランキングに影響
- 実際のエンドユーザーパフォーマンスはCore Web Vitalsで反映
- CWVは訪問者にとっての良い/悪いウェブパフォーマンスの最終的な審判者

**Lighthouse via PageSpeed Insights:**
- CWVは実世界（フィールドデータ）で収集されたメトリクス
- コード、ネットワーク設定、訪問者のデバイスに依存
- PageSpeed Insightsは分離されたサービスで、GoogleのLighthouseスコアを実行
- Lighthouseスコアは相対的な主張を行うための貴重で信頼できるプロキシ

### 13.2 Three-Phase Loading (E-L-D) 戦略の詳細

#### 戦略概要

ウェブページのペイロードを3つのフェーズに分解することで、クリーンなLighthouseスコアを実現し、優れた顧客体験のベースラインを設定

| フェーズ | 説明 | 目的 |
|---------|------|------|
| **Phase E (Eager)** | LCP達成に必要なすべて | Largest Contentful Paintを達成 |
| **Phase L (Lazy)** | プロジェクトで制御されたペイロード | Total Blocking Time (TBT) に影響しない読み込み |
| **Phase D (Delayed)** | その他すべて（サードパーティ等）| 体験に直接影響しない読み込み |

#### Phase E: Eager（LCP達成）

**ボディ非表示ルール:**
- 何よりも先に、ボディを非表示（`display:none`）にして、画像のダウンロード開始と初期CLSを回避

**DOMデコレーション:**
- 最初のアクションはDOMの「デコレーション」
- ローディングシーケンスは微調整を行い、主にCSSクラスをアイコン、ボタン、ブロック、セクションに追加
- オートブロックを作成

**ファーストセクションのローディング:**
- ファーストセクション全体をロード
- ファーストイメージ（「LCP候補」）に優先順位を与える
- 理論的には、ファーストセクションのブロックが少ないほど、LCPを高速にロード可能

**フォントの非同期ローディング:**
- LCP候補とセクションの全ブロックがロードされたら、ファーストセクションを表示可能
- フォントは非同期でロード開始

**LCP達成のベストプラクティス:**
- LCP前の集約ペイロードは100kb以下に抑える（通常1560ms以内のLCPイベント、PageSpeed Insightsで100スコア）
- LCP発生前の第2オリジンへの接続は強く非推奨（TLS、DNS等で大きな遅延）

#### Phase L: Lazy（遅延読み込み）

**目的:**
- Total Blocking Time (TBT) に影響しない読み込み
- 結果的にFirst Input Delay (FID) にも影響しない

**含まれるもの:**
- 次のセクションとそのブロック（JavaScriptとCSS）
- `loading="lazy"`属性を持つ残りのすべての画像
- 非ブロッキングなJavaScriptライブラリ

**推奨事項:**
- ペイロードの大半は同一オリジンから来るべき
- ファーストパーティによって制御されているべき
- 必要に応じて変更が可能

#### Phase D: Delayed（遅延サードパーティ）

**目的:**
- 全体的な顧客体験への影響を最小化
- 体験に即座の影響しない、またはプロジェクトで制御されていないもの

**含まれるもの:**
- マーケティングツール
- 同意管理
- 拡張分析
- チャット/インタラクションモジュール
- タグ管理ソリューションを通じてデプロイされるもの

**重要:**
- このフェーズの開始は大幅に遅延させる必要がある
- 遅延フェーズは少なくともLCPイベントの3秒後
- 残りの体験が落ち着くのに十分な時間を残す

**delayed.jsの役割:**
- 遅延フェーズは通常delayed.jsで処理
- TBTを引き起こすスクリプトの初期キャッチオール
- 理想的には、スクリプトにブロッキング時間はない
- 問題が修正されたら、ライブラリをLazyフェーズに追加し、より早くロード可能

### 13.3 パフォーマンス問題の一般的な原因（Anti-Patterns）

#### 1. Early hints / h2-push / pre-connect

**問題:**
- 本能的には、マークアップ処理が始まる前にできるだけ多くのものをダウンロードするように思える
- しかし、究極の目標は訪問者にできるだけ早く安定したページを表示すること
- LCPタイミングがその良いプロキシ

**影響:**
- Early hints、h2-push、pre-connectは帯域幅を消費
- LCPに不要なリソースをダウンロードするため、パフォーマンスに悪影響
- LCPを100に達成するには、これらを削除する必要がある

#### 2. パス解決のためのリダイレクト

**問題:**
- 訪問者が`www.domain.com`をリクエストし、`www.domain.com/en`、さらに`www.domain.com/en/home`にリダイレクトされる場合
- 各リダイレクトでペナルティを受ける

**影響:**
- パフォーマンスが悪影響を受ける
- PageSpeed Insightsのラボテストではデフォルトでリダイレクトオーバーヘッドが除外されるため、主にRUMまたはCrUXで測定されたCore Web Vitalsで可視化

#### 3. CDNクライアントスクリプトインジェクション

**問題:**
- 一部のCDNベンダーと設定はスクリプトをインジェクト
- 帯域幅を消費し、LCP前にブロッキング時間を作成

**影響:**
- パフォーマンスに悪影響
- これらのスクリプトは無効化するか、ローディングシーケンスで適切にロードする必要がある
- `.aem.live`オリジンのPageSpeed Insightレポートと、CDNがフロントエンドされた対応サイトを比較すると、AEMの制御外のCDNによって生成される悪影響が表示される

#### 4. CDN TTFBとプロトコル実装の影響

**問題:**
- CDNベンダーによっては、プロトコル実装とパフォーマンス特性に差異
- WAFやAEMのアップストリームのネットワークインフラストラクチャもパフォーマンスに悪影響

**影響:**
- HTTPペイロードの純粋な配信に関連
- `.aem.live`オリジンと、CDNがフロントエンドされた対応サイトを比較すると、影響が可視化される

### 13.4 ヘッダーとフッター

**非同期ローディング:**
- ページのヘッダー、特にフッターはLCPへのクリティカルパスに含まれない
- それぞれのブロックで非同期にロード

**リソース分離の重要性:**
- 同じライフサイクルを共有しないリソース（異なる時期にオーサリング変更で更新されるもの）は、別々のドキュメントに保持すべき
- オリジンとブラウザ間のキャッシングチェーンをよりシンプルで効果的にする
- これによりキャッシュヒット比が上昇し、キャッシュ無効化とキャッシュ管理の複雑さが低減

### 13.5 フォント

**基本アプローチ:**
- ウェブフォントは帯域幅への負担が大きい
- フォントサービス（Adobe FontsやGoogle Fonts）経由で異なるオリジンからロードされることが多い
- LCP前にフォントをロードするのはほぼ不可能

**タイミング:**
- LCP直後にロード

**AEM Boilerplateのアプローチ:**
- デフォルトでフォントフォールバック手法を実装
- フォントロード時のCLSを回避
- フォントをプリロード（Early hints、h2-push、マークアップ経由）するのは生産的ではない
- パフォーマンスに大きな悪影響

### 13.6 開発者のためのステップ

#### スタート時のベースライン

**AEM Boilerplateの使用:**
- Boilerplateでプロジェクトをスタートすると、モバイルとデスクトップの両方でPageSpeed Insight上で非常に安定したLighthouseスコア100を達成
- Lighthouseスコアの各コンポーネントに、プロジェクトコードで消費できるバッファがある
- 完璧な100 Lighthouseスコアの境界内に留まる

#### プルリクエストのテスト

**自動テストの重要性:**
- Lighthouseスコアが低くなったら改善するのは困難
- しかし、継続的にテストすれば100を維持するのは難しくない

**テストの仕組み:**
- プロジェクトでプルリクエスト（PR）を開くと、プロジェクトの説明にあるテストURLが使用される
- PageSpeed Insights Serviceが実行される
- AEM GitHubボットが、スコアが100未満の場合（結果の変動性を考慮して少しバッファ付き）に自動的にPRを失敗させる
- 結果はモバイルLighthouseスコア（デスクトップより達成が困難なため）

### 13.7 ボーナス: スピードはグリーン

**環境への配慮:**
- 高速で小さく、クイックにレンダリングするウェブサイトを構築することは、優れた体験を提供し、コンバージョンを向上させるだけでなく
- 炭素排出を削減する良い方法でもある

---

## 14. まとめ（2026-02-13 12:50 更新）

### Universal EditorとEdge Delivery Servicesの統合の価値

**技術的優位性:**
1. **統一されたオーサリング:** AEMの強力なコンテンツ管理機能（MSM、翻訳、Launches等）とEdge Delivery Servicesのパフォーマンスの最適な組み合わせ
2. **100% Core Web Vitalsスコア:** Three-Phase Loading戦略とAEM Boilerplateで開発当初から達成可能
3. **自動品質保証:** プルリクエストごとの自動パフォーマンステストで品質を維持
4. **柔軟な実装:** 属性ベースのインストルメンテーションであらゆる実装に対応

**ビジネス価値:**
- 検索ランキングの改善（Core Web Vitals）
- エンドユーザー体験の向上
- 開発生産性の向上（最小限のSDK、DOMベースのインストルメンテーション）
- 環境への配慮（炭素排出削減）

**今後の展望:**
- Real Use Monitoring (RUM)による継続的なパフォーマンス改善
- Operational Telemetryデータによるフィールドでの結果検証
- 拡張機能による機能追加（Extension Manager経由）

---

*本レポートはMira (AI Assistant) によって作成されました。*
*調査期間: 2026年2月13日*
*最終更新: 2026年2月13日 12:50*

