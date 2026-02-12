# 内容创作助手 - 核心规范

**版本**: v1.5
**最后更新**: 2026-01-30
**状态**: 规则驱动架构

---

## 更新日志

- v1.5 (2026-01-30): **架构重构** - 引入规则驱动架构；图片标记和审查清单自动触发；简化模式选择逻辑
- v1.4 (2026-01-29): **新增技能** - 添加 content-reviewer 和 language-simplifier 技能
- v1.3 (2026-01-27): **文档重构** - 拆分详细文档，引入 @ 引用系统
- v1.2 (2026-01-27): 应用 5 种启发式方法优化
- v1.1 (2026-01-27): 经过 Quick-Spec + Adversarial Review + Party Mode 专家评审
- v1.0 (2026-01-27): 初始版本

---

## 核心原则

### 1. 真实性优先
- ✅ 所有事实性声明需有可验证来源
- ✅ 数据引用需标注出处（官方文档、学术论文、权威媒体）
- ❌ 不得杜撰产品功能、数据、案例

### 2. 平台适配
- ✅ 内容类型符合平台特色（知乎专业/小红书种草/领英商业/X简洁）
- ✅ 字数、格式、话题标签符合平台要求
- ❌ 避免违反社区规则的内容

### 3. 用户价值
- ✅ 提供可行动的建议或工具
- ✅ 解答用户实际问题或满足信息需求
- ❌ 纯广告、无实质内容的"水文"

### 4. 人工审核
- ✅ 事实准确性：数据、名称、日期需核实
- ✅ 逻辑一致性：前后论述不矛盾
- ✅ 语言自然性：符合中文表达习惯

### 5. 原创性
- ✅ 引用内容需注明来源
- ✅ 原创观点需有独立思考
- ❌ 不得直接复制粘贴他人内容

---

## 项目架构

### 技术栈

```
内容创作助手
├── 核心引擎: Claude AI (Claude Code)
├── 技能系统: .claude/skills/
├── 规则系统: .claude/rules/
├── 内容产出: workspace/
└── 对话记录: talk_with_ai/
```

### 目录结构

```
ai_work_record/
├── .claude/
│   ├── skills/              # 技能定义
│   │   ├── _shared/         # 共享核心逻辑
│   │   │   ├── collect-base    # 4轮搜索策略
│   │   │   ├── create-base     # Onboarding + 资料整合
│   │   │   ├── filter-base     # 10分评分系统
│   │   │   └── publish-base    # 自动化发布
│   │   ├── {platform}/     # 平台特定技能
│   │   │   ├── -collect
│   │   │   ├── -create
│   │   │   ├── -filter
│   │   │   └── -publish
│   │   ├── content-reviewer/
│   │   └── language-simplifier/
│   └── rules/              # 自动化规则
│       ├── content-creation-complete.md
│       ├── content-post-checklist.md
│       └── content-image-marking.md
├── workspace/             # 创作产出
│   ├── index.md
│   └── {topic}/{version}/
│       ├── 00_collect/
│       ├── 01_filter/
│       ├── 02_create/{platform}/
│       ├── 03_publish/{platform}/
│       └── task.md
├── talk_with_ai/          # 对话记录
│   ├── index.md
│   └── {topic}/{version}/
│       ├── conversation.md
│       ├── summary.md
│       ├── insights.md
│       ├── actions.md
│       └── tags.txt
├── docs/                  # 详细文档
│   └── content-creation-guides/
├── CLAUDE.md             # 本文件（核心规范）
└── README.md             # 用户指南
```

### 版本管理规则

- 首次创作：`{YYYY-MM-DD}`
- 后续创作：`v2`, `v3`, `v4`...
- 同日多次：`{YYYY-MM-DD}-a`, `{YYYY-MM-DD}-b`

---

## 技能系统架构

### 技能目录结构

