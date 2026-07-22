from __future__ import annotations

import copy
from pathlib import Path
import re
from typing import Mapping, Sequence

from .artifacts import inventory_artifacts, validate_role_records
from .errors import RunBindingError
from .jsonio import sha256_json
from .paths import validate_relative_artifact_path
from .schemas import validate_instance


_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


class ReplayBindingError(ValueError):
    """Raised when a validator report is stale or belongs to another run."""


def validate_bound_document(
    schema_name: str,
    document: Mapping[str, object],
    *,
    expected_run_id: str,
    expected_source_snapshot_sha256: str,
) -> dict[str, object]:
    if not isinstance(document, Mapping):
        raise ValueError(f"{schema_name} artifact must be a structured object")
    if document.get("run_id") != expected_run_id:
        raise RunBindingError(f"{schema_name} is bound to a different run_id")
    if document.get("source_snapshot_sha256") != expected_source_snapshot_sha256:
        raise RunBindingError(
            f"{schema_name} is bound to a different source snapshot"
        )
    normalized = copy.deepcopy(dict(document))
    validate_instance(schema_name, normalized)
    return normalized


def validator_set_sha256(validator_versions: Mapping[str, str]) -> str:
    if not isinstance(validator_versions, Mapping) or not validator_versions:
        raise ValueError("validator_versions must be a non-empty mapping")
    records: list[dict[str, str]] = []
    normalized_versions: dict[str, str] = {}
    for validator_id, version in validator_versions.items():
        if not isinstance(validator_id, str) or not validator_id.strip():
            raise ValueError("validator identifiers must be non-empty strings")
        if not isinstance(version, str) or not version.strip():
            raise ValueError("validator versions must be non-empty strings")
        normalized_id = validator_id.strip()
        if normalized_id in normalized_versions:
            raise ValueError("validator identifiers must be unique after normalization")
        normalized_versions[normalized_id] = version.strip()
    for validator_id in sorted(normalized_versions):
        records.append(
            {"validator_id": validator_id, "version": normalized_versions[validator_id]}
        )
    return sha256_json({"validators": records})


def _current_artifact_refs(
    manifest: Mapping[str, object],
) -> list[dict[str, str]]:
    artifacts = manifest.get("artifacts")
    if not isinstance(artifacts, list):
        raise ReplayBindingError("manifest artifacts must be an array")
    refs: list[dict[str, str]] = []
    seen: set[str] = set()
    for index, item in enumerate(artifacts):
        if not isinstance(item, Mapping):
            raise ReplayBindingError(f"manifest artifact {index} is not an object")
        if item.get("status") != "current":
            continue
        path = item.get("path")
        digest = item.get("sha256")
        media_type = item.get("media_type")
        if not isinstance(path, str) or path in seen:
            raise ReplayBindingError("manifest has duplicate or invalid current paths")
        if not isinstance(digest, str) or _SHA256_RE.fullmatch(digest) is None:
            raise ReplayBindingError(f"manifest artifact hash is invalid: {path}")
        if not isinstance(media_type, str) or "/" not in media_type:
            raise ReplayBindingError(f"manifest media type is invalid: {path}")
        seen.add(path)
        refs.append({"path": path, "sha256": digest, "media_type": media_type})
    if not refs:
        raise ReplayBindingError("manifest has no current artifacts")
    return sorted(refs, key=lambda item: item["path"])


def _assert_manifest_self_hash(manifest: Mapping[str, object]) -> None:
    expected = manifest.get("manifest_sha256")
    if not isinstance(expected, str) or _SHA256_RE.fullmatch(expected) is None:
        raise ReplayBindingError("manifest_sha256 is invalid")
    unsigned = dict(manifest)
    unsigned.pop("manifest_sha256", None)
    if sha256_json(unsigned) != expected:
        raise ReplayBindingError("manifest_sha256 does not bind the current manifest")


def _validate_manifest_semantics(
    run_contract: Mapping[str, object],
    manifest: Mapping[str, object],
) -> None:
    validate_instance("promax-run-contract.schema.json", dict(run_contract))
    validate_instance("promax-artifact-manifest.schema.json", dict(manifest))
    _assert_manifest_self_hash(manifest)
    if manifest.get("run_contract_sha256") != sha256_json(dict(run_contract)):
        raise ReplayBindingError("manifest is bound to a different run contract")
    for field in (
        "run_id",
        "run_nonce",
        "request_sha256",
        "source_snapshot_sha256",
        "mode",
        "orchestration_mode",
    ):
        if manifest.get(field) != run_contract.get(field):
            raise ReplayBindingError(f"manifest changes immutable run binding: {field}")

    artifacts = manifest.get("artifacts")
    role_records = manifest.get("role_records")
    if not isinstance(artifacts, list) or not isinstance(role_records, list):
        raise ReplayBindingError("manifest artifact and role records must be arrays")
    known: dict[str, str] = {}
    folded_paths: dict[str, str] = {}
    for index, item in enumerate(artifacts):
        if not isinstance(item, Mapping):
            raise ReplayBindingError(f"manifest artifact {index} is not an object")
        path = item.get("path")
        digest = item.get("sha256")
        if not isinstance(path, str) or not isinstance(digest, str):
            raise ReplayBindingError(f"manifest artifact {index} has an invalid binding")
        try:
            validate_relative_artifact_path(path)
        except ValueError as error:
            raise ReplayBindingError(
                f"manifest artifact {index} has an unsafe path: {error}"
            ) from error
        if _SHA256_RE.fullmatch(digest) is None:
            raise ReplayBindingError(f"manifest artifact {index} has an invalid hash")
        if path in known:
            raise ReplayBindingError(f"manifest contains duplicate artifact path: {path}")
        folded = path.casefold()
        if folded in folded_paths:
            raise ReplayBindingError(
                "manifest contains a casefold artifact path alias: "
                f"{folded_paths[folded]!r} and {path!r}"
            )
        if item.get("status") == "current":
            known[path] = digest
        folded_paths[folded] = path
    try:
        validate_role_records(
            run_contract,
            role_records,
            known,
            artifact_records=artifacts,
        )
    except (RunBindingError, TypeError, ValueError) as error:
        raise ReplayBindingError(f"manifest role contract is invalid: {error}") from error


