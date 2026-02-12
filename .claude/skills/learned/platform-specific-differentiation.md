# Platform-Specific Differentiation Pattern

**Extracted:** 2026-01-27
**Context:** Implementing same functionality for different platforms with platform-specific customizations

## Problem

When building multi-platform tools, the core functionality is identical (e.g., content filtering, scoring), but each platform requires different:
- Scoring weights (what matters most)
- Content types (supported formats)
- Search keywords (platform terminology)
- Output formats (platform conventions)

**Challenge:** Maintain shared logic while allowing deep platform customization.

## Solution

Use parameterization with platform-specific configuration files that override shared defaults.

### Pattern: Configurable Scoring System

#### Shared Base (filter-base.md)

```markdown
# Filter Base (Shared Module)

## Scoring System

Platform-specific scoring dimensions and weights are defined in `references/scoring-weights.md`

### Standard Dimensions
1. **Trending/热度** (0-5 points): Current popularity
2. **Value/价值** (0-3 points): Practical value
3. **Controversy/争议性** (0-2 points): Discussion potential
4. **Relevance/相关性** (0-0 points): Alignment with user profile

### Scoring Process
For each material, score on all dimensions → Sum → Compare to threshold
```

#### Platform Configuration (知乎: scoring-weights.md)

```markdown
# 知乎评分权重配置

## 评分维度和权重
| 维度 | 权重 | 说明 |
|-----|------|------|
| 热度 | 3 分 | 知乎关注专业深度，不过分追求热点 |
| 专业价值 | 5 分 | 知乎重视专业性和深度分析 |
| 争议性 | 1 分 | 知乎倾向理性讨论，不追求争议 |
| 相关性 | 1 分 | 知乎内容需要与专业领域相关 |

**阈值**: ≥8 分进入创作池

## 评分标准

### 热度 (0-3)
- 3分: 专业领域热门话题
- 2分: 稳定讨论话题
- 1分: 小众专业话题
- 0分: 过时或无人讨论

### 专业价值 (0-5)
- 5分: 深度专业分析，可直接应用
- 4分: 有价值的专业见解
- 3分: 一般专业信息
- 2分: 基础科普
- 1分: 浅显内容
- 0分: 无专业价值
```

#### Platform Configuration (小红书: scoring-weights.md)

```markdown
# 小红书评分权重配置

## 评分维度和权重
| 维度 | 权重 | 说明 |
|-----|------|------|
| 热度 | 5 分 | 小红书追求爆款和传播 |
| 种草价值 | 3 分 | 小红书重视实用性和种草能力 |
| 争议性 | 2 分 | 小红书鼓励讨论和互动 |
| 相关性 | 0 分 | 小红书内容类型多样，不强制相关 |

**阈值**: ≥7 分进入创作池

## 评分标准

### 热度 (0-5)
- 5分: 当前爆款话题，大量讨论和分享
- 4分: 近期热门，关注度快速上升
- 3分: 稳定话题，持续有人讨论
- 2分: 小众话题，关注度有限
- 1分: 过时话题，几乎无人讨论
- 0分: 完全冷门话题

### 种草价值 (0-3)
- 3分: 高种草价值，实用性强，可直接指导行动
- 2分: 有种草潜力，提供有价值信息
- 1分: 一般信息，了解即可
- 0分: 低种草价值，无实质内容
```

## Implementation

### Step 1: Define Shared Interface

```python
# Shared base logic
def score_material(material, platform_config):
    """Score material using platform-specific weights"""
    score = 0

    # Apply platform-specific weights
    for dimension, weight in platform_config['weights'].items():
        dimension_score = evaluate_dimension(material, dimension)
        score += dimension_score * weight

    return score
```

### Step 2: Load Platform Configuration

```python
# Platform-specific implementation
def load_config(platform):
    config_path = f"{platform}-filter/references/scoring-weights.md"
    return parse_config_file(config_path)

# Example usage
zhihu_config = load_config('zhihu')
# weights = {'热度': 3, '专业价值': 5, '争议性': 1, '相关性': 1}
# threshold = 8

xiaohongshu_config = load_config('xiaohongshu')
# weights = {'热度': 5, '种草价值': 3, '争议性': 2, '相关性': 0}
# threshold = 7
```

