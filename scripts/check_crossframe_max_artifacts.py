from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import hashlib
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

from check_crossframe_max_read_ledger import check as check_structured_ledgers
from check_crossframe_max_route_ledgers import check as check_route_ledgers
from crossframe_max_runtime_contract import validate_run_contract


REQUIRED_DOSSIER_HEADINGS = [
    "## max-phase-lock",
    "## max-worldview-capsule",
    "## max-continuation-ledger",
    "## max-source-frontier",
    "## max-transcendence-window",
    "## max-position-matrix",
    "## max-local-world-model",
    "## max-concept-graph",
    "## max-scale-map",
    "## 运行规律",
    "## 问题定位",
    "## max-path-tree",
    "## max-path-confidence-layers",
    "## max-red-team-pass",
    "## max-unexhaustible-declaration",
    "## 处理问题",
    "## 证据与台账",
    "## max-evidence-reasoning-audit",
    "## max-validation-and-repair-state",
    "## 反例与撤回条件",
    "## max-essay 准备",
    "## max-output-layers",
    "## max-continuation-index",
]

REQUIRED_DOSSIER_MARKERS = [
    "phase-lock gate",
    "phase artifacts",
    "max-run-contract.json",
    "max-read-plan.json",
    "max-source-snapshot.json",
    "max-worldview-capsule.locked.md",
    "max-local-world-model.locked.md",
    "max-claim-board.json",
    "max-audit-board.json",
    "max-output-plan.locked.md",
    "phase_exception_record",
    "affected phase reset",
    "source_anchor",
    "claim_id",
    "claim ledger",
    "source ledger",
    "concept-registry lookup",
    "retrieval-trigger-policy",
    "内部概念检索",
    "外部检索触发",
    "先查 registry 再读 full-source",
    "max-evidence-reasoning-audit",
    "举证链",
    "推理链",
    "反向证据",
    "证据-推理-反例-降档循环",
    "max-output-layers",
    "max-continuation-index",
    "max-full-source-read-ledger",
    "full-source exhaustive pass: satisfied",
    "total paragraphs: 3273 / 3273",
    "stage 0 source inventory",
    "stage 8 final read audit",
    "read status: full / partial / missing",
    "layer digest",
    "max-read-ledger.json",
    "max-claim-ledger.json",
    "max-concept-hit-ledger.json",
    "max-evidence-reasoning-audit.json",
    "max-validator-report.json",
    "max-repair-plan.json",
    "validation_attempt",
    "affected_phase",
    "downstream_reset",
    "repair_action",
    "final_output_allowed",
    "registry expected source ranges",
    "source_ranges_from_registry",
    "source_ranges_read",
    "source_paragraph_ids inside read ranges",
    "contract_id",
    "contract heading exists",
    "contract map status",
    "concept-source-contract closure",
]

REQUIRED_ESSAY_MARKERS = [
    "phase-lock gate",
    "max-run-contract.json",
    "max-output-plan.locked.md",
    "局部世界",
    "运行规律",
    "问题形成",
    "路径演化",
    "概念注册表",
    "处理问题",
    "伪修复",
    "资料前沿",
    "retrieval-trigger-policy",
    "路径置信分层",
    "主体位置矩阵",
    "反向推演",
    "不可判断区",
    "撤回条件",
    "不可穷尽",
    "续写索引",
    "max-continuation-index",
    "max-full-source-read-ledger",
    "full-source exhaustive pass: satisfied",
    "total paragraphs: 3273 / 3273",
    "stage 8 final read audit",
    "max-read-ledger.json",
    "max-claim-ledger.json",
    "max-concept-hit-ledger.json",
    "max-evidence-reasoning-audit.json",
    "max-validator-report.json",
]

REQUIRED_LEDGER_MARKERS = [
    "phase-lock gate",
    "phase artifacts",
    "max-run-contract.json",
    "max-source-snapshot.json",
    "max-output-plan.locked.md",
    "max-run-state",
    "已读材料",
    "已展开路径",
    "未展开路径",
    "已撤回判断",
    "下一轮续写入口",
    "防重复",
    "防漂移",
    "max-full-source-read-ledger",
    "full-source exhaustive pass: satisfied",
    "total paragraphs: 3273 / 3273",
    "read status: full / partial / missing",
    "stage 8 final read audit",
    "max-read-ledger.json",
    "max-claim-ledger.json",
    "max-concept-hit-ledger.json",
    "max-evidence-reasoning-audit.json",
]

REQUIRED_INDEX_MARKERS = [
    "下一轮续写入口",
    "未展开路径",
    "未展开主体位置",
    "未穷尽资料队列",
    "未展开反例",
    "不得重复内容",
    "不得越界内容",
]

REQUIRED_MANIFEST_MARKERS = [
    "phase-lock gate",
    "phase artifacts",
    "artifact-first gate",
    "产物目录",
    "生成时间",
    "输入摘要",
    "读态摘要",
    "校验状态",
    "下一轮入口",
    "max-dossier.md",
    "max-essay.md",
    "max-continuation-ledger.md",
    "max-continuation-index.md",
    "max-run-contract.json",
    "max-read-plan.json",
    "max-source-snapshot.json",
    "max-worldview-capsule.locked.md",
    "max-local-world-model.locked.md",
    "max-claim-board.json",
    "max-audit-board.json",
    "max-output-plan.locked.md",
    "max-full-source-read-ledger",
    "full-source exhaustive pass: satisfied",
    "total paragraphs: 3273 / 3273",
    "stage 0 source inventory",
    "stage 8 final read audit",
    "read status: full / partial / missing",
    "max-read-ledger.json",
    "max-claim-ledger.json",
    "max-concept-hit-ledger.json",
    "max-evidence-reasoning-audit.json",
]

REQUIRED_FULL_SOURCE_FILES = [
    "00-source-envelope.md",
    "01-guide.md",
    "02-boundary-layer.md",
    "03-world-layer.md",
    "04-state-layer.md",
    "05-interface-layer.md",
    "06-tool-layer.md",
    "07-intervention-layer.md",
    "08-application-layer.md",
    "09-governance-layer.md",
]

VALIDATION_PROFILES = ("artifact-run", "complete", "design-review", "blocked")

FORBIDDEN_FINAL_MARKERS = [
    "max-incomplete:",
    "full-source exhaustive pass: not satisfied",
    "full-source exhaustive pass: unsatisfied",
    "read status: partial",
    "read status: missing",
]

MIN_ESSAY_TO_DOSSIER_RATIO = 1.6
STRONG_ESSAY_TO_DOSSIER_RATIO = 2.2
MAX_ESSAY_TO_DOSSIER_RATIO = 3.0
MIN_DOSSIER_SECTION_CHARS = 32
MAX_CONSECUTIVE_REPEATED_LINES = 5
MAX_REPEATED_LINE_RATIO = 0.20
MAX_HEADING_LINE_RATIO = 0.45
SOURCE_PARAGRAPH_RE = re.compile(r"\bP\d{4}\b")

DEFAULT_FILENAMES = {
    "manifest": "max-artifact-manifest.md",
    "dossier": "max-dossier.md",
    "essay": "max-essay.md",
    "ledger": "max-continuation-ledger.md",
    "index": "max-continuation-index.md",
}

STRUCTURED_LEDGER_FILENAMES = [
    "max-read-ledger.json",
    "max-claim-ledger.json",
    "max-concept-hit-ledger.json",
    "max-evidence-reasoning-audit.json",
]

