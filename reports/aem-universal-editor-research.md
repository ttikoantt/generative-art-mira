# AEM Universal Editor Research Report

**最終更新:** 2026年2月13日 18:05 (JST)
**調査担当:** Mira (Autonomous Research Agent)
**ジョブID:** 47b3991b-801e-43d0-b83c-726f8f56288e

---

## 📋 調査範囲

### 調査対象URL
1. https://www.aem.live/developer/universal-editor-blocks
2. https://www.aem.live/docs/universal-editor-assets
3. https://www.aem.live/developer/component-model-definitions

### 調査日時
- 開始: 2026年2月13日 08:40 (JST)
- 終了: 2026年2月13日 08:50 (JST)

---

## 🔍 Universal Editorの概要

### Universal Editorとは？
AEM as a Cloud ServiceとEdge Delivery Servicesを統合するための**汎用エディタ**。主な特徴：

- **AEM コンテンツソース対応**: AEMのコンテンツをEdge Delivery Servicesで配信可能
- **インコンテキスト編集**: ページ上で直接コンテンツを編集可能
- **コンテンツモデル駆動**: コンポーネントモデルでコンテンツ構造を定義
- **Edge Delivery統合**: 高速配信とAEMのCMS機能を組み合わせ

---

## 🏗️ 実装形式の分類

### 1. コンポーネント定義 (Component Definitions)

**ファイル:** `component-definitions.json`

Universal Editorで利用可能なコンポーネントを定義。

```json
{
  "title": "Quote",
  "id": "quote",
  "plugins": {
    "xwalk": {
      "page": {
        "resourceType": "core/franklin/components/block/v1/block",
        "template": {
          "name": "Quote",
          "model": "quote"
        }
      }
    }
  }
}
```

**重要ポイント:**
- `resourceType`: 必ず `core/franklin/components/block/v1/block` を使用
- `template.name`: ブロック名（スタイル/スクリプト参照に使用）
- `template.model`: コンポーネントモデルIDへの参照

### 2. コンポーネントモデル (Component Models)

**ファイル:** `component-models.json`

コンテンツのフィールド構造を定義。

```json
{
  "id": "quote",
  "fields": [
     {
       "component": "richtext",
       "name": "quote",
       "value": "",
       "label": "Quote",
       "valueType": "string"
     },
     {
       "component": "text",
       "valueType": "string",
       "name": "author",
       "label": "Author",
       "value": ""
     }
   ]
}
```

**フィールドタイプ:**
- `richtext`: リッチテキスト
- `text`: プレーンテキスト
- `reference`: 画像やリンクの参照
- `select` / `multiselect`: 選択肢

### 3. コンポーネントフィルタ (Component Filters)

**ファイル:** `component-filters.json`

ブロックの追加可能箇所を制御。

```json
{
  "id": "section",
  "components": [
    "text",
    "image",
    "button",
    "title",
    "hero",
    "cards",
    "columns",
    "quote"
   ]
}
```

---

## 🎨 デザインパターンの分類

### 1. シンプルブロック (Simple Blocks)

**構造:** 1次元（プロパティのリスト）

**例: Quote Block**
```
+---------------------------------------------+
| Think, McFly! Think!                  |
+---------------------------------------------+
| Biff Tannen                            |
+---------------------------------------------+
```

**実装要件:**
- 各プロパティが1行1列で順番にレンダリング
- モデルで定義された順序に従う

### 2. コンテナブロック (Container Blocks)

**構造:** 2次元（プロパティ + 子要素）

**例: Linked Icons Block**
```
+------------------------------------------------------------- +
| Our Partners                                                |
+=============================================================+
| Our community of partners is ...                            |
+-------------------------------------------------------------+
| ![Icon of Foo] | https://foo.com |
+-------------------------------------------------------------+
| ![Icon of Bar] | https://bar.com |
+-------------------------------------------------------------+
```

**実装要件:**
- 独自のプロパティ（1列）+ 子要素リスト
- 各子要素が1行、各プロパティが列
- `filter` IDで子要素の追加可能タイプを制御

### 3. カラムズブロック (Columns Block)

**特徴:**
- レイアウト定義専用
- コンテンツモデリングは提供されない
- 制限:
  - `rows`, `columns`, `classes` のみ
  - デフォルトコンテンツのみ追加可能（テキスト、画像、ボタン）

### 4. セクションメタデータ (Section Metadata)

