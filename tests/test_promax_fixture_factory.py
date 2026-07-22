from __future__ import annotations

import io
import json
from pathlib import Path
import sys
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
CANONICAL_SCRIPTS = ROOT / "skills/crossframe-promax/scripts"
sys.path.insert(0, str(CANONICAL_SCRIPTS))

import crossframe_promax_fixture_factory as fixture_factory
from promax_runtime.source_integrity import (
    V8_SOURCE_SNAPSHOT_SHA256,
    validate_read_event_coverage,
)
from promax_runtime.concept_closure import validate_concept_closure
from promax_runtime.claim_path import validate_claim_path_saturation
from promax_runtime.retrieval import validate_retrieval_saturation
from promax_runtime.schemas import validate_instance
from promax_runtime.position import (
    validate_position_semantics,
    validate_recommendation_semantics,
)


REQUIRED_SCENARIOS = {
    "valid-complete",
    "artifact-incomplete",
    "marker-stuffing",
    "empty-strings",
    "forged-read-coverage",
    "equal-count-source-mutation",
    "unsupported-url",
    "duplicate-sources-independent",
    "missing-reverse",
    "no-action-omitted",
    "stance-flip",
    "authorization-leakage",
    "untyped-examples",
    "phase-replay",
    "stale-manifest",
    "wrong-continuation-parent",
}


