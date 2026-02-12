# 目录结构详细规范

**用途**: 本文档详细说明 workspace/ 和 talk_with_ai/ 的完整目录结构。

---

## workspace/ 目录结构

### 完整结构图

```
workspace/                                    # 创作文件夹（项目根目录下）
├── index.md                                  # 索引文档（最外层，必选）
│
├── {topic_name}/                             # 主题文件夹
│   ├── {YYYY-MM-DD}/                         # 版本：首次创作（日期）
│   │   ├── 00_collect/                       # Collect 阶段产出
│   │   │   ├── {platform}/                   # 各平台资料收集
│   │   │   │   ├── materials.md              # 收集报告
│   │   │   │   └── sources.json              # 数据源记录
│   │   │   └── summary.md                    # 跨平台汇总
│   │   │
│   │   ├── 01_filter/                        # Filter 阶段产出
│   │   │   ├── {platform}/
│   │   │   │   └── scored_topics.md          # 评分选题列表
│   │   │   └── selected.md                   # 入选选题汇总
│   │   │
│   │   ├── 02_create/                        # Create 阶段产出
│   │   │   ├── {platform}/
│   │   │   │   ├── draft.md                  # 创作草稿
│   │   │   │   └── final.md                  # 最终内容
│   │   │   └── meta.md                       # 元数据
│   │   │
│   │   ├── 03_publish/                       # Publish 阶段产出
│   │   │   ├── {platform}/
│   │   │   │   └── log.md                    # 发布状态
│   │   │   └── report.md                     # 发布汇总
│   │   │
│   │   └── task.md                           # 任务导航
│   │
│   ├── v2/                                   # 版本2（递增版本）
│   │   └── ... (结构同上)
│   │
│   └── v3/                                   # 版本3
│       └── ... (结构同上)
│
└── {another_topic}/                          # 另一个主题
    └── ...
```

### 目录用途说明

#### 00_collect/ - 收集阶段

**用途**: 存放资料收集阶段的产出

**文件说明**:
- `materials.md`: 收集的资料报告
- `sources.json`: 数据源记录（URL、标题、时间）
- `summary.md`: 跨平台汇总，提炼关键信息

**示例**:
```markdown
## materials.md

# AI写作工具 - 资料收集

**收集时间**: 2026-01-27
**收集轮次**: 4 轮

### 收集到的资料
1. ChatGPT - OpenAI 的大型语言模型
2. Claude - Anthropic 的 AI 助手
3. ...

### 关键发现
- 市场上主流工具约 10 款
- 主要分为写作辅助和内容生成两类
```

#### 01_filter/ - 筛选阶段

**用途**: 存放选题评分和筛选结果

**文件说明**:
- `scored_topics.md`: 按评分排序的选题列表
- `selected.md`: 最终入选的选题

**示例**:
```markdown
## scored_topics.md

| 选题 | 专业性 | 可信度 | 热度 | 相关性 | 总分 | 入选 |
|------|--------|--------|------|--------|------|------|
| AI写作工具评测 | 4 | 3 | 4 | 3 | 14 | ✅ |
| 如何用AI写作 | 3 | 3 | 3 | 3 | 12 | ✅ |
| AI写作的未来 | 2 | 2 | 2 | 2 | 8 | ❌ |
```

#### 02_create/ - 创作阶段

**用途**: 存放内容创作阶段的产出

**文件说明**:
- `draft.md`: 创作草稿（可能有多版）
- `final.md`: 最终确定的内容
- `meta.md`: 元数据（时间、平台、标签等）

**示例**:
```markdown
## meta.md

# 内容元数据

**标题**: AI写作工具深度评测
**平台**: 知乎
**创作时间**: 2026-01-27 14:30
**字数**: 2500 字
**标签**: AI, 写作工具, 评测, ChatGPT, Claude

**内容类型**: 专业回答
**目标受众**: 内容创作者、职场人士

**基于选题**: AI写作工具评测 (14分)
```

#### 03_publish/ - 发布阶段

**用途**: 存放发布记录和状态

**文件说明**:
- `log.md`: 发布日志（时间、状态、截图等）
- `report.md`: 发布汇总报告

**示例**:
```markdown
## log.md

# 发布日志

**发布时间**: 2026-01-27 16:00
**发布方式**: 自动化（Playwright）
**发布状态**: ✅ 成功

**发布链接**: https://zhuanlan.zhihu.com/p/xxxxx

**备注**:
- 成功发布到知乎专栏
- 首小时获得 50 阅读
```

#### task.md - 任务导航

**用途**: 版本级别的导航和概览

**模板**: 参见 @complete-mode-guide.md 中的 task.md 模板

---

## talk_with_ai/ 目录结构

### 完整结构图

```
talk_with_ai/                                 # AI对话文件夹（项目根目录下）
├── index.md                                  # 索引文件
│
├── {topic_name}/                             # 主题文件夹
│   ├── {YYYY-MM-DD}/                         # 版本：首次对话（日期）
│   │   ├── conversation.md                   # 对话记录（完整转录）
│   │   ├── summary.md                        # 对话总结（核心要点）
│   │   ├── insights.md                       # 关键洞察/结论
│   │   ├── actions.md                        # 行动项/待办事项
│   │   ├── tags.txt                          # 标签（一行一个）
│   │   └── related/                          # 相关资料引用
│   │       ├── {reference_name}.md           # 引用文档
│   │       └── ...
│   │
│   ├── v2/                                   # 版本2
│   │   └── ... (结构同上)
│   │
│   └── v3/                                   # 版本3
│       └── ... (结构同上)
│
└── {another_topic}/                          # 另一个主题
    └── ...
```

