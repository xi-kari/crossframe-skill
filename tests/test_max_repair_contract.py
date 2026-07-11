from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_crossframe_max_repair_plan import ValidationError, build_repair_plan
from check_crossframe_max_artifacts import (
    build_validation_result,
    read_manifest_contract,
    report_freshness_errors,
    write_validation_result,
)
from crossframe_max_fixture_factory import (
    write_artifact_run_fixture,
    write_blocked_fixture,
    write_contract,
)


def read_contract(workspace: Path) -> dict[str, object]:
    return json.loads((workspace / "max-run-contract.json").read_text(encoding="utf-8"))


def structured_error(error_type: str = "missing_template_heading") -> dict[str, object]:
    return {
        "error_id": "artifact-0001",
        "validator": "check_crossframe_max_artifacts",
        "error_type": error_type,
        "severity": "error",
        "artifact": "max-dossier.md",
        "field": None,
        "message": "max-dossier.md: missing heading",
        "affected_phase": "final_markdown",
        "repair_action": "regenerate_markdown_only",
        "downstream_reset": [],
        "final_output_allowed": False,
    }


class MaxRepairContractTests(unittest.TestCase):
    def test_artifact_run_report_records_profile_and_incomplete_label(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_artifact_run_fixture(workspace)
            contract = read_contract(workspace)
            projected, report = build_validation_result(
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
            self.assertEqual(projected["validation_state"], "passed")
            self.assertEqual(
                report["final_label"],
                "max-artifact-incomplete:full-source-exhaustive-pass-not-satisfied",
            )

    def test_complete_report_cannot_pass_with_incomplete_contract(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_artifact_run_fixture(workspace)
            contract = read_contract(workspace)
            projected, report = build_validation_result(
                workspace,
                [],
                profile="complete",
                contract=contract,
                manifest=read_manifest_contract(workspace),
            )
            self.assertFalse(report["passed"])
            self.assertEqual(projected["validation_state"], "failed")

    def test_repair_plan_uses_artifact_incomplete_action(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
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

    def test_report_becomes_stale_after_an_artifact_changes(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_artifact_run_fixture(workspace)
            contract = read_contract(workspace)
            projected, report = build_validation_result(
                workspace,
                [],
                profile="artifact-run",
                contract=contract,
                manifest=read_manifest_contract(workspace),
            )
            write_validation_result(workspace, projected, report)
            self.assertEqual(report_freshness_errors(workspace, report), [])
            essay = workspace / "max-essay.md"
            essay.write_text(essay.read_text(encoding="utf-8") + "changed\n", encoding="utf-8")
            errors = report_freshness_errors(workspace, report)
            self.assertTrue(any("artifact_sha256" in error for error in errors), errors)

    def test_blocked_report_becomes_stale_after_contract_change(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_blocked_fixture(workspace)
            contract = read_contract(workspace)
            projected, report = build_validation_result(
                workspace,
                [],
                profile="blocked",
                contract=contract,
                manifest=None,
            )
            write_validation_result(workspace, projected, report)
            self.assertEqual(report_freshness_errors(workspace, report), [])
            projected["blocked_reason"] = "different blocker"
            write_contract(workspace, projected)
            errors = report_freshness_errors(workspace, report)
            self.assertTrue(any("run_contract_sha256" in error for error in errors), errors)

    def test_failed_report_has_total_final_label(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_artifact_run_fixture(workspace)
            projected, report = build_validation_result(
                workspace,
                [structured_error()],
                profile="artifact-run",
                contract=read_contract(workspace),
                manifest=read_manifest_contract(workspace),
            )
            self.assertEqual(projected["validation_state"], "failed")
            self.assertEqual(
                report["final_label"],
                "max-validation-failed:artifact-run:missing_template_heading",
            )

    def test_failed_contract_must_reset_before_it_can_pass(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_artifact_run_fixture(workspace)
            contract = read_contract(workspace)
            contract["validation_state"] = "failed"
            projected, report = build_validation_result(
                workspace,
                [],
                profile="artifact-run",
                contract=contract,
                manifest=read_manifest_contract(workspace),
            )
            self.assertEqual(projected["validation_state"], "failed")
            self.assertFalse(report["passed"])
            self.assertTrue(
                any(error["error_type"] == "invalid_validation_transition" for error in report["errors"])
            )


if __name__ == "__main__":
    unittest.main()
