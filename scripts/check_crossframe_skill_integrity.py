from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


CURRENT_CROSSFRAME_SKILLS = [
    "crossframe",
    "crossframe-casebook",
    "crossframe-critical",
    "crossframe-debate",
    "crossframe-dialogue",
    "crossframe-essay",
    "crossframe-history",
    "crossframe-inquiry",
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
    "source_id",
    "来源",
    "时间",
    "来源类型",
    "支持的 claim_id / 命题",
    "不能证明什么",
    "证据档位",
    "使用位置",
    "降档理由",
    "仍需补证处",
]

CLAIM_LEDGER_FIELDS = [
    "claim_id",
    "可见命题 / 正文短摘",
    "claim_type",
    "支持事实 / source_anchor",
    "机制候选",
    "概念契约",
    "来源台账",
    "judgment_grade",
    "action_ceiling",
    "撤回条件",
    "publish_boundary",
]

CLAIM_LEDGER_NORMALIZED_VALUES = [
    "light_observation",
    "open_assertion",
    "full_diagnosis",
    "strong_judgment",
    "low_condition_action",
    "exit_transfer",
    "internal_only",
    "publishable_with_boundary",
    "blocked",
]

CLAIM_LEDGER_DELTA_SKILLS = [
    "crossframe-casebook",
    "crossframe-critical",
    "crossframe-debate",
    "crossframe-dialogue",
    "crossframe-history",
    "crossframe-inquiry",
    "crossframe-notebook",
    "crossframe-org",
    "crossframe-public",
    "crossframe-teach",
]

SIBLING_CLAIM_BRIDGE_SKILLS = [
    "crossframe-casebook",
    "crossframe-critical",
    "crossframe-debate",
    "crossframe-dialogue",
    "crossframe-history",
    "crossframe-notebook",
    "crossframe-org",
    "crossframe-public",
    "crossframe-teach",
]

SIBLING_AGENT_PROMPT_SKILLS = [
    "crossframe-casebook",
    "crossframe-critical",
    "crossframe-debate",
    "crossframe-dialogue",
    "crossframe-history",
    "crossframe-notebook",
    "crossframe-org",
    "crossframe-public",
    "crossframe-review",
    "crossframe-teach",
]

CORE_RUNTIME_PROTOCOLS = [
    "anti-capture-protocol.md",
    "concept-explanation-protocol.md",
    "diagnosis-protocol.md",
    "expression-translation-protocol.md",
    "field-dissociation-protocol.md",
    "framework-boundary-protocol.md",
    "governance-continuity-protocol.md",
    "healing-transfer-protocol.md",
    "high-reflexivity-protocol.md",
    "inference-protocol.md",
    "intimate-relationship-protocol.md",
    "large-scale-stress-test-protocol.md",
    "lifecycle-diagnosis-protocol.md",
    "low-condition-action-protocol.md",
    "open-assertion-protocol.md",
    "progression-protocol.md",
    "proposition-verification-protocol.md",
    "public-institution-protocol.md",
]

CORE_OUTPUT_TEMPLATES = [
    "concept-explanation-output.md",
    "expression-translation-output.md",
    "field-dissociation-output.md",
    "framework-boundary-output.md",
    "full-diagnosis-output.md",
    "governance-continuity-output.md",
    "healing-transfer-output.md",
    "high-reflexivity-output.md",
    "inference-output.md",
    "intimate-relationship-output.md",
    "large-scale-stress-output.md",
    "lifecycle-output.md",
    "open-assertion-output.md",
    "progression-output.md",
    "public-institution-output.md",
    "quick-diagnosis-output.md",
    "strong-judgment-output.md",
    "user-facing-language.md",
]

SPECIFIC_CONCEPT_CONTRACTS = [
    "contract: power_closure",
    "contract: low_condition_action",
    "contract: love_open_action",
    "contract: reflexivity",
    "contract: toolization_accessibility",
    "contract: metaphor_source_transparency",
    "contract: exit_transfer",
    "contract: repair_byproduct",
]

RETIRED_RUNTIME_ARTIFACTS = [
    "crossframe/worksheets/five-gates-worksheet.md",
    "crossframe/references/crossframe-v2-core.md",
    "crossframe/references/v2-coverage-map.md",
    "crossframe/references/v2-section-digest-index.md",
    "crossframe/references/v2-source-spine.md",
    "crossframe/references/v2-term-fidelity.md",
    "crossframe/references/integrity-check.md",
]

RETIRED_RUNTIME_REFERENCES = [
    "five-gates-worksheet",
    "worksheets/five-gates",
    "五闸工作表",
    "crossframe-v2-core",
    "references/v2-",
    "v2-source",
    "v2-section",
    "v2-term",
    "v2-coverage",
    "references/integrity-check.md",
    "读取 integrity-check.md",
]

