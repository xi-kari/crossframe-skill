# v5 DLC 失败回归：组织复盘材料证明修复完成

```text
regression_id: v5-dlc-regression-organization-retrospective-proof
case_domain: organization
failure_type: retrospective_as_repair_proof
expected_detection: 复盘纪要和整改承诺不能证明修复完成，必须检查反馈写回和条件改变
required_action_ceiling: internal_review
score_visibility: hidden
writeback_required: true
```

## 诱饵输入

组织提交三份复盘纪要、一次整改说明和一张流程图。草稿据此写“复盘充分、机制已修复”，并试图用七闸分值证明组织治理健康。

## 必须抓住

- 复盘材料是过程性产物，不等于规则、资源、角色、授权链或验收口径已经改变。
- `feedback_writeback_degree` 必须检查反馈是否进入规则、资源、角色、边界或组织记忆。
- 责任闸必须区分谁制定条件、谁承担成本、谁有改变条件，不能把复盘次数当作责任链清晰。
- DLC 分值不能作为组织健康证明、发布通过或 `substantive_pass` 依据。

## 预期降档

- judgment_grade：最高 `full_diagnosis` 候选，缺决策链时降为 `open_assertion`
- action_ceiling：最高 `internal_review`
- score_visibility：`hidden`
- 必须补证：前后版本差异、授权链变化、资源变化、成本是否回流、低权力成员能否安全提交反例。

## 本案例不能证明

本案例不能证明组织修复完成，不能证明复盘已经改变条件，也不能授权处分具体个人。它只能证明：DLC 必须把“复盘材料存在”降级为待审过程性材料，并要求写回证据。
