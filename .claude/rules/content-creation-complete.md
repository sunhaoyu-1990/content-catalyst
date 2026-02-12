# 内容创作完整模式规则

**版本**: v1.0
**触发条件**: 用户在 `workspace/{topic}/` 下创建文章，且目录结构符合完整模式

---

## 规则目的

当用户按照完整模式创作内容时（4阶段目录结构），本rule确保：
1. 正确遵循 00_collect → 01_filter → 02_create → 03_publish 流程
2. 每个阶段产出符合规范
3. 自动触发后续处理步骤

## 触发检测

**当以下条件满足时，启用完整模式流程**：
- 文件路径包含 `workspace/{topic}/{version}/00_collect/` 或类似4阶段结构
- 用户明确表示"按照完整模式"或"遵循CLAUDE.md完整模式指南"

## 必须步骤（按顺序）

### 第1步：收集阶段 (00_collect)
- 使用 `{platform}-collect` skill 收集资料
- 产出：`materials.md` 或 `research.md`
- 内容：收集到的原始资料、链接、关键信息

### 第2步：筛选阶段 (01_filter)
- 使用 `{platform}-filter` skill 筛选选题
- 产出：`selection.md` 或 `topics.md`
- 内容：评分结果、入选选题、理由说明

### 第3步：创作阶段 (02_create)
- 使用 `{platform}-create` skill 创作内容
- 产出：`{platform}/article.md`
- 内容：完整文章内容

### 第4步：自动触发审查和标记
**创作完成后，自动按顺序触发**：
1. `content-post-checklist.md` - 创作后审查清单
2. `content-image-marking.md` - 图片标记指南

### 第5步：发布准备 (03_publish)
- 使用 `{platform}-publish` skill 生成发布指南
- 产出：`publish-guide.md`
- 内容：发布建议、配图说明、推广策略

## 质量门禁

**每个阶段完成后检查**：
- [ ] 产出文件存在且非空
- [ ] 内容符合该阶段规范
- [ ] 文件编码为 UTF-8（无BOM）
- [ ] 下一阶段的输入准备就绪

## 异常处理

| 场景 | 处理方法 |
|------|---------|
| 收集为空 | 降低搜索阈值，更换关键词，手动补充资料 |
| 筛选无结果 | 降低评分阈值，调整权重，手动指定选题 |
| 创作失败 | 检查用户画像，提供更详细说明 |
| 审查不通过 | 根据审查清单修改，直到通过 |

## 完成标志

**当以下文件全部存在时，完整模式流程完成**：
```
workspace/{topic}/{version}/
├── 00_collect/{materials,research}.md  ✅
├── 01_filter/{selection,topics}.md     ✅
├── 02_create/{platform}/article.md     ✅
└── 03_publish/{platform}/publish-guide.md ✅
```

---

**注意事项**：
1. 本rule不替代skill，而是确保skill按正确顺序使用
2. 极简模式（单文件创作）不触发本rule
3. 触发本rule后，同时触发 `content-post-checklist.md` 和 `content-image-marking.md`
