# Workflow Routing Map

本文件规定 CrossFrame skill family 的连续触发规则。

## 核心链路

| 用户目标 | 默认工作流 | 说明 |
|---|---|---|
| 结构诊断 | `crossframe` | 事实、尺度、证据、机制候选、判断档位。 |
| 开放式可读分析 | `crossframe -> crossframe-essay(full-visible-v3-longform, editorial-base) -> crossframe-review` | 用户只说分析、怎么看、讲讲、写一下且未指定格式时，默认输出完整可见底稿 + 完整长文正文。 |
| 普通洞察文章 | `crossframe -> crossframe-essay(full-visible-v3-longform, editorial-base) -> crossframe-review` | 先诊断，再完整底稿，再长文正文，再评审；默认不是短答或冷诊断腔。 |
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

## 默认成文规则

当 `crossframe-suite` 被触发，且用户没有指定非文章交付物时，默认把最终输出做成 `full-visible-v3-longform`：3.0 混合长文，包含完整可见底稿和完整长文正文。典型信号：

- “分析一下这个问题”
- “你怎么看”
- “讲讲这个现象”
- “写一下这个主题”
- “给我一个有洞察力的回答”
- “我想看一个能给别人读的输出”

此时默认链路是：

```text
crossframe -> source-continuity-check -> crossframe-essay(full-visible-v3-longform, editorial-base) -> crossframe-review
```

`source-continuity-check` 不是独立 skill，而是 `crossframe` 内部的连续联读检查：读取 `continuity-bundles.md`，必要时读取 `v3-source-spine.md`、`v3-section-digest-index.md` 和 `v3-term-fidelity.md`。v2 文件只在需要历史版本对照时读取。

`editorial-base` 表示自动成文默认启用 `crossframe-essay` 的现代编辑底色：先接住问题，再共同分析结构，必要时严厉批评不当做法，最后给出清醒、有分寸的意见。问题型主题用答复体；公共评论、思想文章、概念文章用评论体。只有用户明确要求中性报告、备忘录、表格、清单、纯诊断或学术摘要时，才关闭这一声口。

`full-visible-v3-longform` 表示底稿完整可见，至少展示对象、事实边界、尺度窗口、机制候选、v3 连续联读包、源结构保真、概念风险、反向条件、声口方案和文章转译方案；正文默认 1200-2200 中文字，有标题、铺陈、概念上升、经典/理论参照或思想映射、现实回落、边界段和余味结尾。

不要擅自成文的信号：

- “评审/审查/打分/是否合格”
- “整理成案例库/来源台账/脱敏材料”
- “给组织修复备忘录/反馈写回方案/低风险试点”
- “列正反方/命题论证/隐藏前提”
- “讲概念并出练习”
- “只要一句话/只要表格/只要清单/只要下一步行动”

这些任务要保留原交付物，而不是转成文章。

## 触发信号

### 追加 `crossframe-public`

- 平台、政策、公共制度、公共承诺、申诉、封禁、处罚、合规、机构声明。
- 最新事实、真实人物、真实公司、真实组织、公共争议。
- 需要查源、证据边界、弱信号保护或反俘获。
- 涉及 AI 合规文本、机构自评、恶意合规、可见性偏误或开放断言被处置化时，必须追加 v3.0 证据可见性包和权力捕获包。

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

### 追加 v3.0 源连续性保护

- 框架是否失效、是否应降级/转接/退场：触发 `v3-framework-governance-falsification-pack`。
- 共识程序、强判断、开放断言被长期引用：触发 `v3-procedural-judgment-pack`。
- 沉默、缺席、不透明、弱信号、AI 缺失材料：触发 `v3-evidence-visibility-pack`。
- 家庭、小团队、非正式关系中没有制度却风险持续：触发 `v3-no-institution-middle-path-pack`。
- 无法退出、复杂创伤、无健康基准：触发 `v3-trapped-trauma-baseline-pack`。
- 引经据典、隐喻、知识谱系、规范性前提：触发 `v3-concept-migration-metaphor-pack`。
- 课程、咨询、AI 工具、认证、商业化：触发 `v3-toolization-accessibility-pack`。
- 高反身追踪、阶段 6、熵增、必须停止观察：触发 `v3-observation-entropy-contraction-pack`。
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
- suite 默认成文也追加，并默认传入 `editorial-base` 声口要求；不要等用户再次说“请用编辑口吻”。
- suite 默认成文必须同时传入 `full-visible-v3-longform` 输出档位；不要把开放式分析压缩成短答。

### 追加 `crossframe-review`

- 任何正式交付、长文、公共议题、强判断、组织修复、案例沉淀、命题结论。
- 用户要求审查、打分、验收、是否合格。

### 追加连续联读包

- 文章、评论、思想文章：至少触发 `diagnosis-mainline-pack` 与 `expression-article-pack`。
- 开放断言、强判断、高责任：触发 `judgment-responsibility-pack`。
- 公共议题、平台治理、合规材料：触发 `public-power-governance-pack`，并视情况触发 `framework-use-discipline-pack`。
- 亲密关系、解释劳动、爱、照护、疗愈：触发 `intimate-love-care-pack`。
- 生命周期、递进、势场、自主解离、治理连续性、文明尺度：触发 `long-evolution-deep-pack`。
- 框架边界、专业替代、AI 合规剧场、概念武器化：触发 `framework-use-discipline-pack`。

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
