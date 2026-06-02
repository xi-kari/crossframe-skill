# Workflow Routing Map

本文件规定 CrossFrame skill family 的连续触发规则。

## 核心链路

| 用户目标 | 默认工作流 | 说明 |
|---|---|---|
| 结构诊断 | `crossframe` | 事实、尺度、证据、机制候选、判断档位。 |
| 普通洞察文章 | `crossframe -> crossframe-essay -> crossframe-review` | 先诊断，再底稿，再正文，再评审。 |
| 公共评论文章 | `crossframe -> crossframe-public -> crossframe-essay -> crossframe-review` | 公共事实和证据边界必须在成文前完成。 |
| 组织复盘文章 | `crossframe -> crossframe-org -> crossframe-essay -> crossframe-review` | 先看责任链、授权链、反馈写回，再成文。 |
| 答读者问 | `crossframe -> crossframe-dialogue -> review-lite` | 短答复可以不输出完整评审报告。 |
| 编辑同志口吻长答 | `crossframe -> crossframe-dialogue -> crossframe-essay -> crossframe-review` | 先回信式判断，再扩成长文。 |
| 案例沉淀 | `crossframe -> crossframe-casebook -> crossframe-review` | 先明确事实边界，再沉淀案例。 |
| 案例后成文 | `crossframe -> crossframe-casebook -> crossframe-essay -> crossframe-review` | 案例是文章材料，不替代文章判断。 |
| 概念教学 | `crossframe -> crossframe-teach -> review-lite` | 教学要有人话解释、误读边界、练习。 |
| 命题辩论 | `crossframe -> crossframe-debate -> crossframe-review` | 先拆命题和证据要求，再评审。 |
| 辩论后成文 | `crossframe -> crossframe-debate -> crossframe-essay -> crossframe-review` | 论证完成后再写文章。 |
| 读书研究 | `crossframe -> crossframe-notebook -> crossframe-review` | 输出关联、不同、可吸收处、冲突处。 |
| 读书后成文 | `crossframe -> crossframe-notebook -> crossframe-essay -> crossframe-review` | 研究笔记先于文章。 |
| 只评审已有输出 | `crossframe-review` | 不强行重跑生成链。 |

## 触发信号

### 追加 `crossframe-public`

- 平台、政策、公共制度、公共承诺、申诉、封禁、处罚、合规、机构声明。
- 最新事实、真实人物、真实公司、真实组织、公共争议。
- 需要查源、证据边界、弱信号保护或反俘获。

### 追加 `crossframe-org`

- 团队、项目、复盘、流程、绩效、授权、责任、管理层、中层耗竭。
- 用户要备忘录、修复方案、反馈写回方案、低风险试点。

### 追加 `crossframe-debate`

- 用户说“辩论、反驳、论证、命题、正反方、隐藏前提、最强反方”。
- 文章中心命题争议较强，需要先压测。

### 追加 `crossframe-notebook`

- 读书、论文、理论、文章、摘录、文献、思想家、经典、关联与不同。
- 需要从外部文本中吸收或反证 CrossFrame。

### 追加 `crossframe-casebook`

- 聊天记录、项目材料、复盘材料、事件链、案例库、可复用案例。
- 用户要沉淀，而不是只要一次性答案。

### 追加 `crossframe-dialogue`

- 读者来信、编辑回信、短答复、咨询式回应、我该怎么看/怎么办。
- 用户明确要亲切、耐心、有意见但不长篇。

### 追加 `crossframe-teach`

- 教概念、讲给普通人、解释术语、做练习、误读纠偏。
- 用户问“这个概念到底什么意思”。

### 追加 `crossframe-essay`

- 写文章、长文、评论、随笔、思想文章、洞察文章、报刊答复体。
- 用户要求概念上升、引经据典、现代编辑同志口吻。

### 追加 `crossframe-review`

- 任何正式交付、长文、公共议题、强判断、组织修复、案例沉淀、命题结论。
- 用户要求审查、打分、验收、是否合格。

## 不读取规则

- 不要因为出现“公共”一词就读取全部公共协议；先判断是否涉及真实公共事实或制度责任。
- 不要因为文章需要漂亮就读取 `notebook`；只有需要外部文本、理论参照或读书比较时才读。
- 不要因为短答复要有温度就读取完整 `essay`；短答复默认用 `dialogue`。
- 不要把 `review` 输出给用户，除非用户要求评审报告或发现硬失败。
- 不要把所有 sibling skill 都列进“本次读取”，未读取的要写在“不读取”里。

## 工作流改写

用户已有部分产物时，可以跳过已完成环节，但必须声明来源：

- 用户给了完整诊断底稿：可从 `essay` 开始，但要做事实边界复核。
- 用户给了文章：可直接 `review`，必要时读取 `essay` 的规则。
- 用户给了证据材料：先 `public` 或 `casebook`，再决定是否 `essay`。
- 用户给了书摘：先 `notebook`，再决定是否 `essay` 或 `teach`。
