from __future__ import annotations

from pathlib import Path
import json
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_crossframe_max_artifacts import REQUIRED_DOSSIER_HEADINGS
import crossframe_max_fixture_factory as fixture_factory


TEMPLATE_ROOT = ROOT / "skills" / "crossframe-max" / "templates"


def markdown_headings(path: Path) -> list[str]:
    return [
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.startswith("## ")
    ]


class MaxTemplateContractTests(unittest.TestCase):
    def test_dossier_template_contains_every_validator_heading(self) -> None:
        template = TEMPLATE_ROOT / "max-dossier-output.md"
        self.assertEqual(markdown_headings(template), REQUIRED_DOSSIER_HEADINGS)

    def test_every_core_artifact_has_a_template(self) -> None:
        expected = {
            "max-dossier-output.md",
            "max-essay-output.md",
            "max-artifact-manifest-output.md",
            "max-continuation-ledger-output.md",
            "max-continuation-index-output.md",
        }
        self.assertTrue(expected.issubset({path.name for path in TEMPLATE_ROOT.glob("*.md")}))

    def test_marker_only_fixture_fails(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            fixture_factory.write_marker_only_fixture(workspace)
            from check_crossframe_max_artifacts import check_crossframe_max_artifacts

            errors = check_crossframe_max_artifacts(workspace, profile="artifact-run")
            self.assertTrue(
                any("marker-only" in error or "section too thin" in error for error in errors),
                errors,
            )

    def test_complete_fixture_keeps_preaudit_claim_candidate(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            workspace = Path(td)
            fixture_factory.write_complete_fixture(workspace)
            board = json.loads((workspace / "max-claim-board.json").read_text(encoding="utf-8"))
            self.assertEqual(board["claims"][0]["status"], "candidate")


if __name__ == "__main__":
    unittest.main()