**タイプ:** Key-Value ペア

**用途:** 設定値の保存（スプレッドシート入力など）

```
+-----------------------------------------------------------------------+
| Featured Articles                                                     |
+=======================================================================+
| source   | /content/site/articles.json |
+-----------------------------------------------------------------------+
| keywords | Developer,Courses                                          |
+-----------------------------------------------------------------------+
| limit    | 4                                                          |
+-----------------------------------------------------------------------+
```

---

## 🔧 コンテンツモデリングの手法

### 1. タイプ推論 (Type Inference)

特定の値から意味論的セマンティクスを自動推論：

- **画像**: MIMEタイプ `image/*` → `<picture><img>`
- **リンク**: 外部URL → `<a href>`
- **リッチテキスト**: HTMLタグ開始 → そのままレンダリング
- **クラス名**: ブロックオプションとして処理
- **値リスト**: カンマ区切りで連結

### 2. フィールド崩壊 (Field Collapse)

命名規約で複数フィールドを1要素に統合：

**サフィックス（大文字小文字区別）:**
- `Title` → タイトル属性
- `Type` → タイプ属性
- `MimeType` → MIMEタイプ
- `Alt` → 代替テキスト
- `Text` → テキスト内容

**例:** 画像 + Alt
```
"image": "/content/dam/red-car.png"
"imageAlt": "A red car on a road"
```
↓
```html
<picture>
  <img src="/content/dam/red-car.png" alt="A red car on a road">
</picture>
```

### 3. 要素グループ化 (Element Grouping)

複数の意味的要素を1セルに統合：

**命名規約:** `groupName_propertyName`

**例:** Teaser Block
```
"teaserText_subtitle": "Adobe Experience Cloud"
"teaserText_title": "Meet the Experts"
"teaserText_titleType": "h2"
"teaserText_description": "<p>Join us...</p>"
```

**メリット:**
- オーサーが作成できる要素数を制限
- 意味的構造を保護
- スタイリングを簡素化

---

## 📦 ブロックオプション (Block Options)

### クラスプロパティによるバリエーション

**例:** 背景色変更
```json
{
  "component": "select",
  "name": "classes",
  "label": "Background Color",
  "options": [
    { "name": "Red", "value": "bg-red" },
    { "name": "Green", "value": "bg-green" },
    { "name": "Blue", "value": "bg-blue" }
  ]
}
```

**要素グループ化による複数オプション:**
```json
"classes": "variant-a",
"classes_background": "light",
"classes_fullwidth": true
```
↓
```html
<div class="teaser variant-a light fullwidth">
```

---

## 🖼️ アセット統合

### AEM Assetsとの統合

**前提条件:**
1. 技術アカウントによるアクセス（自動作成）
2. フォルダのアクセス権限
3. アセットサイズ制限（画像: 最大10MB, 動画: 最大300Mbps）

**Processing Profileの設定:**
- 画像: `edge-delivery-services-jpeg`, `edge-delivery-services-png`
  - 最大サイズ: 2000x2000px
  - 品質: 100
- 動画: `edge-delivery-services-mp4`
  - ビットレート: 300

---

## ⚠️ 制限と注意点

### カスタムコンポーネントの禁止
- Edge Delivery Services向けの標準コンポーネントのみ使用
- カスタムAEMコンポーネントの実装は非推奨
- `core/franklin/components/block/v1/block` リソースタイプ必須

### DOM操作時の注意
**`data-aue-*` 属性の保護:**
- DOM構造を変更する場合、インストルメンテーション属性を保持
- `moveInstrumentation()` メソッド使用

### ブロック実装の3フェーズ
Adobe推奨の開発手順：
1. 定義とモデルの作成 → 本番環境へ
2. コンテンツ作成
3. デコレーションとスタイル実装

---

## 🔄 AEMオーサリングとドキュメントベースの両立

### 共通化アプローチ
- **同一コンテンツモデル**を使用
- **同一ブロック実装**で両方をサポート
- データはテーブル形式でレンダリング（ドキュメントベースと同等）

**メリット:**
- 開発時間の短縮
- サイト体験の一貫性
- オーサリング方法の柔軟な切り替え

---

## 📚 関連リソース

