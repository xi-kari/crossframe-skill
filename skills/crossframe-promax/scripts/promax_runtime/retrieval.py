from __future__ import annotations

from typing import Mapping

from .validation import validate_bound_document


RETRIEVAL_DIRECTIONS = (
    "support",
    "reverse",
    "failure_case",
    "alternative_mechanism",
    "affected_or_low_power_position",
)


def validate_retrieval_ledger(
    document: Mapping[str, object],
    *,
    expected_run_id: str,
    expected_source_snapshot_sha256: str,
) -> dict[str, object]:
    return validate_bound_document(
        "promax-retrieval-ledger.schema.json",
        document,
        expected_run_id=expected_run_id,
        expected_source_snapshot_sha256=expected_source_snapshot_sha256,
    )
