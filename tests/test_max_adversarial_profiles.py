from __future__ import annotations

import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_crossframe_max_artifacts import check_crossframe_max_artifacts_structured
from crossframe_max_fixture_factory import (
    rewrite_manifest,
    write_artifact_run_fixture,
    write_complete_fixture,
    write_contract,
    write_design_review_fixture,
    write_marker_only_fixture,
)


def read_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, object]) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


class MaxAdversarialProfileTests(unittest.TestCase):
    def assert_error_type(
        self,
        workspace: Path,
        profile: str,
        expected: str,
        *,
        allow_manifest_mismatch: bool = False,
    ) -> None:
        errors = check_crossframe_max_artifacts_structured(workspace, profile=profile)
        error_types = {error.error_type for error in errors}
        self.assertIn(expected, error_types, [error.message for error in errors])
        if not allow_manifest_mismatch:
            self.assertNotIn("manifest_state_mismatch", error_types, [error.message for error in errors])

    def test_retired_mode_is_runtime_state_conflict(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_artifact_run_fixture(workspace)
            contract_path = workspace / "max-run-contract.json"
            contract = read_json(contract_path)
            contract["run_mode"] = "max-incomplete/progress"
            write_json(contract_path, contract)
            self.assert_error_type(workspace, "artifact-run", "runtime_state_conflict")

    def test_false_complete_claim_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_artifact_run_fixture(workspace)
            contract_path = workspace / "max-run-contract.json"
            contract = read_json(contract_path)
            contract["final_output_allowed"] = False
            write_json(contract_path, contract)
            essay_path = workspace / "max-essay.md"
            essay_path.write_text(
                essay_path.read_text(encoding="utf-8") + "\n交付状态：max-complete\n",
                encoding="utf-8",
            )
            rewrite_manifest(workspace)
            self.assert_error_type(workspace, "artifact-run", "false_complete_claim")

    def test_premature_evidence_claim_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_design_review_fixture(workspace)
            claim_path = workspace / "max-claim-ledger.json"
            claims = read_json(claim_path)
            claims["claims"][0]["needs_evidence"] = True  # type: ignore[index]
            write_json(claim_path, claims)
            rewrite_manifest(workspace)
            self.assert_error_type(workspace, "design-review", "premature_final_claim")

    def test_marker_only_dossier_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_marker_only_fixture(workspace)
            self.assert_error_type(workspace, "artifact-run", "artifact_semantic_thinness")

    def test_missing_canonical_heading_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_artifact_run_fixture(workspace)
            dossier_path = workspace / "max-dossier.md"
            dossier_path.write_text(
                dossier_path.read_text(encoding="utf-8").replace(
                    "## max-continuation-index",
                    "## removed-continuation-index",
                ),
                encoding="utf-8",
            )
            rewrite_manifest(workspace)
            self.assert_error_type(workspace, "artifact-run", "missing_template_heading")

    def test_present_false_cannot_hide_forbidden_output(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_complete_fixture(workspace)
            dossier_path = workspace / "max-dossier.md"
            dossier_path.write_text(
                dossier_path.read_text(encoding="utf-8")
                + "\n已检查 forbidden output：`把 prompt 当作概念本体`，present=false。\n",
                encoding="utf-8",
            )
            rewrite_manifest(workspace)
            self.assert_error_type(workspace, "complete", "forbidden_output_present")

    def test_stale_manifest_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_artifact_run_fixture(workspace)
            essay_path = workspace / "max-essay.md"
            essay_path.write_text(
                essay_path.read_text(encoding="utf-8") + "\nchanged after manifest\n",
                encoding="utf-8",
            )
            self.assert_error_type(
                workspace,
                "artifact-run",
                "manifest_state_mismatch",
                allow_manifest_mismatch=True,
            )

    def test_mixed_profile_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_artifact_run_fixture(workspace)
            self.assert_error_type(workspace, "complete", "profile_mismatch")

    def test_fake_pass_report_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_artifact_run_fixture(workspace)
            contract_path = workspace / "max-run-contract.json"
            contract = read_json(contract_path)
            contract["validation_state"] = "passed"
            write_contract(workspace, contract)
            fake_report = {
                "report_version": "v2",
                "run_id": contract["run_id"],
                "profile": "artifact-run",
                "run_mode": contract["run_mode"],
                "execution_state": contract["execution_state"],
                "artifact_state": contract["artifact_state"],
                "incomplete_reasons": contract["incomplete_reasons"],
                "input_validation_state": "not_run",
                "validation_state": "passed",
                "run_contract_sha256": "0" * 64,
                "manifest_sha256": "0" * 64,
                "artifact_sha256": {},
                "final_label": "max-artifact-incomplete:full-source-exhaustive-pass-not-satisfied",
                "passed": True,
                "validators": [],
                "errors": [],
            }
            write_json(workspace / "max-validator-report.json", fake_report)
            self.assert_error_type(workspace, "artifact-run", "stale_or_false_validation_claim")

    def test_duplicate_claim_and_source_ids_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_design_review_fixture(workspace)
            claim_path = workspace / "max-claim-ledger.json"
            data = read_json(claim_path)
            first = data["claims"][0]  # type: ignore[index]
            first["source_paragraph_ids"].append(first["source_paragraph_ids"][0])  # type: ignore[index]
            data["claims"].append(copy.deepcopy(first))  # type: ignore[union-attr]
            write_json(claim_path, data)
            rewrite_manifest(workspace)
            self.assert_error_type(workspace, "design-review", "duplicate_identifier")

    def test_broken_audit_backreference_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_design_review_fixture(workspace)
            audit_path = workspace / "max-evidence-reasoning-audit.json"
            data = read_json(audit_path)
            data["audits"][0]["claim_id"] = "CL-missing"  # type: ignore[index]
            write_json(audit_path, data)
            rewrite_manifest(workspace)
            self.assert_error_type(workspace, "design-review", "cross_reference_mismatch")

    def test_design_review_requires_counterevidence_withdrawal_and_action_limit(self) -> None:
        mutations = (
            ("max-evidence-reasoning-audit.json", "audits", "counterevidence"),
            ("max-claim-ledger.json", "claims", "withdrawal_condition"),
            ("max-claim-ledger.json", "claims", "action_limit"),
        )
        for filename, collection, field in mutations:
            with self.subTest(field=field), tempfile.TemporaryDirectory() as td:
                workspace = Path(td)
                write_design_review_fixture(workspace)
                path = workspace / filename
                data = read_json(path)
                data[collection][0].pop(field)  # type: ignore[index]
                write_json(path, data)
                rewrite_manifest(workspace)
                self.assert_error_type(workspace, "design-review", "design_review_closure_failed")


if __name__ == "__main__":
    unittest.main()
