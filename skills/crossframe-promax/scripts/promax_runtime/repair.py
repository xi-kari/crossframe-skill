from __future__ import annotations

import copy
from typing import Mapping, Sequence

from .paths import validate_relative_artifact_path
from .schemas import validate_instance
from .state_machine import PHASES, downstream_phases


_FAILURE_KEYS = {
    "failure_code",
    "affected_artifact_paths",
    "affected_phase",
    "evidence",
}


def build_repair_plan(
    failed_report: Mapping[str, object],
    failures: Sequence[Mapping[str, object]],
    *,
    created_at: str,
) -> dict[str, object]:
    if not isinstance(failed_report, Mapping):
        raise ValueError("failed_report must be a structured object")
    if not isinstance(failures, Sequence) or isinstance(failures, (str, bytes)):
        raise ValueError("failures must be a structured sequence")
    if not failures:
        raise ValueError("a repair plan requires at least one failure")
    normalized: list[dict[str, object]] = []
    path_spellings: dict[str, str] = {}
    for index, failure in enumerate(failures, start=1):
        if not isinstance(failure, Mapping) or set(failure) != _FAILURE_KEYS:
            raise ValueError(f"failure {index} must have the closed repair shape")
        record = copy.deepcopy(dict(failure))
        if record.get("affected_phase") not in PHASES:
            raise ValueError(f"failure {index} has an unknown affected phase")
        paths = record.get("affected_artifact_paths")
        evidence = record.get("evidence")
        if not isinstance(paths, list) or not paths:
            raise ValueError(f"failure {index} has no affected artifact")
        normalized_paths: list[str] = []
        for path in paths:
            canonical_path = validate_relative_artifact_path(path)
            folded = canonical_path.casefold()
            prior = path_spellings.get(folded)
            if prior is not None and prior != canonical_path:
                raise ValueError(
                    "repair failures contain casefold artifact aliases: "
                    f"{prior!r} and {canonical_path!r}"
                )
            path_spellings[folded] = canonical_path
            normalized_paths.append(canonical_path)
        if len(set(normalized_paths)) != len(normalized_paths):
            raise ValueError(f"failure {index} contains duplicate affected paths")
        record["affected_artifact_paths"] = normalized_paths
        if not isinstance(evidence, list) or not evidence:
            raise ValueError(f"failure {index} has no evidence")
        normalized.append(record)
    earliest = min(
        (record["affected_phase"] for record in normalized),
        key=PHASES.index,
    )
    expected_paths = sorted(
        {
            path
            for record in normalized
            for path in record["affected_artifact_paths"]
        }
    )
    if not isinstance(created_at, str) or not created_at.strip():
        raise ValueError("created_at must be a non-empty timestamp")
    plan: dict[str, object] = {
        "schema_id": "crossframe.promax.v8.repair-plan",
        "schema_version": 1,
        "run_id": failed_report.get("run_id"),
        "source_snapshot_sha256": failed_report.get("source_snapshot_sha256"),
        "failed_report_sha256": failed_report.get("report_sha256"),
        "failures": normalized,
        "reset_from_phase": earliest,
        "invalidated_phases": list(downstream_phases(earliest)),
        "repair_actions": [
            {
                "action_id": "REPAIR-1",
                "phase_id": earliest,
                "description": (
                    f"Repair the earliest affected phase {earliest}, rebuild all "
                    "invalidated descendants, regenerate the manifest, and rerun "
                    "the validator set"
                ),
                "expected_output_paths": expected_paths,
            }
        ],
        "revalidation_required": True,
        "created_at": created_at.strip(),
    }
    validate_instance("promax-repair-plan.schema.json", plan)
    return plan
