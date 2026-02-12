#!/usr/bin/env python3
"""
小红书发布 - 剪贴板工具
跨平台剪贴板复制工具，用于手动发布内容
"""

import sys
import platform
from typing import Optional


def copy_to_clipboard_windows(text: str) -> bool:
    """Windows 剪贴板复制"""
    try:
        import win32clipboard
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(text, win32clipboard.CF_UNICODETEXT)
        win32clipboard.CloseClipboard()
        return True
    except ImportError:
        # 回退到 ctypes
        import ctypes
        CF_UNICODETEXT = 13
        ctypes.windll.user32.OpenClipboard(0)
        ctypes.windll.user32.EmptyClipboard()
        buf = ctypes.create_unicode_buffer(text)
        ctypes.windll.kernel32.GlobalAlloc(0x42, len(text.encode('utf-16-le')) + 2)
        ctypes.windll.user32.SetClipboardData(CF_UNICODETEXT, buf)
        ctypes.windll.user32.CloseClipboard()
        return True
    except Exception as e:
        print(f"Windows 剪贴板复制失败: {e}", file=sys.stderr)
        return False


def copy_to_clipboard_macos(text: str) -> bool:
    """macOS 剪贴板复制"""
    try:
        import subprocess
        process = subprocess.Popen(
            ['pbcopy'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        process.communicate(text.encode('utf-8'))
        return process.returncode == 0
    except Exception as e:
        print(f"macOS 剪贴板复制失败: {e}", file=sys.stderr)
        return False


def copy_to_clipboard_linux(text: str) -> bool:
    """Linux 剪贴板复制"""
    # 尝试 xsel
    try:
        import subprocess
        process = subprocess.Popen(
            ['xsel', '--clipboard', '--input'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        process.communicate(text.encode('utf-8'))
        if process.returncode == 0:
            return True
    except FileNotFoundError:
        pass

    # 尝试 xclip
    try:
        import subprocess
        process = subprocess.Popen(
            ['xclip', '-selection', 'clipboard'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        process.communicate(text.encode('utf-8'))
        if process.returncode == 0:
            return True
    except FileNotFoundError:
        pass

    print("Linux 剪贴板复制失败: 请安装 xsel 或 xclip", file=sys.stderr)
    print("安装命令:", file=sys.stderr)
    print("  Ubuntu/Debian: sudo apt-get install xsel", file=sys.stderr)
    print("  Fedora/RHEL: sudo dnf install xsel", file=sys.stderr)
    return False


def copy_to_clipboard(text: str) -> bool:
    """跨平台剪贴板复制"""
    os_name = platform.system()

    if os_name == 'Windows':
        return copy_to_clipboard_windows(text)
    elif os_name == 'Darwin':
        return copy_to_clipboard_macos(text)
    elif os_name == 'Linux':
        return copy_to_clipboard_linux(text)
    else:
        print(f"不支持的操作系统: {os_name}", file=sys.stderr)
        return False


def print_usage():
    """打印使用说明"""
    print("""
小红书剪贴板工具 - 用法

使用方法:
  python copy_to_clipboard.py text "要复制的文本"
  python copy_to_clipboard.py title "标题"
  python copy_to_clipboard.py content "正文内容"

参数:
  text     - 复制任意文本到剪贴板
  title    - 复制标题（带格式）
  content  - 复制正文内容（带格式）

示例:
  python copy_to_clipboard.py text "Hello, 小红书!"
  python copy_to_clipboard.py title "📚 学生党必看！"
  python copy_to_clipboard.py content "姐妹们！今天..."

发布流程:
  1. 使用本工具复制标题和正文
  2. 访问 https://creator.xiaohongshu.com/publish/publish
  3. 粘贴内容到对应位置
  4. 上传图片/视频
  5. 点击"发布"按钮
""")


def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    command = sys.argv[1].lower()

    if command in ['-h', '--help', 'help']:
        print_usage()
        sys.exit(0)

    if len(sys.argv) < 3:
        print("错误: 缺少文本参数", file=sys.stderr)
        print_usage()
        sys.exit(1)

    text = sys.argv[2]

    # 根据命令处理文本格式
    if command == 'title':
        # 标题格式化
        processed = text.strip()
        print(f"已复制标题 ({len(processed)}/20 字): {processed}")
    elif command == 'content':
        # 正文格式化
        processed = text.strip()
        print(f"已复制正文 ({len(processed)}/1000 字)")
    else:
        # 直接复制
        processed = text
        print(f"已复制到剪贴板")

    # 复制到剪贴板
    success = copy_to_clipboard(processed)

    if success:
        print("\n下一步:")
        print("1. 访问 https://creator.xiaohongshu.com/publish/publish")
        print("2. 粘贴内容")
        print("3. 上传图片/视频")
        print("4. 点击发布")
        sys.exit(0)
    else:
        print("\n复制失败，请手动复制以下内容:")
        print("=" * 50)
        print(processed)
        print("=" * 50)
        sys.exit(1)


if __name__ == '__main__':
    main()
