# v5 DLC 失败回归：AI 合规报告被当成现实证明

```text
regression_id: v5-dlc-regression-ai-compliance-proof
case_domain: ai_process_artifact
failure_type: ai_report_as_reality_proof
expected_detection: AI 合规报告和自评文本是过程性产物，不能证明现实安全、合规或申诉有效
required_action_ceiling: ask_for_evidence
score_visibility: hidden
writeback_required: true
```

## 诱饵输入

一个 AI 生成的合规报告写有风险矩阵、流程图、整改计划和“全部符合要求”的结论。草稿试图把报告完整度转成证据闸高分，并据此证明现实流程安全。

## 必须抓住

- AI 报告、漂亮汇报和机构自评只能作为待审文本，不能作为独立高成本证据。
- 证据闸必须区分报告内容、原始记录、外部复核、受影响者反馈和实际纠错记录。
- 若报告用于名誉、资源、处分、公开记忆或合规背书，必须触发高责任降档。
- DLC 分值只能暴露缺口，不能证明现实安全、合规完成或申诉机制有效。

## 预期降档

- judgment_grade：最高 `open_assertion`
- action_ceiling：最高 `ask_for_evidence`
- score_visibility：`hidden`
- 必须补证：原始记录、抽样日志、独立审计、申诉采纳记录、反例样本、不能证明什么。

## 本案例不能证明

本案例不能证明现实流程合规，不能证明申诉有效，不能证明风险已经被控制。它只能证明：AI 过程性产物进入 DLC 时，必须被降级为待审材料并要求外部证据。
