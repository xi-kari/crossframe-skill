from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


CORE_MARKDOWN_FILENAMES = {
    "max-artifact-manifest.md",
    "max-dossier.md",
    "max-essay.md",
    "max-continuation-ledger.md",
    "max-continuation-index.md",
}
CONTROL_PLANE_FILENAMES = {
    "max-run-contract.json",
    "max-validator-report.json",
    "max-repair-plan.json",
}


def _template_root() -> Path:
    return Path(__file__).resolve().parents[1] / "skills" / "crossframe-max" / "templates"


def dossier_headings() -> list[str]:
    path = _template_root() / "max-dossier-output.md"
    return [
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.startswith("## ")
    ]


def semantic_dossier_text() -> str:
    lines: list[str] = []
    for index, heading in enumerate(dossier_headings(), start=1):
        lines.extend(
            [
                heading,
                (
                    f"Section {index} records phase-lock gate state, claim_id, source_anchor P0276, "
                    "claim ledger and source ledger boundaries, counterevidence, withdrawal conditions, "
                    "action limits, and max-continuation-index continuity in substantive prose."
                ),
                (
                    f"Section {index} also explains how the recorded state constrains interpretation, "
                    "keeps evidence separate from inference, preserves a repair entry, and prevents "
                    "the next run from repeating or overstating the same structural judgment."
                ),
            ]
        )
    return "\n\n".join(lines) + "\n"


def extend_semantic_essay(text: str) -> str:
    additions = [
        (
            f"Additional semantic paragraph {index} follows claim_id CL1 and source_anchor P0276 through "
            "a distinct mechanism, counterevidence check, withdrawal condition, action limit, and continuation "
            "entry so the explanation remains longer than its structural dossier without repetitive filler."
        )
        for index in range(1, 13)
    ]
    return text.rstrip() + "\n\n" + "\n\n".join(additions) + "\n"


def semantic_complete_dossier_text(
    headings: list[str],
    required_markers: list[str],
    full_source_files: list[str],
) -> str:
    lines: list[str] = []
    for index, heading in enumerate(headings, start=1):
        lines.extend(
            [
                heading,
                (
                    f"Section {index} explains claim_id CL1 from source_anchor P0276 through a bounded "
                    "claim ledger, source ledger, counterevidence search, withdrawal condition, and action limit."
                ),
                (
                    f"Section {index} preserves phase-lock gate continuity, records repair consequences, "
                    "and identifies the next max-continuation-index entry without overstating the evidence."
                ),
            ]
        )
    for index, marker in enumerate(required_markers + full_source_files, start=1):
        lines.append(
            f"Contract record {index:03d} treats {marker} as a checked field with evidence, state, and repair meaning."
        )
    return "\n\n".join(lines) + "\n"


def semantic_complete_essay_text(required_markers: list[str], repeat: int = 160) -> str:
    paragraphs = [
        "The final explanation keeps claim_id CL1 tied to source_anchor P0276 before moving into interpretation."
    ]
    for index in range(repeat):
        marker = required_markers[index % len(required_markers)]
        paragraphs.append(
            f"Paragraph {index + 1:03d} develops {marker} through bounded evidence, route concepts, "
            "counterevidence, withdrawal conditions, action limits, and continuation discipline."
        )
    return "\n\n".join(paragraphs) + "\n"


def semantic_marker_document(title: str, markers: list[str]) -> str:
    lines = [f"# {title}"]
    for index, marker in enumerate(markers, start=1):
        lines.append(
            f"Record {index:03d}: {marker} is present with a concrete state, boundary, and continuation consequence."
        )
    return "\n\n".join(lines) + "\n"


def artifact_run_contract(run_id: str = "artifact-run-001") -> dict[str, object]:
    return {
        "contract_version": "v2",
        "run_id": run_id,
        "run_mode": "max-artifact-run",
        "execution_state": "finished",
        "artifact_state": "core_complete",
        "validation_state": "not_run",
        "target_profile": "artifact-run",
        "incomplete_reasons": ["full-source-exhaustive-pass-not-satisfied"],
        "blocked_reason": None,
        "final_output_allowed": True,
        "forbidden_behavior": ["claim max-complete before a fresh report"],
        "affected_phase_reset_rule": "reset affected phase and downstream artifacts",
        "phase_exception_rule": "record phase_exception_record before reset",
        "completed_read_state": ["source inventory recorded"],
        "resume_entry": None,
    }


def complete_run_contract(run_id: str = "complete-001") -> dict[str, object]:
    return {
        "contract_version": "v2",
        "run_id": run_id,
        "run_mode": "max-complete",
        "execution_state": "finished",
        "artifact_state": "strict_complete",
        "validation_state": "not_run",
        "target_profile": "complete",
        "incomplete_reasons": [],
        "blocked_reason": None,
        "final_output_allowed": True,
        "forbidden_behavior": ["claim max-complete before a fresh report"],
        "affected_phase_reset_rule": "reset affected phase and downstream artifacts",
        "phase_exception_rule": "record phase_exception_record before reset",
        "completed_read_state": ["3273/3273 source pass recorded"],
        "resume_entry": None,
    }


def design_review_contract(run_id: str = "design-review-001") -> dict[str, object]:
    contract = artifact_run_contract(run_id)
    contract.update(
        {
            "run_mode": "max-design-review",
            "target_profile": "design-review",
            "incomplete_reasons": ["complete-profile-not-requested"],
        }
    )
    return contract


