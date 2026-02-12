# 完整模式使用指南

**用途**: 本文档提供完整模式的详细使用说明，适合需要系统化管理内容的高级用户。

---

## 完整模式 vs 极简模式

| 特性 | 极简模式 | 完整模式 |
|------|---------|---------|
| 文件数量 | 1 个 | 多个（按阶段/平台） |
| 适用场景 | 单次创作、快速尝试 | 长期使用、版本管理 |
| 维护成本 | 低 | 中等 |
| 功能覆盖 | 基础功能 | 全部功能 |
| 升级难度 | - | 低（随时可升级） |

**何时选择完整模式**：
- 需要回顾历史创作
- 需要跨平台复用内容
- 团队协作需要标准化
- 长期使用（>10篇）

---

## 第一次使用：完整示例

假设你要创作关于"AI写作工具"的内容，发布到知乎和小红书：

### 步骤 1: 创建目录结构

```bash
# 创建主题文件夹
mkdir -p workspace/ai-tools/2026-01-27

# 创建阶段文件夹和平台子目录
mkdir -p workspace/ai-tools/2026-01-27/00_collect/zhihu
mkdir -p workspace/ai-tools/2026-01-27/00_collect/xiaohongshu
mkdir -p workspace/ai-tools/2026-01-27/01_filter/zhihu
mkdir -p workspace/ai-tools/2026-01-27/01_filter/xiaohongshu
mkdir -p workspace/ai-tools/2026-01-27/02_create/zhihu
mkdir -p workspace/ai-tools/2026-01-27/02_create/xiaohongshu
mkdir -p workspace/ai-tools/2026-01-27/03_publish
```

### 步骤 2: 收集资料

```bash
/zhihu-collect "AI写作工具"
/xiaohongshu-collect "AI写作工具"
```

输出：
- `workspace/ai-tools/2026-01-27/00_collect/zhihu/materials.md`
- `workspace/ai-tools/2026-01-27/00_collect/xiaohongshu/materials.md`

### 步骤 3: 筛选选题

```bash
/zhihu-filter
/xiaohongshu-filter
```

输出：
- `workspace/ai-tools/2026-01-27/01_filter/zhihu/scored_topics.md`
- `workspace/ai-tools/2026-01-27/01_filter/selected.md`

### 步骤 4: 创作内容

```bash
/zhihu-create "AI写作工具深度评测"
/xiaohongshu-create "AI写作工具推荐" --type 种草笔记
```

输出：
- `workspace/ai-tools/2026-01-27/02_create/zhihu/draft.md`
- `workspace/ai-tools/2026-01-27/02_create/xiaohongshu/draft.md`

### 步骤 5: 发布到草稿箱

```bash
/zhihu-publish
/xiaohongshu-publish
```

输出：
- `workspace/ai-tools/2026-01-27/03_publish/zhihu/log.md`
- `workspace/ai-tools/2026-01-27/03_publish/report.md`

### 步骤 6: 更新索引

编辑 `workspace/index.md`，添加：
```markdown
| AI写作工具 | v1 | 2026-01-27 | 知乎、小红书 | 已完成 | 深度评测+工具推荐 | ai-tools | [查看](ai-tools/2026-01-27/) |
```

---

## 版本管理

### 版本命名规则

**首次创作**：使用日期 `{YYYY-MM-DD}`
```
workspace/ai-tools/2026-01-27/
```

**后续创作**：使用递增版本 `v2`, `v3`, `v4`...
```
workspace/ai-tools/
├── 2026-01-27/    # 首次（日期版本）
├── v2/            # 第二次（递增版本）
└── v3/            # 第三次
```

**同一天多次创作**：添加序号
```
workspace/ai-tools/
├── 2026-01-27/    # 第一次
├── 2026-01-27-a/  # 第二次（同一天）
└── 2026-01-27-b/  # 第三次（同一天）
```

### 版本升级工作流

**极简模式 → 完整模式**：
```bash
# 1. 重命名现有文件
mv workspace/ai-tools/content.md workspace/ai-tools/temp.md

# 2. 创建完整目录结构
mkdir -p workspace/ai-tools/v1/{00_collect,01_filter,02_create,03_publish}

# 3. 移动内容到对应位置
mv workspace/ai-tools/temp.md workspace/ai-tools/v1/02_create/final.md

# 4. 创建其他必要文件（如 task.md）
```

---

## task.md 模板

