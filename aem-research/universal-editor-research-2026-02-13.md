# AEM Universal Editor 調査レポート

**調査日:** 2026年2月13日  
**実施者:** Mira (OpenClaw AI Agent)  
**タスク:** AEM Universal Editorの実装形式とデザインパターン調査

---

## サマリ

### 調査状況
- **ドキュメントアクセス:** 制限あり (aem.live ドキュメントが404でアクセス不可)
- **公式サイト:** https://www.aem.live/ は稼働中
- **調査方法:** 
  - web_fetch 試行 (404エラー)
  - ブラウザアクセス試行 (サービス未起動)

### 現状の課題
1. AEM LiveのドキュメントURL構造が変更されている可能性
2. Edge Deliveryに関するドキュメントに直接アクセスできない
3. Universal Editorの最新実装パターンを確認できない

---

## Universal Editorとは (既知の情報)

### 概要
AEM Universal Editorは、Adobe Experience Managerのコンテンツ編集機能を拡張するエディタで、以下の特徴を持つ：

- **クロスチャネル編集:** 異なるデバイス・チャネルで同じ編集体験
- **ヘッドレス対応:** Headless CMSとしてのAEM利用時も編集可能
- **リアルタイムプレビュー:** 編集中に即座にプレビュー可能

### 予想される実装形式

#### 1. クライアントサイド統合
```javascript
// Universal Editor の読み込み
<script src="https://www.aem.live/editor.js"></script>

// コンテナの初期化
const editor = AEM.UniversalEditor({
  container: '#editor-root',
  project: 'my-project',
  locale: 'ja-JP'
});
```

#### 2. データ通信方式
- **REST API:** GraphQLまたはREST APIでコンテンツ取得
- **WebSocket:** リアルタイム同期
- **Edge Delivery:** CDNエッジでの配信

#### 3. デザインパターン（予測）

| パターン名 | 説明 | ユースケース |
|----------|------|-------------|
| **Split View** | 左右分割のエディタ | デスクトップ編集 |
| **Overlay Mode** | ページ上にオーバーレイ | プレビューしながら編集 |
| **Inline Edit** | コンテンツを直接クリックして編集 | シンプルな編集体験 |
| **Component Palette** | コンポーネントパレットをドラッグ&ドロップ | 構築体験 |

---

## Edge Delivery について

### 既知の特徴
- **パフォーマンス:** CDNエッジでの高速配信
- **キャッシュ戦略:** Smart Cachingとパージ
- **静的生成:** Static Site Generation (SSG)
- **動的機能:** 動的コンテンツも可能

### 実装アーキテクチャ（推定）

```
[Author] → Universal Editor → AEM Content Service
                                     ↓
                              [CDN Edge] → [User]
```

---

## 次回のアクション

### 優先度高
1. ブラウザサービス起動して公式ドキュメントを直接確認
2. Adobe Developer ConsoleでのAPI確認
3. GitHubのサンプルリポジトリ調査

### 優先度中
4. AEM as a Cloud ServiceのSDK確認
5. AEM Project ArchetypeのUniversal Editor統合を確認

---

## 追加調査が必要な項目

- [ ] Universal Editorの最新API仕様
- [ ] Edge Deliveryのキャッシュ戦略詳細
- [ ] React/Angular SPAとの統合方法
- [ ] モバイル編集体験
- [ ] パフォーマンスベストプラクティス

---

## 参考リソース

### 公式リンク
- AEM Live: https://www.aem.live/
- AEM Project Archetype: https://github.com/adobe/aem-project-archetype

### 技術リソース
- AEM Core Components: https://github.com/adobe/aem-core-wcm-components
- Adobe Experience League: https://experienceleague.adobe.com/

---

**ステータス:** 調査中 (ドキュメントアクセス課題あり)  
**次回更新:** ブラウザサービス起動後
