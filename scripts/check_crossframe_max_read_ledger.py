from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


EXPECTED_TOTAL_PARAGRAPHS = 3273
EXPECTED_SOURCE_FILES = [
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
EXPECTED_FILE_RANGES = {
    "00-source-envelope.md": ("P0001", "P0049"),
    "01-guide.md": ("P0050", "P0194"),
    "02-boundary-layer.md": ("P0195", "P0896"),
    "03-world-layer.md": ("P0897", "P1519"),
    "04-state-layer.md": ("P1520", "P1813"),
    "05-interface-layer.md": ("P1814", "P1849"),
    "06-tool-layer.md": ("P1850", "P2270"),
    "07-intervention-layer.md": ("P2271", "P2546"),
    "08-application-layer.md": ("P2547", "P2885"),
    "09-governance-layer.md": ("P2886", "P3273"),
}
SOURCE_ID_RE = re.compile(r"^P\d{4}$")


def read_json(path: Path, errors: list[str]) -> Any:
    if not path.exists():
        errors.append(f"missing structured ledger: {path.name}")
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"{path.name}: invalid JSON: {exc}")
        return None


def source_ids_from_skill(skill_root: Path) -> set[str]:
    source_dir = skill_root / "references" / "v6-full-source"
    ids: set[str] = set()
    for path in source_dir.glob("*.md"):
        if path.name.startswith("00-") and path.name.endswith("index.md"):
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("<!-- source_paragraph:"):
                pid = line.split("source_paragraph:", 1)[1].split(" ", 1)[0]
                ids.add(pid)
    return ids


def pid_number(pid: str) -> int:
    if not isinstance(pid, str) or not SOURCE_ID_RE.match(pid):
        raise ValueError(f"invalid source paragraph id: {pid}")
    return int(pid[1:])


def expand_range(start: str, end: str) -> set[str]:
    start_n = pid_number(start)
    end_n = pid_number(end)
    if end_n < start_n:
        raise ValueError(f"descending paragraph range: {start}-{end}")
    return {f"P{i:04d}" for i in range(start_n, end_n + 1)}


def parse_read_ranges(raw_ranges: Any, label: str, errors: list[str]) -> set[str]:
    if not isinstance(raw_ranges, list) or not raw_ranges:
        errors.append(f"max-read-ledger.json: {label} read_ranges must be a non-empty list")
        return set()
    covered: set[str] = set()
    for idx, item in enumerate(raw_ranges, start=1):
        if not isinstance(item, list) or len(item) != 2:
            errors.append(f"max-read-ledger.json: {label} read_ranges[{idx}] must be [start, end]")
            continue
        try:
            covered.update(expand_range(item[0], item[1]))
        except ValueError as exc:
            errors.append(f"max-read-ledger.json: {label} {exc}")
    return covered


def check_read_ledger(data: Any, errors: list[str]) -> None:
    if not isinstance(data, dict):
        errors.append("max-read-ledger.json: root must be an object")
        return
    if data.get("total_expected_paragraphs") != EXPECTED_TOTAL_PARAGRAPHS:
        errors.append("max-read-ledger.json: total_expected_paragraphs must be 3273")
    if data.get("total_read_paragraphs") != EXPECTED_TOTAL_PARAGRAPHS:
        errors.append("max-read-ledger.json: total_read_paragraphs must be 3273")
    if data.get("full_source_exhaustive_pass") is not True:
        errors.append("max-read-ledger.json: full_source_exhaustive_pass must be true")
    if data.get("missing_paragraphs") not in ([], None):
        errors.append("max-read-ledger.json: missing_paragraphs must be empty")
    files = data.get("files")
    if not isinstance(files, list):
        errors.append("max-read-ledger.json: files must be a list")
        return
    by_name = {entry.get("file"): entry for entry in files if isinstance(entry, dict)}
    all_covered: set[str] = set()
    for file_name in EXPECTED_SOURCE_FILES:
        entry = by_name.get(file_name)
        if entry is None:
            errors.append(f"max-read-ledger.json: missing file entry: {file_name}")
            continue
        if entry.get("status") != "full":
            errors.append(f"max-read-ledger.json: {file_name} status must be full")
        if not entry.get("layer_digest"):
            errors.append(f"max-read-ledger.json: {file_name} missing layer_digest")
        expected_start, expected_end = EXPECTED_FILE_RANGES[file_name]
        if entry.get("expected_range") != [expected_start, expected_end]:
            errors.append(
                f"max-read-ledger.json: {file_name} expected_range must be [{expected_start}, {expected_end}]"
            )
        expected_ids = expand_range(expected_start, expected_end)
        covered = parse_read_ranges(entry.get("read_ranges"), file_name, errors)
        missing = sorted(expected_ids - covered)
        extra = sorted(covered - expected_ids)
        if missing:
            errors.append(f"max-read-ledger.json: {file_name} read_ranges do not cover: {', '.join(missing[:12])}")
        if extra:
            errors.append(f"max-read-ledger.json: {file_name} read_ranges include out-of-file ids: {', '.join(extra[:12])}")
        all_covered.update(covered)
    expected_all = expand_range("P0001", "P3273")
    missing_all = sorted(expected_all - all_covered)
    extra_all = sorted(all_covered - expected_all)
    if missing_all:
        errors.append(f"max-read-ledger.json: read_ranges union missing source ids: {', '.join(missing_all[:12])}")
    if extra_all:
        errors.append(f"max-read-ledger.json: read_ranges union includes invalid source ids: {', '.join(extra_all[:12])}")
    if len(all_covered & expected_all) != EXPECTED_TOTAL_PARAGRAPHS:
        errors.append("max-read-ledger.json: read_ranges union must cover exactly 3273 source paragraphs")


