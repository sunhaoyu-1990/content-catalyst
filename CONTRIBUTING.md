# 贡献指南

感谢你对内容创作助手项目的关注！我们欢迎各种形式的贡献。

---

## 🤝 如何贡献

### 报告问题

如果你发现了 Bug 或有功能建议：

1. 检查 [Issues](../../issues) 是否已存在类似问题
2. 如果没有，创建新的 Issue，包含：
   - 清晰的标题
   - 详细的复现步骤（针对 Bug）
   - 预期行为 vs 实际行为
   - 环境信息（操作系统、Claude Code 版本）

### 提交代码

1. **Fork** 本仓库
2. 创建特性分支：`git checkout -b feature/your-feature`
3. 提交更改：`git commit -m "feat: 添加某功能"`
4. 推送分支：`git push origin feature/your-feature`
5. 创建 Pull Request

---

## 📋 开发规范

### 技能开发

技能位于 `.claude/skills/` 目录：

```
.claude/skills/
├── _shared/              # 共享核心逻辑
│   ├── collect-base      # 4轮搜索策略
│   ├── create-base       # Onboarding + 资料整合
│   ├── filter-base       # 10分评分系统
│   └── publish-base      # 自动化发布
└── {platform}/           # 平台特定技能
    ├── -collect
    ├── -create
    ├── -filter
    └── -publish
```

### 规则开发

规则位于 `.claude/rules/` 目录，用于自动化触发：

```
.claude/rules/
├── content-creation-complete.md    # 完整模式流程控制
├── content-post-checklist.md       # 创作后审查清单
└── content-image-marking.md        # 图片标记指南
```

### 配置开发

平台配置位于 `.claude/profiles/` 目录：

```
.claude/profiles/
├── content-creator-common.md    # 通用配置
├── zhihu-creator.md          # 知乎配置
├── xiaohongshu-creator.md    # 小红书配置
├── linkedin-creator.md        # 领英配置
└── x-twitter-creator.md       # X/Twitter 配置
```

---

## 📝 提交信息规范

使用 [Conventional Commits](https://www.conventionalcommits.org/) 格式：

```
<type>: <description>

[optional body]
```

**类型 (type)**：
- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档更新
- `refactor`: 代码重构
- `chore`: 构建/工具更新
- `test`: 测试相关

**示例**：
```
feat: 添加 B站平台支持

- 新增 bilibili-collect 技能
- 新增 bilibili-create 技能
- 更新 README 添加平台说明
```

---

## ✅ 代码审查

所有 Pull Request 需要通过：

1. **代码风格检查**：遵循项目编码规范
2. **功能测试**：确保技能/规则正常工作
3. **文档更新**：相关文档同步更新
4. **无冲突**：与主分支可顺利合并

---

## 🌟 贡献者

感谢所有贡献者！你的名字将出现在 [Contributors](../../graphs/contributors) 列表中。

---

## 📧 联系方式

- 提 Issue：最直接的方式
- 讨论：在 Issue 中提出想法
- PR：直接提交代码

---

**再次感谢你的贡献！**