### Step 3: Apply Platform Logic

```python
def filter_materials(materials, platform):
    config = load_config(platform)

    scored_materials = []
    for material in materials:
        score = score_material(material, config)
        if score >= config['threshold']:
            scored_materials.append({
                'material': material,
                'score': score,
                'platform': platform
            })

    return sorted(scored_materials, key=lambda x: x['score'], reverse=True)
```

## Content Type Mapping Pattern

### Problem: Same topic → Different content types per platform

| Material | 知乎 | 小红书 | 领英 |
|---------|------|--------|------|
| AI tool review | 专业回答 | 种草笔记 | 案例研究 |
| Tutorial | 专栏文章 | 教程 | 专业分享 |
| Opinion | 观点文章 | 生活方式 | 观点文章 |

### Solution: Platform-specific content type tables

**知乎 (references/content-types.md):**
```markdown
| 素材特点 | 推荐内容类型 |
|---------|-------------|
| 专业问题 + 深度分析 | 专业回答 |
| 技术讨论 + 代码示例 | 专栏文章 |
| 观点表达 + 讨论引导 | 观点文章 |
```

**小红书 (references/content-types.md):**
```markdown
| 素材特点 | 推荐内容类型 |
|---------|-------------|
| 产品推荐 + 使用体验 | 种草笔记 |
| 多产品对比 + 测评 | 测评分享 |
| 生活场景 + 个人风格 | 生活方式 |
```

## Search Keyword Customization Pattern

### Problem: Same topic → Different search keywords per platform

**知乎:** "{topic} 知乎", "{topic} 专业", "{topic} 问答"
**小红书:** "{topic} 小红书", "{topic} 种草", "{topic} 爆款"
**领英:** "{topic} LinkedIn", "{topic} business", "{topic} trends"

### Solution: Platform-specific keyword templates

```markdown
# references/search-keywords.md

## Round 1: 热门话题
- "{topic} 知乎热门"
- "{topic} 知乎热榜"
- "{topic} 专业讨论"

## Round 2: 专业深度
- "{topic} 教程"
- "{topic} 最佳实践"
- "{topic} 深度分析"
```

## When to Use

**Activate this pattern when:**
- Same functionality applies to multiple platforms
- Platforms have different priorities/weights
- Platforms support different content types/formats
- Platform terminology differs significantly
- Need consistent behavior with platform-specific tuning

**Key triggers:**
- "How do I make this work for [platform A] and [platform B]?"
- Notice different scoring/keywords/types needed per platform
- Platform differences are data-driven, not logic-driven

## Benefits

### 1. Consistency
- Same workflow across platforms
- Same evaluation criteria (just weighted differently)
- Same user experience patterns

### 2. Customization
- Deep platform-specific tuning
- Easy to adjust per platform
- Platform expertise captured in config

### 3. Maintainability
- Logic changes in shared base
- Platform changes in config files
- Clear separation of concerns

### 4. Extensibility
- Add new platform: Create config files
- Add new dimension: Update shared base + all configs
- Adjust weights: Edit config file only

## Best Practices

### 1. Config File Design
```markdown
# scoring-weights.md structure

## 评分维度和权重
| 维度 | 权重 | 说明 |

## 评分标准
### Dimension 1 (0-X)
- X分: Description
- ...

## 阈值
**阈值**: ≥X 分
```

### 2. Dimension Naming
- Use platform-specific names (专业价值 vs. 种草价值)
- Include Chinese and English variants
- Document why each dimension matters

### 3. Weight Allocation
- Weights should sum to meaningful total (e.g., 10)
- Document rationale for each weight
- Provide examples for each score level

### 4. Threshold Setting
- Base on platform content volume
- Consider platform quality standards
- Test with real data to validate

## Extension: User Customization

Allow users to customize weights in their profile:

```yaml
# user-profile.md
scoring:
  trending: 5      # Default: 5
  seeding: 3        # Default: 3
  controversy: 2   # Default: 2
  relevance: 0      # Default: 0
  threshold: 7     # Default: 7
```

## Related Patterns

- **Multi-Platform Skill Architecture**: Shared base with inheritance
- **Configuration File Management**: Platform-specific reference files
- **Local Material Analysis Integration**: Platform-specific analysis prompts