### 文件说明

#### conversation.md - 对话记录

**用途**: 完整的对话转录

**格式**:
```markdown
# 对话记录

**时间**: 2026-01-27 10:00 - 11:30
**主题**: prompt 优化策略
**参与者**: User, Claude

## 对话内容

### User (10:00)
如何优化 prompt 以获得更好的输出质量？

### Claude (10:01)
优化 prompt 的几个关键策略...

### User (10:05)
那如何平衡详细指令和简洁性呢？

...
```

#### summary.md - 对话总结

**用途**: 对话的核心要点总结

**格式**:
```markdown
# 对话总结

**主题**: prompt 优化策略
**时间**: 2026-01-27
**对话轮次**: 15 轮

## 核心要点

1. **明确指令**: 使用具体、可操作的指令
2. **提供上下文**: 给出足够的背景信息
3. **分步思考**: 引导模型逐步推理

## 关键结论

- 好的 prompt 需要 3 个要素：明确性、上下文、示例
- 过于详细的指令可能限制模型创造力
- 迭代优化比一次到位更有效

## 下一步

- 实践新的 prompt 策略
- 收集效果数据
- 下次对话时分享结果
```

#### insights.md - 关键洞察

**用途**: 对话中的关键洞察和启示

**格式**:
```markdown
# 关键洞察

## 洞察 1: Prompt 是编程的自然语言版本

就像写代码需要清晰的逻辑，写 prompt 也需要结构化思维。

## 洞察 2: 迭代优于完美

与其花 1 小时写完美 prompt，不如用 10 分钟写 6 个版本并测试。

## 洞察 3: 上下文是关键

没有上下文的指令就像没有参数的函数，模型不知道如何执行。
```

#### actions.md - 行动项

**用途**: 对话后的待办事项

**格式**:
```markdown
# 行动项

## 待办

- [ ] 重构现有的 5 个常用 prompt
- [ ] 创建 prompt 模板库
- [ ] 测试新的优化策略
- [ ] 记录效果数据

## 进行中

- [x] 学习 prompt 工程基础

## 已完成

- [x] 与 Claude 讨论 prompt 优化
```

#### tags.txt - 标签

**用途**: 便于分类和检索

**格式**:
```
prompt-engineering
workflow-optimization
ai-interaction
content-creation
```

**规范**:
- 每行一个标签
- 小写英文，连字符分隔
- 使用具体、有意义的词汇
- 3-7 个标签为宜

#### related/ - 相关资料

**用途**: 引用的文档、图片、链接等

**示例**:
```
related/
├── openai-prompt-guide.md     # 引用的 OpenAI 文档
├── prompt-examples.md         # 收集的示例
└── best-practices.md          # 最佳实践
```

---

## talk_with_ai/index.md 模板

```markdown
# AI对话索引

最后更新：{YYYY-MM-DD HH:MM}

## 对话列表

| 主题 | 版本 | 日期 | 两句话总结 | 标签 | 路径 |
|------|------|------|-----------|------|------|
| prompt优化 | v1 | 2026-01-27 | 探讨了prompt优化的核心策略，决定采用迭代方法 | prompt,ai | [查看](prompt-optimization/2026-01-27/) |
| 内容策略 | v2 | 2026-01-28 | 深入分析了多平台内容适配，得出差异化结论 | strategy,content | [查看](content-strategy/v2/) |

## 统计信息

- 总对话次数：2
- 涉及主题：2 个
- 最近更新：2026-01-28

## 按标签查看

- [prompt-engineering](#)
- [content-strategy](#)
- [ai-interaction](#)
```

---

## 命名规范总结

### 主题命名
- ✅ `ai-writing-tools`
- ✅ `python-tutorial`
- ✅ `content-strategy`
- ❌ `AI写作工具`
- ❌ `Python Tutorial`

### 版本命名
- 首次: `{YYYY-MM-DD}`
- 后续: `v2`, `v3`, `v4`
- 同一天多次: `{YYYY-MM-DD}-a`, `{YYYY-MM-DD}-b`

### 平台命名
- `x` - X (Twitter)
- `zhihu` - 知乎
- `xiaohongshu` - 小红书
- `linkedin` - 领英

### 阶段命名
- `00_collect` - 收集阶段
- `01_filter` - 筛选阶段
- `02_create` - 创作阶段
- `03_publish` - 发布阶段

---

## Windows 路径限制注意事项

**问题**: Windows 路径长度限制为 260 字符

**解决方案**:
1. 主题名称 ≤ 30 字符
2. 完整路径 ≤ 200 字符（留 60 字符余量）
3. 避免特殊字符：`< > : " | ? *`
4. 使用连字符 `-` 代替空格

**路径长度估算**:
```
D:\BaiduSyncdisk\ai_work_record\workspace\very-long-topic-name\2026-01-27\00_collect\zhihu\materials.md
└────────────────────────────────────── ~100 字符 ───────────────────────────────────┘
```

**详细指南**: 参见 @improvement-roadmap.md 中的 Windows 路径检查清单

---

**相关文档**:
- @complete-mode-guide.md - 完整模式使用指南
- @faq.md - 常见问题
