# max-phase-lock phase artifacts

`crossframe-max` 完整运行必须生成以下阶段锁产物。所有字段按本模板登记。

## max-run-contract.json

```json
{
  "contract_version": "v2",
  "run_id": "run-001",
  "run_mode": "max-artifact-run | max-complete | max-design-review | max-blocked/progress",
  "execution_state": "pending | running | blocked | finished",
  "artifact_state": "absent | partial | core_complete | strict_complete",
  "validation_state": "not_run | failed | passed",
  "target_profile": "artifact-run | complete | design-review | blocked",
  "incomplete_reasons": ["registered-reason"],
  "blocked_reason": null,
  "final_output_allowed": true,
  "forbidden_behavior": [
    "claim max-complete before a fresh complete report"
  ],
  "affected_phase_reset_rule": "fatal contradiction returns to the nearest affected phase",
  "phase_exception_rule": "later phases record exceptions without altering locked artifacts",
  "completed_read_state": ["source inventory recorded"],
  "resume_entry": null
}
```

## max-read-plan.json

```json
{
  "phase": "read-plan",
  "route_key": "history_analysis | framework_self_review | skill_design | document_question | ...",
  "route_map_version": "v6.0",
  "route_required_layers": ["01-guide.md", "02-boundary-layer.md", "05-interface-layer.md"],
  "route_required_concepts": ["工具准入", "过程性产物边界"],
  "route_required_outputs": ["max-local-world-model", "max-concept-graph"],
  "route_forbidden_outputs_checked": [
    {
      "forbidden_output": "把 prompt 当作概念本体",
      "checked": true,
      "present": false
    }
  ],
  "priority_layers": ["03-world-layer.md"],
  "required_full_source_files": [
    "00-source-envelope.md",
    "01-guide.md",
    "02-boundary-layer.md",
    "03-world-layer.md",
    "04-state-layer.md",
    "05-interface-layer.md",
    "06-tool-layer.md",
    "07-intervention-layer.md",
    "08-application-layer.md",
    "09-governance-layer.md"
  ],
  "concept_triggers": [
    {
      "concept_id": "行动承接层",
      "expected_source_ranges": ["P0901-P0920"]
    }
  ],
  "external_retrieval_decision": "mandatory | optional | skipped",
  "final_full_source_required": true
}
```

## max-source-snapshot.json

```json
{
  "phase": "source-snapshot",
  "source_snapshot_id": "source_snapshot_001",
  "source_sha256": "d3f3c666ef0d4f6d0a3a0517ae98acbbeeaa7143abd82927ee06fa39e5d80499",
  "total_paragraphs": 3273,
  "full_source_exhaustive_pass": true,
  "covered_range": ["P0001", "P3273"],
  "table_count": 60,
  "source_anchor_verification_only_after_freeze": true,
  "frozen": true
}
```

## max-worldview-capsule.locked.md

```markdown
# max-worldview-capsule.locked

locked: true
source_snapshot_id: source_snapshot_001

## 本轮预先设计的世界观

## 八层结构启动核

## 核心概念启动核

## A1-A10 / R1-R6 边界

## 强判断边界

## 开放性承担行动边界

## 低权力主体保护

## 反模型殖民 / 反领域殖民

## worldview_exception_record
```

## max-local-world-model.locked.md

```markdown
# max-local-world-model.locked

locked: true
source_snapshot_id: source_snapshot_001

## 对象边界

## 尺度层级

## 主体位置

## 承接链

## 反馈通道

## 运行规律候选

## 判断边界

本文件只建模，不下最终判断。
```

## max-claim-board.json

```json
{
  "phase": "claim-board",
  "allowed_statuses": [
    "candidate",
    "supported",
    "downgraded",
    "split",
    "withdrawn",
    "needs_search",
    "unexhaustible",
    "final"
  ],
  "claims": [
    {
      "claim_id": "CL1",
      "status": "candidate",
      "claim": "...",
      "source_paragraph_ids": ["P0901", "P1450"],
      "concept_ids": ["行动承接层", "反馈写回"],
      "needs_evidence": true,
      "needs_counterevidence": true,
      "allowed_next_statuses": ["supported", "downgraded", "split", "withdrawn", "needs_search", "unexhaustible"]
    }
  ]
}
```

## max-audit-board.json

```json
{
  "phase": "audit-board",
  "audits": [
    {
      "claim_id": "CL1",
      "audit_result": "downgrade",
      "reason": "source supports mechanism candidate, not strong judgment",
      "required_change": "从强判断降为开放断言",
      "source_paragraph_ids": ["P0901", "P1450"],
      "counterevidence_status": "searched",
      "final_status": "downgraded"
    }
  ],
  "red_team_final_text_authority": false
}
```

## max-output-plan.locked.md

```markdown
# max-output-plan.locked

locked: true
source_snapshot_id: source_snapshot_001

## 进入正文的 claim

CL1

## 降档表达的 claim

CL2

## 撤回的 claim

CL4

## 进入不可判断区的 claim

CL6

## 不可写强的句子

## 必须保留的撤回条件

## final essay permission

`max-output-plan.locked.md` exists; `max-essay.md may now be written` from this plan only.
```

## State Table

```text
candidate -> supported -> final
candidate -> downgraded
candidate -> split
candidate -> withdrawn
candidate -> needs_search
candidate -> unexhaustible
supported -> downgraded / split / withdrawn / final
needs_search -> supported / downgraded / withdrawn / unexhaustible
```