SOURCE_LEDGER_OLD_MARKERS = [
    "九字段",
    "九个字段",
    "来源、时间、来源类型、支持命题、不能证明什么、证据档位、使用位置、降档理由、仍需补证处",
    "支持的命题",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def joined_markdown(path: Path) -> str:
    if not path.is_dir():
        return ""
    return "\n".join(read(child) for child in sorted(path.glob("*.md")))


def iter_text_files(root: Path):
    suffixes = {".md", ".py", ".json", ".txt", ".ps1", ".sh", ".yaml", ".yml"}
    for skill in CURRENT_CROSSFRAME_SKILLS:
        skill_dir = root / skill
        if not skill_dir.is_dir():
            continue
        for path in skill_dir.rglob("*"):
            if path.is_file() and path.suffix.lower() in suffixes:
                yield path


def section_after(text: str, heading: str) -> str:
    start = text.find(heading)
    require(start >= 0, f"missing section heading: {heading}")
    end = text.find("\n---", start + len(heading))
    if end == -1:
        return text[start:]
    return text[start:end]


def skill_root_from_arg(value: str) -> Path:
    path = Path(value).resolve()
    if (path / "skills").is_dir():
        return path / "skills"
    return path


def repo_root_from_arg(value: str) -> Path:
    path = Path(value).resolve()
    if (path / "skills").is_dir():
        return path
    if path.name == "skills":
        return path.parent
    return path


def check_no_retired_dirs(root: Path, label: str) -> None:
    retired = []
    for path in root.glob("crossframe-v5*"):
        if path.is_dir():
            retired.append(path.name)
    require(not retired, f"{label}: retired active skill dirs still exist: {', '.join(sorted(retired))}")


def check_required_skill_dirs(root: Path, label: str) -> None:
    missing = [skill for skill in CURRENT_CROSSFRAME_SKILLS if not (root / skill / "SKILL.md").exists()]
    require(not missing, f"{label}: missing current crossframe skills: {', '.join(missing)}")


def check_repo_adapters(repo: Path, label: str) -> None:
    if not (repo / "skills").is_dir():
        return

    adapter_needles = {
        "AGENTS.md": ["crossframe-history", "crossframe-inquiry", "完成态后继续追问", "纯致谢"],
        "CLAUDE.md": [
            ".claude/skills/crossframe-inquiry/SKILL.md",
            ".claude/commands/crossframe-inquiry.md",
            "/crossframe-inquiry",
            "skills/crossframe-inquiry/SKILL.md",
            "纯致谢",
        ],
        "GEMINI.md": ["crossframe-history", "crossframe-inquiry", "完成后追问", "纯致谢"],
        "CONVENTIONS.md": ["crossframe-inquiry", "14 CrossFrame skills", "pure acknowledgments"],
        "INTERFACES.md": ["skills/crossframe-inquiry/SKILL.md", "14 个 CrossFrame skill", "纯致谢"],
        "llms.txt": ["History skill", "Inquiry skill", "crossframe-inquiry", "pure acknowledgments"],
        ".github/copilot-instructions.md": ["crossframe-history", "crossframe-inquiry", "完成后追问", "纯致谢"],
        ".cursor/rules/crossframe.mdc": ["crossframe-history", "crossframe-inquiry", "post-completion inquiry", "pure acknowledgment/thanks signal"],
        ".cursor/rules/crossframe-suite.mdc": ["crossframe-history", "crossframe-inquiry", "post-completion inquiry", "pure acknowledgment/thanks signal"],
        ".cursor/rules/crossframe-essay.mdc": ["skills/crossframe-essay/SKILL.md", "runtime-read-policy.md"],
        ".continue/rules/crossframe.md": ["history research", "crossframe-inquiry", "post-completion inquiry", "pure acknowledgment/thanks signal"],
        ".clinerules/crossframe.md": ["history research", "crossframe-inquiry", "post-completion inquiry", "pure acknowledgment/thanks signal"],
        ".roo/rules/crossframe.md": ["history research", "crossframe-inquiry", "post-completion inquiry", "pure acknowledgment/thanks signal"],
        ".windsurf/rules/crossframe.md": ["history research", "crossframe-inquiry", "post-completion inquiry", "pure acknowledgment/thanks signal"],
        "docs/ADAPTERS.md": ["crossframe-history", "crossframe-inquiry", "纯致谢"],
        "scripts/install-codex.ps1": ["skills/crossframe-history", "skills/crossframe-inquiry"],
        "scripts/install-codex.sh": ["skills/crossframe-history", "skills/crossframe-inquiry"],
    }
    runtime_ref_adapters = set(adapter_needles) - {"docs/ADAPTERS.md", "scripts/install-codex.ps1", "scripts/install-codex.sh"}
    retired_adapter_refs = [
        "skills/crossframe/references/integrity-check.md",
        "`integrity-check.md`",
    ]
    old_public_copy_markers = [
        "5.0 混合长文",
        "5.0混合长文",
        "complete visible 5.0 dossier",
    ]

    for rel, needles in adapter_needles.items():
        path = repo / rel
        require(path.exists(), f"{label}: missing adapter file: {rel}")
        text = read(path)
        for needle in needles:
            require(needle in text, f"{label}: adapter {rel} missing marker: {needle}")
        for retired in retired_adapter_refs:
            require(retired not in text, f"{label}: adapter {rel} references retired file: {retired}")
        for marker in old_public_copy_markers:
            require(marker not in text, f"{label}: adapter {rel} still has old public copy marker: {marker}")
        if rel in runtime_ref_adapters:
            for needle in [
                "runtime-read-policy.md",
                "continuity-closure-map.md",
            ]:
                require(needle in text, f"{label}: adapter {rel} missing runtime closure marker: {needle}")

    claude_command_dir = repo / ".claude" / "commands"
    require(claude_command_dir.is_dir(), f"{label}: missing Claude command directory")
    for command_file in sorted(claude_command_dir.glob("crossframe*.md")):
        command_text = read(command_file)
        for retired in retired_adapter_refs:
            require(retired not in command_text, f"{label}: Claude command {command_file.name} references retired file: {retired}")

    claude_text = read(repo / "CLAUDE.md")
    command_refs = sorted(set(re.findall(r"`(\.claude/commands/[^`]+\.md)`", claude_text)))
    require(command_refs, f"{label}: CLAUDE.md has no .claude command references")
    for ref in command_refs:
        require((repo / ref).exists(), f"{label}: CLAUDE.md references missing command: {ref}")

    inquiry_command = repo / ".claude" / "commands" / "crossframe-inquiry.md"
    require(inquiry_command.exists(), f"{label}: missing Claude command for crossframe-inquiry")
    inquiry_command_text = read(inquiry_command)
    for needle in ["# /crossframe-inquiry", "skills/crossframe-inquiry/SKILL.md", "post-completion follow-up layer"]:
        require(needle in inquiry_command_text, f"{label}: crossframe-inquiry command missing marker: {needle}")


def check_public_release_docs(repo: Path, label: str) -> None:
    if not (repo / "skills").is_dir():
        return

    website_files = {
        "site/index.html": [
            "CrossFrame Skill Suite",
            "给 AI 装上的中文结构思考系统",
            "让 AI 在回答前先交账",
            "这是项目介绍页",
            "普通 AI 的问题，不是不会说，而是太会说",
            "CrossFrame 让 AI 先做四件事",
            "source_id",
            "claim_id",
            "concept contract",
            "crossframe-inquiry",
            "https://xi-kari.github.io/crossframe-skill/assets/og-image.png",
            "twitter:image",
            "rel=\"canonical\"",
            "og:url",
            "选择一个安全模拟场景，看它怎么工作",
            "首页示例均为虚构或匿名结构样例",
            "匿名模拟示例",
            "示例说明",
            "Use Boundary",
            "什么时候适合用 CrossFrame？",
            "开始安装",
            "查看文档",
            "https://github.com/xi-kari/crossframe-skill#docs",
            "<noscript>",
            "noscript-note",
            "交互示例需要 JavaScript",
            "概念追问",
            "历史接口",
            "组织机制",
            "公共证据",
            "data-demo=\"philosophy\"",
            "data-install=\"codex\"",
            "aria-controls=\"demo-panel\"",
            "role=\"tabpanel\" id=\"demo-panel\"",
            "一键安装脚本覆盖 Windows PowerShell 与 macOS / Linux Bash",
            "到对应 skills 目录",
            "这个网页能直接运行 CrossFrame 吗？",
            "为什么首页示例都是虚构或匿名的？",
            "它会让 AI 变慢吗？",
            "CrossFrame Skill Suite · v5.1.5 · explicit-only",
        ],
        "site/styles.css": [
            "--bg: #f7f3ea",
            "--accent: #5b6ee1",
            ".hero-note",
            ".noscript-note",
            ".micro-flow",
            ".section-note",
            ".clean-list",
            ".safe-demo-badge",
            ".demo-disclaimer",
            ".install-note",
            "height: 240px",
            "grid-template-columns",
            "@media (max-width: 980px)",
        ],
        "site/app.js": [
            "const demos",
            "philosophy",
            "history",
            "org",
            "public",
            "inquiry",
            "一个问题什么时候不该被直接回答",
            "虚构城邦",
            "虚构团队",
            "虚构平台",
            "匿名结构分析",
            "const installs",
            ".\\\\scripts\\\\install-codex.ps1",
            "bash scripts/install-codex.sh",
            "setDemo",
            "setInstall",
        ],
        "site/assets/crossframe-mark.svg": ["CrossFrame mark"],
        "site/assets/flow.svg": ["CrossFrame quality chain", "concept contract"],
        "site/assets/og-image.svg": ["CrossFrame Skill Suite"],
        ".github/workflows/pages.yml": [
            "Deploy Website",
            "actions/upload-pages-artifact@v3",
            "path: site",
            "actions/deploy-pages@v4",
        ],
        ".github/workflows/verify.yml": [
            "Verify CrossFrame Repository",
            "pull_request:",
            "workflow_dispatch:",
            "actions/setup-python@v5",
            'python-version: "3.11"',
            "python scripts/check_crossframe_skill_integrity.py --repo .",
            "python scripts/check_source_continuity.py --materials-only --repo .",
            "python -m json.tool skills/crossframe/schemas/claim-ledger.schema.json > /dev/null",
            "python scripts/sync_skill_mirrors.py --check",
            "git diff --check",
        ],
    }
    for rel, needles in website_files.items():
        path = repo / rel
        require(path.exists(), f"{label}: missing website file: {rel}")
        text = read(path)
        for needle in needles:
            require(needle in text, f"{label}: website file {rel} missing marker: {needle}")

    require((repo / "site" / "assets" / "og-image.png").exists(), f"{label}: missing website file: site/assets/og-image.png")
    public_page_text = read(repo / "site" / "index.html") + "\n" + read(repo / "site" / "app.js")
    for retired_demo_marker in [
        "生命的第一因",
        "苏联",
        "一個平台的申诉入口",
        "一个平台的申诉入口是否等于治理有效",
        "为什么这个团队越复盘越失真",
    ]:
        require(retired_demo_marker not in public_page_text, f"{label}: public page still has sensitive landing demo marker: {retired_demo_marker}")

    required_docs = {
        "README.md": ["14 个显式触发", "source_id -> claim_id", "docs/QUICKSTART.md", "framework-CrossFrame_v5.1.5", "review_%E2%86%92_inquiry", "https://xi-kari.github.io/crossframe-skill/", "网页介绍", "install-codex.sh"],
        "CHANGELOG.md": ["v5.1.5", "v5.1.4", "v5.1.3", "site/", "GitHub Pages", "v5.0.2", "crossframe-history", "crossframe-inquiry", "source_id"],
        "docs/WHAT_IS_CROSSFRAME.md": ["CrossFrame 是一组给 AI 使用的中文结构思考 skills", "一个一分钟例子", "它不是什么", "最推荐怎么用", "crossframe-inquiry"],
        "docs/QUICKSTART.md": ["install-codex.ps1", "install-codex.sh", "--materials-only", "--source-docx"],
        "docs/CONCEPTS.md": ["Claim Ledger", "source_id", "Concept Contract"],
        "docs/WORKFLOWS.md": ["previous_context -> crossframe-inquiry", "claim ledger / claim-ledger-check", "纯致谢"],
        "docs/EXAMPLES.md": ["首页只使用安全模拟样例", "真实/高敏主题", "source_id", "claim_id", "evidence grade", "withdrawal condition", "publish_boundary", "历史草稿档", "crossframe-inquiry", "mini 输出示例"],
        "docs/ADAPTERS.md": ["sync_skill_mirrors.py", "install-codex.sh", "Codex", "Claude Code", "crossframe-history", "crossframe-inquiry", "纯致谢"],
        "docs/SAFETY_AND_LIMITS.md": ["默认不展示内部 reasoning", "工具调用参数"],
        "docs/FAQ.md": ["explicit-only", "--materials-only"],
    }
    for rel, needles in required_docs.items():
        path = repo / rel
        require(path.exists(), f"{label}: missing public doc: {rel}")
        text = read(path)
        for needle in needles:
            require(needle in text, f"{label}: public doc {rel} missing marker: {needle}")

    for rel in [
        "AGENTS.md",
        "CLAUDE.md",
        "GEMINI.md",
        "CONVENTIONS.md",
        "INTERFACES.md",
        "llms.txt",
        ".github/copilot-instructions.md",
        "skills/crossframe-suite/SKILL.md",
    ]:
        text = read(repo / rel)
        require("内部 reasoning" in text or "internal reasoning" in text, f"{label}: {rel} missing internal reasoning visibility boundary")
        require("工具调用参数" in text or "tool-call parameters" in text, f"{label}: {rel} missing tool-call visibility boundary")
        for marker in ["5.0 混合长文", "5.0混合长文", "complete visible 5.0 dossier"]:
            require(marker not in text, f"{label}: {rel} still has old public copy marker: {marker}")

    for rel in [
        "skills/crossframe-suite/references/workflow-routing-map.md",
        "skills/crossframe-suite/protocols/suite-dispatch-protocol.md",
        "skills/crossframe-suite/SKILL.md",
        "skills/crossframe-inquiry/SKILL.md",
        "skills/crossframe-inquiry/protocols/inquiry-protocol.md",
        "skills/crossframe-inquiry/evals/crossframe-inquiry-smoke-tests.md",
        "skills/crossframe-suite/evals/crossframe-suite-smoke-tests.md",
    ]:
        text = read(repo / rel)
        require("纯致谢" in text, f"{label}: {rel} missing pure acknowledgment inquiry exception")
        for marker in ["5.0 混合长文", "5.0混合长文", "complete visible 5.0 dossier"]:
            require(marker not in text, f"{label}: {rel} still has old public copy marker: {marker}")

    for rel in [
        "scripts/sync_skill_mirrors.py",
        "scripts/package_crossframe_skill.py",
    ]:
        require((repo / rel).exists(), f"{label}: missing release maintenance script: {rel}")

    package_script = read(repo / "scripts" / "package_crossframe_skill.py")
    require('"site"' in package_script, f"{label}: package script does not include site directory")
    require('default="v5.1.5"' in package_script, f"{label}: package script default version is not v5.1.5")

    require(not (repo / "scripts" / "check_v2_continuity.py").exists(), f"{label}: retired v2 checker still exists")
    require(not (repo / "scripts" / "generate_v2_continuity.py").exists(), f"{label}: retired v2 generator still exists")
    for rel in [
        "scripts/check_source_continuity.py",
        "scripts/generate_source_continuity.py",
    ]:
        text = read(repo / rel)
        require("E:\\世界模型" not in text, f"{label}: {rel} still contains private source-docx path")
        require("--source-docx" in text, f"{label}: {rel} missing explicit source-docx argument")


def check_source_ledger(root: Path, label: str) -> None:
    ledger = root / "crossframe" / "references" / "source-ledger-workflow.md"
    require(ledger.exists(), f"{label}: missing source-ledger-workflow.md")
    text = read(ledger)
    for field in SOURCE_LEDGER_FIELDS:
        require(field in text, f"{label}: source ledger missing field: {field}")
    for needle in ["十字段硬校验", "时间", "使用位置", "单一来源族", "降档", "不得判定为来源完整"]:
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


def check_claim_ledger(root: Path, label: str) -> None:
    template = root / "crossframe" / "templates" / "claim-ledger.md"
    worksheet = root / "crossframe" / "worksheets" / "claim-ledger-check.md"
    schema = root / "crossframe" / "schemas" / "claim-ledger.schema.json"
    contracts = root / "crossframe" / "references" / "concept-contracts" / "core-contracts.md"

    for path in [template, worksheet, schema, contracts]:
        require(path.exists(), f"{label}: missing claim-ledger hardening file: {path.relative_to(root)}")

    template_text = read(template)
    for field in CLAIM_LEDGER_FIELDS:
        require(field in template_text, f"{label}: claim ledger template missing field: {field}")
    for value in CLAIM_LEDGER_NORMALIZED_VALUES:
        require(value in template_text, f"{label}: claim ledger template missing normalized value: {value}")
    for needle in ["body_excerpt", "mapping_status", "same_strength", "unmapped", "claim_id` 必须为 `null`"]:
        require(needle in template_text, f"{label}: claim ledger template missing body mapping normalized marker: {needle}")

    worksheet_text = read(worksheet)
    for needle in ["正文抽句反查", "判断档位上限", "裸奔命题", "substantive_pass"]:
        require(needle in worksheet_text, f"{label}: claim ledger check missing marker: {needle}")

    contracts_text = read(contracts)
    for needle in [
        "contract: open_assertion",
        "contract: judgment_grades",
        "contract: evidence_cost",
        "contract: scale_transfer",
        "contract: responsibility_chain",
        "contract: generic_high_risk_concept",
        "contract: chengjie_huiliu",
        "allowed_when",
        "forbidden_when",
        "downgrade_if",
    ]:
        require(needle in contracts_text, f"{label}: concept contracts missing marker: {needle}")
    for contract in [
        "contract: open_assertion",
        "contract: judgment_grades",
        "contract: evidence_cost",
        "contract: scale_transfer",
        "contract: responsibility_chain",
        "contract: generic_high_risk_concept",
        "contract: chengjie_huiliu",
    ]:
        require("audit_questions:" in section_after(contracts_text, contract), f"{label}: {contract} missing audit_questions")

    routing_text = read(root / "crossframe" / "references" / "read-routing-map.md")
    require("contract: pending" not in routing_text, f"{label}: read-routing-map still has contract: pending")
    for needle in [
        "concept-contracts/core-contracts.md#contract-generic_high_risk_concept",
        "concept-contracts/core-contracts.md#contract-chengjie_huiliu",
        "承接、回流、反馈写回、解释劳动、单方吸收成本、修复没有改变条件",
    ]:
        require(needle in routing_text, f"{label}: read-routing-map missing claim/concept contract routing: {needle}")

    for rel in [
        "crossframe/SKILL.md",
        "crossframe/templates/read-state-capsule.md",
        "crossframe/worksheets/source-anchor-integrity-check.md",
        "crossframe-essay/SKILL.md",
        "crossframe-essay/templates/insight-dossier-template.md",
        "crossframe-essay/templates/essay-output-template.md",
        "crossframe-review/SKILL.md",
        "crossframe-review/protocols/review-protocol.md",
        "crossframe-review/templates/review-report.md",
        "crossframe-suite/SKILL.md",
        "crossframe-suite/protocols/suite-dispatch-protocol.md",
        "crossframe-suite/templates/suite-reasoning-outline.md",
        "crossframe/templates/reasoning-outline-output.md",
    ]:
        path = root / rel
        require(path.exists(), f"{label}: missing file for claim ledger reference: {rel}")
        text = read(path)
        require("claim" in text.lower() or "命题台账" in text, f"{label}: {rel} does not reference claim ledger")

    suite_skill = read(root / "crossframe-suite" / "SKILL.md")
    for needle in ["命题台账归属", "crossframe-review` 必须抽句回指 `claim_id`"]:
        require(needle in suite_skill, f"{label}: suite skill missing claim ledger routing marker: {needle}")
    for needle in ["- 读态胶囊：", "- 源锚点检查：", "- 命题台账："]:
        require(needle in suite_skill, f"{label}: suite skill output outline missing field: {needle}")

    suite_protocol = read(root / "crossframe-suite" / "protocols" / "suite-dispatch-protocol.md")
    for needle in ["命题台账层", "templates/claim-ledger.md", "worksheets/claim-ledger-check.md"]:
        require(needle in suite_protocol, f"{label}: suite protocol missing claim ledger layer: {needle}")

    suite_outline = read(root / "crossframe-suite" / "templates" / "suite-reasoning-outline.md")
    for needle in ["- 命题台账：", "正文和 review 必须回指 `claim_id`", "源锚点完整性检查 -> claim ledger -> 结构洞察底稿"]:
        require(needle in suite_outline, f"{label}: suite outline missing claim ledger marker: {needle}")
    for needle in ["胶囊、来源台账、命题台账、技法", "中心命题、命题台账、来源台账、胶囊锚点、概念契约"]:
        require(needle in suite_outline, f"{label}: suite outline pass definition missing claim ledger marker: {needle}")

    workflow_map = read(root / "crossframe-suite" / "references" / "workflow-routing-map.md")
    for needle in ["claim-ledger-check", "claim ledger", "voice_mode"]:
        require(needle in workflow_map, f"{label}: workflow routing map missing claim ledger / voice_mode marker: {needle}")
    require("editorial-base" not in workflow_map, f"{label}: workflow routing map still contains retired editorial-base voice marker")

    reasoning_outline = read(root / "crossframe" / "templates" / "reasoning-outline-output.md")
    for needle in ["- 命题台账：", "- 概念契约：", "关键 `claim_id`", "本次命题台账与概念契约状态是"]:
        require(needle in reasoning_outline, f"{label}: reasoning outline missing claim ledger/concept contract marker: {needle}")

    essay_protocol = read(root / "crossframe-essay" / "protocols" / "essay-protocol.md")
    for needle in ["先回指对应 `claim_id`", "internal_only / publishable_with_boundary / blocked"]:
        require(needle in essay_protocol, f"{label}: essay protocol missing claim_id/publish boundary marker: {needle}")

    anchor_check = read(root / "crossframe" / "worksheets" / "source-anchor-integrity-check.md")
    for needle in ["| 正文短摘 | 类型 | claim_id | 胶囊中是否已有锚点 | 概念契约状态 | 处理 |", "没有对应 `claim_id`", "claim_id` 无法回指"]:
        require(needle in anchor_check, f"{label}: source anchor integrity check missing claim_id sweep marker: {needle}")
    require("可见摘要七项" in anchor_check, f"{label}: source anchor integrity check still uses old six-item summary")

    insight_dossier = read(root / "crossframe-essay" / "templates" / "insight-dossier-template.md")
    for needle in ["claim_type", "judgment_grade", "action_ceiling", "low_condition_action", "exit_transfer", "publish_boundary"]:
        require(needle in insight_dossier, f"{label}: insight dossier claim ledger summary missing normalized field: {needle}")

    review_report = read(root / "crossframe-review" / "templates" / "review-report.md")
    for needle in ["命题台账候选", "有 claim_id / 无 claim_id / 强于台账", "历史史料台账候选"]:
        require(needle in review_report, f"{label}: review report missing claim ledger reverse check marker: {needle}")

    failure_taxonomy = read(root / "crossframe-review" / "references" / "failure-taxonomy.md")
    for needle in ["命题台账缺失", "正文裸奔命题", "claim_id", "不得判 `substantive_pass`"]:
        require(needle in failure_taxonomy, f"{label}: failure taxonomy missing claim ledger failure marker: {needle}")

    review_rubric = read(root / "crossframe-review" / "references" / "review-rubric.md")
    for needle in ["claim ledger", "claim_id", "不得判 `substantive_pass`"]:
        require(needle in review_rubric, f"{label}: review rubric missing claim ledger grade cap marker: {needle}")
    for needle in ["命题台账缺失、正文裸奔命题", "`structural_pass`：字段、顺序、读态胶囊、来源台账、命题台账", "`substantive_pass`：中心命题、`claim_id`、来源台账"]:
        require(needle in review_rubric, f"{label}: review rubric missing claim ledger pass/hard-fail marker: {needle}")

    for skill in CLAIM_LEDGER_DELTA_SKILLS:
        text = read(root / skill / "SKILL.md")
        require("claim ledger delta" in text, f"{label}: {skill} missing claim ledger delta rule")
        require("不得新增未登记判断" in text, f"{label}: {skill} missing no-unregistered-judgment rule")

    critical_text = read(root / "crossframe-critical" / "SKILL.md")
    for needle in ["批判矩阵", "点睛句只能绑定已有 `claim_id`", "没有 `claim_id` 的批判句不得进入正文"]:
        require(needle in critical_text, f"{label}: crossframe-critical missing stricter claim ledger article rule: {needle}")

    teach_text = read(root / "crossframe-teach" / "SKILL.md")
    require("undefined" not in teach_text, f"{label}: crossframe-teach contains undefined in SKILL.md")

    schema_obj = json.loads(read(schema))
    require(schema_obj.get("additionalProperties") is False, f"{label}: claim ledger schema root must set additionalProperties=false")
    claims = schema_obj["properties"]["claims"]
    require("minItems" not in claims, f"{label}: claim ledger schema claims minItems must be conditional on ledger_status")
    root_all_text = json.dumps(schema_obj.get("allOf", []), ensure_ascii=False)
    for needle in ["drafted", "minItems", "missing", "maxItems"]:
        require(needle in root_all_text, f"{label}: claim ledger schema missing ledger_status conditional marker: {needle}")
    claim_item = claims["items"]
    require(claim_item.get("additionalProperties") is False, f"{label}: claim ledger schema claim items must set additionalProperties=false")
    support = claim_item["properties"]["support"]
    require(support.get("minItems") == 1, f"{label}: claim ledger schema support must require minItems=1")
    require(support["items"].get("minLength") == 1, f"{label}: claim ledger schema support items must require minLength=1")
    require("allOf" in claim_item, f"{label}: claim ledger schema missing conditional requirements")
    require("body_mappings" in schema_obj["properties"], f"{label}: claim ledger schema missing body_mappings")
    body_item = schema_obj["properties"]["body_mappings"]["items"]
    body_claim = body_item["properties"]["claim_id"]
    body_claim_text = json.dumps(body_claim, ensure_ascii=False)
    require("null" in body_claim_text and "CL[0-9]+" in body_claim_text, f"{label}: body_mappings claim_id must allow null or CL id")
    body_all_text = json.dumps(body_item.get("allOf", []), ensure_ascii=False)
    for needle in ["unmapped", "null", "handling", "same_strength", "stronger_than_claim"]:
        require(needle in body_all_text, f"{label}: body_mappings missing mapping_status conditional marker: {needle}")
    stronger_requires_handling = False
    for branch in body_item.get("allOf", []):
        if_status = branch.get("if", {}).get("properties", {}).get("mapping_status", {})
        then_required = branch.get("then", {}).get("required", [])
        if if_status.get("const") == "stronger_than_claim" and "handling" in then_required:
            stronger_requires_handling = True
    require(stronger_requires_handling, f"{label}: body_mappings stronger_than_claim must require handling")


def check_history_adapter(root: Path, label: str) -> None:
    suite_dispatch = read(root / "crossframe-suite" / "protocols" / "suite-dispatch-protocol.md")
    for needle in [
        "`history`：历史研究",
        "历史研究、史料互读、历史制度、文明连续史、长时段比较或 archive/FOIA backlog：追加 `../../crossframe-history/SKILL.md`",
        "`public` / `org` / `debate` / `notebook` / `history`",
    ]:
        require(needle in suite_dispatch, f"{label}: suite dispatch missing history routing marker: {needle}")

    history_template = read(root / "crossframe-history" / "templates" / "history-interface-summary.md")
    for needle in ["source_id", "claim_id", "mechanism_id", "claim ledger delta", "历史机制候选"]:
        require(needle in history_template, f"{label}: history interface summary missing claim bridge marker: {needle}")

    history_source_protocol = read(root / "crossframe-history" / "protocols" / "history-source-ledger-protocol.md")
    for needle in ["source_id", "支持的 claim_id / 命题", "历史史料台账必须能回指 `claim ledger`"]:
        require(needle in history_source_protocol, f"{label}: history source ledger missing claim bridge marker: {needle}")

    review_report = read(root / "crossframe-review" / "templates" / "review-report.md")
    for needle in ["有具体史料与 source_id", "是否能回指 claim_id", "历史草稿档或材料背景"]:
        require(needle in review_report, f"{label}: review report missing history source-to-claim marker: {needle}")


def check_inquiry_layer(root: Path, label: str) -> None:
    inquiry_root = root / "crossframe-inquiry"
    required_files = [
        "SKILL.md",
        "agents/openai.yaml",
        "protocols/inquiry-protocol.md",
        "references/question-taxonomy.md",
        "references/inquiry-boundaries.md",
        "templates/inquiry-panel.md",
        "templates/inquiry-state.md",
        "templates/knowledge-retrieval-log.md",
        "templates/user-answer-digest.md",
        "templates/deeper-question-set.md",
        "evals/crossframe-inquiry-smoke-tests.md",
    ]
    for rel in required_files:
        require((inquiry_root / rel).exists(), f"{label}: missing crossframe-inquiry file: {rel}")

    skill_text = read(inquiry_root / "SKILL.md")
    for needle in [
        "name: crossframe-inquiry",
        "trigger: suite-only",
        "不独立响应",
        "claim ledger",
        "mechanism_candidates",
        "concept_contracts",
        "inquiry_state",
        "inquiry_claim_delta",
        "不得制造新中心命题",
        "不得诱导用户接受 CrossFrame 的原判断",
        "claim ledger delta",
        "不得新增未登记判断",
        "3-5 个主追问点，并可附加最多 2 个可选深挖问题",
        "post_completion_inquiry_armed",
        "完成态后续输入",
        "上一轮 `claim ledger`、机制候选、概念契约、结构洞察底稿、文章正文和 review 结果",
        "sibling_knowledge_retrieval",
        "知识库检索",
        "定向读取 sibling skill",
        "不得把检索材料直接写成新结论",
        "纯致谢",
    ]:
        require(needle in skill_text, f"{label}: crossframe-inquiry SKILL.md missing marker: {needle}")
    require("3-7 个追问点" not in skill_text, f"{label}: crossframe-inquiry SKILL.md still allows 3-7 inquiry points")

    protocol = read(inquiry_root / "protocols" / "inquiry-protocol.md")
    for needle in [
        "追问对象池",
        "理解型追问",
        "反证型追问",
        "补证型追问",
        "迁移型追问",
        "自我定位型追问",
        "行动边界型追问",
        "概念保真型追问",
        "用户回答后，先摘要",
        "inquiry_delta",
        "完成态后续输入接管",
        "任何实质后续用户输入",
        "纯致谢",
        "上一轮上下文回收",
        "Sibling skill 知识库检索",
        "retrieval_log",
        "只读必要协议、references、templates",
        "如果需要专项判断，回到 suite",
    ]:
        require(needle in protocol, f"{label}: inquiry protocol missing marker: {needle}")

    taxonomy = read(inquiry_root / "references" / "question-taxonomy.md")
    for needle in ["clarify_object", "seek_counterexample", "evidence_upgrade", "action_boundary", "transfer_conditions", "stop_condition"]:
        require(needle in taxonomy, f"{label}: inquiry question taxonomy missing marker: {needle}")

    boundaries = read(inquiry_root / "references" / "inquiry-boundaries.md")
    for needle in ["追问不是诊断升级", "追问不是心理审判", "追问不是行动催促", "追问不是无限循环", "发布边界", "检索不是授权"]:
        require(needle in boundaries, f"{label}: inquiry boundaries missing marker: {needle}")

    templates = joined_markdown(inquiry_root / "templates")
    for needle in [
        "# 结构追问",
        "追问对象",
        "用户回答摘要",
        "不应升级的地方",
        "深挖问题组",
        "claim_id",
        "mechanism_id",
        "q_id：Q1",
        "期待回答类型：",
        "风险边界：",
        "上游上下文索引",
        "post_completion_inquiry_armed",
        "知识库检索",
        "retrieval_log",
        "knowledge_sources",
    ]:
        require(needle in templates, f"{label}: inquiry templates missing marker: {needle}")

    agent = read(inquiry_root / "agents" / "openai.yaml")
    for needle in [
        "display_name: CrossFrame Inquiry",
        "short_description:",
        "default_prompt:",
        "claim ledger",
        "inquiry_delta",
        "post_completion_inquiry_armed",
        "sibling_knowledge_retrieval",
        "retrieval_log",
    ]:
        require(needle in agent, f"{label}: inquiry agent metadata missing marker: {needle}")

    evals = read(inquiry_root / "evals" / "crossframe-inquiry-smoke-tests.md")
    for needle in [
        "文章后追问",
        "用户反对结论",
        "行动边界",
        "概念保真",
        "用户只想收束",
        "不得直接再写一篇文章",
        "inquiry_delta",
        "完成态接管",
        "任何实质后续输入",
        "纯致谢",
        "知识库检索",
        "不得调用全部 sibling skill",
        "retrieval_log",
    ]:
        require(needle in evals, f"{label}: inquiry eval missing smoke marker: {needle}")

    suite_skill = read(root / "crossframe-suite" / "SKILL.md")
    for needle in [
        "后续实质输入默认进入 crossframe-inquiry 结构追问",
        "追问层归属",
        "追问例外",
        "不默认重新成文",
        "完成态追问接管",
        "post_completion_inquiry_armed",
        "纯致谢",
        "sibling 知识库检索",
        "- 追问层：不触发 / 触发；追问目标：",
    ]:
        require(needle in suite_skill, f"{label}: suite SKILL.md missing inquiry routing marker: {needle}")

    suite_protocol = read(root / "crossframe-suite" / "protocols" / "suite-dispatch-protocol.md")
    for needle in [
        "`inquiry`：诊断、文章或 review 完成后",
        "若主目标为 `inquiry` 且已有上游 CrossFrame 输出",
        "不进入默认 essay",
        "post_completion_inquiry_armed=true",
        "完整链路完成后的下一轮实质用户输入",
        "纯致谢",
        "允许 `crossframe-inquiry` 做定向 sibling 知识库检索",
        "继续追问、深思、反证、补证、迁移应用、用户反对结论或要求“问我几个问题”：追加 `../../crossframe-inquiry/SKILL.md`",
        "结构追问层：完成态后的实质后续输入默认启动 `crossframe-inquiry`",
    ]:
        require(needle in suite_protocol, f"{label}: suite dispatch missing inquiry marker: {needle}")

    workflow = read(root / "crossframe-suite" / "references" / "workflow-routing-map.md")
    for needle in [
        "继续追问我",
        "crossframe -> crossframe-review(lite) -> crossframe-inquiry",
        "crossframe-inquiry(counterexample)",
        "这个怎么用到另一个案例",
        "crossframe -> crossframe-review(lite) -> crossframe-inquiry(transfer_conditions)",
        "这个怎么用到我/我们公司/团队",
        "crossframe -> crossframe-org -> crossframe-review(lite) -> crossframe-inquiry(transfer_conditions)",
        "crossframe-inquiry(action_boundary) -> crossframe-review(lite)",
        "完整链路完成后的实质后续输入",
        "纯致谢",
        "post_completion_inquiry_armed",
    ]:
        require(needle in workflow, f"{label}: workflow routing map missing inquiry route: {needle}")

    suite_outline = read(root / "crossframe-suite" / "templates" / "suite-reasoning-outline.md")
    require("- 追问层：" in suite_outline, f"{label}: suite reasoning outline missing inquiry field")
    for needle in ["- 完成态追问接管：", "post_completion_inquiry_armed"]:
        require(needle in suite_outline, f"{label}: suite reasoning outline missing post-completion inquiry marker: {needle}")

    essay_template = read(root / "crossframe-essay" / "templates" / "essay-output-template.md")
    for needle in ["## 可选追问入口", "反驳本文中心命题", "不得在用户未选择时自动展开完整追问"]:
        require(needle in essay_template, f"{label}: essay output template missing inquiry entry marker: {needle}")

    review_template = read(root / "crossframe-review" / "templates" / "review-report.md")
    for needle in ["## 可进入追问层的问题", "| q_seed | 来源 | 为什么值得追问 |", "交给 `crossframe-inquiry`"]:
        require(needle in review_template, f"{label}: review report missing inquiry handoff marker: {needle}")

    suite_agent = read(root / "crossframe-suite" / "agents" / "openai.yaml")
    for needle in ["post_completion_inquiry_armed", "next substantive user message", "crossframe-inquiry", "Pure acknowledgments"]:
        require(needle in suite_agent, f"{label}: suite agent metadata missing post-completion inquiry marker: {needle}")


def check_suite_routes_all_siblings(root: Path, label: str) -> None:
    dispatch = read(root / "crossframe-suite" / "protocols" / "suite-dispatch-protocol.md")
    workflow = read(root / "crossframe-suite" / "references" / "workflow-routing-map.md")

    for needle in ["`history`：历史研究", "crossframe-history"]:
        require(needle in dispatch or needle in workflow, f"{label}: suite routing missing history marker: {needle}")

    for needle in ["`inquiry`：诊断、文章或 review 完成后", "crossframe-inquiry"]:
        require(needle in dispatch or needle in workflow, f"{label}: suite routing missing inquiry marker: {needle}")

    critical_skill = read(root / "crossframe-critical" / "SKILL.md")
    if "trigger: suite-only" in critical_skill:
        for needle in ["`critical`：结构批判文章", "crossframe-critical"]:
            require(needle in dispatch, f"{label}: crossframe-critical is suite-only but missing from suite dispatch: {needle}")
        require("crossframe-critical" in workflow, f"{label}: crossframe-critical is suite-only but missing from workflow map")


def check_sibling_claim_bridges(root: Path, label: str) -> None:
    for dirname in SIBLING_CLAIM_BRIDGE_SKILLS:
        skill_dir = root / dirname
        require((skill_dir / "SKILL.md").exists(), f"{label}: missing sibling skill: {dirname}")

        skill_text = read(skill_dir / "SKILL.md")
        require("claim ledger delta" in skill_text, f"{label}: {dirname} missing claim ledger delta rule in SKILL.md")
        require("不得新增未登记判断" in skill_text, f"{label}: {dirname} missing no-unregistered-judgment rule")

        templates = joined_markdown(skill_dir / "templates")
        require(
            "claim_id" in templates
            or "claim ledger" in templates
            or "micro claim" in templates
            or "命题台账" in templates,
            f"{label}: {dirname} templates missing claim bridge marker",
        )

        evals = joined_markdown(skill_dir / "evals")
        require(
            "claim_id" in evals or "claim ledger" in evals or "命题台账" in evals,
            f"{label}: {dirname} evals missing claim ledger regression",
        )

        protocols = joined_markdown(skill_dir / "protocols")
        require(
            "concept-contracts/core-contracts.md" in protocols,
            f"{label}: {dirname} protocols missing high-risk concept contract rule",
        )

    casebook_template = read(root / "crossframe-casebook" / "templates" / "casebook-entry-template.md")
    for needle in ["claim ledger delta", "机制候选登记", "mechanism_id", "concept_contract", "对应 claim_id"]:
        require(needle in casebook_template, f"{label}: casebook entry template missing claim bridge marker: {needle}")
    casebook_eval = read(root / "crossframe-casebook" / "evals" / "crossframe-casebook-smoke-tests.md")
    for needle in ["concept_contract", "claim_id", "标签候选"]:
        require(needle in casebook_eval, f"{label}: casebook eval missing concept/claim regression marker: {needle}")

    public_institution = read(root / "crossframe-public" / "templates" / "public-institution-diagnosis.md")
    for needle in ["公共 claim ledger delta", "source_id / 来源", "judgment_grade", "publish_boundary"]:
        require(needle in public_institution, f"{label}: public institution template missing claim marker: {needle}")
    public_comment = read(root / "crossframe-public" / "templates" / "public-comment-draft.md")
    for needle in ["中心命题 claim_id", "judgment_grade"]:
        require(needle in public_comment, f"{label}: public comment template missing claim marker: {needle}")
    public_source_rules = read(root / "crossframe-public" / "references" / "source-and-evidence-rules.md")
    for needle in ["source_id", "支持的 claim_id / 命题", "不能证明什么", "降档理由"]:
        require(needle in public_source_rules, f"{label}: public source rules missing source-to-claim marker: {needle}")

    org_protocol = read(root / "crossframe-org" / "protocols" / "org-diagnostic-protocol.md")
    for needle in ["判断档位使用主 schema", "light_observation", "组织诊断备忘录` 只是输出类型"]:
        require(needle in org_protocol, f"{label}: org protocol missing normalized judgment grade marker: {needle}")
    org_memo = read(root / "crossframe-org" / "templates" / "org-diagnostic-memo.md")
    for needle in ["- 命题台账：", "- 概念契约：", "组织 claim ledger delta", "withdrawal_condition"]:
        require(needle in org_memo, f"{label}: org diagnostic memo missing claim bridge marker: {needle}")
    for rel in ["feedback-writeback-plan.md", "low-risk-pilot-plan.md", "stop-condition-card.md"]:
        text = read(root / "crossframe-org" / "templates" / rel)
        require("本行动建议必须回指某个 `claim_id`" in text, f"{label}: org action template missing claim_id action rule: {rel}")

    dialogue_protocol = read(root / "crossframe-dialogue" / "protocols" / "dialogue-protocol.md")
    for needle in ["内部 micro claim 检查", "micro_claim", "没有 micro claim"]:
        require(needle in dialogue_protocol, f"{label}: dialogue protocol missing micro claim check: {needle}")
    dialogue_template = read(root / "crossframe-dialogue" / "templates" / "default-short-answer.md")
    require("核心判断、批评句、行动建议和停止条件各自有 micro claim" in dialogue_template, f"{label}: dialogue default template missing micro claim marker")

    debate_protocol = read(root / "crossframe-debate" / "protocols" / "debate-protocol.md")
    for needle in ["proposition_type", "judgment_grade", "light_observation"]:
        require(needle in debate_protocol, f"{label}: debate protocol missing proposition/judgment split: {needle}")
    debate_template = read(root / "crossframe-debate" / "templates" / "debate-analysis-output.md")
    for needle in ["proposition_id", "对应 claim_id", "debate claim bridge"]:
        require(needle in debate_template, f"{label}: debate template missing claim bridge marker: {needle}")

    notebook_template = read(root / "crossframe-notebook" / "templates" / "research-notebook.md")
    for needle in ["insight_id", "来源依据 / source_id", "是否影响概念契约", "对应 claim_id"]:
        require(needle in notebook_template, f"{label}: notebook template missing absorption claim marker: {needle}")
    notebook_protocol = read(root / "crossframe-notebook" / "protocols" / "bidirectional-reading-protocol.md")
    for needle in ["absorption_candidate", "claim ledger delta", "review"]:
        require(needle in notebook_protocol, f"{label}: notebook protocol missing absorption candidate gate: {needle}")

    teach_protocol = read(root / "crossframe-teach" / "protocols" / "teach-protocol.md")
    for needle in ["concept-contracts/core-contracts.md", "什么时候允许用", "什么时候禁止用", "什么时候必须降档"]:
        require(needle in teach_protocol, f"{label}: teach protocol missing concept contract teaching marker: {needle}")
    teach_template = read(root / "crossframe-teach" / "templates" / "concept-lesson.md")
    for needle in ["## 使用契约", "什么时候可以用", "什么时候不能用", "什么时候必须降档"]:
        require(needle in teach_template, f"{label}: teach template missing use contract marker: {needle}")

    critical_template = read(root / "crossframe-critical" / "templates" / "critical-output-template.md")
    for needle in ["批判 claim ledger delta", "concept_contract", "example_id", "支持 claim_id", "不能证明什么"]:
        require(needle in critical_template, f"{label}: critical template missing claim/example bridge: {needle}")
    critical_eval = read(root / "crossframe-critical" / "evals" / "crossframe-critical-smoke-tests.md")
    for needle in ["claim_id", "claim ledger", "点睛句"]:
        require(needle in critical_eval, f"{label}: critical eval missing claim ledger regression marker: {needle}")

    core_agent = read(root / "crossframe" / "agents" / "openai.yaml")
    for needle in ["过七闸", "claim ledger", "概念契约", "没有 claim_id"]:
        require(needle in core_agent, f"{label}: crossframe agent prompt missing updated marker: {needle}")
    require("过五闸" not in core_agent, f"{label}: crossframe agent prompt still says 过五闸")

    essay_agent = read(root / "crossframe-essay" / "agents" / "openai.yaml")
    for needle in ["voice_mode", "claim_id", "结构洞察底稿"]:
        require(needle in essay_agent, f"{label}: essay agent prompt missing updated marker: {needle}")
    require("现代编辑同志口吻" not in essay_agent, f"{label}: essay agent prompt still has retired fixed voice")

    for dirname in SIBLING_AGENT_PROMPT_SKILLS:
        agent = root / dirname / "agents" / "openai.yaml"
        require(agent.exists(), f"{label}: missing sibling agent prompt: {dirname}")
        text = read(agent)
        for needle in ["claim ledger delta", "claim_id"]:
            require(needle in text, f"{label}: {dirname} agent prompt missing claim handoff marker: {needle}")


def check_deep_concept_reasoning_hardening(root: Path, label: str) -> None:
    for filename in CORE_RUNTIME_PROTOCOLS:
        path = root / "crossframe" / "protocols" / filename
        require(path.exists(), f"{label}: missing core protocol: {filename}")
        text = read(path)
        for needle in [
            "## runtime hardening",
            "v5-read-state-capsule",
            "source-anchor-integrity-check",
            "concept-fidelity-check",
            "claim ledger",
            "claim-ledger-check",
            "没有 `claim_id` 的判断不得进入本协议输出",
            "概念契约",
        ]:
            require(needle in text, f"{label}: {filename} missing runtime hardening marker: {needle}")

    for filename in CORE_OUTPUT_TEMPLATES:
        path = root / "crossframe" / "templates" / filename
        require(path.exists(), f"{label}: missing core output template: {filename}")
        text = read(path)
        for needle in [
            "- 命题台账：",
            "- 概念契约：",
            "source_anchor / claim_id 边界",
            "## claim_id 输出前检查",
            "没有 `claim_id` 的中心命题",
        ]:
            require(needle in text, f"{label}: {filename} missing claim output hardening marker: {needle}")

    source_ledger = read(root / "crossframe" / "references" / "source-ledger-workflow.md")
    for needle in ["十字段硬校验", "source_id", "支持的 claim_id / 命题", "claim ledger 和 review 回指"]:
        require(needle in source_ledger, f"{label}: source ledger workflow missing ten-field claim marker: {needle}")
    require("九字段硬校验" not in source_ledger, f"{label}: source ledger workflow still says 九字段硬校验")

    capsule = read(root / "crossframe" / "templates" / "read-state-capsule.md")
    for needle in [
        "对应 claim_id",
        "是否强于 claim ledger",
        "概念契约状态",
        "先反查 `claim_id`",
        "来源台账和概念契约",
    ]:
        require(needle in capsule, f"{label}: read-state capsule missing claim-first body sweep marker: {needle}")

    suite_skill = read(root / "crossframe-suite" / "SKILL.md")
    for needle in [
        "v5-read-state-capsule",
        "source-anchor-integrity-check",
        "claim ledger / claim-ledger-check",
        "必要专项 skill 的 claim ledger delta",
        "不得早于命题台账",
    ]:
        require(needle in suite_skill, f"{label}: suite skill fixed sequence missing claim/capsule step: {needle}")

    critical_skill = read(root / "crossframe-critical" / "SKILL.md")
    for needle in ["Suite-directed use is allowed", "Do not trigger from ordinary CrossFrame"]:
        require(needle in critical_skill, f"{label}: critical skill trigger description missing suite-only clarification: {needle}")
    critical_agent = read(root / "crossframe-critical" / "agents" / "openai.yaml")
    require("suite_routing_allowed: true" in critical_agent, f"{label}: critical agent missing suite_routing_allowed policy")

    failure_taxonomy = read(root / "crossframe-review" / "references" / "failure-taxonomy.md")
    for needle in ["## AI / 弱信号强证据化", "AI 材料、弱信号、过程性产物", "行动上限"]:
        require(needle in failure_taxonomy, f"{label}: failure taxonomy missing AI weak-signal hardening entry: {needle}")

    casebook_index = read(root / "crossframe-casebook" / "templates" / "casebook-index-template.md")
    for needle in ["支持 claim_id", "机制簇", "共性条件"]:
        require(needle in casebook_index, f"{label}: casebook index missing claim bridge marker: {needle}")
    redacted_ledger = read(root / "crossframe-casebook" / "templates" / "redacted-source-ledger-template.md")
    for needle in ["source_id", "支持 claim_id", "不支撑的判断"]:
        require(needle in redacted_ledger, f"{label}: redacted source ledger missing source-to-claim marker: {needle}")

    org_retro = read(root / "crossframe-org" / "templates" / "retrospective-redesign-recommendation.md")
    for needle in ["本改造建议必须回指某个 `claim_id`", "- 对应 claim_id：", "- judgment_grade：", "- action_ceiling："]:
        require(needle in org_retro, f"{label}: org retrospective template missing claim/action boundary marker: {needle}")

    public_action = read(root / "crossframe-public" / "templates" / "action-boundary.md")
    for needle in ["## claim 边界", "- 对应 claim_id：", "- action_ceiling：", "- withdrawal_condition："]:
        require(needle in public_action, f"{label}: public action boundary missing claim boundary field: {needle}")
    public_evidence = read(root / "crossframe-public" / "templates" / "evidence-boundary-summary.md")
    for needle in ["## claim / source 对齐", "- 对应 claim_id：", "- source_id：", "- publish_boundary："]:
        require(needle in public_evidence, f"{label}: public evidence summary missing claim/source alignment field: {needle}")

    notebook_source = read(root / "crossframe-notebook" / "templates" / "source-ledger.md")
    for needle in ["source_id", "支持 claim_id / 洞察", "不可引用范围"]:
        require(needle in notebook_source, f"{label}: notebook source ledger missing source-to-claim fields: {needle}")

    archive_packet = read(root / "crossframe-history" / "templates" / "archive-request-packet.md")
    for needle in ["Affected claim_id", "Current judgment_grade", "Current publish_boundary"]:
        require(needle in archive_packet, f"{label}: history archive packet missing claim boundary field: {needle}")

    teach_exercises = read(root / "crossframe-teach" / "templates" / "micro-exercises.md")
    for needle in ["本模板只生成教学练习", "claim_id / claim ledger", "没有 `claim_id` 时不得诊断"]:
        require(needle in teach_exercises, f"{label}: teach micro exercises missing no-diagnosis boundary marker: {needle}")

    critical_template = read(root / "crossframe-critical" / "templates" / "critical-output-template.md")
    for needle in ["publish_boundary", "批判 claim ledger delta"]:
        require(needle in critical_template, f"{label}: critical output template missing publish boundary marker: {needle}")

    debate_template = read(root / "crossframe-debate" / "templates" / "debate-analysis-output.md")
    for needle in ["concept_contract", "judgment_grade", "debate claim bridge"]:
        require(needle in debate_template, f"{label}: debate claim bridge missing concept/judgment marker: {needle}")

    contracts = read(root / "crossframe" / "references" / "concept-contracts" / "core-contracts.md")
    for contract in SPECIFIC_CONCEPT_CONTRACTS:
        require(contract in contracts, f"{label}: concept contracts missing specific contract: {contract}")
        require("audit_questions:" in section_after(contracts, contract), f"{label}: {contract} missing audit_questions")

    runtime_policy = read(root / "crossframe" / "references" / "runtime-read-policy.md")
    require("相对路径默认以当前 skill 目录为语义基准" in runtime_policy, f"{label}: runtime read policy missing path semantic-base convention")


def check_freeze_cleanup(root: Path, label: str) -> None:
    for rel in RETIRED_RUNTIME_ARTIFACTS:
        require(not (root / rel).exists(), f"{label}: retired runtime artifact still exists: {rel}")

    for path in iter_text_files(root):
        try:
            text = read(path)
        except UnicodeDecodeError:
            continue
        rel = path.relative_to(root).as_posix()
        for needle in RETIRED_RUNTIME_REFERENCES:
            require(needle not in text, f"{label}: retired runtime reference {needle!r} remains in {rel}")
        for needle in SOURCE_LEDGER_OLD_MARKERS:
            require(needle not in text, f"{label}: old source ledger wording {needle!r} remains in {rel}")
        for needle in ["editorial-base", "undefined", "System.Object"]:
            require(needle not in text, f"{label}: generated/retired marker {needle!r} remains in {rel}")

    routing = read(root / "crossframe" / "references" / "read-routing-map.md")
    route_expectations = [
        ("被诊断后变化、表演、反制、策略反应", "concept-contracts/core-contracts.md#contract-reflexivity"),
        ("爱、牺牲、忍耐、照护、开放行动", "concept-contracts/core-contracts.md#contract-love_open_action"),
        ("公共承诺、平台治理、制度、分配回流、权力封闭", "concept-contracts/core-contracts.md#contract-power_closure"),
        ("工具化、公开发布、AI 工具、认证、使用门槛债", "concept-contracts/core-contracts.md#contract-toolization_accessibility"),
        ("责任链、主体、问责、干预边界、谁有改变条件", "concept-contracts/core-contracts.md#contract-responsibility_chain"),
        ("低条件行动、低风险试探、小步验证、可撤回行动", "concept-contracts/core-contracts.md#contract-low_condition_action"),
        ("退出、退出转移、保护性撤离、修复失败后的转移", "concept-contracts/core-contracts.md#contract-exit_transfer"),
        ("修复副产品、伪修复、道歉/报告/复盘替代真实改变", "concept-contracts/core-contracts.md#contract-repair_byproduct"),
        ("隐喻漂移、来源透明、规范前提、外部理论映射", "concept-contracts/core-contracts.md#contract-metaphor_source_transparency"),
    ]
    for trigger, contract in route_expectations:
        lines = [line for line in routing.splitlines() if trigger in line]
        require(lines, f"{label}: read-routing-map missing trigger row: {trigger}")
        require(any(contract in line for line in lines), f"{label}: read-routing-map trigger {trigger} does not route to {contract}")
        require(not any("generic_high_risk_concept" in line for line in lines), f"{label}: read-routing-map trigger {trigger} still routes through generic_high_risk_concept")

    crossframe_skill = read(root / "crossframe" / "SKILL.md")
    for needle in [
        "结论可以很短，但不能跳过事实抽取、七闸复核、机制候选、概念契约、判断档位、源结构连续性、claim ledger 和表达闸。",
        "- 命题台账：已生成 / 缺失已降档 / 不触发；关键 claim_id：",
        "- 概念契约：pass / partial / fail；降档决定：",
        "- 读态胶囊：已生成 / 复用 / 缺失已降档：",
        "- source_anchor / claim_id 边界：中心命题、机制句、行动建议是否已回指：",
    ]:
        require(needle in crossframe_skill, f"{label}: crossframe SKILL.md missing freeze outline marker: {needle}")

    runtime_policy = read(root / "crossframe" / "references" / "runtime-read-policy.md")
    for needle in [
        "命题台账状态，只列关键 claim_id 和是否降档，不展开完整台账。",
        "概念契约状态，只列 pass / partial / fail 和降档决定。",
        "来源台账状态，不堆所有来源字段；高责任或用户要求时再展开。",
    ]:
        require(needle in runtime_policy, f"{label}: runtime read policy missing foreground summary marker: {needle}")

    critical_protocol = read(root / "crossframe-critical" / "protocols" / "critical-article-protocol.md")
    require(
        "Use this protocol after `crossframe-suite` routes the task to `crossframe-critical`, or when the user explicitly requests CrossFrame Suite to use the critical path." in critical_protocol,
        f"{label}: critical protocol still has old explicit-invocation wording",
    )
    critical_agent = read(root / "crossframe-critical" / "agents" / "openai.yaml")
    require(
        'short_description: "经由 CrossFrame Suite 路由的结构批判长文 skill：先做 CrossFrame 底稿，再写有现实例子和篇幅规划的批判文章。"' in critical_agent,
        f"{label}: critical agent short_description still has old explicit-invocation wording",
    )

    suite_agent = read(root / "crossframe-suite" / "agents" / "openai.yaml")
    for needle in [
        "Use CrossFrame Suite as the explicit CrossFrame family entry.",
        "v5-read-state-capsule",
        "source-anchor-integrity-check",
        "claim ledger / claim-ledger-check",
        "sibling claim ledger delta",
        "without claim_id",
    ]:
        require(needle in suite_agent, f"{label}: suite agent prompt missing claim-ledger routing marker: {needle}")

    open_assertion = read(root / "crossframe" / "protocols" / "open-assertion-protocol.md")
    require("judgment-responsibility-pack" not in open_assertion, f"{label}: open assertion protocol references nonexistent judgment-responsibility-pack")
    for needle in [
        "references/concept-cards/procedural-judgment-responsibility.md",
        "v5-open-assertion-proposition-pack",
        "v5-strong-judgment-eight-pack",
        "v5-evidence-downgrade-action-ceiling-pack",
        "v5-low-power-protection-pack",
    ]:
        require(needle in open_assertion, f"{label}: open assertion high-responsibility route missing marker: {needle}")

    suite_root = root / "crossframe-suite"
    for path in iter_text_files(root):
        rel = path.relative_to(root).as_posix()
        if not rel.startswith("crossframe-suite/"):
            continue
        text = read(path)
        for needle in ["crossframe-review-lite", "review-lite"]:
            require(needle not in text, f"{label}: ghost review-lite route {needle!r} remains in {rel}")
    for rel in [
        "SKILL.md",
        "references/workflow-routing-map.md",
        "evals/crossframe-suite-smoke-tests.md",
        "examples/reader-reply-workflow-case.md",
    ]:
        text = read(suite_root / rel)
        require("crossframe-review(lite)" in text, f"{label}: {rel} missing explicit crossframe-review(lite) route label")

    evidence_checklist = read(root / "crossframe-review" / "references" / "evidence-boundary-checklist.md")
    for needle in [
        "- source_id",
        "- 来源",
        "- 时间",
        "- 来源类型",
        "- 支持的 claim_id / 命题",
        "- 不能证明什么",
        "- 证据档位",
        "- 使用位置",
        "- 降档理由",
        "- 仍需补证处",
    ]:
        require(needle in evidence_checklist, f"{label}: evidence boundary checklist missing source ledger field: {needle}")

    insight_dossier = read(root / "crossframe-essay" / "templates" / "insight-dossier-template.md")
    require("  - source_id：" in insight_dossier, f"{label}: insight dossier source ledger summary missing source_id")

    routing = read(root / "crossframe" / "references" / "read-routing-map.md")
    open_assertion_lines = [
        line for line in routing.splitlines()
        if all(marker in line for marker in ["开放断言", "可撤回判断", "当前只能说", "撤回条件", "不能证明什么"])
    ]
    require(open_assertion_lines, f"{label}: read-routing-map missing open_assertion high-risk concept row")
    require(
        any("concept-contracts/core-contracts.md#contract-open_assertion" in line for line in open_assertion_lines),
        f"{label}: read-routing-map open_assertion row missing contract-open_assertion route",
    )
    require(
        any("concept-cards/open-assertion.md" in line and "protocols/open-assertion-protocol.md" in line for line in open_assertion_lines),
        f"{label}: read-routing-map open_assertion row missing concept card/protocol route",
    )
    for bundle in ["v5-open-assertion-proposition-pack", "v5-source-evidence-separation-pack", "v5-evidence-downgrade-action-ceiling-pack"]:
        require(any(bundle in line for line in open_assertion_lines), f"{label}: read-routing-map open_assertion row missing bundle: {bundle}")

    generation_gate_requirements = {
        "crossframe/SKILL.md": [
            "生成层不得宣布质量闸通过、完全通过、A档、合格或 `substantive_pass`。",
            "没有进入 `crossframe-review` 前，不得给出 `structural_pass`、`substantive_pass` 或 `publish_boundary` 的通过结论。",
            "生成层自我盖章",
            "只要输出中出现 `open_assertion`、开放断言、可撤回判断、最高开放断言、不能终局裁决、当前只能说、不能证明什么或撤回条件",
            "不得写“概念契约不触发”",
        ],
        "crossframe-essay/SKILL.md": [
            "`crossframe-essay` 不得宣布质量闸通过",
            "标题、小标题、中心点睛句和结尾",
            "文章类型选择器若要求用户选编号、默认项或推荐项，必须等待用户回复",
            "不得写“所有技法已读取”",
        ],
        "crossframe-essay/templates/essay-output-template.md": [
            "生成层只能输出自检摘要",
            "标题参与 `body_mappings` 反查",
            "只能写“已读取本次选用技法”",
        ],
        "crossframe-suite/SKILL.md": [
            "质量闸归属",
            "生成层是否自我盖章",
            "`structural_pass`、`substantive_pass` 和 `publish_boundary` 只能由 review 判定",
        ],
        "crossframe-suite/agents/openai.yaml": [
            "crossframe-inquiry",
            "continue thinking",
            "ask questions",
        ],
        "crossframe-suite/protocols/suite-dispatch-protocol.md": [
            "生成层自检摘要：已修正 X，待 review 判定",
            "不得写“质量闸通过 / 完全通过 / substantive_pass”",
        ],
        "crossframe-suite/templates/suite-reasoning-outline.md": [
            "structural_pass 待 review 判定",
            "不能写 `structural_pass=true`、`substantive_pass=true`",
        ],
        "crossframe/templates/claim-ledger.md": [
            "## 前台摘要与完整台账",
            "缺少 `source_anchor`、`mechanism_id`、`concept_contract`、`source_ledger_id` 或 `publish_boundary`",
            "| 台账摘要冒充完整台账 |",
            "| mechanism_candidate 无 mechanism_id |",
            "| open_assertion 未触发概念契约 |",
            "| 标题强于台账 |",
            "| 生成层自称质量闸通过 |",
        ],
        "crossframe-review/protocols/review-protocol.md": [
            "6. 自我盖章候选",
            "9. 台账摘要伪完整候选",
            "生成层自称质量闸通过、完全通过、A 档、合格或 `substantive_pass`",
            "补 `contract-open_assertion`",
        ],
        "crossframe-review/references/failure-taxonomy.md": [
            "## 生成层自我盖章",
            "## 概念契约伪未触发",
            "## 命题台账摘要冒充完整台账",
            "## 标题/点睛句强于台账",
        ],
        "crossframe-review/references/review-rubric.md": [
            "生成层自称质量闸通过",
            "正文出现 `open_assertion`",
            "不完整命题台账",
            "标题、首段或结尾强于 `claim_id`",
            "`substantive_pass` 不能由生成层自评",
        ],
        "crossframe-review/templates/review-report.md": [
            "| 自我盖章候选 |",
            "| 概念契约伪未触发候选 |",
            "| 标题强于台账候选 |",
            "| 台账摘要伪完整候选 |",
            "是否出现生成层质量自我通过",
        ],
        "crossframe-review/evals/crossframe-review-smoke-tests.md": [
            "## 概念契约伪未触发与自我盖章",
            "质量闸：通过",
            "概念契约：不触发",
        ],
        "crossframe/templates/reasoning-outline-output.md": [
            "## 自检边界",
            "提纲和自检不得写",
        ],
    }
    for rel, needles in generation_gate_requirements.items():
        text = read(root / rel)
        for needle in needles:
            require(needle in text, f"{label}: generation/review gate hardening missing {needle!r} in {rel}")

    open_assertion_trigger_line = next((line for line in routing.splitlines() if "开放断言、可撤回判断" in line), "")
    for needle in ["最高开放断言", "不能终局裁决"]:
        require(needle in open_assertion_trigger_line, f"{label}: read-routing-map open_assertion trigger row missing: {needle}")


def check_no_trailing_whitespace(root: Path, label: str) -> None:
    for path in iter_text_files(root):
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        for idx, line in enumerate(lines, start=1):
            require(not line.endswith((" ", "\t")), f"{label}: trailing whitespace in {path.relative_to(root)}:{idx}")


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

    for skill in ["crossframe-suite", "crossframe-essay", "crossframe-review", "crossframe-public", "crossframe-org", "crossframe-debate", "crossframe-critical", "crossframe-history", "crossframe-inquiry"]:
        eval_dir = root / skill / "evals"
        require(eval_dir.is_dir(), f"{label}: missing eval directory for {skill}")
        require(any(eval_dir.glob("*.md")), f"{label}: empty eval directory for {skill}")

    review_failure = read(root / "crossframe-review" / "references" / "failure-taxonomy.md")
    for needle in ["选择器压缩失败", "技法越界失败", "来源用途越界失败", "来源台账缺失", "来源台账字段伪完整", "技法落地不可审计", "结构通过误作发布通过"]:
        require(needle in review_failure, f"{label}: review failure taxonomy missing: {needle}")

    review_eval = read(root / "crossframe-review" / "evals" / "crossframe-review-smoke-tests.md")
    for needle in ["来源台账字段伪完整", "单一来源族", "技法落地不可审计", "胶囊闭包自证失败", "结构通过误作发布通过"]:
        require(needle in review_eval, f"{label}: review eval missing hardening case: {needle}")

    anti_imitation_eval = read(root / "crossframe" / "evals" / "crossframe-anti-imitation-tests.md")
    for needle in ["claim ledger", "claim_id", "概念契约", "开放断言", "不得判 substantive_pass"]:
        require(needle in anti_imitation_eval, f"{label}: anti-imitation eval missing marker: {needle}")

    essay_eval = read(root / "crossframe-essay" / "evals" / "crossframe-essay-smoke-tests.md")
    for needle in ["命题台账摘要", "关键 `claim_id`", "写作技法是否只绑定已有 `claim_id`", "无 `claim_id` 的强句子"]:
        require(needle in essay_eval, f"{label}: essay eval missing claim_id regression marker: {needle}")

    suite_eval = read(root / "crossframe-suite" / "evals" / "crossframe-suite-smoke-tests.md")
    for needle in ["claim ledger", "命题台账摘要", "命题台账候选"]:
        require(needle in suite_eval, f"{label}: suite eval missing claim ledger regression marker: {needle}")

    review_eval = read(root / "crossframe-review" / "evals" / "crossframe-review-smoke-tests.md")
    for needle in ["命题台账裸奔失败", "责任链彻底断裂", "不得判 `substantive_pass`"]:
        require(needle in review_eval, f"{label}: review eval missing claim ledger naked-claim case: {needle}")


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

    claim_ledger = read(root / "crossframe" / "templates" / "claim-ledger.md")
    for needle in ["claim_id", "judgment_grade", "action_ceiling", "撤回条件", "publish_boundary"]:
        require(needle in claim_ledger, f"{label}: claim ledger missing hardening marker: {needle}")

    anchor = read(root / "crossframe" / "worksheets" / "source-anchor-integrity-check.md")
    for needle in ["正文高风险概念回扫", "仅写一行", "source modules 是否有", "正文短摘"]:
        require(needle in anchor, f"{label}: source anchor check missing hardening marker: {needle}")

    review_protocol = read(root / "crossframe-review" / "protocols" / "review-protocol.md")
    for needle in ["反向否决最小块", "正文抽句回指", "claim_id", "structural_pass", "substantive_pass", "publish_boundary"]:
        require(needle in review_protocol, f"{label}: review protocol missing hardening marker: {needle}")

    review_rubric = read(root / "crossframe-review" / "references" / "review-rubric.md")
    for needle in ["等级上限", "structural_pass", "substantive_pass", "publish_boundary"]:
        require(needle in review_rubric, f"{label}: review rubric missing pass-boundary marker: {needle}")


def check_root(root: Path, label: str) -> None:
    require(root.is_dir(), f"{label}: skill root does not exist: {root}")
    check_no_retired_dirs(root, label)
    check_required_skill_dirs(root, label)
    check_source_ledger(root, label)
    check_claim_ledger(root, label)
    check_history_adapter(root, label)
    check_inquiry_layer(root, label)
    check_suite_routes_all_siblings(root, label)
    check_sibling_claim_bridges(root, label)
    check_deep_concept_reasoning_hardening(root, label)
    check_techniques(root, label)
    check_evals(root, label)
    check_quality_gate_hardening(root, label)
    check_freeze_cleanup(root, label)
    check_no_trailing_whitespace(root, label)


def main() -> int:
    parser = argparse.ArgumentParser(description="Check CrossFrame skill integrity outside v5 source continuity.")
    parser.add_argument("--repo", default=".", help="Repository root or skill root.")
    parser.add_argument("--mirror", action="append", default=[], help="Additional skill root to validate.")
    args = parser.parse_args()

    check_repo_adapters(repo_root_from_arg(args.repo), "repo")
    check_public_release_docs(repo_root_from_arg(args.repo), "repo")

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
