from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ANCHOR_RE = re.compile(r"`([^`]+\.md)`\s+`(P\d{4})(?:-P?(\d{4}))?`")
SOURCE_RE = re.compile(r"^<!-- source_paragraph:(P\d{4}) style=.* -->$")


def source_ids(path: Path) -> set[str]:
    ids: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        match = SOURCE_RE.match(line)
        if match:
            ids.add(match.group(1))
    return ids


def ids_for_range(start: str, end_digits: str | None) -> list[str]:
    start_n = int(start[1:])
    end_n = int(end_digits) if end_digits else start_n
    if end_n < start_n:
        raise ValueError(f"invalid descending range: {start}-P{end_n:04d}")
    return [f"P{i:04d}" for i in range(start_n, end_n + 1)]


def check(repo: Path) -> list[str]:
    errors: list[str] = []
    max_root = repo / "skills" / "crossframe-max"
    registry = max_root / "references" / "concept-registry" / "index.md"
    source_dir = max_root / "references" / "v6-full-source"
    if not registry.exists():
        return [f"missing registry: {registry}"]
    if not source_dir.is_dir():
        return [f"missing v6 full-source directory: {source_dir}"]

    cache: dict[str, set[str]] = {}
    registry_text = registry.read_text(encoding="utf-8")
    for match in ANCHOR_RE.finditer(registry_text):
        file_name, start, end_digits = match.groups()
        path = source_dir / file_name
        if not path.exists():
            errors.append(f"missing anchor file: {file_name}")
            continue
        if file_name not in cache:
            cache[file_name] = source_ids(path)
        try:
            needed = ids_for_range(start, end_digits)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        missing = [pid for pid in needed if pid not in cache[file_name]]
        if missing:
            errors.append(f"{registry}: {file_name} missing paragraph ids: {', '.join(missing[:12])}")
    if "P0585-P0621" in registry_text and "条件势场" in registry_text:
        errors.append("registry still contains suspicious 条件势场 P0585-P0621 anchor")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Check crossframe-max concept-registry source anchors.")
    parser.add_argument("--repo", default=".", help="Repository root.")
    args = parser.parse_args()
    errors = check(Path(args.repo).resolve())
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("ok: crossframe-max registry anchors resolve to v6 full-source paragraphs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
