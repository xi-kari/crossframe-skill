from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVAL_ROOT = ROOT / "tests/evals/promax-red"
SCENARIOS_PATH = EVAL_ROOT / "scenarios.json"
README_PATH = EVAL_ROOT / "README.md"
PROMAX_ROOT = ROOT / "skills/crossframe-promax"
PROMAX_SKILL = PROMAX_ROOT / "SKILL.md"

EXPECTED_SCENARIO_IDS = (
    "A1",
    "A2",
    "A3",
    "B1",
    "B2",
    "B3",
    "B4",
    "C1",
    "C2",
    "C3",
    "C4",
    "D1",
)
EXPLICIT_ONLY_FORMS = (
    "crossframe-promax",
    "$crossframe-promax",
    "/crossframe-promax",
    "CrossFrame ProMax",
)
REQUIRED_RUNTIME_MARKERS = (
    "v8-anchor",
    "read-event",
    "concept-terminal-closure",
    "claim-path",
    "retrieval-ledger",
    "red-team-saturation",
    "typed-example",
    "artifact-contract",
    "artifact-validation",
    "position-ledger",
    "recommendation-ledger",
    "continuation-ledger",
    "validator",
    "repair-loop",
)
EXPECTED_RAW_SHA256 = {
    "A1": "6fabf3a24e252f160415fa455f9a94507abffc394726b330e83c7709d3c4a3fb",
    "A2": "1e864f8e6319e705cad1252e52a8cfe9556ff1b3129be552c11e32f66dbd01df",
    "A3": "7e4b08392527860a434cc0ff96323eb404bd18b6d83f17165a0fa62cf3ab3569",
    "B1": "36cf68f3dbb46df1a88df3d5a56694fc67d5ef8a6b4e088fc572ba025a2eb58d",
    "B2": "75da140fc6363aaecaaba1da68896a10266e6322c4c9d7b637d7526658016019",
    "B3": "3aef05681b3684a15f8a32c4a9137aad0197fd7b54726ac8d61d1de79ad6b63f",
    "B4": "7fa2631d8d19a1d614bbe823552ecb063e2fd8effbb1120d28111e4de58f321f",
    "C1": "ba49ee70d702c18dba7aa38229f84d1c8a7d6ec5188be3e4cabba002d6a8051b",
    "C2": "a62c0ac1ad65de7a4dea37b002227256c8a408b44457a6852a46e316cc547105",
    "C3": "cdf4e08d38e5c7215cfb5baa58e6b1383107dc801b052acc8629280a42bf5ea4",
    "C4": "8a86a76648851a8dfa9dc4a6fbfeb1d3dcca8e563eea27843d002a1122f1e484",
    "D1": "5f4c1b1980a398bd507aa24422fd7b3aa3a42234396be70eb121dc4df78cd5bf",
}


def load_scenarios() -> list[dict[str, object]]:
    return json.loads(SCENARIOS_PATH.read_text(encoding="utf-8"))


def promax_corpus(test: unittest.TestCase) -> str:
    test.assertTrue(
        PROMAX_SKILL.is_file(),
        "CrossFrame ProMax canonical skill is missing: skills/crossframe-promax/SKILL.md",
    )
    files = sorted(
        path
        for path in PROMAX_ROOT.rglob("*")
        if path.is_file() and path.suffix.lower() in {".md", ".json", ".yaml", ".yml", ".py"}
    )
    test.assertTrue(files, "CrossFrame ProMax protocol corpus is empty")
    return "\n".join(path.read_text(encoding="utf-8") for path in files)


