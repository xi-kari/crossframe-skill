from __future__ import annotations

import argparse
import sys
from pathlib import Path


REQUIRED_CASEBOOK_FILES = [
    "skills/crossframe-casebook/references/v5-dlc-casebook-validation-protocol.md",
    "skills/crossframe-casebook/templates/v5-dlc-quant-case-trial-template.md",
    "skills/crossframe-casebook/templates/v5-dlc-rater-disagreement-record-template.md",
    "skills/crossframe-casebook/examples/v5-dlc-quant-trials/organization-case-trial.md",
    "skills/crossframe-casebook/examples/v5-dlc-quant-trials/relationship-case-trial.md",
    "skills/crossframe-casebook/examples/v5-dlc-quant-trials/public-dispute-case-trial.md",
    "skills/crossframe-casebook/examples/v5-dlc-quant-trials/misuse-counterexample-trial.md",
    "skills/crossframe-casebook/examples/v5-dlc-quant-trials/rater-disagreement-sample.md",
    "skills/crossframe-casebook/examples/v5-dlc-quant-trials/validation-summary.md",
]

TRIAL_FILES = [
    "skills/crossframe-casebook/examples/v5-dlc-quant-trials/organization-case-trial.md",
    "skills/crossframe-casebook/examples/v5-dlc-quant-trials/relationship-case-trial.md",
    "skills/crossframe-casebook/examples/v5-dlc-quant-trials/public-dispute-case-trial.md",
    "skills/crossframe-casebook/examples/v5-dlc-quant-trials/misuse-counterexample-trial.md",
]

SUMMARY_AND_REVIEW_FILES = [
    "skills/crossframe-casebook/examples/v5-dlc-quant-trials/rater-disagreement-sample.md",
    "skills/crossframe-casebook/examples/v5-dlc-quant-trials/validation-summary.md",
]

REQUIRED_TRIAL_KEYS = [
    "trial_id",
    "source_case",
    "case_domain",
    "trial_status",
    "primary_scale",
    "judgment_grade",
    "action_ceiling",
    "downgrade_triggered",
    "anchor_revision_required",
    "template_revision_required",
    "counterexample_pressure",
    "rater_record",
]

TRIAL_ALLOWED_VALUES = {
    "case_domain": {"relationship", "organization", "public_dispute", "misuse_counterexample"},
    "trial_status": {"training", "calibration", "formal", "counterexample"},
    "judgment_grade": {
        "light_observation",
        "open_assertion",
        "full_diagnosis",
        "strong_judgment",
        "low_condition_action",
        "exit_transfer",
    },
    "action_ceiling": {
        "observe",
        "ask_for_evidence",
        "internal_review",
        "publish_with_boundary",
        "block_publication",
        "exit_transfer",
    },
    "downgrade_triggered": {"true", "false"},
    "anchor_revision_required": {"true", "false"},
    "template_revision_required": {"true", "false"},
    "counterexample_pressure": {"none", "weak", "moderate", "strong", "decisive"},
    "rater_record": {"none", "embedded", "separate"},
}

REQUIRED_DISAGREEMENT_KEYS = [
    "conflict_id",
    "source_trial",
    "conflict_type",
    "rater_a_judgment_grade",
    "rater_b_judgment_grade",
    "rater_a_action_ceiling",
    "rater_b_action_ceiling",
    "unresolved",
    "writeback_required",
]

CONFLICT_TYPES = {"judgment_grade", "action_ceiling", "both"}
BOOLEAN_VALUES = {"true", "false"}

FORBIDDEN_LANGUAGE = [
    "total_score",
    "overall_score",
    "average_score",
    "weighted_score",
    "final_score",
    "success_rate",
    "reliability_proved",
    "validated_framework",
    "prediction_probability",
    "casebook_coverage_proves",
    "案例库证明框架正确",
    "一致性证明现实判断为真",
    "覆盖率证明外部有效性",
]

REQUIRED_DOMAINS = {"relationship", "organization", "public_dispute", "misuse_counterexample"}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_marker_values(text: str, keys: list[str]) -> dict[str, str]:
    wanted = set(keys)
    values: dict[str, str] = {}
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        if key in wanted and key not in values:
            values[key] = value.strip()
    return values


def add_error(errors: list[str], rel: str, message: str) -> None:
    errors.append(f"{rel}: {message}")


def check_required_files(repo: Path, errors: list[str]) -> None:
    for rel in REQUIRED_CASEBOOK_FILES:
        if not (repo / rel).exists():
            add_error(errors, rel, "missing required v5 DLC casebook validation file")


def check_forbidden_language(repo: Path, rels: list[str], errors: list[str]) -> None:
    for rel in rels:
        path = repo / rel
        if not path.exists():
            continue
        text = read(path)
        lowered = text.lower()
        for marker in FORBIDDEN_LANGUAGE:
            haystack = lowered if marker.isascii() else text
            needle = marker.lower() if marker.isascii() else marker
            if needle in haystack:
                add_error(errors, rel, f"forbidden proof/score language: {marker}")


