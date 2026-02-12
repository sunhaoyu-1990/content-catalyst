---
name: xiaohongshu-publish
description: Publish 小红书 content to draft using browser automation. Use when user wants to publish content, save to drafts, or mentions "publish to 小红书", "post xiaohongshu", "xiaohongshu-publish". Supports 图文笔记 and 视频笔记. NEVER auto-publish, always saves to draft.
---

# 小红书 Publish

Publish 小红书 content to draft using browser automation. NEVER auto-publish, always saves to draft for user review.

## 继承模块

```
继承: ../_shared/publish-base.md
```

本模块继承共享的 Playwright 自动化发布核心逻辑，并定制小红书特定的发布流程和配置。

## Content Types

小红书支持的内容类型：

| Type | Description | Limits |
|------|-------------|--------|
| **图文笔记** | 图片 + 文字笔记 | 标题 20 字，正文 1000 字，最多 10 个标签 |
| **视频笔记** | 短视频笔记 | 标题 20 字，视频 15 秒 - 5 分钟，最多 10 个标签 |

## URLs

- **创作中心**: `https://creator.xiaohongshu.com/publish/publish`
- **草稿箱**: `https://creator.xiaohongshu.com/publish/draft`

## Workflow

### Prerequisites

- Content from xiaohongshu-create
- Playwright MCP server configured
- User logged in to 小红书创作平台

### Publication Process

**Step 1: Validate content**

```
1. Check content length (标题 ≤ 20 字, 正文 ≤ 1000 字)
2. Verify hashtags count (≤ 10 个)
3. Check image/video requirements
```

**Step 2: Navigate to publish page**

```
1. Go to creator.xiaohongshu.com/publish/publish
2. Wait for page load
3. Verify user is logged in
```

**Step 3: Fill content**

#### For 图文笔记:
```
1. Click "图文" tab
2. Upload images (5-9 recommended)
3. Enter title (≤ 20 字)
4. Enter content (≤ 1000 字)
5. Add hashtags (#话题)
6. Select location (optional)
7. Add @mention (optional)
```

#### For 视频笔记:
```
1. Click "视频" tab
2. Upload video file (15s - 5min)
3. Enter title (≤ 20 字)
4. Enter description (≤ 1000 字)
5. Add hashtags (#话题)
6. Select cover image (auto-generated or custom)
7. Add location (optional)
```

**Step 4: Save to draft**

```
1. Click "存草稿" button (NEVER "发布")
2. Wait for save confirmation
3. Verify draft appears in draft box
```

**Step 5: Manual review and publish**

User must:
1. Go to draft box
2. Review content
3. Make final adjustments
4. Manually click "发布" button

## Manual Fallback

If automation fails, provide manual instructions:

### Option 1: Copy to clipboard

Use the `scripts/copy_to_clipboard.py` script:

```bash
python scripts/copy_to_clipboard.py text "{content}"
```

Then manually paste in 小红书创作者平台.

### Option 2: Manual publish guide

See `references/manual-publish-guide.md` for detailed step-by-step instructions.

## Output Format

```markdown
# 小红书发布结果

## 状态
{success/failure}

## 内容类型
{content_type}

## 发布位置
{draft_url}

## 后续步骤
1. 登录小红书创作者平台
2. 进入草稿箱
3. 预览并编辑内容
4. 手动点击"发布"按钮

## 内容预览
标题: {title}
正文长度: {word_count} 字
标签: {tags}
图片/视频: {media_count} 个
```

## Platform Specifics

### 小红书内容特点

- **标题**: 吸引眼球，SEO 优化，使用 emoji
- **正文**: 图文并茂，分段清晰，话题标签
- **图片**: 5-9 张为佳，高清竖图
- **标签**: 最多 10 个，包含热门话题

### 话题标签策略

推荐标签组合：
- 1-2 个热门话题标签
- 2-3 个垂直领域标签
- 1-2 个长尾标签

### 图片要求

- 格式: JPG, PNG
- 比例: 3:4 (竖图) 或 1:1 (方图)
- 大小: 单张不超过 20MB
- 数量: 1-9 张（5-9 张推荐）

### 视频要求

- 格式: MP4, MOV
- 时长: 15 秒 - 5 分钟
- 大小: 不超过 500MB
- 分辨率: 720p 及以上

## Troubleshooting

### Common Issues

**Issue 1: Login required**
```
Solution:
1. Manually log in to creator.xiaohongshu.com
2. Re-run automation
```

**Issue 2: Content too long**
```
Solution:
1. Check title length (≤ 20 字)
2. Check content length (≤ 1000 字)
3. Truncate or split content
```

**Issue 3: Too many hashtags**
```
Solution:
1. Limit to ≤ 10 hashtags
2. Remove less relevant tags
```

**Issue 4: Image upload failed**
```
Solution:
1. Check image format and size
2. Try manual upload
3. Use copy to clipboard fallback
```

## Resources

### references/manual-publish-guide.md
Detailed manual publishing instructions with screenshots

### scripts/copy_to_clipboard.py
Cross-platform clipboard tool for manual publishing

### xiaohongshu-create/references/user-profile.md
User profile for content customization

## Example

Input from xiaohongshu-create:
```markdown
标题: 📚 学生党必看！这些AI学习工具让我的效率提升了300%！

正文:
姐妹们！今天必须给你们种草我最近发现的宝藏AI学习工具...

标签: #AI工具 #学习效率 #学生党 #种草推荐 #好物分享
```

Process:
```bash
1. Navigate to creator.xiaohongshu.com/publish/publish
2. Click "图文" tab
3. Upload 5-7 images
4. Enter title: "📚 学生党必看！..."
5. Enter content and hashtags
6. Click "存草稿"
```

Output:
```markdown
# 小红书发布结果

## 状态
✓ 成功保存到草稿箱

## 内容类型
图文笔记

## 发布位置
https://creator.xiaohongshu.com/publish/draft

## 后续步骤
1. 登录小红书创作者平台
2. 进入草稿箱查看
3. 预览并确认内容
4. 手动点击"发布"按钮

## 内容预览
标题: 📚 学生党必看！这些AI学习工具让我的效率提升了300%！
正文长度: 850 字
标签: #AI工具 #学习效率 #学生党 #种草推荐 #好物分享
图片: 5 张
```

## Directory Structure

```
xiaohongshu-publish/
├── SKILL.md                          # 主技能文件
├── references/
│   └── manual-publish-guide.md       # 手动发布指南
└── scripts/
    └── copy_to_clipboard.py          # 剪贴板工具
```
