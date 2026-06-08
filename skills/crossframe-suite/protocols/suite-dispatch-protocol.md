# Suite Dispatch Protocol

本协议把用户请求转成连续 skill 工作流。它只做调度，不替代专项判断。

**suite 本身仅通过 `/crossframe-suite` 斜杠命令触发。** 不存在自然语言触发途径。suite 被斜杠命令激活后，再按本协议做内部调度。

## 0. 模式与角色判定（强制交互）

读取 `../crossframe-suite/references/output-mode-selector.md`，根据用户触发词自动判定本次的 output_mode（保守/客观/激进/批判）、role（学术专家/实践工匠/战略决策者/大众传播/批判反思者/未来探索者）和 `topic_sensitivity`（low/normal/vulnerable/high-stakes）。

**若用户在本次对话中未使用任何触发关键词（保守、客观、激进、批判、学术、实操、战略、通俗、批判反思、未来、1-6 数字加模式组合），AI 必须主动展示 `../crossframe-suite/templates/mode-selection-dialog.md` 弹窗，并在此处停止，等待用户回复后再继续。**

即使用户只说了一句"分析一下这个现象"，没有提任何模式或角色，也必须先弹出选项。不得以"用户没说"为由跳过弹窗、直接使用默认值跑完全程。默认值（客观/学术专家）仅在以下情况生效：用户明确回复"默认"、或以"直接开始/随便/都行/不用选"等措辞表示不需要选择。`topic_sensitivity` 不需要用户选择，由题材自动判定；若出现痛苦、绝望、创伤、无法退出、求助暗示或高责任现实处置，必须显式写入调度提纲。

## 1. 判断任务主目标

**suite 是子 skill 的唯一合法入口。** 如果 AI 直接从用户消息中匹配到子 skill 的 description 而绕过本节，视为调度错误。所有 CrossFrame 任务必须经过本协议的路由判断。

先选一个主目标：

- `diagnose`：只要结构诊断、推演、开放断言或低条件行动。
- `essay`：要文章、评论、思想文章、长文、报刊答复体文章。
- `dialogue`：要短答复、编辑回信、咨询式回应。
- `casebook`：要把材料沉淀成案例。
- `public`：公共议题、制度、平台、政策、机构合规、公共承诺。
- `org`：团队、项目、组织修复、复盘改造、反馈写回。
- `teach`：解释 CrossFrame 概念、讲给普通人、出练习。
- `debate`：命题辩论、正反双方、隐藏前提、反驳。
- `notebook`：读书、理论、文章研究笔记。
- `review`：审查一个已有输出。

如果用户同时要求多个目标，确定一个最终交付物，再安排前置 skill。例如“分析公共议题并写文章”的最终交付物是文章，但前置需要 `public`。

只要用户通过 `crossframe-suite` 进入 CrossFrame 内容任务，默认最终交付物都定为 `essay`，走同一完整链路 `crossframe -> [needed sibling skills] -> crossframe-essay(full-visible-v3-longform) -> crossframe-review`。不做深度分级，不因问题"小"而跳过步骤。如果任务还需要评审、案例库、组织修复、命题辩论、概念教学、读书研究或短答复，先完成对应专项产物，再进入 `crossframe-essay`。

默认 `output_mode=full-visible-v3-longform`。`voice_mode` 不再默认设为 `editorial-base`——由 §0 判定的角色自动决定：学术专家/批判反思者→中性分析体；大众传播/未来探索者→按需启用编辑底色。用户显式要求"亲切/编辑口吻"时覆盖。

只有用户明确要求“只要/不要文章/不要成文/短答/三句话/表格/清单/原始评审/原始案例库/原始备忘录/纯诊断/仅行动方案”时，才不要默认成文。此时评审报告、案例库、组织修复备忘录、反馈写回方案、命题辩论表、概念教学练习、来源台账、表格、清单、一句话结论、低条件行动方案和纯诊断保持原形态。

## 2. 先定基础 skill

除以下情况外，复杂任务都先读取 `../crossframe/SKILL.md`：

- 用户只要求评审某段输出：先读 `../crossframe-review/SKILL.md`。
- 用户只要求安装、解释 skill 触发方式或仓库维护：不进入诊断链。
- 用户只要求改写一句话、翻译或格式化：不使用 CrossFrame Suite。

读取 `crossframe` 后，必须带出最小内部产物：

- 对象
- 事实边界
- 尺度窗口
- 至少两个机制候选，或说明为何只有一个
- 判断档位
- 本次连续联读包；深度、审计、高责任、公共制度、亲密关系、长期演化和文章输出场景必须从 `../crossframe/references/integrity-check.md` 中确认
- 需要追加的专项 skill

## 3. 加专项 skill

按任务信号追加，不要全量读取：

