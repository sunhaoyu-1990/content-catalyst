# Windows Bash Path Handling

**Extracted:** 2026-01-27
**Context:** Cross-platform development using Bash commands on Windows systems

## Problem

Bash commands fail when using Windows backslash paths (`D:\path\to\file`) in Git Bash or similar environments on Windows. The backslash character is interpreted as an escape character, causing command failures.

**Error Examples:**
```bash
cd D:\BaiduSyncdisk\ai_work_record
# Output: bash: cd: D:BaiduSyncdiskai_work_record: No such file or directory
```

## Solution

Use one of these patterns to ensure path compatibility:

### Pattern 1: cd + Relative Path (Recommended)

```bash
cd "relative/path/from/current/dir" && command
```

**Why it works:**
- Avoids absolute path issues entirely
- Works across all platforms
- No path conversion needed

**Example:**
```bash
cd ".claude/skills/zhihu-collect" && ls -la
```

### Pattern 2: Forward Slash Conversion

Convert all backslashes to forward slashes:

```bash
# WRONG (Windows backslash)
cd D:\BaiduSyncdisk\ai_work_record

# CORRECT (Forward slash)
cd D:/BaiduSyncdisk/ai_work_record
```

**Why it works:**
- Git Bash on Windows accepts forward slashes
- Forward slashes are POSIX-compliant
- No escape character interpretation issues

### Pattern 3: Quote + Relative Path

```bash
cd "relative/path" && command
```

**When to use:**
- Paths contain spaces
- Paths contain special characters
- Multiple commands in sequence

## Example

**WRONG:**
```bash
cd D:\BaiduSyncdisk\ai_work_record\.claude\skills && ls
```

**CORRECT:**
```bash
cd ".claude/skills" && ls
# OR
cd D:/BaiduSyncdisk/ai_work_record/.claude/skills && ls
```

## When to Use

**Activate this pattern when:**
- Working on Windows with Git Bash, MSYS2, or WSL
- Using Bash tool in Claude Code on Windows
- Seeing "No such file or directory" errors
- Paths contain backslashes
- Executing multi-command sequences with `&&`

**Key trigger:** Any Bash command on Windows that involves file paths

## Additional Notes

### Absolute Path Handling

If you must use absolute paths, prefer forward slashes:
```bash
cd "D:/BaiduSyncdisk/ai_work_record" && command
```

### Nested Directory Operations

For nested operations, always use `cd` prefix:
```bash
cd "relative/path" && mkdir -p subdir && cd subdir && command
```

### Tool-Specific Considerations

Some tools (Read, Write, Edit) accept absolute paths with backslashes on Windows, but Bash tool always requires forward slash or relative path + `cd`.

## Related Patterns

- **Nested Directory Creation**: See `nested-directory-creation.md`
- **Path Conversion Automation**: Can be combined with shell functions for bulk operations
