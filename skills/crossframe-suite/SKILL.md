---
name: crossframe-suite
description: |
  CrossFrame Suite 是 CrossFrame skill family 的默认总入口和调度入口。Use by default for CrossFrame-style complex analysis, especially when the user asks for an open-ended readable answer, article-like output, diagnosis-to-essay, public commentary, organization repair writing, reader replies, debate-to-article, casebook extraction, teaching plus exercises, reading notes, or review after generation. It decides which CrossFrame skills to read, in what order, when to produce a readable essay/article, and where to stop, so the agent does not trigger every skill at once or skip required reasoning.
---

# CrossFrame Suite

`crossframe-suite` 是总调度 skill，不替代任何专项 skill。它只做三件事：

1. 判断用户任务属于哪条工作流。
2. 安排连续读取顺序。
3. 输出一个简短的调度提纲，然后进入相应 skill。

它不复制 `crossframe`、`crossframe-essay` 或其它平行 skill 的正文。中文为权威语义；英文只作 skill id、文件名和对外传播名。

当任务触发 CrossFrame 主体时，suite 还要把 `../crossframe/references/continuity-bundles.md` 纳入调度判断：本次是否需要按 v3.0 原文连续板块联读，而不是只读单个概念卡。v2.0 文件只作为历史基线；默认以 v3.0 源结构为准。

## 默认入口

一般使用 CrossFrame family 时，优先从本 skill 进入。只有任务非常单一时，才直接使用对应专项 skill。

当用户没有明确指定交付物，只是说“分析一下”“怎么看”“讲讲这个问题”“给我一个有洞察的回答”“写一下这个主题”时，本 skill 默认把最终输出做成**可读文章/文章式回答**：

```text
crossframe -> crossframe-essay -> crossframe-review
```

这条默认不是为了把所有回答写长，而是因为可读文章更适合把结构判断交给普通读者：先有底稿，再成文，最后过质量闸。

这条默认同时默认启用 `crossframe-essay` 的现代编辑底色：像一位耐心、谦逊、认真、果敢的中文编辑在回应读者问题。除非用户明确要求中性报告、备忘录、表格、清单、纯诊断或学术摘要，否则不要把最终输出写成冷冰冰的诊断说明。

不要在以下场景擅自生成文章：用户明确要求评审报告、案例库条目、组织修复备忘录、反馈写回方案、命题辩论表、概念教学练习、来源台账、表格、清单、一句话结论、低条件行动方案或纯诊断。此时应保留用户指定的交付物。

## 何时使用

当任务不是单一诊断，而可能需要多个 CrossFrame skill 连续协作时，优先使用本 skill：

- 用户希望使用 CrossFrame，但没有指定具体子 skill。
- 用户只说“分析一下/怎么看/讲讲/写一下”，且更像想看一段可读输出。
- 写文章、评论、思想文章、公共评论、组织复盘文章。
- 答读者问、编辑回信、咨询式回应，但问题背后有结构诊断。
- 把材料整理成案例，再写分析或沉淀概念。
- 读书、理论、文章研究笔记，需要比较与 CrossFrame 的关联和不同。
- 命题辩论后需要成文、给结论或写反驳。
- 先生成输出，再评审它是否真的推理。
- 用户说“这些 skill 应该一起用”“连续触发”“总规则”“总入口”“怎么组合调用”。

若任务非常单一，直接使用对应专项 skill，不要绕行：

- 只要结构诊断：`../crossframe/SKILL.md`
- 只要文章：`../crossframe-essay/SKILL.md`
- 只要评审：`../crossframe-review/SKILL.md`
- 只要短答复：`../crossframe-dialogue/SKILL.md`
- 只要案例库：`../crossframe-casebook/SKILL.md`
- 只要公共议题证据边界：`../crossframe-public/SKILL.md`
- 只要组织修复备忘录：`../crossframe-org/SKILL.md`
- 只要概念教学：`../crossframe-teach/SKILL.md`
- 只要命题论证：`../crossframe-debate/SKILL.md`
- 只要读书研究笔记：`../crossframe-notebook/SKILL.md`

