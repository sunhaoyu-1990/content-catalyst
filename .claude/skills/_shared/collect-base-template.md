---
name: {platform}-collect
description: Collect and research materials for {Platform} content creation using multi-round web search strategy. Use when user wants to gather trending topics, research subjects for {Platform} content, or mentions "collect materials", "research topic", "find content for {Platform}", "{platform}-collect". Performs 4-round deep research mimicking human research workflow.
---

# {Platform} Collect

Collect trending topics and research materials for {Platform} content creation using a systematic 4-round web search strategy.

## 继承模块

```
继承: ../_shared/collect-base.md
```

本模块继承共享的 4 轮搜索策略核心逻辑，并定制 {Platform} 特定的搜索关键词和内容类型映射。

## Prerequisites

- WebSearch tool available
- Internet connection

## Workflow

### Input

User provides:
- **Topic** (required): The subject to research (e.g., "{example_topic_1}", "{example_topic_2}")
- **Language** (optional): Output language, defaults to Chinese (zh-CN)

### 4-Round Search Strategy

Simulate human research thinking process with progressive depth:

**Round 1: 官方权威信息 (Official Sources)**
```
Search: "{topic} {Platform} 官方"
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

### {Platform} 特定搜索关键词

从 `references/search-keywords.md` 读取 {Platform} 定制的搜索关键词模板：

```markdown
# {Platform} 搜索关键词模板

## Round 1: 官方权威信息
- {platform_specific_search_1}
- {platform_specific_search_2}

## Round 2: 详细技术解析
- {platform_specific_search_3}
- {platform_specific_search_4}

## Round 3: 对比评测
- {platform_specific_search_5}
- {platform_specific_search_6}

## Round 4: 补充验证
- {platform_specific_search_7}
- {platform_specific_search_8}
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
- **推荐内容类型**: [{Platform} 特定内容类型]

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
使用 /{platform}-filter 对素材进行打分筛选
```

### 推荐内容类型映射

根据素材特点推荐 {Platform} 特定内容类型：

| 素材特点 | 推荐内容类型 | 说明 |
|---------|-------------|------|
| 技术性强 | {type_1} | {type_1_description} |
| 有争议 | {type_2} | {type_2_description} |
| 实用干货 | {type_3} | {type_3_description} |
| ... | ... | ... |

## Execution Steps

1. **Receive topic** from user
2. **Load search keywords** from `references/search-keywords.md`
3. **Execute Round 1** searches (official sources)
4. **Execute Round 2** searches (technical analysis)
5. **Execute Round 3** searches (comparisons)
6. **Analyze gaps** from rounds 1-3
7. **Execute Round 4** searches (fill gaps)
8. **Map content types** based on material characteristics
9. **Synthesize results** into structured format
10. **Save to temp file** for {platform}-filter to use
11. **Report summary** to user

## Example

User: `/{platform}-collect {example_topic}`

Expected behavior:
1. Search "{example_topic} {Platform} 官方"
2. Search "{example_topic} 官方文档"
3. Search "{example_topic} 详细介绍"
4. Search "{example_topic} 教程"
5. Search "{example_topic} vs {competitor}"
6. Search "{example_topic} 评测"
7. Identify gaps: need more about {gap_example}
8. Search "{example_topic} {gap_example}"
9. Search "{example_topic} 最新 2025"
10. Generate structured material report

## Integration

After collection, suggest:
```
素材收集完成！共找到 X 条相关素材。

下一步：运行 /{platform}-filter 对素材进行打分筛选，≥{threshold}分的选题将进入创作池。
```

## Tips

- For trending topics, prioritize recency (2024-2025)
- For technical topics, prioritize official docs and GitHub
- For controversial topics, collect multiple perspectives
- Always note the source URL for credibility
- Tailor search keywords to {Platform}'s content ecosystem

## Resources

### references/search-keywords.md
{Platform} 特定的 4 轮搜索关键词模板

### ../_shared/collect-base.md
共享的 4 轮搜索策略核心逻辑

## Configuration

创建 `references/search-keywords.md`：

```markdown
# {Platform} 搜索关键词模板

## Round 1: 官方权威信息
- "{topic} {Platform} 官方"
- "{topic} 官方文档"
- "{topic} GitHub"
- "{topic} official announcement"

## Round 2: 详细技术解析
- "{topic} 详细介绍"
- "{topic} 教程 tutorial"
- "{topic} how it works"
- "{topic} 原理"

## Round 3: 对比评测
- "{topic} vs {competitor}"
- "{topic} 评测 review"
- "{topic} pros cons"
- "{topic} 优缺点"

## Round 4: 补充验证
- "{topic} 常见问题 FAQ"
- "{topic} 最新 latest 2024 2025"
- "{topic} 实战案例"
- "{topic} 最佳实践"
```

---

## 使用说明

**创建平台 skill 步骤**：

1. 复制此模板文件到 `{platform}-collect/SKILL.md`
2. 替换模板变量：
   - `{Platform}` → 平台名称（中文）
   - `{platform}` → 平台标识符（英文小写）
   - `{example_topic_1}` → 示例主题 1
   - `{example_topic_2}` → 示例主题 2
   - `{type_1}`, `{type_2}` 等 → 平台特定内容类型
3. 创建 `references/search-keywords.md` 并定制搜索关键词
4. 根据平台特性调整搜索策略和内容类型映射
