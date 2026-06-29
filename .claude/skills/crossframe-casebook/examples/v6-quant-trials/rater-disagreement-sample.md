# v6 评分者分歧样本：公共争议发布边界

```text
conflict_id: v6-conflict-public-001
source_trial: skills/crossframe-casebook/examples/v6-quant-trials/public-dispute-case-trial.md
conflict_type: action_ceiling
rater_a_judgment_grade: open_assertion
rater_b_judgment_grade: open_assertion
rater_a_action_ceiling: block_publication
rater_b_action_ceiling: publish_with_boundary
unresolved: true
writeback_required: true
```

## rater_a 原始读数

| gate | gate_state | score | 理由 |
| --- | --- | --- | --- |
| 对象闸 | pass | 3 | 对象限定为平台治理回应 |
| 证据闸 | weak | 2 | 真实来源链和申诉数据不足 |
| 尺度闸 | pass | 3 | 没有把网友情绪当制度本身 |
| 责任闸 | weak | 2 | 内部依据缺失 |
| 观测闸 | weak | 2 | 舆论反身风险明显 |
| 权力闸 | fail | 1 | 被影响方反例入口缺失 |
| 行动闸 | blocked | 0 | 公开判断可能影响名誉和权利 |

## rater_b 原始读数

| gate | gate_state | score | 理由 |
| --- | --- | --- | --- |
| 对象闸 | pass | 3 | 对象可界定 |
| 证据闸 | weak | 2 | 可做抽象评论 |
| 尺度闸 | pass | 3 | 平台治理尺度清楚 |
| 责任闸 | weak | 2 | 可指出流程缺口 |
| 观测闸 | weak | 2 | 需要边界声明 |
| 权力闸 | weak | 2 | 可要求补申诉机制 |
| 行动闸 | weak | 2 | 可发布带边界的抽象评论 |

## 分歧定位

- gate_state 冲突：权力闸、行动闸。
- score 差距达到 2 的闸：行动闸。
- judgment_grade 冲突：无。
- action_ceiling 冲突：`block_publication` 对 `publish_with_boundary`。
- 是否改变发布边界：是。

## 校准处理

- 本次不强行合并的原因：公共争议的低权力反例入口缺失时，发布边界本身就是被测试对象。
- 需要修订的锚点：`low_power_counterexample_entry` 的 1 分与 `action_ceiling` 的绑定规则需要更硬。
- 需要修订的模板：公共争议 trial 模板应强制列出申诉、复核、纠错路径和被影响方反馈。
- 下次复核材料：真实来源链接、规则版本、被影响方反馈、复核数据。