每个版本目录下应包含 `task.md` 作为导航文件：

```markdown
# {主题名称} - {版本}

**创建日期**: {YYYY-MM-DD}
**状态**: {进行中/已完成/已发布}
**涉及平台**: {平台列表}

## 快速导航

- [收集阶段](00_collect/summary.md) - 资料收集汇总
- [筛选阶段](01_filter/selected.md) - 入选选题
- [创作阶段](02_create/meta.md) - 创作元数据
- [发布阶段](03_publish/report.md) - 发布报告

## 内容关系

### 平台间内容关系
- 知乎：{描述}
- 小红书：{基于知乎内容，简化为工具推荐}
- 领英：{提取商业洞察}
- X: {提炼核心观点}

## 备注

{任何需要记录的备注信息}
```

---

## 跨平台内容复用

### 场景：同一内容多平台适配

```
用户需求: "创作一篇关于 AI 工具的文章，发布到知乎和领英"

推荐流程：
1. 先在知乎创作（专业深度）
2. 基于知乎内容，改编为领英版本（商业导向）

workspace/
└── ai-tools/
    └── 2026-01-27/
        ├── 02_create/
        │   ├── zhihu/
        │   │   ├── draft.md    # 主版本：专业详细
        │   │   └── final.md
        │   └── linkedin/
        │       ├── draft.md    # 衍生版本：商业导向
        │       └── final.md
        └── task.md             # 记录内容改编关系
```

### task.md 中的内容关系记录

```markdown
## 内容关系

- 主版本：知乎（专业详细，2000字）
- 衍生版本：
  - 领英：提取商业洞察，强调价值（800字）
  - 小红书：简化为工具推荐，添加emoji（500字）
  - X: 提炼核心观点，制作线程（3条推文）
```

---

## 索引维护

### 何时必须更新

- ✅ **创建新任务时**：添加条目到索引表格
- ✅ **完成任务时**：更新状态为"已完成"
- 🔄 **建议每周整理**：清理旧任务，更新统计

### workspace/index.md 完整模板

```markdown
# 创作任务索引

最后更新：{YYYY-MM-DD HH:MM}

## 创作任务列表

| 主题 | 版本 | 日期 | 平台 | 状态 | 两句话总结 | 标签 | 路径 |
|------|------|------|------|------|-----------|------|------|
| AI写作工具 | v1 | 2026-01-27 | 知乎、小红书 | 已完成 | 深度评测知乎版，工具推荐小红书版 | ai,tools | [查看](ai-tools/2026-01-27/) |
| Python入门 | v1 | 2026-01-26 | 知乎 | 进行中 | 面向零基础，包含实战案例 | python,learn | [查看](python-intro/2026-01-26/) |

## 统计信息

- 总创作任务：2
- 涉及主题：2 个
- 完成状态：已完成 1，进行中 1，待开始 0
- 最近更新：2026-01-27

## 按平台查看

> 注意：以下链接需要手动筛选

- [知乎任务](#) (待实现)
- [小红书任务](#) (待实现)
- [领英任务](#) (待实现)
- [X任务](#) (待实现)

## 按状态查看

- [已完成](#)
- [进行中](#)
- [待开始](#)
```

---

## 目录命名规范

- **topic_name**: 使用英文或拼音，小写，连字符分隔空格
  - ✅ `ai-writing-tools`, `python-tutorial`
  - ❌ `AI写作工具`, `Python Tutorial`

- **platform**: 平台标识
  - `x` - X (Twitter)
  - `zhihu` - 知乎
  - `xiaohongshu` - 小红书
  - `linkedin` - 领英

- **阶段前缀**: 保持排序
  - `00_collect` - 收集阶段
  - `01_filter` - 筛选阶段
  - `02_create` - 创作阶段
  - `03_publish` - 发布阶段

---

## 文件编码规范

- 所有 `.md` 文件使用 **UTF-8** 编码（无 BOM）
- 所有 `.txt` 文件使用 **UTF-8** 编码（无 BOM）
- 所有 `.json` 文件使用 **UTF-8** 编码（无 BOM）

**Windows 用户**：确保编辑器保存为 UTF-8 without BOM
- VS Code: 右下角显示 "UTF-8"
- Notepad++: 编码 → 转为 UTF-8 无 BOM

---

**相关文档**:
- @directory-structure.md - 完整目录结构说明
- @platform-configs.md - 平台详细配置
- @faq.md - 常见问题