def blocked_run_contract(run_id: str = "blocked-001") -> dict[str, object]:
    return {
        "contract_version": "v2",
        "run_id": run_id,
        "run_mode": "max-blocked/progress",
        "execution_state": "blocked",
        "artifact_state": "partial",
        "validation_state": "not_run",
        "target_profile": "blocked",
        "incomplete_reasons": ["required-source-unavailable"],
        "blocked_reason": "required source is unavailable inside the authorized boundary",
        "final_output_allowed": False,
        "forbidden_behavior": ["claim analysis completion while blocked"],
        "affected_phase_reset_rule": "resume from the recorded blocked phase",
        "phase_exception_rule": "preserve completed read state while blocked",
        "completed_read_state": ["source inventory recorded"],
        "resume_entry": "restore required source access and resume the read phase",
    }


def write_contract(workspace: Path, contract: dict[str, object]) -> None:
    workspace.mkdir(parents=True, exist_ok=True)
    (workspace / "max-run-contract.json").write_text(
        json.dumps(contract, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _manifest_inventory(workspace: Path) -> list[dict[str, str]]:
    return [
        {"path": path.name, "sha256": _sha256(path)}
        for path in sorted(workspace.iterdir(), key=lambda item: item.name)
        if path.is_file()
        and path.name != "max-artifact-manifest.md"
        and path.name not in CONTROL_PLANE_FILENAMES
    ]


def rewrite_manifest(workspace: Path) -> None:
    manifest_path = workspace / "max-artifact-manifest.md"
    existing = manifest_path.read_text(encoding="utf-8") if manifest_path.exists() else ""
    marker = "```manifest-contract"
    if marker in existing:
        existing = existing.split(marker, 1)[0].rstrip()
    if not existing:
        existing = "\n".join(
            [
                "# CrossFrame Max artifact manifest",
                "phase-lock gate",
                "phase artifacts",
                "artifact-first gate",
                "产物目录",
                "生成时间：fixture",
                "输入摘要：semantic fixture",
                "读态摘要：see run contract",
                "校验状态：pending-validator",
                "下一轮入口：see max-continuation-index.md",
            ]
        )
    contract = json.loads((workspace / "max-run-contract.json").read_text(encoding="utf-8"))
    manifest_contract = {
        "manifest_version": "v2",
        "run_id": contract["run_id"],
        "artifacts": _manifest_inventory(workspace),
    }
    manifest_path.write_text(
        existing.rstrip()
        + "\n\n```manifest-contract\n"
        + json.dumps(manifest_contract, ensure_ascii=False, indent=2)
        + "\n```\n",
        encoding="utf-8",
    )


def write_complete_fixture(workspace: Path) -> None:
    from validate_crossframe_max_route_ledger_fixtures import write_full_artifact_fixture

    workspace.mkdir(parents=True, exist_ok=True)
    write_full_artifact_fixture(workspace)
    write_contract(workspace, complete_run_contract())
    rewrite_manifest(workspace)


def write_artifact_run_fixture(workspace: Path) -> None:
    write_complete_fixture(workspace)
    for path in list(workspace.iterdir()):
        if path.is_file() and path.name not in CORE_MARKDOWN_FILENAMES | {"max-run-contract.json"}:
            path.unlink()
    (workspace / "max-dossier.md").write_text(semantic_dossier_text(), encoding="utf-8")
    essay_path = workspace / "max-essay.md"
    essay_path.write_text(extend_semantic_essay(essay_path.read_text(encoding="utf-8")), encoding="utf-8")
    write_contract(workspace, artifact_run_contract())
    rewrite_manifest(workspace)


def write_design_review_fixture(workspace: Path) -> None:
    from validate_crossframe_max_route_ledger_fixtures import base_fixture

    write_artifact_run_fixture(workspace)
    route_fixture = base_fixture("skill_design")
    for filename in (
        "max-read-plan.json",
        "max-concept-hit-ledger.json",
        "max-claim-ledger.json",
        "max-evidence-reasoning-audit.json",
    ):
        (workspace / filename).write_text(
            json.dumps(route_fixture[filename], ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    (workspace / "max-output-plan.locked.md").write_text(
        "\n".join(
            [
                "locked: true",
                "route_key: skill_design",
                "design_decision_id: DD1",
                "v6_rule_ids: R-skill-design-tool-boundary, R-process-artifact-action-limit",
                "counterevidence: route concept missing would invalidate this decision",
                "withdrawal_condition: withdraw if route-ledger validation fails",
                "action_limit: guide structure only; do not certify external reality",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    write_contract(workspace, design_review_contract())
    rewrite_manifest(workspace)


def write_blocked_fixture(workspace: Path) -> None:
    workspace.mkdir(parents=True, exist_ok=True)
    write_contract(workspace, blocked_run_contract())


def write_marker_only_fixture(workspace: Path) -> None:
    write_artifact_run_fixture(workspace)
    marker_only = "\n".join(
        line
        for heading in dossier_headings()
        for line in (heading, "marker")
    )
    (workspace / "max-dossier.md").write_text(marker_only + "\n", encoding="utf-8")
    rewrite_manifest(workspace)
