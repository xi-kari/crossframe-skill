from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


FORBIDDEN_SCORE_KEYS = {
    "total_score",
    "overall_score",
    "average_score",
    "weighted_score",
    "final_score",
    "rank_score",
    "prediction_probability",
    "collapse_probability",
    "health_score",
    "personality_score",
    "disposition_basis",
}

EXPECTED_ERROR_MARKERS = {
    "seven-gates-quant/invalid-total-score.json": ["forbidden totalizing score key: total_score"],
    "seven-gates-quant/invalid-fail-allows-strong.json": [
        "failed or blocked gate cannot allow strong_judgment"
    ],
    "seven-gates-quant/invalid-power-public-pressure.json": [
        "power gate below 3 cannot allow public pressure"
    ],
    "evidence-ledger-v6/invalid-strong-without-source-ledger.json": [
        "strong_judgment requires source_ledger_id"
    ],
    "evidence-ledger-v6/invalid-claim-without-withdrawal.json": ["CL4 missing withdrawal_condition"],
    "evidence-ledger-v6/invalid-low-cost-strong-judgment.json": [
        "low cost evidence cannot support strong_judgment"
    ],
    "calibration-anchor/invalid-missing-misuse-risk.json": ["'misuse_risks' is a required property"],
    "calibration-anchor/invalid-totalizing-construct.json": ["forbidden totalizing score key: health_score"],
    "mechanism-update/invalid-withdraw-without-counterevidence.json": [
        "[] should be non-empty"
    ],
    "mechanism-update/invalid-strong-judgment-without-source-ledger.json": [
        "strong_judgment requires source_ledger_id"
    ],
    "counterexample-register/invalid-missing-writeback.json": [
        "'version_writeback' is a required property"
    ],
    "counterexample-register/invalid-misuse-without-action-change.json": [
        "misuse or high_harm counterexample requires action_ceiling_change"
    ],
}


@dataclass(frozen=True)
class SchemaTarget:
    schema_id: str
    schema_path: Path
    fixture_dir: Path


TARGETS = [
    SchemaTarget(
        "seven-gates-quant",
        Path("skills/crossframe/schemas/seven-gates-quant.schema.json"),
        Path("skills/crossframe/schemas/fixtures/v6/seven-gates-quant"),
    ),
    SchemaTarget(
        "evidence-ledger-v6",
        Path("skills/crossframe/schemas/evidence-ledger-v6.schema.json"),
        Path("skills/crossframe/schemas/fixtures/v6/evidence-ledger-v6"),
    ),
    SchemaTarget(
        "calibration-anchor",
        Path("skills/crossframe/schemas/calibration-anchor.schema.json"),
        Path("skills/crossframe/schemas/fixtures/v6/calibration-anchor"),
    ),
    SchemaTarget(
        "mechanism-update",
        Path("skills/crossframe/schemas/mechanism-update.schema.json"),
        Path("skills/crossframe/schemas/fixtures/v6/mechanism-update"),
    ),
    SchemaTarget(
        "counterexample-register",
        Path("skills/crossframe/schemas/counterexample-register.schema.json"),
        Path("skills/crossframe/schemas/fixtures/v6/counterexample-register"),
    ),
]


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def walk_dicts(value: Any) -> list[dict[str, Any]]:
    found: list[dict[str, Any]] = []
    if isinstance(value, dict):
        found.append(value)
        for child in value.values():
            found.extend(walk_dicts(child))
    elif isinstance(value, list):
        for child in value:
            found.extend(walk_dicts(child))
    return found


def semantic_errors(instance: Any) -> list[str]:
    errors: list[str] = []
    for item in walk_dicts(instance):
        forbidden = FORBIDDEN_SCORE_KEYS.intersection(item)
        for key in sorted(forbidden):
            errors.append(f"forbidden totalizing score key: {key}")

        if item.get("judgment_grade") == "strong_judgment" and not item.get("source_ledger_id"):
            errors.append("strong_judgment requires source_ledger_id")

        if item.get("claim_id") and not item.get("withdrawal_condition"):
            errors.append(f"{item['claim_id']} missing withdrawal_condition")

        if item.get("claim_id") and not item.get("action_ceiling"):
            errors.append(f"{item['claim_id']} missing action_ceiling")

        if item.get("evidence_cost") == "low" and item.get("judgment_grade") == "strong_judgment":
            errors.append("low cost evidence cannot support strong_judgment")

        if item.get("gate_state") in {"fail", "blocked"} and item.get("max_judgment_grade") == "strong_judgment":
            errors.append("failed or blocked gate cannot allow strong_judgment")

        if item.get("gate_id") == "power" and item.get("score", 0) < 3 and item.get("allows_public_pressure") is True:
            errors.append("power gate below 3 cannot allow public pressure")

        if item.get("counterexample_type") in {"misuse", "high_harm"}:
            if not item.get("action_ceiling_change"):
                errors.append("misuse or high_harm counterexample requires action_ceiling_change")
            if not item.get("tool_consequence"):
                errors.append("misuse or high_harm counterexample requires tool_consequence")

    return errors


def validate_target(repo: Path, target: SchemaTarget) -> int:
    schema_path = repo / target.schema_path
    fixture_dir = repo / target.fixture_dir
    if not schema_path.exists():
        raise SystemExit(f"missing v6 schema: {schema_path}")
    if not fixture_dir.is_dir():
        raise SystemExit(f"missing v6 fixture directory: {fixture_dir}")

    schema = load_json(schema_path)
    validator = Draft202012Validator(schema)
    fixtures = sorted(fixture_dir.glob("*.json"))
    if not fixtures:
        raise SystemExit(f"missing v6 fixtures: {fixture_dir}")

    checked = 0
    for fixture in fixtures:
        instance = load_json(fixture)
        schema_errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.path))
        extra_errors = semantic_errors(instance)
        errors = [error.message for error in schema_errors] + extra_errors
        should_pass = fixture.name.startswith("valid-")
        should_fail = fixture.name.startswith("invalid-")

        if not should_pass and not should_fail:
            raise SystemExit(f"fixture name must start with valid- or invalid-: {fixture}")
        if should_pass and errors:
            details = "\n".join(f"- {message}" for message in errors)
            raise SystemExit(f"valid fixture failed v6 validation: {fixture.name}\n{details}")
        if should_fail and not errors:
            raise SystemExit(f"invalid fixture unexpectedly passed v6 validation: {fixture.name}")
        if should_fail:
            marker_key = f"{target.schema_id}/{fixture.name}"
            expected_markers = EXPECTED_ERROR_MARKERS.get(marker_key, [])
            error_text = "\n".join(errors)
            for marker in expected_markers:
                if marker not in error_text:
                    raise SystemExit(
                        f"invalid fixture failed for the wrong reason: {fixture.name}\n"
                        f"missing expected error marker: {marker}\n"
                        f"actual errors:\n{error_text}"
                    )
        checked += 1

    print(f"ok: {target.schema_id} fixtures validated: {checked}")
    return checked


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate CrossFrame v6 quantification schema fixtures.")
    parser.add_argument("--repo", default=".", help="Repository root.")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    total = 0
    for target in TARGETS:
        total += validate_target(repo, target)
    print(f"ok: v6 quantification schema fixtures validated: {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
