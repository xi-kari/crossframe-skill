# Current CrossFrame Max Control Plane Repair Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restore a green, protected v6 CrossFrame Max baseline by giving runtime state, artifact profiles, templates, fixtures, documentation, validators, mirrors, and CI one consistent machine contract.

**Architecture:** Add one versioned run-contract schema plus a dependency-free schema evaluator, then make the artifact validator profile-aware (`artifact-run`, `complete`, `design-review`, `blocked`). Treat the run contract, validator report, and repair plan as control-plane sidecars outside the analysis-artifact manifest. Validation projects `passed` or `failed` into a new run-contract snapshot and report together; the report binds the resulting run-contract SHA256, profile, manifest SHA256, and every inventoried artifact SHA256. This gives `not_run -> passed|failed` a reachable transition without a manifest cycle and prevents blocked-report replay. Canonical templates and semantic fixtures become executable contracts; repository integrity and CI verify those contracts independently before a PR can merge.

**Tech Stack:** Python 3.11 standard library, JSON Schema draft 2020-12, `jsonschema` for schema fixture tests, `unittest`, Markdown templates, GitHub Actions, PowerShell/Git.

**Scope guard:** Do not add v7 theory/contracts, edit the v6 full source or route/concept corpus, redesign installers/releases, modify locally installed `$HOME/.codex` or `$HOME/.agents` skills, or touch the original checkout. Package and installer files may be executed for verification but are not implementation targets.

---

## File map

### New files

- `skills/crossframe-max/schemas/max-run-contract.schema.json` — canonical runtime state schema.
- `skills/crossframe-max/scripts/crossframe_max_runtime_contract.py` — installed-skill loader and cross-field validator.
- `scripts/crossframe_max_runtime_contract.py` — repository-side byte-identical executable copy.
- `skills/crossframe-max/templates/max-artifact-manifest-output.md` — canonical manifest contract.
- `skills/crossframe-max/templates/max-continuation-ledger-output.md` — canonical continuation-state contract.
- `skills/crossframe-max/templates/max-continuation-index-output.md` — canonical continuation-index contract.
- `tests/__init__.py` — unittest package marker.
- `scripts/crossframe_max_fixture_factory.py` — packaged semantic artifact-run, complete, design-review, and blocked fixture builder.
- `tests/test_max_run_contract.py` — run-state schema and cross-field tests.
- `tests/test_max_artifact_profiles.py` — artifact-run/complete/design/blocked profile tests.
- `tests/test_max_adversarial_profiles.py` — parameterized false-claim, manifest, ID, and semantic-thinness regressions.
- `tests/test_max_template_contract.py` — template/validator/fixture closure tests.
- `tests/test_max_repair_contract.py` — validator-report and repair-plan lifecycle tests.
- `tests/test_max_report_schema.py` — Draft 2020-12 gold/invalid report instance tests.
- `tests/test_max_status_docs.py` — public/runtime terminology consistency tests.
- `tests/test_mirror_integrity.py` — content-hash mirror and root/skill script parity tests.
- `tests/test_verify_workflow_contract.py` — independent CI job contract tests.

### Existing implementation files

- `scripts/check_crossframe_max_artifacts.py` and `skills/crossframe-max/scripts/check_crossframe_max_artifacts.py` — profile-aware artifact validation.
- `scripts/validate_crossframe_max_route_ledger_fixtures.py` — replace marker-only full fixture with semantic factory use and adversarial cases.
- `scripts/build_crossframe_max_repair_plan.py` — map structured profile failures to the new incomplete action and v2 repair plan.
- `scripts/validate_crossframe_max_repair_fixtures.py` — v2 validator/repair report fixtures.
- `scripts/check_crossframe_skill_integrity.py` — current-state markers, schema/template presence, root/skill parity.
- `scripts/sync_skill_mirrors.py` — content-hash equality instead of shallow comparison.
- `skills/crossframe-max/schemas/max-validator-report.schema.json` — add profile/run/final-label fields.
- `skills/crossframe-max/schemas/max-repair-plan.schema.json` — rename old incomplete fields/actions.
- `skills/crossframe-max/templates/max-dossier-output.md` — add the missing continuation-index section.
- `skills/crossframe-max/templates/max-phase-lock-output.md` — represent four run modes and orthogonal states.
- `skills/crossframe-max/templates/max-essay-output.md` — distinguish artifact-run status from complete claims.

### Existing semantic/document files

- `skills/crossframe-max/SKILL.md`
- `skills/crossframe-max/agents/openai.yaml`
- `skills/crossframe-max/protocols/max-worldview-protocol.md`
- `skills/crossframe-max/protocols/max-repair-loop-protocol.md`
- `skills/crossframe-max/evals/crossframe-max-smoke-tests.md`
- `README.md`
- `docs/QUICKSTART.md`
- `CHANGELOG.md`
- `.github/workflows/verify.yml`
- `.claude/skills/crossframe-max/**` — generated only via mirror synchronization after canonical edits.

## Task 1: Establish the canonical run-state contract

**Files:**

- Create: `tests/__init__.py`
- Create: `tests/test_max_run_contract.py`
- Create: `skills/crossframe-max/schemas/max-run-contract.schema.json`
- Create: `scripts/crossframe_max_runtime_contract.py`
- Create: `skills/crossframe-max/scripts/crossframe_max_runtime_contract.py`

- [ ] **Step 1: Write the failing run-contract tests**

Create `tests/test_max_run_contract.py` with these cases:

