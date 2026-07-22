from __future__ import annotations

import re
from pathlib import Path

from check_crossframe_promax_v8_knowledge import (
    pollution_errors_for_text as _canonical_pollution_errors_for_text,
    scan_version_pollution as _canonical_scan_version_pollution,
)


class ExplicitRouteError(ValueError):
    """Raised when a request did not explicitly name CrossFrame ProMax."""


class VersionPollutionError(ValueError):
    """Raised when non-v8 knowledge or unsafe assets enter the ProMax skill."""

    def __init__(self, errors: list[str]) -> None:
        self.errors = tuple(errors)
        super().__init__("; ".join(errors))


_PROMAX_PATTERNS = (
    re.compile(r"(?<![A-Za-z0-9_-])crossframe-promax(?![A-Za-z0-9_-])"),
    re.compile(r"(?<![A-Za-z0-9_-])CrossFrame ProMax(?![A-Za-z0-9_-])"),
)
_MAX_WORD = "m" + "ax"
_SIBLING_SKILL = "crossframe-" + _MAX_WORD
_MAX_PATTERNS = (
    re.compile(
        r"(?<![A-Za-z0-9_-])" + re.escape(_SIBLING_SKILL) + r"(?![A-Za-z0-9_-])"
    ),
    re.compile(
        r"(?<![A-Za-z0-9_-])"
        + re.escape("CrossFrame " + _MAX_WORD.title())
        + r"(?![A-Za-z0-9_-])"
    ),
)


def _contains_any(text: str, patterns: tuple[re.Pattern[str], ...]) -> bool:
    return any(pattern.search(text) is not None for pattern in patterns)


def pollution_errors_for_text(text: str, path_label: str) -> list[str]:
    """Apply the canonical repository v8-only lexical/path isolation rules."""

    if not isinstance(text, str) or not isinstance(path_label, str):
        raise TypeError("pollution scan inputs must be strings")
    return _canonical_pollution_errors_for_text(text, path_label)


def scan_version_pollution(skill_root: Path | str) -> list[str]:
    """Scan one ProMax skill tree with the canonical version-isolation core."""

    root = Path(skill_root)
    if not root.is_dir():
        raise ValueError(f"skill root is not a directory: {root}")
    return _canonical_scan_version_pollution(root)


def validate_version_isolation(skill_root: Path | str) -> dict[str, int]:
    """Require zero pollution and return an auditable scan summary."""

    root = Path(skill_root)
    errors = scan_version_pollution(root)
    if errors:
        raise VersionPollutionError(errors)
    scanned_file_count = sum(
        1
        for path in root.rglob("*")
        if path.is_file()
        and not any(part.casefold() == "__pycache__" for part in path.relative_to(root).parts)
    )
    return {
        "scanned_file_count": scanned_file_count,
        "pollution_count": 0,
    }


def resolve_explicit_route(request_text: str) -> dict[str, object]:
    """Resolve only the four approved ProMax spellings.

    ``$crossframe-promax`` and ``/crossframe-promax`` are recognized because
    they contain the exact lower-case token with a non-word command prefix.
    Semantic approximations and bare ``ProMax`` never activate this runtime.
    """

    if not isinstance(request_text, str):
        raise ExplicitRouteError("request text must be a string")
    promax_requested = _contains_any(request_text, _PROMAX_PATTERNS)
    if not promax_requested:
        raise ExplicitRouteError(
            "CrossFrame ProMax requires one exact explicit trigger: "
            "crossframe-promax, CrossFrame ProMax, $crossframe-promax, "
            "or /crossframe-promax"
        )
    max_requested = _contains_any(request_text, _MAX_PATTERNS)
    requested_names = ["crossframe-promax"]
    conflicting_names: list[str] = []
    if max_requested:
        requested_names.append(_SIBLING_SKILL)
        conflicting_names = ["crossframe-promax", _SIBLING_SKILL]
    return {
        "requested_skill_names": requested_names,
        "routing_conflict": {
            "detected": max_requested,
            "conflicting_names": conflicting_names,
            "resolved_to": "crossframe-promax",
            "priority_rule": (
                "routing-priority-crossframe-promax-over-"
                + _SIBLING_SKILL
                + "-no-fallback"
            ),
            "fallback_allowed": False,
        },
    }
