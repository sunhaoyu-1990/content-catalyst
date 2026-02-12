# Browser Automation Fallback Strategy

**Extracted:** 2026-01-27
**Context:** Playwright browser automation skills that cannot be fully tested in development environment

## Problem

Browser automation skills (e.g., publishing to social media platforms) require:
1. Browser environment setup (Playwright, browsers)
2. User authentication (cookies, sessions)
3. Network access to target platforms
4. Interactive testing (cannot be fully automated)

**Challenge:** How to deliver functional code when environment is not ready for full testing?

## Solution

Implement a layered approach: Core automation code + Manual testing guide + Clipboard fallback tool.

### Layer 1: Core Automation Code

Implement full Playwright automation with proper error handling:

```typescript
// publish.ts
import { chromium, Browser, Page, BrowserContext } from 'playwright';

export class PlatformPublisher {
  private browser: Browser | null = null;
  private context: BrowserContext | null = null;
  private page: Page | null = null;

  async initialize(platform: string) {
    try {
      // Launch browser
      this.browser = await chromium.launch({
        headless: false,  // Allow user to see what's happening
        slowMo: 50,       // Slow down for debugging
      });

      // Create context with cookies if available
      const cookiesPath = this.getCookiePath(platform);
      if (fs.existsSync(cookiesPath)) {
        const cookies = JSON.parse(fs.readFileSync(cookiesPath, 'utf-8'));
        this.context = await this.browser.newContext({
          storageState: { cookies },
        });
      } else {
        this.context = await this.browser.newContext();
        console.log('⚠️  No cookies found. User will need to log in manually.');
      }

      this.page = await this.context.newPage();

      return true;
    } catch (error) {
      console.error('Failed to initialize browser:', error);
      return false;
    }
  }

  async publishToDraft(content: Content, platform: string) {
    if (!this.page) {
      throw new Error('Browser not initialized');
    }

    try {
      // Navigate to platform
      await this.page.goto(this.getPlatformUrl(platform));

      // Check if authenticated
      if (await this.needsAuthentication()) {
        console.log('🔐 Authentication required. Please log in manually.');
        console.log('💡 After logging in, cookies will be saved for future use.');

        // Wait for user to log in
        await this.page.waitForURL(/dashboard|home|feed/, { timeout: 0 });

        // Save cookies for future use
        await this.saveCookies(platform);
      }

      // Fill content form
      await this.fillContentForm(content);

      // Save to draft (NOT publish)
      await this.saveToDraft();

      console.log('✅ Content saved to draft!');

      // Save cookies before closing
      await this.saveCookies(platform);

      return true;
    } catch (error) {
      console.error('Publishing failed:', error);
      return false;
    }
  }

  private async saveCookies(platform: string) {
    if (!this.context) return;

    const cookies = await this.context.cookies();
    const cookiesPath = this.getCookiePath(platform);
    fs.writeFileSync(cookiesPath, JSON.stringify(cookies, null, 2));
    console.log(`💾 Cookies saved to ${cookiesPath}`);
  }

  private async needsAuthentication(): Promise<boolean> {
    if (!this.page) return true;

    // Platform-specific authentication check
    const url = this.page.url();
    return url.includes('/login') || url.includes('/signin');
  }
}
```

### Layer 2: Manual Testing Guide

Provide comprehensive manual testing instructions:

```markdown
# Manual Testing Guide

## Prerequisites

1. Install dependencies:
   ```bash
   npm install playwright
   npx playwright install chromium
   ```

2. Configure cookie storage:
   ```bash
   mkdir -p ~/.content-creator/cookies
   ```

## Testing Steps

### Test 1: Browser Launch

```bash
npm run test:publish -- --test=launch
```

**Expected:**
- Browser window opens
- No authentication errors
- Browser stays open

**If fails:**
- Check Playwright installation
- Check browser installation
- Check firewall/antivirus settings

### Test 2: Authentication

```bash
npm run test:publish -- --test=auth
```

**Expected:**
- Browser navigates to platform login page
- User can log in manually
- Cookies are saved after login
- Next run uses saved cookies

**If fails:**
- Check cookie storage path
- Check file permissions
- Clear old cookies and retry

### Test 3: Draft Creation

```bash
npm run test:publish -- --test=draft
```

**Expected:**
- Content is filled into form fields
- Images are uploaded (if any)
- Content is saved to draft (NOT published)
- Draft appears in platform's draft section

**If fails:**
- Check platform UI hasn't changed
- Check CSS selectors
- Check form field IDs/classes

### Test 4: Full Workflow

```bash
npm run publish -- --platform=xiaohongshu --content=test.md
```

**Expected:**
- Browser opens and navigates
- User logs in (first time only)
- Content is filled and saved to draft
- Browser closes
- Cookies saved

**If fails:**
- Check console error messages
- Check browser screenshot (saved automatically)
- Check logs in `logs/` directory
```

