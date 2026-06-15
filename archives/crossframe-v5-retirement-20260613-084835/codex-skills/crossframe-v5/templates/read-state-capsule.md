# v5-read-state-capsule

本模板用于 `crossframe-v5` 在中枢诊断前生成一次性的源结构摘要，并传给专项 skill、essay 和 review。它不是文章正文，也不是完整原文摘录。

## 胶囊字段

```text
v5-read-state-capsule
- selection_state：
  - output_mode：
  - role：
  - topic_sensitivity：
  - voice：
  - user_closed_article_layer：
  - user_closed_review：
- workflow_state：
- user_task：
- v5_source_modules：
  - source_module_id：
  - 源范围：
  - 触发理由：
  - 必读相邻模块：
  - 本次使用的模块摘要：
  - 降档边界：
- v5_continuity_bundles：
  - 包 ID：
  - 触发理由：
  - 源锚点/章节范围：
  - 本次使用的源结构摘要：
  - 相邻约束：
  - 不可单读风险：
  - 降档规则：
- source_grounding：
  - 中心命题可用锚点：
  - 机制候选可用锚点：
  - 高风险概念可用锚点：
  - 行动/边界可用锚点：
  - 需要标为“本文推断/思想映射”的内容：
- downstream_read_policy：
  - 默认只读本胶囊和本 skill 协议。
  - 禁止重复整块读取 v5-source-spine.md、v5-section-digest-index.md、v5-continuity-bundles.md。
  - 允许定向补读的条件：
- integrity_risks：
```

## 写法要求

- 每个触发的连读包只写本次相关摘要，不复制完整包说明。
- 每个触发的 source module 只写本次相关摘要，不复制原文或完整索引。
- 每条关键判断至少关联一个源锚点或章节范围。
- 不能从源锚点推出的内容，必须标成“本文推断”“表达转译”或“外部思想映射”。
- 生成胶囊时先按 `source_module_id` 定向抽取，再按包 ID 定向抽取；禁止把完整 `v5-material-selection-map.md`、`v5-continuity-bundles.md`、`v5-source-spine.md` 或 `v5-section-digest-index.md` 填进上下文。
- 胶囊应尽量短；普通文章任务控制在 800-1500 中文字，高责任审计可更长。
- 胶囊只在底稿或审计输出中按需显示；正文不得出现胶囊标题或流程说明。

## 定向补读条件

只有以下情况允许下游补读源索引或连读包：

- 胶囊缺少本次中心命题需要的 source module 或源锚点。
- 高责任、公开判断、现实处置或用户要求审计源结构。
- integrity-check 发现漏读前置包、只读单卡或源锚点不足。
- review 需要定位连续性保真失败。

补读时只打开相关锚点或章节，不整块吞入全量索引。