```python
from __future__ import annotations

import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from crossframe_max_runtime_contract import load_schema, validate_run_contract


def valid_contract(**overrides):
    contract = {
        "contract_version": "v2",
        "run_id": "run-001",
        "run_mode": "max-artifact-run",
        "execution_state": "finished",
        "artifact_state": "core_complete",
        "validation_state": "not_run",
        "target_profile": "artifact-run",
        "incomplete_reasons": ["full-source-exhaustive-pass-not-satisfied"],
        "blocked_reason": None,
        "final_output_allowed": True,
        "forbidden_behavior": ["claim max-complete without strict validation"],
        "affected_phase_reset_rule": "reset affected phase and downstream artifacts",
        "phase_exception_rule": "record phase_exception_record before reset",
        "completed_read_state": ["source inventory recorded"],
        "resume_entry": None,
    }
    contract.update(overrides)
    return contract


class MaxRunContractTests(unittest.TestCase):
    def test_schema_declares_only_current_modes(self):
        schema = load_schema(ROOT / "skills" / "crossframe-max")
        modes = schema["properties"]["run_mode"]["enum"]
        self.assertEqual(
            modes,
            ["max-artifact-run", "max-complete", "max-design-review", "max-blocked/progress"],
        )
        self.assertNotIn("max-incomplete/progress", json.dumps(schema, ensure_ascii=False))

    def test_honest_artifact_run_is_valid(self):
        self.assertEqual(validate_run_contract(valid_contract()), [])

    def test_complete_target_requires_strict_artifacts_but_not_a_predeclared_pass(self):
        errors = validate_run_contract(
            valid_contract(
                run_mode="max-complete",
                target_profile="complete",
                artifact_state="core_complete",
            )
        )
        self.assertTrue(any("strict_complete" in error for error in errors))
        self.assertEqual(
            validate_run_contract(
                valid_contract(
                    run_mode="max-complete",
                    target_profile="complete",
                    artifact_state="strict_complete",
                    incomplete_reasons=[],
                    validation_state="not_run",
                )
            ),
            [],
        )

    def test_blocked_mode_requires_a_real_blocker(self):
        errors = validate_run_contract(
            valid_contract(
                run_mode="max-blocked/progress",
                target_profile="blocked",
                execution_state="blocked",
                artifact_state="partial",
                final_output_allowed=False,
                blocked_reason=None,
                completed_read_state=[],
                resume_entry=None,
            )
        )
        self.assertTrue(any("blocked_reason" in error for error in errors))
        self.assertTrue(any("completed_read_state" in error for error in errors))
        self.assertTrue(any("resume_entry" in error for error in errors))

    def test_old_mode_is_rejected(self):
        errors = validate_run_contract(valid_contract(run_mode="max-incomplete/progress"))
        self.assertTrue(any("run_mode" in error for error in errors))

    def test_runtime_and_jsonschema_agree_on_validity(self):
        from jsonschema import Draft202012Validator

        schema = load_schema(ROOT / "skills" / "crossframe-max")
        samples = [
            valid_contract(),
            valid_contract(extra_field=True),
            valid_contract(run_id=""),
            valid_contract(final_output_allowed="yes"),
            valid_contract(incomplete_reasons=["duplicate", "duplicate"]),
            valid_contract(run_mode="max-artifact-run", target_profile="complete"),
        ]
        reference = Draft202012Validator(schema)
        for sample in samples:
            self.assertEqual(
                bool(list(reference.iter_errors(sample))),
                bool(validate_run_contract(sample)),
            )


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the test and confirm the missing module failure**

Run:

```powershell
python -B -m unittest tests.test_max_run_contract -v
```

Expected: FAIL with `ModuleNotFoundError: No module named 'crossframe_max_runtime_contract'`.

- [ ] **Step 3: Add the canonical JSON Schema**

Create `skills/crossframe-max/schemas/max-run-contract.schema.json` with draft 2020-12 and `additionalProperties: false`. Require every field in `valid_contract()`. Define `contract_version` as `const: v2`; define `run_id`, `affected_phase_reset_rule`, and `phase_exception_rule` as non-empty strings; define `final_output_allowed` as boolean; define `forbidden_behavior`, `completed_read_state`, and `incomplete_reasons` as unique arrays of non-empty strings; and define `blocked_reason` and `resume_entry` as string-or-null. Use these enums:

```json
{
  "run_mode": ["max-artifact-run", "max-complete", "max-design-review", "max-blocked/progress"],
  "execution_state": ["pending", "running", "blocked", "finished"],
  "artifact_state": ["absent", "partial", "core_complete", "strict_complete"],
  "validation_state": ["not_run", "failed", "passed"],
  "target_profile": ["artifact-run", "complete", "design-review", "blocked"]
}
```

Add these exact conditional rules in `allOf`:

- each `run_mode` implies its matching `target_profile`;
- `run_mode=max-complete` implies `execution_state=finished` and `artifact_state=strict_complete`, but it does **not** imply a predeclared `validation_state=passed`;
- `execution_state=blocked` implies `run_mode=max-blocked/progress`, `target_profile=blocked`, non-empty `blocked_reason`, at least one `completed_read_state` entry, non-empty `resume_entry`, and `final_output_allowed=false`;
- non-blocked execution requires both `blocked_reason` and `resume_entry` to be null;
- finished non-blocked execution requires `final_output_allowed=true`; the final artifact validator never reuses the old pre-output-lock rule that required false;
- `artifact_state=strict_complete` requires an empty `incomplete_reasons` array;
- finished non-strict artifacts require at least one `incomplete_reasons` entry.

The schema describes every run-contract snapshot across the lifecycle. New or repaired artifacts start at `validation_state=not_run`; the validator materializes the only legal transition to `passed` or `failed`. A pre-existing `passed` snapshot is accepted by artifact validation only when a fresh report binds its exact run-contract SHA256 and current artifact manifest.

- [ ] **Step 4: Implement the dependency-free runtime-contract loader**

Create identical root and skill copies of `crossframe_max_runtime_contract.py` with these public functions and exact cross-field rules:

```python
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def default_skill_root(script_path: Path | None = None) -> Path:
    path = (script_path or Path(__file__)).resolve()
    candidate = path.parent.parent
    if (candidate / "SKILL.md").is_file():
        return candidate
    return candidate / "skills" / "crossframe-max"


def load_schema(skill_root: Path | None = None) -> dict[str, Any]:
    root = (skill_root or default_skill_root()).resolve()
    return json.loads((root / "schemas" / "max-run-contract.schema.json").read_text(encoding="utf-8"))


def validate_schema_instance(instance: object, schema: dict[str, Any], path: str = "$") -> list[str]:
    """Evaluate the exact schema subset used by max-run-contract without third-party imports."""
    errors: list[str] = []

    def matches_type(value: object, expected: str) -> bool:
        return {
            "object": isinstance(value, dict),
            "array": isinstance(value, list),
            "string": isinstance(value, str),
            "boolean": isinstance(value, bool),
            "null": value is None,
            "integer": isinstance(value, int) and not isinstance(value, bool),
            "number": isinstance(value, (int, float)) and not isinstance(value, bool),
        }[expected]

    expected_type = schema.get("type")
    if expected_type is not None:
        accepted = [expected_type] if isinstance(expected_type, str) else expected_type
        if not any(matches_type(instance, item) for item in accepted):
            return [f"{path}: expected type {accepted}"]
    if "const" in schema and instance != schema["const"]:
        errors.append(f"{path}: expected const {schema['const']!r}")
    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{path}: value is not in enum")

    if isinstance(instance, dict):
        properties = schema.get("properties", {})
        for field in schema.get("required", []):
            if field not in instance:
                errors.append(f"{path}: missing {field}")
        if schema.get("additionalProperties") is False:
            for field in sorted(set(instance) - set(properties)):
                errors.append(f"{path}.{field}: additional property is forbidden")
        for field, child_schema in properties.items():
            if field in instance:
                errors.extend(validate_schema_instance(instance[field], child_schema, f"{path}.{field}"))

    if isinstance(instance, str) and len(instance) < schema.get("minLength", 0):
        errors.append(f"{path}: shorter than minLength")
    if isinstance(instance, list):
        if len(instance) < schema.get("minItems", 0):
            errors.append(f"{path}: fewer than minItems")
        if "maxItems" in schema and len(instance) > schema["maxItems"]:
            errors.append(f"{path}: more than maxItems")
        if schema.get("uniqueItems"):
            normalized = [json.dumps(item, ensure_ascii=False, sort_keys=True) for item in instance]
            if len(normalized) != len(set(normalized)):
                errors.append(f"{path}: items must be unique")
        if "items" in schema:
            for index, item in enumerate(instance):
                errors.extend(validate_schema_instance(item, schema["items"], f"{path}[{index}]"))

    for child_schema in schema.get("allOf", []):
        errors.extend(validate_schema_instance(instance, child_schema, path))
    if "anyOf" in schema and not any(
        not validate_schema_instance(instance, child_schema, path)
        for child_schema in schema["anyOf"]
    ):
        errors.append(f"{path}: no anyOf branch matched")
    if "if" in schema:
        branch = "then" if not validate_schema_instance(instance, schema["if"], path) else "else"
        if branch in schema:
            errors.extend(validate_schema_instance(instance, schema[branch], path))
    return errors


def validate_run_contract(data: object, skill_root: Path | None = None) -> list[str]:
    schema = load_schema(skill_root)
    return [
        f"max-run-contract.json {error}"
        for error in validate_schema_instance(data, schema)
    ]
