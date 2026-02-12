---
name: {platform}-filter
description: Score and filter topics for {Platform} content creation using weighted criteria. Use when user wants to evaluate collected materials, filter topics by score, or mentions "filter topics", "score materials", "{platform}-filter", "选题筛选". Applies {score_count}-point scoring system with customizable weights.
---

# {Platform} Filter

Score and filter collected materials for {Platform} content creation. Topics scoring ≥{threshold} points enter the creation pool.

## 继承模块

```
继承: ../_shared/filter-base.md
```

本模块继承共享的评分系统核心逻辑，并定制 {Platform} 特定的评分权重和内容类型映射。

## Scoring System (满分 {max_score} 分)

{Platform} 特定的评分维度和权重：

| 评分维度 | 权重 | 说明 |
|---------|------|------|
| **{dimension_1}** | {weight_1} 分 | {dimension_1_description} |
| **{dimension_2}** | {weight_2} 分 | {dimension_2_description} |
| **{dimension_3}** | {weight_3} 分 | {dimension_3_description} |
| **{dimension_4}** | {weight_4} 分 | {dimension_4_description} |

**阈值**：≥{threshold} 分进入创作池

## Prerequisites

- Materials from {platform}-collect (or manual input)
- User profile from {platform}-create/references/user-profile.md (for relevance scoring)

## Workflow

### Input

Accept materials from:
1. **{platform}-collect output** - Structured material report
2. **Manual list** - User-provided topics/URLs
3. **Raw text** - Unstructured content to evaluate
4. **Material analysis** - Local material analysis results

### Scoring Process

For each material/topic:

**1. {dimension_1} ({dimension_1_en_name}: 0-{weight_1})**
```
{weight_1}分: {dimension_1_level_4}
{weight_1_minus_1}分: {dimension_1_level_3}
{weight_1_minus_2}分: {dimension_1_level_2}
1分: {dimension_1_level_1}
0分: {dimension_1_level_0}
```

**2. {dimension_2} ({dimension_2_en_name}: 0-{weight_2})**
```
{weight_2}分: {dimension_2_level_2}
{weight_2_minus_1}分: {dimension_2_level_1}
0分: {dimension_2_level_0}
```

**3. {dimension_3} ({dimension_3_en_name}: 0-{weight_3})**
```
{weight_3}分: {dimension_3_level_3}
{weight_3_minus_1}分: {dimension_3_level_2}
{weight_3_minus_2}分: {dimension_3_level_1}
0分: {dimension_3_level_0}
```

**4. {dimension_4} ({dimension_4_en_name}: 0-{weight_4})**
```
{weight_4}分: {dimension_4_level_1}
0分: {dimension_4_level_0}
```

### Relevance Scoring

Check user profile at: `{platform}-create/references/user-profile.md`
If not found, assume domains: [{default_domain_1}, {default_domain_2}, {default_domain_3}]

### Output Format

```markdown
# 选题筛选报告

## 筛选时间
{timestamp}

## 用户定位
- 领域: {domains}
- 人设: {persona_style}
- 平台: {Platform}

## 筛选结果

### 入选创作池 (≥{threshold}分)

#### 1. {Topic Title} - **{total_score}分**
| {dimension_1} | {dimension_2} | {dimension_3} | {dimension_4} |
|------|------|------|------|
| {score_1}/{weight_1} | {score_2}/{weight_2} | {score_3}/{weight_3} | {score_4}/{weight_4} |

- **推荐类型**: [{Platform} 特定内容类型]
- **推荐风格**: [风格类型]
- **创作角度**: 建议的切入点
- **核心观点**: 可提炼的关键论点
- **素材来源**: {collect/资料分析/用户输入}

#### 2. ...
...

### 待定 ({threshold_minus_2}-{threshold_minus_1}分)
- {Topic} - {score}分 - {原因}

### 淘汰 (<{threshold_minus_2}分)
- {Topic} - {score}分 - {原因}

## 创作建议

入选 {n} 个选题，建议优先级：
1. {最高分选题} - 理由
2. {次高分选题} - 理由

下一步：运行 `/{platform}-create {选题}` 开始创作
```

## Content Type Mapping

根据素材特点推荐 {Platform} 特定内容类型：

| 素材特点 | 推荐内容类型 | 说明 |
|---------|-------------|------|
| {characteristic_1} | {type_1} | {type_1_description} |
| {characteristic_2} | {type_2} | {type_2_description} |
| {characteristic_3} | {type_3} | {type_3_description} |
| {characteristic_4} | {type_4} | {type_4_description} |
| {characteristic_5} | {type_5} | {type_5_description} |

## Execution Steps

1. **Load materials** from {platform}-collect or user input
2. **Read user profile** for relevance scoring
3. **Score each material** on 4 criteria
4. **Calculate totals** and sort by score
5. **Categorize**: ≥{threshold} (入选), {threshold_minus_2}-{threshold_minus_1} (待定), <{threshold_minus_2} (淘汰)
6. **Generate recommendations** for top topics
7. **Map content types** based on material characteristics
8. **Output report** with next steps

## Example

Input from {platform}-collect:
```
素材1: {example_topic_1}
素材2: {example_topic_2}
素材3: {example_topic_3}
```

