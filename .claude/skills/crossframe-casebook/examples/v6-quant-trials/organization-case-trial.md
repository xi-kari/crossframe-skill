# v6 试跑：组织复盘伪修复案例

```text
trial_id: v6-trial-organization-001
source_case: skills/crossframe-casebook/examples/organization-case.md
case_domain: organization
trial_status: formal
primary_scale: organization_project_governance
judgment_grade: full_diagnosis
action_ceiling: internal_review
downgrade_triggered: false
anchor_revision_required: false
template_revision_required: false
counterexample_pressure: moderate
rater_record: embedded
```

## 源案例边界

- 源案例：`skills/crossframe-casebook/examples/organization-case.md`
- 本次只使用的材料：三次复盘纪要摘要、验收标准修改记录摘要、脱敏访谈摘记。
- 本次不新增的事实：不补写管理层动机、不推断客户真实意图、不扩展到组织文化定性。
- 缺失材料：管理层决策记录、客户验收依据、变更审批原始链路。

## 试跑目的

本 trial 测试 v6 能否把“复盘很多但没有改变条件”的组织案例拆成责任链、反馈写回、证据成本和行动上限，而不是把它写成团队沟通差或执行层态度问题。

## 七闸半量化剖面

| gate | gate_state | score | 本案依据 | 降档或补证要求 |
| --- | --- | --- | --- | --- |
| 对象闸 | pass | 3 | 诊断对象限定为项目复盘机制和验收口径漂移 | 不扩大为整个组织人格化判断 |
| 证据闸 | weak | 2 | 有纪要、版本记录和访谈摘记，但缺管理层决策链 | 补决策记录前不能升级为强判断 |
| 尺度闸 | pass | 3 | 主尺度是组织项目治理，明确阻断“一线执行差”归因 | 若发现一线拥有同等改变权需重写 |
| 责任闸 | pass | 3 | 条件制定者、执行者、成本承担者和潜在承接者可区分 | 需补验收权归属 |
| 观测闸 | weak | 2 | 复盘本身可能改变发言策略，访谈摘记受组织压力影响 | 需要下一轮复盘行为观察 |
| 权力闸 | weak | 2 | 一线成员表达成本较高，低权力反例入口不完整 | 需建立匿名补证与申诉窗口 |
| 行动闸 | pass | 3 | 行动上限限定为内部复盘、冻结验收标准、记录变更成本 | 不允许公开定责或处分 |

## 证据台账摘记

| evidence_id | 来源类型 | directness | independence | verifiability | 不能证明什么 | diagnostic_force |
| --- | --- | --- | --- | --- | --- | --- |
| ev-org-001 | 会议纪要摘要 | direct | related | partly_verifiable | 不能证明管理层故意转移责任 | moderate |
| ev-org-002 | 版本记录摘要 | direct | independent | verifiable | 不能证明每次修改都不合理 | strong |
| ev-org-003 | 脱敏访谈摘记 | indirect | related | partly_verifiable | 不能代表全部一线成员 | moderate |

## 构念剖面

| construct_id | 当前读数 | 支撑材料 | 反向条件 | 是否需要校准修订 |
| --- | --- | --- | --- | --- |
| responsibility_chain_traceability | 3 | 责任链角色可以分出，但验收权细节缺失 | 发现一线拥有同等验收修改权 | 否 |
| feedback_writeback_degree | 1 | 三次复盘均停留在“加强沟通” | 后续复盘记录成本回流和规则改写 | 否 |
| action_ceiling_clarity | 3 | 内部复盘和流程冻结边界清楚 | 若材料被用于处分个人则必须降级 | 否 |

## 机制候选更新

| mechanism_id | 机制候选 | 支持材料 | 反例压力 | update_direction | 撤回条件 |
| --- | --- | --- | --- | --- | --- |
| mech-org-pseudo-repair | 复盘动作承担归档和安抚功能，但没有改变验收条件 | 三次纪要重复同一口号，验收标准仍漂移 | 管理层记录缺失，存在执行偏差可能 | strengthen | 变更审批完整且一线未按流程执行 |
| mech-org-responsibility-drift | 上游口径变化成本下沉到项目经理和一线 | 版本记录和访谈摘记相互支持 | 访谈可能只覆盖部分成员 | pending | 成本记录已制度化回流 |

## 判断档位与行动上限

- judgment_grade：full_diagnosis
- action_ceiling：internal_review
- 不能升级的原因：证据闸和权力闸均为 weak，缺管理层决策记录和安全反例入口。
- 可撤回的小动作：冻结验收标准、记录口径变更成本、把复盘问题从“沟通”改成“谁能改变条件”。

## 评分者原始记录

### rater_a

| gate | gate_state | score | 理由 |
| --- | --- | --- | --- |
| 对象闸 | pass | 3 | 对象边界清楚 |
| 证据闸 | weak | 2 | 缺决策记录 |
| 尺度闸 | pass | 3 | 明确阻断执行层归因 |
| 责任闸 | pass | 3 | 责任链可追踪 |
| 观测闸 | weak | 2 | 复盘会改变组织发言 |
| 权力闸 | weak | 2 | 一线反例入口不足 |
| 行动闸 | pass | 3 | 行动上限清楚 |

- judgment_grade: full_diagnosis
- action_ceiling: internal_review
- evidence_gap: 管理层决策记录、客户验收依据
- counterexample_pressure: moderate

### rater_b

| gate | gate_state | score | 理由 |
| --- | --- | --- | --- |
| 对象闸 | pass | 3 | 案例对象稳定 |
| 证据闸 | weak | 2 | 材料可追溯但不完整 |
| 尺度闸 | pass | 3 | 没有尺度偷换 |
| 责任闸 | weak | 2 | 条件制定者仍需补证 |
| 观测闸 | weak | 2 | 访谈可能有压力 |
| 权力闸 | weak | 2 | 低权力反证渠道不足 |
| 行动闸 | pass | 3 | 仅限内部制度修复 |

- judgment_grade: full_diagnosis
- action_ceiling: internal_review
- evidence_gap: 验收权归属、变更审批原文
- counterexample_pressure: moderate

## 反例压力与撤回条件

- 已发现反例：如果存在明确变更审批且一线未按流程执行，本判断要从伪修复转为执行偏差。
- 仍缺失的反例入口：一线成员匿名补充、管理层决策链、客户验收依据。
- 哪些新材料会撤回判断：稳定运行的验收冻结机制和成本回流记录。
- 哪些新材料会降级行动上限：访谈样本单一且版本记录无法核验。

## 写回结果

- downgrade_triggered：false
- anchor_revision_required：false
- template_revision_required：false
- 写回到哪个锚点、模板、checker 或文本边界：保留为责任链与反馈写回的校准样本。

## 本案例不能证明

本案例不能证明组织整体失能，不能证明管理层主观恶意，不能证明所有复盘都是伪修复，也不能授权处分具体个人。它只能支持一次内部机制复盘，并要求补证后再决定是否升级。
