---
name: xiaohongshu-create
description: Create viral 小红书 content based on user's persona and post patterns. Use when user wants to write 小红书 content, create posts, or mentions "create 小红书 post", "write 小红书 content", "xiaohongshu-create". Supports 5 post styles with customizable templates. First-time users go through onboarding to set up profile.
---

# 小红书 Create

Create viral 小红书 content based on user's persona and post patterns.

## 继承模块

```
继承: ../_shared/create-base.md
```

本模块继承共享的用户画像、内容生成和资料分析整合核心逻辑，并定制小红书特定的内容类型和 onboarding 问题。

## First-Time Setup (Onboarding)

**Check user profile before creating content:**

1. Read `references/user-profile.md`
2. If `initialized: false` or file doesn't exist → Run onboarding
3. If `initialized: true` → Proceed to content creation

### Layer 1: 共享信息（所有平台通用）

使用 AskUserQuestion 工具收集：

1. **使用场景**：你主要用小红书做什么？
   - Options: 分享生活, 种草推荐, 记录成长, 商业推广, Other

2. **内容领域**：你主要分享什么内容？
   - Options: 美妆护肤, 穿搭时尚, 美食探店, 生活方式, Other

3. **语言风格**：你希望的内容风格是？
   - Options: 亲切可爱, 专业认真, 轻松幽默, 真实接地气, Other

### Layer 2: 小红书特定问题

使用 AskUserQuestion 工具收集小红书特定问题：

1. **目标性别**：你的内容主要面向哪个群体？
   - Options: 女性, 男性, 全部

2. **内容风格**：你更喜欢哪种风格？
   - Options: 图文并茂（图片为主）, 文字为主, 视频, Other

3. **发布频率**：你计划多久发布一次？
   - Options: 每天, 每周, 每月, 不定期

After collecting answers, update `references/user-profile.md` with `initialized: true`.

## Content Types

### 小红书特定内容类型（5种）

| Type | Style | Use When |
|------|-------|----------|
| **种草笔记** | 图文并茂，突出产品优势 | 产品推荐、好物分享 |
| **测评分享** | 真实体验，客观评价 | 多产品对比、使用心得 |
| **生活方式** | 生活场景，个人品味 | 日常记录、生活分享 |
| **美妆教程** | 步骤详细，易于跟随 | 技能教学、步骤演示 |
| **穿搭灵感** | 视觉呈现，搭配建议 | 穿搭展示、搭配技巧 |

### Output Formats

小红书支持的内容格式：

- **种草笔记**: 图文笔记形式，100-1000字 + 5-9 张图片
- **视频笔记**: 短视频形式，15秒-5分钟
- **图文文章**: 纯文字形式，较少使用

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
- 产品文档: {material_1}
- 用户反馈: {material_2}

是否需要分析这些资料并整合到小红书内容创作中？
```

### 分析结果整合

```
正在整合资料分析结果：
- {material}: {key_insights}

基于本地资料和您的个人风格，为您创作以下小红书内容...
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
加载小红书创作者Profile规范：
1. Read ../../profiles/content-creator-common.md
   → 应用通用创作规范（核心原则、质量标准、图片规范）
2. Read ../../profiles/xiaohongshu-creator.md
   → 应用小红书特定规范（种草风格、亲和力、emoji使用）

确保生成内容符合：
✅ Profile的核心原则（真实性、用户价值、平台适配）
✅ Profile的内容质量标准（真实性、实用性、种草价值）
✅ Profile的格式规范（标题、emoji、段落、标签）
✅ Profile的语言风格要求（亲切自然、口语化、情绪饱满）
```

### Step 2: 确定格式

Based on content length and complexity:
- **种草笔记**: 图文并茂，100-1000 字
- **测评分享**: 真实体验，300-1500 字
- **生活方式**: 生活记录，200-1000 字
- **美妆教程**: 步骤教学，500-2000 字
- **穿搭灵感**: 搭配展示，200-800 字

### Step 3: 应用模式

Read `references/post-patterns.md` for the specific post type pattern.

### Step 4: 生成内容

Create content following:
1. User's persona style
2. Post type pattern
3. Reference examples (if available)
4. Material analysis results (if available)

**小红书内容特点**:
- 图文并茂（图片说明很重要）
- 标题吸引眼球（SEO 优化）
- 表情符号丰富
- 话题标签 #话题

## Output Format

```markdown
# 小红书内容创作

## 选题
{topic}

## 内容类型
{content_type}

## 风格
{post_style}

---

## 标题
{吸引眼球的标题，20字内}

## 正文
{生成的内容主体，包含：
- 介绍/开场
- 核心内容（分点说明）
- 个人体验/感受
- 使用建议/推荐
- 结尾/互动引导}

## 话题标签
#话题1 #话题2 #话题3

---

## 创作说明
- 素材来源: {本地资料 / 网络搜索 / 用户输入}
- 参考类型: {参考的内容类型}
- 图片建议: {图片数量和风格建议}
- 预期效果: {expected_effect}

下一步：运行 /xiaohongshu-publish 发布到小红书草稿箱
```

## Template Priority

1. **User templates first**: Check `assets/templates/{type}/`
2. **Material analysis**: Check `assets/analyzed/`
3. **Default patterns**: Use `references/post-patterns.md`

Example:
```
Creating 种草笔记:
1. Check assets/templates/种草笔记/
2. If files exist → Learn style from examples
3. If empty → Use default pattern from post-patterns.md
```

## Resources

### references/user-profile.md
User customization info (shared across all xiaohongshu skills)

### references/post-patterns.md
Default viral post patterns for 5 categories

### assets/materials/
User-provided local materials for analysis

### assets/analyzed/
Analysis results of local materials

### assets/templates/
User-provided reference posts organized by type:
- `种草笔记/` - 种草笔记类参考
- `测评分享/` - 测评分享类参考
- `生活方式/` - 生活方式类参考
- `美妆教程/` - 美妆教程类参考
- `穿搭灵感/` - 穿搭灵感类参考

## Example

User: `/xiaohongshu-create AI学习工具推荐 --type 种草笔记`

1. Read user-profile.md → persona: 亲切可爱、女性用户、图文并茂
2. Check assets/materials/ → No new materials
3. Check assets/templates/种草笔记/ → empty
4. Read post-patterns.md → Get 种草笔记 pattern
5. Generate content:

```markdown
# 小红书内容创作

## 选题
AI学习工具推荐

## 内容类型
种草笔记

## 风格
亲切可爱、图文并茂

---

## 标题
📚 学生党必看！这些AI学习工具让我的效率提升了300%！

## 正文
姐妹们！今天必须给你们种草我最近发现的宝藏AI学习工具...

[详细内容...]

## 话题标签
#AI工具 #学习效率 #学生党 #种草推荐 #好物分享

---

## 创作说明
- 素材来源: 网络搜索 + 个人使用体验
- 参考类型: 种草笔记
- 图片建议: 5-7张，展示工具界面和使用效果
- 预期效果: 引发购买/使用欲望，获得收藏和点赞

下一步：运行 /xiaohongshu-publish 发布到小红书草稿箱
```

## Integration

After creation, suggest:
```
小红书内容创作完成！

- 类型: {content_type}
- 字数: {word_count}
- 图片建议: {image_count} 张
- 话题标签: {tags}

下一步：运行 /xiaohongshu-publish 发布到小红书草稿箱
```

## Directory Structure

```
xiaohongshu-create/
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
        ├── 种草笔记/
        ├── 测评分享/
        ├── 生活方式/
        ├── 美妆教程/
        └── 穿搭灵感/
```
