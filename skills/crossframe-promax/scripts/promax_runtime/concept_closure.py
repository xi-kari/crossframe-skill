from __future__ import annotations

from typing import Mapping

from .validation import validate_bound_document


def validate_concept_disposition(
    document: Mapping[str, object],
    *,
    expected_run_id: str,
    expected_source_snapshot_sha256: str,
) -> dict[str, object]:
    """Validate the closed P4 artifact shape and immutable run binding.

    Registry-wide disposition and neighbor closure are deliberately enforced by
    the semantic artifact validator, not inferred by this schema-bound helper.
    """

    return validate_bound_document(
        "promax-concept-disposition.schema.json",
        document,
        expected_run_id=expected_run_id,
        expected_source_snapshot_sha256=expected_source_snapshot_sha256,
    )
