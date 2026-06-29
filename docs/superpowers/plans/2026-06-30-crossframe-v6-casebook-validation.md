# CrossFrame v6 Casebook Validation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development for independent rater drafts when available, then use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the first v6.0 casebook validation layer: run 4 old cases through the half-quantification foundation, preserve raw rater disagreement, force at least one downgrade or writeback from a counterexample, and add a local checker that prevents the validation package from becoming a success-rate or reliability claim.

**Architecture:** Treat the casebook as a failure-discovery instrument. Trial records live in `skills/crossframe-casebook/` because they are reusable cases; they reference v6 worksheets and schemas under `skills/crossframe/` without copying the whole quantification system. Markdown remains the main review surface. A small Python checker enforces required fields, anti-total-score language, domain coverage, downgrade/writeback evidence, and rater-disagreement preservation.

**Tech Stack:** Markdown, simple front-matter markers parsed with Python standard library, existing v6 JSON schema validator, existing CrossFrame integrity scripts.

---

## Scope Split

This plan implements Phase 3 from `docs/superpowers/specs/2026-06-30-crossframe-v6-quantification-design.md`.

This plan does not create the final v6.0 DOCX, does not publish the framework, does not claim empirical reliability, and does not replace real investigation or affected-position feedback. It only validates whether the v6 half-quantification templates can expose downgrade pressure, missing evidence, disagreement, and misuse risk across a small case set.

## Source Cases

Use these existing cases as the first trial set:

- `skills/crossframe-casebook/examples/organization-case.md` for organization repair and responsibility-chain pressure.
- `skills/crossframe-casebook/examples/relationship-case.md` for intimate-relationship and explanation-labor pressure.
- `skills/crossframe-casebook/examples/public-dispute-case.md` for public dispute, platform governance, and high-responsibility publication boundary.
- `skills/crossframe/examples/scale-transfer-misuse-case.md` for misuse and counterexample pressure.

The set intentionally covers relationship, organization, public institution/platform, and misuse/counterexample domains. It is too small for external validity and must be described as a protocol shakedown.

## File Structure

Create these files:

- `skills/crossframe-casebook/references/v6-casebook-validation-protocol.md` defines trial purpose, case selection rules, rater protocol, disagreement handling, downgrade triggers, and forbidden claims.
- `skills/crossframe-casebook/templates/v6-quant-case-trial-template.md` gives the reusable trial record format.
- `skills/crossframe-casebook/templates/v6-rater-disagreement-record-template.md` gives the raw rater disagreement format.
- `skills/crossframe-casebook/examples/v6-quant-trials/organization-case-trial.md` runs the organization case through v6.
- `skills/crossframe-casebook/examples/v6-quant-trials/relationship-case-trial.md` runs the relationship case through v6.
- `skills/crossframe-casebook/examples/v6-quant-trials/public-dispute-case-trial.md` runs the public dispute case through v6.
- `skills/crossframe-casebook/examples/v6-quant-trials/misuse-counterexample-trial.md` runs the misuse case through v6 and must force at least one downgrade, anchor revision, or template/checker revision.
- `skills/crossframe-casebook/examples/v6-quant-trials/rater-disagreement-sample.md` preserves an unreconciled A/B scoring difference and the follow-up calibration decision.
- `skills/crossframe-casebook/examples/v6-quant-trials/validation-summary.md` summarizes what failed, what was downgraded, and what must be revised before v6.0 publication.
- `scripts/check_v6_casebook_trials.py` checks the Phase 3 casebook validation layer.

Modify these files:

- `scripts/check_crossframe_skill_integrity.py` requires the new Phase 3 protocol, templates, examples, and checker in canonical repo roots.
- `.github/workflows/verify.yml` runs `python scripts/check_v6_casebook_trials.py --repo .`.
- `docs/QUICKSTART.md` adds the Phase 3 checker to local verification.
- `README.md` states that casebook validation is a failure-discovery shakedown, not proof of framework correctness.

Mirror created `skills/crossframe-casebook/` files into `.claude/skills/crossframe-casebook/` in the same commit. Do not update user-global mirrors in this implementation step; the existing `scripts/sync_skill_mirrors.py --check` gate is enough before release packaging.

## Trial Record Contract

Every trial Markdown file must include a simple marker block with one `key: value` per line:

```text
trial_id:
source_case:
case_domain:
trial_status:
primary_scale:
judgment_grade:
action_ceiling:
downgrade_triggered:
anchor_revision_required:
template_revision_required:
counterexample_pressure:
rater_record:
```

Allowed values:

```text
case_domain: relationship | organization | public_dispute | misuse_counterexample
trial_status: training | calibration | formal | counterexample
judgment_grade: light_observation | open_assertion | full_diagnosis | strong_judgment | low_condition_action | exit_transfer
action_ceiling: observe | ask_for_evidence | internal_review | publish_with_boundary | block_publication | exit_transfer
downgrade_triggered: true | false
anchor_revision_required: true | false
template_revision_required: true | false
counterexample_pressure: none | weak | moderate | strong | decisive
rater_record: none | embedded | separate
```

Forbidden markers or prose claims in valid trial files:

```text
total_score
overall_score
average_score
weighted_score
final_score
success_rate
reliability_proved
validated_framework
prediction_probability
casebook_coverage_proves
```

Chinese prose must also avoid claims equivalent to “案例库证明框架正确”, “一致性证明现实判断为真”, or “覆盖率证明外部有效性”.

