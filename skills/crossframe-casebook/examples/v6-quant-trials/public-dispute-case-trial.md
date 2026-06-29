# v6 试跑：公共争议平台治理案例

```text
trial_id: v6-trial-public-001
source_case: skills/crossframe-casebook/examples/public-dispute-case.md
case_domain: public_dispute
trial_status: formal
primary_scale: platform_governance_public_commitment
judgment_grade: open_assertion
action_ceiling: block_publication
downgrade_triggered: true
anchor_revision_required: true
template_revision_required: false
counterexample_pressure: strong
rater_record: embedded
```

## 源案例边界

- 源案例：`skills/crossframe-casebook/examples/public-dispute-case.md`
- 本次只使用的材料：公开公告摘要、公告对比、公开评论抽样、规则文本这一材料类型说明。
- 本次不新增的事实：不补写真实平台名，不推断内部处置动机，不把评论抽样当成全部用户意见。
- 缺失材料：内部处置依据、申诉数据、被影响方完整反馈、规则版本时间线。

## 试跑目的

本 trial 测试公共争议场景中，v6 是否会在低权力反例入口和公开边界不足时主动阻断发布，而不是把平台公告或舆论热度当成治理完成证据。

## 七闸半量化剖面

| gate | gate_state | score | 本案依据 | 降档或补证要求 |
| --- | --- | --- | --- | --- |
| 对象闸 | pass | 3 | 对象是平台回应与制度承接差距 | 不判断真实事件责任 |
| 证据闸 | weak | 2 | 有公告摘要和评论抽样，但缺申诉数据和被影响方反馈 | 真实事件必须补源链接和时间线 |
| 尺度闸 | pass | 3 | 区分舆论反应、平台制度和个案处置 | 不用网友情绪替代制度问题 |
| 责任闸 | weak | 2 | 规则制定者和处置团队可见，但内部依据缺失 | 补流程责任链 |
| 观测闸 | weak | 2 | 舆论压力改变回应策略，材料高度反身 | 不把回应次数当承接程度 |
| 权力闸 | fail | 1 | 被影响方申诉、复核和纠错入口缺失 | 公开发布必须阻断 |
| 行动闸 | blocked | 0 | 真实公共事件会影响名誉和权利，当前材料不能授权公开判断 | 只可作为内部模板压力测试 |

## 证据台账摘记

| evidence_id | 来源类型 | directness | independence | verifiability | 不能证明什么 | diagnostic_force |
| --- | --- | --- | --- | --- | --- | --- |
| ev-pub-001 | 公开公告摘要 | direct | same_source_family | partly_verifiable | 不能证明申诉机制有效 | moderate |
| ev-pub-002 | 公告对比 | direct | related | partly_verifiable | 不能证明处置依据充分 | moderate |
| ev-pub-003 | 公开评论抽样 | indirect | related | partly_verifiable | 不能代表全部受影响者 | weak |

## 构念剖面

| construct_id | 当前读数 | 支撑材料 | 反向条件 | 是否需要校准修订 |
| --- | --- | --- | --- | --- |
| low_power_counterexample_entry | 1 | 没有申诉、复核、纠错路径说明 | 平台公开有效复核机制和纠错数据 | 是 |
| observation_reflexivity_risk | 3 | 舆论压力明显影响公告细节 | 新材料显示回应与公共压力无关 | 否 |
| action_ceiling_clarity | 0 | 当前材料会诱导公共判断越权 | 公开来源、复核数据和被影响方反馈齐备 | 是 |

## 机制候选更新

| mechanism_id | 机制候选 | 支持材料 | 反例压力 | update_direction | 撤回条件 |
| --- | --- | --- | --- | --- | --- |
| mech-pub-visible-response | 平台补充处置细节主要回应可见压力 | 两次公告与公开评论时间关系 | 真实时间线缺失 | pending | 规则修订早于舆论压力且可核验 |
| mech-pub-closed-review | 申诉和复核不透明导致制度承接不足 | 公告未说明申诉复核边界 | 缺内部依据 | strengthen | 平台公开纠错路径和透明数据 |

## 判断档位与行动上限

- judgment_grade：open_assertion
- action_ceiling：block_publication
- 不能升级的原因：权力闸 fail、行动闸 blocked，且真实事件缺源链接、时间线、申诉数据和被影响方反馈。
- 可撤回的小动作：只作为内部公共制度模板试跑；真实公共事件必须先补源和反例入口。

## 评分者原始记录

### rater_a

| gate | gate_state | score | 理由 |
| --- | --- | --- | --- |
| 对象闸 | pass | 3 | 对象限定为回应与制度承接 |
| 证据闸 | weak | 2 | 公告材料不足以支持公开判断 |
| 尺度闸 | pass | 3 | 平台治理尺度清楚 |
| 责任闸 | weak | 2 | 内部处置依据缺失 |
| 观测闸 | weak | 2 | 公开争议影响平台回应 |
| 权力闸 | fail | 1 | 低权力申诉入口缺失 |
| 行动闸 | blocked | 0 | 公开判断会影响权利和名誉 |

- judgment_grade: open_assertion
- action_ceiling: block_publication
- evidence_gap: 申诉数据、被影响方反馈、规则版本时间线
- counterexample_pressure: strong

### rater_b

| gate | gate_state | score | 理由 |
| --- | --- | --- | --- |
| 对象闸 | pass | 3 | 对象边界可用 |
| 证据闸 | weak | 2 | 公告对比可做低强度判断 |
| 尺度闸 | pass | 3 | 没有明显尺度偷换 |
| 责任闸 | weak | 2 | 责任链可初步定位 |
| 观测闸 | weak | 2 | 反身风险存在 |
| 权力闸 | weak | 2 | 可以先写边界声明 |
| 行动闸 | weak | 2 | 可在强边界下发布抽象评论 |

- judgment_grade: open_assertion
- action_ceiling: publish_with_boundary
- evidence_gap: 真实来源链接、被影响方反馈
- counterexample_pressure: moderate

## 反例压力与撤回条件

- 已发现反例：如果平台随后公开复核机制、数据和纠错路径，机制链应改写为承接中的治理修复。
- 仍缺失的反例入口：被处置用户反馈、申诉材料、外部监督记录。
- 哪些新材料会撤回判断：争议事实被证伪，或平台在争议前已有可核验复核机制。
- 哪些新材料会降级行动上限：评论抽样来自单一来源族或公告摘要无法核验。

## 写回结果

- downgrade_triggered：true
- anchor_revision_required：true
- template_revision_required：false
- 写回到哪个锚点、模板、checker 或文本边界：公共争议 trial 要求将 `low_power_counterexample_entry <= 1` 与 `action_ceiling: block_publication` 绑定，除非补足申诉和复核材料。

## 本案例不能证明

本案例不能证明平台治理失败，不能证明处置错误，不能证明用户群体意见一致，也不能授权真实公共事件发布。它只能暴露 v6 公共场景需要更硬的低权力反例入口锚点。
