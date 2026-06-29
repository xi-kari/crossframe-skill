# v6 试跑：关系解释劳动堆积案例

```text
trial_id: v6-trial-relationship-001
source_case: skills/crossframe-casebook/examples/relationship-case.md
case_domain: relationship
trial_status: formal
primary_scale: intimate_relationship_interaction
judgment_grade: open_assertion
action_ceiling: ask_for_evidence
downgrade_triggered: false
anchor_revision_required: false
template_revision_required: false
counterexample_pressure: moderate
rater_record: none
```

## 源案例边界

- 源案例：`skills/crossframe-casebook/examples/relationship-case.md`
- 本次只使用的材料：脱敏聊天摘要、用户复盘记录、源案例已列出的反向条件。
- 本次不新增的事实：不补写对方心理动机，不写人格判断，不把“爱”写成继续忍耐的要求。
- 缺失材料：完整聊天上下文、对方视角、后续行为记录。

## 试跑目的

本 trial 测试 v6 能否把解释劳动堆积保持在开放断言层级，并自动限制行动上限，防止把低成本材料升级成人格定性或关系处置依据。

## 七闸半量化剖面

| gate | gate_state | score | 本案依据 | 降档或补证要求 |
| --- | --- | --- | --- | --- |
| 对象闸 | pass | 3 | 对象是重复互动结构，不是对方人格 | 不得扩展为动机审判 |
| 证据闸 | weak | 1 | 只有摘要和单方复盘，缺原文与对方视角 | 最高保持开放断言 |
| 尺度闸 | pass | 3 | 明确阻断用人格问题替代关系结构 | 若完整上下文显示双方成本对等需重写 |
| 责任闸 | weak | 2 | 可见解释成本单向堆积，但共同规则未完整呈现 | 补双方行动记录 |
| 观测闸 | weak | 2 | 命名结构可能改变关系互动 | 只建议可撤回观察 |
| 权力闸 | weak | 2 | 低权力位置可能是长期解释者，但材料来自单方 | 不得剥夺另一方反例入口 |
| 行动闸 | pass | 3 | 行动只限补证、低成本边界和观察承诺是否落地 | 不建议惩罚或公开定性 |

## 证据台账摘记

| evidence_id | 来源类型 | directness | independence | verifiability | 不能证明什么 | diagnostic_force |
| --- | --- | --- | --- | --- | --- | --- |
| ev-rel-001 | 脱敏聊天摘要 | indirect | related | partly_verifiable | 不能证明完整互动责任分布 | weak |
| ev-rel-002 | 用户复盘记录 | indirect | same_source_family | partly_verifiable | 不能证明对方主观故意 | weak |
| ev-rel-003 | 后续行为缺口 | background | related | not_verifiable | 不能证明承诺是否落地 | weak |

## 构念剖面

| construct_id | 当前读数 | 支撑材料 | 反向条件 | 是否需要校准修订 |
| --- | --- | --- | --- | --- |
| evidence_support_degree | 1 | 材料低成本且同源 | 完整聊天和双方记录可核验 | 否 |
| low_power_counterexample_entry | 2 | 需要保留双方补证入口 | 对方视角显示另一种责任链 | 否 |
| action_ceiling_clarity | 3 | 行动上限限定为补证和观察 | 若输出变成公开定性则必须降级 | 否 |

## 机制候选更新

| mechanism_id | 机制候选 | 支持材料 | 反例压力 | update_direction | 撤回条件 |
| --- | --- | --- | --- | --- | --- |
| mech-rel-explanation-labor | 同一方反复负责解释、安抚和安排 | 三次冲突后同一方发起复盘 | 完整上下文缺失 | pending | 双方解释成本实际对等 |
| mech-rel-short-promise | 短承诺用于结束压力但未改变条件 | 源案例记录“下次会注意” | 转述把握度中低 | pending | 后续出现主动稳定改变 |

## 判断档位与行动上限

- judgment_grade：open_assertion
- action_ceiling：ask_for_evidence
- 不能升级的原因：证据闸只有 1，材料同源且缺对方视角。
- 可撤回的小动作：记录下一轮承诺是否转成具体行为；设置低成本复盘窗口；明确哪些解释劳动不再由单方承担。

## 反例压力与撤回条件

- 已发现反例：完整聊天可能显示另一方也承担大量隐形修复。
- 仍缺失的反例入口：对方视角、原文上下文、后续行为记录。
- 哪些新材料会撤回判断：双方共同承接机制稳定运行，解释成本不再单向堆积。
- 哪些新材料会降级行动上限：摘要无法对应原文或只覆盖冲突片段。

## 写回结果

- downgrade_triggered：false
- anchor_revision_required：false
- template_revision_required：false
- 写回到哪个锚点、模板、checker 或文本边界：保持为低证据成本关系案例，不进入强判断训练集。

## 本案例不能证明

本案例不能证明任何一方人格有问题，不能证明对方故意操控，也不能证明关系必须结束。它只能说明当前材料支持一个可撤回的结构观察：解释和修复成本可能正在单向堆积。
