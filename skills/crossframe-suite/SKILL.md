---
name: crossframe-suite
description: |
  CrossFrame Suite 是 CrossFrame skill family 的总调度入口。Use when the user asks for a complex CrossFrame task that may need multiple sibling skills in sequence, such as writing an essay from diagnosis, public commentary, organization repair writing, reader replies, debate-to-article, casebook extraction, teaching plus exercises, reading notes, or review after generation. It decides which CrossFrame skills to read, in what order, and where to stop, so the agent does not trigger every skill at once or skip required reasoning.
---

# CrossFrame Suite

`crossframe-suite` 是总调度 skill，不替代任何专项 skill。它只做三件事：

1. 判断用户任务属于哪条工作流。
2. 安排连续读取顺序。
3. 输出一个简短的调度提纲，然后进入相应 skill。

它不复制 `crossframe`、`crossframe-essay` 或其它平行 skill 的正文。中文为权威语义；英文只作 skill id、文件名和对外传播名。

## 何时使用

当任务不是单一诊断，而可能需要多个 CrossFrame skill 连续协作时，优先使用本 skill：

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
- 评审收束：重要输出默认最后用 `crossframe-review` 做质量闸；轻量短答复可只做内部自检。
- 查源克制：公共议题、真实机构、平台、政策、人物、公司和最新事实要查源；私人关系、哲学泛论、用户自给材料默认不查源。
- 人话优先：最终输出先给普通人能读懂的结果，术语只做必要映射。

## 默认连续链路

```text
结构诊断：
crossframe

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
