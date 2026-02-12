---
name: zhihu-create
description: Create viral 知乎 content based on user's persona and post patterns. Use when user wants to write 知乎 content, create posts, or mentions "create 知乎 post", "write 知乎 content", "zhihu-create". Supports 5 post styles with customizable templates. First-time users go through onboarding to set up profile.
---

# 知乎 Create

Create viral 知乎 content based on user's persona and post patterns.

## 继承模块

```
继承: ../_shared/create-base.md
```

本模块继承共享的用户画像、内容生成和资料分析整合核心逻辑，并定制知乎特定的内容类型和 onboarding 问题。

## First-Time Setup (Onboarding)

**Check user profile before creating content:**

1. Read `references/user-profile.md`
2. If `initialized: false` or file doesn't exist → Run onboarding
3. If `initialized: true` → Proceed to content creation

### Layer 1: 共享信息（所有平台通用）

使用 AskUserQuestion 工具收集：

1. **使用场景**：你主要用知乎做什么？
   - Options: 分享知识, 个人品牌建设, 回答问题, 写专栏文章, Other

2. **内容领域**：你主要分享什么内容？
   - Options: AI/科技, 编程/开发, 产品/设计, 创业/商业, 学术/研究, Other

3. **语言风格**：你希望的内容风格是？
   - Options: 专业严肃, 深入浅出, 通俗易懂, 幽默风趣, Other

### Layer 2: 知乎特定问题

使用 AskUserQuestion 工具收集知乎特定问题：

1. **专业程度**：你的内容专业程度如何？
   - Options: 专家级别（行业资深）, 进阶级别（有一定经验）, 入门级别（学习者视角）

2. **回答频率**：你计划多久创作一次内容？
   - Options: 每天, 每周, 每月, 不定期

3. **内容偏好**：你更倾向于哪种内容形式？
   - Options: 问题回答（短篇幅）, 专栏文章（长篇幅）, 想法分享（短动态）

After collecting answers, update `references/user-profile.md` with `initialized: true`.

## Content Types

### 知乎特定内容类型（5种）

| Type | Style | Use When |
|------|-------|----------|
| **专业回答** | 深度专业 | 技术问题、专业领域、知识分享 |
| **专栏文章** | 长文深度 | 系统性知识、深度分析、完整观点 |
| **经验分享** | 实战导向 | 项目经验、踩坑记录、成长感悟 |
| **学术讨论** | 理论严谨 | 学术观点、理论分析、研究探讨 |
| **观点评论** | 有态度有立场 | 热点评论、行业观点、反常识思考 |

### Output Formats

知乎支持的内容格式：

- **专业回答**：问题回答形式，300-3000字，针对性强
- **专栏文章**：长文形式，1000-10000字，系统性表达
- **想法**：短动态形式，300字以内，快速分享

## 本地资料分析整合

### Step 1: 检查本地资料

```
1. 检查 assets/materials/ 目录是否有新文件
2. 检查 assets/analyzed/ 目录是否有分析结果
3. If 有新资料且无分析结果 → 提示用户是否需要分析
4. If 有分析结果 → 整合到内容生成中
```

### 资料分析提示

```
检测到本地资料：
- 技术文档: {material_1}
- 研究报告: {material_2}

是否需要分析这些资料并整合到知乎内容创作中？
```

### 分析结果整合

```
正在整合资料分析结果：
- {material}: {key_insights}

基于本地资料和您的专业背景，为您创作以下知乎内容...
```

## Creation Workflow

### Step 1: 加载上下文

```
1. Read references/user-profile.md → Get persona, style
2. 检查 assets/analyzed/ 目录:
   - If 有分析结果 → 整合到创作中
   - If 无 → 询问是否需要分析本地资料
3. Check assets/templates/{type}/ → Look for user reference posts
4. If no references → Use default patterns from references/post-patterns.md
```

### Step 1.5: 加载Profile质量规范

