from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from build_v6_publication_bundle import BUNDLE_SOURCE_FILES, PROTOTYPE_AUDIT_FILES, SOURCE_FILES, sha256


REQUIRED_HEADINGS = [
    "# 跨尺度结构诊断框架 v6.0",
    "## 发布边界",
    "## 从 v5.0 到 v6.0",
    "## v6.0 不是什么",
    "## 半量化层的四项责任",
    "## 构念图谱",
    "## 七闸半量化",
    "## 证据台账",
    "## 校准锚点",
    "## 机制候选更新",
    "## 判断档位与行动上限",
    "## 反例、撤回与治理写回",
    "## 案例库验证与评分者一致性",
    "## 反误用红线",
    "## 工具原型",
    "## 发布前检查清单",
]

REQUIRED_REFERENCES = [
    "skills/crossframe/references/construct-map-v6.md",
    "skills/crossframe/worksheets/seven-gates-quant-rubric.md",
    "skills/crossframe/worksheets/evidence-ledger-v6.md",
    "skills/crossframe/worksheets/calibration-anchor-card.md",
    "skills/crossframe/worksheets/mechanism-update-rules.md",
    "skills/crossframe/worksheets/counterexample-register.md",
    "skills/crossframe-casebook/examples/v6-quant-trials/validation-summary.md",
    "scripts/validate_v6_quantification_schema_fixtures.py",
    "scripts/check_v6_casebook_trials.py",
]

TOOL_BOUNDARY = "本工具只帮助整理结构判断，不替代现实调查、专业判断、受影响位置反馈、外部复核和最终责任承担。分数只能触发降级、复核或补证，不能单独授权处置。"

FORBIDDEN_LANGUAGE = [
    "total_score",
    "overall_score",
    "average_score",
    "weighted_score",
    "final_score",
    "prediction_probability",
    "success_rate",
    "reliability_proved",
    "validated_framework",
    "casebook_coverage_proves",
    "经验验证",
    "实证验证",
    "可靠性证明",
    "安全证明",
    "安全性证明",
    "处置授权",
    "授权处置",
    "发布证明",
    "现实正确性证明",
    "总分系统",
    "预测模型",
    "认证系统",
    "处置依据",
    "证明框架正确",
    "一致性证明现实判断为真",
    "覆盖率证明外部有效性",
]

NEGATION_MARKERS = ["不得", "不能", "不是", "不作为", "禁止", "反误用", "不能证明", "不替代"]
MAX_NEGATION_DISTANCE = 24


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def add_error(errors: list[str], rel: str, message: str) -> None:
    errors.append(f"{rel}: {message}")


def line_bounds(text: str, idx: int) -> tuple[int, int]:
    line_start = text.rfind("\n", 0, idx) + 1
    line_end = text.find("\n", idx)
    if line_end == -1:
        line_end = len(text)
    return line_start, line_end


def is_negated_on_same_line(text: str, idx: int, marker: str) -> bool:
    line_start, line_end = line_bounds(text, idx)
    line = text[line_start:line_end]
    local_idx = idx - line_start
    prefix = line[:local_idx]
    for negation in NEGATION_MARKERS:
        negation_idx = prefix.rfind(negation)
        if negation_idx != -1 and local_idx - negation_idx <= MAX_NEGATION_DISTANCE:
            return True
    return False


def check_forbidden_language(rel: str, text: str, errors: list[str]) -> None:
    for marker in FORBIDDEN_LANGUAGE:
        start = 0
        while True:
            idx = text.find(marker, start)
            if idx == -1:
                break
            if not is_negated_on_same_line(text, idx, marker):
                line_no = text.count("\n", 0, idx) + 1
                add_error(errors, rel, f"forbidden unbounded language at line {line_no}: {marker}")
            start = idx + len(marker)


def check_tracked_sources(repo: Path, errors: list[str]) -> None:
    for rel in SOURCE_FILES:
        path = repo / rel
        if not path.exists():
            add_error(errors, rel, "missing v6 publication source")

    doc_rel = "docs/CROSSFRAME_V6.md"
    doc_path = repo / doc_rel
    if not doc_path.exists():
        return
    doc = read(doc_path)
    for heading in REQUIRED_HEADINGS:
        if heading not in doc:
            add_error(errors, doc_rel, f"missing heading: {heading}")
    for ref in REQUIRED_REFERENCES:
        if ref not in doc:
            add_error(errors, doc_rel, f"missing source reference: {ref}")
    if TOOL_BOUNDARY not in doc:
        add_error(errors, doc_rel, "missing exact tool boundary sentence")

    for rel in [
        "docs/CROSSFRAME_V6.md",
        "docs/V5_TO_V6_CHANGES.md",
        "docs/V6_TOOL_PROTOTYPE.md",
        "skills/crossframe/references/judgment-action-matrix-v6.md",
        "skills/crossframe/references/falsification-governance-v6.md",
    ]:
        path = repo / rel
        if path.exists():
            check_forbidden_language(rel, read(path), errors)


def build_default_bundle(repo: Path) -> Path:
    stamp = "check"
    subprocess.run(
        [
            sys.executable,
            str(repo / "scripts" / "build_v6_publication_bundle.py"),
            "--repo",
            str(repo),
            "--stamp",
            stamp,
        ],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return repo / "outputs" / f"crossframe-v6.0-publication-{stamp}.md"


def check_bundle(repo: Path, bundle_path: Path, errors: list[str]) -> None:
    if not bundle_path.exists():
        add_error(errors, str(bundle_path), "missing generated publication bundle")
        return
    text = read(bundle_path)
    if TOOL_BOUNDARY not in text:
        add_error(errors, str(bundle_path), "bundle missing exact tool boundary sentence")
    for rel in BUNDLE_SOURCE_FILES:
        if f"## Source: `{rel}`" not in text:
            add_error(errors, str(bundle_path), f"bundle missing source section: {rel}")
    for rel in PROTOTYPE_AUDIT_FILES:
        if f"## Source: `{rel}`" in text:
            add_error(errors, str(bundle_path), f"bundle should manifest but not inline audit-only source: {rel}")
    check_forbidden_language(str(bundle_path), text, errors)

    manifest_path = bundle_path.with_suffix(".manifest.json")
    if not manifest_path.exists():
        add_error(errors, str(manifest_path), "missing generated publication manifest")
        return

    manifest = json.loads(read(manifest_path))
    sources = manifest.get("sources", [])
    if len(sources) != len(SOURCE_FILES):
        add_error(errors, str(manifest_path), f"manifest source count mismatch: {len(sources)}")
    by_path = {item.get("path"): item for item in sources if isinstance(item, dict)}
    for rel in SOURCE_FILES:
        item = by_path.get(rel)
        if not item:
            add_error(errors, str(manifest_path), f"manifest missing source: {rel}")
            continue
        expected_in_bundle = rel in BUNDLE_SOURCE_FILES
        if item.get("included_in_bundle") is not expected_in_bundle:
            add_error(errors, str(manifest_path), f"manifest included_in_bundle mismatch: {rel}")
        current = sha256(repo / rel)
        if item.get("sha256") != current:
            add_error(errors, str(manifest_path), f"manifest hash mismatch: {rel}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Check CrossFrame v6 publication source and generated bundle.")
    parser.add_argument("--repo", default=".", help="Repository root.")
    parser.add_argument("--bundle", default=None, help="Optional generated bundle path.")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    errors: list[str] = []
    check_tracked_sources(repo, errors)

    bundle_path = Path(args.bundle).resolve() if args.bundle else build_default_bundle(repo)
    check_bundle(repo, bundle_path, errors)

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1
    print("ok: v6 publication bundle checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
