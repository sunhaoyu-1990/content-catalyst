# Learned Patterns

Reusable patterns extracted from development sessions. Each pattern addresses a specific problem encountered during implementation.

## Available Patterns

### Platform & Infrastructure

**[Multi-Platform Skill Architecture](./multi-platform-skill-architecture.md)** (301 lines)
Building content creation assistants for multiple platforms with shared core logic
- **Problem**: Code duplication across 12+ skill implementations
- **Solution**: Inheritance-based architecture with shared base modules
- **Use when**: Implementing similar functionality across 3+ platforms

**[Platform-Specific Differentiation](./platform-specific-differentiation.md)** (301 lines)
Implementing same functionality for different platforms with platform-specific customizations
- **Problem**: Same workflow needs different weights, types, and keywords per platform
- **Solution**: Parameterization with platform-specific configuration files
- **Use when**: Platform differences are data-driven, not logic-driven

**[Skill Validation Framework](./skill-validation-framework.md)** (397 lines)
Validating complex skill architectures with shared modules and inheritance
- **Problem**: Manual validation of 12+ skill files is error-prone
- **Solution**: Automated validation script with comprehensive checks
- **Use when**: Multi-file skill architectures with inheritance

### User Experience

**[Multi-Stage Onboarding](./multi-stage-onboarding.md)** (212 lines)
User onboarding when data collection exceeds tool constraints
- **Problem**: AskUserQuestion tool limited to 4 questions, but onboarding needs 6+
- **Solution**: Split into Layer 1 (shared) and Layer 2 (platform-specific)
- **Use when**: Onboarding requires more questions than tool allows

### Data Management

**[Local Material Analysis Integration](./local-material-analysis-integration.md)** (322 lines)
Content creation systems that incorporate user's local documents
- **Problem**: Need to detect, analyze, and integrate local files (PDFs, notes)
- **Solution**: 3-stage pipeline (Import → Analyze → Integrate) with caching
- **Use when**: Users have local materials relevant to content generation

### Development Environment

**[Windows Bash Path Handling](./windows-bash-path-handling.md)** (112 lines)
Cross-platform development using Bash commands on Windows systems
- **Problem**: Bash commands fail with Windows backslash paths
- **Solution**: Use "cd + relative path" or forward slash conversion
- **Use when**: Bash tool on Windows with file paths

**[Nested Directory Creation](./nested-directory-creation.md)** (150 lines)
Multi-level directory structure creation on Windows systems
- **Problem**: mkdir -p doesn't create all nested subdirectories reliably
- **Solution**: Separate mkdir commands or loop-based creation
- **Use when**: Creating multi-level directory structures on Windows

### Testing & Automation

**[Browser Automation Fallback Strategy](./browser-automation-fallback-strategy.md)** (408 lines)
Playwright browser automation skills that cannot be fully tested in development
- **Problem**: Need to deliver functional code when browser environment isn't ready
- **Solution**: Layered approach (automation + manual guide + clipboard tool)
- **Use when**: Browser automation requires user interaction or environment setup

## Usage

### Apply a Pattern

1. Read the pattern file to understand the problem and solution
2. Adapt the example code to your specific context
3. Follow the "When to Use" section to verify applicability

### Extract New Patterns

Use the `/learn` command to extract new patterns from your session:

```bash
/learn
```

The system will:
1. Analyze the current session
2. Identify reusable patterns
3. Create skill files in this directory

## Pattern Format

Each pattern follows this structure:

```markdown
# [Pattern Name]

**Extracted:** [Date]
**Context:** [When this applies]

## Problem
[What problem this solves]

## Solution
[The pattern/technique/workaround]

## Example
[Code example if applicable]

## When to Use
[Trigger conditions]
```

## Contributing

When you solve a non-trivial problem, extract it as a pattern:

1. **Identify the problem** - What broke or didn't work?
2. **Document the solution** - What fixed it?
3. **Verify reusability** - Will this save time in future?
4. **Create pattern file** - Follow the format above
5. **Test the pattern** - Apply to similar scenarios

Don't extract:
- Trivial fixes (typos, simple syntax errors)
- One-time issues (specific API outages)
- Platform-specific quirks (unless reusable principle)

## Statistics

- **Total patterns**: 7
- **Total lines**: 1,902
- **Average lines per pattern**: 272
- **Last updated**: 2026-01-27

## Related Resources

- [/.claude/commands/learn.md](../../commands/learn.md) - Learn command documentation
- [/.claude/skills/_shared/](../_shared/) - Shared skill modules
- [/.claude/templates/](../../templates/) - Skill templates
