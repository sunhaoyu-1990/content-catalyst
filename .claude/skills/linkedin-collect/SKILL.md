---
name: linkedin-collect
description: Collect and research materials for 领英 content creation using multi-round web search strategy. Use when user wants to gather trending topics, research subjects for 领英 posts, or mentions "collect materials", "research topic", "find content for 领英", "linkedin-collect". Performs 4-round deep research mimicking human research workflow.
---

# 领英 Collect

Collect and research materials for 领英 content creation using 4-round search strategy.

## 继承模块

```
继承: ../_shared/collect-base.md
```

本模块继承共享的 4 轮搜索核心逻辑，并定制领英特定的搜索关键词和内容类型映射。

## 领英平台特点

领英是专业职场社交平台，内容聚焦：
- **B2B 营销**: 商业洞察、行业趋势
- **职场发展**: 职业技能、管理经验
- **专业知识**: 行业分析、技术分享
- **人脉建设**: 专业见解、观点评论

## 4-Round Search Strategy

### Round 1: 行业洞察与趋势

**搜索目标**: 获取权威的行业报告和趋势分析

**搜索关键词**:
- `{topic} industry report 2025 2026`
- `{topic} market trends analysis`
- `{topic} business insights`
- `{topic} 专业报告`
- `{topic} 行业趋势 领英`

**预期结果**:
- 权威咨询公司报告（McKinsey, Deloitte, Gartner）
- 行业媒体深度分析
- 专业机构发布的数据

### Round 2: 专业解读与技术分析

**搜索目标**: 获取专家解读和技术细节

**搜索关键词**:
- `{topic} expert analysis`
- `{topic} professional perspective`
- `{topic} 技术解析 专业解读`
- `{topic} best practices`
- `{topic} implementation guide`

**预期结果**:
- 行业专家观点文章
- 技术深度解析
- 最佳实践案例
- 实施指南

### Round 3: 商业应用与案例对比

**搜索目标**: 获取真实商业应用场景和案例

**搜索关键词**:
- `{topic} business case study`
- `{topic} company examples`
- `{topic} ROI analysis`
- `{topic} 商业案例 企业实践`
- `{topic} success stories`

**预期结果**:
- 知名企业案例
- ROI 分析报告
- 实施效果对比
- 成功/失败案例

### Round 4: 补充验证与最新动态

**搜索目标**: 验证信息准确性并补充最新动态

**搜索关键词**:
- `{topic} latest news 2026`
- `{topic} update January`
- `{topic} verification`
- `{topic} fact check`
- `{topic} 最新消息`

**预期结果**:
- 最新行业新闻
- 产品更新动态
- 数据验证来源
- 补充背景信息

## Content Type Mapping

根据搜索结果推荐领英特定的内容类型：

| 搜索结果特征 | 推荐内容类型 | 说明 |
|-------------|-------------|------|
| 行业报告 + 数据分析 | 行业洞察 | 权威数据 + 趋势分析 |
| 技术解析 + 实施指南 | 专业分享 | 技术深度 + 实用建议 |
| 企业案例 + ROI 分析 | 案例研究 | 真实案例 + 效果展示 |
| 职场经验 + 技能提升 | 职场发展 | 个人经验 + 成长建议 |
| 观点评论 + 行业讨论 | 观点文章 | 个人见解 + 互动讨论 |

## Content Types

领英支持的内容类型（5种）：

| Type | Style | Use When |
|------|-------|----------|
| **行业洞察** | 数据驱动，权威分析 | 行业趋势、市场分析 |
| **专业分享** | 技术深度，实用建议 | 技术解析、最佳实践 |
| **案例研究** | 真实案例，ROI 展示 | 企业实践、成功案例 |
| **职场发展** | 个人经验，成长建议 | 职场技能、管理心得 |
| **观点文章** | 个人见解，讨论互动 | 热点评论、观点表达 |

## Output Format

```markdown
# 领英素材收集报告

## 收集时间
{timestamp}

## 研究主题
{topic}

## 搜索轮次汇总

### Round 1: 行业洞察与趋势
{round1_summary}

### Round 2: 专业解读与技术分析
{round2_summary}

### Round 3: 商业应用与案例对比
{round3_summary}

### Round 4: 补充验证与最新动态
{round4_summary}

## 推荐内容类型
{content_type}

## 核心素材
### 关键数据
- {data_point_1}
- {data_point_2}

### 权威来源
- {source_1}: {url}
- {source_2}: {url}

### 案例参考
- {case_1}: {description}
- {case_2}: {description}

## 创作角度
{suggested_angles}

## 话题标签
#话题1 #话题2 #话题3

下一步：运行 /linkedin-filter 进行选题筛选
```

## Execution Steps

1. **确认主题**: 从用户输入或 xiaohongshu-filter 获取
2. **执行 4 轮搜索**: 每轮使用特定关键词组合
3. **整理素材**: 提取关键数据、来源、案例
4. **推荐内容类型**: 基于素材特点匹配
5. **生成报告**: 输出结构化收集报告

## Example

Input: `AI in business 2026`

Round 1 Search:
- `AI in business industry report 2026`
- `AI business trends analysis`

Round 2 Search:
- `AI implementation expert analysis`
- `AI business best practices`

Round 3 Search:
- `AI business case study ROI`
- `AI company examples success stories`

Round 4 Search:
- `AI business latest news 2026`
- `AI implementation update`

Output:
```markdown
# 领英素材收集报告

## 收集时间
2026-01-27

## 研究主题
AI in business 2026

## 推荐内容类型
行业洞察

## 核心素材
### 关键数据
- 72% 企业已采用 AI 技术（McKinsey 2025）
- AI 市场规模预计 2026 年达到 $900B
- 平均 ROI: 3.5x 投资回报

### 权威来源
- McKinsey AI Report 2025
- Deloitte Business AI Analysis
- Gartner AI Magic Quadrant

### 案例参考
- 某知名企业: AI 客服降低 40% 成本
- 某金融公司: AI 风控提升 60% 效率

## 创作角度
1. 数据驱动: 用权威报告数据支撑观点
2. 案例说话: 真实企业 ROI 分析
3. 趋势洞察: 2026 年 AI 商业应用趋势

## 话题标签
#AI #BusinessTransformation #DigitalStrategy #Innovation #Leadership
```

## Customization

Users can customize search keywords in `references/search-keywords.md`:

```markdown
## Round 1 Keywords
- Custom keyword 1
- Custom keyword 2

## Round 2 Keywords
...
```

## Resources

### references/search-keywords.md
领英特定的搜索关键词配置

### ../_shared/collect-base.md
共享的 4 轮搜索核心逻辑

## Tips

- 领英内容重视权威性和专业性
- 优先引用知名机构和专家观点
- 数据和案例要有明确来源
- 关注商业价值和 ROI
- 话题标签使用行业关键词

## Directory Structure

```
linkedin-collect/
├── SKILL.md                          # 主技能文件
└── references/
    └── search-keywords.md            # 搜索关键词配置
```
