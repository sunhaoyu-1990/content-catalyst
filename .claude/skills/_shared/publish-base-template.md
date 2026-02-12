---
name: {platform}-publish
description: Publish {Platform} content to draft using browser automation. Use when user wants to publish content to {Platform}, save to drafts, or mentions "publish to {Platform}", "post {Platform}", "{platform}-publish", "发布{Platform}内容". Supports {content_formats}. NEVER auto-publish, always saves to draft.
---

# {Platform} Publish

Publish {Platform} content to draft using Playwright browser automation.

## 继承模块

```
继承: ../_shared/publish-base.md
```

本模块继承共享的 Playwright 自动化发布核心逻辑，并定制 {Platform} 特定的发布流程。

## Prerequisites

- Playwright MCP for browser automation
- User logged into {Platform}
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

{Platform} 支持的内容类型：

{content_types_list}

## Workflow

### Step 1: 准备内容

```bash
# 保存内容到临时文件
echo "{content}" > /tmp/content.txt

# 复制到剪贴板
python scripts/copy_to_clipboard.py text --file /tmp/content.txt
```

### Step 2: 打开{Platform}创建页面

```
browser_navigate: {compose_url}
```

### Step 3: 粘贴内容

```
browser_snapshot → Find content textbox
browser_click: textbox
browser_press_key: Meta+v (或 Ctrl+v)
```

### Step 4: 添加附加元素

{platform_specific_elements}

### Step 5: 保存草稿

```
browser_click: {save_button_selector}
browser_click: confirm_save_button
```

### Step 6: 验证并报告

```
Report: "Draft saved. Please review at {draft_url}"
```

## {Platform} 特定配置

### 发布配置

| 配置项 | 值 | 说明 |
|-------|-----|------|
| compose_url | {compose_url} | 创建页面 URL |
| content_selector | {content_selector} | 内容框选择器 |
| title_selector | {title_selector} | 标题框选择器 |
| save_button | {save_button_selector} | 保存按钮选择器 |
| draft_url | {draft_url} | 草稿箱 URL |

### 平台限制

| 限制项 | 限制 | 说明 |
|-------|------|------|
| 标题 | {title_limit} | {title_limit_description} |
| 正文 | {content_limit} | {content_limit_description} |
| 标签 | {tag_limit} | {tag_limit_description} |
| 图片 | {image_limit} | {image_limit_description} |

## 错误处理

### 用户未登录

```
If login page detected:
→ "请先登录 {Platform}，然后再次运行 /{platform}-publish"
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
→ 显示平台限制（字数、格式等）
```

## 手动发布指引

`references/manual-publish-guide.md`：

```markdown
# {Platform} 手动发布指引

## 发布步骤

1. **登录平台**
   - 访问: {platform_url}
   - 确保已登录账号

2. **创建内容**
   - 点击: {create_button_location}
   - 选择类型: {short_post/long_post/note/etc}

3. **粘贴内容**
   - 标题: {title_placeholder}
   - 正文: {content_placeholder}
   - 格式: {Markdown/纯文本/富文本}

4. **添加附加元素**
   - 标签: {tag_placeholder}
   - 配图: {image_requirements}
   - 其他: {other_elements}

5. **保存草稿/发布**
   - 选择草稿或发布
   - 确认提交

## 平台限制
- 标题字数: {title_limit}
- 正文字数: {content_limit}
- 标签数量: {tag_limit}
- 图片要求: {image_requirements}

## 注意事项
- {note_1}
- {note_2}
```

## 跨平台剪贴板脚本

`scripts/copy_to_clipboard.py`（已存在于各平台 publish skill 中）：

```python
#!/usr/bin/env python3
"""跨平台剪贴板复制工具"""

import sys
import platform

def copy_to_windows(text):
    """Windows 复制到剪贴板"""
    import win32clipboard
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(text, win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()

def copy_to_macos(text):
    """macOS 复制到剪贴板"""
    import subprocess
    process = subprocess.Popen(
        ['pbcopy', 'w'],
        stdin=subprocess.PIPE,
        text=True
    )
    process.communicate(text)

def copy_to_linux(text):
    """Linux 复制到剪贴板"""
    import subprocess
    process = subprocess.Popen(
        ['xclip', '-selection', 'clipboard'],
        stdin=subprocess.PIPE,
        text=True
    )
    process.communicate(text)

def main():
    if len(sys.argv) < 2:
        print("Usage: python copy_to_clipboard.py <text>")
        sys.exit(1)

    text = ' '.join(sys.argv[1:])
    os_name = platform.system()

    try:
        if os_name == 'Windows':
            copy_to_windows(text)
        elif os_name == 'Darwin':
            copy_to_macos(text)
        else:
            copy_to_linux(text)
        print("✓ Copied to clipboard")
    except Exception as e:
        print(f"✗ Failed: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
```

