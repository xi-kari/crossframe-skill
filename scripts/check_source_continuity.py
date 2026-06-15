from __future__ import annotations

import argparse
import importlib.util
import re
import sys
from pathlib import Path


V5_DOCX = r"E:\世界模型\跨尺度结构诊断框架v5.0.docx"


def load_generator(script_dir: Path):
    module_path = script_dir / "generate_source_continuity.py"
    spec = importlib.util.spec_from_file_location("generate_source_continuity", module_path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"cannot load generator: {module_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def expand_required_closure(start: str, required_with: dict[str, tuple[str, ...]]) -> set[str]:
    """Return the recursive must-read closure without recursing forever on mutual dependencies."""
    closure: set[str] = set()
    visiting: set[str] = set()

    def visit(bundle_id: str) -> None:
        if bundle_id in visiting:
            return
        visiting.add(bundle_id)
        for required_id in required_with.get(bundle_id, ()):
            if required_id not in closure:
                closure.add(required_id)
                visit(required_id)
            else:
                visit(required_id)
        visiting.remove(bundle_id)

    visit(start)
    closure.discard(start)
    return closure


def active_markdown_files(repo: Path) -> list[Path]:
    files: list[Path] = []
    for root in [repo / "skills"]:
        for path in root.rglob("*.md"):
            rel = path.relative_to(repo).as_posix()
            if "/references/v2-" in rel or "/references/v3-" in rel:
                continue
            if "/references/crossframe-v2-core.md" in rel:
                continue
            files.append(path)
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description="Check CrossFrame v5 source continuity files.")
    parser.add_argument("--version", default="v5")
    parser.add_argument("--source-docx", default=V5_DOCX)
    parser.add_argument("--repo", default=".")
    args = parser.parse_args()

    version = args.version.lower()
    require(version == "v5", "this checker is versioned for v5; pass --version v5")
    repo = Path(args.repo).resolve()
    source_docx = Path(args.source_docx)
    require(source_docx.exists(), f"missing source docx: {source_docx}")

    generator = load_generator(Path(__file__).resolve().parent)
    bundle_ids = [bundle.id for bundle in generator.V5_BUNDLES]
    bundle_id_set = set(bundle_ids)
    for bundle_id, required_ids in generator.REQUIRED_WITH.items():
        require(bundle_id in bundle_id_set, f"unknown required-with source bundle: {bundle_id}")
        require(bundle_id not in required_ids, f"self dependency in required-with graph: {bundle_id}")
        for required_id in required_ids:
            require(required_id in bundle_id_set, f"unknown required-with target bundle: {bundle_id} -> {required_id}")
    recursive_closures = {
        bundle_id: expand_required_closure(bundle_id, generator.REQUIRED_WITH)
        for bundle_id in bundle_ids
    }
    nodes, tables = generator.extract_nodes(source_docx)

    crossframe = repo / "skills" / "crossframe"
    refs = crossframe / "references"
    templates = crossframe / "templates"
    worksheets = crossframe / "worksheets"
    required = [
        refs / "v5-source-spine.md",
        refs / "v5-section-digest-index.md",
        refs / "v5-coverage-map.md",
        refs / "v5-term-fidelity.md",
        refs / "v5-material-selection-map.md",
        refs / "continuity-bundles.md",
        refs / "read-routing-map.md",
        templates / "read-state-capsule.md",
        worksheets / "source-continuity-check.md",
        worksheets / "source-anchor-integrity-check.md",
        worksheets / "seven-gates-worksheet.md",
    ]
    required.extend(refs / "continuity-bundles" / "v5" / f"{bundle_id}.md" for bundle_id in bundle_ids)
    missing = [path for path in required if not path.exists()]
    require(not missing, "missing required files:\n" + "\n".join(str(path) for path in missing))

    spine = read(refs / "v5-source-spine.md")
    digest = read(refs / "v5-section-digest-index.md")
    coverage = read(refs / "v5-coverage-map.md")
    terms = read(refs / "v5-term-fidelity.md")
    material_map = read(refs / "v5-material-selection-map.md")
    bundles = read(refs / "continuity-bundles.md")
    routing = read(refs / "read-routing-map.md")
    read_state_capsule = read(templates / "read-state-capsule.md")
    worksheet = read(worksheets / "source-continuity-check.md")
    anchor_integrity = read(worksheets / "source-anchor-integrity-check.md")
    seven_gates = read(worksheets / "seven-gates-worksheet.md")

    spine_ids = set(re.findall(r"`V5-H\d{3}`", spine))
    digest_ids = set(re.findall(r"`V5-H\d{3}`", digest))
    require(len(spine_ids) == len(nodes), f"spine id count mismatch: docx={len(nodes)} spine={len(spine_ids)}")
    require(len(digest_ids) == len(nodes), f"digest id count mismatch: docx={len(nodes)} digest={len(digest_ids)}")
    require(f"表格数量：{len(tables)}" in spine, "source spine table count mismatch")

    combined = "\n".join([spine, digest, coverage, terms, material_map, bundles, routing, read_state_capsule, worksheet, anchor_integrity, seven_gates])
    for bundle_id in bundle_ids:
        bundle_file = refs / "continuity-bundles" / "v5" / f"{bundle_id}.md"
        text = read(bundle_file)
        require(bundle_id in bundles, f"bundle missing in continuity-bundles.md: {bundle_id}")
        require(bundle_id in routing, f"bundle missing in read-routing-map.md: {bundle_id}")
        require(bundle_id in combined, f"bundle missing in v5 source materials: {bundle_id}")
        for heading in [
            "## 源锚点",
            "## 必须连读原因",
            "## 触发场景",
            "## 必须同读材料",
            "## 必须同读包（硬约束）",
            "## 必须同读闭包（递归展开）",
            "## 硬失败",
            "## 降档规则",
            "## 相邻候选包（非硬约束）",
            "## 输出影响",
            "## 输出自检",
        ]:
            require(heading in text, f"bundle file missing heading {heading}: {bundle_id}")
        for required_id in generator.REQUIRED_WITH.get(bundle_id, ()):
            require(required_id in text, f"bundle file missing required dependency: {bundle_id} -> {required_id}")
        for closure_id in recursive_closures[bundle_id]:
            require(closure_id in text, f"bundle file missing recursive closure dependency: {bundle_id} -> {closure_id}")

    for needle in [
        "v5-source-spine.md",
        "v5-section-digest-index.md",
        "v5-coverage-map.md",
        "v5-term-fidelity.md",
        "v5-material-selection-map.md",
        "continuity-bundles/v5",
        "必须同读闭包",
        "必须同读包",
        "v5-read-state-capsule",
        "v5_source_modules",
        "v5_continuity_bundles",
        "required_closure",
        "adjacent_candidates",
        "source_grounding",
        "downstream_read_policy",
        "闭包是否读完",
        "源锚点",
        "本文推断",
        "表达转译",
        "外部思想映射",
    ]:
        require(needle in combined, f"v5 material reference missing: {needle}")

    for needle in [
        "七闸",
        "强判断八件套",
        "低权力主体保护",
        "证据降级",
        "行动上限",
        "过程性产物不得充当现实证明",
        "局部状态坐标",
    ]:
        require(needle in combined, f"v5 key term missing: {needle}")

    stale_hits: list[str] = []
    for path in active_markdown_files(repo):
        text = read(path)
        for needle in ["当前权威源为 `v3.0`", "full-visible-v3-longform"]:
            if needle in text:
                stale_hits.append(f"{path.relative_to(repo)}: {needle}")
    require(not stale_hits, "stale active v3 authority markers:\n" + "\n".join(stale_hits))

    for skill_id in ["crossframe", "crossframe-suite", "crossframe-essay", "crossframe-review"]:
        skill_path = repo / "skills" / skill_id / "SKILL.md"
        require(skill_path.exists(), f"missing skill entry: {skill_id}")
        text = read(skill_path)
        require("v5.0" in text or "v5" in text, f"skill not updated to v5: {skill_id}")

    print("ok: v5 source continuity files match DOCX heading structure")
    print(f"headings: {len(nodes)}")
    print(f"tables: {len(tables)}")
    print(f"v5 bundles: {len(bundle_ids)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
