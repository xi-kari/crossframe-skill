from __future__ import annotations

import argparse
import sys
from pathlib import Path


REQUIRED_DOSSIER_HEADINGS = [
    "## max-worldview-capsule",
    "## max-continuation-ledger",
    "## max-source-frontier",
    "## max-transcendence-window",
    "## max-position-matrix",
    "## max-local-world-model",
    "## max-concept-graph",
    "## max-scale-map",
    "## 运行规律",
    "## 问题定位",
    "## max-path-tree",
    "## max-path-confidence-layers",
    "## max-red-team-pass",
    "## max-unexhaustible-declaration",
    "## 处理问题",
    "## 证据与台账",
    "## 反例与撤回条件",
    "## max-essay 准备",
    "## max-output-layers",
    "## max-continuation-index",
]

REQUIRED_DOSSIER_MARKERS = [
    "source_anchor",
    "claim_id",
    "claim ledger",
    "source ledger",
    "max-output-layers",
    "max-continuation-index",
]

REQUIRED_ESSAY_MARKERS = [
    "路径置信分层",
    "主体位置矩阵",
    "反向推演",
    "不可判断区",
    "续写索引",
    "max-continuation-index",
]

REQUIRED_LEDGER_MARKERS = [
    "max-run-state",
    "已读材料",
    "已展开路径",
    "未展开路径",
    "已撤回判断",
    "下一轮续写入口",
    "防重复",
    "防漂移",
]

REQUIRED_INDEX_MARKERS = [
    "下一轮续写入口",
    "未展开路径",
    "未展开主体位置",
    "未穷尽资料队列",
    "未展开反例",
    "不得重复内容",
    "不得越界内容",
]

DEFAULT_FILENAMES = {
    "dossier": "max-dossier.md",
    "essay": "max-essay.md",
    "ledger": "max-continuation-ledger.md",
    "index": "max-continuation-index.md",
}


def read_text(path: Path, errors: list[str]) -> str:
    if not path.exists():
        errors.append(f"missing file: {path}")
        return ""
    if not path.is_file():
        errors.append(f"not a file: {path}")
        return ""
    return path.read_text(encoding="utf-8")


def check_markers(text: str, markers: list[str], label: str, errors: list[str]) -> None:
    for marker in markers:
        if marker not in text:
            errors.append(f"{label}: missing marker: {marker}")


def check_ordered_headings(text: str, headings: list[str], label: str, errors: list[str]) -> None:
    previous = -1
    lines = text.splitlines()
    for heading in headings:
        current = -1
        for idx, line in enumerate(lines):
            if line.startswith(heading):
                current = idx
                break
        if current == -1:
            errors.append(f"{label}: missing heading: {heading}")
            continue
        if current < previous:
            errors.append(f"{label}: heading out of order: {heading}")
        previous = current


def check_no_template_truncation(text: str, errors: list[str]) -> None:
    if "## max-unexhaustible-declaration" in text and "## 证据与台账" not in text:
        errors.append(
            "max-dossier.md: template-fidelity gate failed: template appears truncated after max-unexhaustible-declaration"
        )
    if "CL1" in text and ("source_anchor" not in text or "claim ledger" not in text):
        errors.append(
            "max-dossier.md: CL-style claim ids require source_anchor, claim_id, source ledger, and claim ledger"
        )


def check_crossframe_max_artifacts(workspace: Path) -> list[str]:
    """Validate generated crossframe-max artifacts against the template-fidelity gate."""
    errors: list[str] = []
    dossier = read_text(workspace / DEFAULT_FILENAMES["dossier"], errors)
    essay = read_text(workspace / DEFAULT_FILENAMES["essay"], errors)
    ledger = read_text(workspace / DEFAULT_FILENAMES["ledger"], errors)
    index = read_text(workspace / DEFAULT_FILENAMES["index"], errors)

    if dossier:
        check_ordered_headings(dossier, REQUIRED_DOSSIER_HEADINGS, "max-dossier.md", errors)
        check_markers(dossier, REQUIRED_DOSSIER_MARKERS, "max-dossier.md", errors)
        check_no_template_truncation(dossier, errors)
    if essay:
        check_markers(essay, REQUIRED_ESSAY_MARKERS, "max-essay.md", errors)
    if ledger:
        check_markers(ledger, REQUIRED_LEDGER_MARKERS, "max-continuation-ledger.md", errors)
    if index:
        check_markers(index, REQUIRED_INDEX_MARKERS, "max-continuation-index.md", errors)

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="check_crossframe_max_artifacts: validate generated crossframe-max files against the template-fidelity gate."
    )
    parser.add_argument("--workspace", default=".", help="Directory containing max-dossier.md and related artifacts.")
    args = parser.parse_args()

    workspace = Path(args.workspace).resolve()
    errors = check_crossframe_max_artifacts(workspace)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print(f"ok: crossframe max artifacts passed template-fidelity gate -> {workspace}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
