---
name: zhihu-publish
description: Publish 知乎 content to draft using browser automation. Use when user wants to publish content to 知乎, save to drafts, or mentions "publish to 知乎", "post 知乎", "zhihu-publish", "发布知乎内容". Supports 专业回答 and 专栏文章. NEVER auto-publish, always saves to draft.
---

# 知乎 Publish

Publish 知乎 content to draft using Playwright browser automation.

## 继承模块

```
继承: ../_shared/publish-base.md
```

本模块继承共享的 Playwright 自动化发布核心逻辑，并定制知乎特定的发布流程。

## Prerequisites

- Playwright MCP for browser automation
- User logged into 知乎
- Python 3.9+ with dependencies:
  - macOS: `uv pip install Pillow pyobjc-framework-Cocoa`
  - Windows: `uv pip install Pillow pywin32`
  - Linux: `uv pip install Pillow`

## Critical Rules

1. **NEVER auto-publish** - Only save to draft
2. **User must be logged in** - Prompt to login if not
3. **Verify content before saving** - Double-check content
4. **Provide manual fallback** - Always have manual guide as backup

## Content Types

知乎支持的内容类型：

- **专业回答**：回答问题形式，300-3000字
- **专栏文章**：长文形式，1000-10000字
- **想法**：短动态形式，300字以内

## Workflow

### Step 1: 准备内容

```bash
# 保存内容到临时文件
echo "{content}" > /tmp/content.txt

# 复制到剪贴板
python scripts/copy_to_clipboard.py text --file /tmp/content.txt
```

### Step 2: 打开知乎创建页面

**专业回答**：
```
browser_navigate: https://www.zhihu.com/question/{question_id}
```

**专栏文章**：
```
browser_navigate: https://zhuanlan.zhihu.com/write
```

**想法**：
```
browser_navigate: https://www.zhihu.com/signals
```

### Step 3: 粘贴内容

```
browser_snapshot → Find content textbox
browser_click: textbox
browser_press_key: Meta+v (或 Ctrl+v)
```

### Step 4: 保存草稿

```
browser_click: 保存草稿按钮
```

### Step 5: 验证并报告

```
Report: "Draft saved. Please review at {draft_url}"
```

## 知乎特定配置

### 发布配置

| 配置项 | 值 | 说明 |
|-------|-----|------|
| compose_url (回答) | https://www.zhihu.com/question/{question_id} | 问题页面 URL |
| compose_url (专栏) | https://zhuanlan.zhihu.com/write | 专栏写作页面 |
| compose_url (想法) | https://www.zhihu.com/signals | 想法页面 |
| content_selector | [data-testid='answer-content'] 或 .DraftEditor-content | 内容框选择器 |
| title_selector | input[placeholder='请输入标题'] | 标题框选择器（专栏） |
| save_button | 保存草稿 | 保存按钮文本 |
| draft_url | https://www.zhihu.com/drafts | 草稿箱 URL |

### 平台限制

| 限制项 | 限制 | 说明 |
|-------|------|------|
| 回答字数 | 300-30000 字 | 最少 300 字，最多 30000 字 |
| 专栏标题 | 1-100 字 | 建议简洁有力 |
| 专栏正文 | 1000-100000 字 | 长文形式 |
| 想法字数 | 最多 3000 字 | 短动态形式 |
| 话题标签 | 最多 5 个 | 回答可添加话题 |

## 错误处理

### 用户未登录

```
If login page detected:
→ "请先登录知乎，然后再次运行 /zhihu-publish"
→ 登录地址: https://www.zhihu.com/signin
```

### Playwright 失效

```
If browser automation fails:
→ 提供手动发布指引
→ "自动化发布失败，请按以下步骤手动发布："
→ 显示 manual-publish-guide.md 内容
```

### 内容验证失败

```
If content exceeds limits:
→ 提示用户调整内容
→ 回答最少 300 字
→ 专栏建议 1000 字以上
```

## 手动发布指引

`references/manual-publish-guide.md` 提供详细的手动发布步骤。

## Example Flows

### 专业回答示例

User: `/zhihu-publish`（带回答内容）

```bash
# 1. 复制到剪贴板
python scripts/copy_to_clipboard.py text "要快速上手 Claude 4.5 API..."

# 2. 导航到问题页面（用户提供问题 URL 或 ID）
browser_navigate: https://www.zhihu.com/question/{question_id}

# 3. 找到回答框
browser_snapshot → find answer textbox
browser_click: textbox
browser_press_key: Meta+v

# 4. 检查字数，确保 ≥300 字
# 5. 保存草稿
browser_click: "保存草稿"

# 6. 报告
"回答草稿已保存！请审核后发布。"
```

### 专栏文章示例

User: `/zhihu-publish`（带专栏内容）

```bash
# 1. 准备标题和正文
python scripts/copy_to_clipboard.py text "2025年AI Agent发展趋势"

# 2. 导航到专栏写作页面
browser_navigate: https://zhuanlan.zhihu.com/write

# 3. 输入标题
browser_click: title_input
browser_type: "2025年AI Agent发展趋势"

# 4. 输入正文
browser_click: content_textarea
browser_type: "{full_article_content}"

# 5. 保存草稿
browser_click: "保存草稿"

# 6. 报告
"专栏文章草稿已保存！请审核后发布。"
```

## Integration

After publishing:
```
内容已保存到知乎草稿箱！

- 类型: {content_type}
- 字数: {word_count}
- 草稿链接: https://www.zhihu.com/drafts

请手动审核后发布。
```

## Configuration Files

### manual-publish-guide.md

详细的知乎手动发布指引（见 references/manual-publish-guide.md）

### scripts/copy_to_clipboard.py

跨平台剪贴板复制工具（支持 Windows/macOS/Linux）

## Tips

- 确保用户已登录知乎
- 回答需要至少 300 字才能发布
- 专栏建议添加封面图
- 可以添加话题标签增加曝光
- 草稿保存后可在草稿箱中继续编辑
- 发布前建议再次检查内容

## Resources

### references/manual-publish-guide.md
知乎手动发布指引

### scripts/copy_to_clipboard.py
跨平台剪贴板复制工具

### ../_shared/publish-base.md
共享的 Playwright 自动化发布核心逻辑
