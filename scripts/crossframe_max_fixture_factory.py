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
