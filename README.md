# Skills Repo 工作台

这个仓库用于管理、调用和扩展 ChatGPT / Codex skills。它不是“越多越好”的 skill 收藏夹，而是一个个人工作流工作台：你可以在这里查看已有 skills、安装推荐组合、记录调用模板、添加新 skill，并检查配置是否健康。

## 快速开始

### 查看已有 skills

```bash
python scripts/skills-manager.py list
```

你会看到每个 skill 的名称、分类、是否启用、优先级、是否需要联网。

### 安装推荐 skills

```bash
./install-recommended.sh
```

安装后重启 Codex，让新 skills 生效。脚本会在最后自动运行一次健康检查。

### 调用一个 skill

在 ChatGPT 或 Codex 里直接说明你要使用哪个 skill 和目标。例如：

```text
使用 baoyu-diagram，把下面的大创项目执行流程画成 Mermaid 流程图，并标出每个阶段的输入、输出和负责人：……
```

在 Codex 中，如果该 skill 已安装并匹配任务，它会读取对应 `SKILL.md` 并按工作流执行。ChatGPT 不能直接读取你的本地 skills 目录，但可以复用这里的提示词模板和规则。

### 添加新 skill

```bash
python scripts/skills-manager.py add <name> <path-or-url>
```

例子：

```bash
python scripts/skills-manager.py add academic-writing https://github.com/example/academic-writing-skill
```

添加后请打开 `skills-inventory.json` 补全描述、分类、调用示例、依赖和冲突信息。

### 检查 repo 是否配置正确

```bash
python scripts/skills-manager.py doctor
```

如果看到 `[ERROR]`，先修复再继续使用；如果只有 `[WARN]`，通常可以继续，但要留意提示。

## 常用调用模板

1. Markdown / Obsidian 笔记整理

```text
使用 baoyu-format-markdown，帮我把以下内容整理成 Obsidian 笔记，要求保留 H1/H2/H3 层级、公式、英文术语和复习问题：……
```

2. 学术论文结构优化

```text
使用 writing-localization 方向的 skill，帮我优化下面这篇学术论文草稿结构，要求保留原始论点，不虚构引用，输出 Markdown 大纲和修改建议：……
```

3. 商赛报告撰写

```text
使用 baoyu-format-markdown，帮我把以下商业计划材料整理成商赛报告结构，包含市场痛点、解决方案、商业模式、竞品分析、财务假设和风险控制：……
```

4. PPT 大纲生成

```text
使用 Presentations 能力，帮我把下面的项目材料整理成 10 页 PPT 大纲，每页给出标题、核心观点、证明材料和建议图表：……
```

5. 流程图 / 架构图生成

```text
使用 baoyu-diagram，把下面的系统流程画成架构图，要求先列出节点、关系和数据流，再输出 SVG 或 Mermaid：……
```

6. 前端页面设计

```text
使用 web-design-guidelines 和 vercel-react-best-practices，帮我设计一个 React 页面，要求说明信息架构、组件拆分、可访问性和性能注意事项：……
```

7. 简历优化

```text
使用 baoyu-format-markdown，帮我优化下面的简历内容，要求突出项目结果、量化贡献、保留真实经历，并输出 Markdown 和一版 ATS 友好版本：……
```

8. 翻译与本地化

```text
使用 baoyu-translate，把以下英文内容本地化为中文，目标读者是技术产品经理，要求保留专业术语、补充必要译注，不要直译腔：……
```

9. 文档排版

```text
使用 baoyu-format-markdown，帮我把以下会议记录整理成正式文档，要求包含背景、决策、行动项、负责人、截止时间和待确认问题：……
```

10. 项目管理

```text
使用 baoyu-diagram 和 baoyu-format-markdown，帮我把下面的项目计划整理成里程碑表、风险清单和执行流程图：……
```

11. 信息图生成

```text
使用 baoyu-infographic，把下面的研究结论做成一张高密度信息图，先推荐 layout 和 style，再生成可发布版本：……
```

12. 文章封面生成

```text
使用 baoyu-cover-image，为下面这篇文章生成封面图，要求科技感、中文标题清晰、16:9、不要使用品牌 logo：……
```

## 任务选择表

