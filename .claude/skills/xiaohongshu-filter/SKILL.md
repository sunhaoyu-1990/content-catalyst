---
name: xiaohongshu-filter
description: Score and filter topics for 小红书 content creation using weighted criteria. Use when user wants to evaluate collected materials, filter topics by score, or mentions "filter topics", "score materials", "xiaohongshu-filter", "选题筛选". Applies 10-point scoring system with customizable weights.
---

# 小红书 Filter

Score and filter collected materials for 小红书 content creation. Topics scoring ≥7 points enter the creation pool.

## 继承模块

```
继承: ../_shared/filter-base.md
```

本模块继承共享的评分系统核心逻辑，并定制小红书特定的评分权重和内容类型映射。

## Scoring System (满分 10 分)

小红书特定的评分维度和权重：

| 评分维度 | 权重 | 说明 |
|---------|------|------|
| **热度** | 5 分 | 爆款潜力和讨论热度 |
| **种草价值** | 3 分 | 实用性和种草能力 |
| **争议性** | 2 分 | 讨论价值和互动潜力 |
| **相关性** | 0 分 | 不强制相关（小红书内容宽泛） |

**阈值**：≥7 分进入创作池

## Prerequisites

- Materials from xiaohongshu-collect (or manual input)
- User profile from xiaohongshu-create/references/user-profile.md (optional，小红书不强制相关)

## Workflow

### Input

Accept materials from:
1. **xiaohongshu-collect output** - Structured material report
2. **Manual list** - User-provided topics/URLs
3. **Raw text** - Unstructured content to evaluate
4. **Material analysis** - Local material analysis results

### Scoring Process

For each material/topic:

**1. 热度 (Trending: 0-5)**
```
5分: 当前爆款话题，大量讨论和分享
4分: 近期热门，关注度快速上升
3分: 稳定话题，持续有人讨论
2分: 小众话题，关注度有限
1分: 过时话题，几乎无人讨论
0分: 完全冷门话题
```

**2. 种草价值 (Seeding Value: 0-3)**
```
3分: 高种草价值，实用性强，可直接指导行动
2分: 有种草潜力，提供有价值信息
1分: 一般信息，了解即可
0分: 低种草价值，无实质内容
```

**3. 争议性 (Controversy: 0-2)**
```
2分: 明显争议，多方观点对立，可引发讨论
1分: 存在不同看法，可引发讨论
0分: 共识性话题，难以引发讨论
```

**4. 相关性 (Relevance: 0-0)**
```
0分: 不强制相关（小红书内容类型多样，不强制与账号定位相关）
```

### Output Format

```markdown
# 选题筛选报告

## 筛选时间
{timestamp}

## 用户定位
- 领域: {domains}
- 目标性别: {target_gender}
- 人设: {persona_style}
- 平台: 小红书

## 筛选结果

### 入选创作池 (≥7分)

#### 1. {Topic Title} - **{total_score}分**
| 热度 | 种草价值 | 争议性 |
|------|---------|--------|
| {trending}/5 | {seeding}/3 | {controversy}/2 |

- **推荐类型**: [种草笔记/测评分享/生活方式/美妆教程/穿搭灵感]
- **推荐风格**: [风格类型]
- **创作角度**: 建议的切入点
- **种草要点**: 可提炼的种草点
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

下一步：运行 `/xiaohongshu-create {选题}` 开始创作
```

## Content Type Mapping

根据素材特点推荐小红书特定的内容类型：

| 素材特点 | 推荐内容类型 | 说明 |
|---------|-------------|------|
| 产品推荐 + 使用体验 | 种草笔记 | 重点突出产品优势和使用感受 |
| 多产品对比 + 真实体验 | 测评分享 | 真实体验，客观评价 |
| 生活场景 + 个人风格 | 生活方式 | 结合个人生活和品味 |
| 技能技巧 + 步骤 | 美妆教程 | 详细步骤，易于跟随 |
| 视觉呈现 + 搭配 | 穿搭灵感 | 视觉为主，搭配建议 |

## Execution Steps

1. **Load materials** from xiaohongshu-collect or user input
2. **Read user profile** (optional)
3. **Score each material** on 4 criteria (热度、种草价值、争议性)
4. **Calculate totals** and sort by score
5. **Categorize**: ≥7 (入选), 5-6 (待定), <5 (淘汰)
6. **Generate recommendations** for top topics
7. **Map content types** based on material characteristics
8. **Output report** with next steps

## Example

Input from xiaohongshu-collect:
```
素材1: AI学习工具推荐
素材2: 春季护肤步骤
素材3: 极简穿搭指南
```

Scoring:
```
AI学习工具推荐:
- 热度: 5/5 (当前爆款话题，大量讨论)
- 种草价值: 3/3 (实用性强，直接指导行动)
- 争议性: 1/2 (有一定讨论空间)
- 相关性: 0/0 (不强制相关)
- 总分: 9/10 ✓ 入选
- 推荐类型: 种草笔记

春季护肤步骤:
- 热度: 4/5 (季节性热门)
- 种草价值: 3/3 (实用性强)
- 争议性: 0/2 (共识性话题)
- 相关性: 0/0 (不强制相关)
- 总分: 7/10 ✓ 入选
- 推荐类型: 美妆教程

极简穿搭指南:
- 热度: 3/5 (稳定话题)
- 种草价值: 2/3 (有一定价值)
- 争议性: 0/2 (共识性话题)
- 相关性: 0/0 (不强制相关)
- 总分: 5/10 × 待定
```

## Customization

Users can customize weights in user-profile.md:
```yaml
scoring:
  trending: 5      # 热度权重
  seeding: 3        # 种草价值权重
  controversy: 2   # 争议性权重
  relevance: 0      # 相关性权重（小红书为0）
  threshold: 7     # 入选阈值
```

## Configuration

### scoring-weights.md

`references/scoring-weights.md` 配置文件包含小红书的评分标准详情。

## Integration

After filtering, suggest:
```
筛选完成！{n} 个选题入选创作池。

推荐优先创作：{top_topic}（{score}分）

下一步：运行 `/{platform}-create {top_topic}` 开始创作
```

## Tips

- 对于产品类话题，优先热度和种草价值
- 对于教程类话题，重视种草价值和实用性
- 对于生活方式话题，关注热度和争议性
- 对于时尚话题，重视热度和种草价值
- 不强制相关，内容类型可以多样化

## Resources

### references/scoring-weights.md
小红书特定的评分权重配置

### xiaohongshu-create/references/user-profile.md
用户画像（可选）

### ../_shared/filter-base.md
共享的评分系统核心逻辑