### Layer 3: Clipboard Fallback Tool

Provide a simple clipboard-based fallback:

```python
# clipboard_tool.py
import pyperclip
import sys

def copy_to_clipboard(content: str, platform: str):
    """Copy content to clipboard for manual pasting"""

    # Platform-specific formatting
    if platform == 'xiaohongshu':
        # 小红书: Add line breaks and emoji placeholders
        formatted = format_for_xiaohongshu(content)
    elif platform == 'linkedin':
        # 领英: Add professional formatting
        formatted = format_for_linkedin(content)
    elif platform == 'zhihu':
        # 知乎: Add markdown formatting
        formatted = format_for_zhihu(content)
    else:
        formatted = content

    # Copy to clipboard
    pyperclip.copy(formatted)

    print(f"✅ Content copied to clipboard!")
    print(f"📋 Platform: {platform}")
    print(f"🔢 Length: {len(formatted)} characters")
    print(f"\n📝 Next steps:")
    print(f"1. Open {platform} in your browser")
    print(f"2. Create new post")
    print(f"3. Paste content (Ctrl+V / Cmd+V)")
    print(f"4. Review and publish")

def format_for_xiaohongshu(content: str) -> str:
    """Format content for 小红书"""
    # Add extra line breaks
    content = content.replace('\n', '\n\n')

    # Add emoji placeholders if not present
    if not any(emoji in content for emoji in ['😊', '🔥', '💡']):
        content = '✨ ' + content

    return content

def format_for_linkedin(content: str) -> str:
    """Format content for 领英"""
    # Ensure proper spacing
    content = content.replace('\n\n\n', '\n\n')

    # Add hashtags if not present
    if not '#' in content:
        content += '\n\n#Professional #Networking #Growth'

    return content

def format_for_zhihu(content: str) -> str:
    """Format content for 知乎"""
    # Ensure markdown headers
    lines = content.split('\n')
    formatted_lines = []

    for line in lines:
        if line and not line.startswith('#'):
            # Add bold to key points (heuristic)
            if '：' in line or ':' in line:
                line = f"**{line}**"
        formatted_lines.append(line)

    return '\n'.join(formatted_lines)
```

## Integration Pattern

### Skill Implementation

```markdown
# Platform Publish

## Execution Steps

1. **Check environment**
   ```bash
   npx playwright --version
   npx playwright install chromium
   ```

2. **Try automation**
   ```bash
   npm run publish -- --platform=platform --content=path/to/content.md
   ```

3. **If automation fails**
   - Show error message
   - Suggest manual testing guide
   - Offer clipboard fallback

4. **Clipboard fallback**
   ```bash
   python clipboard_tool.py --platform=platform --content=path/to/content.md
   ```
```

## When to Use

**Activate this pattern when:**
- Implementing browser automation features
- Full testing environment is not available
- User authentication is required
- Need to deliver working code despite testing limitations
- Platform UI may change frequently

**Key triggers:**
- "I can't test this fully in development"
- "Browser automation needs user interaction"
- "How to handle authentication in automation?"
- "What if the automation script fails?"

## Benefits

### 1. Progressive Enhancement
- Automation works when environment is ready
- Fallback to manual process when not
- User can still achieve goal either way

### 2. Clear Path Forward
- Manual testing guide provides steps
- Clipboard tool ensures immediate usability
- Error messages guide troubleshooting

### 3. Development Efficiency
- Don't block on environment setup
- Deliver working code immediately
- Test automation when ready

### 4. User Flexibility
- Users can choose automation or manual
- Clipboard tool works on any platform
- No dependency on browser automation

## Best Practices

### 1. Error Messages

```typescript
if (error instanceof BrowserNotInstalledError) {
  console.error('❌ Playwright browser not installed');
  console.log('💡 Run: npx playwright install chromium');
  console.log('📋 Or use clipboard tool: python clipboard_tool.py');
}
```

### 2. Screenshot on Error

```typescript
try {
  await publishToDraft(content);
} catch (error) {
  // Save screenshot for debugging
  if (this.page) {
    await this.page.screenshot({
      path: `logs/error-${Date.now()}.png`
    });
  }
  throw error;
}
```

### 3. Verbose Logging

```typescript
console.log('🌐 Navigating to...', url);
console.log('📝 Filling title field...');
console.log('✅ Title filled');
console.log('📝 Filling body field...');
console.log('✅ Body filled');
console.log('💾 Saving to draft...');
```

### 4. Cookie Security

```typescript
// Never log cookie values
console.log(`💾 Cookies saved to ${cookiesPath}`);

// Warn user about security
console.log('⚠️  Cookies contain sensitive information.');
console.log('🔒 Keep cookie files secure and private.');
```

## Related Patterns

- **Graceful Degradation**: Core features work without enhancements
- **Progressive Enhancement**: Advanced features when environment supports
- **Manual Testing Guides**: Clear steps for manual verification
