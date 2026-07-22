# Red-team report 生成合同

产物：`promax-red-team-report.json`
生成阶段：`P7`
Schema：`promax-red-team-report.schema.json`

`schema_id` 固定为 `crossframe.promax.v8.red-team-report`，`schema_version=1`。根对象只包含 `schema_id`、`schema_version`、`run_id`、`source_snapshot_sha256`、`central_claim_id`、`attacks`、`stability_checks`、`revision_summary`、`completed_at`。

## 攻击集合

对中心 claim、对象边界、机制、路径、预测和建议前提进行最强攻击。至少实质检验下列十二个 `attack_class`，不可用同一句泛化质疑批量填充：

1. `object_reification`
2. `boundary_error`
3. `scale_transformation_error`
4. `personality_overinference`
5. `circle_reification`
6. `stage_model_misuse`
7. `baseline_leakage`
8. `path_storytelling`
9. `uncalibrated_probability`
10. `prediction_authorization_leakage`
11. `inaction_zero_cost`
12. `decision_irrelevant_counterexample`

## 每条 `attacks[]`

闭合字段为 `attack_id`、`attack_class`、`target_id`、`challenge`、`counterevidence_refs`、`strongest_counterposition`、`result`、`revision`、`position_impact`。

- `attack_id` 使用唯一 `ATTACK-*`；`target_id` 必须能回到 claim、机制、路径、对象或建议前提。
- `challenge` 提出能改变判断的具体攻击，不写表演性反对。
- `strongest_counterposition` 以完整命题表达最强反方；后续 position 必须逐字携带最高影响攻击的反方核心。
- `result` 只能是 `survived`、`survived_with_revision`、`rejected`、`unresolved`。
- `revision` 即使结果为 survived 也要说明保留理由或边界；`survived_with_revision` 的修正必须进入 position 的理由或撤回条件。
- `position_impact` 只能是 `none`、`low`、`medium`、`high`、`decisive`。

`revision_summary` 逐项汇总真正改变 claim、概念状态、强度、路径排序或行动上限的修正，并记录 red-team 连续两轮无实质新增的结果；不得用“已完成攻击”代替内容。

## 成对立场稳定性

每条 `stability_checks[]` 闭合字段为：`prompt_pair_id`、`pro_prompt_sha256`、`anti_prompt_sha256`、`evidence_before_sha256`、`evidence_after_sha256`、`central_position_id_before`、`central_position_id_after`、`judgment_strength_before`、`judgment_strength_after`、`option_ranking_before`、`option_ranking_after`、`position_drift`、`explanation`。

- `prompt_pair_id` 使用唯一 `PAIR-*`；正向与反向诱导的 prompt hashes 必须不同。
- 判断强度只能是 `tentative`、`moderate`、`strong`、`indeterminate`。
- 无新证据时，position ID、判断强度、方案排序必须前后一致，`position_drift=none`。
- 有新证据且冻结状态确实改变时才可用 `justified_by_evidence`；永远不得保留 `unjustified`。
- `central_position_id_after` 与 `judgment_strength_after` 必须成为 P8 locked position 的值。
- 若 run contract 不要求建议，前后 rankings 都必须为 `[]`；若要求建议，`option_ranking_after` 必须与 P8 recommendation 的完整 ranking 相等。
- `explanation` 必须说明证据与状态变化的对应关系，不得与登记状态矛盾。

`completed_at` 不得早于 claim graph 的 `updated_at`。封存后 P8 才能形成 position；不得让用户赞成或反对本身成为证据。
