# Codex Skills Catalog

本仓库是当前 Codex 本地 skills 的确认稿，用来检查安装结果、功能分类和后续取舍。

## 安装状态

已确认安装在 `/Users/chenxinyu/.codex/skills` 的个人 skills：

| Skill | 分类 | 状态 | 主要用途 | 本地路径 |
| --- | --- | --- | --- | --- |
| `web-design-guidelines` | 前端设计审查 | 已安装 | UI/UX、可访问性、Web 界面规范审查 | `/Users/chenxinyu/.codex/skills/web-design-guidelines` |
| `vercel-react-best-practices` | React/Next.js 工程 | 已安装 | React/Next.js 性能、数据获取、包体积、渲染优化 | `/Users/chenxinyu/.codex/skills/vercel-react-best-practices` |
| `baoyu-cover-image` | 内容视觉生成 | 已安装 | 文章封面图生成，支持类型、色板、渲染、文本、情绪五维控制 | `/Users/chenxinyu/.codex/skills/baoyu-cover-image` |
| `baoyu-infographic` | 内容视觉生成 | 已安装 | 高密度信息图、视觉总结、信息可视化 | `/Users/chenxinyu/.codex/skills/baoyu-infographic` |
| `baoyu-diagram` | 图解与技术可视化 | 已安装 | 架构图、流程图、时序图、状态机、概念图，输出 SVG | `/Users/chenxinyu/.codex/skills/baoyu-diagram` |
| `baoyu-translate` | 写作与本地化 | 已安装 | 文章、文档翻译，支持 quick、normal、refined 三种模式 | `/Users/chenxinyu/.codex/skills/baoyu-translate` |
| `baoyu-format-markdown` | 写作与整理 | 已安装 | Markdown / 纯文本排版、标题、摘要、结构整理 | `/Users/chenxinyu/.codex/skills/baoyu-format-markdown` |

系统内置 skills 已存在，不纳入个人安装仓库：

| Skill | 用途 |
| --- | --- |
| `imagegen` | 原生图片生成与编辑 |
| `openai-docs` | OpenAI 官方文档查询 |
| `plugin-creator` | 创建 Codex 插件 |
| `skill-creator` | 创建 / 更新 Codex skill |
| `skill-installer` | 安装 skill |

插件提供的能力也已存在，不建议重复安装为个人 skill：

| 插件能力 | 对应用途 |
| --- | --- |
| Browser / Chrome | 浏览器自动化 |
| Figma | Figma 设计、设计系统、Code Connect |
| GitHub | PR、Issue、CI、发布草稿 PR |
| Presentations | PPTX / deck |
| Documents | DOCX |
| Spreadsheets | XLSX / CSV |

## 推荐分组

### 1. 前端设计与工程质量

适合前端项目开发、审查、性能优化。

- `web-design-guidelines`
- `vercel-react-best-practices`

查看：[categories/frontend-design-engineering.md](categories/frontend-design-engineering.md)

### 2. 内容视觉生成

适合文章、知识内容、营销材料、社媒图和视觉解释。

- `baoyu-cover-image`
- `baoyu-infographic`

查看：[categories/content-visuals.md](categories/content-visuals.md)

### 3. 图解与技术可视化

适合架构解释、流程讲解、系统关系表达。

- `baoyu-diagram`

查看：[categories/diagrams.md](categories/diagrams.md)

### 4. 写作、翻译与整理

适合内容生产、双语发布、文档打磨。

- `baoyu-translate`
- `baoyu-format-markdown`

查看：[categories/writing-localization.md](categories/writing-localization.md)

## 使用建议

日常默认启用这 7 个即可。暂时不建议再加入 `UI-UX-PRO-MAX` 一类大而全的设计 skill，除非你明确想要一个独立的设计系统生成器；否则会和现有前端设计规则、Codex 自带前端规范发生风格重叠。

## 待确认

- 是否把这个目录升级成真正的 Git 仓库。
- 是否复制完整 skill 内容到仓库中，还是只保留安装清单和分类说明。
- 是否加入 `baoyu-markdown-to-html`、`baoyu-xhs-images`、`baoyu-slide-deck` 等更多内容发布类 skills。
- 是否为 `baoyu-translate` 创建默认 `EXTEND.md` 偏好，例如目标语言、翻译模式、术语表。

