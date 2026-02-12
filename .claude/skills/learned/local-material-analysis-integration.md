# Local Material Analysis Integration

**Extracted:** 2026-01-27
**Context:** Content creation systems that need to incorporate user's local documents (PDFs, notes, articles) into generated content

## Problem

Content creation tools typically rely on web search or user input, but users often have valuable local materials (product documentation, user feedback, research notes) that should inform content creation. These materials need to be:
1. Detected and imported
2. Analyzed for key insights
3. Integrated into content generation
4. Cached to avoid re-analysis

**Challenges:**
- How to detect new local materials?
- How to analyze different file types (PDF, MD, TXT)?
- How to integrate analysis into content creation?
- How to avoid re-analyzing unchanged files?

## Solution

Implement a 3-stage pipeline: Import → Analyze → Integrate, with caching for efficiency.

### Directory Structure

```
platform-create/
├── assets/
│   ├── materials/          # User uploads local files here
│   │   ├── reports/        # PDF reports
│   │   ├── notes/          # Markdown notes
│   │   └── articles/       # Text articles
│   ├── analyzed/           # Analysis cache (auto-generated)
│   │   ├── ai-report-analysis.md
│   │   └── user-notes-analysis.md
│   └── templates/          # Reference content examples
│       ├── 专业回答/
│       └── 专栏文章/
```

### Stage 1: Material Detection

```python
def check_local_materials(platform):
    """Check for new materials that need analysis"""
    materials_dir = f"{platform}-create/assets/materials/"
    analyzed_dir = f"{platform}-create/assets/analyzed/"

    # Get all material files
    material_files = []
    for category in ['reports', 'notes', 'articles']:
        category_dir = f"{materials_dir}/{category}"
        if os.path.exists(category_dir):
            material_files.extend(glob(f"{category_dir}/*.*"))

    # Check which files have been analyzed
    new_materials = []
    for material_file in material_files:
        filename = os.path.basename(material_file)
        analysis_file = f"{analyzed_dir}/{filename}-analysis.md"

        if not os.path.exists(analysis_file):
            new_materials.append(material_file)

    return new_materials
```

### Stage 2: Material Analysis

```python
def analyze_material(material_file, platform):
    """Analyze local material and extract key insights"""
    # Determine file type
    file_ext = os.path.splitext(material_file)[1].lower()

    # Read content
    if file_ext == '.pdf':
        content = read_pdf(material_file)
    elif file_ext in ['.md', '.markdown']:
        content = read_markdown(material_file)
    elif file_ext == '.txt':
        content = read_text(material_file)
    else:
        return None

    # Platform-specific analysis prompt
    analysis_prompt = get_analysis_prompt(platform)

    # Analyze content
    analysis = analyze_with_llm(content, analysis_prompt)

    # Cache analysis result
    filename = os.path.basename(material_file)
    analysis_file = f"{platform}-create/assets/analyzed/{filename}-analysis.md"
    write_file(analysis_file, analysis)

    return analysis_file
```

### Platform-Specific Analysis Prompts

**知乎:**
```markdown
请分析这份资料，提取以下信息用于知乎内容创作：

1. **核心观点**: 3-5个关键专业观点
2. **专业深度**: 可深入分析的专业知识点
3. **实用价值**: 对读者的实际帮助
4. **争议点**: 可引发讨论的专业争议
5. **推荐内容类型**: [专业回答/专栏文章/观点文章]
```

**小红书:**
```markdown
请分析这份资料，提取以下信息用于小红书内容创作：

1. **核心卖点**: 3-5个吸引人的卖点
2. **使用场景**: 实际应用场景
3. **种草要点**: 可提炼的种草点
4. **避坑指南**: 需要注意的事项
5. **推荐内容类型**: [种草笔记/测评分享/生活方式]
```

**领英:**
```markdown
请分析这份资料，提取以下信息用于领英内容创作：

1. **关键数据**: 支撑观点的数据和统计
2. **商业价值**: 对企业的实际价值
3. **ROI展示**: 可量化的效果或收益
4. **行业趋势**: 反映的行业趋势
5. **推荐内容类型**: [行业洞察/案例研究/专业分享]
```

### Stage 3: Integration into Content Creation

