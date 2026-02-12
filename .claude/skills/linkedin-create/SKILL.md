---
name: linkedin-create
description: Create viral 领英 content based on user's persona and post patterns. Use when user wants to write 领英 content, create posts, or mentions "create linkedin post", "write 领英 content", "linkedin-create". Supports 5 post styles with customizable templates. First-time users go through onboarding to set up profile.
---

# 领英 Create

Create viral 领英 content based on user's persona and post patterns.

## 继承模块

```
继承: ../_shared/create-base.md
```

本模块继承共享的用户画像、内容生成和资料分析整合核心逻辑，并定制领英特定的内容类型和 onboarding 问题。

## First-Time Setup (Onboarding)

**Check user profile before creating content:**

1. Read `references/user-profile.md`
2. If `initialized: false` or file doesn't exist → Run onboarding
3. If `initialized: true` → Proceed to content creation

### Layer 1: 共享信息（所有平台通用）

使用 AskUserQuestion 工具收集：

1. **使用场景**：你主要用领英做什么？
   - Options: 个人品牌建设, 企业推广, 行业分享, 职场发展, Other

2. **内容领域**：你主要分享什么内容？
   - Options: 科技/AI, 商业/管理, 营销/销售, 职业/发展, Other

3. **语言风格**：你希望的内容风格是？
   - Options: 专业权威, 真实诚恳, 数据驱动, 故事化, Other

### Layer 2: 领英特定问题

使用 AskUserQuestion 工具收集领英特定问题：

1. **目标受众**：你的内容主要面向谁？
   - Options: 企业决策者, 同行专业人士, 潜在客户, 招聘者, Other

2. **内容形式**：你更喜欢哪种形式？
   - Options: 文章为主, 动态为主, 文档分享, 多媒体, Other

3. **发布频率**：你计划多久发布一次？
   - Options: 每天, 每周, 每月, 不定期

After collecting answers, update `references/user-profile.md` with `initialized: true`.

## Content Types

### 领英特定内容类型（5种）

| Type | Style | Use When |
|------|-------|----------|
| **行业洞察** | 数据驱动，权威分析 | 行业趋势、市场分析 |
| **专业分享** | 技术深度，实用建议 | 技术解析、最佳实践 |
| **案例研究** | 真实案例，ROI 展示 | 企业实践、成功案例 |
| **职场发展** | 个人经验，成长建议 | 职场技能、管理心得 |
| **观点文章** | 个人见解，讨论互动 | 热点评论、观点表达 |

### Output Formats

领英支持的内容格式：

- **文章**: 长文形式，1000-3000 字，支持富文本
- **动态**: 短内容，100-1300 字，纯文本
- **文档**: PDF/PPT 上传分享
- **视频**: 短视频形式

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
- 行业报告: {material_1}
- 案例研究: {material_2}

是否需要分析这些资料并整合到领英内容创作中？
```

### 分析结果整合

```
正在整合资料分析结果：
- {material}: {key_insights}

基于本地资料和您的个人风格，为您创作以下领英内容...
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
加载领英创作者Profile规范：
1. Read ../../profiles/content-creator-common.md
   → 应用通用创作规范（核心原则、质量标准、图片规范）
2. Read ../../profiles/linkedin-creator.md
   → 应用领英特定规范（职业化、商业思维、洞察驱动）

确保生成内容符合：
✅ Profile的核心原则（真实性、平台适配、用户价值）
✅ Profile的内容质量标准（商业价值、专业性、深度要求）
✅ Profile的格式规范（标题结构、数据呈现、案例格式）
✅ Profile的语言风格要求（职业化、建设性、数据驱动）
```

### Step 2: 确定格式

Based on content length and complexity:
- **行业洞察**: 数据驱动，1500-3000 字
- **专业分享**: 技术深度，1000-2000 字
- **案例研究**: 真实案例，1200-2500 字
- **职场发展**: 个人经验，800-1500 字
- **观点文章**: 个人见解，300-1300 字

### Step 3: 应用模式

Read `references/post-patterns.md` for the specific post type pattern.

### Step 4: 生成内容

Create content following:
1. User's persona style
2. Post type pattern
3. Reference examples (if available)
4. Material analysis results (if available)

**领英内容特点**:
- 专业权威（引用数据和研究）
- 结构清晰（使用标题和列表）
- 互动导向（提出问题和观点）
- 话题标签 #话题
- 提及相关人 @mention

## Output Format

```markdown
# 领英内容创作

## 选题
{topic}

## 内容类型
{content_type}

## 风格
{post_style}

---

## 标题
{专业标题，30字内}

## 正文
{生成的内容主体，包含：
- 开场（引入主题）
- 核心内容（分点说明，数据支撑）
- 个人见解/经验
- 行动建议/总结
- 互动引导（提问）}

## 话题标签
#话题1 #话题2 #话题3

---

## 创作说明
- 素材来源: {本地资料 / 网络搜索 / 用户输入}
- 参考类型: {参考的内容类型}
- 数据来源: {引用的数据和研究}
- 预期效果: {expected_effect}

下一步：运行 /linkedin-publish 发布到领英
```

## Template Priority

1. **User templates first**: Check `assets/templates/{type}/`
2. **Material analysis**: Check `assets/analyzed/`
3. **Default patterns**: Use `references/post-patterns.md`

Example:
```
Creating 行业洞察:
1. Check assets/templates/行业洞察/
2. If files exist → Learn style from examples
3. If empty → Use default pattern from post-patterns.md
```

## Resources

### references/user-profile.md
User customization info (shared across all linkedin skills)

### references/post-patterns.md
Default viral post patterns for 5 categories

### assets/materials/
User-provided local materials for analysis

### assets/analyzed/
Analysis results of local materials

### assets/templates/
User-provided reference posts organized by type:
- `行业洞察/` - 行业洞察类参考
- `专业分享/` - 专业分享类参考
- `案例研究/` - 案例研究类参考
- `职场发展/` - 职场发展类参考
- `观点文章/` - 观点文章类参考

## Example

User: `/linkedin-create AI business transformation --type 行业洞察`

1. Read user-profile.md → persona: 专业权威、企业决策者、数据驱动
2. Check assets/materials/ → No new materials
3. Check assets/templates/行业洞察/ → empty
4. Read post-patterns.md → Get 行业洞察 pattern
5. Generate content:

```markdown
# 领英内容创作

## 选题
AI business transformation

## 内容类型
行业洞察

## 风格
专业权威、数据驱动

---

## 标题
72% 的企业已开始 AI 转型，你的公司准备好了吗？

## 正文
根据 McKinsey 2025 年最新报告...

[详细内容...]

你的公司如何应对 AI 转型？欢迎在评论区分享。

## 话题标签
#AI #DigitalTransformation #BusinessStrategy #Innovation #Leadership

---

## 创作说明
- 素材来源: 网络搜索 + 行业报告
- 参考类型: 行业洞察
- 数据来源: McKinsey 2025 AI Report
- 预期效果: 建立专业权威，引发讨论

下一步：运行 /linkedin-publish 发布到领英
```

## Integration

After creation, suggest:
```
领英内容创作完成！

- 类型: {content_type}
- 字数: {word_count}
- 话题标签: {tags}

下一步：运行 /linkedin-publish 发布到领英
```

## Directory Structure

```
linkedin-create/
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
        ├── 行业洞察/
        ├── 专业分享/
        ├── 案例研究/
        ├── 职场发展/
        └── 观点文章/
```
