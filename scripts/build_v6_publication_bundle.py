from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path


BUNDLE_SOURCE_FILES = [
    "docs/CROSSFRAME_V6.md",
    "docs/V5_TO_V6_CHANGES.md",
    "docs/V6_TOOL_PROTOTYPE.md",
    "skills/crossframe/references/construct-map-v6.md",
    "skills/crossframe/worksheets/seven-gates-quant-rubric.md",
    "skills/crossframe/worksheets/evidence-ledger-v6.md",
    "skills/crossframe/worksheets/calibration-anchor-card.md",
    "skills/crossframe/worksheets/mechanism-update-rules.md",
    "skills/crossframe/worksheets/counterexample-register.md",
    "skills/crossframe/references/judgment-action-matrix-v6.md",
    "skills/crossframe/references/falsification-governance-v6.md",
    "skills/crossframe-casebook/examples/v6-quant-trials/validation-summary.md",
]

PROTOTYPE_AUDIT_FILES = [
    "scripts/build_v6_publication_bundle.py",
    "scripts/build_v6_docx.py",
    "scripts/check_v6_publication_bundle.py",
    "scripts/validate_v6_quantification_schema_fixtures.py",
    "scripts/check_v6_casebook_trials.py",
    "skills/crossframe/schemas/seven-gates-quant.schema.json",
    "skills/crossframe/schemas/evidence-ledger-v6.schema.json",
    "skills/crossframe/schemas/calibration-anchor.schema.json",
    "skills/crossframe/schemas/mechanism-update.schema.json",
    "skills/crossframe/schemas/counterexample-register.schema.json",
]

SOURCE_FILES = BUNDLE_SOURCE_FILES + PROTOTYPE_AUDIT_FILES


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_bundle(repo: Path, output_dir: Path, stamp: str) -> tuple[Path, Path, list[dict[str, object]]]:
    output_dir.mkdir(parents=True, exist_ok=True)
    bundle_path = output_dir / f"crossframe-v6.0-publication-{stamp}.md"
    manifest_path = output_dir / f"crossframe-v6.0-publication-{stamp}.manifest.json"

    manifest_sources: list[dict[str, object]] = []
    parts = [
        "# CrossFrame v6.0 Publication Bundle",
        "",
        "This generated bundle is an audit artifact. The tracked Markdown files remain the source of truth.",
        "",
    ]

    for rel in SOURCE_FILES:
        path = repo / rel
        if not path.exists():
            raise SystemExit(f"missing publication source: {rel}")
        manifest_sources.append(
            {
                "path": rel,
                "sha256": sha256(path),
                "bytes": path.stat().st_size,
                "included_in_bundle": rel in BUNDLE_SOURCE_FILES,
            }
        )
        if rel not in BUNDLE_SOURCE_FILES:
            continue
        parts.extend(
            [
                f"---\n\n## Source: `{rel}`\n",
                read(path).rstrip(),
                "",
            ]
        )

    bundle_path.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")
    manifest = {
        "bundle": bundle_path.name,
        "generated_at": stamp,
        "source_count": len(manifest_sources),
        "sources": manifest_sources,
    }
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return bundle_path, manifest_path, manifest_sources


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the CrossFrame v6.0 publication bundle.")
    parser.add_argument("--repo", default=".", help="Repository root.")
    parser.add_argument("--output-dir", default="outputs", help="Output directory for generated artifacts.")
    parser.add_argument("--stamp", default=None, help="Stable stamp for deterministic smoke tests.")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    stamp = args.stamp or dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    bundle_path, manifest_path, sources = build_bundle(repo, repo / args.output_dir, stamp)
    print(f"created: {bundle_path}")
    print(f"created: {manifest_path}")
    print(f"sources: {len(sources)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
