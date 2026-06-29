# CrossFrame v6 Quantification Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the first testable v6.0 half-quantification foundation: schemas, fixtures, Markdown worksheets, guardrail validation, and integrity-check wiring.

**Architecture:** Keep v6.0 quantification as a bounded audit layer inside `skills/crossframe/`, not a new scoring product. JSON schemas define allowed structured records, Markdown worksheets keep the Chinese semantic contract visible, and a validator rejects total-score keys, missing withdrawal conditions, missing action ceilings, and strong-judgment records without source ledgers. Existing CrossFrame integrity checks remain the outer gate.

**Tech Stack:** Markdown, JSON Schema draft 2020-12, Python 3 with `jsonschema`, existing CrossFrame scripts and skill layout.

---

## Scope Split

This plan implements Phase 2 from `docs/superpowers/specs/2026-06-30-crossframe-v6-quantification-design.md`.

This plan does not implement casebook trial runs, the final v6.0 publication document, DOCX generation, public site copy, or release packaging. Those need separate plans after this foundation is green.

## File Structure

Create these files:

- `skills/crossframe/references/construct-map-v6.md` defines the first v6 construct set and forbidden merges.
- `skills/crossframe/worksheets/seven-gates-quant-rubric.md` is the user-facing seven-gate half-quantification worksheet.
- `skills/crossframe/worksheets/evidence-ledger-v6.md` extends the evidence ledger with v6 fields.
- `skills/crossframe/worksheets/calibration-anchor-card.md` defines calibration cards.
- `skills/crossframe/worksheets/mechanism-update-rules.md` extends mechanism candidates with update direction.
- `skills/crossframe/worksheets/counterexample-register.md` records counterexamples and writeback effects.
- `skills/crossframe/schemas/seven-gates-quant.schema.json` validates seven-gate records.
- `skills/crossframe/schemas/evidence-ledger-v6.schema.json` validates v6 evidence-ledger records.
- `skills/crossframe/schemas/calibration-anchor.schema.json` validates construct anchor cards.
- `skills/crossframe/schemas/mechanism-update.schema.json` validates mechanism-edge updates.
- `skills/crossframe/schemas/counterexample-register.schema.json` validates counterexample records.
- `skills/crossframe/schemas/fixtures/v6/<schema-id>/valid-*.json` and `invalid-*.json` prove every schema gate.
- `scripts/validate_v6_quantification_schema_fixtures.py` validates every v6 schema fixture and applies cross-schema semantic guardrails.

Modify these files:

- `scripts/check_crossframe_skill_integrity.py` adds a `check_v6_quantification_foundation()` function and calls it from `check_root()`.
- `docs/QUICKSTART.md` adds the v6 validator command to local verification.
- `README.md` mentions the v6 quantification foundation as a guarded internal audit layer, not a scoring system.

Do not modify `skills/crossframe/SKILL.md` in this phase. The installable runtime should only route to these files after templates and review behavior have been tested.

## Normalized Vocabulary

Use these exact normalized values across schemas:

```text
gate_state: pass | weak | fail | blocked
score: 0 | 1 | 2 | 3 | 4
judgment_grade: light_observation | open_assertion | full_diagnosis | strong_judgment | low_condition_action | exit_transfer
publish_boundary: internal_only | publishable_with_boundary | blocked
evidence_cost: low | medium | high
directness: direct | indirect | background
independence: independent | related | same_source_family
verifiability: verifiable | partly_verifiable | not_verifiable
counterevidence_status: searched | partial | missing | unsafe_to_collect
diagnostic_force: weak | moderate | strong | decisive_candidate
update_direction: strengthen | weaken | neutral | pending | withdraw
counterexample_type: minor | repeated | high_harm | systemic | misuse | unrecoverable
```

Forbidden keys anywhere in valid v6 fixtures:

```text
total_score
overall_score
average_score
weighted_score
final_score
rank_score
prediction_probability
collapse_probability
health_score
personality_score
```

## Task 1: Add V6 Fixture Validator

**Files:**
- Create: `scripts/validate_v6_quantification_schema_fixtures.py`
- Test: `skills/crossframe/schemas/fixtures/v6/**`

