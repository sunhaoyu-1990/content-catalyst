---
name: linkedin-filter
description: Score and filter topics for 领英 content creation using weighted criteria. Use when user wants to evaluate collected materials, filter topics by score, or mentions "filter topics", "score materials", "linkedin-filter", "选题筛选". Applies 10-point scoring system with customizable weights.
---

# 领英 Filter

Score and filter collected materials for 领英 content creation. Topics scoring ≥7 points enter the creation pool.

## 继承模块

```
继承: ../_shared/filter-base.md
```

本模块继承共享的评分系统核心逻辑，并定制领英特定的评分权重和内容类型映射。

## Scoring System (满分 10 分)

领英特定的评分维度和权重：

| 评分维度 | 权重 | 说明 |
|---------|------|------|
| **商业价值** | 4 分 | ROI、业务影响、实用性 |
| **专业性** | 3 分 | 专业深度、权威性 |
| **热度** | 2 分 | 行业关注度、讨论热度 |
| **相关性** | 1 分 | 与个人定位的相关性 |

**阈值**：≥7 分进入创作池

## Prerequisites

- Materials from linkedin-collect (or manual input)
- User profile from linkedin-create/references/user-profile.md (optional)

## Workflow

### Input

Accept materials from:
1. **linkedin-collect output** - Structured material report
2. **Manual list** - User-provided topics/URLs
3. **Raw text** - Unstructured content to evaluate
4. **Material analysis** - Local material analysis results

### Scoring Process

For each material/topic:

**1. 商业价值 (Business Value: 0-4)**
```
4分: 高商业价值，直接影响 ROI 或业务决策
3分: 中等商业价值，有明确应用场景
2分: 一般商业价值，间接参考价值
1分: 低商业价值，背景知识
0分: 无商业价值
```

**2. 专业性 (Professionalism: 0-3)**
```
3分: 高专业性，专家级深度，权威来源
2分: 中等专业性，专业见解
1分: 一般专业性，基础信息
0分: 缺乏专业性
```

**3. 热度 (Trending: 0-2)**
```
2分: 行业热门话题，高关注度
1分: 稳定话题，持续讨论
0分: 小众或冷门话题
```

**4. 相关性 (Relevance: 0-1)**
```
1分: 高度相关，符合个人定位
0分: 相关性一般或不相关
```

### Output Format

```markdown
# 选题筛选报告

## 筛选时间
{timestamp}

## 用户定位
- 领域: {domains}
- 目标受众: {target_audience}
- 人设: {persona_style}
- 平台: 领英

## 筛选结果

### 入选创作池 (≥7分)

#### 1. {Topic Title} - **{total_score}分**
| 商业价值 | 专业性 | 热度 | 相关性 |
|---------|--------|------|--------|
| {business}/4 | {professional}/3 | {trending}/2 | {relevance}/1 |

- **推荐类型**: [行业洞察/专业分享/案例研究/职场发展/观点文章]
- **推荐风格**: [风格类型]
- **创作角度**: 建议的切入点
- **商业价值**: 可提炼的商业点
- **素材来源**: {collect/资料分析/用户输入}

#### 2. ...
...

### 待定 (5-6分)
- {Topic} - {score}分 - {原因}

### 淘汰 (<5分)
- {Topic} - {score}分 - {原因}

## 创作建议

入选 {n} 个选题，建议优先级：
1. {最高分选题} - 理由
2. {次高分选题} - 理由

下一步：运行 `/linkedin-create {选题}` 开始创作
```

## Content Type Mapping

根据素材特点推荐领英特定的内容类型：

| 素材特点 | 推荐内容类型 | 说明 |
|---------|-------------|------|
| 行业报告 + 数据分析 | 行业洞察 | 权威数据 + 趋势分析 |
| 技术解析 + 实施指南 | 专业分享 | 技术深度 + 实用建议 |
| 企业案例 + ROI 分析 | 案例研究 | 真实案例 + 效果展示 |
| 职场经验 + 技能提升 | 职场发展 | 个人经验 + 成长建议 |
| 观点评论 + 行业讨论 | 观点文章 | 个人见解 + 互动讨论 |

## Execution Steps

1. **Load materials** from linkedin-collect or user input
2. **Read user profile** (optional)
3. **Score each material** on 4 criteria (商业价值、专业性、热度、相关性)
4. **Calculate totals** and sort by score
5. **Categorize**: ≥7 (入选), 5-6 (待定), <5 (淘汰)
6. **Generate recommendations** for top topics
7. **Map content types** based on material characteristics
8. **Output report** with next steps

## Example

Input from linkedin-collect:
```
素材1: AI business transformation
素材2: Leadership skills for managers
素材3: Digital marketing trends
```

Scoring:
```
AI business transformation:
- 商业价值: 4/4 (直接影响业务决策)
- 专业性: 3/3 (权威报告，专家分析)
- 热度: 2/2 (行业热门话题)
- 相关性: 1/1 (符合定位)
- 总分: 10/10 ✓ 入选
- 推荐类型: 行业洞察

Leadership skills for managers:
- 商业价值: 3/4 (有明确应用场景)
- 专业性: 2/3 (专业见解)
- 热度: 1/2 (稳定话题)
- 相关性: 1/1 (符合定位)
- 总分: 7/10 ✓ 入选
- 推荐类型: 职场发展

Digital marketing trends:
- 商业价值: 2/4 (间接参考价值)
- 专业性: 2/3 (专业见解)
- 热度: 1/2 (稳定话题)
- 相关性: 0/1 (相关性一般)
- 总分: 5/10 × 待定
```

## Customization

Users can customize weights in user-profile.md:
```yaml
scoring:
  business_value: 4  # 商业价值权重
  professionalism: 3  # 专业性权重
  trending: 2        # 热度权重
  relevance: 1       # 相关性权重
  threshold: 7       # 入选阈值
```

## Configuration

### scoring-weights.md

`references/scoring-weights.md` 配置文件包含领英的评分标准详情。

## Integration

After filtering, suggest:
```
筛选完成！{n} 个选题入选创作池。

推荐优先创作：{top_topic}（{score}分）

下一步：运行 `/linkedin-create {top_topic}` 开始创作
```

## Tips

- 对于行业话题，优先商业价值和专业性
- 对于案例研究，重视商业价值和热度
- 对于职场话题，关注专业性和相关性
- 对于观点文章，平衡专业性和热度
- 领英内容重视权威性和数据支撑

## Resources

### references/scoring-weights.md
领英特定的评分权重配置

### linkedin-create/references/user-profile.md
用户画像

### ../_shared/filter-base.md
共享的评分系统核心逻辑
