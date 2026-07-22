from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRESERVATION_PATH = ROOT / "tests/fixtures/promax-preservation.json"
SUITE_ROUTE_PATHS = (
    ROOT / "skills/crossframe-suite/SKILL.md",
    ROOT / "skills/crossframe-suite/protocols/suite-dispatch-protocol.md",
    ROOT / "skills/crossframe-suite/references/workflow-routing-map.md",
)


def canonical_git_bytes(path: Path) -> bytes:
    # Git's text clean filter stores LF. Normalize only checkout line endings so
    # this byte-level preservation contract is stable on Windows and Linux.
    return path.read_bytes().replace(b"\r\n", b"\n")


def tree_hash(paths: list[Path]) -> str:
    digest = hashlib.sha256()
    for path in sorted(paths, key=lambda item: item.relative_to(ROOT).as_posix()):
        relative = path.relative_to(ROOT).as_posix()
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(canonical_git_bytes(path))
        digest.update(b"\0")
    return digest.hexdigest()


def current_surfaces() -> dict[str, list[Path]]:
    return {
        "skills_crossframe_max": [
            path for path in (ROOT / "skills/crossframe-max").rglob("*") if path.is_file()
        ],
        "claude_skills_crossframe_max": [
            path for path in (ROOT / ".claude/skills/crossframe-max").rglob("*") if path.is_file()
        ],
        "claude_command_crossframe_max": [
            ROOT / ".claude/commands/crossframe-max.md"
        ],
        "root_scripts_filename_contains_max": [
            path
            for path in (ROOT / "scripts").iterdir()
            if path.is_file() and "max" in path.name.lower()
        ],
        "max_contract_tests": list((ROOT / "tests").glob("test_max_*.py")),
    }


def workflow_job_blocks(text: str) -> dict[str, str]:
    jobs_text = text.split("\njobs:\n", 1)[1]
    matches = list(re.finditer(r"(?m)^  ([a-z0-9-]+):\s*$", jobs_text))
    return {
        match.group(1): jobs_text[
            match.start() : matches[index + 1].start() if index + 1 < len(matches) else len(jobs_text)
        ]
        for index, match in enumerate(matches)
    }


class ProMaxPreservationTests(unittest.TestCase):
    def test_all_max_surfaces_match_frozen_tree_hashes(self) -> None:
        manifest = json.loads(PRESERVATION_PATH.read_text(encoding="utf-8"))
        self.assertEqual(manifest["base_commit"], "e2e0965")
        self.assertEqual(
            manifest["tree_hash_algorithm"],
            "SHA-256 over each repository-relative POSIX path in lexical order: "
            "path_utf8 + NUL + bytes + NUL",
        )
        surfaces = current_surfaces()
        self.assertEqual(set(surfaces), set(manifest["surfaces"]))
        for name, paths in surfaces.items():
            expected = manifest["surfaces"][name]
            with self.subTest(surface=name):
                self.assertTrue(all(path.is_file() for path in paths))
                self.assertEqual(len(paths), expected["file_count"])
                self.assertEqual(tree_hash(paths), expected["tree_sha256"])

    def test_max_workflow_job_matches_frozen_raw_text_and_hash(self) -> None:
        manifest = json.loads(PRESERVATION_PATH.read_text(encoding="utf-8"))
        job = manifest["workflow_job"]
        workflow_text = canonical_git_bytes(ROOT / job["workflow_path"]).decode("utf-8")
        actual = workflow_job_blocks(workflow_text)[job["job_id"]]
        self.assertEqual(actual, job["raw_text"])
        self.assertEqual(hashlib.sha256(actual.encode("utf-8")).hexdigest(), job["sha256"])


class ProMaxRepositoryTargetTests(unittest.TestCase):
    def test_crossframe_skill_inventory_has_sixteen_entries(self) -> None:
        skills = sorted(
            path.name
            for path in (ROOT / "skills").iterdir()
            if path.is_dir() and (path / "SKILL.md").is_file()
        )
        self.assertEqual(len(skills), 16, f"expected 16 CrossFrame skills, got {len(skills)}")
        self.assertIn("crossframe-promax", skills)

    def test_promax_canonical_skill_exists(self) -> None:
        path = ROOT / "skills/crossframe-promax/SKILL.md"
        self.assertTrue(path.is_file(), path.as_posix())

    def test_promax_claude_command_exists(self) -> None:
        path = ROOT / ".claude/commands/crossframe-promax.md"
        self.assertTrue(path.is_file(), path.as_posix())

    def test_suite_routes_named_promax_before_max(self) -> None:
        for path in SUITE_ROUTE_PATHS:
            text = path.read_text(encoding="utf-8")
            lower = text.lower()
            with self.subTest(path=path.relative_to(ROOT).as_posix()):
                self.assertTrue(
                    "crossframe-promax" in lower,
                    f"missing named ProMax route in {path.relative_to(ROOT).as_posix()}",
                )
                self.assertIn("crossframe-max", lower)
                self.assertLess(lower.index("crossframe-promax"), lower.index("crossframe-max"))
                self.assertRegex(lower, r"named-only|精确点名|显式点名")

    def test_generic_maximum_requests_still_route_to_max(self) -> None:
        text = (ROOT / "skills/crossframe-suite/SKILL.md").read_text(encoding="utf-8")
        matching_lines = [line for line in text.splitlines() if "最大算力" in line]
        self.assertTrue(matching_lines)
        self.assertTrue(
            any("crossframe-max" in line and "crossframe-promax" not in line for line in matching_lines)
        )

    def test_named_max_still_identifies_the_existing_max_skill(self) -> None:
        text = (ROOT / "skills/crossframe-max/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("name: crossframe-max", text)
        for form in ("crossframe-max", "$crossframe-max", "/crossframe-max"):
            self.assertIn(form, text)


if __name__ == "__main__":
    unittest.main()