PHASE_LOCK_FILENAMES = [
    "max-run-contract.json",
    "max-read-plan.json",
    "max-source-snapshot.json",
    "max-worldview-capsule.locked.md",
    "max-local-world-model.locked.md",
    "max-claim-board.json",
    "max-audit-board.json",
    "max-output-plan.locked.md",
]

ALLOWED_CLAIM_STATUSES = {
    "candidate",
    "supported",
    "downgraded",
    "split",
    "withdrawn",
    "needs_search",
    "unexhaustible",
    "final",
}

ALLOWED_AUDIT_RESULTS = {
    "keep",
    "downgrade",
    "split",
    "withdraw",
    "needs_external_search",
    "move_to_unexhaustible",
}

VALIDATOR_NAME = "check_crossframe_max_artifacts"

PHASE_DOWNSTREAM = {
    "run_contract": [
        "max-read-plan.json",
        "max-source-snapshot.json",
        "max-worldview-capsule.locked.md",
        "max-local-world-model.locked.md",
        "max-concept-hit-ledger.json",
        "max-claim-ledger.json",
        "max-claim-board.json",
        "max-evidence-reasoning-audit.json",
        "max-audit-board.json",
        "max-output-plan.locked.md",
        "max-dossier.md",
        "max-essay.md",
        "max-continuation-ledger.md",
        "max-continuation-index.md",
    ],
    "read_plan": [
        "max-source-snapshot.json",
        "max-worldview-capsule.locked.md",
        "max-local-world-model.locked.md",
        "max-concept-hit-ledger.json",
        "max-claim-board.json",
        "max-audit-board.json",
        "max-output-plan.locked.md",
        "max-dossier.md",
        "max-essay.md",
    ],
    "source_snapshot": [
        "max-worldview-capsule.locked.md",
        "max-local-world-model.locked.md",
        "max-concept-hit-ledger.json",
        "max-claim-ledger.json",
        "max-evidence-reasoning-audit.json",
        "max-output-plan.locked.md",
        "max-dossier.md",
        "max-essay.md",
    ],
    "concept_hit": [
        "max-claim-ledger.json",
        "max-claim-board.json",
        "max-evidence-reasoning-audit.json",
        "max-audit-board.json",
        "max-output-plan.locked.md",
        "max-dossier.md",
        "max-essay.md",
    ],
    "claim": [
        "max-evidence-reasoning-audit.json",
        "max-audit-board.json",
        "max-output-plan.locked.md",
        "max-dossier.md",
        "max-essay.md",
    ],
    "audit": [
        "max-output-plan.locked.md",
        "max-dossier.md",
        "max-essay.md",
    ],
    "output_plan": [
        "max-dossier.md",
        "max-essay.md",
        "max-continuation-ledger.md",
        "max-continuation-index.md",
    ],
    "final_markdown": [],
    "repository_maintenance": [],
}


@dataclass(frozen=True)
class ValidationError:
    error_id: str
    validator: str
    error_type: str
    severity: str
    artifact: str
    field: str | None
    message: str
    affected_phase: str
    repair_action: str
    downstream_reset: list[str]
    final_output_allowed: bool

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def read_text(path: Path, errors: list[str]) -> str:
    if not path.exists():
        errors.append(f"missing file: {path}")
        return ""
    if not path.is_file():
        errors.append(f"not a file: {path}")
        return ""
    return path.read_text(encoding="utf-8")


def read_json_file(path: Path, errors: list[str], missing_label: str = "phase-lock artifact") -> object | None:
    if not path.exists():
        errors.append(f"missing {missing_label}: {path.name}")
        return None
    if not path.is_file():
        errors.append(f"phase-lock artifact is not a file: {path}")
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"{path.name}: invalid JSON: {exc}")
        return None


def check_markers(text: str, markers: list[str], label: str, errors: list[str]) -> None:
    for marker in markers:
        if marker not in text:
            errors.append(f"{label}: missing marker: {marker}")


def check_ordered_headings(text: str, headings: list[str], label: str, errors: list[str]) -> None:
    previous = -1
    lines = text.splitlines()
    for heading in headings:
        current = -1
        for idx, line in enumerate(lines):
            if line.startswith(heading):
                current = idx
                break
        if current == -1:
            errors.append(f"{label}: missing heading: {heading}")
            continue
        if current < previous:
            errors.append(f"{label}: heading out of order: {heading}")
        previous = current


def heading_positions(text: str, headings: list[str]) -> list[tuple[str, int]]:
    lines = text.splitlines()
    positions: list[tuple[str, int]] = []
    for heading in headings:
        for idx, line in enumerate(lines):
            if line.startswith(heading):
                positions.append((heading, idx))
                break
    return positions


def check_heading_sections_nonempty(text: str, headings: list[str], label: str, errors: list[str]) -> None:
    lines = text.splitlines()
    positions = heading_positions(text, headings)
    if len(positions) != len(headings):
        return
    for index, (heading, start) in enumerate(positions):
        end = positions[index + 1][1] if index + 1 < len(positions) else len(lines)
        section = "\n".join(line for line in lines[start + 1 : end] if line.strip())
        section_chars = visible_chars(section)
        if section_chars < MIN_DOSSIER_SECTION_CHARS:
            errors.append(
                f"{label}: heading section too thin: {heading} "
                f"({section_chars} visible chars, required>={MIN_DOSSIER_SECTION_CHARS})"
            )


def check_repetitive_filler(text: str, label: str, errors: list[str]) -> None:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return
    heading_lines = [line for line in lines if line.startswith("#")]
    if len(lines) >= 10 and len(heading_lines) / len(lines) > MAX_HEADING_LINE_RATIO:
        errors.append(f"{label}: heading-to-content ratio too high for a completed artifact")

    previous = None
    repeated = 0
    for line in lines:
        if line == previous:
            repeated += 1
            if repeated >= MAX_CONSECUTIVE_REPEATED_LINES:
                errors.append(f"{label}: consecutive repeated line filler detected")
                break
        else:
            previous = line
            repeated = 1

    countable = [line for line in lines if not line.startswith("#") and len(line) >= 8]
    if len(countable) < 12:
        return
    line, count = Counter(countable).most_common(1)[0]
    if count >= 6 and count / len(countable) > MAX_REPEATED_LINE_RATIO:
        errors.append(f"{label}: repeated template line filler detected: {line[:60]}")


def check_no_template_truncation(text: str, errors: list[str]) -> None:
    if "## max-unexhaustible-declaration" in text and "## 证据与台账" not in text:
        errors.append(
            "max-dossier.md: template-fidelity gate failed: template appears truncated after max-unexhaustible-declaration"
        )
    if "CL1" in text and ("source_anchor" not in text or "claim ledger" not in text):
        errors.append(
            "max-dossier.md: CL-style claim ids require source_anchor, claim_id, source ledger, and claim ledger"
        )


def visible_chars(text: str) -> int:
    return len("".join(text.split()))


def check_longform_dominance(dossier: str, essay: str, errors: list[str]) -> None:
    """Enforce the longform-dominance gate: max-essay is the final explanation, not a dossier summary."""
    dossier_chars = visible_chars(dossier)
    essay_chars = visible_chars(essay)
    required_chars = int(dossier_chars * MIN_ESSAY_TO_DOSSIER_RATIO)
    if dossier_chars and essay_chars < required_chars:
        errors.append(
            "max-essay.md: longform-dominance gate failed: "
            f"max-essay visible chars must be at least {MIN_ESSAY_TO_DOSSIER_RATIO:.1f}x max-dossier "
            f"(essay={essay_chars}, dossier={dossier_chars}, required>={required_chars})"
        )