```
加载知乎创作者Profile规范：
1. Read ../../profiles/content-creator-common.md
   → 应用通用创作规范（核心原则、质量标准、图片规范）
2. Read ../../profiles/zhihu-creator.md
   → 应用知乎特定规范（专业性、深度、语言风格）

确保生成内容符合：
✅ Profile的核心原则（真实性、平台适配、用户价值、人工审核、原创性）
✅ Profile的内容质量标准（专业深度、数据支撑、逻辑严密）
✅ Profile的格式规范（标题、章节、代码块）
✅ Profile的语言风格要求（专业、严谨、有深度）
```

### Step 2: 确定格式

Based on content length and complexity:
- **专业回答**：单个问题回答，聚焦具体问题
- **专栏文章**：系统长文，适合深度论述
- **想法**：短动态，适合快速分享观点

### Step 3: 应用模式

Read `references/post-patterns.md` for the specific post type pattern.

### Step 4: 生成内容

Create content following:
1. User's persona style
2. Post type pattern
3. Reference examples (if available)
4. Material analysis results (if available)

## Output Format

```markdown
# 知乎内容创作

## 选题
{topic}

## 内容类型
{content_type}

## 风格
{post_style}

---

## 正文
{生成的内容主体}

---

## 创作说明
- 素材来源: {本地资料 / 网络搜索 / 用户输入}
- 参考类型: {参考的内容类型}
- 预期效果: {expected_effect}
- 字数: {word_count}

下一步：运行 /zhihu-publish 发布到知乎草稿箱
```

## Template Priority

1. **User templates first**: Check `assets/templates/{type}/`
2. **Material analysis**: Check `assets/analyzed/`
3. **Default patterns**: Use `references/post-patterns.md`

Example:
```
Creating 专业回答:
1. Check assets/templates/专业回答/
2. If files exist → Learn style from examples
3. If empty → Use default pattern from post-patterns.md
```

## Resources

### references/user-profile.md
User customization info (shared across all zhihu skills)

### references/post-patterns.md
Default viral post patterns for 5 categories

### assets/materials/
User-provided local materials for analysis

### assets/analyzed/
Analysis results of local materials

### assets/templates/
User-provided reference posts organized by type:
- `专业回答/` - 专业回答类参考
- `专栏文章/` - 专栏文章类参考
- `经验分享/` - 经验分享类参考
- `学术讨论/` - 学术讨论类参考
- `观点评论/` - 观点评论类参考

## Example

User: `/zhihu-create 如何快速上手 Claude 4.5 API --type 专业回答`

1. Read user-profile.md → persona: 专业严肃、专家级别
2. Check assets/materials/ → No new materials
3. Check assets/templates/专业回答/ → empty
4. Read post-patterns.md → Get 专业回答 pattern
5. Generate content:

```markdown
# 知乎内容创作

## 选题
如何快速上手 Claude 4.5 API

## 内容类型
专业回答

## 风格
专业严谨、深入浅出

---

## 正文
要快速上手 Claude 4.5 API，建议按以下步骤进行...

### 1. 环境准备
...

### 2. 获取 API 密钥
...

### 3. 第一个调用
...

### 4. 最佳实践
...

---

## 创作说明
- 素材来源: 官方文档 + 实战经验
- 参考类型: 专业回答
- 预期效果: 帮助开发者快速上手
- 字数: 约 1200 字

下一步：运行 /zhihu-publish 发布到知乎草稿箱
```

## Integration

After creation, suggest:
```
知乎内容创作完成！

- 类型: {content_type}
- 字数: {word_count}
- 预计阅读: {read_time}

下一步：运行 /zhihu-publish 发布到知乎草稿箱
```

## Directory Structure

```
zhihu-create/
├── SKILL.md                          # 主技能文件
├── references/
│   ├── user-profile.md               # 用户画像（onboarding 生成）
│   └── post-patterns.md              # 内容类型模式
└── assets/
    ├── materials/                     # 用户本地资料
    │   ├── reports/                   # PDF 报告
    │   ├── notes/                     # Markdown 笔记
    │   └── articles/                  # 文本资料
    ├── analyzed/                      # 分析结果缓存
    └── templates/                     # 参考内容模板
        ├── 专业回答/
        ├── 专栏文章/
        ├── 经验分享/
        ├── 学术讨论/
        └── 观点评论/
```
