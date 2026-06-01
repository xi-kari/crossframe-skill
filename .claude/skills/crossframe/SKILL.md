---
name: crossframe
description: 跨尺度结构诊断框架 v2.0 的中文结构推理协议；用于复杂关系、团队、组织、制度与公共议题的诊断、推演、开放断言、反俘获审查和低条件试探行动。
---

# CrossFrame for Claude Code

本 Claude Code skill 是薄适配层。权威主体在 `skills/crossframe/SKILL.md`。

使用时必须：

1. 读取 `skills/crossframe/SKILL.md`。
2. 根据任务类型读取对应 protocol。
3. 默认先输出可见推理提纲。
4. 先说人话，再按需补术语映射。
5. 不把结构诊断写成人格审判、宿命判断或概念堆砌。
6. 使用高风险概念前，读取 `skills/crossframe/references/concept-cards/README.md` 与对应概念卡。

常用入口：

- 普通诊断：`skills/crossframe/protocols/diagnosis-protocol.md`
- 推演：`skills/crossframe/protocols/inference-protocol.md`
- 开放断言：`skills/crossframe/protocols/open-assertion-protocol.md`
- 高责任反俘获：`skills/crossframe/protocols/anti-capture-protocol.md`
- 低条件行动：`skills/crossframe/protocols/low-condition-action-protocol.md`
- 可见提纲：`skills/crossframe/templates/reasoning-outline-output.md`
- 高风险概念：`skills/crossframe/references/concept-cards/`