```

Use this implementation in both copies. Unknown schema keywords such as `$schema`, `$id`, `title`, and `description` are intentionally ignored. Do not duplicate the mode/profile or blocked rules in Python; the JSON Schema remains the single rule source.

- [ ] **Step 5: Run the contract tests**

```powershell
python -m pip install jsonschema
python -B -m unittest tests.test_max_run_contract -v
```

Expected: 6 tests, all PASS, including parity with `jsonschema` on every invalid sample.

- [ ] **Step 6: Commit the run contract**

```powershell
git add tests skills/crossframe-max/schemas/max-run-contract.schema.json scripts/crossframe_max_runtime_contract.py skills/crossframe-max/scripts/crossframe_max_runtime_contract.py
git commit -m "feat: define crossframe max runtime states"
```

## Task 2: Make artifact validation profile-aware

**Files:**

- Create: `scripts/crossframe_max_fixture_factory.py`
- Create: `tests/test_max_artifact_profiles.py`
- Modify: `scripts/check_crossframe_max_artifacts.py:17-255,510-755,863-935`
- Modify: `skills/crossframe-max/scripts/check_crossframe_max_artifacts.py`
- Modify: `scripts/validate_crossframe_max_route_ledger_fixtures.py:360-375`

- [ ] **Step 1: Write failing profile tests**

Create packaged fixture helpers `write_artifact_run_fixture(path)`, `write_complete_fixture(path)`, `write_design_review_fixture(path)`, and `write_blocked_fixture(path)` in `scripts/crossframe_max_fixture_factory.py`. Tests add `ROOT/scripts` to `sys.path` before importing them.

Also expose `complete_run_contract(run_id="complete-001") -> dict[str, object]` so the existing route fixture can adopt the v2 object without copying its fields.

- Artifact-run writes the run contract plus the five core Markdown files, uses `core_complete`, omits the four strict ledgers, and declares `full-source-exhaustive-pass-not-satisfied`.
- Complete writes all existing strict phase and ledger artifacts, but its input contract uses `artifact_state=strict_complete` and `validation_state=not_run`; it never predeclares a validator pass.
- Design-review writes the five core artifacts plus the `skill_design` read-plan, concept-hit, claim, evidence/audit, and output-plan artifacts needed to prove a design decision's v6 rules, counterevidence, withdrawal condition, and action limit.
- Blocked writes only a valid blocked run contract with `completed_read_state` and `resume_entry`; it deliberately omits the five long-form artifacts.

Every non-blocked fixture writes the manifest last. Its fenced `manifest-contract` JSON inventories every analysis/phase artifact except the manifest itself and the three control-plane sidecars (`max-run-contract.json`, `max-validator-report.json`, `max-repair-plan.json`); each entry contains `path` and lowercase SHA256. The run contract is hashed separately by the validator report.

Create these tests:

```python
class MaxArtifactProfileTests(unittest.TestCase):
    def test_honest_artifact_run_passes_artifact_profile(self):
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_artifact_run_fixture(workspace)
            self.assertEqual(check_crossframe_max_artifacts(workspace, profile="artifact-run"), [])

    def test_honest_artifact_run_fails_complete_profile(self):
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_artifact_run_fixture(workspace)
            errors = check_crossframe_max_artifacts(workspace, profile="complete")
            self.assertTrue(any("missing structured ledger" in error for error in errors))

    def test_complete_profile_rejects_partial_source(self):
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_complete_fixture(workspace)
            snapshot = json.loads((workspace / "max-source-snapshot.json").read_text(encoding="utf-8"))
            snapshot["full_source_exhaustive_pass"] = False
            (workspace / "max-source-snapshot.json").write_text(json.dumps(snapshot), encoding="utf-8")
            errors = check_crossframe_max_artifacts(workspace, profile="complete")
            self.assertTrue(any("full_source_exhaustive_pass" in error for error in errors))

    def test_artifact_run_cannot_claim_max_complete(self):
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_artifact_run_fixture(workspace)
            manifest = workspace / "max-artifact-manifest.md"
            manifest.write_text(manifest.read_text(encoding="utf-8") + "\n交付状态：max-complete\n", encoding="utf-8")
            errors = check_crossframe_max_artifacts(workspace, profile="artifact-run")
            self.assertTrue(any("false max-complete claim" in error for error in errors))

    def test_skill_design_review_requires_design_route_closure(self):
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_design_review_fixture(workspace)
            self.assertEqual(check_crossframe_max_artifacts(workspace, profile="design-review"), [])
            read_plan = json.loads((workspace / "max-read-plan.json").read_text(encoding="utf-8"))
            read_plan["route_key"] = "default"
            (workspace / "max-read-plan.json").write_text(json.dumps(read_plan), encoding="utf-8")
            errors = check_crossframe_max_artifacts(workspace, profile="design-review")
            self.assertTrue(any("skill_design" in error for error in errors))

    def test_blocked_profile_does_not_require_longform_artifacts(self):
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_blocked_fixture(workspace)
            self.assertEqual(check_crossframe_max_artifacts(workspace, profile="blocked"), [])
            self.assertFalse((workspace / "max-dossier.md").exists())
```

- [ ] **Step 2: Run the tests and verify the missing `profile` argument failure**

Run: `python -B -m unittest tests.test_max_artifact_profiles -v`

Expected: FAIL because `check_crossframe_max_artifacts()` does not accept `profile`.

- [ ] **Step 3: Split strict and core requirements**

In both validator copies:

- Rename current marker collections to `COMPLETE_*`.
- Add explicit `ARTIFACT_RUN_*` collections containing only core artifact, template, state, claim/source honesty, and continuation markers.
- Add `VALIDATION_PROFILES = ("artifact-run", "complete", "design-review", "blocked")`.
- Add `load_run_contract(workspace, skill_root, errors)` and call `validate_run_contract()` from Task 1.
- Change the public signature to:

```python
def check_crossframe_max_artifacts(
    workspace: Path,
    skill_root: Path | None = None,
    profile: str | None = None,
) -> list[str]:
```

Apply the same optional `profile` parameter to `check_crossframe_max_artifacts_structured()` and pass it through to the string validator before classification.

Infer the profile from `max-run-contract.json.target_profile` when omitted. A CLI `--profile` value overrides inference only when it agrees with the run contract; disagreement is an error.

- [ ] **Step 4: Add profile branches without weakening complete**

Implement this control flow:

```python
contract = load_run_contract(workspace, resolved_skill_root, errors)
active_profile = resolve_profile(profile, contract, errors)
if active_profile == "blocked":
    check_blocked_record_only(contract, workspace, errors)
    check_no_completion_claim_in_present_text(workspace, errors)
    return errors

core = read_and_check_core_artifacts(workspace, active_profile, errors)
manifest = check_manifest_inventory(workspace, contract, errors)
check_run_state_consistency(contract, active_profile, core.visible_text, errors)

if active_profile == "artifact-run":
    require_declared_strict_gaps(contract, errors)
    check_optional_ledgers_when_present(workspace, resolved_skill_root, errors)
elif active_profile == "design-review":
    require_skill_design_route_artifacts(workspace, errors)
    errors.extend(check_route_ledgers(workspace, resolved_skill_root))
    check_design_decision_closure(workspace, errors)
elif active_profile == "complete":
    check_phase_lock_artifacts(workspace, errors, strict=True)
    require_all_structured_ledgers(workspace, errors)
    errors.extend(check_structured_ledgers(workspace, resolved_skill_root))
    errors.extend(check_route_ledgers(workspace, resolved_skill_root))
