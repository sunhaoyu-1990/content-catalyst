# Collect Base Module

**共享模块**：素材收集的 4 轮搜索策略核心逻辑

## 模块说明

本模块定义了素材收集的通用 4 轮搜索策略。各平台 collect skill 应继承此模块，并定制平台特定的搜索关键词。

## 4-Round Search Strategy

### Round 1: 官方权威信息 (Official Sources)

**目标**：获取权威的一手信息

**搜索模式**：
```
Search: "{topic} 官方文档"
Search: "{topic} GitHub"
Search: "{topic} official announcement"
Search: "{topic} 官网"
```

**输出字段**：
- 官方定义
- 关键特性
- 最新动态
- 官方公告

### Round 2: 详细技术解析 (Technical Analysis)

**目标**：理解技术细节和机制

**搜索模式**：
```
Search: "{topic} 详细介绍"
Search: "{topic} 教程 tutorial"
Search: "{topic} how it works"
Search: "{topic} 原理"
```

**输出字段**：
- 技术原理
- 实现方式
- 使用方法
- 注意事项

### Round 3: 对比评测 (Comparison & Reviews)

**目标**：获取不同视角和比较

**搜索模式**：
```
Search: "{topic} vs {competitor}"
Search: "{topic} 评测 review"
Search: "{topic} pros cons"
Search: "{topic} 优缺点"
```

**输出字段**：
- 对比结果
- 用户评价
- 优缺点分析
- 适用场景

### Round 4: 补充验证 (Supplementary Verification)

**目标**：填补信息缺口，获取最新更新

**搜索模式**：
```
1. 分析前 3 轮结果中的信息缺口
2. Search: "{missing_info}"
3. Search: "{topic} 最新 latest 2024 2025"
4. Search: "{topic} 常见问题 FAQ"
```

**输出字段**：
- 补充信息
- 最新动态
- 常见问题

## 输出格式

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
- **推荐内容类型**: [平台特定内容类型]

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

## 平台定制接口

### 搜索关键词模板

各平台应在 `references/search-keywords.md` 中定义：

```markdown
# {Platform} 搜索关键词模板

## Round 1: 官方权威信息
- {platform}_specific_search_1
- {platform}_specific_search_2

## Round 2: 详细技术解析
- {platform}_specific_search_3
- {platform}_specific_search_4

## Round 3: 对比评测
- {platform}_specific_search_5
- {platform}_specific_search_6

## Round 4: 补充验证
- {platform}_specific_search_7
- {platform}_specific_search_8
```

### 推荐内容类型映射

各平台应根据素材特点推荐该平台特定的内容类型：

| 素材特点 | 知乎 | 领英 | 小红书 |
|---------|------|------|--------|
| 技术性强 | 技术解析 | 行业评论 | (无) |
| 有争议 | 观点评论 | 职场洞察 | 讨论类笔记 |
| 实用干货 | 专业回答 | 职业建议 | 测评分享 |
| ... | ... | ... | ... |

## 执行步骤

1. 接收用户提供的主题
2. 执行 Round 1 搜索（官方信息）
3. 执行 Round 2 搜索（技术分析）
4. 执行 Round 3 搜索（对比评测）
5. 分析前 3 轮的信息缺口
6. 执行 Round 4 搜索（补充验证）
7. 综合结果，生成结构化报告
8. 保存到临时文件供 filter 使用
9. 向用户报告摘要

## 使用方式

**平台 skill 引用方式**：

```markdown
# {platform}-collect/SKILL.md

---
继承: ../_shared/collect-base.md
---

## {Platform} 特定定制

### 搜索策略
- Round 1: {platform} 官方信息
- Round 2: {platform} 技术分析
- Round 3: {platform} 对比评测
- Round 4: {platform} 补充验证

### 配置文件
- search-keywords.md: {platform} 搜索关键词模板
```

## 依赖工具

- WebSearch tool：必需，用于执行搜索
- 互联网连接：必需
