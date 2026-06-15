from __future__ import annotations

import argparse
import sys
from pathlib import Path


CURRENT_CROSSFRAME_SKILLS = [
    "crossframe",
    "crossframe-casebook",
    "crossframe-critical",
    "crossframe-debate",
    "crossframe-dialogue",
    "crossframe-essay",
    "crossframe-notebook",
    "crossframe-org",
    "crossframe-public",
    "crossframe-review",
    "crossframe-suite",
    "crossframe-teach",
]

TECHNIQUE_FIELDS = [
    "原书操作要点（转述）",
    "段落动作",
    "CrossFrame 适配",
    "原书页码/OCR锚点",
    "好句类型",
    "段落前后关系",
    "文章类型微用法",
    "失败示例（转述）",
    "文章类型用法",
    "失败形态",
    "输出自检",
]

SOURCE_LEDGER_FIELDS = [
    "来源",
    "时间",
    "来源类型",
    "支持的命题",
    "不能证明什么",
    "证据档位",
    "使用位置",
    "降档理由",
    "仍需补证处",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def skill_root_from_arg(value: str) -> Path:
    path = Path(value).resolve()
    if (path / "skills").is_dir():
        return path / "skills"
    return path


def check_no_retired_dirs(root: Path, label: str) -> None:
    retired = []
    for path in root.glob("crossframe-v5*"):
        if path.is_dir():
            retired.append(path.name)
    if (root / "crossframe-v3.1").exists():
        retired.append("crossframe-v3.1")
    require(not retired, f"{label}: retired active skill dirs still exist: {', '.join(sorted(retired))}")


def check_required_skill_dirs(root: Path, label: str) -> None:
    missing = [skill for skill in CURRENT_CROSSFRAME_SKILLS if not (root / skill / "SKILL.md").exists()]
    require(not missing, f"{label}: missing current crossframe skills: {', '.join(missing)}")


def check_source_ledger(root: Path, label: str) -> None:
    ledger = root / "crossframe" / "references" / "source-ledger-workflow.md"
    require(ledger.exists(), f"{label}: missing source-ledger-workflow.md")
    text = read(ledger)
    for field in SOURCE_LEDGER_FIELDS:
        require(field in text, f"{label}: source ledger missing field: {field}")
    for needle in ["九字段硬校验", "时间", "使用位置", "单一来源族", "降档", "不得判定为来源完整"]:
        require(needle in text, f"{label}: source ledger missing hardening marker: {needle}")
    for rel in [
        "crossframe-essay/SKILL.md",
        "crossframe-essay/protocols/essay-protocol.md",
        "crossframe-public/SKILL.md",
        "crossframe-public/protocols/public-issue-protocol.md",
        "crossframe-critical/SKILL.md",
        "crossframe-critical/protocols/critical-article-protocol.md",
        "crossframe-review/SKILL.md",
        "crossframe-review/protocols/review-protocol.md",
        "crossframe-review/protocols/article-review-protocol.md",
    ]:
        path = root / rel
        require(path.exists(), f"{label}: missing file for source ledger reference: {rel}")
        require("source-ledger-workflow.md" in read(path), f"{label}: {rel} does not reference source ledger workflow")


def check_techniques(root: Path, label: str) -> None:
    tech_dir = root / "crossframe-essay" / "references" / "writing-techniques"
    require(tech_dir.is_dir(), f"{label}: missing writing-techniques directory")
    cards = sorted(path for path in tech_dir.glob("*.md") if path.name != "index.md")
    require(len(cards) == 50, f"{label}: expected 50 writing technique cards, found {len(cards)}")
    for card in cards:
        text = read(card)
        for field in TECHNIQUE_FIELDS:
            require(f"- {field}：" in text, f"{label}: {card.name} missing technique field: {field}")

    routing = root / "crossframe-essay" / "references" / "article-technique-routing-map.md"
    require(routing.exists(), f"{label}: missing article-technique-routing-map.md")
    routing_text = read(routing)
    for needle in ["好句类型", "段落前后关系", "文章类型微用法", "失败示例（转述）", "不得超过 5 个", "技法落地证据表", "正文对应短摘/段落编号"]:
        require(needle in routing_text, f"{label}: technique routing missing refinement marker: {needle}")


def check_evals(root: Path, label: str) -> None:
    critical_eval = root / "crossframe-critical" / "evals" / "crossframe-critical-smoke-tests.md"
    require(critical_eval.exists(), f"{label}: missing crossframe-critical smoke tests")
    critical_text = read(critical_eval)
    for needle in ["v5-read-state-capsule", "源锚点", "来源台账", "撤回条件", "review 不得吞正文"]:
        require(needle in critical_text, f"{label}: critical eval missing marker: {needle}")

    for skill in ["crossframe-suite", "crossframe-essay", "crossframe-review", "crossframe-public", "crossframe-org", "crossframe-debate", "crossframe-critical"]:
        eval_dir = root / skill / "evals"
        require(eval_dir.is_dir(), f"{label}: missing eval directory for {skill}")
        require(any(eval_dir.glob("*.md")), f"{label}: empty eval directory for {skill}")

    review_failure = read(root / "crossframe-review" / "references" / "failure-taxonomy.md")
    for needle in ["选择器压缩失败", "技法越界失败", "来源用途越界失败", "来源台账缺失", "来源台账字段伪完整", "技法落地不可审计", "结构通过误作发布通过"]:
        require(needle in review_failure, f"{label}: review failure taxonomy missing: {needle}")

    review_eval = read(root / "crossframe-review" / "evals" / "crossframe-review-smoke-tests.md")
    for needle in ["来源台账字段伪完整", "单一来源族", "技法落地不可审计", "胶囊闭包自证失败", "结构通过误作发布通过"]:
        require(needle in review_eval, f"{label}: review eval missing hardening case: {needle}")


def check_quality_gate_hardening(root: Path, label: str) -> None:
    runtime_policy_path = root / "crossframe" / "references" / "runtime-read-policy.md"
    closure_map_path = root / "crossframe" / "references" / "continuity-closure-map.md"
    require(runtime_policy_path.exists(), f"{label}: missing runtime-read-policy.md")
    require(closure_map_path.exists(), f"{label}: missing continuity-closure-map.md")

    runtime_policy = read(runtime_policy_path)
    for needle in ["默认不读", "evals/", "examples/", "不全量打开", "v5-source-spine.md", "v5-section-digest-index.md"]:
        require(needle in runtime_policy, f"{label}: runtime read policy missing marker: {needle}")

    closure_map = read(closure_map_path)
    for needle in ["v5-use-boundary-governance-pack", "v5-domain-translation-normative-source-pack", "v5-toolization-accessibility-release-pack", "运行时轻量闭包图"]:
        require(needle in closure_map, f"{label}: continuity closure map missing marker: {needle}")

    capsule = read(root / "crossframe" / "templates" / "read-state-capsule.md")
    for needle in ["post_body_risk_sweep", "入口包 -> 直接闭包", "V5-H 锚点", "锚点缺失"]:
        require(needle in capsule, f"{label}: read-state capsule missing hardening marker: {needle}")

    anchor = read(root / "crossframe" / "worksheets" / "source-anchor-integrity-check.md")
    for needle in ["正文高风险概念回扫", "仅写一行", "source modules 是否有", "正文短摘"]:
        require(needle in anchor, f"{label}: source anchor check missing hardening marker: {needle}")

    review_protocol = read(root / "crossframe-review" / "protocols" / "review-protocol.md")
    for needle in ["反向否决最小块", "正文抽句回指", "structural_pass", "substantive_pass", "publish_boundary"]:
        require(needle in review_protocol, f"{label}: review protocol missing hardening marker: {needle}")

    review_rubric = read(root / "crossframe-review" / "references" / "review-rubric.md")
    for needle in ["等级上限", "structural_pass", "substantive_pass", "publish_boundary"]:
        require(needle in review_rubric, f"{label}: review rubric missing pass-boundary marker: {needle}")


def check_root(root: Path, label: str) -> None:
    require(root.is_dir(), f"{label}: skill root does not exist: {root}")
    check_no_retired_dirs(root, label)
    check_required_skill_dirs(root, label)
    check_source_ledger(root, label)
    check_techniques(root, label)
    check_evals(root, label)
    check_quality_gate_hardening(root, label)


def main() -> int:
    parser = argparse.ArgumentParser(description="Check CrossFrame skill integrity outside v5 source continuity.")
    parser.add_argument("--repo", default=".", help="Repository root or skill root.")
    parser.add_argument("--mirror", action="append", default=[], help="Additional skill root to validate.")
    args = parser.parse_args()

    roots: list[tuple[Path, str]] = [(skill_root_from_arg(args.repo), "repo")]
    for idx, mirror in enumerate(args.mirror, start=1):
        roots.append((skill_root_from_arg(mirror), f"mirror{idx}"))

    for root, label in roots:
        check_root(root, label)
        print(f"ok: {label} -> {root}")

    print("ok: crossframe skill integrity checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