```

Implement the named helpers exactly as routed above. `check_blocked_record_only()` requires a real blocker, at least one completed-read-state entry, a resume entry, and no completion claim, but it must not call the core/phase/long-form readers. `check_design_decision_closure()` requires `route_key=skill_design`, a design decision ID, v6 rule IDs, counterevidence, withdrawal condition, and action limit. Keep the existing 3273/3273 and four-ledger requirements unchanged inside the complete branch.

Refactor `check_phase_lock_artifacts()` so a finished non-blocked run requires `final_output_allowed=true` together with the locked output-plan authorization. Remove the old final-validator assertion that the flag must remain false before output lock; that pre-lock state belongs to generation, not final artifact validation.

Detect false completion claims through explicit delivery assertions (`delivery_label=max-complete`, `交付状态：max-complete`, or equivalent completed-sentence markers), not by rejecting the machine value `run_mode=max-complete` inside the run contract. The mode is a target; the delivery label is a validator result.

- [ ] **Step 5: Add profile-aware CLI and report fields**

Add `--profile` with the four choices and introduce `build_validation_result(workspace, errors, *, profile, contract, manifest)`. After all checks finish, copy the input contract and project `validation_state=passed` when the structured error list is empty or `failed` otherwise. Serialize the projected contract deterministically with `json.dumps(projected_contract, ensure_ascii=False, sort_keys=True, indent=2) + "\n"`, hash those exact bytes, and build report v2 with `run_id`, `profile`, `run_mode`, `execution_state`, `artifact_state`, `incomplete_reasons`, `input_validation_state`, computed `validation_state`, `run_contract_sha256`, `manifest_sha256`, `artifact_sha256`, `passed`, and `final_label`.

For non-blocked profiles, the artifact hash map must equal the manifest inventory and the manifest digest must be recomputed from bytes on disk. A valid blocked record has no manifest, so its report uses `manifest_sha256=null` and `artifact_sha256={}`, but it still binds the projected blocked contract through `run_contract_sha256`.

Use this total final-label mapping:

| Profile/result | Exact final label |
| --- | --- |
| artifact-run passed with incomplete reasons | `max-artifact-incomplete:` plus the first registered reason |
| artifact-run passed without incomplete reasons | `max-artifact-run-valid` |
| complete passed | `max-complete` |
| design-review passed | `max-design-review` |
| blocked passed | `max-blocked/progress` |
| any profile failed | `max-validation-failed:` plus profile, `:`, and the first structured `error_type` |

Add `write_validation_result()` for `--write-report`. It writes projected contract bytes and report JSON to sibling temporary files, then uses `os.replace()` to replace `max-run-contract.json` followed by `max-validator-report.json`. A crash between replacements is safe because freshness will fail. A pre-existing `validation_state=passed` is accepted only when the existing report's `run_contract_sha256`, `run_id`, profile, manifest SHA256, and artifact hashes all match; otherwise emit `stale_or_false_validation_claim`.

Enforce these persisted-state transitions: `not_run -> passed|failed`, fresh `passed -> passed`, `passed -> failed`, and `failed -> failed`. Reject `failed -> passed` by synthesizing `invalid_validation_transition` and keeping the projected state failed. A repair must explicitly reset the contract to `not_run` before a later pass.

- [ ] **Step 6: Run profile and legacy fixture tests**

Before running them, replace the legacy complete fixture's old `crossframe-v6-max`/`max_run_level` object with `complete_run_contract()` imported from `crossframe_max_fixture_factory`. This is a compatibility edit only; Task 3 subsequently moves the remaining artifact construction into the packaged semantic factory.

```powershell
python -B -m unittest tests.test_max_artifact_profiles -v
python -B scripts/validate_crossframe_max_route_ledger_fixtures.py
python -B scripts/validate_crossframe_max_repair_fixtures.py
```

Expected: every command PASS. Do not commit a checkpoint that leaves an existing fixture command red.

- [ ] **Step 7: Commit profile-aware validation**

```powershell
git add scripts/crossframe_max_fixture_factory.py tests/test_max_artifact_profiles.py scripts/check_crossframe_max_artifacts.py skills/crossframe-max/scripts/check_crossframe_max_artifacts.py scripts/validate_crossframe_max_route_ledger_fixtures.py
git commit -m "feat: validate max artifact profiles separately"
```

## Task 3: Make templates and semantic fixtures executable contracts

**Files:**

- Create: `tests/test_max_template_contract.py`
- Create: `tests/test_max_adversarial_profiles.py`
- Create: `skills/crossframe-max/templates/max-artifact-manifest-output.md`
- Create: `skills/crossframe-max/templates/max-continuation-ledger-output.md`
- Create: `skills/crossframe-max/templates/max-continuation-index-output.md`
- Modify: `skills/crossframe-max/templates/max-dossier-output.md:406-419`
- Modify: `skills/crossframe-max/templates/max-phase-lock-output.md:1-110`
- Modify: `skills/crossframe-max/templates/max-essay-output.md`
- Modify: `scripts/crossframe_max_fixture_factory.py`
- Modify: `scripts/check_crossframe_max_artifacts.py`
- Modify: `skills/crossframe-max/scripts/check_crossframe_max_artifacts.py`
- Modify: `scripts/validate_crossframe_max_route_ledger_fixtures.py:302-570`

- [ ] **Step 1: Write failing template-contract tests**

Add tests that:

```python
def markdown_headings(path: Path) -> list[str]:
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.startswith("## ")]


def test_dossier_template_contains_every_validator_heading(self):
    template = ROOT / "skills/crossframe-max/templates/max-dossier-output.md"
    self.assertEqual(markdown_headings(template), REQUIRED_DOSSIER_HEADINGS)


def test_every_core_artifact_has_a_template(self):
    expected = {
        "max-dossier-output.md",
        "max-essay-output.md",
        "max-artifact-manifest-output.md",
        "max-continuation-ledger-output.md",
        "max-continuation-index-output.md",
    }
    self.assertTrue(expected.issubset({p.name for p in TEMPLATE_ROOT.glob("*.md")}))


def test_marker_only_fixture_fails(self):
    with tempfile.TemporaryDirectory() as td:
        workspace = Path(td)
        write_marker_only_fixture(workspace)
        errors = check_crossframe_max_artifacts(workspace, profile="artifact-run")
        self.assertTrue(any("marker-only" in error or "section too thin" in error for error in errors))
```

Create `tests/test_max_adversarial_profiles.py` as a parameterized structured-error regression. Expose `rewrite_manifest(workspace)` from the fixture factory. For every case, build a fresh gold fixture, apply exactly one mutation, call `rewrite_manifest()` unless the case is specifically `stale manifest`, then call `check_crossframe_max_artifacts_structured()` and assert the expected `error_type` is present while `manifest_state_mismatch` is absent. This keeps semantic regressions single-variable instead of letting a stale hash mask them:

| Case | Exact mutation | Expected error type |
| --- | --- | --- |
| retired mode | set `run_mode=max-incomplete/progress` | `runtime_state_conflict` |
| false final | set `final_output_allowed=false` and append `max-complete` to essay | `false_complete_claim` |
| premature evidence | add `needs_evidence=true` to a final claim referenced by essay | `premature_final_claim` |
| marker-only | replace dossier sections with headings plus validator marker strings | `artifact_semantic_thinness` |
| missing heading | delete `## max-continuation-index` from dossier | `missing_template_heading` |
| forbidden bypass | quote a forbidden output beside `present=false` in final Markdown | `forbidden_output_present` |
| stale manifest | change one essay byte after manifest creation and deliberately do not call `rewrite_manifest()` | `manifest_state_mismatch` |
| mixed profile | validate an artifact-run contract with CLI profile `complete` | `profile_mismatch` |
| fake pass | write a passed report with the wrong manifest SHA256 and set input state to `passed` | `stale_or_false_validation_claim` |
| duplicate IDs | duplicate a claim ID and duplicate a source paragraph ID inside one claim | `duplicate_identifier` |
| broken backref | change the audit's claim ID so it no longer resolves | `cross_reference_mismatch` |

For the design-review gold fixture, add separate mutations removing `counterevidence`, `withdrawal_condition`, and `action_limit`; call `rewrite_manifest()` after each mutation, and require `design_review_closure_failed` without `manifest_state_mismatch`. This list is the minimum adversarial set and may not be replaced by marker-presence assertions.

- [ ] **Step 2: Verify the current template mismatch**

Run: `python -B -m unittest tests.test_max_template_contract -v`

Expected: FAIL because the dossier lacks a `## max-continuation-index` heading and three core templates do not exist.

- [ ] **Step 3: Complete the canonical templates**

- Add a real final `## max-continuation-index` section to the dossier template with next entry, undeveloped paths, omitted positions, material queue, counterexamples, no-repeat, and no-overreach fields.
- Create the three missing core templates with explicit `run_id`, `run_mode`, `execution_state`, `artifact_state`, input `validation_state`, and `incomplete_reasons` fields.
- In the manifest template, add a fenced `manifest-contract` JSON block containing `manifest_version=v2`, `run_id`, and an `artifacts` array of `{path, sha256}` objects. Exclude the manifest itself and all three control-plane sidecars (`max-run-contract.json`, `max-validator-report.json`, `max-repair-plan.json`) so validation-state materialization cannot form an inventory cycle.
- Replace the phase template's old `max_run_level` union with the v2 run-contract fields.
- In the essay template, use `delivery_label=pending-validator`; forbid embedding `max-complete` in a pre-validation artifact. The final user-facing label comes only from the fresh validator report.

- [ ] **Step 4: Replace marker construction with semantic fixture construction**

Refactor `scripts/crossframe_max_fixture_factory.py` so it parses headings from `skills/crossframe-max/templates/max-dossier-output.md` rather than importing validator marker constants. Construct each section with section-specific prose of at least 64 visible characters. Use unique claim/source references, compute real SHA256 values, and write the manifest after every inventoried file. Implement `rewrite_manifest(workspace)` with the same inventory policy for adversarial tests and repair simulation. Because this factory is imported by packaged repository scripts, it must use only the standard library and paths relative to the supplied repository/skill root.

Refactor `write_full_artifact_fixture()` in `validate_crossframe_max_route_ledger_fixtures.py` to import the semantic factory instead of constructing dossier and essay text from `marker_blob(REQUIRED_DOSSIER_MARKERS + REQUIRED_FULL_SOURCE_FILES)` and `marker_blob(REQUIRED_ESSAY_MARKERS)`. Correct the complete fixture to use:

```json
{
  "contract_version": "v2",
  "run_id": "complete-001",
  "run_mode": "max-complete",
  "execution_state": "finished",
  "artifact_state": "strict_complete",
  "validation_state": "not_run",
  "target_profile": "complete",
  "incomplete_reasons": [],
  "blocked_reason": null,
  "final_output_allowed": true,
  "forbidden_behavior": ["claim max-complete before a fresh report"],
  "affected_phase_reset_rule": "reset affected phase and downstream artifacts",
  "phase_exception_rule": "record phase_exception_record before reset",
  "completed_read_state": ["3273/3273 source pass recorded"],
  "resume_entry": null
}
```