def check_trial(repo: Path, rel: str, errors: list[str]) -> dict[str, str] | None:
    path = repo / rel
    if not path.exists():
        return None
    text = read(path)
    markers = parse_marker_values(text, REQUIRED_TRIAL_KEYS)
    missing = [key for key in REQUIRED_TRIAL_KEYS if not markers.get(key)]
    if missing:
        add_error(errors, rel, f"missing marker values: {', '.join(missing)}")
        return markers

    for key, allowed in TRIAL_ALLOWED_VALUES.items():
        value = markers[key]
        if value not in allowed:
            add_error(errors, rel, f"invalid {key}: {value}")

    source_case = repo / markers["source_case"]
    if not source_case.exists():
        add_error(errors, rel, f"source_case does not exist: {markers['source_case']}")

    if "不能证明" not in text:
        add_error(errors, rel, "trial must state what the case cannot prove")
    if "撤回" not in text and "降级" not in text:
        add_error(errors, rel, "trial must state withdrawal or downgrade conditions")

    if markers.get("rater_record") == "embedded":
        if "### rater_a" not in text or "### rater_b" not in text:
            add_error(errors, rel, "embedded rater_record must preserve rater_a and rater_b sections")

    return markers


def check_trials(repo: Path, errors: list[str]) -> None:
    markers_by_file: dict[str, dict[str, str]] = {}
    for rel in TRIAL_FILES:
        markers = check_trial(repo, rel, errors)
        if markers:
            markers_by_file[rel] = markers

    domains = {markers["case_domain"] for markers in markers_by_file.values() if markers.get("case_domain")}
    missing_domains = sorted(REQUIRED_DOMAINS - domains)
    if missing_domains:
        add_error(errors, "skills/crossframe-casebook/examples/v5-dlc-quant-trials", f"missing domains: {', '.join(missing_domains)}")

    formal_or_counterexample = [
        markers for markers in markers_by_file.values()
        if markers.get("trial_status") in {"formal", "counterexample"}
    ]
    if len(formal_or_counterexample) < 3:
        add_error(errors, "skills/crossframe-casebook/examples/v5-dlc-quant-trials", "need at least three formal or counterexample trials")

    writeback_trials = [
        markers for markers in markers_by_file.values()
        if markers.get("downgrade_triggered") == "true"
        or markers.get("anchor_revision_required") == "true"
        or markers.get("template_revision_required") == "true"
    ]
    if not writeback_trials:
        add_error(errors, "skills/crossframe-casebook/examples/v5-dlc-quant-trials", "need at least one downgrade, anchor revision, or template revision")

    embedded_raters = [
        markers for markers in markers_by_file.values()
        if markers.get("trial_status") == "formal" and markers.get("rater_record") == "embedded"
    ]
    if len(embedded_raters) < 2:
        add_error(errors, "skills/crossframe-casebook/examples/v5-dlc-quant-trials", "need at least two formal trials with embedded rater_a/rater_b readings")


def check_disagreement(repo: Path, errors: list[str]) -> None:
    rel = "skills/crossframe-casebook/examples/v5-dlc-quant-trials/rater-disagreement-sample.md"
    path = repo / rel
    if not path.exists():
        return
    text = read(path)
    markers = parse_marker_values(text, REQUIRED_DISAGREEMENT_KEYS)
    missing = [key for key in REQUIRED_DISAGREEMENT_KEYS if not markers.get(key)]
    if missing:
        add_error(errors, rel, f"missing disagreement marker values: {', '.join(missing)}")
        return

    source_trial = repo / markers["source_trial"]
    if not source_trial.exists():
        add_error(errors, rel, f"source_trial does not exist: {markers['source_trial']}")

    conflict_type = markers["conflict_type"]
    if conflict_type not in CONFLICT_TYPES:
        add_error(errors, rel, f"invalid conflict_type: {conflict_type}")

    for key in ["unresolved", "writeback_required"]:
        if markers[key] not in BOOLEAN_VALUES:
            add_error(errors, rel, f"invalid {key}: {markers[key]}")

    judgment_conflict = markers["rater_a_judgment_grade"] != markers["rater_b_judgment_grade"]
    action_conflict = markers["rater_a_action_ceiling"] != markers["rater_b_action_ceiling"]
    if conflict_type in {"judgment_grade", "both"} and not judgment_conflict:
        add_error(errors, rel, "conflict_type requires judgment_grade conflict")
    if conflict_type in {"action_ceiling", "both"} and not action_conflict:
        add_error(errors, rel, "conflict_type requires action_ceiling conflict")
    if not (judgment_conflict or action_conflict):
        add_error(errors, rel, "need at least one judgment_grade or action_ceiling conflict")
    if markers["writeback_required"] != "true":
        add_error(errors, rel, "weak consistency must require writeback")

    if "不强行合并" not in text or "锚点" not in text:
        add_error(errors, rel, "disagreement must preserve conflict and point to anchor/template revision")


def check_summary(repo: Path, errors: list[str]) -> None:
    rel = "skills/crossframe-casebook/examples/v5-dlc-quant-trials/validation-summary.md"
    path = repo / rel
    if not path.exists():
        return
    text = read(path)
    for needle in ["降档", "写回", "评分者一致性", "不要求评分者收敛", "模板修订建议"]:
        if needle not in text:
            add_error(errors, rel, f"missing summary marker: {needle}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Check CrossFrame v5 DLC casebook validation trials.")
    parser.add_argument("--repo", default=".", help="Repository root.")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    errors: list[str] = []

    check_required_files(repo, errors)
    check_forbidden_language(repo, TRIAL_FILES + SUMMARY_AND_REVIEW_FILES, errors)
    check_trials(repo, errors)
    check_disagreement(repo, errors)
    check_summary(repo, errors)

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print("ok: v5 DLC casebook validation trials passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