| 用户想做什么 | 推荐 skill | 输出形式 | 注意事项 |
| --- | --- | --- | --- |
| 整理 Obsidian 笔记 | `baoyu-format-markdown` | Markdown | 说明是否保留原文、是否生成复习问题 |
| 做流程图 | `baoyu-diagram` | Mermaid / SVG | 先明确节点、关系、方向和边界 |
| 画系统架构图 | `baoyu-diagram` | SVG | 不要用不明含义的箭头；标出数据流 |
| 写学术文章 | `writing-localization` / custom academic skill | Markdown / DOCX | 避免凭空引用，引用需要来源 |
| 商赛报告 | `baoyu-format-markdown` | Markdown / PPT 大纲 | 先给评分标准和页数 |
| 做前端页面 | `web-design-guidelines` + `vercel-react-best-practices` | React / HTML | 明确技术栈、设备尺寸和交互状态 |
| React 性能优化 | `vercel-react-best-practices` | 代码建议 / patch | 重点检查数据瀑布、bundle、重渲染 |
| UI/UX 审查 | `web-design-guidelines` | 审查清单 | 该 skill 使用最新 Web 规范，需要联网 |
| 翻译文章 | `baoyu-translate` | Markdown | 首次使用需要配置 `EXTEND.md` |
| 文档排版 | `baoyu-format-markdown` | Markdown | 默认不改写原意，只整理结构 |
| 生成封面图 | `baoyu-cover-image` | PNG / JPG | 调用前确认风格、比例、文字层级 |
| 生成信息图 | `baoyu-infographic` | PNG / JPG | 信息必须足够结构化，避免塞太多字 |
| 生成 PPTX | 平台 Presentations 插件 | PPTX / PNG 预览 | 如果平台能直接导出 PPTX，优先用内置工具 |
| 生成 DOCX | 平台 Documents 插件 | DOCX / PDF 预览 | 优先用内置工具，不重复安装 docx skill |
| 生成 XLSX | 平台 Spreadsheets 插件 | XLSX / CSV | 公式、表格和图表优先用内置工具 |

## Skills 管理命令

```bash
python scripts/skills-manager.py list
python scripts/skills-manager.py add <name> <path-or-url>
python scripts/skills-manager.py remove <name>
python scripts/skills-manager.py enable <name>
python scripts/skills-manager.py disable <name>
python scripts/skills-manager.py update <name|all>
python scripts/skills-manager.py doctor
```

这些命令只管理 `skills-inventory.json`。它们不会删除你电脑里的真实 skill 文件，也不会自动联网更新 skill 源码。

## 冲突与优先级规则

- 如果平台内置工具能直接生成 DOCX / PPTX / PDF，优先使用内置工具。
- 如果任务是结构化写作、格式规范、领域模板，优先使用 skill。
- 如果多个 skill 都能完成任务，优先选择更具体的 skill。
- 不要重复安装与插件功能完全重叠的 skill，例如已有 Presentations、Documents、Spreadsheets 插件时，不要再装泛用 `pptx`、`docx`、`xlsx` skill。
- 对需要联网、API Key、首次配置的 skill，在调用前先提示用户。
- 如果一个 skill 的 `blocking_steps` 非空，即使 `enabled=true`，也要先完成阻塞步骤。
- 如果两个已启用 skills 在 `conflicts` 中互相冲突，优先保留更具体、优先级更高的那个。

## 新增 skill 的规范

每个 skill 至少要在 `skills-inventory.json` 中包含：

- `name`
- `description`
- `category`
- `path`
- `enabled`
- `priority`
- `use_cases`
- `invocation_examples`
- `dependencies`
- `needs_network`
- `blocking_steps`
- `conflicts`
- `last_updated`

建议分类使用：

- `frontend-design-engineering`
- `content-visuals`
- `diagrams`
- `writing-localization`
- `documents-presentations-sheets`
- `research`
- `project-management`
- `custom`

## 当前推荐组合

- 前端设计与工程质量：`web-design-guidelines`、`vercel-react-best-practices`
- 内容视觉生成：`baoyu-cover-image`、`baoyu-infographic`
- 图解与技术可视化：`baoyu-diagram`
- 写作、翻译与整理：`baoyu-translate`、`baoyu-format-markdown`

配置文件：

- `skills-inventory.json`
- `templates/EXTEND.md.example`

