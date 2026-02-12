# Multi-Stage Onboarding with Tool Limitations

**Extracted:** 2026-01-27
**Context:** User onboarding when data collection exceeds tool constraints

## Problem

The `AskUserQuestion` tool has a limitation of 4 questions per call, but onboarding for multi-platform systems often requires 6+ questions to collect comprehensive user profiles.

**Specific scenario:**
- Layer 1: 3 shared questions (all platforms)
- Layer 2: 3 platform-specific questions
- Total: 6 questions needed
- Tool limit: 4 questions per call

## Solution

Split onboarding into multiple stages (layers) to work within tool constraints while collecting all necessary information.

### Pattern: Two-Layer Onboarding

#### Layer 1: Shared Information (3 questions)

Collect platform-agnostic information first:

```python
questions_layer1 = [
    {
        "question": "你主要用[平台]做什么？",
        "options": ["分享生活", "种草推荐", "记录成长", "商业推广", "Other"]
    },
    {
        "question": "你主要分享什么内容？",
        "options": ["美妆护肤", "穿搭时尚", "美食探店", "生活方式", "Other"]
    },
    {
        "question": "你希望的内容风格是？",
        "options": ["亲切可爱", "专业认真", "轻松幽默", "真实接地气", "Other"]
    }
]
```

**Purpose:** Establish user persona that applies across all platforms

#### Layer 2: Platform-Specific (3 questions)

Collect platform-specific customization:

```python
questions_layer2 = [
    {
        "question": "你的内容主要面向哪个群体？",
        "options": ["女性", "男性", "全部"]
    },
    {
        "question": "你更喜欢哪种风格？",
        "options": ["图文并茂", "文字为主", "视频", "Other"]
    },
    {
        "question": "你计划多久发布一次？",
        "options": ["每天", "每周", "每月", "不定期"]
    }
]
```

**Purpose:** Customize content for specific platform characteristics

## Implementation

### Check User Profile Status

```python
def check_onboarding_status(platform):
    profile_path = f"{platform}-create/references/user-profile.md"

    if not os.path.exists(profile_path):
        return "not_initialized"

    with open(profile_path, 'r') as f:
        content = f.read()
        if 'initialized: false' in content:
            return "not_initialized"

    return "initialized"
```

### Execute Layered Onboarding

```python
def run_onboarding(platform):
    # Stage 1: Shared questions
    print("👋 欢迎使用 {platform} 内容创作助手！")
    print("让我们先了解一些基本信息...\n")

    answers_layer1 = AskUserQuestion(
        questions=questions_layer1,
        max_selections=1
    )

    # Stage 2: Platform-specific questions
    print("\n现在让我们了解一些{platform}特定的偏好...\n")

    answers_layer2 = AskUserQuestion(
        questions=questions_layer2,
        max_selections=1
    )

    # Merge answers
    profile = {
        **answers_layer1,
        **answers_layer2,
        "initialized": True,
        "platform": platform
    }

    # Save profile
    save_user_profile(platform, profile)
```

## Example

**小红书 Onboarding:**

```
👋 欢迎使用小红书内容创作助手！
让我们先了解一些基本信息...

[Layer 1 - 3 Questions]
1. 你主要用小红书做什么？ → 种草推荐
2. 你主要分享什么内容？ → 美妆护肤
3. 你希望的内容风格是？ → 亲切可爱

现在让我们了解一些小红书特定的偏好...

[Layer 2 - 3 Questions]
1. 你的内容主要面向哪个群体？ → 女性
2. 你更喜欢哪种风格？ → 图文并茂（图片为主）
3. 你计划多久发布一次？ → 每周

✅ 用户画像配置完成！
```

## User Profile Structure

```yaml
# user-profile.md
initialized: true
platform: xiaohongshu

# Layer 1: Shared
usage_scenario: 种草推荐
content_domain: 美妆护肤
language_style: 亲切可爱

# Layer 2: Platform-specific
target_gender: 女性
content_format: 图文并茂（图片为主）
publish_frequency: 每周
```

## When to Use

**Activate this pattern when:**
- User onboarding requires more than 4 questions
- Questions can be logically split into layers
- Layer 1 questions are shared across multiple contexts
- Layer 2+ questions are specific to current context
- Using `AskUserQuestion` tool or similar with question limits

**Key triggers:**
- "How to collect more than 4 questions in onboarding?"
- Need to collect comprehensive user profiles
- Multi-platform systems with shared + specific preferences

## Benefits

### 1. Works Within Tool Constraints
- Each layer stays within 4-question limit
- No tool violation

### 2. Better User Experience
- Progressive disclosure (simple → complex)
- Less overwhelming than 6+ questions at once
- Clear stage transitions

### 3. Code Reusability
- Layer 1 shared across all platforms
- Layer 2 customized per platform
- DRY principle applied

### 4. Maintainability
- Easy to add/remove questions per layer
- Clear separation of concerns
- Profile structure is explicit

## Extension: Three-Layer Onboarding

For even more complex scenarios:

```
Layer 1: Core identity (2-3 questions)
  ↓
Layer 2: Platform preferences (2-3 questions)
  ↓
Layer 3: Advanced customization (2-3 questions)
```

## Related Patterns

- **Shared Module Inheritance**: See `multi-platform-skill-architecture.md`
- **Progressive Disclosure**: UX pattern for complex forms
- **Profile Persistence**: User profile storage and retrieval