def check_essay_claim_or_source_references(
    essay: str, claim_ids: set[str], source_paragraph_ids: set[str], errors: list[str]
) -> None:
    if not claim_ids and not source_paragraph_ids:
        return
    if any(claim_id in essay for claim_id in claim_ids):
        return
    essay_source_ids = set(SOURCE_PARAGRAPH_RE.findall(essay))
    if source_paragraph_ids & essay_source_ids:
        return
    errors.append("max-essay.md: final explanation must reference a real claim_id or source_paragraph_id from structured ledgers")


def check_no_incomplete_final(text: str, label: str, errors: list[str]) -> None:
    normalized = text.lower()
    for marker in FORBIDDEN_FINAL_MARKERS:
        if marker in normalized:
            errors.append(f"{label}: incomplete full-source read state cannot pass final artifact validation: {marker}")


def default_skill_root() -> Path:
    script_path = Path(__file__).resolve()
    if script_path.parent.name == "scripts" and script_path.parent.parent.name == "crossframe-max":
        return script_path.parent.parent
    return script_path.parents[1] / "skills" / "crossframe-max"


CONTROL_PLANE_FILENAMES = {
    "max-run-contract.json",
    "max-validator-report.json",
    "max-repair-plan.json",
}


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_run_contract(workspace: Path, skill_root: Path, errors: list[str]) -> dict[str, Any]:
    data = read_json_file(workspace / "max-run-contract.json", errors, "run contract")
    if not isinstance(data, dict):
        return {}
    errors.extend(validate_run_contract(data, skill_root))
    return data


def resolve_profile(requested: str | None, contract: dict[str, Any], errors: list[str]) -> str:
    declared = contract.get("target_profile")
    if requested is not None and requested not in VALIDATION_PROFILES:
        errors.append(f"profile mismatch: unsupported profile {requested}")
        return "artifact-run"
    active = requested or declared or "artifact-run"
    if declared in VALIDATION_PROFILES and requested is not None and requested != declared:
        errors.append(f"profile mismatch: requested {requested}, contract declares {declared}")
    return str(active)


