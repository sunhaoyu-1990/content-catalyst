# Nested Directory Creation on Windows

**Extracted:** 2026-01-27
**Context:** Multi-level directory structure creation on Windows systems

## Problem

When creating nested directories with `mkdir -p` on Windows, intermediate directories may not be created as expected. The command may fail silently or create only partial directory structures.

**Issue Example:**
```bash
mkdir -p assets/materials/reports assets/materials/notes assets/materials/articles
# Result: Only some directories created, or command fails
```

## Solution

Use one of these patterns to ensure reliable nested directory creation:

### Pattern 1: Separate mkdir Commands (Most Reliable)

```bash
mkdir -p assets/materials/reports
mkdir -p assets/materials/notes
mkdir -p assets/materials/articles
```

**Why it works:**
- Each directory path is created independently
- Clear error messages if any path fails
- Works consistently across platforms

### Pattern 2: Loop-Based Creation

```bash
for dir in reports notes articles; do
    mkdir -p "assets/materials/$dir"
done
```

**When to use:**
- Creating many similar directories
- Paths follow a predictable pattern
- Need to ensure all or nothing creation

### Pattern 3: Sequential mkdir with cd

```bash
cd "parent/path" && mkdir -p subdir1/subdir2 && mkdir -p subdir3/subdir4
```

**Advantages:**
- Shorter absolute paths
- Easier to read
- Works with relative paths

## Example

**Scenario:** Create material analysis directory structure

**WRONG:**
```bash
mkdir -p assets/materials/{reports,notes,articles} assets/analyzed assets/templates/{type1,type2}
# May fail or create incomplete structure
```

**CORRECT (Pattern 1):**
```bash
mkdir -p assets/materials/reports
mkdir -p assets/materials/notes
mkdir -p assets/materials/articles
mkdir -p assets/analyzed
mkdir -p assets/templates/种草笔记
mkdir -p assets/templates/测评分享
```

**CORRECT (Pattern 2):**
```bash
# Material directories
for dir in reports notes articles; do
    mkdir -p "assets/materials/$dir"
done

# Template directories
for type in 种草笔记 测评分享 生活方式; do
    mkdir -p "assets/templates/$type"
done
```

## When to Use

**Activate this pattern when:**
- Creating multi-level directory structures
- Directory names contain spaces or special characters
- Working on Windows with Git Bash or similar
- `mkdir -p` has failed or created incomplete structures
- Need to ensure all directories are created successfully

**Key trigger:** Nested directory creation commands on Windows

## Verification Pattern

After creating directories, verify success:

```bash
# Verify all directories were created
ls -la assets/materials/
ls -la assets/templates/

# Or check each specific directory
for dir in reports notes articles; do
    if [ -d "assets/materials/$dir" ]; then
        echo "✓ Created: assets/materials/$dir"
    else
        echo "✗ Failed: assets/materials/$dir"
    fi
done
```

## Combined Pattern with Windows Path Handling

**Best practice:** Combine with Windows path handling pattern:

```bash
cd ".claude/skills/xiaohongshu-create" && \
mkdir -p assets/materials/reports && \
mkdir -p assets/materials/notes && \
mkdir -p assets/materials/articles && \
ls -la assets/materials/
```

## Platform-Specific Notes

### Windows (Git Bash/MSYS2)
- Use separate `mkdir -p` commands
- Quote paths with spaces
- Use forward slashes

### Linux/macOS
- `mkdir -p parent/{child1,child2,child3}` works reliably
- Brace expansion is native to bash

### Cross-Platform
- Use separate commands for maximum compatibility
- Or use loop-based approach

## Related Patterns

- **Windows Bash Path Handling**: See `windows-bash-path-handling.md`
- **Directory Structure Verification**: Use `ls -la` after creation
