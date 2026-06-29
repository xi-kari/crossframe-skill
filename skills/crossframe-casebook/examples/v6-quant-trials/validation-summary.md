# v6 案例库验证摘要：第一轮 shakedown

本摘要只记录第一轮 v6 半量化案例试跑暴露的问题。它不能支持外部有效性、现实正确性、方法优越性或可处置性结论。

## 试跑覆盖

| trial | domain | status | judgment_grade | action_ceiling | 主要暴露 |
| --- | --- | --- | --- | --- | --- |
| organization-case-trial.md | organization | formal | full_diagnosis | internal_review | 责任链可用，但管理层决策记录和低权力反例入口不足 |
| relationship-case-trial.md | relationship | formal | open_assertion | ask_for_evidence | 低成本同源材料必须限制在开放断言 |
| public-dispute-case-trial.md | public_dispute | formal | open_assertion | block_publication | 公共争议缺申诉复核材料时必须阻断发布 |
| misuse-counterexample-trial.md | misuse_counterexample | counterexample | open_assertion | block_publication | 尺度升维误用必须触发降档和模板写回 |

## 降档与写回

- `public-dispute-case-trial.md` 触发降档：低权力反例入口不足，公共发布边界阻断。
- `public-dispute-case-trial.md` 要求锚点修订：`low_power_counterexample_entry <= 1` 时，默认不能发布真实公共判断。
- `misuse-counterexample-trial.md` 触发降档、锚点修订和模板修订：尺度闸 fail 且低尺度痛苦被高尺度叙事稀释时，行动上限必须阻断或回到补证。

## 评分者一致性发现

- 组织 trial 中两个评分者对责任闸存在 1 分差异，但 judgment_grade 和 action_ceiling 相同。
- 公共争议 trial 中两个评分者对权力闸、行动闸和 action_ceiling 有实质分歧。
- `rater-disagreement-sample.md` 保留了未合并分歧：A 要求阻断发布，B 认为可带边界发布抽象评论。
- 处理决定：不要求评分者收敛；先修订公共争议锚点和模板。

## 模板修订建议

- 公共争议 trial 必须单列申诉、复核、纠错路径和被影响方反馈。
- 误用 trial 必须检查是否存在高尺度叙事压低低尺度痛苦。
- 关系 trial 必须显式写出“材料来自单方时不能升级”的边界。
- 组织 trial 必须把“谁能改变条件”和“谁承担返工成本”分开登记。

## 下一轮补证

- 为公共争议案例增加真实来源链模拟材料，但仍保持脱敏。
- 为关系案例增加双方视角的对照样本。
- 为组织案例增加变更审批链样本。
- 为误用案例增加安全风险分支，确认何时需要退出 CrossFrame 结构判断并转向现实支持。
