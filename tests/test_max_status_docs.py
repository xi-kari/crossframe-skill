from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CURRENT_MODES = (
    "max-artifact-run",
    "max-complete",
    "max-design-review",
    "max-blocked/progress",
)
RUNTIME_CONTRACT_FILES = (
    ROOT / "skills/crossframe-max/SKILL.md",
    ROOT / "skills/crossframe-max/agents/openai.yaml",
    ROOT / "skills/crossframe-max/protocols/max-worldview-protocol.md",
    ROOT / "skills/crossframe-max/protocols/max-repair-loop-protocol.md",
    ROOT / "skills/crossframe-max/templates/max-phase-lock-output.md",
    ROOT / "skills/crossframe-max/templates/max-repair-plan-output.md",
    ROOT / "skills/crossframe-max/evals/crossframe-max-smoke-tests.md",
    ROOT / "README.md",
    ROOT / "docs/QUICKSTART.md",
)


class MaxStatusDocsTests(unittest.TestCase):
    def test_runtime_contract_files_retire_old_mode_and_action_names(self) -> None:
        for path in RUNTIME_CONTRACT_FILES:
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("max-incomplete/progress", text, path.as_posix())
            self.assertNotIn("max_incomplete", text, path.as_posix())

    def test_primary_surfaces_list_all_current_modes(self) -> None:
        skill_text = (ROOT / "skills/crossframe-max/SKILL.md").read_text(encoding="utf-8")
        readme_text = (ROOT / "README.md").read_text(encoding="utf-8")
        phase_template_text = (ROOT / "skills/crossframe-max/templates/max-phase-lock-output.md").read_text(
            encoding="utf-8"
        )
        for mode in CURRENT_MODES:
            self.assertIn(mode, skill_text)
            self.assertIn(mode, readme_text)
            self.assertIn(mode, phase_template_text)

    def test_repository_integrity_accepts_current_contract(self) -> None:
        result = subprocess.run(
            [sys.executable, "-B", "scripts/check_crossframe_skill_integrity.py", "--repo", "."],
            cwd=ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