## Rater Consistency Protocol

Use two independent rater drafts, `rater_a` and `rater_b`, for at least two formal trials.

Record raw disagreement before reconciliation:

- Per-gate `gate_state`.
- Per-gate `score`.
- Judgment grade.
- Action ceiling.
- Evidence gap list.
- Counterexample pressure.
- Short reason for each score that differs by 2 or more.

Compute only lightweight protocol-stability indicators:

- Exact gate-state agreement count.
- Maximum score delta.
- Count of gate-state conflicts.
- Count of action-ceiling conflicts.
- Whether conflict changed publication boundary or action ceiling.

Do not compute a total score, pass rate, framework reliability rate, or prediction accuracy. If consistency is weak, the action is anchor/template revision, not pressure on raters to converge.

## Task 1: Add Protocol and Templates

- [ ] Create `v6-casebook-validation-protocol.md` with sections for purpose, selection, source boundary, trial states, rater independence, disagreement preservation, downgrade/writeback triggers, privacy, and forbidden claims.
- [ ] Create `v6-quant-case-trial-template.md` with the marker block, source-case reference, seven-gate profile, evidence ledger notes, construct profile, judgment/action ceiling, counterexample pressure, downgrade decision, and writeback effects.
- [ ] Create `v6-rater-disagreement-record-template.md` with separate A/B raw readings and a reconciliation note that points to anchor/template revision when needed.

## Task 2: Create Four Trial Cases

- [ ] Create the organization trial from `organization-case.md` and require responsibility-chain and action-ceiling review.
- [ ] Create the relationship trial from `relationship-case.md` and require evidence-cost, low-power counterexample access, and non-pathologizing language review.
- [ ] Create the public dispute trial from `public-dispute-case.md` and require publication-boundary, public-pressure, and reversibility review.
- [ ] Create the misuse counterexample trial from `scale-transfer-misuse-case.md` and force at least one of:
  - `downgrade_triggered: true`
  - `anchor_revision_required: true`
  - `template_revision_required: true`
- [ ] In every trial, state what the case cannot prove and what evidence would withdraw or downgrade the judgment.

## Task 3: Preserve Rater Disagreement

- [ ] Add at least two rater A/B readings across the formal trial set.
- [ ] Add `rater-disagreement-sample.md` with one unresolved disagreement that changes either `judgment_grade` or `action_ceiling`.
- [ ] In `validation-summary.md`, report disagreement as a calibration finding, not as an error to hide.
- [ ] Require weak consistency to produce anchor/template revision recommendations.

## Task 4: Add Checker

- [ ] Implement `scripts/check_v6_casebook_trials.py` using only Python standard library.
- [ ] Check that all required protocol, template, summary, and trial files exist.
- [ ] Parse marker blocks from trial files and reject missing required keys or unknown normalized values.
- [ ] Require the four domains: `relationship`, `organization`, `public_dispute`, and `misuse_counterexample`.
- [ ] Require at least three formal or counterexample trial records.
- [ ] Require at least one trial with downgrade, anchor revision, or template revision.
- [ ] Require at least one rater-disagreement file and at least one action-ceiling or judgment-grade conflict.
- [ ] Reject forbidden score, success-rate, prediction, and reliability-proof language.
- [ ] Print concise file-specific errors and return non-zero on failure.

## Task 5: Wire Verification

- [ ] Add the checker to `.github/workflows/verify.yml`.
- [ ] Add Phase 3 file requirements to `scripts/check_crossframe_skill_integrity.py`.
- [ ] Update `docs/QUICKSTART.md` with the new checker command.
- [ ] Update `README.md` with a short Phase 3 description and anti-proof warning.
- [ ] Mirror new casebook files into `.claude/skills/crossframe-casebook/`.

## Acceptance Criteria

Run these commands from `E:\世界模型\skill\crossframe-skill`:

```powershell
$env:PYTHONPATH='work/pydeps'; python scripts/validate_v6_quantification_schema_fixtures.py --repo .
$env:PYTHONPATH='work/pydeps'; python scripts/validate_claim_ledger_schema_fixtures.py --repo .
python scripts/check_v6_casebook_trials.py --repo .
python scripts/check_crossframe_skill_integrity.py --repo . --mirror .claude/skills
python scripts/check_source_continuity.py --materials-only --repo .
python scripts/sync_skill_mirrors.py --repo . --check
Get-ChildItem scripts -Filter *.py | ForEach-Object { python -m py_compile $_.FullName }
bash -n scripts/install-codex.sh
git diff --check
```

Expected result:

- The four selected domains are represented.
- At least one counterexample or uncomfortable case causes a downgrade, anchor revision, or template/checker revision.
- Raw rater disagreement is visible in the repo.
- No file claims that casebook coverage, score agreement, or checker success proves real-world correctness.
- Existing v6 foundation, claim-ledger, integrity, source-continuity, mirror, compile, shell, and whitespace checks stay green.

## Review Notes

Use one independent review pass after implementation. The reviewer should look for semantic misuse rather than only script failures:

- Does any case quietly become a proof of framework correctness?
- Does any score authorize action without evidence and boundary review?
- Does disagreement get hidden by reconciliation prose?
- Does the public-dispute trial allow public pressure where low-power counterexample access is absent?
- Does the counterexample trial actually write back into an anchor, template, checker, or judgment downgrade?
