# Suite Dispatch Protocol

本协议把用户请求转成连续 skill 工作流。它只做调度，不替代专项判断。

## 1. 判断任务主目标

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

如果用户没有指定最终交付物，但请求是开放式分析或可读表达，默认把最终交付物定为 `essay`。常见表达包括“分析一下”“怎么看”“讲讲”“写一下”“给我一个有洞察的回答”。这时走 `crossframe -> crossframe-essay -> crossframe-review`。

如果用户明确要求非文章交付物，不要默认成文：评审报告、案例库、组织修复备忘录、反馈写回方案、命题辩论表、概念教学练习、来源台账、表格、清单、一句话结论、低条件行动方案和纯诊断，都必须保持原形态。

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
- 本次连续联读包；深度、审计、高责任、公共制度、亲密关系、长期演化和文章输出场景必须从 `../crossframe/references/continuity-bundles.md` 中选择
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
3. 源连续性层：确认是否已读取 `continuity-bundles.md`、`v2-source-spine.md`、`v2-section-digest-index.md` 和 `source-continuity-check.md`
4. 表达生成层：`essay` 或 `dialogue`
5. 质量闸：`review`

例外：

- 只评审：`review` 单独启动。
- 已有完整诊断结果，用户只要成文：`essay -> review`，但需要在底稿中标明诊断来源。
- 开放式分析且未指定格式：`crossframe -> essay -> review`，默认输出可读文章或文章式回答。
- 已有文章，用户只要评审：`review`，必要时读取 `essay` 规则。
- 公共评论必须在 `essay` 前完成 `public` 证据边界。
- 组织修复文章必须在 `essay` 前完成 `org` 责任/授权/回流判断。
- 读书后成文必须在 `essay` 前完成 `notebook` 的关联、不同、可吸收处和冲突处。
- 任何成文任务必须在 `essay` 前完成源结构连续性检查；如果只读了孤立概念卡，先补读或在底稿中降档。

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
