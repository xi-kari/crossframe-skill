from __future__ import annotations

import copy
import json
import sys
import tempfile
from pathlib import Path

from check_crossframe_max_artifacts import (
    REQUIRED_DOSSIER_HEADINGS,
    REQUIRED_DOSSIER_MARKERS,
    REQUIRED_ESSAY_MARKERS,
    REQUIRED_FULL_SOURCE_FILES,
    REQUIRED_INDEX_MARKERS,
    REQUIRED_LEDGER_MARKERS,
    REQUIRED_MANIFEST_MARKERS,
    check_crossframe_max_artifacts,
)
from check_crossframe_max_read_ledger import EXPECTED_FILE_RANGES, EXPECTED_TOTAL_PARAGRAPHS
from check_crossframe_max_route_ledgers import check


ROUTE_CONCEPTS = [
    "工具准入",
    "过程性产物边界",
    "开放断言",
    "命题验证表",
    "强判断八件套",
    "观测反身性",
    "反模型殖民",
    "概念武器化",
]

ROUTE_LAYERS = [
    "01-guide.md",
    "02-boundary-layer.md",
    "05-interface-layer.md",
    "06-tool-layer.md",
    "09-governance-layer.md",
]

ROUTE_OUTPUTS = [
    "max-local-world-model",
    "max-concept-graph",
    "max-evidence-reasoning-audit",
    "max-red-team-pass",
]

FORBIDDEN_OUTPUTS = [
    "把 prompt 当作概念本体",
    "让运行入口吞掉长协议",
    "让工具输出越过行动上限",
]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def base_fixture() -> dict[str, object]:
    concept_hits = []
    for index, concept in enumerate(ROUTE_CONCEPTS, start=1):
        concept_hits.append(
            {
                "concept_id": concept,
                "hit_type": "direct",
                "trigger_variable": f"skill-design-variable-{index}",
                "registry_anchor": "concept-registry/index.md",
                "source_ranges_from_registry": ["P0276-P0355"],
                "source_ranges_read": ["P0276-P0355"],
                "source_paragraph_ids": ["P0276"],
                "contract_id": f"v6-core-contracts.md#{concept}",
                "contract_checked": True,
                "downgraded_after_source_read": False,
            }
        )
    return {
        "max-read-plan.json": {
            "phase": "read-plan",
            "route_key": "skill_design",
            "route_map_version": "v6.0",
            "final_full_source_required": True,
            "required_full_source_files": REQUIRED_FULL_SOURCE_FILES,
            "route_required_layers": ROUTE_LAYERS,
            "route_required_concepts": ROUTE_CONCEPTS,
            "route_required_outputs": ROUTE_OUTPUTS,
            "route_forbidden_outputs_checked": [
                {"forbidden_output": value, "checked": True, "present": False}
                for value in FORBIDDEN_OUTPUTS
            ],
        },
        "max-concept-hit-ledger.json": {"concept_hits": concept_hits},
        "max-claim-ledger.json": {
            "claims": [
                {
                    "claim_id": "CL1",
                    "claim": "The skill entry must remain a boundary, not the concept body.",
                    "claim_type": "mechanism_candidate",
                    "source_anchor": "P0276-P0355",
                    "source_paragraph_ids": ["P0276"],
                    "concept_ids": ROUTE_CONCEPTS,
                    "v6_rule_ids": ROUTE_CONCEPTS,
                    "design_decision_id": "DD1",
                    "evidence_status": "full",
                    "counterevidence_status": "searched",
                    "downgrade_condition": "If route concepts are not consumed, downgrade to incomplete design review.",
                    "withdrawal_condition": "Withdraw if the entry is used as protocol authority.",
                    "action_limit": "May guide skill design; may not certify external reality.",
                }
            ]
        },
        "max-evidence-reasoning-audit.json": {
            "audits": [
                {
                    "claim_id": "CL1",
                    "design_decision_id": "DD1",
                    "source_paragraph_ids": ["P0276"],
                    "evidence_chain": ["P0276-P0355", "P3103-P3116"],
                    "reasoning_chain": [
                        "skill object -> tool admission",
                        "tool admission -> process artifact boundary",
                        "process boundary -> action limit",
                    ],
                    "counterevidence": ["route concept missing would invalidate this decision"],
                    "counterevidence_status": "searched",
                    "calibration_rounds": [
                        {
                            "round": 1,
                            "result": "kept",
                            "reason": "Decision remains inside process artifact boundaries.",
                        }
                    ],
                    "final_strength": "mechanism_candidate",
                    "withdrawal_condition": "Withdraw if route-ledger validation fails.",
                    "final_output_allowed": True,
                }
            ]
        },
        "max-dossier.md": "clean artifact text",
        "max-essay.md": "clean artifact text",
    }


