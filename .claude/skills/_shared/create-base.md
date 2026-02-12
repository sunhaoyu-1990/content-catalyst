# Create Base Module

**共享模块**：用户画像 + 内容生成 + 资料分析整合核心逻辑

## 模块说明

本模块定义了内容创作的通用逻辑，包括：
1. 用户画像 onboarding 系统
2. 本地资料分析与整合
3. 内容类型与模式生成
4. 平台定制接口

## First-Time Setup (Onboarding)

### 检查用户画像

```
1. Read references/user-profile.md
2. If initialized: false or file doesn't exist → Run onboarding
3. If initialized: true → Proceed to content creation
```

### Onboarding 问题设计

**第一层：共享信息**（所有平台通用）

使用 AskUserQuestion 工具收集：

1. **使用场景**：你主要用这个平台做什么？
   - 内容创作
   - 个人品牌建设
   - 商业推广
   - 学习分享
   - Other

2. **内容领域**：你主要分享什么内容？
   - [平台特定选项，如：AI/科技、创业/商业、个人成长...]
   - Other

3. **语言风格**：你希望的内容风格是？
   - 专业严肃
   - 轻松幽默
   - 犀利观点
   - 温暖亲和
   - Other

**第二层：平台特定问题**（各平台定制 5-7 个问题）

各平台在自己的 SKILL.md 中定义平台特定问题。

### 用户画像格式

`references/user-profile.md`：

```yaml
---
initialized: true  # false 时触发 onboarding

account:
  domains: ["领域1", "领域2"]  # 内容领域
  target_audience: "目标受众描述"
  persona_style: "人设风格"
  language: "zh-CN"  # 或 "en-US"

scoring:
  trending: 4      # 热度权重
  controversy: 2   # 争议性权重
  value: 3         # 高价值权重
  relevance: 1     # 相关性权重
  threshold: 7     # 入选阈值

# 平台特定字段（可选）
{platform}_specific_fields:
  field1: value1
  field2: value2
---
```

## 本地资料分析整合

### Step 1: 检查本地资料

```
1. 检查 assets/materials/ 目录是否有新文件
2. 检查 assets/analyzed/ 目录是否有分析结果
3. If 有新资料且无分析结果 → 提示用户是否需要分析
4. If 有分析结果 → 整合到内容生成中
```

### 目录结构

```
assets/
├── materials/           # 用户本地资料
│   ├── reports/         # PDF 报告
│   ├── notes/           # Markdown 笔记
│   └── articles/        # 文本资料
├── analyzed/            # 分析结果缓存
│   └── {material_name}-analysis.md
└── templates/           # 参考内容模板
    ├── {type1}/
    ├── {type2}/
    └── ...
```

### 资料分析输出格式

`assets/analyzed/{material}-analysis.md`：

```markdown
# {资料名称} 分析报告

## 资料信息
- 文件名: {filename}
- 文件类型: {pdf/markdown/txt}
- 分析时间: {timestamp}
- 资料来源: {本地/网络}

## 核心内容提取

### 关键观点
1. 观点1: ...
2. 观点2: ...

### 重要数据
- 数据1: ...
- 数据2: ...

### 案例/实例
1. 案例1: ...
2. 案例2: ...

### 引用原文
> {重要引用段}

## 创作建议
- **推荐类型**: {适合的内容类型}
- **切入角度**: {建议的切入点}
- **可补充点**: {需要进一步搜索的内容}

## 标签
{自动生成的标签，用于检索}
```

### 支持格式

- **PDF**: 使用 Read 工具读取（支持 PDF）
- **Markdown**: 使用 Read 工具读取
- **纯文本**: 使用 Read 工具读取
- **Word 文档**: 用户转换为 Markdown/纯文本后分析

## 内容类型与模式

### 内容类型定义

各平台定义 5 种平台特定的内容类型：

| 类型 | 风格 | 使用场景 |
|------|------|---------|
| 类型 1 | ... | ... |
| 类型 2 | ... | ... |
| ... | ... | ... |

### 输出格式

各平台定义自己的输出格式（短文/长文/笔记等）

## Step 1: 加载上下文

```
1. Read references/user-profile.md → Get persona, style
2. 检查 assets/analyzed/ 目录:
   - If 有分析结果 → 整合到创作中
   - If 无 → 询问是否需要分析本地资料
3. Check assets/templates/{type}/ → Look for user reference posts
4. If no references → Use default patterns from references/post-patterns.md
```

## Step 2: 确定创作素材

- 优先使用本地资料分析结果（如有）
- 整合网络搜索素材（如有）
- 用户提供的话题/指令

## Step 3: 应用模式

```
Read references/post-patterns.md for the specific post type pattern
```

## Step 4: 生成内容

```
Create content following:
1. User's persona style
2. Post type pattern
3. Reference examples (if available)
4. Material analysis results (if available)
```

## 输出格式

```markdown
# 内容创作

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
- 预期效果: {expected engagement}

下一步：运行 /{platform}-publish 发布到草稿箱
```

## Template Priority

1. **User templates first**: Check `assets/templates/{type}/`
2. **Material analysis**: Check `assets/analyzed/`
3. **Default patterns**: Use `references/post-patterns.md`

## 平台定制接口

### 用户画像字段

各平台可在 user-profile.md 中添加平台特定字段：

```yaml
# 知乎示例
zhihu_fields:
  expertise_level: "专家 / 进阶 / 入门"
  answer_frequency: "每天 / 每周 / 不定期"

# 小红书示例
xiaohongshu_fields:
  content_vertical: "美妆 / 时尚 / 美食 / 旅行 / ..."
  target_gender: "女性 / 男性 / 全部"
  content_tone: "种草 / 测评 / 日常 / ..."

# 领英示例
linkedin_fields:
  industry_type: "科技 / 金融 / 教育 / ..."
  job_role: "高管 / 工程师 / 销售 / ..."
  content_goal: "个人品牌 / 公司推广 / 行业影响"
```

### 内容类型定义

各平台在 `references/post-patterns.md` 中定义 5 种内容类型：

```markdown
# {Platform} 内容类型模式

## 类型 1: {类型名称}
- 风格特点: ...
- 使用场景: ...
- 结构模板: ...
- 示例: ...

## 类型 2: ...
...
```

## 使用方式

**平台 skill 引用方式**：

```markdown
# {platform}-create/SKILL.md

---
继承: ../_shared/create-base.md
---

## {Platform} 特定定制

### Onboarding 问题
1. 平台特定问题 1
2. 平台特定问题 2
...

### 内容类型（5种）
1. 类型1: ...
2. 类型2: ...
...

### 用户画像字段
{platform}_specific_fields:
  field1: value1
```

## 资源文件

### references/user-profile.md
用户定制信息（首次 onboarding 生成）

### references/post-patterns.md
默认内容类型模式（5 种类型）

### assets/templates/
用户提供的参考内容，按类型组织

### assets/materials/
用户本地资料存放目录

### assets/analyzed/
资料分析结果缓存
