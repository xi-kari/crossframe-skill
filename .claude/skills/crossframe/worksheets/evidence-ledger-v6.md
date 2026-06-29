# v6.0 证据台账扩展

本表在现有来源台账和证据台账基础上增加半量化字段。它不替代来源台账，也不让低成本材料叠加成强判断。

## 字段

| 字段 | 取值 | 作用 |
| --- | --- | --- |
| evidence_id | `EV1` | 证据项编号 |
| source_id | 文本 | 回指来源 |
| source_ledger_id | 文本 | 强判断必填 |
| claim_id | `CL1` | 回指命题台账 |
| evidence_cost | low / medium / high | 证据成本 |
| directness | direct / indirect / background | 是否直接支持命题 |
| independence | independent / related / same_source_family | 来源独立性 |
| verifiability | verifiable / partly_verifiable / not_verifiable | 可复核性 |
| counterevidence_status | searched / partial / missing / unsafe_to_collect | 反例搜索状态 |
| diagnostic_force | weak / moderate / strong / decisive_candidate | 对机制候选的诊断力 |
| mechanism_edge | `mechanism_id:edge_id` | 命中的机制边 |
| judgment_grade | 标准判断档位 | 当前证据允许的最高判断 |
| downgrade_reason | 文本 | 为什么不能升级 |
| withdrawal_condition | 文本 | 什么事实触发撤回 |
| action_ceiling | 文本 | 当前最多允许什么行动 |
| cannot_prove | 文本 | 不能证明什么 |

## 证据成本边界

- `low`：AI 摘要、单方表述、热度、满意度、内部评分、漂亮汇报、过程性产物；只能作线索。
- `medium`：可追溯但独立性或反例检查不足的材料；通常只能支持开放断言或完整诊断候选。
- `high`：原始记录、独立复核、可反查材料、高代价行动痕迹；仍不能自动支撑强判断。

## 不能证明什么

每条证据必须写 `cannot_prove`。如果一条来源不能说明“不能证明什么”，它不得进入公共判断或强判断。

常见边界：

- AI/过程性产物不能证明现实安全、修复完成或反例不存在。
- 投诉减少不能证明伤害减少。
- 满意度上升不能证明责任链修复。
- 内部压力测试分数不能证明框架真实有效。
- 同源材料不能通过数量叠加变成独立证据。

## 输出摘要

```text
ledger_id:
case_id:
evidence_id:
source_id:
claim_id:
evidence_cost:
directness:
independence:
verifiability:
counterevidence_status:
diagnostic_force:
mechanism_edge:
downgrade_reason:
withdrawal_condition:
action_ceiling:
cannot_prove:
```
