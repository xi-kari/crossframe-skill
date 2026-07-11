from __future__ import annotations

import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_crossframe_max_artifacts import (
    build_validation_result,
    read_manifest_contract,
    report_freshness_errors,
    write_validation_result,
)
from crossframe_max_fixture_factory import (
    write_artifact_run_fixture,
    write_blocked_fixture,
    write_complete_fixture,
    write_design_review_fixture,
)
from tests.test_max_repair_contract import structured_error


SCHEMA_PATH = ROOT / "skills" / "crossframe-max" / "schemas" / "max-validator-report.schema.json"


def read_contract(workspace: Path) -> dict[str, object]:
    return json.loads((workspace / "max-run-contract.json").read_text(encoding="utf-8"))


class MaxReportSchemaTests(unittest.TestCase):
    def setUp(self) -> None:
        self.validator = Draft202012Validator(json.loads(SCHEMA_PATH.read_text(encoding="utf-8")))

    def build_report(self, workspace: Path, profile: str, failed: bool = False) -> dict[str, object]:
        manifest = None if profile == "blocked" else read_manifest_contract(workspace)
        projected, report = build_validation_result(
            workspace,
            [structured_error()] if failed else [],
            profile=profile,
            contract=read_contract(workspace),
            manifest=manifest,
        )
        write_validation_result(workspace, projected, report)
        return report

    def test_passed_and_failed_reports_for_all_profiles_match_schema(self) -> None:
        fixtures = {
            "artifact-run": write_artifact_run_fixture,
            "complete": write_complete_fixture,
            "design-review": write_design_review_fixture,
            "blocked": write_blocked_fixture,
        }
        for profile, writer in fixtures.items():
            for failed in (False, True):
                with self.subTest(profile=profile, failed=failed), tempfile.TemporaryDirectory() as td:
                    workspace = Path(td)
                    writer(workspace)
                    report = self.build_report(workspace, profile, failed)
                    self.assertEqual(list(self.validator.iter_errors(report)), [])

    def test_invalid_report_combinations_are_rejected_by_schema_and_runtime(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_artifact_run_fixture(workspace)
            valid = self.build_report(workspace, "artifact-run")
            invalid_reports: list[dict[str, object]] = []

            report = copy.deepcopy(valid)
            report["validation_state"] = "failed"
            invalid_reports.append(report)

            report = copy.deepcopy(valid)
            report["passed"] = False
            report["errors"] = []
            invalid_reports.append(report)

            report = copy.deepcopy(valid)
            report["final_label"] = "max-complete"
            invalid_reports.append(report)

            report = copy.deepcopy(valid)
            report["manifest_sha256"] = None
            report["artifact_sha256"] = {}
            invalid_reports.append(report)

            report = copy.deepcopy(valid)
            report["run_contract_sha256"] = "bad-hash"
            invalid_reports.append(report)

            for report in invalid_reports:
                with self.subTest(report=report):
                    self.assertTrue(list(self.validator.iter_errors(report)))
                    self.assertTrue(report_freshness_errors(workspace, report))

    def test_blocked_report_rejects_manifest_binding(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            write_blocked_fixture(workspace)
            report = self.build_report(workspace, "blocked")
            report["manifest_sha256"] = "0" * 64
            report["artifact_sha256"] = {"max-dossier.md": "0" * 64}
            self.assertTrue(list(self.validator.iter_errors(report)))
            self.assertTrue(report_freshness_errors(workspace, report))


if __name__ == "__main__":
    unittest.main()