## 必须读取

每次触发后读取：

1. `references/workflow-routing-map.md`
2. `protocols/suite-dispatch-protocol.md`
3. `templates/suite-reasoning-outline.md`

然后按路由读取对应 sibling skill。基础结构判断通常先读 `../crossframe/SKILL.md` 与 `../crossframe/references/read-routing-map.md`。

## 调度原则

- 基础先行：多数复杂任务先由 `crossframe` 建立事实边界、尺度窗口、机制候选和判断档位。
- 场景追加：只读取本次必要的专项 skill，不把全部 skill 一起触发。
- 成文后置：写文章前先有结构洞察底稿；公共、组织、辩论、读书等专项判断先完成，再进入 `crossframe-essay`。
- 默认成文：suite 被触发且用户未指定非文章交付物时，最终输出默认走 `crossframe-essay`，生成可读文章或文章式回答。
- 默认声口：suite 默认成文时，必须把“现代编辑底色”传给 `crossframe-essay`。问题型主题用答复体；公共评论、思想文章和概念文章用评论体；只有用户显式要求中性报告/备忘录/表格/纯诊断时才关闭文章声口。
- 成文边界：只有用户想看可读输出、文章、评论、思想文章、长答复或面向他人传播的内容时才生成文章；明确要备忘录、评审、案例、教学、表格或行动清单时不生成文章。
- 源连续性：高责任、公共制度、亲密关系、长期演化、深度分析、框架治理、AI 现实验证、弱信号/不透明、无法退出和文章输出，要在调度中列出本次触发的 v3.0 连续联读包；不要只列概念卡。
- 评审收束：重要输出默认最后用 `crossframe-review` 做质量闸；轻量短答复可只做内部自检。
- 查源克制：公共议题、真实机构、平台、政策、人物、公司和最新事实要查源；私人关系、哲学泛论、用户自给材料默认不查源。
- 人话优先：最终输出先给普通人能读懂的结果，术语只做必要映射。

## 默认连续链路

```text
结构诊断：
crossframe

开放式可读分析：
crossframe -> crossframe-essay -> crossframe-review

普通洞察文章：
crossframe -> crossframe-essay -> crossframe-review

公共评论文章：
crossframe -> crossframe-public -> crossframe-essay -> crossframe-review

组织复盘/修复文章：
crossframe -> crossframe-org -> crossframe-essay -> crossframe-review

答读者问/编辑回信：
crossframe -> crossframe-dialogue -> crossframe-review-lite

案例沉淀：
crossframe -> crossframe-casebook -> crossframe-review

概念教学：
crossframe -> crossframe-teach -> crossframe-review-lite

命题辩论：
crossframe -> crossframe-debate -> crossframe-review

辩论后成文：
crossframe -> crossframe-debate -> crossframe-essay -> crossframe-review

读书/理论研究：
crossframe -> crossframe-notebook -> crossframe-review

读书后成文：
crossframe -> crossframe-notebook -> crossframe-essay -> crossframe-review
```

`crossframe-review-lite` 表示不必输出完整评审报告，但必须检查：是否跳过事实边界、是否人格审判、是否概念堆砌、是否越过证据档位。

## 输出方式

除非用户只问“该用哪个 skill”，否则最终输出先给一个短调度提纲：

```text
调度提纲
- 任务类型：
- 工作流：
- 必读 skill：
- 按需读取：
- 连续联读包：
- 正文声口：
- 不读取：
- 质量闸：
```

然后进入对应 skill 的正常输出。不要把调度提纲写得比任务本身还长。

## 禁止

- 禁止为了显得完整而触发全部 skill。
- 禁止跳过 `crossframe` 的事实边界和判断档位直接写文章。
- 禁止公共议题不查源却做强判断。
- 禁止把 `crossframe-review` 当作形式收尾；它必须能否决坏输出。
- 禁止让调度规则取代专项 skill 的协议。