The pre-audit claim board must use `status=candidate`; the final claim ledger and audit board may use `supported` only after evidence and counterevidence fields are populated.

- [ ] **Step 5: Close the forbidden-output bypass**

Remove the special case that ignores a forbidden phrase merely because the line contains `present=false`. Store forbidden-output audit results as identifiers in JSON rather than quoting the forbidden sentence in final Markdown. Add the existing `forbidden-output-present-false` case as a required failure.

Implement the semantic, duplicate-ID, cross-reference, manifest-freshness, premature-evidence, false-final, and design-review closure checks needed by the adversarial table. Extend `classify_message()` in both validator copies so every table row returns its exact named `error_type`; Task 4 then adds those names to the report schema enum.

- [ ] **Step 6: Run template and fixture tests**

```powershell
python -B -m unittest tests.test_max_template_contract tests.test_max_artifact_profiles -v
python -B -m unittest tests.test_max_adversarial_profiles -v
python -B scripts/validate_crossframe_max_route_ledger_fixtures.py
```

Expected: all PASS, including marker-only rejection and `present=false` rejection.

- [ ] **Step 7: Commit executable template contracts**

```powershell
git add tests scripts/crossframe_max_fixture_factory.py scripts/check_crossframe_max_artifacts.py skills/crossframe-max/scripts/check_crossframe_max_artifacts.py skills/crossframe-max/templates scripts/validate_crossframe_max_route_ledger_fixtures.py
git commit -m "test: bind max fixtures to canonical templates"
```

## Task 4: Align validator reports and repair lifecycle

**Files:**

- Create: `tests/test_max_repair_contract.py`
- Create: `tests/test_max_report_schema.py`
- Modify: `skills/crossframe-max/schemas/max-validator-report.schema.json`
- Modify: `skills/crossframe-max/schemas/max-repair-plan.schema.json`
- Modify: `scripts/check_crossframe_max_artifacts.py`
- Modify: `skills/crossframe-max/scripts/check_crossframe_max_artifacts.py`
- Modify: `scripts/build_crossframe_max_repair_plan.py`
- Modify: `skills/crossframe-max/scripts/build_crossframe_max_repair_plan.py`
- Modify: `scripts/validate_crossframe_max_repair_fixtures.py`
- Modify: `skills/crossframe-max/protocols/max-repair-loop-protocol.md`

- [ ] **Step 1: Write failing report/repair tests**

Test these invariants:

```python
def test_artifact_run_report_records_profile_and_incomplete_label(self):
    projected_contract, report = build_validation_result(
        workspace,
        [],
        profile="artifact-run",
        contract=contract,
        manifest=read_manifest_contract(workspace),
    )
    self.assertEqual(report["report_version"], "v2")
    self.assertEqual(report["profile"], "artifact-run")
    self.assertEqual(report["input_validation_state"], "not_run")
    self.assertEqual(report["validation_state"], "passed")
    self.assertEqual(projected_contract["validation_state"], "passed")
    self.assertEqual(report["final_label"], "max-artifact-incomplete:full-source-exhaustive-pass-not-satisfied")


def test_complete_report_cannot_pass_with_incomplete_contract(self):
    projected_contract, report = build_validation_result(
        workspace,
        [],
        profile="complete",
        contract=artifact_run_contract,
        manifest=read_manifest_contract(workspace),
    )
    self.assertFalse(report["passed"])
    self.assertEqual(projected_contract["validation_state"], "failed")


def test_repair_plan_uses_artifact_incomplete_action(self):
    strict_gap = ValidationError(
        error_id="artifact-0001",
        validator="check_crossframe_max_artifacts",
        error_type="full_source_incomplete",
        severity="error",
        artifact="max-source-snapshot.json",
        field="full_source_exhaustive_pass",
        message="complete profile requires full-source exhaustive pass",
        affected_phase="source_snapshot",
        repair_action="mark_artifact_incomplete",
        downstream_reset=[],
        final_output_allowed=True,
    )
    plan = build_repair_plan([strict_gap], workspace)
    self.assertIn("mark_artifact_incomplete", plan["repair_actions"])
    self.assertNotIn("max_incomplete", json.dumps(plan))


def test_report_becomes_stale_after_an_artifact_changes(self):
    projected_contract, report = build_validation_result(
        workspace,
        [],
        profile="artifact-run",
        contract=contract,
        manifest=read_manifest_contract(workspace),
    )
    write_validation_result(workspace, projected_contract, report)
    persisted = json.loads((workspace / "max-run-contract.json").read_text(encoding="utf-8"))
    self.assertEqual(persisted["validation_state"], "passed")
    self.assertEqual(report_freshness_errors(workspace, report), [])
    essay = workspace / "max-essay.md"
    essay.write_text(essay.read_text(encoding="utf-8") + "changed\n", encoding="utf-8")
    errors = report_freshness_errors(workspace, report)
    self.assertTrue(any("artifact_sha256" in error for error in errors))


def test_blocked_report_becomes_stale_after_contract_change(self):
    projected_contract, report = build_validation_result(
        workspace,
        [],
        profile="blocked",
        contract=blocked_contract,
        manifest=None,
    )
    write_validation_result(workspace, projected_contract, report)
    self.assertEqual(report_freshness_errors(workspace, report), [])
    projected_contract["blocked_reason"] = "different blocker"
    write_contract(workspace, projected_contract)
    errors = report_freshness_errors(workspace, report)
    self.assertTrue(any("run_contract_sha256" in error for error in errors))


def test_failed_report_has_a_total_final_label(self):
    projected_contract, report = build_validation_result(
        workspace,
        [missing_heading_error],
        profile="artifact-run",
        contract=contract,
        manifest=read_manifest_contract(workspace),
    )
    self.assertEqual(projected_contract["validation_state"], "failed")
    self.assertEqual(
        report["final_label"],
        "max-validation-failed:artifact-run:missing_template_heading",
    )


def test_failed_contract_must_reset_before_it_can_pass(self):
    failed_contract = dict(contract, validation_state="failed")
    projected_contract, report = build_validation_result(
        workspace,
        [],
        profile="artifact-run",
        contract=failed_contract,
        manifest=read_manifest_contract(workspace),
    )
    self.assertEqual(projected_contract["validation_state"], "failed")
    self.assertFalse(report["passed"])
    self.assertTrue(
        any(error["error_type"] == "invalid_validation_transition" for error in report["errors"])
    )
```

Create `tests/test_max_report_schema.py`. Load `max-validator-report.schema.json` with `Draft202012Validator` and build eight gold instances: one passed and one failed report for each of the four profiles. Assert `list(validator.iter_errors(report)) == []` for all eight. Then mutate one field at a time and require schema rejection for:

- `passed=true` with `validation_state=failed`;
- `passed=false` with an empty error array;
- complete passed with a non-`max-complete` label;
- artifact-run passed with incomplete reasons but no incomplete-label prefix;
- blocked with a non-null manifest hash or non-empty artifact map;
- non-blocked with a null manifest hash or empty artifact map;
- malformed run-contract/artifact SHA256;
- a failed label that does not contain profile and first error type.

For each invalid report, also assert `report_freshness_errors(workspace, report)` is non-empty so runtime acceptance cannot be weaker than schema acceptance on the persisted-report surface.

- [ ] **Step 2: Verify v1 fields fail the new tests**

Run: `python -B -m unittest tests.test_max_repair_contract -v`

Expected: FAIL because report v1 has no profile or final label and the repair plan still uses `max_incomplete`.

- [ ] **Step 3: Upgrade report and repair schemas to v2**

Validator report v2 must require `run_id`, `profile`, `run_mode`, `execution_state`, `artifact_state`, `incomplete_reasons`, `input_validation_state`, computed `validation_state`, `run_contract_sha256`, `manifest_sha256`, `artifact_sha256`, `final_label`, `passed`, `validators`, and `errors`. Both SHA fields use lowercase 64-character hex when non-null. `artifact_sha256` is an object whose keys and values exactly match the parsed manifest inventory. Schema conditionals require `passed=true`, `validation_state=passed`, and an empty error array together, or `passed=false`, `validation_state=failed`, and at least one error together. They also require a manifest hash plus at least one artifact hash for non-blocked profiles, and `manifest_sha256=null` plus an empty artifact object for blocked. Additional `if`/`then` branches enforce exact success labels, the artifact-run incomplete-label prefix, and profile-specific failure-label patterns. Because JSON Schema has no cross-field string interpolation, `report_freshness_errors()` enforces that the failed label's final segment equals the first structured `error_type` exactly.