- 写成文章：追加 `../crossframe-essay/SKILL.md`。
- 公共议题：追加 `../crossframe-public/SKILL.md`。
- 组织修复：追加 `../crossframe-org/SKILL.md`。
- 短答复/回信：追加 `../crossframe-dialogue/SKILL.md`。
- 案例沉淀：追加 `../crossframe-casebook/SKILL.md`。
- 概念教学：追加 `../crossframe-teach/SKILL.md`。
- 命题论证：追加 `../crossframe-debate/SKILL.md`。
- 读书研究：追加 `../crossframe-notebook/SKILL.md`。
- 质量验收：追加 `../crossframe-review/SKILL.md`。

## 4. 排序规则

默认顺序：

1. 结构事实层：`crossframe`
2. 场景专项层：`public` / `org` / `debate` / `notebook` / `casebook` / `teach` / `dialogue`
3. 源连续性层：读取 `../crossframe/references/integrity-check.md` 做一次性完整性检查（覆盖联读包、概念保真和源连续性）
4. 表达生成层：`essay` 或 `dialogue`
5. 质量闸：`review`

例外：

- 只评审：`review` 单独启动。
- 已有完整诊断结果，用户只要成文：`essay -> review`，但需要在底稿中标明诊断来源。
- suite 默认：`crossframe -> needed sibling skills -> essay -> review`，默认输出 `full-visible-v3-longform`，也就是完整可见底稿 + 完整长文正文。
- 已有文章，用户只要评审：`review`，必要时读取 `essay` 规则。
- 公共评论必须在 `essay` 前完成 `public` 证据边界。
- 组织修复文章必须在 `essay` 前完成 `org` 责任/授权/回流判断。
- 读书后成文必须在 `essay` 前完成 `notebook` 的关联、不同、可吸收处和冲突处。
- 任何成文任务必须在 `essay` 前完成源结构连续性检查；如果只读了孤立概念卡，先补读或在底稿中降档。
- **dialogue→essay 收束规则**：用户收到短答复后，如果回复"好的/谢谢/明白了/懂了/我再想想/嗯/了解了"等收束性措辞，视为短答复已满足需求，不追成文章。只有用户明确说"展开/写详细/能不能写成长文/继续分析/然后呢/还有什么"时才进入 essay。

## 4.1 声口传递规则

只要 suite 没有被用户显式关闭文章层，就把 `voice_mode` 和 `topic_sensitivity` 一起传给 `crossframe-essay`：

- `neutral-analysis`：学术专家/批判反思者默认使用。允许清楚、平实、有正常温度；不启用现代编辑底色。
- `neutral-decisive`：实践工匠/战略决策者默认使用。可以给出优先级、步骤和止损条件。
- `editorial-reply`：大众传播或用户显式要求亲切/编辑口吻时，用于读者提问、关系困惑、组织困惑、怎么办/怎么看/为什么会这样。
- `editorial-commentary`：大众传播/未来探索者或用户显式要求时，用于公共评论、思想文章、制度评论、概念文章。

这些声口只改变前台表达，不改变事实边界、概念保真、连续联读包和判断档位。若未启用编辑底色的角色因为 `topic_sensitivity=vulnerable` 需要明显共情承接，或因为论证需要拆题/改良版选项，必须在底稿中声明原因和边界。`topic_sensitivity=high-stakes` 默认优先审计型底稿，不用文章温度覆盖判断责任。

## 4.2 输出档位规则

只要 suite 没有被用户显式关闭文章层，就把 `output_mode=full-visible-v3-longform` 传给 `crossframe-essay`。

该档位要求：

- 底稿完整可见，不把 v3.0 源连续性、联读包、概念风险和反向条件藏掉。
- 正文默认 1200-2200 中文字，写成文章而不是项目符号答复。
- 哲学概念、思想文章、关系/组织/公共评论默认必须有标题、铺陈、概念上升、现实回落、边界段和余味结尾。
- 禁止用“如果只要一句话”“换成人话说”作为正文开篇来替代完整文章。

所有任务默认输出 `full-visible-v3-longform`。只有用户明确要短答、只要一句话、三句话、表格、备忘录、清单、行动方案、纯诊断、学术摘要或不要文章时，才把 `output_mode` 改为对应专项交付物。不以"问题简单"为由自动降档。

## 5. 质量闸

默认最后加入 `crossframe-review`，但有两档：

- 完整评审：文章、公共议题、组织修复、案例库、辩论结论、读书研究、强判断。
- 轻量自检：短答复、教学解释、低风险概念说明。

完整评审可输出报告；轻量自检只需要在内部检查，不必打扰用户，除非发现硬失败。

## 6. 输出收束

调度提纲必须短。它的目的不是展示复杂，而是让用户看见 AI 为什么按这个顺序工作。

如果用户要求“只给最终结果”，可以压缩为一行：

```text
本次按 crossframe -> crossframe-public -> crossframe-essay -> crossframe-review 处理。
```

然后直接输出结果。