```
.claude/skills/
├── _shared/              # 共享核心逻辑
│   ├── collect-base      # 4轮搜索策略
│   ├── create-base       # Onboarding + 资料整合
│   ├── filter-base       # 10分评分系统
│   └── publish-base      # 自动化发布
│
├── content-reviewer/     # 内容审查技能
│   └── skill.md          # 审查简化概念、术语、结构、图片
│
├── language-simplifier/  # 语言简化技能
│   └── skill.md          # 大众版/学生版/儿童版转换
│
└── {platform}/           # 平台特定技能
    ├── -collect          # 平台搜索关键词
    ├── -create           # 平台内容类型
    ├── -filter           # 平台评分权重
    └── -publish          # 平台发布方式
```

### Collect 工作流程（4轮搜索）

```
第1轮: 核心关键词搜索
    ↓
第2轮: 热门话题搜索
    ↓
第3轮: 竞品文章分析
    ↓
第4轮: 深度资料挖掘
    ↓
输出: materials.md
```

### Filter 评分系统（10分制）

```
总分 = Σ(维度权重 × 维度得分)

知乎: 专业性(4) + 可信度(3) + 热度(2) + 相关性(1)
小红书: 热度(5) + 种草价值(3) + 争议性(2) + 相关性(0)
领英: 商业价值(4) + 专业性(3) + 热度(2) + 相关性(1)
X: 影响力(4) + 相关性(3) + 时效性(2) + 传播度(1)
```

---

## 平台配置

| 平台 | 评分权重 | 阈值 | 风格 | 内容类型 |
|------|---------|------|------|---------|
| **知乎** | 专业性(4)+可信度(3)+热度(2)+相关性(1) | ≥7 | 专业严肃 | 技术文章、专业回答 |
| **小红书** | 热度(5)+种草价值(3)+争议性(2)+相关性(0) | ≥7 | 亲和力强 | 种草笔记、测评分享 |
| **领英** | 商业价值(4)+专业性(3)+热度(2)+相关性(1) | ≥7 | 职业化 | 行业洞察、管理经验 |
| **X (Twitter)** | 影响力(4)+相关性(3)+时效性(2)+传播度(1) | ≥7 | 简洁有力 | 短推文、长线程 |

**详细配置**: `@platform-configs.md`

---

## 规则驱动架构

### 规则文件

```
.claude/rules/
├── content-creation-complete.md    # 完整模式流程控制
├── content-post-checklist.md       # 创作后审查清单
└── content-image-marking.md        # 图片标记指南
```

### 规则触发机制

| 规则文件 | 触发条件 | 适用模式 | 执行内容 |
|---------|---------|---------|---------|
| `content-creation-complete.md` | 检测到4阶段目录结构 | 完整模式 | 引导 collect→filter→create→publish 流程 |
| `content-post-checklist.md` | 文章初稿完成（>1000字） | 极简+完整 | 6维度质量审查 |
| `content-image-marking.md` | 审查通过 | 极简+完整 | 自动添加图片标记 |

### 自动化流程（完整模式）

```
用户创建4阶段目录
    ↓
触发 content-creation-complete.md
    ↓
┌─────────────────────────────────────┐
│  完整模式流程控制                    │
├─────────────────────────────────────┤
│  Step 1: 引导 collect               │
│  Step 2: 引导 filter                │
│  Step 3: 引导 create                │
│  Step 4: 自动触发 checklist         │
│  Step 5: 自动触发 image marking     │
│  Step 6: 引导 publish               │
└─────────────────────────────────────┘
    ↓
产出高质量内容 + 发布准备材料
```

### 审查维度（content-post-checklist.md）

1. **事实准确性**：数据可验证、来源标注
2. **逻辑一致性**：前后论述不矛盾
3. **语言质量**：符合中文表达习惯
4. **平台适配**：符合平台风格要求
5. **结构完整性**：标题、引言、主体、总结
6. **原创性**：引用标注、独立思考

### 图片标记规范（content-image-marking.md）

**标准格式**：
```markdown
> [📷 图片X - 名称]
> **描述**：画面描述（50-150字）
> **位置**：具体位置说明
> **Prompt**：AI绘画提示词
```

**Prompt 必需元素**：
1. 场景描述（主体 + 动作 + 环境 + 情绪）
2. 中文文字（图片上需要显示的文字）
3. 宽高比（--ar X:Y）
4. 风格（--style xxx）
5. 版本（--v 6）

