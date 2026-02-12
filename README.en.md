# Content Catalyst

<div align="center">

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Claude Code](https://img.shields.io/badge/Claude_Code-Compatible-green.svg)
![Platforms](https://img.shields.io/badge/platforms-4-blueviolet.svg)

**Multi-Platform Content Creation Automation System Based on Claude AI**

[Quick Start](#-quick-start) • [Features](#-features) • [Contributing](#-contributing)

[中文版](README.md) | [日本語版](README.ja.md)

</div>

---

## 📖 Overview

[Content Catalyst](https://github.com/sunhaoyu-1990/content-catalyst) is an AI-powered content creation assistant built for [Claude Code](https://claude.ai/code). It automates content production for multiple platforms including Zhihu, LinkedIn, Xiaohongshu, and X/Twitter.

### Key Features

- ✅ **Multi-Platform Support** - Zhihu, LinkedIn, Xiaohongshu, X/Twitter
- ✅ **Smart Research** - 4-round search strategy for comprehensive material collection
- ✅ **Topic Scoring** - 10-point scoring system for topic selection
- ✅ **One-Click Creation** - Automated content generation workflow
- ✅ **Auto Quality Review** - 6-dimensional quality assessment
- ✅ **Auto Image Marking** - Includes AI-generated image prompts
- ✅ **Dual Modes** - Simple mode + Complete mode

---

## 🚀 Quick Start

### Prerequisites

- [Claude Code](https://claude.ai/code) installed
- Basic Markdown knowledge

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/sunhaoyu-1990/content-catalyst.git
cd content-catalyst

# 2. Copy skills to Claude Code skills directory
# Windows: %USERPROFILE%\.claude\skills\
# macOS/Linux: ~/.claude/skills/
cp -r .claude/skills/* ~/.claude/skills/

# 3. Copy rules
cp -r .claude/rules/* ~/.claude/rules/

# 4. Copy profiles
cp -r .claude/profiles/* ~/.claude/profiles/
```

### First Use

```bash
# Simplest way - Create content directly
/xiaohongshu-create "AI Writing Tools Recommendation"

# System will automatically:
# 1. Collect materials
# 2. Create content
# 3. Quality review
# 4. Image marking
```

---

## 📂 Project Structure

```
content-catalyst/
├── .claude/
│   ├── skills/              # Skill definitions
│   │   ├── _shared/         # Shared core logic
│   │   ├── {platform}/     # Platform-specific skills
│   │   ├── content-reviewer/
│   │   └── language-simplifier/
│   ├── rules/              # Automation rules
│   │   ├── content-creation-complete.md
│   │   ├── content-post-checklist.md
│   │   └── content-image-marking.md
│   └── profiles/           # Platform configurations
├── workspace/             # User outputs
├── talk_with_ai/          # Conversation logs
├── docs/                 # Documentation
├── CLAUDE.md            # Core specifications
└── README.md            # This file
```

---

## 🎯 Supported Platforms

| Platform | Content Types | Style |
|-----------|---------------|--------|
| **Zhihu** | Technical articles, professional answers | Professional, in-depth analysis |
| **LinkedIn** | Industry insights, professional sharing | Professional, business value |
| **Xiaohongshu** | Product reviews, experience sharing | Engaging, conversational |
| **X (Twitter)** | Posts, Threads, Replies | Concise, viral |

---

## 🛠️ Architecture

- **Core Engine**: Claude AI (Claude Code)
- **Skill System**: Markdown-based skill definitions
- **Rule System**: Auto-triggered workflows
- **Scoring System**: 10-point topic selection

For detailed architecture, see [CLAUDE.md](CLAUDE.md)

---

## 📚 Core Commands

```bash
# Material collection
/{platform}-collect "topic"

# Topic filtering
/{platform}-filter

# Content creation
/{platform}-create "topic"

# Publish preparation
/{platform}-publish

# Content review
Use content-reviewer to review [article]

# Language simplification
Use language-simplifier to simplify "[expression]"
```

---

## 🤝 Contributing

We welcome all forms of contribution! See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### Ways to Contribute

- Report bugs
- Suggest new features
- Submit code
- Improve documentation

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🌟 Acknowledgments

- [Claude AI](https://claude.ai) - Core AI engine
- [Claude Code](https://claude.ai/code) - Development environment
- All contributors

---

<div align="center">

**[⬆ Back to Top](#content-catalyst)**

Made with ❤️ by Content Catalyst Contributors

**[中文版](README.md) | [日本語版](README.ja.md)**

</div>
