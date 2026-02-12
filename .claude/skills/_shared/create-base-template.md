---
name: {platform}-create
description: Create viral {Platform} content based on user's persona and post patterns. Use when user wants to write {Platform} content, create posts, or mentions "create {Platform} post", "write {Platform} content", "{platform}-create". Supports {content_type_count} post styles with customizable templates. First-time users go through onboarding to set up profile.
---

# {Platform} Create

Create viral {Platform} content based on user's persona and post patterns.

## 继承模块

```
继承: ../_shared/create-base.md
```

本模块继承共享的用户画像、内容生成和资料分析整合核心逻辑，并定制 {Platform} 特定的内容类型和 onboarding 问题。

## First-Time Setup (Onboarding)

**Check user profile before creating content:**

1. Read `references/user-profile.md`
2. If `initialized: false` or file doesn't exist → Run onboarding
3. If `initialized: true` → Proceed to content creation

### Layer 1: 共享信息（所有平台通用）

使用 AskUserQuestion 工具收集：

1. **使用场景**：你主要用 {Platform} 做什么？
   - Options: 内容创作, 个人品牌建设, 商业推广, 学习分享, Other

2. **内容领域**：你主要分享什么内容？
   - Options: {domain_options_1}, {domain_options_2}, {domain_options_3}, Other

3. **语言风格**：你希望的内容风格是？
   - Options: 专业严肃, 轻松幽默, 犀利观点, 温暖亲和, Other

### Layer 2: {Platform} 特定问题

使用 AskUserQuestion 工具收集 {Platform} 特定问题：

1. **{Platform} 问题 1**: {question_1}
   - Options: {option_1}, {option_2}, {option_3}, Other

2. **{Platform} 问题 2**: {question_2}
   - Options: {option_1}, {option_2}, {option_3}, Other

3. **{Platform} 问题 3**: {question_3}
   - Options: {option_1}, {option_2}, {option_3}, Other

After collecting answers, update `references/user-profile.md` with `initialized: true`.

## Content Types

### {Platform} 特定内容类型（5种）

| Type | Style | Use When |
|------|-------|----------|
| **{type_1}** | {type_1_style} | {type_1_usage} |
| **{type_2}** | {type_2_style} | {type_2_usage} |
| **{type_3}** | {type_3_style} | {type_3_usage} |
| **{type_4}** | {type_4_style} | {type_4_usage} |
| **{type_5}** | {type_5_style} | {type_5_usage} |

### Output Formats

{Platform} 支持的输出格式：

{output_formats_list}

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
- {material_1}: {brief_description}
- {material_2}: {brief_description}

是否需要分析这些资料并整合到内容创作中？
```

### 分析结果整合

```
正在整合资料分析结果：
- {material}: {key_insights}

基于本地资料和用户画像，为您创作以下内容...
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

### Step 2: 确定格式

Based on content length and complexity:
{format_criteria}

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
# {Platform} 内容创作

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

下一步：运行 /{platform}-publish 发布到草稿箱
```

## Template Priority

1. **User templates first**: Check `assets/templates/{type}/`
2. **Material analysis**: Check `assets/analyzed/`
3. **Default patterns**: Use `references/post-patterns.md`

Example:
```
Creating {type_1} post:
1. Check assets/templates/{type_1}/
2. If files exist → Learn style from examples
3. If empty → Use default pattern from post-patterns.md
```

## Resources

### references/user-profile.md
User customization info (shared across all {platform} skills)

### references/post-patterns.md
Default viral post patterns for 5 categories

### assets/materials/
User-provided local materials for analysis

### assets/analyzed/
Analysis results of local materials

### assets/templates/
User-provided reference posts organized by type:
- `{type_1}/` - {type_1} 类参考
- `{type_2}/` - {type_2} 类参考
- `{type_3}/` - {type_3} 类参考
- `{type_4}/` - {type_4} 类参考
- `{type_5}/` - {type_5} 类参考

## Example

User: `/{platform}-create {example_topic} --type {type_1}`

1. Read user-profile.md → persona: {example_persona}
2. Check assets/materials/ → No new materials
3. Check assets/templates/{type_1}/ → empty
4. Read post-patterns.md → Get {type_1} pattern
5. Generate content:

```markdown
# {Platform} 内容创作

## 选题
{example_topic}

## 内容类型
{type_1}

## 风格
{example_style}

---

## 正文
{示例内容}

---

## 创作说明
- 素材来源: 用户输入
- 参考类型: {type_1}
- 预期效果: {expected_effect}

下一步：运行 /{platform}-publish 发布到草稿箱
```

## Integration

After creation, suggest:
```
内容创作完成！

- 类型: {content_type}
- 字数: {word_count}
- 预计阅读: {read_time}

下一步：运行 /{platform}-publish 发布到{Platform}草稿箱
```

## Configuration Files

### user-profile.md 模板

创建 `references/user-profile.md`：

```yaml
---
initialized: true  # false 时触发 onboarding

account:
  domains: ["{domain_1}", "{domain_2}"]  # 内容领域
  target_audience: "{target_audience_description}"
  persona_style: "{persona_style}"
  language: "zh-CN"  # 或 "en-US"

scoring:
  trending: 4      # 热度权重
  controversy: 2   # 争议性权重
  value: 3         # 高价值权重
  relevance: 1     # 相关性权重
  threshold: 7     # 入选阈值

# {Platform} 特定字段
{platform}_fields:
  field1: value1
  field2: value2
---
```

### post-patterns.md 模板

创建 `references/post-patterns.md`：

```markdown
# {Platform} 内容类型模式

## {type_1}: {type_1_full_name}

**风格特点**：{type_1_characteristics}

**使用场景**：{type_1_scenarios}

**结构模板**：
```
{type_1_template}
```

**示例**：
```
{type_1_example}
```

## {type_2}: ...
...
```

### 目录结构

创建以下目录结构：

```
assets/
├── materials/           # 用户本地资料
│   ├── reports/         # PDF 报告
│   ├── notes/           # Markdown 笔记
│   └── articles/        # 文本资料
├── analyzed/            # 分析结果缓存
│   └── README.md        # 说明文件
└── templates/           # 参考内容模板
    ├── {type_1}/
    ├── {type_2}/
    ├── {type_3}/
    ├── {type_4}/
    └── {type_5}/
```

---

## 使用说明

**创建平台 skill 步骤**：

1. 复制此模板文件到 `{platform}-create/SKILL.md`
2. 替换模板变量：
   - `{Platform}` → 平台名称（中文）
   - `{platform}` → 平台标识符（英文小写）
   - `{type_1}` ~ `{type_5}` → 平台特定的 5 种内容类型
   - `{domain_options}` → 平台特定的领域选项
   - `{question}` → 平台特定的 onboarding 问题
   - `{example_topic}` → 示例主题
   - `{example_persona}` → 示例人设
3. 创建 `references/user-profile.md` 和 `post-patterns.md`
4. 创建 `assets/` 目录结构
5. 根据平台特性调整内容类型定义和输出格式
