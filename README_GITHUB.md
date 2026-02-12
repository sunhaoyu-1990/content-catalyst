# 内容创作助手

<div align="center">

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Claude Code](https://img.shields.io/badge/Claude_Code-Compatible-green.svg)
![Platforms](https://img.shields.io/badge/platforms-4-blueviolet.svg)

**基于 Claude AI 的多平台内容创作自动化系统**

[快速开始](#-30秒快速开始) • [功能特性](#-核心特性) • [贡献指南](#-贡献)

</div>

---

## 📖 项目简介

这是一个基于 Claude AI 的内容创作助手，支持为多个平台（知乎、领英、小红书、X/Twitter）自动生成高质量内容。

### 核心特性

- ✅ **多平台支持** - 知乎、领英、小红书、X/Twitter
- ✅ **智能资料收集** - 4轮搜索策略
- ✅ **选题评分筛选** - 10分评分系统
- ✅ **一键内容生成** - 自动化创作流程
- ✅ **自动质量审查** - 6维度质量检查
- ✅ **自动图片标记** - 包含 AI 绘图 Prompt
- ✅ **双模式工作** - 极简模式 + 完整模式

---

## 🚀 30秒快速开始

### 前置要求

- [Claude Code](https://claude.ai/code) 已安装
- 基础 Markdown 知识

### 安装

```bash
# 1. 克隆仓库
git clone https://github.com/your-username/content-creation-assistant.git
cd content-creation-assistant

# 2. 复制技能文件到 Claude Code 技能目录
# Windows: %USERPROFILE%\.claude\skills\
# macOS/Linux: ~/.claude/skills/
cp -r .claude/skills/* ~/.claude/skills/

# 3. 复制规则文件
cp -r .claude/rules/* ~/.claude/rules/

# 4. 复制配置文件
cp -r .claude/profiles/* ~/.claude/profiles/
```

### 第一次使用

```bash
# 最简单的方式 - 直接创作
/xiaohongshu-create "AI写作工具推荐"

# 系统会自动：
# 1. 收集资料
# 2. 创作内容
# 3. 质量审查
# 4. 图片标记
```

---

## 📂 项目结构

```
content-creation-assistant/
├── .claude/
│   ├── skills/              # 技能定义
│   │   ├── _shared/         # 共享核心逻辑
│   │   ├── {platform}/     # 平台特定技能
│   │   ├── content-reviewer/
│   │   └── language-simplifier/
│   ├── rules/              # 自动化规则
│   │   ├── content-creation-complete.md
│   │   ├── content-post-checklist.md
│   │   └── content-image-marking.md
│   └── profiles/           # 平台配置
├── workspace/             # 创作产出（用户数据）
├── talk_with_ai/          # 对话记录（用户数据）
├── docs/                 # 详细文档
├── CLAUDE.md            # 核心规范
└── README.md            # 本文件
```

---

## 🎯 支持平台

| 平台 | 内容类型 | 风格特点 |
|------|---------|-----------|
| **知乎** | 技术文章、专业回答 | 专业严肃、深度分析 |
| **领英** | 行业洞察、专业分享 | 职业化、商业价值 |
| **小红书** | 种草笔记、测评分享 | 亲和力强、种草风格 |
| **X (Twitter)** | Posts, Threads, Replies | 简洁有力、高传播 |

---

## 🛠️ 技术架构

- **核心引擎**: Claude AI (Claude Code)
- **技能系统**: 基于 Markdown 的技能定义
- **规则系统**: 自动触发的工作流
- **评分系统**: 10分制选题筛选

详细架构请参考 [CLAUDE.md](CLAUDE.md)

---

## 📚 核心命令

```bash
# 资料收集
/{platform}-collect "主题"

# 选题筛选
/{platform}-filter

# 内容创作
/{platform}-create "选题"

# 发布准备
/{platform}-publish

# 内容审查
使用 content-reviewer 审查 [文章]

# 语言简化
使用 language-simplifier 简化 "[表达]"
```

---

## 🤝 贡献

我们欢迎各种形式的贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详情。

### 贡献方式

- 报告 Bug
- 提出新功能建议
- 提交代码
- 改进文档

---

## 📄 许可证

本项目采用 [MIT License](LICENSE) 开源协议。

---

## 🌟 致谢

- [Claude AI](https://claude.ai) - 核心 AI 引擎
- [Claude Code](https://claude.ai/code) - 开发环境
- 所有贡献者

---

<div align="center">

**[⬆ 返回顶部](#内容创作助手)**

Made with ❤️ by Content Creation Assistant Contributors

</div>