def check_claim_ledger(data: Any, source_ids: set[str], errors: list[str]) -> None:
    if not isinstance(data, dict) or not isinstance(data.get("claims"), list):
        errors.append("max-claim-ledger.json: claims must be a list")
        return
    if not data["claims"]:
        errors.append("max-claim-ledger.json: claims must contain at least one final claim")
    for idx, claim in enumerate(data["claims"], start=1):
        if not isinstance(claim, dict):
            errors.append(f"max-claim-ledger.json: claim {idx} must be an object")
            continue
        label = claim.get("claim_id", f"claim {idx}")
        paragraph_ids = claim.get("source_paragraph_ids")
        if not paragraph_ids:
            errors.append(f"max-claim-ledger.json: {label} missing source_paragraph_ids")
        else:
            for pid in paragraph_ids:
                if not isinstance(pid, str) or not SOURCE_ID_RE.match(pid):
                    errors.append(f"max-claim-ledger.json: {label} invalid source paragraph id: {pid}")
                elif pid not in source_ids:
                    errors.append(f"max-claim-ledger.json: {label} source paragraph id not in v6 source: {pid}")
        for field in ["counterevidence_status", "downgrade_condition", "withdrawal_condition", "action_limit"]:
            if not claim.get(field):
                errors.append(f"max-claim-ledger.json: {label} missing {field}")
        if not claim.get("concept_ids"):
            errors.append(f"max-claim-ledger.json: {label} missing concept_ids")


def check_concept_hits(data: Any, source_ids: set[str], errors: list[str]) -> None:
    if not isinstance(data, dict) or not isinstance(data.get("concept_hits"), list):
        errors.append("max-concept-hit-ledger.json: concept_hits must be a list")
        return
    if not data["concept_hits"]:
        errors.append("max-concept-hit-ledger.json: concept_hits must contain at least one concept hit")
    for idx, hit in enumerate(data["concept_hits"], start=1):
        if not isinstance(hit, dict):
            errors.append(f"max-concept-hit-ledger.json: hit {idx} must be an object")
            continue
        label = hit.get("concept_id", f"hit {idx}")
        if hit.get("hit_type") not in {"direct", "neighbor", "conflict", "gap"}:
            errors.append(f"max-concept-hit-ledger.json: {label} invalid hit_type")
        if hit.get("contract_checked") is not True:
            errors.append(f"max-concept-hit-ledger.json: {label} contract_checked must be true")
        paragraph_ids = hit.get("source_paragraph_ids")
        if not paragraph_ids:
            errors.append(f"max-concept-hit-ledger.json: {label} missing source_paragraph_ids")
            continue
        for pid in paragraph_ids:
            if not isinstance(pid, str) or not SOURCE_ID_RE.match(pid):
                errors.append(f"max-concept-hit-ledger.json: {label} invalid source paragraph id: {pid}")
            elif pid not in source_ids:
                errors.append(f"max-concept-hit-ledger.json: {label} source paragraph id not in v6 source: {pid}")