Repair plan v2 must rename:

- `max_incomplete_if_unresolved` → `artifact_incomplete_if_unresolved`
- repair action `max_incomplete` → `mark_artifact_incomplete`

Keep all existing error types; add `runtime_state_conflict`, `invalid_validation_transition`, `profile_mismatch`, `manifest_state_mismatch`, `false_complete_claim`, `stale_or_false_validation_claim`, `premature_final_claim`, `artifact_semantic_thinness`, `missing_template_heading`, `duplicate_identifier`, `cross_reference_mismatch`, and `design_review_closure_failed`.

- [ ] **Step 4: Make report generation a post-validation action**

Finalize the `build_validation_result(workspace, errors, *, profile, contract, manifest) -> tuple[dict[str, Any], dict[str, Any]]` API introduced in Task 2 and remove the old `validator_report()` function. It returns the projected contract and report without writing. Compute `passed`, projected `validation_state`, hashes, and `final_label` only after profile, freshness, and transition checks. It must defensively synthesize a structured failure when the profile disagrees with the contract, complete is paired with a non-strict artifact state, or a failed input attempts to jump directly to passed, even if the caller supplies an empty error list.

Implement `write_validation_result(workspace, projected_contract, report)` exactly as Task 2 specifies. This is the only function that transitions the persisted run contract from `not_run` to `passed` or `failed`; the report binds the exact projected-contract bytes. Report creation therefore does not consume its own output and does not alter manifest-covered analysis files.

Remove the duplicate report implementation from both `build_crossframe_max_repair_plan.py` copies. Import `build_validation_result`, `write_validation_result`, `load_run_contract`, and `read_manifest_contract` from the matching `check_crossframe_max_artifacts.py` copy so CLI report generation has one implementation per execution root.

Manifest lifecycle:

1. analysis artifacts are written;
2. the input run contract is written with `validation_state=not_run` outside the analysis manifest;
3. manifest inventories and hashes analysis/phase artifacts, excluding itself and all control-plane sidecars;
4. validator recomputes every artifact hash and builds projected contract plus report;
5. `write_validation_result()` atomically replaces the run contract and then report; the report binds both control-plane state and analysis state;
6. repair resets the contract to `not_run`, changes analysis artifacts, regenerates the manifest, and reruns validation; either a contract change or an inventoried hash change makes the old report stale.

Add `report_freshness_errors(workspace, report) -> list[str]` and use it whenever an input contract or visible artifact claims `validation_state=passed` or `max-complete`. With standard-library checks, enforce the v2 required fields/types and recompute expected `passed`, `validation_state`, and `final_label` from profile, incomplete reasons, and ordered errors. Return an empty list only when those semantics plus run ID, profile, run-contract SHA256, manifest SHA256, inventory keys, and every artifact SHA256 match. For blocked, compare run ID, profile, and run-contract SHA256 while requiring the manifest fields to remain null/empty. The schema fixture tests remain the full draft-2020-12 reference check.

- [ ] **Step 5: Update repair builder and fixtures**

Map strict-only gaps encountered under the complete profile to `mark_artifact_incomplete` without deleting valid core artifacts. A passing artifact-run already carries an incomplete delivery label and needs no repair plan. Keep evidence, source-anchor, and contract failures mapped to downgrade, withdraw, or repository maintenance as currently defined.

Update each existing semantic mutation in `validate_crossframe_max_repair_fixtures.py` to call `rewrite_manifest(workspace)` before validation; only a dedicated stale-manifest repair case may leave hashes unchanged. This preserves the fixture's intended error/action mapping.

Add `profile: str | None = None` to `run_validators()` in both repair-builder copies and add the same four-choice `--profile` CLI option. Pass the resolved profile through `check_crossframe_max_artifacts_structured()` and into report generation; never infer one profile for validation and another for repair.

- [ ] **Step 6: Validate schemas and repair behavior**

```powershell
python -m json.tool skills/crossframe-max/schemas/max-run-contract.schema.json > $null
python -m json.tool skills/crossframe-max/schemas/max-validator-report.schema.json > $null
python -m json.tool skills/crossframe-max/schemas/max-repair-plan.schema.json > $null
python -B -m unittest tests.test_max_repair_contract tests.test_max_report_schema -v
python -B scripts/validate_crossframe_max_repair_fixtures.py
```

Expected: all PASS.

- [ ] **Step 7: Commit report and repair alignment**

```powershell
git add tests/test_max_repair_contract.py tests/test_max_report_schema.py scripts skills/crossframe-max/scripts skills/crossframe-max/schemas skills/crossframe-max/protocols/max-repair-loop-protocol.md
git commit -m "fix: align max validation and repair states"
```

## Task 5: Unify public and runtime terminology

**Files:**

- Create: `tests/test_max_status_docs.py`
- Modify: `skills/crossframe-max/SKILL.md:15-166`
- Modify: `skills/crossframe-max/agents/openai.yaml`
- Modify: `skills/crossframe-max/protocols/max-worldview-protocol.md`
- Modify: `skills/crossframe-max/evals/crossframe-max-smoke-tests.md`
- Modify: `README.md:190-225`
- Modify: `docs/QUICKSTART.md`
- Modify: `CHANGELOG.md:3-16`
- Modify: `scripts/check_crossframe_skill_integrity.py:2199-2300,2959-3015`

- [ ] **Step 1: Write failing terminology tests**

Create a test that reads the listed canonical files and asserts:

```python
CURRENT_MODES = (
    "max-artifact-run",
    "max-complete",
    "max-design-review",
    "max-blocked/progress",
)

for path in RUNTIME_CONTRACT_FILES:
    text = path.read_text(encoding="utf-8")
    self.assertNotIn("max-incomplete/progress", text, path.as_posix())

for mode in CURRENT_MODES:
    self.assertIn(mode, skill_text)
    self.assertIn(mode, readme_text)
    self.assertIn(mode, phase_template_text)
```

Also run `check_crossframe_skill_integrity.py` as a subprocess and assert return code zero after the repair.

- [ ] **Step 2: Verify the current terminology drift**

Run: `python -B -m unittest tests.test_max_status_docs -v`

Expected: FAIL on README, agent prompt, phase template, and integrity checker old markers.

- [ ] **Step 3: Update canonical runtime text**

Apply these exact semantic rules everywhere:

- Four run modes use the current names.
- `max-artifact-incomplete:` plus a registered reason is a derived delivery label, not a mode.
- A new or repaired run contract starts at `not_run`; validator materialization persists `passed` or `failed`, and a fresh report binds the exact contract, manifest, and artifact hashes.
- A failed contract cannot jump directly to passed; repair resets it to `not_run` before revalidation.
- Only a passed complete report may claim `max-complete`; pre-validation Markdown uses `pending-validator`.
- Artifact-run validation failure does not erase artifacts, but the report projects effective `validation_state=failed` and a non-complete final label.
- Every failed profile concatenates `max-validation-failed:`, the profile, another colon, and the first structured error type; no failed report may leave `final_label` undefined.
- The analysis manifest excludes run contract, validator report, and repair plan; the report separately hashes the run contract to prevent state cycles and blocked-report replay.
- `max-blocked/progress` requires a real blocker.
- Repair protocol uses `mark_artifact_incomplete`, not `max_incomplete`.

Update Changelog Unreleased with the state-contract repair, validator profiles, semantic fixtures, and split CI.

- [ ] **Step 4: Replace brittle obsolete integrity markers**

Remove requirements for old repair-preload text and `max-incomplete/progress`. Add checks for the new schema, new core templates, current modes, profile-aware CLI, manifest/report hash binding, v2 report fields, all four gold fixtures, adversarial tests, and root/skill script parity. Do not merely add the old string back to make CI green.

- [ ] **Step 5: Synchronize canonical skills to `.claude`**

Run:

```powershell
python -B scripts/sync_skill_mirrors.py
python -B scripts/sync_skill_mirrors.py --check
```

Expected: both commands return zero; `.claude/skills/crossframe-max` matches canonical.

