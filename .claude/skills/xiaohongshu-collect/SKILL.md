---
name: xiaohongshu-collect
description: Collect and research materials for 小红书 content creation using multi-round web search strategy. Use when user wants to gather trending topics, research subjects for 小红书 content, or mentions "collect materials", "research topic", "find content for 小红书", "xiaohongshu-collect". Performs 4-round deep research mimicking human research workflow.
---

# 小红书 Collect

Collect trending topics and research materials for 小红书 content creation using a systematic 4-round web search strategy.

## 继承模块

```
继承: ../_shared/collect-base.md
```

本模块继承共享的 4 轮搜索策略核心逻辑，并定制小红书特定的搜索关键词和内容类型映射。

## Prerequisites

- WebSearch tool available
- Internet connection

## Workflow

### Input

User provides:
- **Topic** (required): The subject to research (e.g., "AI工具推荐", "美妆教程", "穿搭灵感", "种草笔记")
- **Language** (optional): Output language, defaults to Chinese (zh-CN)

### 4-Round Search Strategy

Simulate human research thinking process with progressive depth:

**Round 1: 热门话题 (Trending Topics)**
```
Search: "{topic} 小红书热门"
Search: "{topic} 小红书爆款"
Search: "{topic} 种草"
Search: "{topic} 小红书推荐"
```
Goal: Get trending topics and viral content on 小红书

**Round 2: 用户痛点 (User Pain Points)**
```
Search: "{topic} 使用技巧"
Search: "{topic} 避坑指南"
Search: "{topic} 注意事项"
Search: "{topic} 教程"
```
Goal: Understand user problems and practical solutions

**Round 3: 爆款笔记分析 (Viral Notes Analysis)**
```
Search: "{topic} 对比"
Search: "{topic} 测评"
Search: "{topic} 使用心得"
Search: "{topic} 体验"
```
Goal: Get different perspectives and user experiences

**Round 4: 补充验证 (Supplementary Verification)**
```
# Analyze gaps from previous rounds
missing_info = analyze_gaps(previous_results)
Search: "{missing_info}"
Search: "{topic} 小红书 最新 2024 2025"
Search: "{topic} 挑选品牌"
```
Goal: Fill information gaps and get latest updates

### 小红书特定搜索关键词

从 `references/search-keywords.md` 读取小红书定制的搜索关键词模板：

```markdown
# 小红书搜索关键词模板

## Round 1: 热门话题
- "{topic} 小红书热门"
- "{topic} 小红书爆款"
- "{topic} 种草推荐"
- "{topic} 小红书榜单"

## Round 2: 用户痛点
- "{topic} 使用技巧"
- "{topic} 避坑指南"
- "{topic} 新手教程"
- "{topic} 经验分享"

## Round 3: 爆款笔记分析
- "{topic} 对比测评"
- "{topic} 使用心得"
- "{topic} 真实体验"
- "{topic} 优缺点"

## Round 4: 补充验证
- "{topic} 挑选攻略"
- "{topic} 选购指南"
- "{topic} 最新 2024 2025"
- "{topic} 价格对比"
```

### Output Format

Generate structured material document:

```markdown
# {Topic} 素材收集报告

## 收集时间
{timestamp}

## 核心信息
- **热门程度**: 爆款/上升/稳定/小众
- **目标人群**: {target_audience_description}
- **内容趋势**: {trend_analysis}

## 素材列表

### 素材 1
- **标题**: ...
- **来源**: {url}
- **摘要**: 2-3句话概括
- **关键点**:
  - 要点1
  - 要点2
- **潜在选题角度**: ...
- **推荐内容类型**: [种草笔记/测评分享/生活方式/美妆教程/穿搭灵感]

### 素材 2
...

## 热度分析
- **当前热度**: 高/中/低
- **趋势**: 上升/稳定/下降
- **讨论焦点**: ...

## 种草价值
- **种草潜力**: 高/中/低
- **争议性**: 有/无
- **实用价值**: 高/中/低

## 下一步建议
使用 /xiaohongshu-filter 对素材进行打分筛选
```

### 推荐内容类型映射

根据素材特点推荐小红书特定的内容类型：

| 素材特点 | 推荐内容类型 | 说明 |
|---------|-------------|------|
| 产品推荐 + 使用体验 | 种草笔记 | 重点突出产品优势和使用感受 |
| 多产品对比 + 测评 | 测评分享 | 真实体验，客观评价 |
| 生活场景 + 个人风格 | 生活方式 | 结合个人生活和品味 |
| 技能教学 + 步骤演示 | 美妆教程 | 详细步骤，易于跟随 |
| 穿搭展示 + 搭配灵感 | 穿搭灵感 | 视觉呈现，搭配建议 |

## Execution Steps

1. **Receive topic** from user
2. **Load search keywords** from `references/search-keywords.md`
3. **Execute Round 1** searches (热门话题)
4. **Execute Round 2** searches (用户痛点)
5. **Execute Round 3** searches (爆款笔记分析)
6. **Analyze gaps** from rounds 1-3
7. **Execute Round 4** searches (补充验证)
8. **Map content types** based on material characteristics
9. **Synthesize results** into structured format
10. **Save to temp file** for xiaohongshu-filter to use
11. **Report summary** to user

## Example

User: `/xiaohongshu-collect AI学习工具`

Expected behavior:
1. Search "AI学习工具 小红书热门"
2. Search "AI学习工具 小红书爆款"
3. Search "AI学习工具 使用技巧"
4. Search "AI学习工具 对比"
5. Identify gaps: need more about pricing, specific tool features
6. Search "AI学习工具 价格对比"
7. Search "AI学习工具 最新 2025"
8. Generate structured material report

## Integration

After collection, suggest:
```
素材收集完成！共找到 X 条相关素材。

下一步：运行 /xiaohongshu-filter 对素材进行打分筛选，≥7分的选题将进入创作池。
```

## Tips

- 对于产品类话题，优先搜索种草笔记和测评
- 对于教程类话题，优先搜索实用技巧和避坑指南
- 对于生活方式话题，优先搜索爆款笔记和流行趋势
- 始终记录来源 URL 以确保可信度
- 根据素材特点推荐最合适的小红书内容类型
- 关注图片和视觉呈现的重要性（小红书是视觉平台）

## Resources

### references/search-keywords.md
小红书特定的 4 轮搜索关键词模板

### ../_shared/collect-base.md
共享的 4 轮搜索策略核心逻辑