```python
def generate_content(topic, platform, user_profile):
    """Generate content integrating local material analysis"""

    # Check for analyzed materials
    analyzed_dir = f"{platform}-create/assets/analyzed/"
    analysis_files = glob(f"{analyzed_dir}/*.md")

    # Load analysis results
    material_insights = []
    for analysis_file in analysis_files:
        insights = parse_analysis_file(analysis_file)
        material_insights.append(insights)

    # Generate content with material integration
    if material_insights:
        content = generate_with_materials(
            topic=topic,
            platform=platform,
            user_profile=user_profile,
            material_insights=material_insights
        )

        # Add material attribution
        content['sources'] = [insight['source'] for insight in material_insights]

    return content
```

## User Interaction Pattern

### Prompt: Detection

```
检测到本地资料：
- 📄 AI行业报告.pdf (reports/)
- 📝 用户反馈汇总.md (notes/)

是否需要分析这些资料并整合到知乎内容创作中？
[选项: 分析全部 / 分析部分 / 跳过]
```

### Process: Analysis

```
正在分析资料...

✅ AI行业报告.pdf → assets/analyzed/AI行业报告.pdf-analysis.md
   - 提取 5 个关键专业观点
   - 识别 3 个数据支撑点
   - 推荐内容类型: 专栏文章

✅ 用户反馈汇总.md → assets/analyzed/用户反馈汇总.md-analysis.md
   - 提取 8 个用户痛点
   - 识别 4 个实用建议
   - 推荐内容类型: 专业回答

资料分析完成！整合到内容创作中...
```

### Output: Attribution

```markdown
# 知乎内容创作

## 选题
AI工具在企业的应用实践

## 内容类型
专栏文章

---

## 核心观点
1. [来自 AI行业报告.pdf] 72%的企业已开始AI转型...
2. [来自 用户反馈汇总.md] 用户最关注的是...

## 素材来源
- 📄 AI行业报告.pdf
- 📝 用户反馈汇总.md

---
```

## When to Use

**Activate this pattern when:**
- Users have local documents relevant to content creation
- Content quality benefits from specific material analysis
- Platform-specific content types benefit from different analysis angles
- Need to attribute sources in generated content
- Want to avoid re-analyzing unchanged files

**Key triggers:**
- "I have a PDF/article I want to base content on"
- "Can I use my own research materials?"
- "How to integrate local documents into content generation?"

## Benefits

### 1. Content Quality
- Real data and insights from authoritative sources
- Platform-specific analysis angles
- Attribution builds credibility

### 2. User Control
- Users control what materials are used
- Clear source attribution
- Easy to update or remove materials

### 3. Efficiency
- Cache analysis results
- Only analyze new/changed files
- Reusable across multiple content pieces

### 4. Platform Customization
- Different analysis prompts per platform
- Different insights extracted per platform
- Platform-appropriate content recommendations

## Best Practices

### 1. File Organization
- Separate by type (reports, notes, articles)
- Use clear, descriptive filenames
- Include date in filename if versioned

### 2. Analysis Format
```markdown
# {filename}-analysis.md

## 来源
- 文件: {filename}
- 类型: {report/note/article}
- 分析时间: {timestamp}

## 提取信息
- 核心观点: ...
- 数据支撑: ...
- 推荐类型: ...

## 平台建议
### 知乎
- 推荐类型: 专栏文章
- 创作角度: ...

### 小红书
- 推荐类型: 种草笔记
- 创作角度: ...
```

### 3. Cache Invalidation
- Check file modification time
- Re-analyze if source file updated
- Manual "re-analyze" option

### 4. Error Handling
- Skip unsupported file types with warning
- Handle corrupted files gracefully
- Provide clear error messages

## Extension: Multi-File Synthesis

For complex topics, synthesize insights from multiple materials:

```python
def synthesize_materials(analysis_files, topic):
    """Synthesize insights from multiple materials"""

    # Load all analyses
    insights = [parse_analysis_file(f) for f in analysis_files]

    # Find connections between materials
    connections = find_connections(insights)

    # Synthesize into coherent narrative
    synthesis = synthesize_with_llm(insights, connections, topic)

    return synthesis
```

## Related Patterns

- **Platform-Specific Differentiation**: Different analysis prompts per platform
- **Template Priority System**: Materials → Templates → Defaults
- **Content Generation Pipeline**: Multi-stage content creation
