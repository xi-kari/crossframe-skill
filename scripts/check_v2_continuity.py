from __future__ import annotations

import argparse
import re
from pathlib import Path

from docx import Document


REQUIRED_BUNDLES = {
    "framework-use-discipline-pack",
    "judgment-responsibility-pack",
    "diagnosis-mainline-pack",
    "intimate-love-care-pack",
    "public-power-governance-pack",
    "long-evolution-deep-pack",
    "expression-article-pack",
}


def extract_docx_headings(path: Path) -> list[str]:
    doc = Document(str(path))
    headings: list[str] = []
    for para in doc.paragraphs:
        text = " ".join(para.text.split())
        if text and para.style.name.startswith("Heading"):
            headings.append(text)
    return headings


def main() -> int:
    parser = argparse.ArgumentParser(description="Check CrossFrame v2.0 source continuity files.")
    parser.add_argument("--docx", default=r"D:\下载\跨尺度结构诊断框架v2.0.docx")
    parser.add_argument("--repo", default=".")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    docx = Path(args.docx)
    crossframe = repo / "skills" / "crossframe"
    source_spine = crossframe / "references" / "v2-source-spine.md"
    digest_index = crossframe / "references" / "v2-section-digest-index.md"
    bundles = crossframe / "references" / "continuity-bundles.md"
    worksheet = crossframe / "worksheets" / "source-continuity-check.md"
    routing = crossframe / "references" / "read-routing-map.md"
    review = repo / "skills" / "crossframe-review" / "SKILL.md"
    suite = repo / "skills" / "crossframe-suite" / "SKILL.md"

    missing = [p for p in [docx, source_spine, digest_index, bundles, worksheet, routing, review, suite] if not p.exists()]
    if missing:
        for path in missing:
            print(f"missing: {path}")
        return 1

    headings = extract_docx_headings(docx)
    spine_text = source_spine.read_text(encoding="utf-8")
    digest_text = digest_index.read_text(encoding="utf-8")
    bundle_text = bundles.read_text(encoding="utf-8")
    routing_text = routing.read_text(encoding="utf-8")
    review_text = review.read_text(encoding="utf-8")
    suite_text = suite.read_text(encoding="utf-8")

    spine_ids = re.findall(r"`V2-H\d{3}`", spine_text)
    digest_ids = re.findall(r"`V2-H\d{3}`", digest_text)
    if len(set(spine_ids)) != len(headings):
        print(f"spine id count mismatch: docx={len(headings)} spine={len(set(spine_ids))}")
        return 1
    if len(set(digest_ids)) != len(headings):
        print(f"digest id count mismatch: docx={len(headings)} digest={len(set(digest_ids))}")
        return 1

    missing_titles = [title for title in headings if title not in spine_text]
    if missing_titles:
        print("missing titles in source spine:")
        for title in missing_titles[:20]:
            print(f"- {title}")
        return 1

    for bundle_id in REQUIRED_BUNDLES:
        if bundle_id not in bundle_text:
            print(f"bundle missing in continuity-bundles: {bundle_id}")
            return 1
        if bundle_id not in routing_text:
            print(f"bundle missing in read-routing-map: {bundle_id}")
            return 1

    adapter_text = routing_text + suite_text + review_text
    required_routes = [
        ("source-continuity-check.md", "integrity-check.md"),
        ("continuity-bundles.md",),
        ("v2-source-spine.md",),
    ]
    for alternatives in required_routes:
        if not any(required in adapter_text for required in alternatives):
            print(f"adapter route missing reference: {' or '.join(alternatives)}")
            return 1

    print("ok: v2.0 source continuity files match DOCX heading structure")
    print(f"headings: {len(headings)}")
    print(f"bundles: {len(REQUIRED_BUNDLES)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