def read_manifest_contract(workspace: Path, errors: list[str] | None = None) -> dict[str, Any] | None:
    path = workspace / "max-artifact-manifest.md"
    if not path.is_file():
        if errors is not None:
            errors.append("missing file: max-artifact-manifest.md")
        return None
    text = path.read_text(encoding="utf-8")
    matches = re.findall(r"```manifest-contract\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if not matches:
        if errors is not None:
            errors.append("max-artifact-manifest.md: missing manifest-contract block")
        return None
    try:
        data = json.loads(matches[-1])
    except json.JSONDecodeError as exc:
        if errors is not None:
            errors.append(f"max-artifact-manifest.md: invalid manifest-contract JSON: {exc}")
        return None
    if not isinstance(data, dict):
        if errors is not None:
            errors.append("max-artifact-manifest.md: manifest-contract must be an object")
        return None
    return data


def check_manifest_inventory(
    workspace: Path,
    contract: dict[str, Any],
    errors: list[str],
) -> dict[str, Any] | None:
    manifest = read_manifest_contract(workspace, errors)
    if manifest is None:
        return None
    if manifest.get("manifest_version") != "v2":
        errors.append("manifest state mismatch: manifest_version must be v2")
    if manifest.get("run_id") != contract.get("run_id"):
        errors.append("manifest state mismatch: run_id differs from max-run-contract.json")
    raw_artifacts = manifest.get("artifacts")
    if not isinstance(raw_artifacts, list):
        errors.append("manifest state mismatch: artifacts must be a list")
        return manifest
    declared: dict[str, str] = {}
    for index, item in enumerate(raw_artifacts, start=1):
        if not isinstance(item, dict):
            errors.append(f"manifest state mismatch: artifact {index} must be an object")
            continue
        name = item.get("path")
        digest = item.get("sha256")
        if not isinstance(name, str) or not isinstance(digest, str):
            errors.append(f"manifest state mismatch: artifact {index} needs path and sha256")
            continue
        if name in declared:
            errors.append(f"manifest state mismatch: duplicate artifact path {name}")
        declared[name] = digest
    actual_paths = {
        path.name: path
        for path in workspace.iterdir()
        if path.is_file()
        and path.name != "max-artifact-manifest.md"
        and path.name not in CONTROL_PLANE_FILENAMES
    }
    if set(declared) != set(actual_paths):
        errors.append(
            "manifest state mismatch: inventory paths differ; "
            f"declared={sorted(declared)}, actual={sorted(actual_paths)}"
        )
    for name in sorted(set(declared) & set(actual_paths)):
        actual_digest = file_sha256(actual_paths[name])
        if declared[name] != actual_digest:
            errors.append(f"manifest state mismatch: artifact_sha256 differs for {name}")
    return manifest


def check_no_completion_claim_in_present_text(workspace: Path, errors: list[str]) -> None:
    claim_patterns = [
        re.compile(r"delivery_label\s*[:=]\s*max-complete", re.IGNORECASE),
        re.compile(r"交付状态\s*[：:]\s*max-complete", re.IGNORECASE),
        re.compile(r"validator\s+passed\s*[:=]?\s*max-complete", re.IGNORECASE),
    ]
    for path in sorted(workspace.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if any(pattern.search(text) for pattern in claim_patterns):
            errors.append(f"{path.name}: false max-complete claim before a fresh complete report")


def read_and_check_core_artifacts(workspace: Path, errors: list[str]) -> dict[str, str]:
    texts = {
        key: read_text(workspace / filename, errors)
        for key, filename in DEFAULT_FILENAMES.items()
    }
    manifest = texts["manifest"]
    dossier = texts["dossier"]
    essay = texts["essay"]
    ledger = texts["ledger"]
    index = texts["index"]
    if manifest:
        check_markers(
            manifest,
            [
                "phase-lock gate",
                "artifact-first gate",
                "产物目录",
                "max-dossier.md",
                "max-essay.md",
                "max-continuation-ledger.md",
                "max-continuation-index.md",
            ],
            "max-artifact-manifest.md",
            errors,
        )
    if dossier:
        check_ordered_headings(dossier, REQUIRED_DOSSIER_HEADINGS, "max-dossier.md", errors)
        check_heading_sections_nonempty(dossier, REQUIRED_DOSSIER_HEADINGS, "max-dossier.md", errors)
        check_markers(
            dossier,
            ["phase-lock gate", "claim_id", "source_anchor", "max-continuation-index"],
            "max-dossier.md",
            errors,
        )
        check_no_template_truncation(dossier, errors)
        check_repetitive_filler(dossier, "max-dossier.md", errors)
    if essay:
        check_markers(
            essay,
            ["phase-lock gate", "局部世界", "运行规律", "处理问题", "max-continuation-index"],
            "max-essay.md",
            errors,
        )
        check_repetitive_filler(essay, "max-essay.md", errors)
    if dossier and essay:
        check_longform_dominance(dossier, essay, errors)
    if ledger:
        check_markers(
            ledger,
            ["phase-lock gate", "max-run-state", "已读材料", "下一轮续写入口"],
            "max-continuation-ledger.md",
            errors,
        )
    if index:
        check_markers(index, REQUIRED_INDEX_MARKERS, "max-continuation-index.md", errors)
    check_no_completion_claim_in_present_text(workspace, errors)
    return texts


def require_declared_strict_gaps(contract: dict[str, Any], errors: list[str]) -> None:
    if contract.get("artifact_state") != "strict_complete" and not contract.get("incomplete_reasons"):
        errors.append("max-run-contract.json: non-strict artifact run must declare incomplete_reasons")


def require_all_structured_ledgers(workspace: Path, errors: list[str]) -> None:
    for filename in STRUCTURED_LEDGER_FILENAMES:
        if not (workspace / filename).exists():
            errors.append(f"missing structured ledger: {filename}")


def check_optional_ledgers_when_present(workspace: Path, skill_root: Path, errors: list[str]) -> None:
    present = [(workspace / filename).exists() for filename in STRUCTURED_LEDGER_FILENAMES]
    if any(present) and not all(present):
        missing = [name for name, exists in zip(STRUCTURED_LEDGER_FILENAMES, present) if not exists]
        errors.append(f"partial optional structured ledgers: {', '.join(missing)}")
    if all(present):
        errors.extend(check_structured_ledgers(workspace, skill_root))
        errors.extend(check_route_ledgers(workspace, skill_root))


def require_skill_design_route_artifacts(workspace: Path, errors: list[str]) -> None:
    for filename in (
        "max-read-plan.json",
        "max-concept-hit-ledger.json",
        "max-claim-ledger.json",
        "max-evidence-reasoning-audit.json",
        "max-output-plan.locked.md",
    ):
        if not (workspace / filename).exists():
            errors.append(f"design-review: missing skill_design artifact {filename}")


def check_design_decision_closure(workspace: Path, errors: list[str]) -> None:
    read_plan = read_json_file(workspace / "max-read-plan.json", errors, "skill_design read plan")
    if isinstance(read_plan, dict) and read_plan.get("route_key") != "skill_design":
        errors.append("design-review: route_key must be skill_design")
    claims_data = read_json_file(workspace / "max-claim-ledger.json", errors, "skill_design claim ledger")
    audits_data = read_json_file(
        workspace / "max-evidence-reasoning-audit.json",
        errors,
        "skill_design evidence audit",
    )
    claims = claims_data.get("claims") if isinstance(claims_data, dict) else None
    audits = audits_data.get("audits") if isinstance(audits_data, dict) else None
    if not isinstance(claims, list) or not claims:
        errors.append("design-review: skill_design claim ledger must contain a decision")
    else:
        for claim in claims:
            if not isinstance(claim, dict):
                continue
            for field in ("design_decision_id", "v6_rule_ids", "withdrawal_condition", "action_limit"):
                if not claim.get(field):
                    errors.append(f"design-review: skill_design decision missing {field}")
            if claim.get("needs_evidence") is True:
                errors.append(
                    f"premature final claim: {claim.get('claim_id', 'unknown')} still has needs_evidence=true"
                )
    if not isinstance(audits, list) or not audits:
        errors.append("design-review: skill_design audit must contain counterevidence")
    else:
        for audit in audits:
            if isinstance(audit, dict) and not audit.get("counterevidence"):
                errors.append("design-review: skill_design audit missing counterevidence")


def check_claim_identity_and_backreferences(workspace: Path, errors: list[str]) -> None:
    claims_data = read_json_file(workspace / "max-claim-ledger.json", errors, "claim ledger")
    audits_data = read_json_file(workspace / "max-evidence-reasoning-audit.json", errors, "evidence audit")
    claims = claims_data.get("claims") if isinstance(claims_data, dict) else None
    audits = audits_data.get("audits") if isinstance(audits_data, dict) else None
    if not isinstance(claims, list) or not isinstance(audits, list):
        return
    claim_ids = [
        claim.get("claim_id")
        for claim in claims
        if isinstance(claim, dict) and isinstance(claim.get("claim_id"), str)
    ]
    if len(claim_ids) != len(set(claim_ids)):
        errors.append("duplicate identifier: max-claim-ledger.json contains duplicate claim_id")
    for claim in claims:
        if not isinstance(claim, dict):
            continue
        source_ids = claim.get("source_paragraph_ids")
        if isinstance(source_ids, list) and len(source_ids) != len(set(source_ids)):
            errors.append(
                f"duplicate identifier: {claim.get('claim_id', 'unknown')} contains duplicate source_paragraph_ids"
            )
    audit_claim_ids = {
        audit.get("claim_id")
        for audit in audits
        if isinstance(audit, dict) and isinstance(audit.get("claim_id"), str)
    }
    if set(claim_ids) != audit_claim_ids:
        errors.append(
            "cross reference mismatch: claim and audit claim_id sets differ; "
            f"claims={sorted(set(claim_ids))}, audits={sorted(audit_claim_ids)}"
        )


def check_forbidden_outputs_in_final_markdown(workspace: Path, errors: list[str]) -> None:
    read_plan = read_json_file(workspace / "max-read-plan.json", [], "read plan")
    if not isinstance(read_plan, dict):
        return
    checks = read_plan.get("route_forbidden_outputs_checked")
    if not isinstance(checks, list):
        return
    forbidden = [
        item.get("forbidden_output")
        for item in checks
        if isinstance(item, dict) and isinstance(item.get("forbidden_output"), str)
    ]
    for path in (workspace / "max-dossier.md", workspace / "max-essay.md"):
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in forbidden:
            if phrase in text:
                errors.append(f"forbidden output appears in {path.name}: {phrase}")


def report_freshness_errors(workspace: Path, report: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = {
        "report_version",
        "run_id",
        "profile",
        "run_mode",
        "execution_state",
        "artifact_state",
        "incomplete_reasons",
        "input_validation_state",
        "validation_state",
        "run_contract_sha256",
        "manifest_sha256",
        "artifact_sha256",
        "final_label",
        "passed",
        "validators",
        "errors",
    }
    missing = sorted(required - set(report))
    if missing:
        errors.append(f"report schema: missing fields {', '.join(missing)}")
    if report.get("report_version") != "v2":
        errors.append("report schema: report_version must be v2")
    passed = report.get("passed")
    error_records = report.get("errors")
    if not isinstance(passed, bool):
        errors.append("report schema: passed must be boolean")
        passed = False
    if not isinstance(error_records, list) or any(not isinstance(item, dict) for item in error_records):
        errors.append("report schema: errors must be a list of objects")
        error_records = []
    if passed:
        if report.get("validation_state") != "passed" or error_records:
            errors.append("report schema: passed report requires validation_state=passed and no errors")
    elif report.get("validation_state") != "failed" or not error_records:
        errors.append("report schema: failed report requires validation_state=failed and at least one error")
    profile_value = report.get("profile")
    profile = profile_value if isinstance(profile_value, str) and profile_value in VALIDATION_PROFILES else "artifact-run"
    if profile_value != profile:
        errors.append("report schema: invalid profile")
    reasons_value = report.get("incomplete_reasons")
    reasons = [item for item in reasons_value if isinstance(item, str)] if isinstance(reasons_value, list) else []
    if reasons_value != reasons:
        errors.append("report schema: incomplete_reasons must contain only strings")
    expected_label = _final_label(profile, bool(passed), reasons, error_records)
    if report.get("final_label") != expected_label:
        errors.append(f"report schema: final_label must be {expected_label}")
    sha_pattern = re.compile(r"^[0-9a-f]{64}$")
    if not isinstance(report.get("run_contract_sha256"), str) or not sha_pattern.fullmatch(
        str(report.get("run_contract_sha256"))
    ):
        errors.append("report schema: run_contract_sha256 must be lowercase SHA256")
    artifact_hashes_value = report.get("artifact_sha256")
    if not isinstance(artifact_hashes_value, dict) or any(
        not isinstance(name, str) or not isinstance(digest, str) or not sha_pattern.fullmatch(digest)
        for name, digest in artifact_hashes_value.items()
    ):
        errors.append("report schema: artifact_sha256 must map paths to lowercase SHA256")
    contract_path = workspace / "max-run-contract.json"
    if not contract_path.is_file():
        return ["run_contract_sha256: max-run-contract.json is missing"]
    try:
        contract = json.loads(contract_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"run_contract_sha256: invalid max-run-contract.json: {exc}"]
    if report.get("run_id") != contract.get("run_id"):
        errors.append("run_id differs from max-run-contract.json")
    if report.get("profile") != contract.get("target_profile"):
        errors.append("profile differs from max-run-contract.json")
    if report.get("run_contract_sha256") != file_sha256(contract_path):
        errors.append("run_contract_sha256 differs from max-run-contract.json")
    profile = report.get("profile")
    if profile == "blocked":
        if report.get("manifest_sha256") is not None or report.get("artifact_sha256") != {}:
            errors.append("blocked report must not bind an artifact manifest")
        return errors
    manifest_path = workspace / "max-artifact-manifest.md"
    if not manifest_path.is_file():
        errors.append("manifest_sha256: max-artifact-manifest.md is missing")
        return errors
    if report.get("manifest_sha256") != file_sha256(manifest_path):
        errors.append("manifest_sha256 differs from max-artifact-manifest.md")
    manifest = read_manifest_contract(workspace)
    expected: dict[str, str] = {}
    if isinstance(manifest, dict) and isinstance(manifest.get("artifacts"), list):
        for item in manifest["artifacts"]:
            if isinstance(item, dict) and isinstance(item.get("path"), str) and isinstance(item.get("sha256"), str):
                expected[item["path"]] = item["sha256"]
    if report.get("artifact_sha256") != expected:
        errors.append("artifact_sha256 differs from manifest inventory")
    for name, digest in expected.items():
        path = workspace / name
        if not path.is_file() or file_sha256(path) != digest:
            errors.append(f"artifact_sha256 differs for {name}")
    return errors


def check_existing_validation_claim(
    workspace: Path,
    contract: dict[str, Any],
    errors: list[str],
) -> None:
    if contract.get("validation_state") != "passed":
        return
    report_path = workspace / "max-validator-report.json"
    if not report_path.is_file():
        errors.append("stale or false validation claim: passed contract has no validator report")
        return
    try:
        report = json.loads(report_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"stale or false validation claim: invalid validator report: {exc}")
        return
    if not isinstance(report, dict):
        errors.append("stale or false validation claim: validator report must be an object")
        return
    for freshness_error in report_freshness_errors(workspace, report):
        errors.append(f"stale or false validation claim: {freshness_error}")


def check_blocked_record_only(contract: dict[str, Any], errors: list[str]) -> None:
    if contract.get("run_mode") != "max-blocked/progress":
        errors.append("blocked profile requires run_mode=max-blocked/progress")
    if contract.get("execution_state") != "blocked":
        errors.append("blocked profile requires execution_state=blocked")


def ids_from_claim_ledger(workspace: Path, errors: list[str]) -> set[str]:
    data = read_json_file(workspace / "max-claim-ledger.json", errors, "structured ledger")
    if not isinstance(data, dict) or not isinstance(data.get("claims"), list):
        return set()
    return {
        claim.get("claim_id")
        for claim in data["claims"]
        if isinstance(claim, dict) and isinstance(claim.get("claim_id"), str)
    }


def source_ids_from_claim_ledger(workspace: Path, errors: list[str]) -> set[str]:
    data = read_json_file(workspace / "max-claim-ledger.json", errors, "structured ledger")
    if not isinstance(data, dict) or not isinstance(data.get("claims"), list):
        return set()
    source_ids: set[str] = set()
    for claim in data["claims"]:
        if not isinstance(claim, dict) or not isinstance(claim.get("source_paragraph_ids"), list):
            continue
        source_ids.update(
            source_id
            for source_id in claim["source_paragraph_ids"]
            if isinstance(source_id, str) and SOURCE_PARAGRAPH_RE.fullmatch(source_id)
        )
    return source_ids


def check_phase_lock_artifacts(workspace: Path, errors: list[str]) -> None:
    for filename in PHASE_LOCK_FILENAMES:
        if not (workspace / filename).exists():
            errors.append(f"missing phase-lock artifact: {filename}")

    run_contract = read_json_file(workspace / "max-run-contract.json", errors)
    if isinstance(run_contract, dict):
        errors.extend(validate_run_contract(run_contract, default_skill_root()))
        if run_contract.get("execution_state") == "finished" and run_contract.get("final_output_allowed") is not True:
            errors.append("max-run-contract.json: finished output requires final_output_allowed=true")
        forbidden = run_contract.get("forbidden_behavior")
        if not isinstance(forbidden, list) or not forbidden:
            errors.append("max-run-contract.json: forbidden_behavior must be a non-empty list")
        for field in ["affected_phase_reset_rule", "phase_exception_rule"]:
            if not run_contract.get(field):
                errors.append(f"max-run-contract.json: missing {field}")

    read_plan = read_json_file(workspace / "max-read-plan.json", errors)
    if isinstance(read_plan, dict):
        if read_plan.get("final_full_source_required") is not True:
            errors.append("max-read-plan.json: final_full_source_required must be true")
        required_files = read_plan.get("required_full_source_files")
        if not isinstance(required_files, list):
            errors.append("max-read-plan.json: required_full_source_files must be a list")
        else:
            missing = sorted(set(REQUIRED_FULL_SOURCE_FILES) - set(required_files))
            if missing:
                errors.append(f"max-read-plan.json: missing required full-source files: {', '.join(missing)}")

    source_snapshot = read_json_file(workspace / "max-source-snapshot.json", errors)
    if isinstance(source_snapshot, dict):
        if not source_snapshot.get("source_snapshot_id"):
            errors.append("max-source-snapshot.json: missing source_snapshot_id")
        if source_snapshot.get("total_paragraphs") != 3273:
            errors.append("max-source-snapshot.json: total_paragraphs must be 3273")
        if source_snapshot.get("full_source_exhaustive_pass") is not True:
            errors.append("max-source-snapshot.json: full_source_exhaustive_pass must be true")
        if source_snapshot.get("table_count") != 60:
            errors.append("max-source-snapshot.json: table_count must be 60")
        if source_snapshot.get("frozen") is not True:
            errors.append("max-source-snapshot.json: frozen must be true")
        if source_snapshot.get("source_anchor_verification_only_after_freeze") is not True:
            errors.append(
                "max-source-snapshot.json: source_anchor_verification_only_after_freeze must be true"
            )

    worldview = read_text(workspace / "max-worldview-capsule.locked.md", errors)
    if worldview:
        check_markers(
            worldview,
            ["locked: true", "source_snapshot_id", "本轮预先设计的世界观", "worldview_exception_record"],
            "max-worldview-capsule.locked.md",
            errors,
        )

    local_world = read_text(workspace / "max-local-world-model.locked.md", errors)
    if local_world:
        check_markers(
            local_world,
            ["locked: true", "局部世界", "对象边界", "主体位置", "承接链", "只建模，不下最终判断"],
            "max-local-world-model.locked.md",
            errors,
        )

    claim_board = read_json_file(workspace / "max-claim-board.json", errors)
    claim_board_ids: set[str] = set()
    if isinstance(claim_board, dict):
        claims = claim_board.get("claims")
        if not isinstance(claims, list) or not claims:
            errors.append("max-claim-board.json: claims must be a non-empty list")
        else:
            for idx, claim in enumerate(claims, start=1):
                if not isinstance(claim, dict):
                    errors.append(f"max-claim-board.json: claim {idx} must be an object")
                    continue
                claim_id = claim.get("claim_id")
                if not isinstance(claim_id, str) or not claim_id:
                    errors.append(f"max-claim-board.json: claim {idx} missing claim_id")
                    continue
                claim_board_ids.add(claim_id)
                status = claim.get("status")
                if status not in ALLOWED_CLAIM_STATUSES:
                    errors.append(f"max-claim-board.json: {claim_id} invalid status: {status}")
                if not claim.get("source_paragraph_ids"):
                    errors.append(f"max-claim-board.json: {claim_id} missing source_paragraph_ids")
                if not claim.get("concept_ids"):
                    errors.append(f"max-claim-board.json: {claim_id} missing concept_ids")
                if claim.get("needs_evidence") is not True:
                    errors.append(f"max-claim-board.json: {claim_id} needs_evidence must be true before audit")
                if claim.get("needs_counterevidence") is not True:
                    errors.append(f"max-claim-board.json: {claim_id} needs_counterevidence must be true before audit")

    audit_board = read_json_file(workspace / "max-audit-board.json", errors)
    audit_board_ids: set[str] = set()
    if isinstance(audit_board, dict):
        if audit_board.get("red_team_final_text_authority") is not False:
            errors.append("max-audit-board.json: red_team_final_text_authority must be false")
        audits = audit_board.get("audits")
        if not isinstance(audits, list) or not audits:
            errors.append("max-audit-board.json: audits must be a non-empty list")
        else:
            for idx, audit in enumerate(audits, start=1):
                if not isinstance(audit, dict):
                    errors.append(f"max-audit-board.json: audit {idx} must be an object")
                    continue
                claim_id = audit.get("claim_id")
                if not isinstance(claim_id, str) or not claim_id:
                    errors.append(f"max-audit-board.json: audit {idx} missing claim_id")
                    continue
                audit_board_ids.add(claim_id)
                if audit.get("audit_result") not in ALLOWED_AUDIT_RESULTS:
                    errors.append(f"max-audit-board.json: {claim_id} invalid audit_result")
                if audit.get("final_status") not in ALLOWED_CLAIM_STATUSES:
                    errors.append(f"max-audit-board.json: {claim_id} invalid final_status")
                if not audit.get("source_paragraph_ids"):
                    errors.append(f"max-audit-board.json: {claim_id} missing source_paragraph_ids")
                if not audit.get("counterevidence_status"):
                    errors.append(f"max-audit-board.json: {claim_id} missing counterevidence_status")

    output_plan = read_text(workspace / "max-output-plan.locked.md", errors)
    if output_plan:
        check_markers(
            output_plan,
            [
                "locked: true",
                "进入正文的 claim",
                "降档表达的 claim",
                "撤回的 claim",
                "进入不可判断区的 claim",
                "不可写强的句子",
                "必须保留的撤回条件",
                "max-essay.md may now be written",
            ],
            "max-output-plan.locked.md",
            errors,
        )

    final_claim_ids = ids_from_claim_ledger(workspace, errors)
    if final_claim_ids and claim_board_ids:
        missing = sorted(final_claim_ids - claim_board_ids)
        if missing:
            errors.append(f"phase-lock gate: final claims missing from max-claim-board.json: {', '.join(missing)}")
    if final_claim_ids and audit_board_ids:
        missing = sorted(final_claim_ids - audit_board_ids)
        if missing:
            errors.append(f"phase-lock gate: final claims missing from max-audit-board.json: {', '.join(missing)}")


def check_crossframe_max_artifacts(
    workspace: Path,
    skill_root: Path | None = None,
    profile: str | None = None,
) -> list[str]:
    """Validate generated crossframe-max artifacts against artifact, template, and longform gates."""
    errors: list[str] = []
    if not workspace.exists():
        errors.append(f"missing workspace directory: {workspace}")
        return errors
    if not workspace.is_dir():
        errors.append(f"workspace is not a directory: {workspace}")
        return errors

    resolved_skill_root = skill_root or default_skill_root()
    contract = load_run_contract(workspace, resolved_skill_root, errors)
    active_profile = resolve_profile(profile, contract, errors)
    check_existing_validation_claim(workspace, contract, errors)
    if active_profile == "blocked":
        check_blocked_record_only(contract, errors)
        check_no_completion_claim_in_present_text(workspace, errors)
        return errors

    if active_profile in {"artifact-run", "design-review"}:
        read_and_check_core_artifacts(workspace, errors)
        check_manifest_inventory(workspace, contract, errors)
        require_declared_strict_gaps(contract, errors)
        if active_profile == "artifact-run":
            check_optional_ledgers_when_present(workspace, resolved_skill_root, errors)
        else:
            require_skill_design_route_artifacts(workspace, errors)
            if all(
                (workspace / filename).exists()
                for filename in (
                    "max-read-plan.json",
                    "max-concept-hit-ledger.json",
                    "max-claim-ledger.json",
                    "max-evidence-reasoning-audit.json",
                )
            ):
                errors.extend(check_route_ledgers(workspace, resolved_skill_root))
            check_design_decision_closure(workspace, errors)
            check_claim_identity_and_backreferences(workspace, errors)
            check_forbidden_outputs_in_final_markdown(workspace, errors)
        return errors

    check_manifest_inventory(workspace, contract, errors)

    manifest = read_text(workspace / DEFAULT_FILENAMES["manifest"], errors)
    dossier = read_text(workspace / DEFAULT_FILENAMES["dossier"], errors)
    essay = read_text(workspace / DEFAULT_FILENAMES["essay"], errors)
    ledger = read_text(workspace / DEFAULT_FILENAMES["ledger"], errors)
    index = read_text(workspace / DEFAULT_FILENAMES["index"], errors)
    claim_ids_for_essay = (
        ids_from_claim_ledger(workspace, errors) if (workspace / "max-claim-ledger.json").exists() else set()
    )
    source_ids_for_essay = (
        source_ids_from_claim_ledger(workspace, errors) if (workspace / "max-claim-ledger.json").exists() else set()
    )

    if manifest:
        check_markers(manifest, REQUIRED_MANIFEST_MARKERS, "max-artifact-manifest.md", errors)
        check_no_incomplete_final(manifest, "max-artifact-manifest.md", errors)
    if dossier:
        check_ordered_headings(dossier, REQUIRED_DOSSIER_HEADINGS, "max-dossier.md", errors)
        check_heading_sections_nonempty(dossier, REQUIRED_DOSSIER_HEADINGS, "max-dossier.md", errors)
        check_markers(dossier, REQUIRED_DOSSIER_MARKERS, "max-dossier.md", errors)
        check_markers(dossier, REQUIRED_FULL_SOURCE_FILES, "max-dossier.md", errors)
        check_no_incomplete_final(dossier, "max-dossier.md", errors)
        check_no_template_truncation(dossier, errors)
        check_repetitive_filler(dossier, "max-dossier.md", errors)
    if essay:
        check_markers(essay, REQUIRED_ESSAY_MARKERS, "max-essay.md", errors)
        check_no_incomplete_final(essay, "max-essay.md", errors)
        check_essay_claim_or_source_references(essay, claim_ids_for_essay, source_ids_for_essay, errors)
        check_repetitive_filler(essay, "max-essay.md", errors)
    if dossier and essay:
        check_longform_dominance(dossier, essay, errors)
    if ledger:
        check_markers(ledger, REQUIRED_LEDGER_MARKERS, "max-continuation-ledger.md", errors)
        check_markers(ledger, REQUIRED_FULL_SOURCE_FILES, "max-continuation-ledger.md", errors)
        check_no_incomplete_final(ledger, "max-continuation-ledger.md", errors)
    if index:
        check_markers(index, REQUIRED_INDEX_MARKERS, "max-continuation-index.md", errors)
        check_no_incomplete_final(index, "max-continuation-index.md", errors)
    for filename in STRUCTURED_LEDGER_FILENAMES:
        if not (workspace / filename).exists():
            errors.append(f"missing structured ledger: {filename}")
    check_phase_lock_artifacts(workspace, errors)
    if not any(error.startswith("missing structured ledger:") for error in errors):
        errors.extend(check_structured_ledgers(workspace, resolved_skill_root))
        errors.extend(check_route_ledgers(workspace, resolved_skill_root))
        check_claim_identity_and_backreferences(workspace, errors)
        check_forbidden_outputs_in_final_markdown(workspace, errors)

    return errors


def phase_for_artifact(artifact: str) -> str:
    if artifact == "max-run-contract.json":
        return "run_contract"
    if artifact == "max-read-plan.json":
        return "read_plan"
    if artifact == "max-source-snapshot.json":
        return "source_snapshot"
    if artifact == "max-concept-hit-ledger.json":
        return "concept_hit"
    if artifact in {"max-claim-ledger.json", "max-claim-board.json"}:
        return "claim"
    if artifact in {"max-evidence-reasoning-audit.json", "max-audit-board.json"}:
        return "audit"
    if artifact == "max-output-plan.locked.md":
        return "output_plan"
    if artifact in {
        "max-artifact-manifest.md",
        "max-dossier.md",
        "max-essay.md",
        "max-continuation-ledger.md",
        "max-continuation-index.md",
    }:
        return "final_markdown"
    return "final_markdown"


def extract_artifact(message: str) -> str:
    for token in [
        "max-run-contract.json",
        "max-read-plan.json",
        "max-source-snapshot.json",
        "max-worldview-capsule.locked.md",
        "max-local-world-model.locked.md",
        "max-concept-hit-ledger.json",
        "max-claim-ledger.json",
        "max-claim-board.json",
        "max-evidence-reasoning-audit.json",
        "max-audit-board.json",
        "max-output-plan.locked.md",
        "max-artifact-manifest.md",
        "max-dossier.md",
        "max-essay.md",
        "max-continuation-ledger.md",
        "max-continuation-index.md",
        "v6-route-map.yaml",
        "v6-contract-map.json",
        "concept-registry/index.md",
    ]:
        if token in message:
            return token
    if message.startswith("missing file:"):
        name = Path(message.split(":", 1)[1].strip()).name
        if name:
            return name
    if ": " in message:
        prefix = message.split(":", 1)[0]
        if prefix.endswith((".json", ".md", ".yaml")):
            return prefix
    return "workspace"


def classify_message(message: str) -> tuple[str, str, str, str | None]:
    lowered = message.lower()
    artifact = extract_artifact(message)
    if "stale or false validation claim" in lowered:
        return "stale_or_false_validation_claim", "reset_run_contract_and_revalidate", "run_contract", "validation_state"
    if "manifest state mismatch" in lowered:
        return "manifest_state_mismatch", "regenerate_manifest_and_revalidate", "final_markdown", None
    if "profile mismatch" in lowered:
        return "profile_mismatch", "reset_run_contract_and_revalidate", "run_contract", "target_profile"
    if "false max-complete claim" in lowered:
        return "false_complete_claim", "remove_false_completion_claim", "final_markdown", None
    if "premature final claim" in lowered:
        return "premature_final_claim", "regenerate_audit_and_downstream", "claim", "needs_evidence"
    if "duplicate identifier" in lowered:
        return "duplicate_identifier", "regenerate_claim_and_downstream", "claim", "claim_id"
    if "cross reference mismatch" in lowered or "final claims missing audits" in lowered or "audits without matching claims" in lowered:
        return "cross_reference_mismatch", "regenerate_audit_and_downstream", "audit", "claim_id"
    if "design-review:" in lowered:
        return "design_review_closure_failed", "regenerate_output_plan_and_final_markdown", "output_plan", None
    if "heading section too thin" in lowered or "marker-only" in lowered:
        return "artifact_semantic_thinness", "regenerate_markdown_only", "final_markdown", None
    if "missing heading" in lowered:
        return "missing_template_heading", "regenerate_markdown_only", "final_markdown", None
    if "forbidden output appears" in lowered:
        return "forbidden_output_present", "regenerate_markdown_only", "final_markdown", None
    if message.startswith("max-run-contract.json"):
        return "runtime_state_conflict", "reset_run_contract_and_revalidate", "run_contract", None
    if "invalid json" in lowered:
        return "invalid_json", "create_missing_artifact", phase_for_artifact(artifact), None
    if message.startswith("missing file:") or message.startswith("missing structured ledger:") or "missing phase-lock artifact" in message or "missing route-ledger artifact" in message:
        return "missing_artifact", "create_missing_artifact", phase_for_artifact(artifact), None
    if "full-source" in message and ("not satisfied" in lowered or "partial" in lowered or "missing" in lowered):
        return "full_source_incomplete", "mark_artifact_incomplete", "source_snapshot", None
    if "source_ranges_from_registry does not match" in message or "source_ranges_read does not overlap" in message:
        return "concept_source_anchor_mismatch", "regenerate_concept_hit_and_downstream", "concept_hit", "source_ranges_from_registry"
    if "source_paragraph_ids not covered" in message:
        return "source_paragraph_not_in_read_range", "regenerate_concept_hit_and_downstream", "concept_hit", "source_paragraph_ids"
    if "contract_id" in message or "v6-contract-map.json" in message:
        return "concept_contract_missing", "repository_maintenance_required", "repository_maintenance", "contract_id"
    if "not found in concept registry" in message:
        return "concept_registry_missing", "regenerate_concept_hit_and_downstream", "concept_hit", "concept_id"
    if "required_concepts missing from concept registry" in message or "missing route required concepts" in message:
        return "route_registry_closure_failed", "regenerate_concept_hit_and_downstream", "concept_hit", "route_required_concepts"
    if "route_key" in message or "route_map_version" in message or "missing route " in message or "forbidden output check" in message:
        return "route_plan_mismatch", "regenerate_output_plan_and_final_markdown", "read_plan", None
    if "concept_ids missing concept hits" in message:
        return "claim_missing_concept_hit", "regenerate_concept_hit_and_downstream", "concept_hit", "concept_ids"
    if "final claims missing audits" in message or "design decisions missing audits" in message:
        return "claim_missing_audit", "regenerate_audit_and_downstream", "audit", "claim_id"
    if "missing evidence_chain" in message or "evidence chain" in lowered:
        return "evidence_chain_missing", "regenerate_audit_and_downstream", "audit", "evidence_chain"
    if "missing counterevidence" in message or "counterevidence_status" in message:
        return "counterevidence_missing", "regenerate_audit_and_downstream", "audit", "counterevidence"
    if "external search" in lowered or "needs_external_search" in message:
        return "external_search_required", "needs_external_search", "audit", None
    if "longform-dominance gate failed" in message:
        return "essay_too_short", "regenerate_markdown_only", "final_markdown", None
    if "heading section too thin" in message:
        return "dossier_section_too_thin", "regenerate_markdown_only", "final_markdown", None
    if "repeated" in lowered or "marker stuffing" in lowered:
        return "repeated_filler", "regenerate_markdown_only", "final_markdown", None
    if "forbidden output appears" in message:
        return "forbidden_output_present", "regenerate_markdown_only", "final_markdown", None
    if "must reference a real claim_id or source_paragraph_id" in message:
        return "missing_claim_or_source_reference", "regenerate_markdown_only", "final_markdown", None
    return "unrepairable_repository_state", "mark_artifact_incomplete", phase_for_artifact(artifact), None


def check_crossframe_max_artifacts_structured(
    workspace: Path,
    skill_root: Path | None = None,
    profile: str | None = None,
) -> list[ValidationError]:
    errors = check_crossframe_max_artifacts(workspace, skill_root, profile)
    structured: list[ValidationError] = []
    for index, message in enumerate(errors, start=1):
        error_type, repair_action, affected_phase, field = classify_message(message)
        structured.append(
            ValidationError(
                error_id=f"artifact-{index:04d}",
                validator=VALIDATOR_NAME,
                error_type=error_type,
                severity="error",
                artifact=extract_artifact(message),
                field=field,
                message=message,
                affected_phase=affected_phase,
                repair_action=repair_action,
                downstream_reset=list(PHASE_DOWNSTREAM.get(affected_phase, [])),
                final_output_allowed=False,
            )
        )
    return structured


def _canonical_contract_bytes(contract: dict[str, Any]) -> bytes:
    return (json.dumps(contract, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def _error_record(error: ValidationError | dict[str, Any]) -> dict[str, Any]:
    if isinstance(error, ValidationError):
        return error.to_dict()
    return dict(error)


def _synthetic_error(error_type: str, message: str) -> dict[str, Any]:
    return {
        "error_id": f"runtime-{error_type}",
        "validator": VALIDATOR_NAME,
        "error_type": error_type,
        "severity": "error",
        "artifact": "max-run-contract.json",
        "field": "validation_state",
        "message": message,
        "affected_phase": "run_contract",
        "repair_action": "reset_run_contract_and_revalidate",
        "downstream_reset": list(PHASE_DOWNSTREAM["run_contract"]),
        "final_output_allowed": False,
    }


def _final_label(
    profile: str,
    passed: bool,
    incomplete_reasons: list[str],
    error_records: list[dict[str, Any]],
) -> str:
    if not passed:
        first_error = str(error_records[0].get("error_type", "unknown_error")) if error_records else "unknown_error"
        return f"max-validation-failed:{profile}:{first_error}"
    if profile == "artifact-run":
        if incomplete_reasons:
            return f"max-artifact-incomplete:{incomplete_reasons[0]}"
        return "max-artifact-run-valid"
    return {
        "complete": "max-complete",
        "design-review": "max-design-review",
        "blocked": "max-blocked/progress",
    }[profile]


def build_validation_result(
    workspace: Path,
    errors: list[ValidationError | dict[str, Any]],
    *,
    profile: str,
    contract: dict[str, Any],
    manifest: dict[str, Any] | None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    error_records = [_error_record(error) for error in errors]
    if contract.get("target_profile") != profile:
        error_records.append(
            _synthetic_error(
                "profile_mismatch",
                f"profile {profile} disagrees with contract target {contract.get('target_profile')}",
            )
        )
    if profile == "complete" and contract.get("artifact_state") != "strict_complete":
        error_records.append(
            _synthetic_error(
                "runtime_state_conflict",
                "complete profile requires artifact_state=strict_complete",
            )
        )
    if contract.get("validation_state") == "failed" and not error_records:
        error_records.append(
            _synthetic_error(
                "invalid_validation_transition",
                "failed validation must reset to not_run before it can pass",
            )
        )

    passed = not error_records
    projected_contract = dict(contract)
    projected_contract["validation_state"] = "passed" if passed else "failed"
    contract_bytes = _canonical_contract_bytes(projected_contract)
    contract_digest = hashlib.sha256(contract_bytes).hexdigest()
    incomplete_reasons = [
        str(reason)
        for reason in projected_contract.get("incomplete_reasons", [])
        if isinstance(reason, str)
    ]
    artifact_hashes: dict[str, str] = {}
    if manifest is not None and isinstance(manifest.get("artifacts"), list):
        for item in manifest["artifacts"]:
            if isinstance(item, dict) and isinstance(item.get("path"), str) and isinstance(item.get("sha256"), str):
                artifact_hashes[item["path"]] = item["sha256"]
    manifest_path = workspace / "max-artifact-manifest.md"
    manifest_digest = file_sha256(manifest_path) if profile != "blocked" and manifest_path.is_file() else None
    report = {
        "report_version": "v2",
        "run_id": projected_contract.get("run_id"),
        "profile": profile,
        "run_mode": projected_contract.get("run_mode"),
        "execution_state": projected_contract.get("execution_state"),
        "artifact_state": projected_contract.get("artifact_state"),
        "incomplete_reasons": incomplete_reasons,
        "input_validation_state": contract.get("validation_state"),
        "validation_state": projected_contract["validation_state"],
        "run_contract_sha256": contract_digest,
        "manifest_sha256": manifest_digest,
        "artifact_sha256": artifact_hashes,
        "final_label": _final_label(profile, passed, incomplete_reasons, error_records),
        "passed": passed,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "validators": ["check_crossframe_max_artifacts", "check_crossframe_max_route_ledgers"],
        "errors": error_records,
    }
    return projected_contract, report


def write_validation_result(
    workspace: Path,
    projected_contract: dict[str, Any],
    report: dict[str, Any],
) -> None:
    contract_path = workspace / "max-run-contract.json"
    report_path = workspace / "max-validator-report.json"
    contract_temp = contract_path.with_suffix(contract_path.suffix + ".tmp")
    report_temp = report_path.with_suffix(report_path.suffix + ".tmp")
    contract_temp.write_bytes(_canonical_contract_bytes(projected_contract))
    report_temp.write_text(
        json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    os.replace(contract_temp, contract_path)
    os.replace(report_temp, report_path)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="check_crossframe_max_artifacts: validate generated crossframe-max files against artifact-first, template-fidelity, longform-dominance, and route-ledger gates."
    )
    parser.add_argument("--workspace", default=".", help="Directory containing max-dossier.md and related artifacts.")
    parser.add_argument("--skill-root", default=None, help="Path to the crossframe-max skill root for source-id validation.")
    parser.add_argument("--profile", choices=VALIDATION_PROFILES, default=None, help="Validation profile; defaults to the run contract.")
    parser.add_argument("--json", action="store_true", dest="json_output", help="Emit machine-readable validator report.")
    parser.add_argument(
        "--write-report",
        nargs="?",
        const="",
        default=None,
        help="Write max-validator-report.json; optional explicit path.",
    )
    args = parser.parse_args()

    workspace = Path(args.workspace).resolve()
    skill_root = Path(args.skill_root).resolve() if args.skill_root else default_skill_root()
    structured_errors = check_crossframe_max_artifacts_structured(workspace, skill_root, args.profile)
    contract_errors: list[str] = []
    contract = load_run_contract(workspace, skill_root, contract_errors)
    active_profile = args.profile or str(contract.get("target_profile") or "artifact-run")
    manifest = None if active_profile == "blocked" else read_manifest_contract(workspace)
    projected_contract, report = build_validation_result(
        workspace,
        structured_errors,
        profile=active_profile,
        contract=contract,
        manifest=manifest,
    )
    if args.write_report is not None:
        write_validation_result(workspace, projected_contract, report)
        if args.write_report:
            report_path = Path(args.write_report).resolve()
            if report_path != workspace / "max-validator-report.json":
                report_path.write_text(
                    json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
                    encoding="utf-8",
                )
    if args.json_output:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0 if report["passed"] else 1
    errors = [str(error.get("message", error.get("error_type"))) for error in report["errors"]]
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print(
        "ok: crossframe max artifacts passed "
        f"profile={active_profile} label={report['final_label']} -> {workspace}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
