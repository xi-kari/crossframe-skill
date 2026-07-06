# Structured Max Ledgers

These JSON ledgers are mandatory for completed `crossframe-max` artifacts. Markdown sections remain required, but final validation must also inspect structured ledgers.

`max-claim-board.json` and `max-audit-board.json` are phase-lock ledgers. `max-claim-ledger.json` is the final claim ledger; it must be consistent with the claim board and audit board.

## max-claim-ledger.json

```json
{
  "claims": [
    {
      "claim_id": "CL1",
      "claim": "Current strongest structural judgment...",
      "claim_type": "fact_path | mechanism_candidate | low_confidence_thought_experiment | counterfactual_path | value_explanation",
      "design_decision_id": "DD1",
      "v6_rule_ids": ["工具准入", "过程性产物边界"],
      "source_paragraph_ids": ["P0901", "P1451"],
      "concept_ids": ["结构域", "行动承接层"],
      "source_anchor": "user-material-1",
      "evidence_status": "full | partial | missing",
      "counterevidence_status": "searched | not_triggered | missing",
      "downgrade_condition": "If X appears, downgrade to mechanism candidate.",
      "withdrawal_condition": "If Y appears, withdraw this claim.",
      "action_limit": "What this claim may and may not authorize."
    }
  ]
}
```

## max-concept-hit-ledger.json

```json
{
  "concept_hits": [
    {
      "concept_id": "反馈写回",
      "hit_type": "direct | neighbor | conflict | gap",
      "trigger_variable": "bad news cannot change rule or role",
      "registry_anchor": "concept-registry/index.md",
      "source_ranges_from_registry": ["P0917-P0918"],
      "source_ranges_read": ["P0917-P0918", "P1461-P1463"],
      "source_paragraph_ids": ["P0917", "P1461"],
      "contract_id": "v6-core-contracts.md#反馈写回",
      "contract_checked": true,
      "downgraded_after_source_read": false,
      "notes": "Why this concept is or is not active."
    }
  ]
}
```

## max-evidence-reasoning-audit.json

```json
{
  "audits": [
    {
      "claim_id": "CL1",
      "design_decision_id": "DD1",
      "source_paragraph_ids": ["P0901", "P1451"],
      "evidence_chain": ["user-material-1", "P0901", "external-source-1"],
      "reasoning_chain": [
        "material -> structural variable",
        "structural variable -> concept hit",
        "concept hit -> mechanism judgment",
        "mechanism judgment -> path confidence"
      ],
      "counterevidence": ["counter-source-1"],
      "counterevidence_status": "searched",
      "calibration_rounds": [
        {
          "round": 1,
          "result": "kept | split | downgraded | withdrawn | pending_evidence",
          "reason": "Why the judgment changed or stayed."
        }
      ],
      "final_strength": "fact_path | mechanism_candidate | low_confidence_thought_experiment | counterfactual_path | value_explanation | undecidable",
      "withdrawal_condition": "If the source anchor or route concept fails, withdraw this claim.",
      "final_output_allowed": true
    }
  ]
}
```

Required rules:

- Every final claim must first appear in `max-claim-board.json`.
- Every final audit must first appear in `max-audit-board.json`.
- Red-team may change claim status, but has no final text authority.
- Allowed claim statuses are `candidate`, `supported`, `downgraded`, `split`, `withdrawn`, `needs_search`, `unexhaustible`, and `final`.
- Every final strong claim must have `source_paragraph_ids`.
- Every final audit must have non-empty `source_paragraph_ids`.
- Source paragraph ids must exist in the v6 full-source files.
- Every final strong claim must have `counterevidence_status`.
- Every final strong claim must have `downgrade_condition` and `withdrawal_condition`.
- Every skill or runtime design claim must have `design_decision_id`, `v6_rule_ids`, `source_anchor`, `action_limit`, `counterevidence`, and `withdrawal_condition`.
- Every concept hit must have `registry_anchor`, `trigger_variable`, `source_ranges_from_registry`, `source_ranges_read`, and `contract_id`.
- If `final_output_allowed` is not true, the claim cannot enter final conclusion.