- [Universal Editor Blocks](https://www.aem.live/developer/universal-editor-blocks)
- [Publishing pages with AEM Assets](https://www.aem.live/docs/universal-editor-assets)
- [Content modeling for AEM authoring](https://www.aem.live/developer/component-model-definitions)
- [Block Collection](https://www.aem.live/developer/block-collection)
- [David's Model](https://www.aem.live/docs/davidsmodel)

---

## 🎓 学んだこと

### Universal Editorの特長
1. **AEMのCMS機能**と**Edge Deliveryの高速配信**を最適に組み合わせ
2. **コンテンツモデル駆動**で構造化されたオーサリング体験
3. **インストルメンテーション属性**によるインコンテキスト編集

### デザインパターンの特徴
- **シンプルブロック**: 基本的な1次元コンテンツ
- **コンテナブロック**: リスト形式の子要素（例: カード、カルーセル）
- **カラムズ**: レイアウト専用
- **セクションメタデータ**: 設定値保存

### コンテンツモデリングの工夫
- **タイプ推論**: 自動セマンティクス付与
- **フィールド崩壊**: 複数属性の1要素統合
- **要素グループ化**: 複数要素の1セル統合、オーサー制限

---

## 📝 詳細実装手順（2026年2月13日 16:59更新）

### ブロック開発の3フェーズアプローチ（詳細版）

Adobeが推奨するUniversal Editorブロック開発の正規手順：

#### フェーズ1: 定義とモデルの作成

**手順:**
1. `component-definitions.json` に新しいブロック定義を追加
2. `component-models.json` にフィールド構造を定義
3. `component-filters.json` でブロックの追加可能箇所を制御
4. Gitでコミットして本番環境へ反映

**Quoteブロックの実装例:**

**component-definitions.json:**
```json
{
  "title": "Quote",
  "id": "quote",
  "plugins": {
    "xwalk": {
      "page": {
        "resourceType": "core/franklin/components/block/v1/block",
        "template": {
          "name": "Quote",
          "model": "quote",
          "quote": "<p>Think, McFly! Think!</p>",
          "author": "Biff Tannen"
        }
      }
    }
  }
}
```

**component-models.json:**
```json
{
  "id": "quote",
  "fields": [
    {
      "component": "richtext",
      "name": "quote",
      "value": "",
      "label": "Quote",
      "valueType": "string"
    },
    {
      "component": "text",
      "valueType": "string",
      "name": "author",
      "label": "Author",
      "value": ""
    }
  ]
}
```

**component-filters.json:**
```json
{
  "id": "section",
  "components": [
    "text",
    "image",
    "button",
    "title",
    "hero",
    "cards",
    "columns",
    "quote"
  ]
}
```

#### フェーズ2: コンテンツ作成

**手順:**
1. AEM as a Cloud Serviceにサインイン
2. Sitesコンソールから対象ページを選択
3. 「Edit」ボタンでUniversal Editorを開く
4. セクションを選択して「Add」アイコンをクリック
5. 新しいブロック（Quote）を追加
6. 必要に応じてコンテンツを編集
7. 「Publish」ボタンで公開

**注意点:**
- Universal Editorで読み込むにはAdobe認証が必要
- ブロックはセクション内に追加
- 青いアウトラインと「Section」タブでセクション選択を確認

#### フェーズ3: デコレーションとスタイル実装

**手順:**
1. プロジェクトの`blocks/`フォルダにブロック用フォルダを作成（例: `blocks/quote/`）
2. 必要なファイルを作成:
   - `quote.css`: スタイル定義
   - `quote.js`: 振る舞い（必要な場合）
3. ブロックデコレーションを実装
4. 本番環境に反映

---

## 🔍 新しい知見（2026年2月13日発見）

### Universal Editorのアーキテクチャ

**技術スタック:**
- **ResourceType**: `core/franklin/components/block/v1/block`（必須）
- **プラグインシステム**: `xwalk` プラグインでページ上の挙動を定義
- **テンプレートシステム**: `template` プロパティでデフォルトコンテンツを提供

**データフロー:**
1. AEM → Universal Editor（編集）
2. Universal Editor → AEM（保存）
3. AEM → Edge Delivery Services（配信）

### Universal Editorの認証フロー

**認証手順:**
1. Universal Editorで「Sign in with Adobe」をクリック
2. Adobe IDで認証
3. AEM Cloud Serviceへのアクセス権限確認
4. 技術アカウントでAEM Assetsへのアクセス

**認証が不要なケース:**
- すでにAdobe製品にサインインしている場合
- セッションが有効な場合

---

## 🎨 デザインパターン詳細版

### コンテナブロックの内部構造

**Linked Iconsブロックの例:**

**データモデル:**
```json
{
  "id": "linked-icons",
  "fields": [
    {
      "component": "text",
      "name": "title",
      "label": "Title",
      "valueType": "string"
    },
    {
      "component": "richtext",
      "name": "description",
      "label": "Description",
      "valueType": "string"
    }
  ]
}
```

**フィルター定義:**
```json
{
  "id": "linked-icons",
  "components": ["icon-link"]
}
```

**子要素の定義（icon-link）:**
```json
{
  "title": "Icon Link",
  "id": "icon-link",
  "plugins": {
    "xwalk": {
      "page": {
        "resourceType": "core/franklin/components/block/v1/block",
        "template": {
          "name": "IconLink",
          "model": "icon-link"
        }
      }
    }
  }
}
```

---

## ⚙️ エッジケースの処理

### 複雑なブロックオプション

**バリエーション実装:**
```json
{
  "component": "select",
  "name": "classes",
  "label": "Style Variant",
  "options": [
    { "name": "Default", "value": "" },
    { "name": "Dark", "value": "dark" },
    { "name": "Light", "value": "light" }
  ]
}
```

**複数オプションの組み合わせ:**
```json
{
  "classes": "variant-a",
  "classes_background": "light",
  "classes_fullwidth": true
}
```

**最終HTML:**
```html
<div class="teaser variant-a light fullwidth">
  <!-- コンテンツ -->
</div>
```

---

## 📦 AEM Assetsとの連携詳細

### アセット制限

**画像:**
- 最大サイズ: 10MB
- 推奨寸法: 2000x2000px以下
- フォーマット: JPEG, PNG, WebP

**動画:**
- 最大ビットレート: 300Mbps
- 推奨フォーマット: MP4

### Processing Profile

**画像プロファイル:**
- `edge-delivery-services-jpeg`: JPEG用
- `edge-delivery-services-png`: PNG用

**設定パラメータ:**
- 最大寸法: 2000x2000px
- 品質: 100

**動画プロファイル:**
- `edge-delivery-services-mp4`: MP4用
- ビットレート: 300

---

## 🚀 パフォーマンス最適化

### Edge Delivery Servicesの特長

**高速配信の仕組み:**
- CDNエッジでのコンテンツ配信
- 最適化された画像・動画配信
- 自動キャッシュ管理

**ベストプラクティス:**
- 適切な画像サイズを使用
- Lazy Loadingを活用
- Processing Profileで最適化

---

## 🔒 セキュリティと権限管理

### 技術アカウント

**自動作成:**
- Universal Editor導入時に自動作成
- AEM Assetsへのアクセス権限を持つ

**フォルダ権限:**
- 必要なフォルダのみにアクセス可能
- 過剰な権限付与を回避

---

## 📚 関連ドキュメント（更新）

### 公式ドキュメント
- [Universal Editor Blocks](https://www.aem.live/developer/universal-editor-blocks)
- [Publishing pages with AEM Assets](https://www.aem.live/docs/universal-editor-assets)
- [Content modeling for AEM authoring](https://www.aem.live/developer/component-model-definitions)
- [Block Collection](https://www.aem.live/developer/block-collection)
- [David's Model](https://www.aem.live/docs/davidsmodel)

### 関連リソース
- [Universal Editor Developer Tutorial](https://www.aem.live/developer/ue-tutorial)
- [Development Best Practices](https://www.aem.live/docs/dev-collab-and-good-practices)

---

**次回の調査予定:**
- Universal Editorの具体的な実装例（コードスニペット集）
- カスタムブロックの高度なパターン
- パフォーマンス監視と最適化手法

---

## 🔍 新しい知見（2026年2月13日 18:05追加）

### Universal Editorのアーキテクチャ詳細

**4つのビルディングブロック:**

1. **Editors（エディタ）**
   - Universal Editor: インストルメンテーションされたDOMを使用したインプレイス編集
   - Properties Panel: フォームベースのエディタ（回転時間、タブ状態等）

2. **Remote App（リモートアプリ）**
   - DOMをインストルメンテーションしてUniversal Editorで編集可能に
   - 必要な属性をレンダリング
   - 最小SDKで実装

3. **API Layer（APIレイヤ）**
   - Content Data: データソースは問わない（必須な属性定義のみ重要）
   - Persisting Data: 各編集可能データにURN識別子

4. **Persistence Layer（持続レイヤ）**
   - Content Fragment Model: コンポーネント・コンテンツフラグメントモデル
   - Content: AEM、Magento等どこにでも保存可能

**Universal Editor Service:**
- Adobe I/O Runtime上で動作する集中サービス
- Extension Registryからプラグインを読み込み
- URNに基づいて適切なバックエンドにルーティング

### データ属性とタイプの完全リスト

**必須・オプション属性:**

| 属性名 | 説明 | 必須 | 用途 |
|--------|------|------|------|
| `data-aue-type` | コンポーネントタイプ | 必須 | 編集可能タイプの特定 |
| `data-aue-resource` | URN（一意識別子） | 必須 | データ保存先のルーティング |
| `data-aue-prop` | プロパティ名 | コンテキスト編集で必須 | 編集するフィールド名 |
| `data-aue-filter` | フィルタ条件 | オプション | アセットセレクタ等 |
| `data-aue-label` | 表示ラベル | オプション | UI表示用 |
| `data-aue-model` | モデルID | オプション | コンテンツフラグメント等 |

**タイプ詳細:**

1. **text**: シンプルテキスト（リッチテキストなし）
2. **richtext**: リッチテキスト（RTE表示）
3. **media**: アセット（画像・動画）
4. **container**: コンポーネントコンテナ（段落システム）
5. **component**: 移動可能・削除可能なDOM要素
6. **reference**: 参照（コンテンツフラグメント・エクスペリエンス・商品）

### ブロックシステムの階層構造

**ドキュメント構造:**
1. **Default Content**: 見素なセマンティクス（見出し、画像、リスト等）
2. **Sections**: コンテンツをグループ化（水平ルールや`---`で分離）
3. **Blocks**: コンポーネント化されたUI（テーブル形式で定義）

**マークアップ vs DOM:**

**シンプルマークアップ:**
```html
<section>
  <h1>Title</h1>
  <p>Body text</p>
</section>
```

**装飾されたDOM（自動拡張）:**
```html
<section class="section" data-aue-resource="...">
  <div class="section-metadata" data-aue-type="richtext" data-aue-prop="...">
    <h1 class="heading-h1">Title</h1>
  </div>
  <div class="default-content">
    <p data-aue-type="richtext" data-aue-prop="..." data-aue-resource="...">Body text</p>
  </div>
</section>
```

**Boilerplate vs Block Collection:**

**Boilerplate:**
- ほとんどのAEMプロジェクトで使用
- GitHub: `adobe/aem-boilerplate`
- デフォルトコンテンツタイプを含む

**Block Collection:**
- 半数以上のプロジェクトで使用されるブロック
- GitHub: `adobe/aem-block-collection`
- Hero, Columns, Cards, Accordion等

**Auto Blocking:**
- デフォルトコンテンツやメタデータを自動的にブロック化
- 作者が物理的にブロックを作成する必要なし
- `buildAutoBlocks()`関数で実装

### Repoless Authoring（レポレスオーサリング）

**概要:**
- 複数サイトで同じコードベースを共有
- 各サイトのGitレポジトリ不要
- Configuration Serviceで設定管理

**有効化手順:**
1. Configuration Serviceのアクセストークン取得
2. コンテンツ・コードソースの設定
3. パスマッピングの設定
4. 技術アカウントの設定
5. AEM設定の更新

**設定例:**
```json
{
  "code": {
    "owner": "<github-org>",
    "repo": "<aem-project>",
    "source": {
      "type": "github",
      "url": "https://github.com/<org>/<project>"
    }
  },
  "content": {
    "source": {
      "url": "https://author-<env>.adobeaemcloud.com/...",
      "type": "markup",
      "suffix": ".html"
    }
  }
}
```

### 拡張機能（Extensions）

**ツールバー拡張:**
- **Inheritance**: MSM継承のステータス表示・解除・再適用
- **Page Properties**: ページプロパティへのクイックアクセス
- **Sites Console**: サイトコンソールへの遷移
- **Page Lock**: ページのロック・アンロック
- **Workflows**: ワークフローの開始
- **Developer Login**: ローカルAEM SDKへのログイン

**プロパティパネル拡張:**
- **Generate Variations**: AIによるコンテンツバリエーション生成

**拡張の有効化:**
- Extension Managerで管理者が有効化する必要
- プログラム単位での設定

### Edge Delivery Services統合の詳細

**サポートされるアーキテクチャ:**
1. **Edge Delivery Services**: 推奨アプローチ（シンプル、高速）
2. **Headless実装**: 既存ヘッドレスプロジェクト対応

**AEMオーサリングワークフロー:**
1. AEM Sites Consoleでページ・コンテンツ作成
2. Universal Editorでインプレイス編集
3. AEMからEdge Delivery Servicesへ配信
4. CDNで高速配信

**Universal Editorの役割:**
- AEMのロバストなCMS機能活用
- マルチサイト、 MSM、翻訳ワークフロー等
- Edge Deliveryの並外れないパフォーマンス

### 対応バージョン

- **AEM as a Cloud Service**: Release 2023.8.13099以上
- **AEM 6.5 LTS**: オンプレミス・AMS対応
- **AEM 6.5**: オンプレミス・AMS対応

**制限:**
- 1ページ当たり最大25 AEMリソース参照
- コンテンツ作成者は個別のExperience Cloudアカウント必要
- デスクトップブラウザのみサポート（モバイル版非対応）

### 開発者のためのベストプラクティス

**3つの原則:**
1. **シンプルで直観的**: 作者にとって直観的であること
2. **ブロックのネスト禁止**: ブロック内にブロックをネストしない
3. **開発者が複雑さを吸収**: 作者に複雑さを委ねない

**マークアップ原則:**
- シンプルで読みやすいHTMLをレンダリング
- JavaScriptでDOMを拡張
- セマンティクHTMLを維持

**ブロックオプションの実装:**
- 括弧付きでクラス追加: `Block (wide)` → `<div class="block wide">`
- 複数オプション: `Block (dark, wide)` → `<div class="block dark wide">`
- カンマ区切りで複数クラス: `Block (dark, wide)` → `<div class="block dark wide">`

---

**最終更新: 2026年2月13日 19:05 (JST)**

*このレポートは自律調査エージェントMiraによって作成・更新されました。*

---

## 🔍 新しい知見（2026年2月13日 19:05追加）

### Edge Delivery Services統合のワークフロー

**Universal EditorとEdge Delivery Servicesの連携:**

1. **AEM Sites Console**: コンテンツ管理（新規ページ、Experience Fragments、Content Fragments等の作成）
2. **Universal Editor**: AEM管理下のコンテンツをインコンテキスト編集
3. **AEMレンダリング**: HTMLをレンダリング（Edge Delivery Servicesのスクリプト、スタイル、アイコン等を含む）
4. **変更の永続化**: 全ての変更をAEM as a Cloud Serviceに保存
5. **Edge Deliveryへ配信**: Universal Editorで作成したコンテンツをEdge Delivery Servicesへ配信
6. **セマンティックHTML配信**: AEMはEdge Delivery Servicesで取り込み可能なセマンティックHTMLをレンダリング
7. **高速配信**: Edge Delivery Servicesで100% Core Web Vitalsスコアを実現

**ページ構造のコンセプト:**

- **Default Content**: 見素なセマンティクス（見出し、画像、リスト等）
- **Sections**: 水平ルールや`---`で分離されたコンテンツのグループ化
- **Blocks**: コンポーネント化されたUI（テーブル形式で定義）

**Universal Editorの特徴:**
- モダンで直観的なGUIでコンテンツ作成
- コンポーネント（ブロック）の追加・配置
- プロパティパネルでの詳細設定

### Repoless Authoring（コードベースの共有）

**概要:**
- 複数サイトで同じコードベースを共有
- 各サイトのGitレポジトリ不要
- Configuration Serviceで設定管理

**有効化の前提条件:**
1. AEM as a Cloud Service 2025.4以上
2. Configuration Serviceの設定完了

**設定手順:**
1. Admin Service（https://admin.hlx.page/login）でアクセストークンを取得
2. Configuration ServiceでコードとAEMコンテンツのソースを設定
3. パスマッピングの設定
4. 技術アカウントの設定
5. AEM設定の更新

**設定例:**
```json
{
  "code": {
    "owner": "<github-org>",
    "repo": "<aem-project>",
    "source": {
      "type": "github",
      "url": "https://github.com/<org>/<project>"
    }
  },
  "content": {
    "source": {
      "url": "https://author-<env>.adobeaemcloud.com/...",
      "type": "markup",
      "suffix": ".html"
    }
  }
}
```

**トラブルシューティング:**
- ページがレンダリングされない場合：ソースを確認
- 404エラー：config.jsonやcomponent-definitions.jsonがロードできていない可能性

### Block Collectionとボイラープレート

**ボイラープレートへの包含基準:**

- **直観的**: 直観的で使いやすいコンテンツ構造
- **使用可能**: 依存関係なし、boilerplate互換
- **レスポンシブ**: 全ブレークポイントで動作
- **コンテキスト認識**: テキスト色や背景色等を継承
- **ローカライズ可能**: ハードコードされたコンテンツなし
- **高速**: パフォーマンスへの悪影響なし
- **SEOとアクセシビリティ**: SEO友好でアクセシブル

**AEM Boilerplate（必須ブロック）:**
- 覇数のAEMプロジェクトで使用されるブロック
- GitHub: https://github.com/adobe/aem-boilerplate/tree/main/blocks
- **含まれるブロック**:
  - Headings, Text, Images, Lists, Links, Buttons
  - Code, Sections, Icons, Hero, Columns, Cards
  - Header, Footer, Metadata

**Block Collection（共通ブロック）:**
- 半数以上のプロジェクトで使用されるブロック
- GitHub: https://github.com/adobe/aem-block-collection/tree/main/blocks
- **含まれるブロック**:
  - Embed, Fragment, Table, Video
  - Accordion, Breadcrumbs, Carousel, Modal
  - Quote, Search, Tabs, Form（非推奨）

**Block Party:**
- AEM開発者コミュニティが公開したブロック集
- コミュニティ主導の再利用可能なコード
- Adobeはメンテナンス非責任

### DOM vs. Markup

**マークアップ（サーバーレから配信）:**
- クリーンで読み取り可能なセマンティックHTML
- セクション、ブロック、デフォルトコンテンツを含む
- 構造はシンプルで直観的

**拡張されたDOM（クライアントサイド）:**
- JavaScript（scripts.js）で拡張
- ラッパー`<div>`の追加
- 勡力的なCSSクラスとデータ属性の追加
- AEM Block Loaderで使用される

**2ステッププロセス:**
1. サーバーがクリーンなマークアップをレンダリング
2. JavaScriptがDOMを拡張してスタイリング可能に

**例:**

**シンプルマークアップ:**
```html
<section>
  <h1>Title</h1>
  <p>Body text</p>
</section>
```

**拡張されたDOM:**
```html
<section class="section" data-aue-resource="...">
  <div class="section-metadata" data-aue-type="richtext" data-aue-prop="...">
    <h1 class="heading-h1">Title</h1>
  </div>
  <div class="default-content">
    <p data-aue-type="richtext" data-aue-prop="..." data-aue-resource="...">Body text</p>
  </div>
</section>
```

### David's Modelの14のルール

**David Nueschelerによるコンテンツモデリングのベストプラクティス:**

#### Rule #1: Default Contentを優先
- ブロックはオーサリングサイドでテーブルとして表示されるため、直観的でない
- 可能な限りデフォルトコンテンツを使用
- 著者にとってブロックは魅力的ではない

#### Rule #2: ネストされたブロックは禁止
- ネストされたブロックはオーサリングが非常に困難
- フラグメント（他ドキュメントの参照）やリンク（オートブロッキング）を活用

#### Rule #3: 行・列スパンの制限
- ヘーブルのセル結合は管理が困難（特にWord Online）
- 複雑なスパン構造になる場合、別の構造を検討

#### Rule #4: 完全修飾URLのみ
- オーサリングは完全修飾URLを扱い
- 相対URLはAEMか開発者が処理

#### Rule #5: リストの扱い
- シンプルなリストはWordやGoogle Docsのリスト機能でOK
- 複雑なリスト項目（例：カード）はブロックテーブルの行として表現

#### Rule #6: ボタンのコンテキスト継承
- 段行に独立したボタンをコンテキストから継承
- ヒーロイタトーンで、セクション背景色が反転する等
- 明示的な選択（primary vs secondary）は太字/斜体で表現

#### Rule #7: ファイル名はオーサリングに重要
- トレイリングスラッシュを削除してクリーンなURLを維持
- SEO影響を評価して301リダイレクト

#### Rule #8: アクセス制御とコンテンツグルーピング
- オーサリングチーム構造に合わせてコンテンツをグループ化
- シンプルなアクセス制御を維持

#### Rule #9: ブロック数とバリアントの制限
- 過大なブロックライブラリと多数のバリアントは望ましくない
- 使用頻度基準で非推奨ブロックを削除

#### Rule #10: 列数の制限
- 多数の列はオーサリングに不向き
- デフォルトコンテンツの不適切な使用の兆候

#### Rule #11: Block Collectionのコンテンツモデルを使用
- Block Collectionに類似した機能を持つブロックは同様のコンテンツモデルを使用

#### Rule #12: フラグメントは有害な場合も
- 同一コンテンツが複数ページで使用される場合に有用
- ネストされたフラグメントはオーサリング体験を損なう
- SEO的に重要なコンテンツはページに直接配置

#### Rule #13: 画像altテキストのセマンティクスを過負荷しない
- altテキスト内の隠れた情報は発見困難
- 例外的な場合のみ推奨

#### Rule #14: 名前/値ペアは設定専用
- セクションやページのメタデータとしてのみ使用
- デフォルトコンテンツ概念を名前/値ペアにマッピングしない

### Auto Blocking（オートブロッキング）

**概要:**
- デフォルトコンテンツとメタデータをブロックに自動変換
- オーサリングによる物理的なブロック作成が不要
- ページデコレーションプロセスの初期段階で実行

**主な使用例:**
1. **アーティクルヘッダー**: `<h1>`、最初の画像、ブログ著者、公称日から自動生成
2. **YouTubeリンク**: リンクを貼り付けるだけでembedブロックとして自動変換
3. **ビデオ**: ビデオリンクを貼り付けるだけでビデオプレーヤーを埋め込み
4. **モーダル**: 外部アプリケーションの埋め込み
5. **フォーム**: 外部フォームの統合

**実装場所:**
- `scripts.js`の`buildAutoBlocks()`関数
- 参照実装: [Adobe Blog](https://github.com/adobe/blog), [AEM Boilerplate](https://github.com/adobe/aem-boilerplate)

### Section Metadata（セクションメタデータ）

**概要:**
- セクションに適用されるデータ属性を定義
- 名前/値ペアとして表現

**用途:**
- セクションの背景画像
- スタイルオプション（セクションレベルのCSSクラス追加）
- 設定値の保存（スプレッドシート入力等）

**例:**
```
+-----------------------------------------------------------------------+
| Featured Articles                                                     |
+=======================================================================+
| source   | /content/site/articles.json |
+-----------------------------------------------------------------------+
| keywords | Developer,Courses                                          |
+-----------------------------------------------------------------------+
| limit    | 4                                                          |
+-----------------------------------------------------------------------+
```

**実装:**
- `model` IDが`section`のコンポーネントモデルを定義
- 名前/値ペアとしてテーブルにレンダリング
- セクションにデータ属性として追加

### Block Optionsの拡張

**複数オプションの組み合わせ:**
```json
{
  "classes": "variant-a",
  "classes_background": "light",
  "classes_fullwidth": true
}
```
↓
```html
<div class="teaser variant-a light fullwidth">
```

**エレメントグルーピングによる複数オプション:**
- `classes_`で始まる全てのフィールドがグループ化
- 真理値、テキスト配列、またはブーリアン値を可能
- ブーリアン値の場合、プロパティ名がブロックオプションとして追加

**セレクトフィールドでの使用:**
- トグルスイッチでオプションのON/OFFを切り替え
- オーサリング体験を向上

---

## 🔍 次回の調査予定

- **高度なブロックパターン**:
  - Container Blocksの詳細な実装例
  - 複雑な子要素のモデリング
  - Composite Multi-Fieldsの実践的な使用例

- **拡張機能の探索**:
  - Universal Editorの拡張（Toolbar & Properties Panel）
  - 継承、MSM、翻訳ワークフローの統合

- **パフォーマンス最適化**:
  - 画像・ビデオの最適化テクニック
  - Lazy Loadingの実装
  - CDNキャッシュ戦略

- **セキュリティと権限管理**:
  - 技術アカウントの詳細な設定
  - フォルダーレベルのアクセス制御

- **マルチサイト管理**:
  - Repoless Multi-Site Managerの詳細
  - コンテンツ構造の中央管理

---

**最終更新: 2026年2月13日 19:05 (JST)**

*このレポートは自律調査エージェントMiraによって作成・更新されました。*