def check_audit(data: Any, source_ids: set[str], errors: list[str]) -> None:
    if not isinstance(data, dict) or not isinstance(data.get("audits"), list):
        errors.append("max-evidence-reasoning-audit.json: audits must be a list")
        return
    if not data["audits"]:
        errors.append("max-evidence-reasoning-audit.json: audits must contain at least one audit")
    for idx, audit in enumerate(data["audits"], start=1):
        if not isinstance(audit, dict):
            errors.append(f"max-evidence-reasoning-audit.json: audit {idx} must be an object")
            continue
        label = audit.get("claim_id", f"audit {idx}")
        for field in ["evidence_chain", "reasoning_chain", "counterevidence_status", "calibration_rounds", "final_strength"]:
            if not audit.get(field):
                errors.append(f"max-evidence-reasoning-audit.json: {label} missing {field}")
        paragraph_ids = audit.get("source_paragraph_ids")
        if not paragraph_ids:
            errors.append(f"max-evidence-reasoning-audit.json: {label} missing source_paragraph_ids")
        else:
            for pid in paragraph_ids:
                if not isinstance(pid, str) or not SOURCE_ID_RE.match(pid):
                    errors.append(f"max-evidence-reasoning-audit.json: {label} invalid source paragraph id: {pid}")
                elif pid not in source_ids:
                    errors.append(f"max-evidence-reasoning-audit.json: {label} source paragraph id not in v6 source: {pid}")
        if audit.get("final_output_allowed") is not True:
            errors.append(f"max-evidence-reasoning-audit.json: {label} final_output_allowed must be true for final artifacts")


def check_cross_ledger_consistency(claim_data: Any, concept_data: Any, audit_data: Any, errors: list[str]) -> None:
    if not all(isinstance(data, dict) for data in [claim_data, concept_data, audit_data]):
        return
    claims = claim_data.get("claims")
    concept_hits = concept_data.get("concept_hits")
    audits = audit_data.get("audits")
    if not all(isinstance(items, list) for items in [claims, concept_hits, audits]):
        return
    claim_ids = {claim.get("claim_id") for claim in claims if isinstance(claim, dict) and claim.get("claim_id")}
    audit_claim_ids = {audit.get("claim_id") for audit in audits if isinstance(audit, dict) and audit.get("claim_id")}
    concept_ids = {hit.get("concept_id") for hit in concept_hits if isinstance(hit, dict) and hit.get("concept_id")}
    if claim_ids - audit_claim_ids:
        errors.append(f"cross-ledger: claims missing audits: {', '.join(sorted(claim_ids - audit_claim_ids))}")
    if audit_claim_ids - claim_ids:
        errors.append(f"cross-ledger: audits without matching claims: {', '.join(sorted(audit_claim_ids - claim_ids))}")
    for claim in claims:
        if not isinstance(claim, dict):
            continue
        label = claim.get("claim_id", "unknown claim")
        missing_concepts = set(claim.get("concept_ids") or []) - concept_ids
        if missing_concepts:
            errors.append(
                f"cross-ledger: {label} concept_ids missing concept hits: {', '.join(sorted(missing_concepts))}"
            )


def check(workspace: Path, skill_root: Path) -> list[str]:
    errors: list[str] = []
    source_ids = source_ids_from_skill(skill_root)
    if len(source_ids) != EXPECTED_TOTAL_PARAGRAPHS:
        errors.append(f"skill source ids mismatch: expected 3273, got {len(source_ids)}")
    read_ledger = read_json(workspace / "max-read-ledger.json", errors)
    claim_ledger = read_json(workspace / "max-claim-ledger.json", errors)
    concept_hits = read_json(workspace / "max-concept-hit-ledger.json", errors)
    audit = read_json(workspace / "max-evidence-reasoning-audit.json", errors)
    if read_ledger is not None:
        check_read_ledger(read_ledger, errors)
    if claim_ledger is not None:
        check_claim_ledger(claim_ledger, source_ids, errors)
    if concept_hits is not None:
        check_concept_hits(concept_hits, source_ids, errors)
    if audit is not None:
        check_audit(audit, source_ids, errors)
    check_cross_ledger_consistency(claim_ledger, concept_hits, audit, errors)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Check crossframe-max structured read, claim, concept, and audit ledgers.")
    parser.add_argument("--workspace", default=".", help="Directory containing max structured ledger JSON files.")
    parser.add_argument("--skill-root", default="skills/crossframe-max", help="Path to crossframe-max skill root.")
    args = parser.parse_args()
    errors = check(Path(args.workspace).resolve(), Path(args.skill_root).resolve())
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("ok: crossframe-max structured ledgers passed coverage checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
