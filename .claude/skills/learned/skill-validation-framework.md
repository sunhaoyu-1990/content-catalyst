# Skill Validation Framework

**Extracted:** 2026-01-27
**Context:** Validating multi-platform skill implementations with shared modules and inheritance

## Problem

When implementing a complex skill architecture with 12+ skill files, shared modules, and inheritance relationships, manual validation is error-prone and time-consuming. Need automated validation to ensure:
1. YAML frontmatter is correct
2. Shared module references are valid
3. Configuration files are well-formed
4. Dependencies are available
5. Directory structure is consistent

**Challenge:** How to validate complex skill architecture systematically and catch errors early?

## Solution

Create a validation framework that checks all aspects of skill integrity and provides clear error messages.

### Validation Script Structure

```python
#!/usr/bin/env python3
"""
SKILL.md Format Validator

Validates:
1. YAML frontmatter (name, description required)
2. references/ directory configuration files
3. Shared module inheritance paths
4. Dependency availability (Playwright, WebSearch)
"""

import os
import sys
import re
import yaml
from pathlib import Path
from typing import List, Tuple


class SkillValidator:
    def __init__(self, skills_dir: str):
        self.skills_dir = Path(skills_dir)
        self.errors = []
        self.warnings = []

    def validate_skill(self, skill_name: str) -> bool:
        """Validate a single skill"""
        # Reset errors/warnings
        self.errors = []
        self.warnings = []

        print(f"\n{'='*60}")
        print(f"Validating Skill: {skill_name}")
        print(f"{'='*60}")

        skill_path = self.skills_dir / skill_name
        if not skill_path.exists():
            print(f"✗ Skill directory doesn't exist: {skill_path}")
            return False

        # Run all validation checks
        self._validate_yaml_frontmatter(skill_path / "SKILL.md")
        self._validate_references(skill_path)
        self._validate_shared_inheritance(skill_path / "SKILL.md")
        self._validate_directory_structure(skill_path)

        # Print results
        self._print_results(skill_name)

        return len(self.errors) == 0

    def validate_all(self) -> Tuple[int, int]:
        """Validate all skills"""
        skill_dirs = [d for d in self.skills_dir.iterdir()
                      if d.is_dir() and not d.name.startswith('_')]

        print(f"\nFound {len(skill_dirs)} skill directories")

        passed = 0
        failed = 0

        for skill_dir in skill_dirs:
            if self.validate_skill(skill_dir.name):
                passed += 1
            else:
                failed += 1

        print(f"\n{'='*60}")
        print(f"Validation Complete: {passed} passed, {failed} failed")
        print(f"{'='*60}")

        return passed, failed
```

### Validation Checks

#### Check 1: YAML Frontmatter Validation

```python
def _validate_yaml_frontmatter(self, skill_file: Path):
    """Validate YAML frontmatter structure"""
    try:
        with open(skill_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check YAML frontmatter exists
        if not content.startswith('---'):
            self.errors.append("Missing YAML frontmatter (must start with ---)")
            return

        # Extract YAML content
        yaml_end = content.find('---', 3)
        if yaml_end == -1:
            self.errors.append("YAML frontmatter not closed (needs second ---)")
            return

        yaml_content = content[3:yaml_end].strip()

        # Parse YAML
        try:
            frontmatter = yaml.safe_load(yaml_content)
        except yaml.YAMLError as e:
            self.errors.append(f"YAML parsing failed: {e}")
            return

        # Check required fields
        if 'name' not in frontmatter:
            self.errors.append("Missing required field: name")
        elif not isinstance(frontmatter['name'], str):
            self.errors.append("name must be a string")

        if 'description' not in frontmatter:
            self.errors.append("Missing required field: description")
        elif not isinstance(frontmatter['description'], str):
            self.errors.append("description must be a string")

        # Check recommended patterns
        if 'name' in frontmatter:
            name = frontmatter['name']
            if not re.match(r'^[a-z0-9-]+$', name):
                self.warnings.append(
                    f"name should use lowercase, numbers, and hyphens only: {name}"
                )

        print("✓ YAML frontmatter format is correct")

    except Exception as e:
        self.errors.append(f"Failed to read file: {e}")
```

#### Check 2: References Directory Validation

```python
def _validate_references(self, skill_path: Path):
    """Validate references/ directory configuration"""
    refs_dir = skill_path / "references"
    if not refs_dir.exists():
        self.warnings.append("references/ directory doesn't exist (optional)")
        return

    # Check configuration files
    config_files = (
        list(refs_dir.glob("*.md")) +
        list(refs_dir.glob("*.yaml")) +
        list(refs_dir.glob("*.yml"))
    )

    for config_file in config_files:
        if config_file.suffix in ['.yaml', '.yml']:
            self._validate_yaml_file(config_file)
        else:
            # Markdown file basic checks
            if config_file.stat().st_size == 0:
                self.warnings.append(f"Config file is empty: {config_file.name}")

    print(f"✓ references/ directory check complete ({len(config_files)} files)")

def _validate_yaml_file(self, yaml_file: Path):
    """Validate YAML configuration file"""
    try:
        with open(yaml_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for YAML frontmatter in markdown files
        if content.startswith('---'):
            yaml_end = content.find('---', 3)
            if yaml_end != -1:
                yaml_content = content[3:yaml_end].strip()
                yaml.safe_load(yaml_content)

        print(f"  ✓ {yaml_file.name}")

    except yaml.YAMLError as e:
        self.errors.append(f"YAML file format error in {yaml_file.name}: {e}")
    except Exception as e:
        self.warnings.append(f"Cannot validate {yaml_file.name}: {e}")
```