- [ ] **Step 6: Run terminology and repository integrity tests**

```powershell
python -B -m unittest tests.test_max_status_docs -v
python -B scripts/check_crossframe_skill_integrity.py --repo .
```

Expected: PASS; the original `missing marker: max-incomplete/progress` failure is gone without restoring the obsolete mode.

- [ ] **Step 7: Commit terminology closure**

```powershell
git add README.md docs/QUICKSTART.md CHANGELOG.md tests/test_max_status_docs.py scripts/check_crossframe_skill_integrity.py skills/crossframe-max .claude/skills/crossframe-max
git commit -m "docs: unify current crossframe max runtime contract"
```

## Task 6: Harden mirror and executable parity checks

**Files:**

- Create: `tests/test_mirror_integrity.py`
- Modify: `scripts/sync_skill_mirrors.py:33-51`
- Modify: `scripts/check_crossframe_skill_integrity.py`

- [ ] **Step 1: Write a same-size/same-mtime drift regression test**

```python
def test_same_tree_detects_same_metadata_different_content(self):
    with tempfile.TemporaryDirectory() as td:
        left = Path(td) / "left"
        right = Path(td) / "right"
        left.mkdir()
        right.mkdir()
        (left / "x.txt").write_text("AAAA", encoding="utf-8")
        (right / "x.txt").write_text("BBBB", encoding="utf-8")
        stamp = 1_700_000_000
        os.utime(left / "x.txt", (stamp, stamp))
        os.utime(right / "x.txt", (stamp, stamp))
        self.assertFalse(same_tree(left, right))
```

Add a parity test for every root Max script that has an installed-skill copy, including the new runtime-contract module.

- [ ] **Step 2: Verify the shallow-comparison bug**

Run: `python -B -m unittest tests.test_mirror_integrity -v`

Expected: FAIL because current `filecmp.dircmp` reports the crafted trees equal.

- [ ] **Step 3: Replace shallow comparison with content hashing**

Implement:

```python
import hashlib


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def tree_hashes(root: Path) -> dict[str, str]:
    return {
        path.relative_to(root).as_posix(): file_sha256(path)
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def same_tree(left: Path, right: Path) -> bool:
    return left.is_dir() and right.is_dir() and tree_hashes(left) == tree_hashes(right)
```

- [ ] **Step 4: Add root/skill executable parity to integrity**

For each root file matching `scripts/check_crossframe_max_*.py`, `scripts/build_crossframe_max_repair_plan.py`, `scripts/generate_crossframe_max_v6_full_source.py`, and `scripts/crossframe_max_runtime_contract.py`, require a same-name skill copy with the same SHA256.

- [ ] **Step 5: Run mirror tests and checks**

```powershell
python -B -m unittest tests.test_mirror_integrity -v
python -B scripts/sync_skill_mirrors.py --check
python -B scripts/check_crossframe_skill_integrity.py --repo .
```

Expected: all PASS.

- [ ] **Step 6: Commit mirror hardening**

```powershell
git add tests/test_mirror_integrity.py scripts/sync_skill_mirrors.py scripts/check_crossframe_skill_integrity.py
git commit -m "test: verify crossframe mirrors by content hash"
```

## Task 7: Split GitHub verification into independent jobs

**Files:**

- Create: `tests/test_verify_workflow_contract.py`
- Modify: `.github/workflows/verify.yml:1-116`

- [ ] **Step 1: Write a failing workflow contract test**

Read `.github/workflows/verify.yml` as text and assert all four stable job IDs and their key commands exist:

```python
EXPECTED_JOBS = {
    "repository-integrity": "check_crossframe_skill_integrity.py --repo .",
    "max-contracts-and-artifacts": "unittest discover -s tests",
    "schemas-and-fixtures": "validate_crossframe_max_repair_fixtures.py",
    "mirrors-and-package": "sync_skill_mirrors.py --check",
}
```

Assert the four jobs have no `needs:` dependency on one another.

- [ ] **Step 2: Verify the monolithic workflow fails the test**

Run: `python -B -m unittest tests.test_verify_workflow_contract -v`

Expected: FAIL because current workflow has only `jobs.verify`.

- [ ] **Step 3: Rewrite the workflow into four jobs**

Use these responsibilities:

- `repository-integrity`: checkout, Python setup, integrity, source continuity, Python/Bash/PowerShell syntax, `git diff --check`.
- `max-contracts-and-artifacts`: checkout, Python setup, `pip install jsonschema`, full unittest discovery, v6 full-source, registry anchors.
- `schemas-and-fixtures`: checkout, Python setup, `pip install jsonschema`, JSON parsing, claim/DLC schemas, route fixtures, repair fixtures and planner smoke.
- `mirrors-and-package`: checkout, Python setup, mirror check, casebook/publication checks, package smoke, required package entries, extraction into a temporary directory, and execution of the packaged route/repair fixture validators from that extracted directory. This proves `scripts/crossframe_max_fixture_factory.py` is shipped and importable without `tests/`.

Set each job's display `name` equal to its stable job ID so branch protection contexts are predictable.

- [ ] **Step 4: Run workflow contract and local equivalents**

```powershell
python -B -m unittest tests.test_verify_workflow_contract -v
python -B -m unittest discover -s tests -p "test_*.py" -v
python -B scripts/check_crossframe_skill_integrity.py --repo .
```

Expected: all PASS.

- [ ] **Step 5: Commit split CI**

```powershell
git add .github/workflows/verify.yml tests/test_verify_workflow_contract.py
git commit -m "ci: split crossframe verification gates"
```

## Task 8: Run the complete local release gate

**Files:**

- Modify only if a validation failure reveals an in-scope defect.

- [ ] **Step 1: Run the complete unit suite**

Run: `python -B -m unittest discover -s tests -p "test_*.py" -v`

Expected: all tests PASS, zero skipped unless a test explicitly documents a platform-only GitHub operation.

- [ ] **Step 2: Run all repository validators**

```powershell
python -B scripts/check_crossframe_skill_integrity.py --repo .
python -B scripts/check_source_continuity.py --materials-only --repo .
python -B scripts/validate_claim_ledger_schema_fixtures.py --repo .
python -B scripts/validate_v5_dlc_quantification_schema_fixtures.py --repo .
python -B scripts/check_v5_dlc_casebook_trials.py --repo .
python -B scripts/check_v5_dlc_publication_bundle.py --repo .
python -B scripts/check_crossframe_max_v6_full_source.py --repo .
python -B scripts/check_crossframe_max_v6_registry_anchors.py --repo .
python -B scripts/validate_crossframe_max_route_ledger_fixtures.py
python -B scripts/validate_crossframe_max_repair_fixtures.py
python -B scripts/sync_skill_mirrors.py --check
```

Expected: every command exits zero.

- [ ] **Step 3: Run syntax and whitespace gates**

```powershell
$pythonFiles = Get-ChildItem -LiteralPath scripts -Filter '*.py' | Select-Object -ExpandProperty FullName
python -B -m py_compile $pythonFiles

$tokens = $null
$parseErrors = $null
$installer = (Resolve-Path 'scripts/install-codex.ps1').Path
[System.Management.Automation.Language.Parser]::ParseFile($installer, [ref] $tokens, [ref] $parseErrors) > $null
if ($parseErrors.Count -gt 0) {
    $parseErrors | ForEach-Object { Write-Error $_ }
    throw 'PowerShell installer syntax validation failed'
}

$bash = Get-Command bash -ErrorAction SilentlyContinue
if ($null -ne $bash) {
    & $bash.Source -n scripts/install-codex.sh
    if ($LASTEXITCODE -ne 0) { throw 'Bash installer syntax validation failed' }
}
git diff --check
```

Expected: zero syntax or whitespace errors.

- [ ] **Step 4: Run package smoke without retaining outputs**

