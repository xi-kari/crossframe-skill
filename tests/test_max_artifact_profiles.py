from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_crossframe_max_artifacts import (
    build_validation_result,
    check_crossframe_max_artifacts,
    read_manifest_contract,
    write_validation_result,
)
from crossframe_max_fixture_factory import (
    write_artifact_run_fixture,
    write_blocked_fixture,
    write_complete_fixture,
    write_design_review_fixture,
)


class MaxArtifactProfileTests(unittest.TestCase):
    def test_honest_artifact_run_passes_artifact_profile(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_artifact_run_fixture(workspace)
            self.assertEqual(check_crossframe_max_artifacts(workspace, profile="artifact-run"), [])

    def test_honest_artifact_run_fails_complete_profile(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_artifact_run_fixture(workspace)
            errors = check_crossframe_max_artifacts(workspace, profile="complete")
            self.assertTrue(any("missing structured ledger" in error for error in errors))

    def test_complete_profile_rejects_partial_source(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_complete_fixture(workspace)
            snapshot_path = workspace / "max-source-snapshot.json"
            snapshot = json.loads(snapshot_path.read_text(encoding="utf-8"))
            snapshot["full_source_exhaustive_pass"] = False
            snapshot_path.write_text(json.dumps(snapshot), encoding="utf-8")
            errors = check_crossframe_max_artifacts(workspace, profile="complete")
            self.assertTrue(any("full_source_exhaustive_pass" in error for error in errors))

    def test_artifact_run_cannot_claim_max_complete(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_artifact_run_fixture(workspace)
            manifest = workspace / "max-artifact-manifest.md"
            manifest.write_text(
                manifest.read_text(encoding="utf-8") + "\n交付状态：max-complete\n",
                encoding="utf-8",
            )
            errors = check_crossframe_max_artifacts(workspace, profile="artifact-run")
            self.assertTrue(any("false max-complete claim" in error for error in errors))

    def test_skill_design_review_requires_design_route_closure(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_design_review_fixture(workspace)
            self.assertEqual(check_crossframe_max_artifacts(workspace, profile="design-review"), [])
            read_plan_path = workspace / "max-read-plan.json"
            read_plan = json.loads(read_plan_path.read_text(encoding="utf-8"))
            read_plan["route_key"] = "default"
            read_plan_path.write_text(json.dumps(read_plan), encoding="utf-8")
            errors = check_crossframe_max_artifacts(workspace, profile="design-review")
            self.assertTrue(any("skill_design" in error for error in errors))

    def test_blocked_profile_does_not_require_longform_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_blocked_fixture(workspace)
            self.assertEqual(check_crossframe_max_artifacts(workspace, profile="blocked"), [])
            self.assertFalse((workspace / "max-dossier.md").exists())

    def test_artifact_profile_report_projects_an_honest_incomplete_label(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_artifact_run_fixture(workspace)
            contract = json.loads((workspace / "max-run-contract.json").read_text(encoding="utf-8"))
            projected, report = build_validation_result(
                workspace,
                [],
                profile="artifact-run",
                contract=contract,
                manifest=read_manifest_contract(workspace),
            )
            self.assertEqual(projected["validation_state"], "passed")
            self.assertEqual(report["profile"], "artifact-run")
            self.assertEqual(
                report["final_label"],
                "max-artifact-incomplete:full-source-exhaustive-pass-not-satisfied",
            )

    def test_write_validation_result_materializes_contract_and_report(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_artifact_run_fixture(workspace)
            contract = json.loads((workspace / "max-run-contract.json").read_text(encoding="utf-8"))
            projected, report = build_validation_result(
                workspace,
                [],
                profile="artifact-run",
                contract=contract,
                manifest=read_manifest_contract(workspace),
            )
            write_validation_result(workspace, projected, report)
            persisted = json.loads((workspace / "max-run-contract.json").read_text(encoding="utf-8"))
            persisted_report = json.loads(
                (workspace / "max-validator-report.json").read_text(encoding="utf-8")
            )
            self.assertEqual(persisted["validation_state"], "passed")
            self.assertEqual(persisted_report["run_contract_sha256"], report["run_contract_sha256"])

    def test_cli_accepts_profile_and_emits_v2_report(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_artifact_run_fixture(workspace)
            result = subprocess.run(
                [
                    sys.executable,
                    "-B",
                    str(ROOT / "scripts" / "check_crossframe_max_artifacts.py"),
                    "--workspace",
                    str(workspace),
                    "--profile",
                    "artifact-run",
                    "--json",
                ],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            report = json.loads(result.stdout)
            self.assertEqual(report["report_version"], "v2")
            self.assertEqual(report["profile"], "artifact-run")


if __name__ == "__main__":
    unittest.main()