#### Check 3: Shared Module Inheritance Validation

```python
def _validate_shared_inheritance(self, skill_file: Path):
    """Validate shared module references are valid"""
    try:
        with open(skill_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for shared module references
        if '../_shared/' in content or '继承:' in content:
            # Extract inheritance declaration
            inherit_match = re.search(
                r'继承:\s*\.\./_shared/([-\w]+\.md)',
                content
            )
            if inherit_match:
                shared_module = inherit_match.group(1)
                shared_path = self.skills_dir / '_shared' / shared_module

                if not shared_path.exists():
                    self.errors.append(
                        f"Referenced shared module doesn't exist: {shared_module}"
                    )
                else:
                    print(f"✓ Shared module reference valid: {shared_module}")

    except Exception as e:
        self.warnings.append(f"Cannot validate shared module reference: {e}")
```

#### Check 4: Directory Structure Validation

```python
def _validate_directory_structure(self, skill_path: Path):
    """Validate expected directory structure"""
    expected_dirs = ['references', 'assets']
    expected_subdirs = {
        'assets': ['materials', 'analyzed', 'templates']
    }

    for dir_name in expected_dirs:
        dir_path = skill_path / dir_name
        if not dir_path.exists():
            self.warnings.append(f"Expected directory missing: {dir_name}/")
        elif dir_name in expected_subdirs:
            # Check subdirectories
            for subdir in expected_subdirs[dir_name]:
                subdir_path = dir_path / subdir
                if not subdir_path.exists():
                    self.warnings.append(
                        f"Expected subdirectory missing: {dir_name}/{subdir}/"
                    )

    print("✓ Directory structure check complete")
```

### Usage

```bash
# Validate single skill
python .claude/skills/_shared/validate-skill.py zhihu-collect

# Validate all skills
python .claude/skills/_shared/validate-skill.py --all

# Interactive mode
python .claude/skills/_shared/validate-skill.py
```

### Output Format

```
============================================================
Validating Skill: zhihu-collect
============================================================
✓ YAML frontmatter format is correct
✓ references/ directory check complete (3 files)
  ✓ search-keywords.md
  ✓ content-types.md
  ✓ scoring-weights.md
✓ Shared module reference valid: collect-base.md
✓ Directory structure check complete

Warnings (1):
  ⚠ Expected subdirectory missing: assets/templates/

============================================================
✅ zhihu-collect validation passed
============================================================
```

## When to Use

**Activate this pattern when:**
- Implementing complex skill architectures
- Using shared modules and inheritance
- Multiple developers contributing skills
- Need to catch errors early (pre-commit)
- Maintaining consistency across many skills

**Key triggers:**
- "How to ensure all skills follow the same structure?"
- "Need to validate skill files before committing"
- "Shared module references are breaking"
- "YAML frontmatter errors causing issues"

## Benefits

### 1. Early Error Detection
- Catch YAML errors before runtime
- Validate inheritance chains
- Check file references exist

### 2. Consistency
- Enforce directory structure
- Ensure required fields present
- Validate naming conventions

### 3. Developer Experience
- Clear error messages
- Specific file locations
- Actionable feedback

### 4. Automation
- Can run in CI/CD
- Pre-commit hooks
- Batch validation

## Extension: Pre-Commit Integration

```bash
# .git/hooks/pre-commit
#!/bin/bash

echo "Running skill validation..."
python .claude/skills/_shared/validate-skill.py --all

if [ $? -ne 0 ]; then
    echo "❌ Skill validation failed. Please fix errors before committing."
    exit 1
fi

echo "✅ All skills validated successfully"
```

## Extension: CI/CD Integration

```yaml
# .github/workflows/validate-skills.yml
name: Validate Skills

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'
      - name: Install dependencies
        run: pip install pyyaml
      - name: Validate skills
        run: python .claude/skills/_shared/validate-skill.py --all
```

## Best Practices

### 1. Validation Levels
- **Required**: Must pass (YAML, inheritance)
- **Warning**: Should fix (empty files, naming)
- **Info**: For awareness (file counts)

### 2. Error Messages
- Be specific about file and location
- Provide actionable suggestions
- Show what was expected vs. found

### 3. Performance
- Cache file reads
- Parallel validation for multiple skills
- Early exit on critical errors

### 4. Extensibility
- Easy to add new validation rules
- Platform-specific checks
- Custom rule plugins

## Related Patterns

- **Multi-Platform Skill Architecture**: Validates inheritance chains
- **Shared Module Management**: Ensures shared modules exist
- **Configuration File Validation**: Checks YAML/Markdown syntax
