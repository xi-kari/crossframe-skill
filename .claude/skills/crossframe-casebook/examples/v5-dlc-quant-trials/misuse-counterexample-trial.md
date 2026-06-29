# v5 DLC 试跑：尺度升维误用反例

```text
trial_id: v5-dlc-trial-misuse-001
source_case: skills/crossframe/examples/scale-transfer-misuse-case.md
case_domain: misuse_counterexample
trial_status: counterexample
primary_scale: intimate_relationship_low_scale_harm
judgment_grade: open_assertion
action_ceiling: block_publication
downgrade_triggered: true
anchor_revision_required: true
template_revision_required: true
counterexample_pressure: decisive
rater_record: none
```

## 源案例边界

- 源案例：`skills/crossframe/examples/scale-transfer-misuse-case.md`
- 本次只使用的材料：用户输入中的长期消耗和“大格局成长阶段”解释，以及源案例的输出要点与撤回条件。
- 本次不新增的事实：不推断关系双方完整责任，不写成长意义是否真实存在，不替代安全、法律或心理支持。
- 缺失材料：具体互动记录、双方反馈后的行为变化、安全风险信息。

## 试跑目的

本 trial 是反例压力测试：如果 v5 DLC 半量化表被用来给“更大格局解释”背书，它必须主动降档并阻断。关键不是给关系打分，而是保护低尺度痛苦、责任链和可撤回行动边界。

## 七闸半量化剖面

| gate | gate_state | score | 本案依据 | 降档或补证要求 |
| --- | --- | --- | --- | --- |
| 对象闸 | weak | 2 | 对象是尺度升维解释是否稀释痛苦，关系事实很少 | 不能转成完整关系诊断 |
| 证据闸 | fail | 1 | 只有一句输入和源案例摘要 | 最高开放断言 |
| 尺度闸 | fail | 0 | “更大格局”正在取消低尺度痛苦和责任问题 | 必须阻断升维背书 |
| 责任闸 | weak | 1 | 谁能改变条件未知，只能要求追问成本承担 | 不能替任何一方定责 |
| 观测闸 | weak | 2 | 公开命名可能改变关系中的压力分布 | 不公开具体判断 |
| 权力闸 | fail | 1 | 长期被消耗者可能处于低权力位置，反例入口不安全 | 先保护边界和补证 |
| 行动闸 | blocked | 0 | 用分数背书成长叙事会越权 | 只能阻断误用并转向低风险观察 |

## 证据台账摘记

| evidence_id | 来源类型 | directness | independence | verifiability | 不能证明什么 | diagnostic_force |
| --- | --- | --- | --- | --- | --- | --- |
| ev-mis-001 | 用户输入片段 | indirect | same_source_family | not_verifiable | 不能证明完整关系结构 | weak |
| ev-mis-002 | 源案例输出要点 | background | related | partly_verifiable | 不能证明现实危险程度 | weak |
| ev-mis-003 | 撤回条件 | background | related | partly_verifiable | 不能证明双方没有共同成长 | weak |

## 构念剖面

| construct_id | 当前读数 | 支撑材料 | 反向条件 | 是否需要校准修订 |
| --- | --- | --- | --- | --- |
| scale_consistency | 0 | 高尺度叙事直接压低低尺度痛苦 | 双方都有真实成本承担且反馈后稳定改变 | 是 |
| evidence_support_degree | 1 | 只有输入片段 | 出现完整互动记录和双方视角 | 否 |
| counterexample_writeback_strength | 4 | 本案暴露模板必须阻断升维背书 | 模板已显式阻断此类用法 | 是 |

## 机制候选更新

| mechanism_id | 机制候选 | 支持材料 | 反例压力 | update_direction | 撤回条件 |
| --- | --- | --- | --- | --- | --- |
| mech-mis-scale-erasure | 高尺度成长叙事抹掉低尺度痛苦和责任链 | 用户输入中的“大格局”解释 | 关系事实不足 | strengthen | 双方反馈后边界和行为稳定改变 |
| mech-mis-failed-repair | 反馈没有改变双方行为和边界 | 源案例机制候选 | 具体互动记录缺失 | pending | 后续显示共同修复机制有效 |

## 判断档位与行动上限

- judgment_grade：open_assertion
- action_ceiling：block_publication
- 不能升级的原因：证据闸 fail、尺度闸 fail、权力闸 fail、行动闸 blocked。
- 可撤回的小动作：先问谁长期承担成本、谁能改变条件、反馈后什么真实变化；只给低风险边界提醒。

## 反例压力与撤回条件

- 已发现反例：如果双方都有真实成本承担，反馈后边界和行为稳定改变，尺度升维稀释机制要撤回。
- 仍缺失的反例入口：被消耗者能否安全补证，对方是否有可核验改变，是否存在安全风险。
- 哪些新材料会撤回判断：具体互动记录显示“成长阶段”并未压低痛苦，反而带来共同承接机制。
- 哪些新材料会降级行动上限：材料涉及安全风险、心理危机、法律风险或公开名誉风险。

## 写回结果

- downgrade_triggered：true
- anchor_revision_required：true
- template_revision_required：true
- 写回到哪个锚点、模板、checker 或文本边界：七闸模板需要增加规则：当尺度闸为 fail 且低尺度痛苦被高尺度叙事稀释时，action_ceiling 必须是 `block_publication` 或 `ask_for_evidence`，不能给任何成长叙事背书。

## 本案例不能证明

本案例不能证明这段关系一定有害，不能证明成长意义不存在，不能证明任何一方应被公开定性。它只证明一个 v5 DLC 治理要求：半量化工具必须能阻断“用尺度解释取消低尺度痛苦”的误用。
