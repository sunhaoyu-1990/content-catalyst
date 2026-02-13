# Content Catalyst

<div align="center">

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Claude Code](https://img.shields.io/badge/Claude_Code-Compatible-green.svg)
![Platforms](https://img.shields.io/badge/platforms-4-blueviolet.svg)

**Multi-Platform Content Creation Automation System Based on Claude AI**

[Quick Start](#quick-start) • [Features](#features) • [Contributing](#contributing)

[中文版](README.md) | [日本語版](README.ja.md)

</div>

---

## 📖 Overview

[Content Catalyst](https://github.com/sunhaoyu-1990/content-catalyst) is an AI-powered content creation assistant built for [Claude Code](https://claude.ai/code). It automates content production for multiple platforms including Zhihu, LinkedIn, Xiaohongshu, and X/Twitter.

### Key Features

- ✅ **Multi-Platform Support** - Zhihu, LinkedIn, Xiaohongshu, X/Twitter
- ✅ **Natural Language Trigger** - Just describe what you need in plain language
- ✅ **Smart Research** - 4-round search strategy for comprehensive material collection
- ✅ **Topic Scoring** - 10-point scoring system for topic selection
- ✅ **Auto Quality Review** - 6-dimensional quality assessment
- ✅ **Auto Image Marking** - Includes AI-generated image prompts
- ✅ **Dual Modes** - Simple mode + Complete mode

---

<a name="quick-start"></a>
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

**Just describe what you need in natural language:**

```
User: Help me write a Xiaohongshu post about "AI Writing Tools Recommendation"

Claude: [Auto execute: Create → Quality Review → Image Marking]
        Done! Content saved to workspace/ai-writing-tools/content.md
```

**That's it!** Claude will automatically create content, run quality review, and add image markers.

---

<a name="features"></a>
## 🎯 Two Modes

Both modes are triggered by **natural language conversation**. Claude handles everything automatically.

### Simple Mode (Recommended for Beginners)

**Use Cases:**
- Quick content creation
- No version management needed
- No cross-platform reuse needed

**How to Use:** Just tell Claude what you need

```
User: Help me write a Xiaohongshu post about "AI Writing Tools"

Claude: [Auto: Create → Review → Mark]
        Done! Content saved.
```

**Automated Flow:**
```
Natural Language Request → Create → Auto Review → Auto Mark → Done
```

### Complete Mode (Recommended for Advanced Users)

**Use Cases:**
- Systematic content management
- Version control and history tracking
- Cross-platform content reuse

**How to Use:** Add "complete mode" keyword

```
User: I want to use complete mode to create content about "AI Writing Tools" for Zhihu and LinkedIn

Claude: Starting complete mode workflow:

        Step 1: Creating directory structure
        workspace/ai-writing-tools/2026-02-13/
        ├── 00_collect/zhihu/
        ├── 00_collect/linkedin/
        ├── 01_filter/
        ├── 02_create/zhihu/
        ├── 02_create/linkedin/
        └── 03_publish/

        Step 2: Collecting materials (4-round search)
        [Auto executing collect skill]

        Step 3: Filtering topics (10-point scoring)
        [Auto executing filter skill]

        Step 4: Creating content (per platform specs)
        [Auto executing create skill → Quality review → Image marking]

        Step 5: Publish preparation
        [Auto executing publish skill]

        All done! Content saved.
```

**Automated Flow:**
```
Natural Language + "Complete Mode"
    ↓
Auto Create Directory Structure
    ↓
Auto Collect Materials
    ↓
Auto Filter Topics
    ↓
Auto Create Content
    ↓
Auto Quality Review
    ↓
Auto Image Marking
    ↓
Auto Publish Preparation
    ↓
Done!
```

**Directory Structure (Auto Created):**
```
workspace/
├── index.md                # Main index (auto updated)
└── {topic}/
    └── {version}/          # Auto naming: date for first, v2,v3... for later
        ├── 00_collect/     # Collect stage (auto generated)
        ├── 01_filter/      # Filter stage (auto generated)
        ├── 02_create/      # Create stage (auto generated)
        ├── 03_publish/     # Publish stage (auto generated)
        └── task.md         # Task tracking (auto maintained)
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

## 📚 Common Examples

**Simple Mode** (just describe your needs):
```
User: Help me write a Xiaohongshu post about "AI Writing Tools Recommendation"
User: Write a Zhihu answer for "What are the must-have performance analysis tools for programmers"
User: Help me write a tweet about AI tools
```

**Complete Mode** (add "complete mode" keyword):
```
User: I want to use complete mode to create content about "Performance Analysis Tools" for Zhihu
User: Please use complete mode to help me create "AI Writing Tools Review" for Zhihu and Xiaohongshu
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
