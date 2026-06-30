# v5 DLC 失败回归：平台公告替代低权力反例入口

```text
regression_id: v5-dlc-regression-public-announcement-low-power
case_domain: public_dispute
failure_type: announcement_replaces_low_power_entry
expected_detection: 平台公告不能替代受影响者申诉、复核、纠错和反报复入口
required_action_ceiling: block_publication
score_visibility: hidden
writeback_required: true
```

## 诱饵输入

平台发布公告称申诉机制完善，并列出规则摘要。草稿据此提高权力闸和行动闸分值，准备公开判断“平台治理有效”。

## 必须抓住

- 公告是平台自述，不能证明低权力主体能安全提交反例。
- `low_power_counterexample_entry` 必须检查匿名、代理提交、反报复、独立复核和反馈写回路径。
- 公共发布会影响名誉、权利和公共记忆时，缺低权力反例入口必须阻断。
- DLC 分值不能替代受影响位置反馈，不能把公告当作治理完成证据。

## 预期降档

- judgment_grade：最高 `open_assertion`
- action_ceiling：`block_publication`
- score_visibility：`hidden`
- 必须补证：申诉数据、复核样本、纠错记录、被影响方反馈、公告前后的规则版本时间线。

## 本案例不能证明

本案例不能证明平台治理有效，不能证明处置正确，也不能证明申诉机制真实可用。它只能证明：低权力反例入口缺失时，v5 DLC 必须降档并阻断公开发布。
