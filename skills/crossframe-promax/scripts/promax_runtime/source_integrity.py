from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Mapping

from .jsonio import load_json_bytes
from .safe_files import read_stable_regular_file
from .schemas import validate_instance


V8_SOURCE_SNAPSHOT_SHA256 = (
    "3186805a3e46e1b16948a4e51d08e7693a8e0dd04aa6b4604e796266d649936c"
)
V8_PARAGRAPH_COUNT = 3863
V8_NON_WHITESPACE_CHARS = 155721
V8_TABLE_COUNT = 117
V8_SECTION_COUNT = 16
V8_CONCEPT_COUNT = 709


def sha256_file(path: Path | str) -> str:
    source = Path(path)
    raw = read_stable_regular_file(source, within_root=source.parent)
    return hashlib.sha256(raw).hexdigest()


def _load_object_and_hash(path: Path, *, root: Path) -> tuple[dict[str, object], str]:
    raw = read_stable_regular_file(path, within_root=root)
    value = load_json_bytes(raw, source=str(path))
    if not isinstance(value, dict):
        raise ValueError(f"canonical v8 asset must be a JSON object: {path}")
    return value, hashlib.sha256(raw).hexdigest()


def _require_exact(
    document: Mapping[str, object],
    expected: Mapping[str, object],
    *,
    source: Path,
) -> None:
    for field, expected_value in expected.items():
        actual = document.get(field)
        if actual != expected_value:
            raise ValueError(
                f"canonical v8 asset {source} has {field}={actual!r}; "
                f"expected {expected_value!r}"
            )


def build_source_snapshot(
    repo: Path | str,
    *,
    verified_at: str,
) -> dict[str, object]:
    """Freeze the four canonical v8 control assets into one runtime snapshot.

    Full paragraph/table byte validation remains the P1 validator's job.  This
    helper binds a run to the committed manifest and knowledge graph files so a
    later report cannot silently substitute another set of control assets.
    """

    repo_root = Path(repo).resolve()
    references = repo_root / "skills" / "crossframe-promax" / "references"
    paths = {
        "source_manifest": references / "source_manifest.json",
        "concept_registry": references
        / "concept-registry"
        / "v8-concept-registry.json",
        "contract_map": references
        / "concept-contracts"
        / "v8-contract-map.json",
        "route_map": references / "v8-route-map.json",
    }
    loaded = {
        name: _load_object_and_hash(path, root=references)
        for name, path in paths.items()
    }
    documents = {name: document for name, (document, _) in loaded.items()}
    hashes = {name: digest for name, (_, digest) in loaded.items()}

    _require_exact(
        documents["source_manifest"],
        {
            "schema_id": "crossframe.promax.v8.source-manifest",
            "schema_version": 1,
            "framework_version": "v8.0",
            "snapshot_sha256": V8_SOURCE_SNAPSHOT_SHA256,
            "paragraph_count": V8_PARAGRAPH_COUNT,
            "non_whitespace_chars": V8_NON_WHITESPACE_CHARS,
            "table_count": V8_TABLE_COUNT,
            "section_count": V8_SECTION_COUNT,
        },
        source=paths["source_manifest"],
    )
    _require_exact(
        documents["concept_registry"],
        {
            "schema_id": "crossframe.promax.v8.concept-registry",
            "schema_version": 1,
            "framework_version": "v8.0",
            "snapshot_sha256": V8_SOURCE_SNAPSHOT_SHA256,
            "concept_count": V8_CONCEPT_COUNT,
        },
        source=paths["concept_registry"],
    )
    _require_exact(
        documents["contract_map"],
        {
            "schema_id": "crossframe.promax.v8.contract-map",
            "schema_version": 1,
            "framework_version": "v8.0",
            "snapshot_sha256": V8_SOURCE_SNAPSHOT_SHA256,
            "contract_count": 3,
        },
        source=paths["contract_map"],
    )
    _require_exact(
        documents["route_map"],
        {
            "schema_id": "crossframe.promax.v8.route-map",
            "schema_version": 1,
            "framework_version": "v8.0",
            "snapshot_sha256": V8_SOURCE_SNAPSHOT_SHA256,
            "route_count": 16,
        },
        source=paths["route_map"],
    )
    for name, path in paths.items():
        if sha256_file(path) != hashes[name]:
            raise ValueError(
                f"canonical v8 asset changed during snapshot verification: {path}"
            )
    if not isinstance(verified_at, str) or not verified_at.strip():
        raise ValueError("verified_at must be a non-empty timestamp")

    snapshot: dict[str, object] = {
        "schema_id": "crossframe.promax.v8.source-snapshot",
        "schema_version": 1,
        "framework_version": "v8.0",
        "snapshot_id": "crossframe-promax-v8-source-3186805a",
        "source_snapshot_sha256": V8_SOURCE_SNAPSHOT_SHA256,
        "source_manifest_sha256": hashes["source_manifest"],
        "concept_registry_sha256": hashes["concept_registry"],
        "contract_map_sha256": hashes["contract_map"],
        "route_map_sha256": hashes["route_map"],
        "paragraph_count": V8_PARAGRAPH_COUNT,
        "non_whitespace_chars": V8_NON_WHITESPACE_CHARS,
        "table_count": V8_TABLE_COUNT,
        "section_count": V8_SECTION_COUNT,
        "verified_at": verified_at.strip(),
    }
    validate_instance("promax-source-snapshot.schema.json", snapshot)
    return snapshot