---

## 设计决策

### 为什么使用规则驱动架构？

**问题**：图片标记和审查清单需要自动触发，但不应让用户手动调用

**解决方案**：
- 使用 `.claude/rules/` 自动触发机制
- 规则文件监听特定条件，自动执行
- 用户无需感知规则的存在

**优势**：
- ✅ 零配置，自动生效
- ✅ 全模式覆盖（极简+完整）
- ✅ 质量保证不会遗漏
- ✅ 可扩展，新增规则无需修改核心流程

### 为什么不将三种模式都作为 rules？

**问题**：用户建议将极简模式、完整模式、talk_with_ai 都作为 rules

**为什么不这样做**：
1. **规则冲突**：多个规则同时激活会相互干扰
2. **控制复杂**：难以选择当前使用哪个模式
3. **职责混乱**：talk_with_ai 是对话记录，不需要自动化

**更好的方案**：
- CLAUDE.md 作为单一入口，提供决策树
- 完整模式通过规则触发（content-creation-complete.md）
- 极简模式直接使用 skill（更快）
- talk_with_ai 保持文档指导性质

### 为什么混合使用日期和版本号？

**规则**：
- 首次：`{YYYY-MM-DD}`
- 后续：`v2`, `v3`, `v4`...

**理由**：
- 日期更直观（首次创作）
- v2/v3 更简洁（后续版本）
- 便于识别最新版本

### 为什么采用4阶段目录结构？

**阶段**：
```
00_collect → 01_filter → 02_create → 03_publish
```

**理由**：
- ✅ 职责分离：每个阶段产出明确
- ✅ 可追溯：保留中间结果
- ✅ 可复用：filter 结果可用于多个平台
- ✅ 质量门禁：每个阶段可检查

---

## 文件编码规范

- 所有 `.md` 文件使用 **UTF-8** 编码（无 BOM）
- 所有 `.txt` 文件使用 **UTF-8** 编码（无 BOM）
- 所有 `.json` 文件使用 **UTF-8** 编码（无 BOM）

**Windows 用户**：确保编辑器保存为 UTF-8 without BOM

---

## 索引维护策略

**最佳努力维护**：

| 时机 | 操作 | 优先级 |
|------|------|--------|
| 创建新任务 | 添加条目 | 必须 |
| 完成任务 | 更新状态 | 必须 |
| 每周整理 | 优化结构 | 建议 |
| 修改内容 | 更新总结 | 可选 |

---

## 技术债务

| 债务项 | 优先级 | 计划 |
|--------|--------|------|
| 手动维护索引 | P1 | P2: 自动化脚本 |
| 评分权重重复定义 | P2 | P1: 单一数据源 |
| 文档与代码同步 | P1 | P1: 更新触发器 |
| Windows 路径限制 | P0 | P1: 路径检查工具 |

**详细路线图**: `@improvement-roadmap.md`

---

## 风险项

1. workspace 目录规范需要在现有技能中实现
2. 版本管理逻辑需要在各技能中集成
3. 目录创建可能受 Windows 路径限制影响

**Windows 路径解决方案**: 参见 `@improvement-roadmap.md`

---

## 相关文档索引

### 核心规范
- [README.md](README.md) - 用户指南（面向使用者）

### 详细指南
- `@complete-mode-guide.md` - 完整模式详细使用指南
- `@technical-architecture.md` - 技术架构详解
- `@directory-structure.md` - 目录结构详细规范
- `@platform-configs.md` - 平台详细配置

### 参考文档
- `@improvement-roadmap.md` - 改进路线图和技术债务
- `@faq.md` - 常见问题解答

### 规则文件
- `.claude/rules/content-creation-complete.md` - 完整模式流程控制
- `.claude/rules/content-post-checklist.md` - 创作后审查清单
- `.claude/rules/content-image-marking.md` - 图片标记指南

---

**文档维护**: 由 Claude AI 和用户共同维护
**反馈渠道**: 如有问题或建议，请更新本文档并记录版本变更
