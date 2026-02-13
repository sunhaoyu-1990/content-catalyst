# Content Catalyst

<div align="center">

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Claude Code](https://img.shields.io/badge/Claude_Code-Compatible-green.svg)
![Platforms](https://img.shields.io/badge/platforms-4-blueviolet.svg)

**Claude AIベースマルチプラットフォームコンテンツ自動作成システム**

[クイックスタート](#クイックスタート) • [機能](#機能) • [コントリビューション](#コントリビューション)

[English](README.en.md) | [中文版](README.md)

</div>

---

## 📖 概要

[Content Catalyst](https://github.com/sunhaoyu-1990/content-catalyst)は、[Claude Code](https://claude.ai/code)向けに構築されたAI駆動コンテンツ作成アシスタントです。Zhihu、LinkedIn、Xiaohongshu（小紅書）、X/Twitterなど複数のプラットフォーム向けにコンテンツ作成を自動化します。

### 主な機能

- ✅ **マルチプラットフォーム対応** - Zhihu、LinkedIn、Xiaohongshu、X/Twitter
- ✅ **自然言語トリガー** - 自然言語で要件を伝えるだけで起動
- ✅ **スマートリサーチ** - 4段階検索戦略による包括的な資料収集
- ✅ **トピックスコアリング** - 10点満点評価システムによるトピック選定
- ✅ **自動品質レビュー** - 6次元品質評価
- ✅ **自動画像マーキング** - AI画像生成プロンプト付き
- ✅ **デュアルモード** - シンプルモード + 完全モード

---

<a name="クイックスタート"></a>
## 🚀 クイックスタート

### 前提条件

- [Claude Code](https://claude.ai/code)がインストールされていること
- Markdownの基礎知識

### インストール

```bash
# 1. リポジトリをクローン
git clone https://github.com/sunhaoyu-1990/content-catalyst.git
cd content-catalyst

# 2. スキルをClaude Codeのスキルディレクトリにコピー
# Windows: %USERPROFILE%\.claude\skills\
# macOS/Linux: ~/.claude/skills/
cp -r .claude/skills/* ~/.claude/skills/

# 3. ルールをコピー
cp -r .claude/rules/* ~/.claude/rules/

# 4. プロファイルをコピー
cp -r .claude/profiles/* ~/.claude/profiles/
```

### 初回使用

**自然言語で要件を伝えるだけ：**

```
ユーザー: 「AIライティングツールのおすすめ」についてXiaohongshuの投稿を書いて

Claude: [自動実行: 作成 → 品質レビュー → 画像マーキング]
        完了！コンテンツは workspace/ai-writing-tools/content.md に保存されました
```

**これだけ！** Claudeが自動的にコンテンツ作成、品質レビュー、画像マーキングを行います。

---

<a name="機能"></a>
## 🎯 2つのモード

両方のモードは**自然言語会話でトリガー**されます。Claudeがすべて自動的に処理します。

### シンプルモード（初心者向け）

**使用シーン：**
- クイックコンテンツ作成
- バージョン管理不要
- クロスプラットフォーム再利用不要

**使い方：** Claudeに必要なことを伝えるだけ

```
ユーザー: 「AIライティングツール」についてXiaohongshuの投稿を書いて

Claude: [自動: 作成 → レビュー → マーク]
        完了！コンテンツを保存しました。
```

**自動フロー：**
```
自然言語リクエスト → 作成 → 自動レビュー → 自動マーク → 完了
```

### 完全モード（上級者向け）

**使用シーン：**
- 体系的なコンテンツ管理
- バージョン管理と履歴追跡
- クロスプラットフォームコンテンツ再利用

**使い方：** 「完全モード」キーワードを追加

```
ユーザー: 完全モードを使って「AIライティングツール」についてZhihuとLinkedIn向けにコンテンツを作成して

Claude: 完全モードワークフローを開始します：

        Step 1: ディレクトリ構造を作成
        workspace/ai-writing-tools/2026-02-13/
        ├── 00_collect/zhihu/
        ├── 00_collect/linkedin/
        ├── 01_filter/
        ├── 02_create/zhihu/
        ├── 02_create/linkedin/
        └── 03_publish/

        Step 2: 資料収集（4段階検索）
        [collectスキルを自動実行]

        Step 3: トピック選定（10点評価）
        [filterスキルを自動実行]

        Step 4: コンテンツ作成（プラットフォーム仕様に従って）
        [createスキルを自動実行 → 品質レビュー → 画像マーキング]

        Step 5: 公開準備
        [publishスキルを自動実行]

        すべて完了！コンテンツを保存しました。
```

**自動フロー：**
```
自然言語 + 「完全モード」
    ↓
ディレクトリ構造を自動作成
    ↓
資料を自動収集
    ↓
トピックを自動選定
    ↓
コンテンツを自動作成
    ↓
品質を自動レビュー
    ↓
画像を自動マーク
    ↓
公開を自動準備
    ↓
完了！
```

**ディレクトリ構造（自動作成）：**
```
workspace/
├── index.md                # メインインデックス（自動更新）
└── {topic}/
    └── {version}/          # 自動命名：初回は日付、以降はv2,v3...
        ├── 00_collect/     # 収集ステージ（自動生成）
        ├── 01_filter/      # 選定ステージ（自動生成）
        ├── 02_create/      # 作成ステージ（自動生成）
        ├── 03_publish/     # 公開ステージ（自動生成）
        └── task.md         # タスク追跡（自動維持）
```

---

## 📂 プロジェクト構造

```
content-catalyst/
├── .claude/
│   ├── skills/              # スキル定義
│   │   ├── _shared/         # 共有コアロジック
│   │   ├── {platform}/     # プラットフォーム別スキル
│   │   ├── content-reviewer/
│   │   └── language-simplifier/
│   ├── rules/              # 自動化ルール
│   │   ├── content-creation-complete.md
│   │   ├── content-post-checklist.md
│   │   └── content-image-marking.md
│   └── profiles/           # プラットフォーム設定
├── workspace/             # ユーザー出力
├── talk_with_ai/          # 会話ログ
├── docs/                 # ドキュメント
├── CLAUDE.md            # コア仕様
└── README.md            # このファイル
```

---

## 🎯 対応プラットフォーム

| プラットフォーム | コンテンツタイプ | スタイル |
|-----------------|------------------|----------|
| **Zhihu** | 技術記事、専門的な回答 | プロフェッショナル、詳細な分析 |
| **LinkedIn** | 業界洞察、専門的共有 | プロフェッショナル、ビジネス価値 |
| **Xiaohongshu** | 商品レビュー、体験共有 | 親しみやすさ、会話調 |
| **X (Twitter)** | 投稿、スレッド、返信 | 簡潔、拡散性 |

---

## 🛠️ アーキテクチャ

- **コアエンジン**: Claude AI (Claude Code)
- **スキルシステム**: Markdownベースのスキル定義
- **ルールシステム**: 自動トリガーワークフロー
- **スコアリングシステム**: 10点評価トピック選定

詳細なアーキテクチャは[CLAUDE.md](CLAUDE.md)を参照してください

---

## 📚 よくある例

**シンプルモード**（必要なことを伝えるだけ）：
```
ユーザー: 「AIライティングツールのおすすめ」についてXiaohongshuの投稿を書いて
ユーザー: 「プログラマー必須のパフォーマンス分析ツール」についてZhihuの回答を書いて
ユーザー: AIツールについてのツイートを書いて
```

**完全モード**（「完全モード」キーワードを追加）：
```
ユーザー: 完全モードを使って「パフォーマンス分析ツール」についてZhihu向けにコンテンツを作成して
ユーザー: 完全モードで「AIライティングツールレビュー」をZhihuとXiaohongshu向けに作成して
```

---

<a name="コントリビューション"></a>
## 🤝 コントリビューション

すべてのコントリビューションを歓迎します！詳細は[CONTRIBUTING.md](CONTRIBUTING.md)を参照してください。

### コントリビューション方法

- バグ報告
- 新機能提案
- コード提交
- ドキュメント改善

---

## 📄 ライセンス

このプロジェクトは[MIT License](LICENSE)の下で提供されています。

---

## 🌟 謝辞

- [Claude AI](https://claude.ai) - コアAIエンジン
- [Claude Code](https://claude.ai/code) - 開発環境
- すべてのコントリビューターの方々

---

<div align="center">

**[⬆ トップに戻る](#content-catalyst)**

Made with ❤️ by Content Catalyst Contributors

**[English](README.en.md) | [中文版](README.md)**

</div>
