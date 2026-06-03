from __future__ import annotations

import argparse
import re
from pathlib import Path

from docx import Document


SKILL_IDS = [
    "crossframe-suite",
    "crossframe",
    "crossframe-essay",
    "crossframe-review",
    "crossframe-dialogue",
    "crossframe-casebook",
    "crossframe-public",
    "crossframe-org",
    "crossframe-teach",
    "crossframe-debate",
    "crossframe-notebook",
]

REQUIRED_V3_BUNDLES = [
    "v3-framework-governance-falsification-pack",
    "v3-procedural-judgment-pack",
    "v3-evidence-visibility-pack",
    "v3-power-capture-malicious-compliance-pack",
    "v3-no-institution-middle-path-pack",
    "v3-trapped-trauma-baseline-pack",
    "v3-love-generative-action-pack",
    "v3-concept-migration-metaphor-pack",
    "v3-toolization-accessibility-pack",
    "v3-observation-entropy-contraction-pack",
]

PATCH_KEY_TERMS = [
    "框架自诊",
    "共识程序",
    "根假设证伪",
    "案例库",
    "前概念闸",
    "概念有效性",
    "可见性偏误",
    "不透明",
    "恶意合规",
    "AI 诊断",
    "弱信号保护",
    "无制度基础设施",
    "无法退出",
    "复杂创伤",
    "爱与开放性承担行动",
    "规范性前提",
    "隐喻漂移",
    "知识谱系",
    "使用门槛债",
    "工具化",
    "开放断言被权力捕获",
    "良性消亡",
]


def extract_docx_headings(path: Path) -> list[str]:
    doc = Document(str(path))
    headings: list[str] = []
    for para in doc.paragraphs:
        text = " ".join(para.text.split())
        if text and para.style.name.startswith("Heading"):
            headings.append(text)
    return headings


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> int:
    parser = argparse.ArgumentParser(description="Check CrossFrame source continuity files.")
    parser.add_argument("--version", default="v3")
    parser.add_argument("--source-docx", default=r"D:\下载\跨尺度结构诊断框架v3.0.docx")
    parser.add_argument("--previous-docx", default=r"D:\下载\跨尺度结构诊断框架v2.0.docx")
    parser.add_argument("--patch-docx", default=r"D:\下载\补丁稿.docx")
    parser.add_argument("--repo", default=".")
    args = parser.parse_args()

    version = args.version.lower()
    prefix = version.upper()
    repo = Path(args.repo).resolve()
    crossframe = repo / "skills" / "crossframe"
    source_docx = Path(args.source_docx)
    previous_docx = Path(args.previous_docx)
    patch_docx = Path(args.patch_docx)

    source_spine = crossframe / "references" / f"{version}-source-spine.md"
    digest_index = crossframe / "references" / f"{version}-section-digest-index.md"
    coverage_map = crossframe / "references" / f"{version}-coverage-map.md"
    term_fidelity = crossframe / "references" / f"{version}-term-fidelity.md"
    rationale = crossframe / "references" / "v3-change-rationale-from-patch.md"
    bundles = crossframe / "references" / "continuity-bundles.md"
    routing = crossframe / "references" / "read-routing-map.md"
    worksheet = crossframe / "worksheets" / "source-continuity-check.md"

    required_paths = [
        source_docx,
        patch_docx,
        source_spine,
        digest_index,
        coverage_map,
        term_fidelity,
        rationale,
        bundles,
        routing,
        worksheet,
    ]
    missing = [path for path in required_paths if not path.exists()]
    require(not missing, "missing required files:\n" + "\n".join(str(path) for path in missing))

    headings = extract_docx_headings(source_docx)
    spine_text = source_spine.read_text(encoding="utf-8")
    digest_text = digest_index.read_text(encoding="utf-8")
    coverage_text = coverage_map.read_text(encoding="utf-8")
    term_text = term_fidelity.read_text(encoding="utf-8")
    rationale_text = rationale.read_text(encoding="utf-8")
    bundle_text = bundles.read_text(encoding="utf-8")
    routing_text = routing.read_text(encoding="utf-8")
    worksheet_text = worksheet.read_text(encoding="utf-8")

    spine_ids = set(re.findall(rf"`{prefix}-H\d{{3}}`", spine_text))
    digest_ids = set(re.findall(rf"`{prefix}-H\d{{3}}`", digest_text))
    require(len(spine_ids) == len(headings), f"spine id count mismatch: docx={len(headings)} spine={len(spine_ids)}")
    require(len(digest_ids) == len(headings), f"digest id count mismatch: docx={len(headings)} digest={len(digest_ids)}")

    missing_titles = [title for title in headings if title not in spine_text]
    require(not missing_titles, "missing titles in source spine:\n" + "\n".join(missing_titles[:20]))

    if previous_docx.exists():
        previous_headings = extract_docx_headings(previous_docx)
        removed = [title for title in previous_headings if title not in headings]
        added = [title for title in headings if title not in previous_headings]
        require(not removed, "v3 is missing v2 headings:\n" + "\n".join(removed[:20]))
        require(len(added) >= 60, f"expected v3 additions from patch, got {len(added)}")

    for bundle_id in REQUIRED_V3_BUNDLES:
        require(bundle_id in bundle_text, f"bundle missing in continuity-bundles: {bundle_id}")
        require(bundle_id in routing_text, f"bundle missing in read-routing-map: {bundle_id}")
        require(bundle_id in source_spine.read_text(encoding="utf-8"), f"bundle missing in source spine: {bundle_id}")

    combined = "\n".join([spine_text, digest_text, coverage_text, term_text, rationale_text, bundle_text, routing_text])
    missing_terms = [term for term in PATCH_KEY_TERMS if term not in combined]
    require(not missing_terms, "patch terms not mapped:\n" + "\n".join(missing_terms))

    for needle in ["v3-source-spine.md", "v3-section-digest-index.md", "v3-term-fidelity.md", "continuity-bundles.md"]:
        require(needle in routing_text + worksheet_text, f"routing/worksheet missing reference: {needle}")

    for skill_id in SKILL_IDS:
        skill_path = repo / "skills" / skill_id / "SKILL.md"
        require(skill_path.exists(), f"missing skill entry: {skill_id}")
        text = skill_path.read_text(encoding="utf-8")
        require(text.startswith("---"), f"missing frontmatter: {skill_id}")
        if skill_id.startswith("crossframe"):
            require("CrossFrame" in text or "crossframe" in text, f"skill does not identify CrossFrame: {skill_id}")

    print(f"ok: {version}.0 source continuity files match DOCX heading structure")
    print(f"headings: {len(headings)}")
    if previous_docx.exists():
        previous_headings = extract_docx_headings(previous_docx)
        print(f"previous headings: {len(previous_headings)}")
        print(f"added headings: {len([title for title in headings if title not in previous_headings])}")
    print(f"v3 bundles: {len(REQUIRED_V3_BUNDLES)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
