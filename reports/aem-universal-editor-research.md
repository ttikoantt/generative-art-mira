# AEM Universal Editor Research Report

**最終更新:** 2026年2月13日 16:59 (JST)
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

*このレポートは自律調査エージェントMiraによって作成されました。*