def _validate_current_artifact_bytes(
    run_dir: Path | str,
    manifest: Mapping[str, object],
) -> None:
    artifacts = manifest.get("artifacts")
    if not isinstance(artifacts, list):
        raise ReplayBindingError("manifest artifacts must be an array")
    expected: list[dict[str, object]] = []
    metadata: dict[str, dict[str, object]] = {}
    for item in artifacts:
        if not isinstance(item, Mapping) or item.get("status") != "current":
            continue
        record = copy.deepcopy(dict(item))
        path = record.get("path")
        if not isinstance(path, str):
            raise ReplayBindingError("current artifact path is invalid")
        expected.append(record)
        metadata[path] = {
            "generating_phase": record.get("generating_phase"),
            "input_artifact_sha256s": record.get("input_artifact_sha256s"),
            "status": "current",
        }
    try:
        observed = inventory_artifacts(run_dir, metadata)
    except (OSError, RuntimeError, TypeError, ValueError) as error:
        raise ReplayBindingError(f"manifest current artifact bytes are stale: {error}") from error
    key = lambda item: str(item.get("path"))
    if sorted(observed, key=key) != sorted(expected, key=key):
        raise ReplayBindingError("manifest does not match current artifact bytes")


def _frozen_validator_ids(run_contract: Mapping[str, object]) -> set[str]:
    capabilities = run_contract.get("capabilities")
    validators = capabilities.get("validators") if isinstance(capabilities, Mapping) else None
    validator_ids = validators.get("validator_ids") if isinstance(validators, Mapping) else None
    if not isinstance(validator_ids, list) or any(
        not isinstance(item, str) or not item for item in validator_ids
    ):
        raise ReplayBindingError("run contract has an invalid frozen validator set")
    if len(set(validator_ids)) != len(validator_ids):
        raise ReplayBindingError("run contract has duplicate frozen validators")
    return set(validator_ids)


def _validate_validator_versions_binding(
    run_contract: Mapping[str, object],
    validator_versions: Mapping[str, str],
) -> set[str]:
    validator_set_sha256(validator_versions)
    supplied = set(validator_versions)
    frozen = _frozen_validator_ids(run_contract)
    if supplied != frozen:
        raise ReplayBindingError(
            "validator versions must match the exact set frozen in the run contract"
        )
    return supplied


def _validate_completion_binding(
    run_contract: Mapping[str, object],
    completion_status: object,
    *,
    error_type: type[ValueError],
) -> None:
    run_mode = run_contract.get("mode")
    incomplete = isinstance(completion_status, str) and completion_status.startswith(
        "promax-artifact-incomplete:"
    )
    if completion_status != run_mode and not incomplete:
        raise error_type("completion status contradicts the frozen run mode")
    if run_mode == "promax-blocked/progress" and completion_status != run_mode:
        raise error_type("a blocked/progress run can never claim completion")


def _validate_report_check_semantics(
    checks: Sequence[Mapping[str, object]],
    *,
    validator_ids: set[str],
    completion_status: object,
    reported_overall_status: object | None = None,
    error_type: type[ValueError] = ValueError,
) -> tuple[list[dict[str, object]], str]:
    if not isinstance(checks, Sequence) or isinstance(checks, (str, bytes)) or not checks:
        raise error_type("checks must be a non-empty structured sequence")
    normalized_checks: list[dict[str, object]] = []
    checked_validator_ids: list[str] = []
    statuses: list[str] = []
    for raw_check in checks:
        if not isinstance(raw_check, Mapping):
            raise error_type("every validator check must be a structured object")
        check = copy.deepcopy(dict(raw_check))
        validator_id = check.get("validator_id")
        if not isinstance(validator_id, str) or validator_id not in validator_ids:
            raise error_type(f"check uses an unfrozen validator: {validator_id!r}")
        status = check.get("status")
        if status not in {"pass", "fail", "blocked"}:
            raise error_type(f"check has an invalid status: {status!r}")
        checked_validator_ids.append(validator_id)
        statuses.append(status)
        normalized_checks.append(check)
    if (
        len(set(checked_validator_ids)) != len(checked_validator_ids)
        or set(checked_validator_ids) != validator_ids
    ):
        raise error_type(
            "validator report must contain exactly one check for every frozen validator"
        )
    overall_status = (
        "fail" if "fail" in statuses else "blocked" if "blocked" in statuses else "pass"
    )
    if reported_overall_status is not None and reported_overall_status != overall_status:
        raise error_type("validator report overall status contradicts its checks")
    if completion_status == "promax-complete" and overall_status != "pass":
        raise error_type("promax-complete requires every validator check to pass")
    return normalized_checks, overall_status