def write_fixture(workspace: Path, fixture: dict[str, object]) -> None:
    for filename, value in fixture.items():
        path = workspace / filename
        if filename.endswith(".json"):
            path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        else:
            path.write_text(str(value) + "\n", encoding="utf-8")


def run_case(name: str, fixture: dict[str, object], expected_fragment: str | None) -> None:
    with tempfile.TemporaryDirectory(prefix=f"crossframe-max-route-{name}-") as temp_dir:
        workspace = Path(temp_dir)
        write_fixture(workspace, fixture)
        errors = check(workspace, repo_root() / "skills" / "crossframe-max")
    if expected_fragment is None:
        if errors:
            raise AssertionError(f"{name}: expected pass, got {errors}")
        return
    if not any(expected_fragment in error for error in errors):
        raise AssertionError(f"{name}: expected {expected_fragment!r}, got {errors}")


def marker_blob(markers: list[str], repeat: int = 1) -> str:
    return "\n".join(markers * repeat) + "\n"


def write_full_artifact_fixture(workspace: Path) -> None:
    fixture = base_fixture()
    write_fixture(workspace, fixture)
    read_files = []
    for file_name in REQUIRED_FULL_SOURCE_FILES:
        start, end = EXPECTED_FILE_RANGES[file_name]
        read_files.append(
            {
                "file": file_name,
                "expected_range": [start, end],
                "read_ranges": [[start, end]],
                "status": "full",
                "layer_digest": f"digest-{file_name}",
            }
        )
    (workspace / "max-read-ledger.json").write_text(
        json.dumps(
            {
                "total_expected_paragraphs": EXPECTED_TOTAL_PARAGRAPHS,
                "total_read_paragraphs": EXPECTED_TOTAL_PARAGRAPHS,
                "full_source_exhaustive_pass": True,
                "missing_paragraphs": [],
                "files": read_files,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    (workspace / "max-run-contract.json").write_text(
        json.dumps(
            {
                "run_mode": "crossframe-v6-max",
                "max_run_level": "max-complete",
                "final_output_allowed": False,
                "forbidden_behavior": ["output before lock"],
                "affected_phase_reset_rule": "affected phase reset",
                "phase_exception_rule": "phase_exception_record",
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    (workspace / "max-source-snapshot.json").write_text(
        json.dumps(
            {
                "source_snapshot_id": "source_snapshot_001",
                "total_paragraphs": 3273,
                "full_source_exhaustive_pass": True,
                "table_count": 60,
                "frozen": True,
                "source_anchor_verification_only_after_freeze": True,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    (workspace / "max-worldview-capsule.locked.md").write_text(
        "locked: true\nsource_snapshot_id\n本轮预先设计的世界观\nworldview_exception_record\n",
        encoding="utf-8",
    )
    (workspace / "max-local-world-model.locked.md").write_text(
        "locked: true\n局部世界\n对象边界\n主体位置\n承接链\n只建模，不下最终判断\n",
        encoding="utf-8",
    )
    (workspace / "max-claim-board.json").write_text(
        json.dumps(
            {
                "claims": [
                    {
                        "claim_id": "CL1",
                        "status": "final",
                        "source_paragraph_ids": ["P0276"],
                        "concept_ids": ROUTE_CONCEPTS,
                        "needs_evidence": True,
                        "needs_counterevidence": True,
                    }
                ]
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    (workspace / "max-audit-board.json").write_text(
        json.dumps(
            {
                "red_team_final_text_authority": False,
                "audits": [
                    {
                        "claim_id": "CL1",
                        "audit_result": "keep",
                        "final_status": "final",
                        "source_paragraph_ids": ["P0276"],
                        "counterevidence_status": "searched",
                    }
                ],
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    (workspace / "max-output-plan.locked.md").write_text(
        marker_blob(
            [
                "locked: true",
                "进入正文的 claim",
                "降档表达的 claim",
                "撤回的 claim",
                "进入不可判断区的 claim",
                "不可写强的句子",
                "必须保留的撤回条件",
                "max-essay.md may now be written",
            ]
        ),
        encoding="utf-8",
    )
    dossier = "\n".join(REQUIRED_DOSSIER_HEADINGS) + "\n" + marker_blob(REQUIRED_DOSSIER_MARKERS + REQUIRED_FULL_SOURCE_FILES)
    essay = marker_blob(REQUIRED_ESSAY_MARKERS, repeat=80)
    ledger = marker_blob(REQUIRED_LEDGER_MARKERS + REQUIRED_FULL_SOURCE_FILES)
    (workspace / "max-artifact-manifest.md").write_text(marker_blob(REQUIRED_MANIFEST_MARKERS), encoding="utf-8")
    (workspace / "max-dossier.md").write_text(dossier, encoding="utf-8")
    (workspace / "max-essay.md").write_text(essay, encoding="utf-8")
    (workspace / "max-continuation-ledger.md").write_text(ledger, encoding="utf-8")
    (workspace / "max-continuation-index.md").write_text(marker_blob(REQUIRED_INDEX_MARKERS), encoding="utf-8")


def main() -> int:
    artifact_validator = (repo_root() / "scripts" / "check_crossframe_max_artifacts.py").read_text(encoding="utf-8")
    if "check_crossframe_max_route_ledgers" not in artifact_validator or "check_route_ledgers" not in artifact_validator:
        raise AssertionError("artifact validator must call check_crossframe_max_route_ledgers")

    valid = base_fixture()
    run_case("valid-skill-design", valid, None)

    missing_route = copy.deepcopy(valid)
    del missing_route["max-read-plan.json"]["route_key"]  # type: ignore[index]
    run_case("missing-route-key", missing_route, "route_key")

    missing_concept = copy.deepcopy(valid)
    missing_concept["max-read-plan.json"]["route_required_concepts"] = ROUTE_CONCEPTS[:-1]  # type: ignore[index]
    run_case("missing-required-concept", missing_concept, "missing route required_concepts")

    fake_concept = copy.deepcopy(valid)
    fake_concept["max-concept-hit-ledger.json"]["concept_hits"][0]["concept_id"] = "不存在概念"  # type: ignore[index]
    run_case("fake-concept-id", fake_concept, "not found in concept registry")

    missing_v6_rule = copy.deepcopy(valid)
    del missing_v6_rule["max-claim-ledger.json"]["claims"][0]["v6_rule_ids"]  # type: ignore[index]
    run_case("missing-v6-rule-ids", missing_v6_rule, "missing v6_rule_ids")

    missing_action_limit = copy.deepcopy(valid)
    del missing_action_limit["max-claim-ledger.json"]["claims"][0]["action_limit"]  # type: ignore[index]
    run_case("missing-action-limit", missing_action_limit, "missing action_limit")

    forbidden_artifact = copy.deepcopy(valid)
    forbidden_artifact["max-dossier.md"] = "把 prompt 当作概念本体"
    run_case("forbidden-output", forbidden_artifact, "forbidden output appears")

    with tempfile.TemporaryDirectory(prefix="crossframe-max-full-artifact-") as temp_dir:
        workspace = Path(temp_dir)
        write_full_artifact_fixture(workspace)
        errors = check_crossframe_max_artifacts(workspace, repo_root() / "skills" / "crossframe-max")
        if errors:
            raise AssertionError(f"full artifact fixture: expected pass, got {errors}")

    with tempfile.TemporaryDirectory(prefix="crossframe-max-short-essay-") as temp_dir:
        workspace = Path(temp_dir)
        write_full_artifact_fixture(workspace)
        (workspace / "max-essay.md").write_text(marker_blob(REQUIRED_ESSAY_MARKERS), encoding="utf-8")
        errors = check_crossframe_max_artifacts(workspace, repo_root() / "skills" / "crossframe-max")
        if not any("longform-dominance gate failed" in error for error in errors):
            raise AssertionError(f"short essay fixture: expected longform failure, got {errors}")

    with tempfile.TemporaryDirectory(prefix="crossframe-max-coverage-") as temp_dir:
        workspace = Path(temp_dir)
        write_full_artifact_fixture(workspace)
        coverage_missing = marker_blob([marker for marker in REQUIRED_ESSAY_MARKERS if marker != "局部世界"], repeat=80)
        (workspace / "max-essay.md").write_text(coverage_missing, encoding="utf-8")
        errors = check_crossframe_max_artifacts(workspace, repo_root() / "skills" / "crossframe-max")
        if not any("missing marker: 局部世界" in error for error in errors):
            raise AssertionError(f"coverage fixture: expected missing marker, got {errors}")

    with tempfile.TemporaryDirectory(prefix="crossframe-max-missing-route-") as temp_dir:
        workspace = Path(temp_dir)
        write_full_artifact_fixture(workspace)
        read_plan = json.loads((workspace / "max-read-plan.json").read_text(encoding="utf-8"))
        del read_plan["route_key"]
        (workspace / "max-read-plan.json").write_text(
            json.dumps(read_plan, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        errors = check_crossframe_max_artifacts(workspace, repo_root() / "skills" / "crossframe-max")
        if not any("missing route_key" in error for error in errors):
            raise AssertionError(f"missing route fixture: expected route_key failure, got {errors}")

    print("ok: crossframe max route-ledger fixtures passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