class ProMaxRedBaselineCaptureTests(unittest.TestCase):
    def test_scenario_manifest_has_twelve_complete_unique_entries(self) -> None:
        scenarios = load_scenarios()
        self.assertEqual(len(scenarios), 12)
        self.assertEqual(
            tuple(item["scenario_id"] for item in scenarios),
            EXPECTED_SCENARIO_IDS,
        )
        for item in scenarios:
            self.assertEqual(
                set(item),
                {
                    "scenario_id",
                    "prompt",
                    "pressure_tags",
                    "evaluator_context",
                    "raw_response_path",
                },
            )
            self.assertTrue(str(item["prompt"]).strip())
            self.assertTrue(item["pressure_tags"])
            self.assertTrue(str(item["evaluator_context"]).strip())

        contexts = {item["scenario_id"]: str(item["evaluator_context"]) for item in scenarios}
        for scenario_id in ("A1", "A2", "A3", "D1"):
            self.assertIn("Fresh-fork", contexts[scenario_id])
            self.assertIn("not loaded", contexts[scenario_id])
        for scenario_id in ("B1", "B2", "B3", "B4", "C1", "C2", "C3", "C4"):
            self.assertIn("thread limit", contexts[scenario_id])
            self.assertIn("same no-skill evaluator", contexts[scenario_id])

    def test_all_raw_responses_are_present_and_identified(self) -> None:
        for item in load_scenarios():
            scenario_id = str(item["scenario_id"])
            path = ROOT / str(item["raw_response_path"])
            self.assertTrue(path.is_file(), path.as_posix())
            text = path.read_text(encoding="utf-8")
            self.assertTrue(text.startswith(f"## SCENARIO {scenario_id}\n"), path.as_posix())
            self.assertGreater(len(text.strip()), 100, path.as_posix())
            canonical_bytes = path.read_bytes().replace(b"\r\n", b"\n")
            self.assertEqual(
                hashlib.sha256(canonical_bytes).hexdigest(),
                EXPECTED_RAW_SHA256[scenario_id],
                path.as_posix(),
            )

    def test_readme_records_method_limitations_and_observable_gaps(self) -> None:
        text = README_PATH.read_text(encoding="utf-8")
        for marker in (
            "agent thread limit",
            "Safety-preserving judgments are not counted as failures",
            "v8 anchor",
            "read-event",
            "concept terminal closure",
            "claim-path",
            "retrieval ledger",
            "red-team saturation",
            "typed example",
            "artifact validation",
            "C4",
            "Max fallback",
        ):
            self.assertIn(marker, text)
        for scenario_id in EXPECTED_SCENARIO_IDS:
            self.assertRegex(text, rf"(?m)^\| {re.escape(scenario_id)} \|")


class ProMaxTargetBehaviorContractTests(unittest.TestCase):
    def test_canonical_skill_and_protocol_corpus_exist(self) -> None:
        corpus = promax_corpus(self)
        protocol_files = list((PROMAX_ROOT / "protocols").glob("*.md"))
        self.assertTrue(protocol_files, "CrossFrame ProMax protocols are missing")
        self.assertTrue(corpus.strip())

    def test_explicit_only_forms_and_no_max_fallback_contract_exist(self) -> None:
        corpus = promax_corpus(self)
        for form in EXPLICIT_ONLY_FORMS:
            self.assertIn(form, corpus)
        self.assertIn("PROMAX-NAMED-ONLY", corpus)
        self.assertIn("PROMAX-NO-FALLBACK-TO-MAX", corpus)
        self.assertIn("PROMAX-PRIORITY-OVER-MAX", corpus)

    def test_judgment_charter_and_all_twelve_phases_exist(self) -> None:
        corpus = promax_corpus(self)
        self.assertIn("PROMAX-JUDGMENT-CHARTER", corpus)
        for phase in range(12):
            self.assertRegex(corpus, rf"(?<![A-Z0-9])P{phase}(?![0-9])")

    def test_runtime_closure_and_validation_markers_exist(self) -> None:
        corpus = promax_corpus(self)
        for marker in REQUIRED_RUNTIME_MARKERS:
            self.assertIn(marker, corpus, marker)


if __name__ == "__main__":
    unittest.main()