Scoring:
```
{example_topic_1}:
- {dimension_1}: {weight_1}/{weight_1} ({reason_1})
- {dimension_2}: {score_2}/{weight_2} ({reason_2})
- {dimension_3}: {weight_3}/{weight_3} ({reason_3})
- {dimension_4}: {weight_4}/{weight_4} ({reason_4})
- 总分: {total_score}/{max_score} ✓ 入选

{example_topic_2}:
- {dimension_1}: {score_1}/{weight_1} ({reason_1})
- {dimension_2}: {weight_2}/{weight_2} ({reason_2})
- {dimension_3}: {weight_3}/{weight_3} ({reason_3})
- {dimension_4}: {weight_4}/{weight_4} ({reason_4})
- 总分: {total_score_2}/{max_score} ✓ 入选

{example_topic_3}:
- {dimension_1}: {score_1}/{weight_1} ({reason_1})
- {dimension_2}: {score_2}/{weight_2} ({reason_2})
- {dimension_3}: {score_3}/{weight_3} ({reason_3})
- {dimension_4}: {score_4}/{weight_4} ({reason_4})
- 总分: {total_score_3}/{max_score} × 待定
```

## Customization

Users can customize weights in user-profile.md:
```yaml
scoring:
  {dimension_1_en_lower}: {weight_1}
  {dimension_2_en_lower}: {weight_2}
  {dimension_3_en_lower}: {weight_3}
  {dimension_4_en_lower}: {weight_4}
  threshold: {threshold}
```

## Configuration

### scoring-weights.md 模板

创建 `references/scoring-weights.md`：

```markdown
# {Platform} 评分权重

## 评分维度

| 维度 | 权重 | 说明 |
|------|------|------|
| {dimension_1} | {weight_1} | {dimension_1_description} |
| {dimension_2} | {weight_2} | {dimension_2_description} |
| {dimension_3} | {weight_3} | {dimension_3_description} |
| {dimension_4} | {weight_4} | {dimension_4_description} |

## 评分标准

### {dimension_1} ({dimension_1_en_name}: 0-{weight_1})
{weight_1}分: {dimension_1_level_4}
{weight_1_minus_1}分: {dimension_1_level_3}
{weight_1_minus_2}分: {dimension_1_level_2}
1分: {dimension_1_level_1}
0分: {dimension_1_level_0}

### {dimension_2} ({dimension_2_en_name}: 0-{weight_2})
{weight_2}分: {dimension_2_level_2}
{weight_2_minus_1}分: {dimension_2_level_1}
0分: {dimension_2_level_0}

### {dimension_3} ({dimension_3_en_name}: 0-{weight_3})
{weight_3}分: {dimension_3_level_3}
{weight_3_minus_1}分: {dimension_3_level_2}
{weight_3_minus_2}分: {dimension_3_level_1}
0分: {dimension_3_level_0}

### {dimension_4} ({dimension_4_en_name}: 0-{weight_4})
{weight_4}分: {dimension_4_level_1}
0分: {dimension_4_level_0}

## 入选阈值
≥{threshold} 分进入创作池
```

## Integration

After filtering, suggest:
```
筛选完成！{n} 个选题入选创作池。

推荐优先创作：{top_topic}（{score}分）

下一步：运行 `/{platform}-create {top_topic}` 开始创作
```

## Tips

- For trending topics, prioritize {dimension_1}
- For controversial topics, prioritize {dimension_2}
- For high-value content, prioritize {dimension_3}
- For brand alignment, prioritize {dimension_4}
- Adjust weights based on account strategy

## Resources

### references/scoring-weights.md
{Platform} 特定的评分权重配置

### {platform}-create/references/user-profile.md
用户画像（用于相关性评分）

### ../_shared/filter-base.md
共享的评分系统核心逻辑

---

## 使用说明

**创建平台 skill 步骤**：

1. 复制此模板文件到 `{platform}-filter/SKILL.md`
2. 替换模板变量：
   - `{Platform}` → 平台名称（中文）
   - `{platform}` → 平台标识符（英文小写）
   - `{dimension_1}` ~ `{dimension_4}` → 平台特定的评分维度
   - `{weight_1}` ~ `{weight_4}` → 各维度权重
   - `{threshold}` → 入选阈值
   - `{max_score}` → 总分
   - `{type_1}` ~ `{type_5}` → 平台特定的 5 种内容类型
3. 创建 `references/scoring-weights.md` 并定义评分标准
4. 根据平台特性调整内容类型映射

**知乎示例**：
- dimension_1: 专业性 (4分)
- dimension_2: 可信度 (3分)
- dimension_3: 热度 (2分)
- dimension_4: 相关性 (1分)
- threshold: 7

**小红书示例**：
- dimension_1: 热度 (5分)
- dimension_2: 种草价值 (3分)
- dimension_3: 争议性 (2分)
- dimension_4: 相关性 (0分)
- threshold: 7

**领英示例**：
- dimension_1: 商业价值 (4分)
- dimension_2: 专业性 (3分)
- dimension_3: 热度 (2分)
- dimension_4: 相关性 (1分)
- threshold: 7
