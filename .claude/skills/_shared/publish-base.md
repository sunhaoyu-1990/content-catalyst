# Publish Base Module

**共享模块**：Playwright 自动化发布核心逻辑

## 模块说明

本模块定义了使用 Playwright 自动化发布到各平台草稿箱的通用流程。

**关键原则**：
- **NEVER auto-publish** - 仅保存到草稿箱
- **User must be logged in** - 提示用户先登录
- **Manual fallback** - 提供手动发布指引作为备选方案

## Prerequisites

- Playwright MCP for browser automation
- User logged into the target platform
- Python 3.9+ with dependencies:
  - macOS: `uv pip install Pillow pyobjc-framework-Cocoa`
  - Windows: `uv pip install Pillow pywin32`
  - Linux: `uv pip install Pillow`

## Critical Rules

1. **NEVER auto-publish** - Only save to draft
2. **User must be logged in** - Prompt to login if not
3. **Verify content before saving** - Double-check content
4. **Provide manual fallback** - Always have manual guide as backup

## 通用发布流程

### Step 1: 准备内容

```bash
# 保存内容到临时文件
echo "{content}" > /tmp/content.txt

# 复制到剪贴板
python scripts/copy_to_clipboard.py text --file /tmp/content.txt
```

### Step 2: 打开平台创建页面

```
browser_navigate: {platform_compose_url}
```

### Step 3: 粘贴内容

```
browser_snapshot → Find content textbox
browser_click: textbox
browser_press_key: Meta+v (或 Ctrl+v)
```

### Step 4: 保存草稿

```
browser_click: close/save button
browser_click: "Save" or "保存" in dialog
```

### Step 5: 验证并报告

```
Report: "Draft saved. Please review at {draft_url}"
```

## 错误处理

### 用户未登录

```
If login page detected:
→ "请先登录 {平台名称}，然后再次运行 /{platform}-publish"
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

## 手动发布指引格式

每个平台应提供 `references/manual-publish-guide.md`：

```markdown
# {平台名称} 手动发布指引

## 发布步骤

1. **登录平台**
   - 访问: {平台 URL}
   - 确保已登录账号

2. **创建内容**
   - 点击: {创建按钮位置和选择器}
   - 选择类型: {短文/长文/笔记等}

3. **粘贴内容**
   - 标题: {生成的标题}
   - 正文: {生成的正文}
   - 格式: {Markdown/纯文本/富文本}

4. **添加附加元素**
   - 标签: {生成的话题标签}
   - 配图: {如有，说明图片要求}
   - 其他: {平台特定元素}

5. **保存草稿/发布**
   - 选择草稿或发布
   - 确认提交

## 平台限制
- 标题字数: {限制}
- 正文字数: {限制}
- 标签数量: {限制}
- 图片要求: {要求}

## 注意事项
- {平台特定注意事项}
```

## 跨平台剪贴板脚本

`scripts/copy_to_clipboard.py`（支持 Windows/macOS/Linux）：

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

## 平台定制接口

### 平台特定配置

各平台应定义：

| 配置项 | 说明 | 示例 |
|-------|------|------|
| compose_url | 创建页面 URL | https://www.zhihu.com/question/write |
| content_selector | 内容框选择器 | [data-testid='post-content'] |
| save_button | 保存按钮选择器 | button:has-text('保存') |
| draft_url | 草稿箱 URL | https://www.zhihu.com/drafts |

### 内容类型

各平台支持的内容类型：

| 平台 | 内容类型 |
|------|---------|
| 知乎 | 回答、文章、想法 |
| 领英 | 短帖子(≤1300字符)、长文章 |
| 小红书 | 图文笔记、视频笔记 |

### 平台限制

| 平台 | 标题限制 | 正文限制 | 标签限制 |
|------|---------|---------|---------|
| 知乎 | - | - | 最多5个话题 |
| 领英 | - | 短帖1300字符 | - |
| 小红书 | 建议20字内 | 1000字内 | 最多10个标签 |

## 多属性选择器策略

为了提高 Playwright 自动化的可靠性，使用多属性选择器：

```javascript
// 优先级: data-testid > aria-label > text
button = page.locator([
  'button[data-testid="save-button"]',
  'button[aria-label="保存"]',
  'button:has-text("保存")'
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

## 使用方式

**平台 skill 引用方式**：

```markdown
# {platform}-publish/SKILL.md

---
继承: ../_shared/publish-base.md
---

## {Platform} 特定定制

### 发布流程
- 创建页面 URL: {url}
- 内容框选择器: {selector}
- 保存按钮: {selector}
- 草稿箱 URL: {url}

### 内容类型
- 类型 1: ...
- 类型 2: ...

### 平台限制
- 标题: {limit}
- 正文: {limit}
- 标签: {limit}

### 配置文件
- manual-publish-guide.md: 手动发布指引
```

## 示例流程

### 知乎回答示例

User: `/zhihu-publish`（带回答内容）

```bash
# 1. 复制到剪贴板
python scripts/copy_to_clipboard.py text "回答内容..."

# 2. 导航到问题页面
browser_navigate: https://www.zhihu.com/question/{question_id}

# 3. 找到回答框并粘贴
browser_snapshot → find answer textbox
browser_click: textbox
browser_press_key: Meta+v

# 4. 保存草稿
browser_click: "保存草稿" button

# 5. 报告
"回答草稿已保存！请审核后发布。"
```

## 依赖工具

- Playwright MCP：浏览器自动化（必需）
- Python 3.9+：辅助脚本（必需）
- Pillow/pywin32/pyobjc：剪贴板操作（必需）
