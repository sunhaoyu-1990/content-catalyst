#!/usr/bin/env python3
"""
跨平台剪贴板复制工具
支持 Windows、macOS、Linux

使用方法:
    python copy_to_clipboard.py text "要复制的文本"
    python copy_to_clipboard.py text --file /path/to/file.txt
"""

import sys
import platform
import subprocess


def copy_to_windows(text):
    """Windows 复制到剪贴板"""
    try:
        import win32clipboard
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(text, win32clipboard.CF_UNICODETEXT)
        win32clipboard.CloseClipboard()
        return True
    except ImportError:
        print("✗ 需要安装 pywin32: uv pip install pywin32")
        return False
    except Exception as e:
        print(f"✗ Windows 剪贴板操作失败: {e}")
        return False


def copy_to_macos(text):
    """macOS 复制到剪贴板"""
    try:
        process = subprocess.Popen(
            ['pbcopy', 'w'],
            stdin=subprocess.PIPE,
            text=True
        )
        process.communicate(text)
        if process.returncode == 0:
            return True
        else:
            print(f"✗ pbcopy 返回错误代码: {process.returncode}")
            return False
    except Exception as e:
        print(f"✗ macOS 剪贴板操作失败: {e}")
        return False


def copy_to_linux(text):
    """Linux 复制到剪贴板"""
    try:
        # 尝试 xclip
        process = subprocess.Popen(
            ['xclip', '-selection', 'clipboard'],
            stdin=subprocess.PIPE,
            text=True
        )
        process.communicate(text)
        if process.returncode == 0:
            return True
        else:
            print(f"✗ xclip 返回错误代码: {process.returncode}")
            return False
    except FileNotFoundError:
        # xclip 未安装，尝试 xsel
        try:
            process = subprocess.Popen(
                ['xsel', '--clipboard', '--input'],
                stdin=subprocess.PIPE,
                text=True
            )
            process.communicate(text)
            if process.returncode == 0:
                return True
            else:
                print(f"✗ xsel 返回错误代码: {process.returncode}")
                return False
        except Exception as e:
            print("✗ 需要安装 xclip 或 xsel:")
            print("  Ubuntu/Debian: sudo apt-get install xclip")
            print("  Fedora/RHEL: sudo dnf install xclip")
            return False
    except Exception as e:
        print(f"✗ Linux 剪贴板操作失败: {e}")
        return False


def main():
    if len(sys.argv) < 2:
        print("用法:")
        print("  python copy_to_clipboard.py text \"要复制的文本\"")
        print("  python copy_to_clipboard.py text --file /path/to/file.txt")
        sys.exit(1)

    # 解析参数
    if sys.argv[1] == "text":
        if "--file" in sys.argv:
            # 从文件读取
            file_index = sys.argv.index("--file") + 1
            if file_index >= len(sys.argv):
                print("✗ --file 参数后需要指定文件路径")
                sys.exit(1)
            file_path = sys.argv[file_index]
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read()
            except Exception as e:
                print(f"✗ 读取文件失败: {e}")
                sys.exit(1)
        else:
            # 从命令行参数读取
            text = ' '.join(sys.argv[2:])
    else:
        print("✗ 未知命令: " + sys.argv[1])
        print("可用命令: text")
        sys.exit(1)

    # 检查文本是否为空
    if not text or text.strip() == "":
        print("✗ 文本内容为空")
        sys.exit(1)

    # 根据操作系统选择复制方法
    os_name = platform.system()
    success = False

    if os_name == 'Windows':
        success = copy_to_windows(text)
    elif os_name == 'Darwin':
        success = copy_to_macos(text)
    elif os_name == 'Linux':
        success = copy_to_linux(text)
    else:
        print(f"✗ 不支持的操作系统: {os_name}")
        sys.exit(1)

    if success:
        text_preview = text[:50] + "..." if len(text) > 50 else text
        print(f"✓ 已复制到剪贴板: {text_preview}")
    else:
        sys.exit(1)


if __name__ == '__main__':
    main()