class ProMaxFixtureFactoryTests(unittest.TestCase):
    def test_read_event_factory_materializes_exact_full_source_proof(self) -> None:
        events = fixture_factory.build_read_events(
            ROOT,
            run_id="promax-fixture-factory-test",
            read_at="2026-07-23T14:00:00Z",
        )
        self.assertEqual(len(events), 3980)
        self.assertEqual(events[0]["source_anchor"], "V8-P0001")
        self.assertEqual(events[-1]["source_anchor"], "V8-T117")
        summary = validate_read_event_coverage(
            events,
            repo=ROOT,
            expected_run_id="promax-fixture-factory-test",
            expected_source_snapshot_sha256=V8_SOURCE_SNAPSHOT_SHA256,
        )
        self.assertEqual(summary["paragraph_count"], 3863)
        self.assertEqual(summary["table_count"], 117)

    def test_concept_factory_materializes_all_709_terminal_dispositions(self) -> None:
        document = fixture_factory.build_concept_disposition(
            ROOT,
            run_id="promax-fixture-factory-test",
            completed_at="2026-07-23T14:30:00Z",
        )
        self.assertEqual(len(document["dispositions"]), 709)
        result = validate_concept_closure(
            document,
            repo=ROOT,
            expected_run_id="promax-fixture-factory-test",
            expected_source_snapshot_sha256=V8_SOURCE_SNAPSHOT_SHA256,
            required_route_ids=tuple(document["route_ids"]),
        )
        self.assertTrue(result["closure_complete"])
        self.assertEqual(result["unchecked_concept_ids"], [])

    def test_claim_path_factory_materializes_a_three_mechanism_closed_dag(self) -> None:
        document = fixture_factory.build_claim_path_graph(
            run_id="promax-fixture-factory-test",
            updated_at="2026-07-23T15:00:00Z",
        )
        result = validate_claim_path_saturation(
            document,
            expected_run_id="promax-fixture-factory-test",
            expected_source_snapshot_sha256=V8_SOURCE_SNAPSHOT_SHA256,
        )
        self.assertEqual(len(result["mechanisms"]), 3)
        self.assertEqual(
            result["central_claim_cycle"]["central_claim_id"],
            result["central_claim_id"],
        )

    def test_retrieval_factory_materializes_five_directions_and_two_real_rounds(self) -> None:
        document = fixture_factory.build_retrieval_ledger(
            run_id="promax-fixture-factory-test",
            completed_at="2026-07-23T15:30:00Z",
        )
        result = validate_retrieval_saturation(
            document,
            expected_run_id="promax-fixture-factory-test",
            expected_source_snapshot_sha256=V8_SOURCE_SNAPSHOT_SHA256,
            required_claim_ids=("CLAIM-CENTRAL",),
        )
        self.assertEqual(len(result["entries"]), 5)
        self.assertEqual({entry["round"] for entry in result["entries"]}, {1, 2})

    def test_local_world_factory_emits_the_complete_p3_contract(self) -> None:
        document = fixture_factory.build_local_world_model(
            run_id="promax-fixture-factory-test",
            locked_at="2026-07-23T16:00:00Z",
        )
        validate_instance("promax-local-world-model.schema.json", document)
        self.assertEqual(document["phase_id"], "P3")
        self.assertTrue(document["action_limits"])
        self.assertTrue(document["authorization_limits"])

    def test_judgment_factory_locks_attack_position_and_six_way_recommendation(self) -> None:
        graph = fixture_factory.build_claim_path_graph(
            run_id="promax-fixture-factory-test",
            updated_at="2026-07-23T16:00:00Z",
        )
        red_team = fixture_factory.build_red_team_report(
            run_id="promax-fixture-factory-test",
            completed_at="2026-07-23T16:30:00Z",
        )
        position = fixture_factory.build_position_lock(
            run_id="promax-fixture-factory-test",
            locked_at="2026-07-23T17:00:00Z",
        )
        validated_position = validate_position_semantics(
            position,
            red_team_report=red_team,
            claim_path_graph=graph,
            expected_run_id="promax-fixture-factory-test",
            expected_source_snapshot_sha256=V8_SOURCE_SNAPSHOT_SHA256,
        )
        recommendation = fixture_factory.build_recommendation_lock(
            validated_position,
            run_id="promax-fixture-factory-test",
            locked_at="2026-07-23T17:30:00Z",
        )
        validated = validate_recommendation_semantics(
            {
                "run_id": "promax-fixture-factory-test",
                "source_snapshot_sha256": V8_SOURCE_SNAPSHOT_SHA256,
                "recommendation_required": True,
            },
            recommendation,
            position=validated_position,
            expected_run_id="promax-fixture-factory-test",
            expected_source_snapshot_sha256=V8_SOURCE_SNAPSHOT_SHA256,
        )
        self.assertEqual(len(validated["options"]), 6)
        self.assertEqual(validated["preferred_option_id"], validated["ranking"][0])

    def test_output_factory_traces_every_major_mechanism_and_applied_concept(self) -> None:
        plan = fixture_factory.build_output_plan(
            run_id="promax-fixture-factory-test",
            locked_at="2026-07-23T18:00:00Z",
        )
        validate_instance("promax-output-plan.schema.json", plan)
        section = plan["sections"][0]
        self.assertEqual(
            section["concept_ids"],
            [fixture_factory.FIXTURE_CONCEPT_ID],
        )
        self.assertEqual(
            set(section["example_ids"]),
            {
                "EX-M1-S1",
                "EX-M1-S2",
                "EX-M2-S1",
                "EX-M2-S2",
                "EX-M3-S1",
                "EX-M3-S2",
            },
        )
        self.assertEqual(
            set(section["counterexample_ids"]),
            {"EX-M1-F1", "EX-M2-F1", "EX-M3-F1"},
        )

        deliverables = fixture_factory.build_deliverables(ROOT)
        self.assertEqual(
            set(deliverables),
            {
                "promax-dossier.md",
                "promax-concept-atlas.md",
                "promax-case-and-countercase.md",
                "promax-essay.md",
            },
        )
        atlas = deliverables["promax-concept-atlas.md"]
        self.assertIn("V8-CANON-ACTOR-STATE", atlas)
        self.assertIn("A* 行动者候选状态", atlas)
        self.assertIn("行动者 ID", atlas)
        cases = deliverables["promax-case-and-countercase.md"]
        for mechanism in ("MECH-1", "MECH-2", "MECH-3"):
            self.assertEqual(cases.count(f"mechanism={mechanism} | relation=similar"), 2)
            self.assertEqual(cases.count(f"mechanism={mechanism} | relation=failure"), 1)

    def test_catalog_is_closed_complete_and_has_all_fixture_classes(self) -> None:
        catalog = fixture_factory.load_scenario_catalog(ROOT)
        self.assertEqual(catalog["schema_version"], 1)
        scenarios = catalog["scenarios"]
        self.assertEqual(
            {scenario["scenario_id"] for scenario in scenarios},
            REQUIRED_SCENARIOS,
        )
        self.assertEqual(
            {scenario["fixture_class"] for scenario in scenarios},
            {"positive", "incomplete", "adversarial"},
        )
        for scenario in scenarios:
            self.assertEqual(
                set(scenario),
                {
                    "scenario_id",
                    "fixture_class",
                    "mutation",
                    (
                        "expected_outcome"
                        if scenario["fixture_class"] != "adversarial"
                        else "expected_error_type"
                    ),
                },
            )

    def test_list_cli_reports_the_canonical_catalog_and_root_entry_is_thin(self) -> None:
        output = io.StringIO()
        with mock.patch("sys.stdout", output):
            exit_code = fixture_factory.main(["list", "--repo", str(ROOT)])
        self.assertEqual(exit_code, 0)
        status = json.loads(output.getvalue())
        self.assertEqual(status["status"], "ok")
        self.assertEqual(set(status["scenario_ids"]), REQUIRED_SCENARIOS)

        root_entry = ROOT / "scripts/crossframe_promax_fixture_factory.py"
        text = root_entry.read_text(encoding="utf-8")
        self.assertIn("runpy.run_path", text)
        self.assertNotIn("ArgumentParser", text)
        self.assertLess(len(text), 2000)


if __name__ == "__main__":
    unittest.main()
