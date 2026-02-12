---
name: linkedin-publish
description: Publish 领英 content using browser automation. Use when user wants to publish content, save to drafts, or mentions "publish to 领英", "post linkedin", "linkedin-publish". Supports Articles and Posts. NEVER auto-publish, always saves to draft.
---

# 领英 Publish

Publish 领英 content using browser automation. NEVER auto-publish, always saves to draft for user review.

## 继承模块

```
继承: ../_shared/publish-base.md
```

本模块继承共享的 Playwright 自动化发布核心逻辑，并定制领英特定的发布流程和配置。

## Content Types

领英支持的内容类型：

| Type | Description | Limits |
|------|-------------|--------|
| **文章** | 长文，支持富文本 | 标题无限制，正文 100-3000 字，支持图片、链接 |
| **动态** | 短内容，纯文本 | 100-1300 字，支持图片、文档、视频 |
| **文档** | PDF/PPT 分享 | 文件上传 |
| **视频** | 短视频 | 最多 10 分钟 |

## URLs

- **写文章**: `https://www.linkedin.com/pulse/write`
- **发布动态**: `https://www.linkedin.com/feed/shares/`
- **草稿箱**: `https://www.linkedin.com/feed/drafts/`

## Workflow

### Prerequisites

- Content from linkedin-create
- Playwright MCP server configured
- User logged in to 领英

### Publication Process

**Step 1: Validate content**

```
1. Check content length (动态 100-1300 字, 文章 100-3000 字)
2. Verify hashtags count (建议 3-5 个)
3. Check media requirements
```

**Step 2: Navigate to publish page**

```
1. Go to linkedin.com/pulse/write (文章) or feed/shares/ (动态)
2. Wait for page load
3. Verify user is logged in
```

**Step 3: Fill content**

#### For 文章 (Article):
```
1. Click "Write article" button
2. Enter headline (title)
3. Enter content body (supports rich text)
4. Add cover image (recommended)
5. Add hashtags (#话题)
6. Preview article
7. Click "Save as draft" (NEVER "Publish")
```

#### For 动态 (Post):
```
1. Click "Start a post"
2. Enter content (100-1300 字)
3. Add media (optional):
   - Images: Upload 1-9 images
   - Documents: Upload PDF/PPT
   - Video: Upload video file
4. Add hashtags (#话题)
5. Add @mentions (optional)
6. Click "Save as draft" (NEVER "Post")
```

**Step 4: Save to draft**

```
1. Click "Save as draft" button (NEVER "Publish" or "Post")
2. Wait for save confirmation
3. Verify draft appears in draft box
```

**Step 5: Manual review and publish**

User must:
1. Go to draft box
2. Review content
3. Make final adjustments
4. Manually click "Publish" or "Post" button

## Manual Fallback

If automation fails, provide manual instructions:

### Option 1: Copy to clipboard

Use the `scripts/copy_to_clipboard.py` script:

```bash
python scripts/copy_to_clipboard.py text "{content}"
```

Then manually paste in 领英.

### Option 2: Manual publish guide

See `references/manual-publish-guide.md` for detailed step-by-step instructions.

## Output Format

```markdown
# 领英发布结果

## 状态
{success/failure}

## 内容类型
{content_type}

## 发布位置
{draft_url}

## 后续步骤
1. 登录领英
2. 进入草稿箱
3. 预览并编辑内容
4. 手动点击"发布"按钮

## 内容预览
标题: {title}
正文长度: {word_count} 字
标签: {tags}
媒体: {media_count} 个
```

## Platform Specifics

### 领英内容特点

- **标题**: 专业简洁，吸引目标受众
- **正文**: 结构清晰，使用标题和列表
- **数据**: 引用权威来源，注明出处
- **互动**: 结尾提出问题，引导讨论
- **标签**: 3-5 个相关话题标签

### 话题标签策略

推荐标签组合：
- 1-2 个热门话题标签
- 2-3 个垂直领域标签
- 避免过度使用（不超过 5 个）

### 媒体要求

**图片**:
- 格式: JPG, PNG
- 比例: 1.91:1 (横图) 或 4:5 (竖图)
- 大小: 不超过 5MB
- 数量: 1-9 张

**文档**:
- 格式: PDF, PPT
- 大小: 不超过 100MB
- 页数: 不超过 300 页

**视频**:
- 格式: MP4, MOV, AVI
- 时长: 不超过 10 分钟
- 大小: 不超过 5GB
- 分辨率: 720p 及以上

## Troubleshooting

### Common Issues

**Issue 1: Login required**
```
Solution:
1. Manually log in to linkedin.com
2. Re-run automation
```

**Issue 2: Content too short/long**
```
Solution:
1. 动态: Check 100-1300 字限制
2. 文章: Check 100-3000 字限制
3. Adjust content length
```

**Issue 3: Media upload failed**
```
Solution:
1. Check file format and size
2. Try manual upload
3. Use copy to clipboard fallback
```

**Issue 4: Hashtag limit**
```
Solution:
1. Limit to 3-5 hashtags
2. Remove less relevant tags
```

## Resources

### references/manual-publish-guide.md
Detailed manual publishing instructions with screenshots

### scripts/copy_to_clipboard.py
Cross-platform clipboard tool for manual publishing

### linkedin-create/references/user-profile.md
User profile for content customization

## Example

Input from linkedin-create:
```markdown
标题: 72% 的企业已开始 AI 转型，你的公司准备好了吗？

正文:
根据 McKinsey 2025 年最新报告...

标签: #AI #DigitalTransformation #BusinessStrategy
```

Process:
```bash
1. Navigate to linkedin.com/pulse/write
2. Enter title: "72% 的企业已开始 AI 转型..."
3. Enter content and hashtags
4. Add cover image
5. Click "Save as draft"
```

Output:
```markdown
# 领英发布结果

## 状态
✓ 成功保存到草稿箱

## 内容类型
文章

## 发布位置
https://www.linkedin.com/feed/drafts/

## 后续步骤
1. 登录领英
2. 进入草稿箱查看
3. 预览并确认内容
4. 手动点击"发布"按钮

## 内容预览
标题: 72% 的企业已开始 AI 转型，你的公司准备好了吗？
正文长度: 1800 字
标签: #AI #DigitalTransformation #BusinessStrategy #Innovation
媒体: 1 张封面图
```

## Directory Structure

```
linkedin-publish/
├── SKILL.md                          # 主技能文件
├── references/
│   └── manual-publish-guide.md       # 手动发布指南
└── scripts/
    └── copy_to_clipboard.py          # 剪贴板工具
```