```powershell
python -B scripts/package_crossframe_skill.py --repo . --version ci

$zip = Get-ChildItem -LiteralPath outputs -Filter 'crossframe-skill-suite-ci-*.zip' |
    Sort-Object LastWriteTimeUtc |
    Select-Object -Last 1 -ExpandProperty FullName
if (-not $zip) { throw 'package smoke did not create a ci zip' }

@'
import sys
import zipfile

required = {
    ".github/workflows/verify.yml",
    "scripts/crossframe_max_fixture_factory.py",
    "scripts/crossframe_max_runtime_contract.py",
    "scripts/validate_crossframe_max_route_ledger_fixtures.py",
    "scripts/validate_crossframe_max_repair_fixtures.py",
    "skills/crossframe-max/scripts/crossframe_max_runtime_contract.py",
    "skills/crossframe-max/schemas/max-run-contract.schema.json",
    "skills/crossframe-max/schemas/max-validator-report.schema.json",
    "skills/crossframe-max/schemas/max-repair-plan.schema.json",
    "skills/crossframe-max/templates/max-artifact-manifest-output.md",
    "skills/crossframe-max/templates/max-continuation-ledger-output.md",
    "skills/crossframe-max/templates/max-continuation-index-output.md",
}
with zipfile.ZipFile(sys.argv[1]) as archive:
    missing = sorted(required - set(archive.namelist()))
if missing:
    raise SystemExit(f"package smoke missing: {missing}")
'@ | python - $zip

$tempBase = [IO.Path]::GetFullPath([IO.Path]::GetTempPath())
$extractRoot = [IO.Path]::GetFullPath((Join-Path $tempBase ("crossframe-package-" + [guid]::NewGuid())))
if (-not $extractRoot.StartsWith($tempBase, [StringComparison]::OrdinalIgnoreCase)) {
    throw "unsafe package extraction path: $extractRoot"
}
New-Item -ItemType Directory -Path $extractRoot > $null
try {
    Expand-Archive -LiteralPath $zip -DestinationPath $extractRoot
    Push-Location $extractRoot
    try {
        python -B scripts/validate_crossframe_max_route_ledger_fixtures.py
        if ($LASTEXITCODE -ne 0) { throw 'packaged route fixtures failed' }
        python -B scripts/validate_crossframe_max_repair_fixtures.py
        if ($LASTEXITCODE -ne 0) { throw 'packaged repair fixtures failed' }
    } finally {
        Pop-Location
    }
} finally {
    Remove-Item -LiteralPath $extractRoot -Recurse -Force
}

$repoRoot = (Resolve-Path .).Path
$outputsRoot = (Resolve-Path outputs).Path
$expectedOutputsRoot = [IO.Path]::GetFullPath((Join-Path $repoRoot 'outputs'))
if (-not $outputsRoot.Equals($expectedOutputsRoot, [StringComparison]::OrdinalIgnoreCase)) {
    throw "unsafe outputs path: $outputsRoot"
}
git check-ignore -q -- outputs
if ($LASTEXITCODE -ne 0) { throw 'outputs/ is not ignored; refusing cleanup' }
Remove-Item -LiteralPath $outputsRoot -Recurse -Force
```

The extracted validators must pass without importing anything from `tests/`. The guarded cleanup must remove both temporary extraction and ignored package output.

- [ ] **Step 5: Review the complete branch diff**

```powershell
git status --short
git diff origin/main...HEAD --check
git diff origin/main...HEAD --stat
git log --oneline origin/main..HEAD
```

Expected: only approved in-scope files; no v7 source or local-install changes.

- [ ] **Step 6: Commit any final in-scope validation correction**

If Step 1-5 exposes a defect, return to the Task that owns that file, add a failing regression there, apply the minimum fix, repeat that Task's test and commit step, then rerun Task 8 from Step 1. Do not create a catch-all validation commit or an empty commit.

## Task 9: Publish, verify, merge, and protect `main`

**Files:**

- GitHub branch, PR, Actions checks, and branch protection only.
- Do not modify local installed skills.

- [ ] **Step 1: Confirm the branch is clean and based on current `origin/main`**

```powershell
git fetch origin main
git status --short
git rev-list --left-right --count origin/main...HEAD
```

Expected: clean status; branch contains the planned commits and no unexpected divergence. If the left count is non-zero because `origin/main` moved, run `git rebase origin/main`, resolve only in-scope conflicts, and rerun Task 8 in full before pushing.

- [ ] **Step 2: Push the maintenance branch**

```powershell
git push --set-upstream origin codex/repair-current-max-control-plane
```

Expected: push succeeds and remote branch points to local HEAD.

- [ ] **Step 3: Create the PR through the GitHub connector**

Title: `Repair current CrossFrame Max control plane`

Body must include:

- the known e384 integrity failure;
- the four-state machine and profile split;
- semantic fixture and template closure;
- mirror hashing and independent CI jobs;
- explicit non-goal: no v7 migration;
- exact local verification commands from Task 8.

- [ ] **Step 4: Wait for every independent check**

Required check names:

```text
repository-integrity
max-contracts-and-artifacts
schemas-and-fixtures
mirrors-and-package
```

Expected: all four SUCCESS. Do not merge on failure, skipped, pending, or missing status.

- [ ] **Step 5: Review the PR patch and merge**

Use the GitHub connector to re-read the final patch and changed filenames, confirm no v7/local-install files, then merge with the repository's normal merge method. Record the merge SHA.

- [ ] **Step 6: Revalidate merged `main`**

Fetch the merge SHA into a clean snapshot/worktree and rerun:

```powershell
python -B -m unittest discover -s tests -p "test_*.py" -v
python -B scripts/check_crossframe_skill_integrity.py --repo .
python -B scripts/sync_skill_mirrors.py --check
```

Expected: all PASS at the actual merged SHA.

- [ ] **Step 7: Enable branch protection after check names are proven stable**

Use `gh api` only if the GitHub connector has no branch-protection operation. Submit this protection policy to `repos/xi-kari/crossframe-skill/branches/main/protection`:

```json
{
  "required_status_checks": {
    "strict": true,
    "contexts": [
      "repository-integrity",
      "max-contracts-and-artifacts",
      "schemas-and-fixtures",
      "mirrors-and-package"
    ]
  },
  "enforce_admins": true,
  "required_pull_request_reviews": {
    "dismiss_stale_reviews": false,
    "require_code_owner_reviews": false,
    "required_approving_review_count": 0,
    "require_last_push_approval": false
  },
  "restrictions": null,
  "required_linear_history": false,
  "allow_force_pushes": false,
  "allow_deletions": false,
  "block_creations": false,
  "required_conversation_resolution": true,
  "lock_branch": false,
  "allow_fork_syncing": false
}
```

If GitHub rejects zero-review PR protection for this repository, retain required status checks, admin enforcement, conversation resolution, and force-push/deletion blocking; report the unsupported review subsetting rather than weakening checks silently.

When the connector lacks this operation, execute the exact payload above with:

```powershell
$protection = @'
{
  "required_status_checks": {
    "strict": true,
    "contexts": [
      "repository-integrity",
      "max-contracts-and-artifacts",
      "schemas-and-fixtures",
      "mirrors-and-package"
    ]
  },
  "enforce_admins": true,
  "required_pull_request_reviews": {
    "dismiss_stale_reviews": false,
    "require_code_owner_reviews": false,
    "required_approving_review_count": 0,
    "require_last_push_approval": false
  },
  "restrictions": null,
  "required_linear_history": false,
  "allow_force_pushes": false,
  "allow_deletions": false,
  "block_creations": false,
  "required_conversation_resolution": true,
  "lock_branch": false,
  "allow_fork_syncing": false
}
'@
$protection | gh api --method PUT `
    -H 'Accept: application/vnd.github+json' `
    -H 'X-GitHub-Api-Version: 2022-11-28' `
    'repos/xi-kari/crossframe-skill/branches/main/protection' `
    --input -
if ($LASTEXITCODE -ne 0) { throw 'branch protection update failed' }
gh api 'repos/xi-kari/crossframe-skill/branches/main/protection'
```

- [ ] **Step 8: Verify protection and leave local state clean**

Read back branch protection and confirm all required contexts. Capture final SHAs and check output, then return to the original checkout and run:

```powershell
Set-Location 'E:\世界模型\skill\crossframe-skill'
git status --short
git worktree remove -- 'C:\Users\cangm\.config\superpowers\worktrees\crossframe-skill\repair-current-max-control-plane'
git branch -d codex/repair-current-max-control-plane
```

The first command must show no original-checkout changes before removal. Use only safe `git branch -d`; if the hosting merge method prevents Git from recognizing the local branch as merged, retain it and report that fact instead of forcing deletion. Do not sync `$HOME/.codex/skills` or `$HOME/.agents/skills` without separate user authorization.

Expected final state: protected green `main`, merged repair PR, no open maintenance branch needed, clean original checkout, no v7 changes.