## 多属性选择器策略

为了提高 Playwright 自动化的可靠性，使用多属性选择器：

```javascript
// 优先级: data-testid > aria-label > text
button = page.locator([
  'button[data-testid="{save_button_id}"]',
  'button[aria-label="{save_button_label}"]',
  'button:has-text("{save_button_text}")'
])
```

## 效率指南

### 避免不必要的等待

```
❌ 每个操作后都 browser_snapshot
✅ 使用操作返回值进行下一步
```

### 并行准备

```
✅ 在浏览器操作前准备好所有内容
✅ 在导航时复制到剪贴板
```

### 顺序执行

```
导航 → 粘贴内容 → 添加元素 → 保存 → 验证
```

## Example Flows

### {content_type_1} Example

User: `/{platform}-publish`（带 {content_type_1} 内容）

```bash
# 1. 复制到剪贴板
python scripts/copy_to_clipboard.py text "{content}"

# 2. 导航到创建页面
browser_navigate: {compose_url}

# 3. 找到内容框并粘贴
browser_snapshot → find textbox
browser_click: textbox
browser_press_key: Meta+v

# 4. 保存草稿
browser_click: "{save_button_text}"

# 5. 报告
"草稿已保存！请审核后发布。"
```

### {content_type_2} Example

User: `/{platform}-publish`（带 {content_type_2} 内容）

{content_type_2_workflow}

## Integration

After publishing:
```
内容已保存到{Platform}草稿箱！

- 类型: {content_type}
- 字数: {word_count}
- 草稿链接: {draft_url}

请手动审核后发布。
```

## Configuration Files

### manual-publish-guide.md 模板

创建 `references/manual-publish-guide.md`：

```markdown
# {Platform} 手动发布指引

## 发布步骤

1. **登录平台**
   - 访问: {platform_url}
   - 确保已登录账号

2. **创建内容**
   - 点击: {create_button_location}
   - 选择类型: {content_type_options}

3. **粘贴内容**
   - 标题: {generated_title}
   - 正文: {generated_content}
   - 格式: {format_type}

4. **添加附加元素**
   - 标签: {generated_tags}
   - 配图: {image_instructions}
   - 其他: {other_instructions}

5. **保存草稿/发布**
   - 选择草稿或发布
   - 确认提交

## 平台限制
- 标题: {title_limit}
- 正文: {content_limit}
- 标签: {tag_limit}
- 图片: {image_limit}

## 注意事项
- {platform_note_1}
- {platform_note_2}
```

### scripts 目录

创建 `scripts/` 目录并复制剪贴板脚本：

```
scripts/
└── copy_to_clipboard.py    # 跨平台剪贴板工具
```

## Tips

- Always verify user is logged in before attempting automation
- Use multiple selector strategies for robustness
- Provide clear manual fallback instructions
- Test automation after platform UI changes
- Report specific errors for debugging

## Resources

### references/manual-publish-guide.md
手动发布指引

### scripts/copy_to_clipboard.py
跨平台剪贴板复制工具

### ../_shared/publish-base.md
共享的 Playwright 自动化发布核心逻辑

---

## 使用说明

**创建平台 skill 步骤**：

1. 复制此模板文件到 `{platform}-publish/SKILL.md`
2. 替换模板变量：
   - `{Platform}` → 平台名称（中文）
   - `{platform}` → 平台标识符（英文小写）
   - `{compose_url}` → 创建页面 URL
   - `{draft_url}` → 草稿箱 URL
   - `{content_selector}` → 内容框选择器
   - `{save_button_selector}` → 保存按钮选择器
3. 根据平台特性调整：
   - 内容类型（{content_type_1}、{content_type_2} 等）
   - 平台限制（字数、标签、图片等）
   - 选择器和元素定位
4. 创建 `references/manual-publish-guide.md`
5. 复制 `scripts/copy_to_clipboard.py`

**知乎示例**：
- compose_url: https://www.zhihu.com/question/write
- content_selector: [data-testid='answer-content']
- save_button: 保存草稿
- 内容类型: 回答、文章、想法

**小红书示例**：
- compose_url: https://creator.xiaohongshu.com/publish/publish
- content_selector: [class='note-textarea']
- save_button: 存为草稿
- 内容类型: 图文笔记、视频笔记

**领英示例**：
- compose_url: https://www.linkedin.com/feed
- content_selector: [data-testid='share-post-trigger']
- save_button: Save draft
- 内容类型: 短帖子(≤1300字符)、长文章
