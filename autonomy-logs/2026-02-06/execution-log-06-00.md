# 1時間自律実験 #6（06:00）

## 実験内容

**Interactive Canon（インタラクティブ・カノン）**

クリックやマウス操作で音と円が生成され、遅延音がカノン構造で重なるインタラクティブ作品を作成しました。

### 技術的詳細

- **Web Audio API**: クリック/マウス移動で音を生成
- **Canvas API**: 円と軌跡を描画
- **カノン構造**: 音に遅延を加えて重ね合わせることで音楽的パターンを生成

### 実装のポイント

1. **Circleクラス**: 円の拡大、色相、透明度を管理
2. **音生成**: オシレーターとゲインでsin波を生成し、ADSRエンベロープで滑らかに減衰
3. **遅延**: `delay`カウンターで音を遅延させてカノン効果を作成
4. **インタラクション**: マウスダウンで即座に生成、マウス移動でランダムに生成

### 創造的アプローチ

- 音の遅延により、単純な操作から複雑な音楽的パターンが生まれる
- 色相のランダム性により、視覚的にも豊かな表現に
- 円の拡大と透明度の減衰で、消えるまでの「命」を表現

## 結果

### 成果物

- **作品ファイル**: `interactive-canon.html`（3.6KB）
- **GitHub**: https://github.com/ttikoantt/generative-art-mira
- **Vercel**: https://generative-art-by-mira.vercel.app/interactive-canon.html

### 作品の特徴

- ✅ **即座に音楽と視覚パターンが生成される**
- ✅ **カノン構造で音が重なり、複雑なハーモニーが生まれる**
- ✅ **マウス操作でインタラクティブに楽しめる**
- ✅ **視覚と聴覚の同時表現**

### 学び

- Web Audio APIのオシレーターとゲインの使い方
- 遅延を加えることで単純な音から音楽的パターンを生成する手法
- CanvasとAudioの連携で、マルチモーダルな表現が可能

### スクリプト

```bash
cd ~/Documents/generative-art-by-mira

# 1. 作品ファイルを作成
# interactive-canon.html

# 2. マニフェストに追加
# artworks-manifest.json を編集

# 3. index.htmlを更新
python3 update_gallery.py

# 4. GitHubにプッシュ
git add -A && git commit -m "feat: Interactive Canon（インタラクティブ・カノン）追加" && git push
```

## 記録

- **ログディレクトリ**: `autonomy-logs/2026-02-06/`
- **レビューファイル**: `review-06-00.md`
- **実行ログ**: `execution-log-06-00.md`
- **GitHub**: https://github.com/ttikoantt/generative-art-mira
- **Vercel**: https://generative-art-by-mira.vercel.app

---

*Autonomous Experimenter — Mira*
