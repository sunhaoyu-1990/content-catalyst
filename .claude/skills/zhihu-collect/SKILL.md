---
name: zhihu-collect
description: Collect and research materials for 知乎 content creation using multi-round web search strategy. Use when user wants to gather trending topics, research subjects for 知乎 content, or mentions "collect materials", "research topic", "find content for 知乎", "zhihu-collect". Performs 4-round deep research mimicking human research workflow.
---

# 知乎 Collect

Collect trending topics and research materials for 知乎 content creation using a systematic 4-round web search strategy.

## 继承模块

```
继承: ../_shared/collect-base.md
```

本模块继承共享的 4 轮搜索策略核心逻辑，并定制知乎特定的搜索关键词和内容类型映射。

## Prerequisites

- WebSearch tool available
- Internet connection

## Workflow

### Input

User provides:
- **Topic** (required): The subject to research (e.g., "AI Agent最新进展", "Claude 4 发布", "前端工程化")
- **Language** (optional): Output language, defaults to Chinese (zh-CN)

### 4-Round Search Strategy

Simulate human research thinking process with progressive depth:

**Round 1: 官方权威信息 (Official Sources)**
```
Search: "{topic} 知乎官方"
Search: "{topic} 官方文档"
Search: "{topic} GitHub"
Search: "{topic} official announcement"
```
Goal: Get authoritative first-hand information

**Round 2: 详细技术解析 (Technical Analysis)**
```
Search: "{topic} 详细介绍"
Search: "{topic} 教程 tutorial"
Search: "{topic} how it works"
Search: "{topic} 原理"
```
Goal: Understand technical details and mechanisms

**Round 3: 对比评测 (Comparison & Reviews)**
```
Search: "{topic} vs {competitor}"
Search: "{topic} 评测 review"
Search: "{topic} pros cons"
Search: "{topic} 优缺点"
```
Goal: Get different perspectives and comparisons

**Round 4: 补充验证 (Supplementary Verification)**
```
# Analyze gaps from previous rounds
missing_info = analyze_gaps(previous_results)
Search: "{missing_info}"
Search: "{topic} 最新 latest 2024 2025"
Search: "{topic} 常见问题 FAQ"
```
Goal: Fill information gaps and get latest updates

### 知乎特定搜索关键词

从 `references/search-keywords.md` 读取知乎定制的搜索关键词模板：

```markdown
# 知乎搜索关键词模板

## Round 1: 官方权威信息
- "{topic} 知乎官方"
- "{topic} 官方文档"
- "{topic} GitHub"
- "{topic} 官方公告"

## Round 2: 详细技术解析
- "{topic} 详细介绍"
- "{topic} 教程 tutorial"
- "{topic} 原理解析"
- "{topic} 技术深度"

## Round 3: 对比评测
- "{topic} 对比"
- "{topic} 评测"
- "{topic} 优缺点分析"
- "{topic} 选择建议"

## Round 4: 补充验证
- "{topic} 常见问题"
- "{topic} 最新 2024 2025"
- "{topic} 实战经验"
- "{topic} 最佳实践"
```

### Output Format

Generate structured material document:

```markdown
# {Topic} 素材收集报告

## 收集时间
{timestamp}

## 核心信息
- **官方定义**: ...
- **关键特性**: ...
- **最新动态**: ...

## 素材列表

### 素材 1
- **标题**: ...
- **来源**: {url}
- **摘要**: 2-3句话概括
- **关键点**:
  - 要点1
  - 要点2
- **潜在选题角度**: ...
- **推荐内容类型**: [专业回答/专栏文章/经验分享/学术讨论/观点评论]

### 素材 2
...

## 热度分析
- **当前热度**: 高/中/低
- **趋势**: 上升/稳定/下降
- **讨论焦点**: ...

## 争议点
- 争议1: ...
- 争议2: ...

## 下一步建议
使用 /zhihu-filter 对素材进行打分筛选
```

### 推荐内容类型映射

根据素材特点推荐知乎特定的内容类型：

| 素材特点 | 推荐内容类型 | 说明 |
|---------|-------------|------|
| 技术性强 | 专业回答 | 深度技术解析，适合回答专业问题 |
| 有争议 | 观点评论 | 有态度有立场的评论文章 |
| 实用干货 | 经验分享 | 个人经验和实操指南 |
| 理论深 | 学术讨论 | 理论分析和学术探讨 |
| 时事热点 | 专栏文章 | 对热点的深度分析 |

## Execution Steps

1. **Receive topic** from user
2. **Load search keywords** from `references/search-keywords.md`
3. **Execute Round 1** searches (官方权威信息)
4. **Execute Round 2** searches (技术解析)
5. **Execute Round 3** searches (对比评测)
6. **Analyze gaps** from rounds 1-3
7. **Execute Round 4** searches (补充验证)
8. **Map content types** based on material characteristics
9. **Synthesize results** into structured format
10. **Save to temp file** for zhihu-filter to use
11. **Report summary** to user

## Example

User: `/zhihu-collect Claude MCP协议`

Expected behavior:
1. Search "Claude MCP协议 知乎官方"
2. Search "Claude MCP协议 官方文档"
3. Search "MCP Model Context Protocol GitHub"
4. Search "Claude MCP协议 详细介绍"
5. Search "MCP协议 教程"
6. Search "MCP协议 原理"
7. Search "MCP vs function calling"
8. Search "MCP协议 评测"
9. Identify gaps: need more about security, adoption rate
10. Search "MCP协议 安全性"
11. Search "MCP协议 最新 2025"
12. Generate structured material report

## Integration

After collection, suggest:
```
素材收集完成！共找到 X 条相关素材。

下一步：运行 /zhihu-filter 对素材进行打分筛选，≥7分的选题将进入创作池。
```

## Tips

- 对于技术话题，优先搜索官方文档和 GitHub
- 对于热点话题，优先搜索知乎热榜和最新动态
- 对于有争议的话题，收集多方观点
- 始终记录来源 URL 以确保可信度
- 根据素材特点推荐最合适的知乎内容类型

## Resources

### references/search-keywords.md
知乎特定的 4 轮搜索关键词模板

### ../_shared/collect-base.md
共享的 4 轮搜索策略核心逻辑
