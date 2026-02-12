---
name: zhihu-filter
description: Score and filter topics for 知乎 content creation using weighted criteria. Use when user wants to evaluate collected materials, filter topics by score, or mentions "filter topics", "score materials", "zhihu-filter", "选题筛选". Applies 10-point scoring system with customizable weights.
---

# 知乎 Filter

Score and filter collected materials for 知乎 content creation. Topics scoring ≥7 points enter the creation pool.

## 继承模块

```
继承: ../_shared/filter-base.md
```

本模块继承共享的评分系统核心逻辑，并定制知乎特定的评分权重和内容类型映射。

## Scoring System (满分 10 分)

知乎特定的评分维度和权重：

| 评分维度 | 权重 | 说明 |
|---------|------|------|
| **专业性** | 4 分 | 内容专业深度和技术准确性 |
| **可信度** | 3 分 | 来源可信程度和论证严谨性 |
| **热度** | 2 分 | 讨论热度和关注度 |
| **相关性** | 1 分 | 与账号定位的匹配度 |

**阈值**：≥7 分进入创作池

## Prerequisites

- Materials from zhihu-collect (or manual input)
- User profile from zhihu-create/references/user-profile.md (for relevance scoring)

## Workflow

### Input

Accept materials from:
1. **zhihu-collect output** - Structured material report
2. **Manual list** - User-provided topics/URLs
3. **Raw text** - Unstructured content to evaluate
4. **Material analysis** - Local material analysis results

### Scoring Process

For each material/topic:

**1. 专业性 (Professionalism: 0-4)**
```
4分: 专业深度高，技术细节准确，有独特见解
3分: 专业内容准确，有一定深度
2分: 基础专业内容，信息正确但缺乏深度
1分: 通用信息，专业性较弱
0分: 信息不准确或缺乏专业价值
```

**2. 可信度 (Credibility: 0-3)**
```
3分: 官方来源、权威机构、或经充分论证
2分: 有一定可信度，来源较为可靠
1分: 来源一般，可信度有限
0分: 来源不明或可信度低
```

**3. 热度 (Trending: 0-2)**
```
2分: 当前热门话题，大量讨论
1分: 近期热点，关注度上升
0分: 稳定或小众话题，关注度有限
```

**4. 相关性 (Relevance: 0-1)**
```
1分: 与账号定位高度相关
0分: 与账号定位关联较弱
```

### Relevance Scoring

Check user profile at: `zhihu-create/references/user-profile.md`
If not found, assume domains: [AI/科技, 编程/开发, 产品/设计]

### Output Format

```markdown
# 选题筛选报告

## 筛选时间
{timestamp}

## 用户定位
- 领域: {domains}
- 专业程度: {expertise_level}
- 人设: {persona_style}
- 平台: 知乎

## 筛选结果

### 入选创作池 (≥7分)

#### 1. {Topic Title} - **{total_score}分**
| 专业性 | 可信度 | 热度 | 相关性 |
|------|--------|------|--------|
| {professional}/4 | {credibility}/3 | {trending}/2 | {relevance}/1 |

- **推荐类型**: [专业回答/专栏文章/经验分享/学术讨论/观点评论]
- **推荐风格**: [风格类型]
- **创作角度**: 建议的切入点
- **核心观点**: 可提炼的关键论点
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

下一步：运行 `/zhihu-create {选题}` 开始创作
```

## Content Type Mapping

根据素材特点推荐知乎特定的内容类型：

| 素材特点 | 推荐内容类型 | 说明 |
|---------|-------------|------|
| 技术性强 + 专业度高 | 专业回答 | 深度技术解析，适合回答专业问题 |
| 争议性 + 独特观点 | 观点评论 | 有态度有立场的评论文章 |
| 实用性强 + 可操作 | 经验分享 | 个人经验和实操指南 |
| 理论深 + 论证严谨 | 学术讨论 | 理论分析和学术探讨 |
| 热度高 + 系统性强 | 专栏文章 | 对热点的深度系统分析 |

## Execution Steps

1. **Load materials** from zhihu-collect or user input
2. **Read user profile** for relevance scoring
3. **Score each material** on 4 criteria (专业性、可信度、热度、相关性)
4. **Calculate totals** and sort by score
5. **Categorize**: ≥7 (入选), 5-6 (待定), <5 (淘汰)
6. **Generate recommendations** for top topics
7. **Map content types** based on material characteristics
8. **Output report** with next steps

## Example

Input from zhihu-collect:
```
素材1: Claude 4.5 Opus发布
素材2: AI编程助手对比评测
素材3: 前端工程化最佳实践
```

Scoring:
```
Claude 4.5 Opus发布:
- 专业性: 4/4 (官方文档，技术细节准确)
- 可信度: 3/3 (官方来源)
- 热度: 2/2 (刚发布，热门话题)
- 相关性: 1/1 (AI/科技相关)
- 总分: 10/10 ✓ 入选
- 推荐类型: 专业回答

AI编程助手对比评测:
- 专业性: 3/4 (技术分析较为深入)
- 可信度: 2/3 (第三方评测)
- 热度: 1/2 (持续话题)
- 相关性: 1/1 (编程相关)
- 总分: 7/10 ✓ 入选
- 推荐类型: 经验分享

前端工程化最佳实践:
- 专业性: 3/4 (实践经验)
- 可信度: 2/3 (个人经验)
- 热度: 1/2 (稳定话题)
- 相关性: 1/1 (开发相关)
- 总分: 7/10 ✓ 入选
- 推荐类型: 经验分享
```

## Customization

Users can customize weights in user-profile.md:
```yaml
scoring:
  professionalism: 4  # 专业性权重
  credibility: 3     # 可信度权重
  trending: 2        # 热度权重
  relevance: 1       # 相关性权重
  threshold: 7       # 入选阈值
```

## Configuration

### scoring-weights.md

`references/scoring-weights.md` 配置文件包含知乎的评分标准详情。

## Integration

After filtering, suggest:
```
筛选完成！{n} 个选题入选创作池。

推荐优先创作：{top_topic}（{score}分）

下一步：运行 `/{platform}-create {top_topic}` 开始创作
```

## Tips

- 对于技术话题，优先专业性维度
- 对于热点话题，关注热度和争议性
- 对于经验分享，重视可信度和实用性
- 对于学术讨论，强调专业性和论证严谨性
- 根据账号定位调整相关性权重

## Resources

### references/scoring-weights.md
知乎特定的评分权重配置

### zhihu-create/references/user-profile.md
用户画像（用于相关性评分）

### ../_shared/filter-base.md
共享的评分系统核心逻辑
