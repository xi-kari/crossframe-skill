---
name: crossframe-suite
description: CrossFrame Suite 是 CrossFrame skill family 的总调度入口。仅通过 /crossframe-suite 斜杠命令触发，不被任何自然语言被动触发。内部调度全部 12 个 skill 的读取顺序和工作流。
trigger: slash-only
---

# CrossFrame Suite

`crossframe-suite` 是总调度 skill，不替代任何专项 skill。它只做三件事：

1. 判断用户任务属于哪条工作流。
2. 安排连续读取顺序。
3. 输出一个简短的调度提纲，然后进入相应 skill。

它不复制 `crossframe`、`crossframe-essay` 或其它平行 skill 的正文。中文为权威语义；英文只作 skill id、文件名和对外传播名。

> **本 skill 仅通过 `/crossframe-suite` 斜杠命令触发。** 不被"用 CrossFrame""crossframe""结构诊断""用框架分析"等任何自然语言被动触发，也不被"分析一下""怎么看""讲讲""写一下"等日常用语触发。唯一入口是用户输入 `/crossframe-suite` 命令。

当任务触发 CrossFrame 主体时，suite 还要把 `../crossframe/references/integrity-check.md` 纳入调度判断：本次是否需要按 v3.0 原文连续板块联读，而不是只读单个概念卡。integrity-check.md 合并了联读包索引、概念保真检查和源结构连续性检查的完整入口。v2.0 文件只作为历史基线；默认以 v3.0 源结构为准。

## 调用方式

用户输入斜杠命令 `/crossframe-suite` 进入本 skill。这是唯一入口——不被任何自然语言触发。suite 被激活后，读取 dispatch 协议、弹出模式/角色选择器、按路由调度子 skill。

当用户通过本 skill 作为入口提出任何 CrossFrame 内容任务时，默认最终都生成**3.0 混合长文**，输出档位为 `full-visible-v3-longform`：完整可见底稿 + 完整长文正文。所有任务走同一完整链路，不做深度分级。框架谦逊地接住每一个问题。

```text
crossframe -> [needed sibling skills] -> crossframe-essay(full-visible-v3-longform) -> crossframe-review
```

这条默认不是为了把所有回答写长，而是因为文章更适合把结构判断、专项产物和 3.0 保真检查交给普通读者：先完成必要的诊断/评审/案例/教学/辩论/备忘录，再形成底稿，再成文，最后过质量闸。

这条默认同时默认启用 `crossframe-essay` 的现代编辑底色：像一位耐心、谦逊、认真、果敢的中文编辑在回应读者问题。除非用户明确要求中性报告、备忘录、表格、清单、纯诊断或学术摘要，否则不要把最终输出写成冷冰冰的诊断说明。

`full-visible-v3-longform` 的意思是：v3.0 连续联读包、源结构保真、概念风险和反向条件要在底稿中可见；但这些后台检查不能吞掉正文。正文仍必须写成完整文章，有标题、铺陈、概念上升、现实回落、边界和余味。

只有在用户明确说“只要/不要文章/不要成文/短答/三句话/表格/清单/原始评审/原始案例库/原始备忘录/纯诊断/仅行动方案”时，才关闭默认文章层。此时应保留用户指定的交付物。

## 何时使用

用户输入斜杠命令 `/crossframe-suite` 时。这是唯一入口。不存在其他触发途径——没有自然语言关键词、没有被动匹配、没有 AI 主动建议。

**所有 CrossFrame 任务统一从本 skill 进入。** suite 被激活后判断工作流，内部调度全部 12 个 skill。用户无需知道子 skill 名称。

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
- 默认成文：suite 被触发时，最终输出默认走 `crossframe-essay`，输出档位固定为 `full-visible-v3-longform`；专项产物先做，文章后置。
- 声口由角色决定：在 v3.1 中，声口不再默认传递，由 `output-mode-selector.md` 中的角色自动决定：学术专家/批判反思者→中性分析体；大众传播/未来探索者→按需启用编辑底色（答复体/评论体）。用户显式要求"亲切/编辑口吻"时覆盖以上默认。
- 长文契约：任何从 suite 进入、且未显式关闭文章层的 CrossFrame 内容任务，默认不是短答，不得用项目符号诊断、摘要式回答或“如果只要一句话”替代完整正文。
- 成文边界：默认对所有 CrossFrame 内容任务成文；只有用户用“只要/不要文章/短答/表格/清单/纯诊断/仅行动方案”等词明确关闭时，才关闭文章层。
- 源连续性：高责任、公共制度、亲密关系、长期演化、深度分析、框架治理、AI 现实验证、弱信号/不透明、无法退出和文章输出，要在调度中列出本次触发的 v3.0 连续联读包；不要只列概念卡。
- 评审收束：重要输出默认最后用 `crossframe-review` 做质量闸；轻量短答复可只做内部自检。
- 查源克制：公共议题、真实机构、平台、政策、人物、公司和最新事实要查源；私人关系、哲学泛论、用户自给材料默认不查源。
- 人话优先：最终输出先给普通人能读懂的结果，术语只做必要映射。

## 默认连续链路

```text
结构诊断：
crossframe -> crossframe-essay(full-visible-v3-longform) -> crossframe-review

开放式可读分析：
crossframe -> crossframe-essay(full-visible-v3-longform) -> crossframe-review

普通洞察文章：
crossframe -> crossframe-essay(full-visible-v3-longform) -> crossframe-review

公共评论文章：
crossframe -> crossframe-public -> crossframe-essay(full-visible-v3-longform) -> crossframe-review

组织复盘/修复文章：
crossframe -> crossframe-org -> crossframe-essay(full-visible-v3-longform) -> crossframe-review

答读者问/编辑回信：
crossframe -> crossframe-dialogue -> crossframe-essay(full-visible-v3-longform) -> crossframe-review

案例沉淀：
crossframe -> crossframe-casebook -> crossframe-essay(full-visible-v3-longform) -> crossframe-review

概念教学：
crossframe -> crossframe-teach -> crossframe-essay(full-visible-v3-longform) -> crossframe-review

命题辩论：
crossframe -> crossframe-debate -> crossframe-essay(full-visible-v3-longform) -> crossframe-review

辩论后成文：
crossframe -> crossframe-debate -> crossframe-essay -> crossframe-review

读书/理论研究：
crossframe -> crossframe-notebook -> crossframe-essay(full-visible-v3-longform) -> crossframe-review

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
- 输出档位：
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
- 禁止以"问题简单/轻量"为由跳过完整诊断链或压缩长文输出。框架谦逊地接住每一个问题。
- 禁止 AI 绕过 suite 直接调用任何子 skill。禁止因用户提到了子 skill 中的概念或场景就直接跳入该子 skill。所有 CrossFrame 任务必须经由 suite 入口统一调度。
- 禁止 AI 在任何自然语言场景下主动触发 CrossFrame。suite 仅通过 /crossframe-suite 斜杠命令激活——不存在自然语言触发词。框架是工具——用户决定何时使用它。