- [ ] **Step 1: Run the missing validator to confirm the starting failure**

Run:

```powershell
python scripts/validate_v6_quantification_schema_fixtures.py --repo .
```

Expected: FAIL because `scripts/validate_v6_quantification_schema_fixtures.py` does not exist.

- [ ] **Step 2: Create the validator**

Add this full file:

```python
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


FORBIDDEN_SCORE_KEYS = {
    "total_score",
    "overall_score",
    "average_score",
    "weighted_score",
    "final_score",
    "rank_score",
    "prediction_probability",
    "collapse_probability",
    "health_score",
    "personality_score",
}


@dataclass(frozen=True)
class SchemaTarget:
    schema_id: str
    schema_path: Path
    fixture_dir: Path


TARGETS = [
    SchemaTarget(
        "seven-gates-quant",
        Path("skills/crossframe/schemas/seven-gates-quant.schema.json"),
        Path("skills/crossframe/schemas/fixtures/v6/seven-gates-quant"),
    ),
    SchemaTarget(
        "evidence-ledger-v6",
        Path("skills/crossframe/schemas/evidence-ledger-v6.schema.json"),
        Path("skills/crossframe/schemas/fixtures/v6/evidence-ledger-v6"),
    ),
    SchemaTarget(
        "calibration-anchor",
        Path("skills/crossframe/schemas/calibration-anchor.schema.json"),
        Path("skills/crossframe/schemas/fixtures/v6/calibration-anchor"),
    ),
    SchemaTarget(
        "mechanism-update",
        Path("skills/crossframe/schemas/mechanism-update.schema.json"),
        Path("skills/crossframe/schemas/fixtures/v6/mechanism-update"),
    ),
    SchemaTarget(
        "counterexample-register",
        Path("skills/crossframe/schemas/counterexample-register.schema.json"),
        Path("skills/crossframe/schemas/fixtures/v6/counterexample-register"),
    ),
]


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def walk_dicts(value: Any) -> list[dict[str, Any]]:
    found: list[dict[str, Any]] = []
    if isinstance(value, dict):
        found.append(value)
        for child in value.values():
            found.extend(walk_dicts(child))
    elif isinstance(value, list):
        for child in value:
            found.extend(walk_dicts(child))
    return found


def semantic_errors(instance: Any) -> list[str]:
    errors: list[str] = []
    for item in walk_dicts(instance):
        forbidden = FORBIDDEN_SCORE_KEYS.intersection(item)
        for key in sorted(forbidden):
            errors.append(f"forbidden totalizing score key: {key}")

        if item.get("judgment_grade") == "strong_judgment" and not item.get("source_ledger_id"):
            errors.append("strong_judgment requires source_ledger_id")

        if item.get("claim_id") and not item.get("withdrawal_condition"):
            errors.append(f"{item['claim_id']} missing withdrawal_condition")

        if item.get("claim_id") and not item.get("action_ceiling"):
            errors.append(f"{item['claim_id']} missing action_ceiling")

        if item.get("gate_state") in {"fail", "blocked"} and item.get("max_judgment_grade") == "strong_judgment":
            errors.append("failed or blocked gate cannot allow strong_judgment")

        if item.get("gate_id") == "power" and item.get("score", 0) < 3 and item.get("allows_public_pressure") is True:
            errors.append("power gate below 3 cannot allow public pressure")

    return errors


def validate_target(repo: Path, target: SchemaTarget) -> int:
    schema_path = repo / target.schema_path
    fixture_dir = repo / target.fixture_dir
    if not schema_path.exists():
        raise SystemExit(f"missing v6 schema: {schema_path}")
    if not fixture_dir.is_dir():
        raise SystemExit(f"missing v6 fixture directory: {fixture_dir}")

    schema = load_json(schema_path)
    validator = Draft202012Validator(schema)
    fixtures = sorted(fixture_dir.glob("*.json"))
    if not fixtures:
        raise SystemExit(f"missing v6 fixtures: {fixture_dir}")

    checked = 0
    for fixture in fixtures:
        instance = load_json(fixture)
        schema_errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.path))
        extra_errors = semantic_errors(instance)
        errors = [error.message for error in schema_errors] + extra_errors
        should_pass = fixture.name.startswith("valid-")
        should_fail = fixture.name.startswith("invalid-")

        if not should_pass and not should_fail:
            raise SystemExit(f"fixture name must start with valid- or invalid-: {fixture}")
        if should_pass and errors:
            details = "\n".join(f"- {message}" for message in errors)
            raise SystemExit(f"valid fixture failed v6 validation: {fixture.name}\n{details}")
        if should_fail and not errors:
            raise SystemExit(f"invalid fixture unexpectedly passed v6 validation: {fixture.name}")
        checked += 1

    print(f"ok: {target.schema_id} fixtures validated: {checked}")
    return checked


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate CrossFrame v6 quantification schema fixtures.")
    parser.add_argument("--repo", default=".", help="Repository root.")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    total = 0
    for target in TARGETS:
        total += validate_target(repo, target)
    print(f"ok: v6 quantification schema fixtures validated: {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 3: Run the validator to confirm expected missing schema failure**

Run:

```powershell
python scripts/validate_v6_quantification_schema_fixtures.py --repo .
```

Expected: FAIL with `missing v6 schema: ...seven-gates-quant.schema.json`.

- [ ] **Step 4: Commit the validator harness**

Run:

```powershell
git add scripts/validate_v6_quantification_schema_fixtures.py
git commit -m "test: add v6 quantification fixture validator"
```

## Task 2: Add Seven-Gates Quant Schema And Worksheet

**Files:**
- Create: `skills/crossframe/schemas/seven-gates-quant.schema.json`
- Create: `skills/crossframe/schemas/fixtures/v6/seven-gates-quant/valid-seven-gates-profile.json`
- Create: `skills/crossframe/schemas/fixtures/v6/seven-gates-quant/invalid-total-score.json`
- Create: `skills/crossframe/schemas/fixtures/v6/seven-gates-quant/invalid-fail-allows-strong.json`
- Create: `skills/crossframe/worksheets/seven-gates-quant-rubric.md`

- [ ] **Step 1: Create a schema with these exact gates**

The schema must require one object with `record_id`, `case_id`, `gates`, `max_judgment_grade`, `action_ceiling`, `withdrawal_condition`, and `publish_boundary`.

`gates` must contain exactly seven entries, one per `gate_id`:

```text
object
evidence
scale
responsibility
observation
power
action
```

Each gate entry must require `gate_id`, `gate_state`, `score`, `anchor_evidence`, `downgrade_reason`, `max_judgment_grade`, `action_ceiling`, and `withdrawal_condition`.

Set `additionalProperties` to `false` at the root object and every nested object. Do not permit any total-score or average-score field.

- [ ] **Step 2: Add valid fixture**

Use a fixture where evidence, scale, and power gates are `weak` or below, so the profile demonstrates that high scores do not combine into a total score. The valid fixture must include a clear `action_ceiling` and `withdrawal_condition` at root and per gate.

- [ ] **Step 3: Add invalid total-score fixture**

Add `invalid-total-score.json` with a root `total_score` key. Expected: the schema or semantic validator rejects it.

- [ ] **Step 4: Add invalid fail-allows-strong fixture**

Add `invalid-fail-allows-strong.json` with one gate set to `gate_state: fail` and `max_judgment_grade: strong_judgment`. Expected: semantic validator rejects it.

- [ ] **Step 5: Add the worksheet**

`seven-gates-quant-rubric.md` must include these headings:

```text
# 七闸半量化复核表
## 使用边界
## 通用锚点
## 对象闸
## 证据闸
## 尺度闸
## 责任闸
## 观测闸
## 权力闸
## 行动闸
## 强制降档规则
## 输出摘要
```

The worksheet must say that scores explain the gate state and cannot upgrade judgment grade by themselves.

- [ ] **Step 6: Run partial validation**

Run:

```powershell
python scripts/validate_v6_quantification_schema_fixtures.py --repo .
```

Expected: FAIL on the next missing schema, `evidence-ledger-v6.schema.json`.

- [ ] **Step 7: Commit seven-gates foundation**

Run:

```powershell
git add skills/crossframe/schemas/seven-gates-quant.schema.json skills/crossframe/schemas/fixtures/v6/seven-gates-quant skills/crossframe/worksheets/seven-gates-quant-rubric.md
git commit -m "feat: add v6 seven-gates quant schema"
```

## Task 3: Add Evidence Ledger V6 Schema And Worksheet

**Files:**
- Create: `skills/crossframe/schemas/evidence-ledger-v6.schema.json`
- Create: `skills/crossframe/schemas/fixtures/v6/evidence-ledger-v6/valid-evidence-ledger.json`
- Create: `skills/crossframe/schemas/fixtures/v6/evidence-ledger-v6/invalid-strong-without-source-ledger.json`
- Create: `skills/crossframe/schemas/fixtures/v6/evidence-ledger-v6/invalid-claim-without-withdrawal.json`
- Create: `skills/crossframe/worksheets/evidence-ledger-v6.md`

- [ ] **Step 1: Create a schema for evidence ledger records**

The root must require `ledger_id`, `case_id`, and `evidence_items`.

Each evidence item must require:

```text
evidence_id
source_id
claim_id
evidence_cost
directness
independence
verifiability
counterevidence_status
diagnostic_force
mechanism_edge
downgrade_reason
withdrawal_condition
action_ceiling
cannot_prove
```

If `judgment_grade` exists and equals `strong_judgment`, require `source_ledger_id`.

- [ ] **Step 2: Add valid fixture**

The valid fixture must include one low-cost AI/process artifact item and one medium or high-cost source item. The low-cost item must include `cannot_prove` explaining that it cannot prove real-world safety, repair, or completion.

- [ ] **Step 3: Add invalid strong-without-source-ledger fixture**

The invalid fixture must set `judgment_grade: strong_judgment` without `source_ledger_id`.

- [ ] **Step 4: Add invalid claim-without-withdrawal fixture**

The invalid fixture must include `claim_id` without `withdrawal_condition`.

- [ ] **Step 5: Add worksheet**

`evidence-ledger-v6.md` must include fields for evidence cost, directness, independence, verifiability, counterevidence status, diagnostic force, mechanism edge, downgrade reason, withdrawal trigger, action ceiling, and cannot-prove boundary.

- [ ] **Step 6: Run partial validation**

Run:

```powershell
python scripts/validate_v6_quantification_schema_fixtures.py --repo .
```

Expected: FAIL on the next missing schema, `calibration-anchor.schema.json`.

- [ ] **Step 7: Commit evidence ledger foundation**

Run:

```powershell
git add skills/crossframe/schemas/evidence-ledger-v6.schema.json skills/crossframe/schemas/fixtures/v6/evidence-ledger-v6 skills/crossframe/worksheets/evidence-ledger-v6.md
git commit -m "feat: add v6 evidence ledger schema"
```

## Task 4: Add Calibration Anchor Schema And Construct Map

**Files:**
- Create: `skills/crossframe/schemas/calibration-anchor.schema.json`
- Create: `skills/crossframe/schemas/fixtures/v6/calibration-anchor/valid-calibration-anchor.json`
- Create: `skills/crossframe/schemas/fixtures/v6/calibration-anchor/invalid-missing-misuse-risk.json`
- Create: `skills/crossframe/schemas/fixtures/v6/calibration-anchor/invalid-totalizing-construct.json`
- Create: `skills/crossframe/worksheets/calibration-anchor-card.md`
- Create: `skills/crossframe/references/construct-map-v6.md`

- [ ] **Step 1: Create calibration anchor schema**

The schema must require:

```text
construct_id
name_zh
definition
not_this
neighbor_concepts
anchors
minimum_evidence
high_responsibility_upgrade_conditions
misuse_risks
withdrawal_condition
v5_source_anchors
worksheets
schema_fields
```

`anchors` must require keys `0`, `1`, `2`, `3`, and `4`, each with a non-empty string.

- [ ] **Step 2: Add valid fixture**

Use `construct_id: low_power_counterexample_entry` and include an anchor 4 condition where low-power counterexamples can change judgment, action ceiling, tool behavior, and version writeback.

- [ ] **Step 3: Add invalid missing misuse risk fixture**

The invalid fixture must omit `misuse_risks`.

- [ ] **Step 4: Add invalid totalizing construct fixture**

The invalid fixture must include `overall_score` or `health_score` to prove totalizing keys are blocked.

- [ ] **Step 5: Add construct map reference**

`construct-map-v6.md` must include the first ten constructs from the design spec:

```text
object_boundary_clarity
evidence_support_degree
scale_consistency
responsibility_chain_traceability
observation_reflexivity_risk
low_power_counterexample_entry
action_ceiling_clarity
feedback_writeback_degree
repair_window_feasibility
counterexample_writeback_strength
```

For each construct, include source interface, real-world question, forbidden misuse, upgrade condition, observable signal, minimum evidence, withdrawal condition, and related worksheet.

- [ ] **Step 6: Add calibration worksheet**

`calibration-anchor-card.md` must include the field list from the design spec and explicitly say that anchors are set before scoring.

- [ ] **Step 7: Run partial validation**

Run:

```powershell
python scripts/validate_v6_quantification_schema_fixtures.py --repo .
```

Expected: FAIL on the next missing schema, `mechanism-update.schema.json`.

- [ ] **Step 8: Commit calibration foundation**

Run:

```powershell
git add skills/crossframe/schemas/calibration-anchor.schema.json skills/crossframe/schemas/fixtures/v6/calibration-anchor skills/crossframe/worksheets/calibration-anchor-card.md skills/crossframe/references/construct-map-v6.md
git commit -m "feat: add v6 calibration anchors"
```

## Task 5: Add Mechanism Update Schema And Worksheet

**Files:**
- Create: `skills/crossframe/schemas/mechanism-update.schema.json`
- Create: `skills/crossframe/schemas/fixtures/v6/mechanism-update/valid-mechanism-update.json`
- Create: `skills/crossframe/schemas/fixtures/v6/mechanism-update/invalid-withdraw-without-counterevidence.json`
- Create: `skills/crossframe/schemas/fixtures/v6/mechanism-update/invalid-strong-judgment-without-source-ledger.json`
- Create: `skills/crossframe/worksheets/mechanism-update-rules.md`

- [ ] **Step 1: Create mechanism update schema**

The schema must require:

```text
mechanism_id
mechanism_edge_id
description
supporting_facts
counterevidence
diagnostic_force
update_direction
current_state
can_explain
cannot_explain
observable_predictions
withdrawal_condition
claim_id
action_ceiling
```

If `update_direction` is `withdraw`, require at least one `counterevidence` item. If `judgment_grade` is `strong_judgment`, require `source_ledger_id`.

- [ ] **Step 2: Add valid fixture**

Use a feedback-writeback mechanism edge with `update_direction: weaken` and include `cannot_explain`.

- [ ] **Step 3: Add invalid withdraw-without-counterevidence fixture**

Set `update_direction: withdraw` and `counterevidence: []`.

- [ ] **Step 4: Add invalid strong-judgment-without-source-ledger fixture**

Set `judgment_grade: strong_judgment` without `source_ledger_id`.

- [ ] **Step 5: Add worksheet**

`mechanism-update-rules.md` must state that mechanism candidates do not receive total rankings or probability scores. It must include the five update directions and the rule that one evidence item only updates the mechanism edge it actually touches.

- [ ] **Step 6: Run partial validation**

Run:

```powershell
python scripts/validate_v6_quantification_schema_fixtures.py --repo .
```

Expected: FAIL on the next missing schema, `counterexample-register.schema.json`.

- [ ] **Step 7: Commit mechanism update foundation**

Run:

```powershell
git add skills/crossframe/schemas/mechanism-update.schema.json skills/crossframe/schemas/fixtures/v6/mechanism-update skills/crossframe/worksheets/mechanism-update-rules.md
git commit -m "feat: add v6 mechanism update schema"
```

## Task 6: Add Counterexample Register Schema And Worksheet

**Files:**
- Create: `skills/crossframe/schemas/counterexample-register.schema.json`
- Create: `skills/crossframe/schemas/fixtures/v6/counterexample-register/valid-counterexample-register.json`
- Create: `skills/crossframe/schemas/fixtures/v6/counterexample-register/invalid-missing-writeback.json`
- Create: `skills/crossframe/schemas/fixtures/v6/counterexample-register/invalid-misuse-without-action-change.json`
- Create: `skills/crossframe/worksheets/counterexample-register.md`

- [ ] **Step 1: Create counterexample register schema**

The schema must require:

```text
counterexample_id
related_claim_ids
related_construct_ids
related_mechanism_ids
source_id
counterexample_type
impact_scope
text_consequence
tool_consequence
action_ceiling_change
version_writeback
withdrawal_condition
```

If `counterexample_type` is `misuse` or `high_harm`, require non-empty `action_ceiling_change` and `tool_consequence`.

- [ ] **Step 2: Add valid fixture**

Use a misuse counterexample where an operator tries to use a seven-gate score as a disposition basis. The fixture must change action ceiling and tool consequence.

- [ ] **Step 3: Add invalid missing-writeback fixture**

Omit `version_writeback`.

- [ ] **Step 4: Add invalid misuse-without-action-change fixture**

Set `counterexample_type: misuse` and use an empty action ceiling change.

- [ ] **Step 5: Add worksheet**

`counterexample-register.md` must say counterexamples are governance events, not appendix notes. It must include minor, repeated, high_harm, systemic, misuse, and unrecoverable categories.

- [ ] **Step 6: Run full v6 validation**

Run:

```powershell
python scripts/validate_v6_quantification_schema_fixtures.py --repo .
```

Expected: PASS and print one `ok:` line for each schema target plus one total line.

- [ ] **Step 7: Commit counterexample foundation**

Run:

```powershell
git add skills/crossframe/schemas/counterexample-register.schema.json skills/crossframe/schemas/fixtures/v6/counterexample-register skills/crossframe/worksheets/counterexample-register.md
git commit -m "feat: add v6 counterexample register schema"
```

## Task 7: Wire V6 Foundation Into Existing Integrity Checks

**Files:**
- Modify: `scripts/check_crossframe_skill_integrity.py`
- Modify: `README.md`
- Modify: `docs/QUICKSTART.md`

- [ ] **Step 1: Add integrity function**

In `scripts/check_crossframe_skill_integrity.py`, add `check_v6_quantification_foundation(root: Path, label: str) -> None` after `check_claim_ledger()`.

The function must check:

```text
all five v6 schema files exist
all five v6 fixture directories exist
each schema contains "$schema", "additionalProperties", and its schema-specific title
all six v6 Markdown reference or worksheet files exist
seven-gates worksheet contains "分值只能解释状态来源"
evidence ledger worksheet contains "不能证明什么"
construct map contains all ten construct ids
mechanism update worksheet contains "不输出总排序"
counterexample register contains "治理事件"
validator script contains "FORBIDDEN_SCORE_KEYS", "strong_judgment requires source_ledger_id", and "valid-"
README says v6 quantification is not a total-score system
QUICKSTART mentions validate_v6_quantification_schema_fixtures.py
```

- [ ] **Step 2: Call the integrity function**

Call `check_v6_quantification_foundation(root, label)` inside `check_root()` immediately after `check_claim_ledger(root, label)`.

- [ ] **Step 3: Update README**

Add a concise note under the existing safety or workflow section:

```markdown
The v6 quantification foundation is an internal audit layer. It uses anchored rubrics, schema fixtures, and downgrade checks to expose uncertainty and action ceilings. It is not a total-score system, prediction model, certification system, or disposition tool.
```

- [ ] **Step 4: Update QUICKSTART verification**

Add this command next to the existing claim-ledger fixture validator:

```powershell
python scripts/validate_v6_quantification_schema_fixtures.py --repo .
```

- [ ] **Step 5: Run integrity checks**

Run:

```powershell
python scripts/check_crossframe_skill_integrity.py --repo .
```

Expected: PASS with `ok: crossframe skill integrity checks passed`.

- [ ] **Step 6: Commit integrity wiring**

Run:

```powershell
git add scripts/check_crossframe_skill_integrity.py README.md docs/QUICKSTART.md
git commit -m "chore: wire v6 quantification integrity checks"
```

## Task 8: Run Full Local Verification

**Files:**
- No source edits unless a verification failure points to a v6 file created by this plan.

- [ ] **Step 1: Validate existing claim-ledger fixtures**

Run:

```powershell
python scripts/validate_claim_ledger_schema_fixtures.py --repo .
```

Expected: PASS with `ok: claim ledger schema fixtures validated: 5`.

- [ ] **Step 2: Validate v6 fixtures**

Run:

```powershell
python scripts/validate_v6_quantification_schema_fixtures.py --repo .
```

Expected: PASS with one line for each v6 schema target and one total line.

- [ ] **Step 3: Run integrity gate**

Run:

```powershell
python scripts/check_crossframe_skill_integrity.py --repo .
```

Expected: PASS with `ok: crossframe skill integrity checks passed`.

- [ ] **Step 4: Run source continuity gate**

Run:

```powershell
python scripts/check_source_continuity.py --repo .
```

Expected: PASS. If it fails only because v6 files are not yet included in source-continuity rules, record the exact failure and add a small continuity mapping in the same implementation slice.

- [ ] **Step 5: Check mirror drift**

Run:

```powershell
python scripts/sync_skill_mirrors.py --repo . --check
```

Expected before mirror sync: FAIL if `.claude/skills` is behind. This is not a source failure after new canonical files are added.

- [ ] **Step 6: Sync the repository-local `.claude/skills` mirror**

Run:

```powershell
python scripts/sync_skill_mirrors.py --repo .
python scripts/sync_skill_mirrors.py --repo . --check
```

Expected: PASS with `ok: checked ...\.claude\skills`.

- [ ] **Step 7: Commit mirror sync**

Run:

```powershell
git add .claude/skills
git commit -m "chore: sync crossframe skill mirror"
```

## Task 9: Final Review Before Next Plan

**Files:**
- No source edits unless review finds a concrete defect in this phase.

- [ ] **Step 1: Search for forbidden placeholders**

Run:

```powershell
rg -n -e 'TB[D]' -e 'TO[D]O' -e 'FIX[M]E' -e '待[定]' -e '占[位]' -- skills/crossframe scripts docs README.md
```

Expected: no matches introduced by this phase.

- [ ] **Step 2: Search for total-score language in v6 files**

Run:

```powershell
rg -n -e 'total_score' -e 'overall_score' -e 'average_score' -e 'weighted_score' -e '总分' -e '综合分' -- skills/crossframe/schemas skills/crossframe/worksheets skills/crossframe/references/construct-map-v6.md
```

Expected: matches only in explicit forbidden-key lists or anti-misuse warnings.

- [ ] **Step 3: Inspect git status**

Run:

```powershell
git status --short --branch
```

Expected: clean worktree, ahead by the commits created in this plan.

- [ ] **Step 4: Write the next-plan note**

Add a short note to the final implementation report that the next separate plan should cover Phase 3: casebook validation with 3 to 5 old cases, including at least one uncomfortable or counterexample case.

## Self-Review

Spec coverage:

- Construct map: Task 4.
- Seven-gate quantification dimensions: Task 2.
- Evidence ledger extension: Task 3.
- Calibration anchors: Task 4.
- Mechanism candidate update: Task 5.
- Judgment grades and action ceilings: Tasks 2, 3, 5, and validator semantic checks.
- Counterexamples and withdrawal conditions: Tasks 1, 3, 5, and 6.
- Casebook validation: deliberately split into the next plan because it requires real case selection and scoring.
- Rater consistency checks: deliberately split into the casebook-validation plan because it depends on a scored case set.
- Anti-misuse governance: Tasks 1, 2, 6, and 7.
- Reusable tool prototype: Tasks 1 through 8 produce schema, fixtures, templates, and validator.

Placeholder scan:

- The plan contains no empty file names, open implementation fields, or unspecified validator behavior.
- Every file to create or modify has a concrete responsibility and verification command.

Type consistency:

- `gate_state`, `judgment_grade`, `publish_boundary`, evidence fields, update directions, and counterexample types are normalized once and reused across tasks.
- The validator semantic checks match the schema fields required by the tasks.
