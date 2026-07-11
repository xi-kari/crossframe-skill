from __future__ import annotations

import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from crossframe_max_runtime_contract import load_schema, validate_run_contract


def valid_contract(**overrides: object) -> dict[str, object]:
    contract: dict[str, object] = {
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
    def test_schema_declares_only_current_modes(self) -> None:
        schema = load_schema(ROOT / "skills" / "crossframe-max")
        modes = schema["properties"]["run_mode"]["enum"]
        self.assertEqual(
            modes,
            ["max-artifact-run", "max-complete", "max-design-review", "max-blocked/progress"],
        )
        self.assertNotIn("max-incomplete/progress", json.dumps(schema, ensure_ascii=False))

    def test_honest_artifact_run_is_valid(self) -> None:
        self.assertEqual(validate_run_contract(valid_contract()), [])

    def test_complete_target_requires_strict_artifacts_but_not_a_predeclared_pass(self) -> None:
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

    def test_blocked_mode_requires_a_real_blocker(self) -> None:
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

    def test_old_mode_is_rejected(self) -> None:
        errors = validate_run_contract(valid_contract(run_mode="max-incomplete/progress"))
        self.assertTrue(any("run_mode" in error for error in errors))

    def test_runtime_and_jsonschema_agree_on_validity(self) -> None:
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
