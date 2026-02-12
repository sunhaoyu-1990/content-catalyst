# Content Catalyst

<div align="center">

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Claude Code](https://img.shields.io/badge/Claude_Code-Compatible-green.svg)
![Platforms](https://img.shields.io/badge/platforms-4-blueviolet.svg)

**Claude AIベースマルチプラットフォームコンテンツ自動作成システム**

[クイックスタート](#-クイックスタート) • [機能](#-主な機能) • [コントリビューション](#-コントリビューション)

[English](README.en.md) | [中文版](README.md)

</div>

---

## 📖 概要

[Content Catalyst](https://github.com/sunhaoyu-1990/content-catalyst)は、[Claude Code](https://claude.ai/code)向けに構築されたAI駆動コンテンツ作成アシスタントです。Zhihu、LinkedIn、Xiaohongshu（小紅書）、X/Twitterなど複数のプラットフォーム向けにコンテンツ作成を自動化します。

### 主な機能

- ✅ **マルチプラットフォーム対応** - Zhihu、LinkedIn、Xiaohongshu、X/Twitter
- ✅ **スマートリサーチ** - 4段階検索戦略による包括的な資料収集
- ✅ **トピックスコアリング** - 10点満点評価システムによるトピック選定
- ✅ **ワンクリック作成** - 自動化されたコンテンツ生成ワークフロー
- ✅ **自動品質レビュー** - 6次元品質評価
- ✅ **自動画像マーキング** - AI画像生成プロンプト付き
- ✅ **デュアルモード** - シンプルモード + 完全モード

---

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

```bash
# 最も簡単な方法 - 直接コンテンツ作成
/xiaohongshu-create "AIライティングツールのおすすめ"

# システムは自動的に実行：
# 1. 資料収集
# 2. コンテンツ作成
# 3. 品質レビュー
# 4. 画像マーキング
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

## 📚 コアコマンド

```bash
# 資料収集
/{platform}-collect "トピック"

# トピックフィルタリング
/{platform}-filter

# コンテンツ作成
/{platform}-create "トピック"

# 公開準備
/{platform}-publish

# コンテンツレビュー
content-reviewerで[記事]をレビュー

# 言語簡素化
language-simplifierで"[表現]"を簡素化
```

---

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