def build_validator_report(
    run_contract: Mapping[str, object],
    manifest: Mapping[str, object],
    *,
    validator_versions: Mapping[str, str],
    checks: Sequence[Mapping[str, object]],
    validation_attempt: int,
    completion_status: str,
    validated_at: str,
    run_dir: Path | str,
) -> dict[str, object]:
    _validate_manifest_semantics(run_contract, manifest)
    _validate_current_artifact_bytes(run_dir, manifest)
    if type(validation_attempt) is not int or validation_attempt < 1:
        raise ValueError("validation_attempt must be a positive integer")
    if not isinstance(validated_at, str) or not validated_at.strip():
        raise ValueError("validated_at must be a non-empty timestamp")
    validator_ids = _validate_validator_versions_binding(
        run_contract, validator_versions
    )
    _validate_completion_binding(
        run_contract,
        completion_status,
        error_type=ValueError,
    )
    normalized_checks, overall_status = _validate_report_check_semantics(
        checks,
        validator_ids=validator_ids,
        completion_status=completion_status,
    )
    body: dict[str, object] = {
        "schema_id": "crossframe.promax.v8.validator-report",
        "schema_version": 1,
        "run_id": run_contract["run_id"],
        "run_nonce": run_contract["run_nonce"],
        "request_sha256": run_contract["request_sha256"],
        "source_snapshot_sha256": run_contract["source_snapshot_sha256"],
        "phase_chain_head_sha256": manifest["phase_chain_head_sha256"],
        "manifest_sha256": manifest["manifest_sha256"],
        "validator_set_sha256": validator_set_sha256(validator_versions),
        "validation_attempt": validation_attempt,
        "current_artifact_hashes": _current_artifact_refs(manifest),
        "checks": normalized_checks,
        "overall_status": overall_status,
        "completion_status": completion_status,
        "validated_at": validated_at.strip(),
    }
    report = {**body, "report_sha256": sha256_json(body)}
    validate_instance("promax-validator-report.schema.json", report)
    return report


def validate_validator_report_freshness(
    report: Mapping[str, object],
    run_contract: Mapping[str, object],
    manifest: Mapping[str, object],
    *,
    validator_versions: Mapping[str, str],
    expected_validation_attempt: int,
    run_dir: Path | str,
) -> dict[str, object]:
    if not isinstance(report, Mapping):
        raise ReplayBindingError("validator report must be a structured object")
    _validate_manifest_semantics(run_contract, manifest)
    _validate_current_artifact_bytes(run_dir, manifest)
    _validate_validator_versions_binding(run_contract, validator_versions)
    _validate_completion_binding(
        run_contract,
        report.get("completion_status"),
        error_type=ReplayBindingError,
    )
    bindings = {
        "run_id": run_contract.get("run_id"),
        "run_nonce": run_contract.get("run_nonce"),
        "request_sha256": run_contract.get("request_sha256"),
        "source_snapshot_sha256": run_contract.get("source_snapshot_sha256"),
        "phase_chain_head_sha256": manifest.get("phase_chain_head_sha256"),
        "manifest_sha256": manifest.get("manifest_sha256"),
        "validator_set_sha256": validator_set_sha256(validator_versions),
        "validation_attempt": expected_validation_attempt,
    }
    for field, expected in bindings.items():
        if report.get(field) != expected:
            raise ReplayBindingError(
                f"validator report replay binding mismatch for {field}"
            )
    if report.get("current_artifact_hashes") != _current_artifact_refs(manifest):
        raise ReplayBindingError("validator report artifact inventory is stale")
    checks = report.get("checks")
    if not isinstance(checks, list):
        raise ReplayBindingError("validator report checks must be an array")
    _validate_report_check_semantics(
        checks,
        validator_ids=set(validator_versions),
        completion_status=report.get("completion_status"),
        reported_overall_status=report.get("overall_status"),
        error_type=ReplayBindingError,
    )
    expected_report_sha = report.get("report_sha256")
    unsigned = dict(report)
    unsigned.pop("report_sha256", None)
    if (
        not isinstance(expected_report_sha, str)
        or _SHA256_RE.fullmatch(expected_report_sha) is None
        or sha256_json(unsigned) != expected_report_sha
    ):
        raise ReplayBindingError("validator report self-hash is stale")
    normalized = copy.deepcopy(dict(report))
    validate_instance("promax-validator-report.schema.json", normalized)
    return normalized
