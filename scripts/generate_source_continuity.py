from __future__ import annotations

import argparse
import re
from pathlib import Path

from docx import Document


BUNDLE_DEFS: dict[str, dict[str, str]] = {
    "framework-use-discipline-pack": {
        "name": "框架使用纪律包",
        "summary": "约束 CrossFrame 如何使用：防概念武器化、防教条化、防万能化、防 AI 文本替代证据。",
        "must": "使用准则、输出禁忌、本体保护、AI 输出分离和适用性分级。",
        "materials": "references/guardrails.md；references/framework-ontology-protection.md；protocols/framework-boundary-protocol.md",
        "failure": "把框架当万能审判、专业替代或人格定性工具。",
    },
    "judgment-responsibility-pack": {
        "name": "判断责任包",
        "summary": "约束开放断言、强判断、命题验证和高责任处置，防止可撤回判断被当成终局裁决。",
        "must": "证据成本、判断档位、命题验证、申诉/反证入口、弱信号保护和反俘获。",
        "materials": "protocols/open-assertion-protocol.md；protocols/proposition-verification-protocol.md；protocols/anti-capture-protocol.md",
        "failure": "用开放断言绕过强判断验证，或把判断用于处置却没有撤回条件。",
    },
    "diagnosis-mainline-pack": {
        "name": "诊断主线包",
        "summary": "保持对象、事实、尺度、机制候选、五闸、工具箱和诊断维度的连续主线。",
        "must": "有限干预、观测登记、诊断档位、主流程、五闸、机制候选和诊断维度。",
        "materials": "protocols/diagnosis-protocol.md；worksheets/five-gates-worksheet.md；references/diagnostic-dimensions.md；references/diagnostic-toolbox-index.md",
        "failure": "只套机制标签，跳过对象、证据、尺度、责任和观测影响。",
    },
    "intimate-love-care-pack": {
        "name": "亲密关系/爱/照护包",
        "summary": "处理关系、照护、爱、解释劳动和疗愈时，先保护痛苦、安全和边界。",
        "must": "亲密关系轻量入口、爱诊断红线、开放行动、修复副产品、责任链和疗愈/转移。",
        "materials": "protocols/intimate-relationship-protocol.md；protocols/healing-transfer-protocol.md；references/concept-cards/love-open-action.md",
        "failure": "把爱写成忍耐命令，把修复责任压回受伤者，或用结构词抹掉痛苦。",
    },
    "public-power-governance-pack": {
        "name": "公共制度与权力包",
        "summary": "处理平台、制度、公共承诺、程序有效性、权力封闭和低权力主体保护。",
        "must": "反俘获、程序有效性、弱信号安全、退出转移、公共承诺、偿付和多中心治理。",
        "materials": "protocols/public-institution-protocol.md；protocols/anti-capture-protocol.md；protocols/governance-continuity-protocol.md",
        "failure": "把程序外观当有效程序，把 AI 文本当强证据，或忽略弱信号安全。",
    },
    "long-evolution-deep-pack": {
        "name": "长期演化深水区包",
        "summary": "处理根假设、生命周期、递进、势场、自主解离、治理连续性和文明尺度压力测试。",
        "must": "根假设/核心推论、生命周期、递进、势场、解离、调节预警偿付、多中心治理和超大规模压力测试。",
        "materials": "references/theory-backend-index.md；protocols/lifecycle-diagnosis-protocol.md；protocols/progression-protocol.md；protocols/field-dissociation-protocol.md",
        "failure": "把阶段写成宿命，把势场写成氛围，把文明尺度写成绝对结论。",
    },
    "expression-article-pack": {
        "name": "表达与文章输出包",
        "summary": "把后台概念翻译成人话、管理/制度/技术语境或文章输出，避免术语墙。",
        "must": "对外表达翻译、用户语言闸、推理提纲和文章底稿/正文规则。",
        "materials": "protocols/expression-translation-protocol.md；templates/user-facing-language.md；../crossframe-essay/SKILL.md",
        "failure": "后台推理存在但前台变成术语墙，或文章只剩概念姿态没有现实入口。",
    },
    "v3-framework-governance-falsification-pack": {
        "name": "框架治理与证伪包",
        "summary": "处理框架自诊、版本治理、根假设暂停、案例库偏差、框架良性消亡和替代框架接口。",
        "must": "自诊对象、版本治理、反例登记、暂停使用、案例库失败样本、良性消亡和替代接口。",
        "materials": "references/v3-term-fidelity.md；references/v3-change-rationale-from-patch.md；references/framework-ontology-protection.md",
        "failure": "用框架自己的语言证明框架安全，或为了保住框架无限加补丁。",
    },
    "v3-procedural-judgment-pack": {
        "name": "程序与判断责任包",
        "summary": "处理共识程序、概念有效性分级、强判断升级和开放断言被权力捕获后的退场。",
        "must": "共识七环节、E0-E4 概念有效性、判断责任、开放断言退场和修复/补偿入口。",
        "materials": "protocols/proposition-verification-protocol.md；references/concept-cards/procedural-judgment-responsibility.md",
        "failure": "把名义共识当有效共识，或让开放断言实际进入处置和公共记忆。",
    },
    "v3-evidence-visibility-pack": {
        "name": "证据可见性包",
        "summary": "处理可见性偏误、缺席信号、正当/压制性不透明、弱信号保护和 AI 现实验证边界。",
        "must": "缺席信号类别、不透明三分、弱信号六件套、AI 缺失材料清单和证据降档。",
        "materials": "references/concept-cards/visibility-opacity-weak-signals.md；references/concept-cards/malicious-compliance-ai-validation.md",
        "failure": "把沉默当不存在，把不透明当天然合理，或把 AI 报告格式当现实核验。",
    },
    "v3-power-capture-malicious-compliance-pack": {
        "name": "权力捕获与恶意合规包",
        "summary": "处理选择性证据、表演性合规、AI 合规幻觉和结构语言被用来洗白不作为。",
        "must": "恶意合规信号、证据选择性、申诉是否改变结果、复核独立性和责任转嫁检查。",
        "materials": "protocols/anti-capture-protocol.md；references/concept-cards/malicious-compliance-ai-validation.md",
        "failure": "规则表面被遵守，但弱信号被过滤、申诉无效、责任被结构语言转移。",
    },
    "v3-no-institution-middle-path-pack": {
        "name": "无制度基础设施包",
        "summary": "处理家庭、小团队、亲密关系、临时项目和非正式社群中没有正式复核但风险持续的场景。",
        "must": "中间路径原则、保护性开放断言、低暴露记录、外部视角和升级/撤回条件。",
        "materials": "protocols/low-condition-action-protocol.md；protocols/intimate-relationship-protocol.md；references/concept-cards/no-institution-middle-path.md",
        "failure": "强行模拟不存在的制度，或因为不能复核就完全不判断。",
    },
    "v3-trapped-trauma-baseline-pack": {
        "name": "无法退出与复杂创伤包",
        "summary": "处理无法退出主体、复杂创伤、无健康基准、初建型修复和创伤建材型结构。",
        "must": "安全优先、代理保护、最小自主、低暴露记录、替代出口和首次建立健康基准。",
        "materials": "protocols/healing-transfer-protocol.md；references/concept-cards/trapped-subject-trauma-baseline.md",
        "failure": "要求无法退出者承担理想退出，或把创伤性生存策略误判为偏离健康锚点。",
    },
    "v3-love-generative-action-pack": {
        "name": "爱与开放行动生成包",
        "summary": "把爱定位为不能由既有结构充分推出、但出现后可被追踪的生成事件，而不是解释失败的剩余。",
        "must": "结构解释线、生成事件线、真实成本、新通道、新记忆、新责任分配和新承接者。",
        "materials": "references/concept-cards/love-open-action.md；references/concept-cards/love-generative-action.md；references/love-as-open-action.md",
        "failure": "把爱神化为不可分析，或还原成利益/依附/恐惧解释后的剩余垃圾桶。",
    },
    "v3-concept-migration-metaphor-pack": {
        "name": "概念迁移与隐喻控制包",
        "summary": "处理跨尺度迁移前概念闸、隐喻漂移、规范性前提声明和知识谱系透明。",
        "must": "六个白话前概念问题、隐喻身份标注、规范性前提公开和来源透明。",
        "materials": "references/scale-transfer-gate.md；references/concept-cards/metaphor-source-transparency.md；references/v3-term-fidelity.md",
        "failure": "用跨域隐喻证明因果，或把框架的价值选择伪装成纯经验结论。",
    },
    "v3-toolization-accessibility-pack": {
        "name": "工具化与可及性包",
        "summary": "处理使用门槛债、可及性审计、商业化工具化风险、认证垄断和分支分裂协议。",
        "must": "学习债、翻译债、证据债、复核债、退出债、身份债、工具化红线和分裂说明。",
        "materials": "references/concept-cards/accessibility-toolization-split.md；references/framework-ontology-protection.md",
        "failure": "让框架变成专家垄断、商业交付压力或新的解释权不平等。",
    },
    "v3-observation-entropy-contraction-pack": {
        "name": "观测收束与熵增边界包",
        "summary": "处理阶段 6、熵增操作边界、观测递归扩张条件和必须收束的元规则。",
        "must": "发现滞后、修复滞后、复发率、修复副产品、负荷分布、观测扩张/收束条件。",
        "materials": "protocols/high-reflexivity-protocol.md；protocols/lifecycle-diagnosis-protocol.md；references/concept-cards/observation-entropy-contraction.md",
        "failure": "无限追踪反应，或把阶段/熵增写成不作为的托词。",
    },
}

BUNDLE_ORDER = list(BUNDLE_DEFS)


SPECIFIC_DIGESTS: list[tuple[str, str]] = [
    ("框架自诊", "框架本身也必须被诊断，但要区分文档对象、概念对象、实践对象和共同体对象，并让外部反例进入版本治理。"),
    ("版本治理", "版本不是文档编号，而是合并权、解释权、发布权、回滚权和反例入口的最低制度安排。"),
    ("共识程序", "共识不是所有人最后同意，而是异议能安全进入、被记录、被回应，并能影响版本写回。"),
    ("根假设", "根假设必须允许降级、暂停、替代假设竞争和退出核心层，不能靠定义转移逃避反例。"),
    ("案例库", "案例库必须登记失败、早期消失、反例、不确定和被排除案例，防止只从成功文本系统里总结规律。"),
    ("跨尺度迁移的前概念闸", "使用术语前先用白话确认对象、边界、互动、共同约束、维护成本和反馈写回是否存在。"),
    ("概念有效性", "概念有效性按 E0-E4 分级：从表达、探索、诊断、强判断到处置，每一级都有证据和责任门槛。"),
    ("可见性偏误", "看不见不等于不存在；沉默、缺席、不表达和无记录都可能是结构性信号。"),
    ("缺席信号", "缺席信号包括锚点缺席、反馈缺席、冲突缺席、修复缺席、退出缺席和语言缺席。"),
    ("正当不透明", "不透明要区分保护性、功能性和压制性，并追问保护谁、谁受益、谁能复核、何时解除。"),
    ("阶段6", "阶段 6 与熵增不能写成完美或宿命，只能用发现滞后、修复滞后、复发率、修复副产品和负荷分布操作化。"),
    ("观测递归", "观测可以扩张，但当反应不再提供新结构变量、增加暴露风险或被对象用来拖延反制时必须收束。"),
    ("恶意合规", "高阶误用会选择性遵守格式，同时操纵证据、压制弱信号、把结构语言变成责任洗白。"),
    ("AI 诊断", "AI 可以整理材料和生成问题，但不能证明现实已被充分诊断，也不能验证委托方诚信和反报复保护。"),
    ("弱信号保护", "弱信号保护不是诊断者善良，而是匿名入口、独立承接、反报复登记、分组校准、延迟公开和写回证明。"),
    ("无制度基础设施", "在家庭、小团队和非正式关系中，不能强行模拟制度，也不能因缺少制度就停止保护性判断。"),
    ("无法退出", "无法退出主体的目标不是完成理想退出，而是在不可退出条件下减少伤害、保存主体性、扩大未来选择。"),
    ("复杂创伤", "没有健康基准时，问题不是回到原状，而是首次建立最低安全、可预测支持和不会被惩罚的表达入口。"),
    ("爱与开放性承担行动", "爱不是结构解释不了的剩余，而是不能由既有结构充分推出、出现后可追踪其新通道和新承接的生成事件。"),
    ("规范性前提", "框架不是价值中立工具，必须公开反对结构语言取消责任、反对用爱/使命/大局抽取低权力主体。"),
    ("隐喻漂移", "跨域隐喻只能打开观察角度，不能直接承担因果证明或强判断。"),
    ("知识谱系", "框架要说明思想亲缘、保留与改造之处，避免把外部理论吞并成全能语言。"),
    ("使用门槛债", "框架复杂性会带来学习债、翻译债、证据债、复核债、退出债和身份债，必须审计可及性。"),
    ("工具化", "框架被课程、咨询、AI 工具或组织软件使用时，不能为交付效率降低反俘获和复核要求。"),
    ("开放断言被权力捕获", "开放断言若被写入考核、档案、资源分配或公共记忆，就必须退场、标注误用并进入修复责任链。"),
    ("良性消亡", "成熟框架要知道何时降级、转接或退场，不能为了保住自身无限扩张概念。"),
]


def has_any(text: str, keywords: list[str]) -> bool:
    return any(keyword in text for keyword in keywords)


def add_if(bundles: set[str], title: str, bundle_id: str, keywords: list[str]) -> None:
    if has_any(title, keywords):
        bundles.add(bundle_id)


def bundles_for(title: str) -> list[str]:
    if title == "目录":
        return ["source-structure-only"]

    bundles: set[str] = set()
    add_if(
        bundles,
        title,
        "framework-use-discipline-pack",
        [
            "极简导读",
            "框架定位",
            "解释对象",
            "使用准则",
            "概念武器化",
            "教条化",
            "本体保护",
            "输出禁忌",
            "适用性",
            "盲区",
            "概念层级",
            "保真",
            "前台",
            "后台",
            "修改资格",
        ],
    )
    add_if(
        bundles,
        title,
        "judgment-responsibility-pack",
        [
            "强判断",
            "开放断言",
            "命题验证",
            "前瞻登记",
            "判断责任",
            "反向条件",
            "申诉",
            "证据要求",
            "证伪",
            "高责任",
            "低条件",
            "反俘获",
            "程序有效性",
        ],
    )
    add_if(
        bundles,
        title,
        "diagnosis-mainline-pack",
        [
            "诊断",
            "预判",
            "有限干预",
            "观测影响",
            "诊断档位",
            "主流程",
            "圈层",
            "对象",
            "约束",
            "锚点",
            "主体层",
            "五闸",
            "工具箱",
            "机制候选",
            "维度",
        ],
    )
    add_if(
        bundles,
        title,
        "intimate-love-care-pack",
        ["亲密", "爱", "照护", "家庭", "解释劳动", "疗愈", "修复", "牺牲", "不浪费爱"],
    )
    add_if(
        bundles,
        title,
        "public-power-governance-pack",
        ["公共", "制度", "治理", "权力", "平台", "合规", "申诉", "承诺", "偿付", "多中心", "低权力"],
    )
    add_if(
        bundles,
        title,
        "long-evolution-deep-pack",
        ["理论", "根假设", "核心推论", "全周期", "生命周期", "阶段", "递进", "势场", "自主解离", "文明", "历史", "熵增"],
    )
    add_if(bundles, title, "expression-article-pack", ["输出", "表达", "翻译", "模板", "格式", "说人话", "文章", "发布"])

    add_if(
        bundles,
        title,
        "v3-framework-governance-falsification-pack",
        ["框架自诊", "版本治理", "根假设证伪", "暂停使用", "案例库", "幸存者偏差", "良性消亡", "替代框架"],
    )
    add_if(
        bundles,
        title,
        "v3-procedural-judgment-pack",
        ["共识程序", "七个环节", "概念有效性", "开放断言被权力捕获", "退场规则", "判断责任"],
    )
    add_if(
        bundles,
        title,
        "v3-evidence-visibility-pack",
        ["可见性偏误", "缺席信号", "正当不透明", "压制性不透明", "弱信号保护", "AI 诊断"],
    )
    add_if(
        bundles,
        title,
        "v3-power-capture-malicious-compliance-pack",
        ["恶意合规", "选择性证据", "AI 合规", "权力捕获"],
    )
    add_if(
        bundles,
        title,
        "v3-no-institution-middle-path-pack",
        ["无制度基础设施", "中间路径", "非正式社群", "临时项目"],
    )
    add_if(
        bundles,
        title,
        "v3-trapped-trauma-baseline-pack",
        ["无法退出", "复杂创伤", "无健康基准", "初建型", "创伤建材"],
    )
    add_if(
        bundles,
        title,
        "v3-love-generative-action-pack",
        ["爱与开放性承担行动", "开放性承担行动", "生成事件", "两条记录线"],
    )
    add_if(
        bundles,
        title,
        "v3-concept-migration-metaphor-pack",
        ["前概念闸", "隐喻漂移", "知识谱系", "来源透明", "规范性前提", "跨尺度迁移"],
    )
    add_if(
        bundles,
        title,
        "v3-toolization-accessibility-pack",
        ["使用门槛债", "可及性", "工具化", "商业化", "分裂风险", "分裂协议"],
    )
    add_if(
        bundles,
        title,
        "v3-observation-entropy-contraction-pack",
        ["阶段6", "熵增", "观测递归", "收束元规则"],
    )

    if not bundles:
        bundles.add("diagnosis-mainline-pack")
    return [bundle for bundle in BUNDLE_ORDER if bundle in bundles]


def status_for(title: str, bundles: list[str]) -> str:
    if "source-structure-only" in bundles:
        return "源结构节点"
    if has_any(title, ["协议", "流程", "入口", "模板", "记录表", "规则", "检查", "七个环节"]):
        return "已协议化/已联读约束"
    if has_any(title, ["概念", "锚点", "势场", "证据", "弱信号", "爱", "退出", "不透明", "门槛债"]):
        return "已概念卡化/已联读约束"
    if has_any(title, ["根假设", "核心推论", "理论", "全周期", "文明", "良性消亡"]):
        return "已索引化/后台联读"
    return "已联读约束"


def carry_for(bundles: list[str]) -> str:
    if "source-structure-only" in bundles:
        return "references/v3-source-spine.md"
    return "；".join(BUNDLE_DEFS[bundle]["materials"] for bundle in bundles if bundle in BUNDLE_DEFS)


def digest_for(title: str, bundles: list[str]) -> str:
    for key, digest in SPECIFIC_DIGESTS:
        if key in title:
            return digest
    names = [BUNDLE_DEFS[bundle]["name"] for bundle in bundles if bundle in BUNDLE_DEFS]
    if not names:
        return "源结构目录节点，用于保持 3.0 原文顺序，不承担独立判断。"
    return f"本节归入{'、'.join(names)}，用于保持“{title}”在 3.0 原文中的连续约束；读取时要放回相邻章节和联读包理解。"


def boundary_for(bundles: list[str]) -> str:
    if "source-structure-only" in bundles:
        return "不能把目录节点当概念依据。"
    parts: list[str] = []
    if "framework-use-discipline-pack" in bundles:
        parts.append("不能把框架当万能审判或专业替代。")
    if "judgment-responsibility-pack" in bundles:
        parts.append("不能用开放断言替代强判断验证。")
    if "diagnosis-mainline-pack" in bundles:
        parts.append("不能跳过对象、证据、尺度、责任和观测闸。")
    if "intimate-love-care-pack" in bundles:
        parts.append("不能把爱或照护写成单方忍耐义务。")
    if "public-power-governance-pack" in bundles:
        parts.append("不能把程序外观或 AI 合规文本当强证据。")
    if "long-evolution-deep-pack" in bundles:
        parts.append("不能把阶段/势场/文明尺度写成宿命结论。")
    if "expression-article-pack" in bundles:
        parts.append("不能用术语墙替代普通人可读表达。")
    if any(bundle.startswith("v3-") for bundle in bundles):
        parts.append("不能只读单点补丁；必须按 v3.0 连续包确认相邻约束。")
    return "".join(parts)


def extract_headings(docx_path: Path) -> tuple[int, list[dict[str, object]]]:
    doc = Document(str(docx_path))
    headings: list[dict[str, object]] = []
    for idx, para in enumerate(doc.paragraphs):
        text = " ".join(para.text.split())
        style = para.style.name
        if text and style.startswith("Heading"):
            match = re.search(r"(\d+)$", style)
            level = int(match.group(1)) if match else 1
            headings.append({"para": idx, "level": level, "title": text})
    return sum(1 for para in doc.paragraphs if para.text.strip()), headings


def extract_patch_paragraphs(patch_docx: Path | None) -> list[str]:
    if not patch_docx or not patch_docx.exists():
        return []
    doc = Document(str(patch_docx))
    return [" ".join(para.text.split()) for para in doc.paragraphs if para.text.strip()]


def prepare_headings(headings: list[dict[str, object]], version: str) -> None:
    prefix = version.upper()
    for idx, heading in enumerate(headings):
        heading["id"] = f"{prefix}-H{idx + 1:03d}"
        heading["prev"] = f"{prefix}-H{idx:03d}" if idx else "-"
        heading["next"] = f"{prefix}-H{idx + 2:03d}" if idx + 1 < len(headings) else "-"
        heading["bundles"] = bundles_for(str(heading["title"]))
        heading["status"] = status_for(str(heading["title"]), heading["bundles"])  # type: ignore[arg-type]
        heading["carry"] = carry_for(heading["bundles"])  # type: ignore[arg-type]
        heading["digest"] = digest_for(str(heading["title"]), heading["bundles"])  # type: ignore[arg-type]
        heading["boundary"] = boundary_for(heading["bundles"])  # type: ignore[arg-type]


def write_source_spine(crossframe: Path, version: str, docx_path: Path, nonempty: int, headings: list[dict[str, object]]) -> None:
    path = crossframe / "references" / f"{version}-source-spine.md"
    lines = [
        f"# {version}.0 源结构脊柱\n\n",
        f"本文件从 `{docx_path.name}` 的 Word 标题层级生成，用于保存 {version}.0 原文的章节顺序、相邻关系和 CrossFrame 承接位置。它不是原文复制件；不得把本文件当作完整理论正文。\n\n",
        f"- 来源：`{docx_path.name}`\n",
        f"- 非空段落：{nonempty}\n",
        f"- Word 标题节点：{len(headings)}\n",
        f"- 稳定 ID：`{version.upper()}-H001` 起按原文标题出现顺序编号。\n",
        "- 使用方法：先按 `read-routing-map.md` 确定任务路由，再用本文件确认相邻章节和连续联读包。\n\n",
        "## 连续联读包图例\n\n",
        "| 联读包 ID | 中文名 | 作用 | 必须避免的读法 |\n",
        "| --- | --- | --- | --- |\n",
    ]
    for bundle_id, bundle in BUNDLE_DEFS.items():
        lines.append(f"| `{bundle_id}` | {bundle['name']} | {bundle['summary']} | 不得只读单个概念卡；必须联读{bundle['must']} |\n")
    lines.extend(
        [
            "| `source-structure-only` | 源结构节点 | 目录或结构占位，只保持原文顺序 | 不得作为诊断依据 |\n\n",
            "## 源章节顺序表\n\n",
            "| ID | 段落 | 层级 | 标题 | 连续联读包 | 承接状态 | CrossFrame 承接位置 | 前一节 | 后一节 |\n",
            "| --- | ---: | ---: | --- | --- | --- | --- | --- | --- |\n",
        ]
    )
    for heading in headings:
        bundles = ", ".join(f"`{bundle}`" for bundle in heading["bundles"])  # type: ignore[index]
        lines.append(
            f"| `{heading['id']}` | P{heading['para']:04d} | H{heading['level']} | {heading['title']} | {bundles} | {heading['status']} | {heading['carry']} | `{heading['prev']}` | `{heading['next']}` |\n"
        )
    path.write_text("".join(lines), encoding="utf-8")


def write_digest(crossframe: Path, version: str, docx_path: Path, headings: list[dict[str, object]]) -> None:
    path = crossframe / "references" / f"{version}-section-digest-index.md"
    lines = [
        f"# {version}.0 逐节保真摘要索引\n\n",
        f"本文件为 `{docx_path.name}` 的章节级摘要索引。它不是全文替代品，而是帮助 agent 在按需读取时知道每节的核心用途、误读边界和相邻约束。\n\n",
        "| ID | 源章节 | 保真摘要 | 不可误读边界 | 相邻联读提醒 |\n",
        "| --- | --- | --- | --- | --- |\n",
    ]
    for heading in headings:
        bundles = ", ".join(f"`{bundle}`" for bundle in heading["bundles"])  # type: ignore[index]
        lines.append(
            f"| `{heading['id']}` | {heading['title']} | {heading['digest']} | {heading['boundary']} | 前接 `{heading['prev']}`，后接 `{heading['next']}`；同包：{bundles} |\n"
        )
    path.write_text("".join(lines), encoding="utf-8")


def write_coverage(crossframe: Path, version: str, headings: list[dict[str, object]]) -> None:
    path = crossframe / "references" / f"{version}-coverage-map.md"
    by_bundle: dict[str, int] = {bundle: 0 for bundle in BUNDLE_DEFS}
    for heading in headings:
        for bundle in heading["bundles"]:  # type: ignore[index]
            if bundle in by_bundle:
                by_bundle[bundle] += 1
    lines = [
        f"# {version}.0 覆盖地图\n\n",
        f"本文件用于回答“CrossFrame 相较 {version}.0 是否还有遗漏”。它不替代原文，而是记录每个重要模块在 skill 中的承接位置。\n\n",
        "章节级覆盖由三层文件共同维护：\n\n",
        f"- `{version}-source-spine.md`：记录源章节节点、相邻关系、联读包和承接状态。\n",
        f"- `{version}-section-digest-index.md`：记录逐节保真摘要、不可误读边界和相邻提醒。\n",
        "- `continuity-bundles.md`：规定哪些板块不能单读概念卡。\n\n",
        "## v3.0 新增重点\n\n",
        "| 新增模块 | 承接文件 | 状态 | 使用边界 |\n",
        "| --- | --- | --- | --- |\n",
        "| 框架自诊、版本治理、根假设证伪、良性消亡 | `v3-term-fidelity.md`、`v3-change-rationale-from-patch.md`、`continuity-bundles.md` | 已联读约束/后台保真 | 框架也要接受外部审计，不能自证安全 |\n",
        "| 共识程序、概念有效性分级、开放断言退场 | `procedural-judgment-responsibility.md`、`read-routing-map.md` | 已概念卡化/已联读约束 | 名义程序不等于有效程序，开放断言不得实际处置 |\n",
        "| 可见性偏误、不透明区分、弱信号保护、AI 现实验证 | `visibility-opacity-weak-signals.md`、`malicious-compliance-ai-validation.md` | 已概念卡化 | AI 文本和漂亮格式不等于现实核验 |\n",
        "| 无制度基础设施、无法退出、复杂创伤 | `no-institution-middle-path.md`、`trapped-subject-trauma-baseline.md` | 已概念卡化 | 不强行模拟制度，不要求不可退出者完成理想退出 |\n",
        "| 爱的生成事件位置 | `love-generative-action.md`、`love-open-action.md` | 已概念卡化 | 爱既不能神化，也不能被塞进解释失败的剩余 |\n",
        "| 隐喻漂移、知识谱系、规范性前提 | `metaphor-source-transparency.md`、`v3-term-fidelity.md` | 已概念卡化/后台保真 | 隐喻不承担强判断，价值前提必须公开 |\n",
        "| 使用门槛债、工具化、商业化、分裂协议 | `accessibility-toolization-split.md` | 已概念卡化 | 防止框架变成专家垄断、产品交付压力或解释权不平等 |\n",
        "| 阶段 6、熵增、观测递归收束 | `observation-entropy-contraction.md`、`high-reflexivity-protocol.md` | 已概念卡化/已协议化 | 不能无限追踪，也不能用阶段/熵增包装不作为 |\n\n",
        "## 联读包覆盖计数\n\n",
        "| 联读包 | 章节节点数 | 说明 |\n",
        "| --- | ---: | --- |\n",
    ]
    for bundle_id, count in by_bundle.items():
        bundle = BUNDLE_DEFS[bundle_id]
        lines.append(f"| `{bundle_id}` | {count} | {bundle['summary']} |\n")
    lines.extend(
        [
            "\n## 判定结论\n\n",
            "当前补全标准不是复制 v3.0 全文，而是让每个重要板块都有可追踪入口：普通使用走轻流程，高风险概念走概念卡和保真检查，连续板块走联读包和源结构连续性检查，深水区走专项 protocol 与 worksheet。\n",
        ]
    )
    path.write_text("".join(lines), encoding="utf-8")


def write_change_rationale(crossframe: Path, patch_docx: Path | None, patch_paragraphs: list[str]) -> None:
    path = crossframe / "references" / "v3-change-rationale-from-patch.md"
    section_titles = [p for p in patch_paragraphs if re.match(r"^[一二三四五六七八九十百]+、", p)]
    lines = [
        "# v3.0 变更依据：2.0 压力测试补丁稿\n\n",
        "本文件把 `补丁稿.docx` 作为 v2.0 到 v3.0 的变更说明使用。补丁稿不是新的独立理论源；v3.0 DOCX 是当前权威源。这里记录补丁稿提出的问题意识如何进入 v3.0 的联读包和概念卡。\n\n",
    ]
    if patch_docx:
        lines.append(f"- 补丁来源：`{patch_docx.name}`\n")
    lines.append(f"- 补丁非空段落：{len(patch_paragraphs)}\n")
    lines.append(f"- 识别到的补丁章节：{len(section_titles)}\n\n")
    lines.extend(
        [
            "## 变更主线\n\n",
            "- 框架也要被框架外部审计，不能用自己的语言证明自己的安全。\n",
            "- 共识、反馈、证伪、保护和复核必须机制化，不能停留在声明。\n",
            "- 越高责任、越高权力、越高反身性的场景，越要防止合规地作恶。\n",
            "- 看见问题不等于看见全部问题，沉默、缺席、不透明和无法退出都要作为信号。\n",
            "- 爱、健康、透明、承接和不浪费爱是框架公开承担的规范前提，不应伪装成纯经验结论。\n",
            "- 框架的最终目标不是让使用者永远依赖框架，而是让判断更负责；当其他方法更能保护现实，框架应允许自己降级、转接或退场。\n\n",
            "## 补丁到 v3.0 的承接\n\n",
            "| 补丁主题 | v3.0 承接位置 | 必须联读包 |\n",
            "| --- | --- | --- |\n",
        ]
    )
    mapping = [
        ("框架自诊与版本治理", "第十六章：框架自诊与版本治理协议", "`v3-framework-governance-falsification-pack`"),
        ("共识程序具体化", "第十七章：共识程序具体化规则", "`v3-procedural-judgment-pack`"),
        ("根假设证伪与暂停使用", "第十八章：根假设证伪与暂停使用协议", "`v3-framework-governance-falsification-pack`"),
        ("案例库与幸存者偏差", "第十九章：案例库与幸存者偏差登记", "`v3-framework-governance-falsification-pack`"),
        ("跨尺度迁移的前概念闸", "第二十章：跨尺度迁移的前概念闸", "`v3-concept-migration-metaphor-pack`"),
        ("概念有效性", "第二十一章：概念有效性分级", "`v3-procedural-judgment-pack`"),
        ("可见性偏误与缺席信号", "第二十二章：可见性偏误与缺席信号检查", "`v3-evidence-visibility-pack`"),
        ("正当不透明与压制性不透明", "第二十三章：正当不透明与压制性不透明区分", "`v3-evidence-visibility-pack`"),
        ("阶段6与熵增", "第二十四章：阶段6与熵增的操作边界", "`v3-observation-entropy-contraction-pack`"),
        ("观测递归扩张与收束", "第二十五章：观测递归扩张与收束元规则", "`v3-observation-entropy-contraction-pack`"),
        ("恶意合规与选择性证据", "第二十六章：恶意合规与选择性证据审计", "`v3-power-capture-malicious-compliance-pack`"),
        ("AI 诊断的现实验证边界", "第二十七章：AI 诊断的现实验证边界", "`v3-evidence-visibility-pack`、`v3-power-capture-malicious-compliance-pack`"),
        ("弱信号保护机制", "第二十八章：弱信号保护机制", "`v3-evidence-visibility-pack`"),
        ("无制度基础设施场景", "第二十九章：无制度基础设施场景的中间路径", "`v3-no-institution-middle-path-pack`"),
        ("无法退出主体保护", "第三十章：无法退出主体保护协议", "`v3-trapped-trauma-baseline-pack`"),
        ("复杂创伤与无健康基准", "第三十一章：复杂创伤与无健康基准场景", "`v3-trapped-trauma-baseline-pack`"),
        ("爱与开放性承担行动", "第三十二章：爱与开放性承担行动的解释位置", "`v3-love-generative-action-pack`"),
        ("规范性前提声明", "第三十三章：规范性前提声明", "`v3-concept-migration-metaphor-pack`"),
        ("隐喻漂移控制", "第三十四章：隐喻漂移控制规则", "`v3-concept-migration-metaphor-pack`"),
        ("知识谱系与来源透明", "第三十五章：知识谱系与来源透明规则", "`v3-concept-migration-metaphor-pack`"),
        ("使用门槛债与可及性", "第三十六章：使用门槛债与可及性审计", "`v3-toolization-accessibility-pack`"),
        ("工具化、商业化与分裂", "第三十七章：框架工具化、商业化与分裂风险协议", "`v3-toolization-accessibility-pack`"),
        ("开放断言被权力捕获", "第三十八章：开放断言被权力捕获后的退场规则", "`v3-procedural-judgment-pack`"),
        ("框架良性消亡", "第三十九章：框架良性消亡与替代框架接口", "`v3-framework-governance-falsification-pack`"),
    ]
    for row in mapping:
        lines.append("| " + " | ".join(row) + " |\n")
    lines.append("\n## 使用边界\n\n补丁稿只能帮助理解 v3.0 为什么新增这些保护模块；实际推理时以 `v3-source-spine.md`、`v3-section-digest-index.md`、`v3-term-fidelity.md` 和 `continuity-bundles.md` 为准。\n")
    path.write_text("".join(lines), encoding="utf-8")


def write_continuity_bundles(crossframe: Path) -> None:
    path = crossframe / "references" / "continuity-bundles.md"
    lines = [
        "# 连续联读包\n\n",
        "本文件规定哪些 CrossFrame 源章节和概念不能孤立读取。v3.0 继承 v2.0 的诊断主线，并新增框架治理、证伪、可见性、弱信号、工具化和退场等保护模块。\n\n",
        "使用规则：先按 `read-routing-map.md` 找到任务路由，再按本文件读取联读包。若任务触发联读包却只读了单张概念卡，必须补读或降档。\n\n",
        "| 联读包 ID | 中文名 | 触发场景 | 必须同读材料 | 硬失败 |\n",
        "| --- | --- | --- | --- | --- |\n",
    ]
    for bundle_id, bundle in BUNDLE_DEFS.items():
        lines.append(f"| `{bundle_id}` | {bundle['name']} | {bundle['summary']} | {bundle['must']} | {bundle['failure']} |\n")
    lines.extend(
        [
            "\n## v3.0 必须联读的高风险组合\n\n",
            "- 开放断言 + 组织处置/名誉/资源/档案：读 `v3-procedural-judgment-pack`，确认是否已经被权力捕获并需要退场。\n",
            "- AI 报告/合规材料 + 公共或组织判断：读 `v3-evidence-visibility-pack` 与 `v3-power-capture-malicious-compliance-pack`，确认缺失材料和恶意合规风险。\n",
            "- 弱信号/沉默/无人反对：读 `v3-evidence-visibility-pack`，不得把缺席当成不存在。\n",
            "- 家庭/小团队/非正式关系 + 持续伤害：读 `v3-no-institution-middle-path-pack`，不要强行模拟制度，也不要完全停止判断。\n",
            "- 无法退出/依赖/被控制：读 `v3-trapped-trauma-baseline-pack`，优先安全、代理保护和最小自主。\n",
            "- 爱/照护/牺牲 + 结构解释：读 `v3-love-generative-action-pack` 和 `intimate-love-care-pack`，同时记录结构解释线与生成事件线。\n",
            "- 跨域隐喻/经典参照/理论上升：读 `v3-concept-migration-metaphor-pack`，标注隐喻身份、相似点、不相似点和误用风险。\n",
            "- 框架产品化/课程化/AI 工具化：读 `v3-toolization-accessibility-pack`，检查使用门槛债和解释权不平等。\n",
            "- 长期追踪/高反身对象/阶段 6：读 `v3-observation-entropy-contraction-pack`，写清扩张、收束、停止追踪和降档条件。\n",
            "- 框架自身是否失效：读 `v3-framework-governance-falsification-pack`，不得用 CrossFrame 自证 CrossFrame。\n\n",
            "## 降档规则\n\n",
            "- 未完成必须联读：不能输出强判断。\n",
            "- 影响权利、名誉、资源、处罚、公共记忆：若缺少程序与判断责任包，必须暂停强判断。\n",
            "- AI 缺失材料超过三项：只能输出轻量观察、问题清单或保护性开放断言。\n",
            "- 无制度基础设施但风险持续：允许保护性开放断言和低风险动作，不做公开定性。\n",
            "- 无法退出主体：行动建议先保护安全和选择空间，不要求高风险对抗。\n",
        ]
    )
    path.write_text("".join(lines), encoding="utf-8")


def write_v3_term_fidelity(crossframe: Path) -> None:
    path = crossframe / "references" / "v3-term-fidelity.md"
    rows = [
        ("框架自诊", "框架也要被诊断", "框架自我辩护", "区分文档、概念、实践、共同体对象；开放外部反例入口"),
        ("版本治理", "解释权、合并权、发布权、回滚权的安排", "只是版本号", "写明谁能改、谁能反对、如何回滚"),
        ("根假设证伪", "根假设可降级、暂停、竞争、退出", "理论自毁或护短", "反例重复出现时登记、降档或转接"),
        ("共识程序", "异议能安全进入并影响写回", "所有人同意", "检查材料公开、异议记录、少数意见保留"),
        ("概念有效性分级", "E0-E4 决定概念能承担多重判断责任", "术语等级炫耀", "处置级概念必须有申诉、复核、补偿和撤回"),
        ("可见性偏误", "看不见也是需要解释的信号", "沉默就是没事", "检查锚点、反馈、冲突、修复、退出和语言缺席"),
        ("正当不透明", "保护性/功能性/压制性不透明要区分", "透明永远正确或不透明永远合理", "追问保护谁、谁受益、谁能复核、何时解除"),
        ("恶意合规", "形式合规中继续制造伤害", "只是程序瑕疵", "超过三项风险信号时降档，超过五项标高风险"),
        ("AI 现实验证边界", "AI 只能说明材料内判断，不能证明现实已诊断", "AI 报告即调查", "列缺失材料清单，缺失过多只能轻量观察"),
        ("弱信号保护六件套", "弱信号要有通道、承接、反报复和写回", "提醒善良即可", "没有机制只能说意识到风险，不能说已保护"),
        ("无制度基础设施中间路径", "无正式程序但风险持续时的保护性判断", "模拟制度或完全不判断", "输出保护性开放断言、记录、外部支持和升级/撤回条件"),
        ("无法退出主体", "不可退出条件下减少伤害、保存主体性", "要求理想退出", "安全、代理保护、最小自主、低暴露记录、替代出口"),
        ("复杂创伤/无健康基准", "从未健康时目标是首次建立", "恢复到原本健康状态", "先问最低安全、可预测支持和小信任体验"),
        ("爱的生成事件", "爱是可追踪的新结构事件", "解释失败的剩余或神秘命令", "同时走结构解释线和生成事件线"),
        ("规范性前提", "公开承担价值边界", "价值中立工具", "承认保护弱信号、不取消责任、不浪费爱等前提"),
        ("隐喻漂移", "隐喻只是观察入口", "跨域规律证明", "标注身份、相似点、不相似点、停止使用条件"),
        ("知识谱系透明", "说明思想亲缘和改造边界", "吞并所有理论", "说明保留什么、改造什么、放弃什么"),
        ("使用门槛债", "复杂框架带来学习、翻译、证据、复核、退出和身份债", "越复杂越安全", "保留轻量安全用法和可及性审计"),
        ("工具化/商业化红线", "产品化不能压缩反俘获和复核", "付费交付等于有效", "禁止把 AI 输出、内部认证、客户满意当外部复核"),
        ("开放断言退场", "被实际用于处置时必须停止作为开放断言", "继续观察即可", "声明不得继续处置，标注误用，进入修复补偿和责任链"),
        ("框架良性消亡", "在局部范围允许降级、转接或退场", "框架失败的羞耻", "说明判断到哪里、哪里失效、外部框架接管什么"),
    ]
    lines = [
        "# v3.0 术语保真表\n\n",
        "本文件补充 v3.0 新增概念的保真边界。它与 `v2-term-fidelity.md` 并行：v2 表保留核心诊断概念，v3 表负责框架治理、证伪、现实保护、可见性、工具化和退场模块。\n\n",
        "## 使用规则\n\n",
        "- v3.0 是当前权威源；v2.0 保留为历史基线。\n",
        "- 涉及本表概念时，必须检查 `continuity-bundles.md` 的 v3 联读包。\n",
        "- v3 概念多为保护性约束，不能当作新术语装饰前台输出。\n",
        "- 若本表概念承担高责任判断，必须优先降档和列缺失材料，而不是提高结论强度。\n\n",
        "| v3.0 概念 | skill 压缩表达 | 不可误读为 | 证据要求与修复动作 |\n",
        "| --- | --- | --- | --- |\n",
    ]
    for row in rows:
        lines.append("| " + " | ".join(row) + " |\n")
    path.write_text("".join(lines), encoding="utf-8")


def concept_card(title: str, body: dict[str, str]) -> str:
    return (
        f"# {title}\n\n"
        f"## 概念原义\n\n{body['meaning']}\n\n"
        f"## 触发场景\n\n{body['trigger']}\n\n"
        f"## 不可误读边界\n\n{body['boundary']}\n\n"
        f"## 必须联读内容\n\n{body['bundle']}\n\n"
        f"## 证据要求\n\n{body['evidence']}\n\n"
        f"## 失败样式\n\n{body['failure']}\n\n"
        f"## 输出时的人话翻译\n\n{body['plain']}\n"
    )


def write_concept_cards(crossframe: Path) -> None:
    cards = {
        "framework-governance-falsification.md": (
            "框架治理与证伪",
            {
                "meaning": "框架本身也要接受诊断、反例登记、版本治理和暂停使用。成熟的框架不是解释一切，而是知道何时降级、转接或退场。",
                "trigger": "用户追问 CrossFrame 是否完整、是否失真、是否能被证伪、是否被商业化/共同体/AI 使用方式扭曲，或某类案例反复让框架误判。",
                "boundary": "不能用框架自己的概念证明框架安全；也不能把外部批评一概视为误解。",
                "bundle": "`v3-framework-governance-falsification-pack`；必要时联读 `framework-use-discipline-pack`。",
                "evidence": "需要反例类别、重复频率、误伤后果、替代解释、替代框架成本和是否存在版本写回机制。",
                "failure": "为了保住框架不断扩张定义；把使用者共同体、商业产品或 AI 输出当成框架有效性的证据。",
                "plain": "先承认：这个框架也可能不好用。再说明它在哪里还能判断，哪里应该停下，哪里要让别的方法接手。",
            },
        ),
        "procedural-judgment-responsibility.md": (
            "程序与判断责任",
            {
                "meaning": "共识、概念分级和开放断言都必须进入程序责任：异议能否进入、判断能否撤回、处置是否有申诉和补偿。",
                "trigger": "涉及处分、名誉、资格、资源、公共记忆、组织标签、平台申诉、开放断言被长期引用。",
                "boundary": "名义程序不是有效程序；开放断言不能因为措辞温和就被实际用于处置。",
                "bundle": "`v3-procedural-judgment-pack` 和 `judgment-responsibility-pack`。",
                "evidence": "需要材料公开程度、异议入口、少数意见记录、反向条件、复核独立性、申诉是否曾改变结果。",
                "failure": "把“我们已经讨论过”当共识，把“先观察”变成长期排斥或资源剥夺。",
                "plain": "这不是有没有流程的问题，而是这个流程能不能让反对意见真的改变结果。",
            },
        ),
        "visibility-opacity-weak-signals.md": (
            "可见性、不透明与弱信号",
            {
                "meaning": "沉默、缺席和不透明本身可能是结构信号；弱信号要有安全入口、独立承接和写回证明。",
                "trigger": "用户材料里出现“没人反对”“没有记录”“大家都满意”“信息不公开”“弱者不说话”。",
                "boundary": "不能把缺席直接当作不存在，也不能把所有不透明都视为压制；要区分保护性、功能性和压制性不透明。",
                "bundle": "`v3-evidence-visibility-pack`；公共或组织场景追加 `public-power-governance-pack`。",
                "evidence": "看谁有发声风险、反馈通道是否安全、谁能复核不透明、弱信号采纳后是否改变规则/资源/记录。",
                "failure": "总体满意度覆盖边缘主体恶化；匿名反馈交给被质疑权力链处理；反馈后发生报复却不登记。",
                "plain": "没有人说，不等于没有事；有时候正因为说了会更危险，问题才看起来很安静。",
            },
        ),
        "malicious-compliance-ai-validation.md": (
            "恶意合规与 AI 现实验证",
            {
                "meaning": "高权力对象可能选择性遵守格式，同时操纵证据、压制弱信号。AI 能整理材料，但不能验证现实保护和委托方诚信。",
                "trigger": "漂亮报告、AI 调查、合规总结、机构自评、申诉复核材料、程序完整但结果从不改变。",
                "boundary": "格式完整不等于程序有效；材料一致不等于事实一致；AI 报告不是独立调查。",
                "bundle": "`v3-power-capture-malicious-compliance-pack`、`v3-evidence-visibility-pack`。",
                "evidence": "列原始证据、受影响者反馈、外部复核、申诉采纳记录、证据链控制方和 AI 是否参与筛选改写。",
                "failure": "把委托方摘要当完整证据链；把 AI 的流畅文字当调查勇气；用结构语言解释为什么不能追责。",
                "plain": "报告写得越漂亮，越要问：原始材料在哪里，谁没被问到，说真话的人安全吗？",
            },
        ),
        "no-institution-middle-path.md": (
            "无制度基础设施中间路径",
            {
                "meaning": "家庭、小团队、亲密关系和临时社群没有正式复核机制，但持续伤害不能因此被悬置。",
                "trigger": "没有委托方、复核者、申诉记录或正式程序，但存在长期单向消耗、依赖、控制、声誉或安全风险。",
                "boundary": "不强行模拟不存在的制度；不要求受影响者冒险收集完整证据；不输出公开定性。",
                "bundle": "`v3-no-institution-middle-path-pack`，亲密场景追加 `intimate-love-care-pack`。",
                "evidence": "记录持续模式、低暴露事实、风险信号、外部支持、下一轮升级/撤回条件。",
                "failure": "因为无法复核就说什么都不能判断；或者把保护性判断升级为惩罚和公开定性。",
                "plain": "现在不适合证明谁错，但可以先保护自己、留下记录、减少暴露，并观察下一轮信号。",
            },
        ),
        "trapped-subject-trauma-baseline.md": (
            "无法退出主体与无健康基准",
            {
                "meaning": "某些主体事实上无法退出；某些系统从未有过健康基准。此时诊断目标是减少伤害、保存主体性、首次建立最低安全。",
                "trigger": "儿童、严重依赖者、经济被控制者、被监禁者、照护绑定者、创伤性家庭/组织/关系。",
                "boundary": "不能把无法退出解释为忠诚、成熟、牺牲或大局意识；不能要求回到从未存在过的健康状态。",
                "bundle": "`v3-trapped-trauma-baseline-pack` 和 `intimate-love-care-pack`。",
                "evidence": "看安全风险、代理保护、最小自主、信息空间、记录能力、支持连接、可重复的小信任体验。",
                "failure": "让低资源主体承担高风险对抗；把创伤性生存策略直接当缺陷；要求受伤者完成修复责任。",
                "plain": "如果一个人根本走不了，建议就不能写成“你离开就好了”。先要让他少受伤、多一点选择。",
            },
        ),
        "love-generative-action.md": (
            "爱的生成事件",
            {
                "meaning": "爱不是既有结构解释不了的剩余，而是一类不能由既有结构充分推出、但出现后可以追踪其后果的生成事件。",
                "trigger": "分析爱、照护、牺牲、公共承诺、超出利益计算的承担行动，或用户担心框架把爱还原掉。",
                "boundary": "不能神化爱，也不能把爱变成忍耐命令；不能只在利益/恐惧解释失败后才谈爱。",
                "bundle": "`v3-love-generative-action-pack` 和 `intimate-love-care-pack`。",
                "evidence": "同时记录结构解释线和生成事件线：真实成本、新通道、新记忆、新责任分配、新修复能力和新承接者。",
                "failure": "用爱要求低权力主体继续承担不可持续成本；或把开放行动说成不可分析的神秘性。",
                "plain": "爱不是让一个人一直扛，而是看这个行动有没有真的打开新的可能、留下新的承接。",
            },
        ),
        "metaphor-source-transparency.md": (
            "隐喻漂移与来源透明",
            {
                "meaning": "跨域隐喻、经典参照和理论来源要标注身份：隐喻、类比、机制候选、经验旁证、形式模型或操作规则。",
                "trigger": "文章概念上升、引经据典、使用物理/生物/历史/心理/系统论隐喻，或说明知识谱系。",
                "boundary": "像某种现象，不等于遵循某种规律；思想亲缘不等于来源吞并；规范性前提不能伪装成事实结论。",
                "bundle": "`v3-concept-migration-metaphor-pack` 和 `expression-article-pack`。",
                "evidence": "写相似点、不相似点、误用风险、停止使用条件；直接引用必须可核验，不确定时只做意译或思想映射。",
                "failure": "堆名人名言、伪造引用、用自然科学概念直接证明社会判断、引用接管现实证据。",
                "plain": "这个比喻只是帮我们看问题，不是替我们证明问题。",
            },
        ),
        "accessibility-toolization-split.md": (
            "使用门槛债、工具化与分裂协议",
            {
                "meaning": "框架越复杂越有保护力，也越容易制造专家垄断、身份债、商业交付压力和解释权不平等。",
                "trigger": "课程、咨询产品、AI 工具、组织管理软件、认证体系、公开评价标准或不同使用者分歧。",
                "boundary": "不得把轻量模板包装成完整诊断；不得把内部培训认证包装成外部复核；分裂不等于背叛。",
                "bundle": "`v3-toolization-accessibility-pack` 和 `framework-use-discipline-pack`。",
                "evidence": "检查学习债、翻译债、证据债、复核债、退出债、身份债，以及付费方是否控制证据入口和发布口径。",
                "failure": "为了产品交付强行输出强诊断；用客户满意度证明框架有效；让“懂框架的人”垄断解释权。",
                "plain": "框架不该变成只有少数人会用的新门槛；越复杂，越要给普通人安全的轻量用法。",
            },
        ),
        "observation-entropy-contraction.md": (
            "观测收束与熵增边界",
            {
                "meaning": "观测递归可以扩张，但必须有收束规则；阶段 6 和熵增只能通过操作指标判断，不能成为宿命或不作为理由。",
                "trigger": "高反身性对象、持续表演反制、长期跟踪、阶段 6、熵增、越修越坏、修复滞后。",
                "boundary": "不能无限追踪反应；不能用“势场不可对抗”“结构性熵增”“阶段如此”包装不作为。",
                "bundle": "`v3-observation-entropy-contraction-pack` 和 `long-evolution-deep-pack`。",
                "evidence": "看发现滞后、修复滞后、复发率、修复副产品、负荷分布；登记何时扩张、何时收束、何时停止追踪。",
                "failure": "对象利用诊断规则伪造证据、拖延、反击或压制弱信号；诊断收益低于扰动和暴露风险。",
                "plain": "不能因为问题很复杂就一直追下去；如果追踪只让人更危险、判断更混乱，就要停下来降档。",
            },
        ),
    }
    folder = crossframe / "references" / "concept-cards"
    for filename, (title, body) in cards.items():
        (folder / filename).write_text(concept_card(title, body), encoding="utf-8")


def update_concept_card_readme(crossframe: Path) -> None:
    path = crossframe / "references" / "concept-cards" / "README.md"
    text = path.read_text(encoding="utf-8")
    marker = "## 固定阅读顺序"
    insert = (
        "| 框架治理 / 证伪 / 良性消亡 | `framework-governance-falsification.md` | 判断框架是否失效、是否需要暂停、降级、转接或退场 |\n"
        "| 程序与判断责任 / 开放断言退场 | `procedural-judgment-responsibility.md` | 共识程序、强判断、开放断言被实际处置化 |\n"
        "| 可见性 / 不透明 / 弱信号 | `visibility-opacity-weak-signals.md` | 沉默、缺席、匿名反馈、不透明材料、弱信号安全 |\n"
        "| 恶意合规 / AI 现实验证 | `malicious-compliance-ai-validation.md` | 漂亮报告、AI 合规文本、选择性证据、机构自评 |\n"
        "| 无制度基础设施中间路径 | `no-institution-middle-path.md` | 家庭、小团队、非正式关系中无正式复核但风险持续 |\n"
        "| 无法退出主体 / 复杂创伤 / 无健康基准 | `trapped-subject-trauma-baseline.md` | 儿童、依赖者、不可退出主体、初建型修复 |\n"
        "| 爱的生成事件 | `love-generative-action.md` | 爱不是解释失败的剩余，而是可追踪的新结构事件 |\n"
        "| 隐喻漂移 / 来源透明 / 规范性前提 | `metaphor-source-transparency.md` | 概念上升、引经据典、跨域隐喻、知识谱系说明 |\n"
        "| 使用门槛债 / 工具化 / 分裂协议 | `accessibility-toolization-split.md` | 课程、咨询、AI 工具、认证、商业化和分支分歧 |\n"
        "| 观测收束 / 熵增边界 | `observation-entropy-contraction.md` | 高反身性追踪、阶段 6、熵增和必须停止追踪的场景 |\n"
    )
    if "framework-governance-falsification.md" not in text and marker in text:
        text = text.replace(marker, insert + "\n" + marker)
    text = text.replace("这些概念在 v2.0 中承担关键判断作用", "这些概念在 v3.0 中承担关键判断作用")
    path.write_text(text, encoding="utf-8")


def update_read_routing(crossframe: Path, version: str) -> None:
    path = crossframe / "references" / "read-routing-map.md"
    old = path.read_text(encoding="utf-8")
    tail_marker = "## 高风险概念触发"
    tail_idx = old.find(tail_marker)
    tail = old[tail_idx:] if tail_idx >= 0 else ""
    lines = [
        "# 读取路由图\n\n",
        "本文件决定一次 CrossFrame 调用应该读取哪些材料。默认先读最少必要内容；当概念承担判断作用时，再加载完整概念卡、保真材料和必要的连续联读包。\n\n",
        f"当前权威源为 `{version}.0`。`v2.0` 文件保留为历史基线；默认连续性检查读取 `v3-source-spine.md`、`v3-section-digest-index.md`、`v3-coverage-map.md` 与 `v3-term-fidelity.md`。当某个概念属于 v3.0 连续板块时，不得只读单个 protocol 或 concept card。\n\n",
        "## 联读包索引\n\n",
        "| 联读包 ID | 中文名 | 何时强制读取 |\n",
        "| --- | --- | --- |\n",
    ]
    for bundle_id, bundle in BUNDLE_DEFS.items():
        lines.append(f"| `{bundle_id}` | {bundle['name']} | {bundle['summary']} |\n")
    rows = [
        ("快速诊断", "`protocols/diagnosis-protocol.md`、核心 worksheets、`templates/quick-diagnosis-output.md`", "涉及高风险概念时读对应概念卡", "`diagnosis-mainline-pack`"),
        ("完整诊断 / 审计 / 深度分析", "`protocols/diagnosis-protocol.md`、全部核心 worksheets、`templates/full-diagnosis-output.md`、`references/v3-term-fidelity.md`", "`references/diagnostic-dimensions.md`、`references/diagnostic-toolbox-index.md`、`references/v3-source-spine.md`、`references/v3-section-digest-index.md`", "`diagnosis-mainline-pack`、`framework-use-discipline-pack`"),
        ("开放断言", "`protocols/open-assertion-protocol.md`、`worksheets/open-assertion-record.md`、`references/concept-cards/open-assertion.md`", "`references/concept-cards/procedural-judgment-responsibility.md`", "`judgment-responsibility-pack`、`v3-procedural-judgment-pack`"),
        ("强判断 / 资格名誉资源权利", "`protocols/proposition-verification-protocol.md`、`worksheets/proposition-verification.md`、`worksheets/prospective-registration.md`", "`protocols/anti-capture-protocol.md`、`references/concept-cards/procedural-judgment-responsibility.md`", "`judgment-responsibility-pack`、`v3-procedural-judgment-pack`、`v3-evidence-visibility-pack`"),
        ("AI 合规 / 漂亮报告 / 机构自评", "`references/concept-cards/malicious-compliance-ai-validation.md`、`references/concept-cards/visibility-opacity-weak-signals.md`", "`protocols/anti-capture-protocol.md`、`references/concept-cards/evidence-cost.md`", "`v3-power-capture-malicious-compliance-pack`、`v3-evidence-visibility-pack`、`framework-use-discipline-pack`"),
        ("弱信号 / 沉默 / 缺席 / 不透明", "`references/concept-cards/visibility-opacity-weak-signals.md`、`references/concept-cards/evidence-cost.md`", "`protocols/public-institution-protocol.md` 或 `protocols/intimate-relationship-protocol.md`", "`v3-evidence-visibility-pack`"),
        ("无制度基础设施 / 家庭小团队 / 非正式关系", "`references/concept-cards/no-institution-middle-path.md`、`protocols/low-condition-action-protocol.md`", "`protocols/intimate-relationship-protocol.md`、`templates/open-assertion-output.md`", "`v3-no-institution-middle-path-pack`、`intimate-love-care-pack`"),
        ("无法退出 / 复杂创伤 / 无健康基准", "`references/concept-cards/trapped-subject-trauma-baseline.md`、`protocols/healing-transfer-protocol.md`", "`references/concept-cards/exit-transfer.md`、`references/concept-cards/repair-byproduct.md`", "`v3-trapped-trauma-baseline-pack`、`intimate-love-care-pack`"),
        ("爱 / 照护 / 牺牲 / 开放行动", "`references/concept-cards/love-generative-action.md`、`references/concept-cards/love-open-action.md`", "`references/concept-cards/responsibility-chain.md`、`references/concept-cards/repair-byproduct.md`", "`v3-love-generative-action-pack`、`intimate-love-care-pack`"),
        ("隐喻 / 引经据典 / 来源透明 / 规范性前提", "`references/concept-cards/metaphor-source-transparency.md`、`references/v3-term-fidelity.md`", "`../crossframe-essay/protocols/concept-elevation-protocol.md`", "`v3-concept-migration-metaphor-pack`、`expression-article-pack`"),
        ("工具化 / 商业化 / 课程 / AI 工具 / 认证", "`references/concept-cards/accessibility-toolization-split.md`、`references/framework-ontology-protection.md`", "`references/v3-change-rationale-from-patch.md`", "`v3-toolization-accessibility-pack`、`framework-use-discipline-pack`"),
        ("阶段 6 / 熵增 / 观测递归 / 高反身追踪", "`references/concept-cards/observation-entropy-contraction.md`、`protocols/high-reflexivity-protocol.md`", "`protocols/lifecycle-diagnosis-protocol.md`、`references/theory-backend-index.md`", "`v3-observation-entropy-contraction-pack`、`long-evolution-deep-pack`"),
        ("框架是否失效 / 证伪 / 良性消亡", "`references/concept-cards/framework-governance-falsification.md`、`references/v3-change-rationale-from-patch.md`", "`references/v3-coverage-map.md`、`references/framework-ontology-protection.md`", "`v3-framework-governance-falsification-pack`"),
        ("公共制度 / 平台治理 / 公共承诺", "`protocols/public-institution-protocol.md`、`worksheets/public-institution-check.md`", "`references/concept-cards/malicious-compliance-ai-validation.md`、`references/concept-cards/visibility-opacity-weak-signals.md`", "`public-power-governance-pack`、`v3-evidence-visibility-pack`、`v3-power-capture-malicious-compliance-pack`"),
        ("文章 / 评论 / 可读输出", "`../crossframe-essay/SKILL.md`、`templates/user-facing-language.md`", "`references/v3-section-digest-index.md`、对应场景概念卡", "`expression-article-pack`、对应场景联读包"),
    ]
    lines.extend(["\n## 基础路由\n\n", "| 用户请求 | 必读 | 按需追加 | 连续联读包 |\n", "| --- | --- | --- | --- |\n"])
    for row in rows:
        lines.append("| " + " | ".join(row) + " |\n")
    lines.extend(
        [
            "\n## 连续联读执行规则\n\n",
            "- 只要上表的“连续联读包”不是空，就先读 `references/continuity-bundles.md`，确认同读材料和降档规则。\n",
            "- 深度、审计、高责任、公共制度、亲密关系、长期演化、框架治理和文章输出场景，必须按需读 `references/v3-source-spine.md` 或 `references/v3-section-digest-index.md`，确认原文相邻章节。\n",
            "- 若 v3.0 与 v2.0 的理解冲突，以 v3.0 为准；若需要追踪演化，再读取 `v2-source-spine.md`、`v2-section-digest-index.md` 和 `v3-change-rationale-from-patch.md`。\n",
            "- 输出前使用 `worksheets/source-continuity-check.md`：若发现只读了单张概念卡，且本文件要求联读，必须补读或降档。\n",
            "- `templates/reasoning-outline-output.md` 中的“本次连续联读包”只列包名，不展开完整工作表。\n\n",
        ]
    )
    if tail:
        tail = tail.replace("`references/v2-coverage-map.md`、`references/v2-source-spine.md`", "`references/v3-coverage-map.md`、`references/v3-source-spine.md`")
        tail = tail.replace("v2", "v3")
        lines.append(tail)
    path.write_text("".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate CrossFrame source continuity files from a DOCX.")
    parser.add_argument("--version", default="v3")
    parser.add_argument("--source-docx", default=r"D:\下载\跨尺度结构诊断框架v3.0.docx")
    parser.add_argument("--patch-docx", default=r"D:\下载\补丁稿.docx")
    parser.add_argument("--repo", default=".")
    args = parser.parse_args()

    version = args.version.lower()
    repo = Path(args.repo).resolve()
    crossframe = repo / "skills" / "crossframe"
    source_docx = Path(args.source_docx)
    patch_docx = Path(args.patch_docx) if args.patch_docx else None

    nonempty, headings = extract_headings(source_docx)
    prepare_headings(headings, version)
    patch_paragraphs = extract_patch_paragraphs(patch_docx)

    write_source_spine(crossframe, version, source_docx, nonempty, headings)
    write_digest(crossframe, version, source_docx, headings)
    write_coverage(crossframe, version, headings)
    write_change_rationale(crossframe, patch_docx, patch_paragraphs)
    write_continuity_bundles(crossframe)
    write_v3_term_fidelity(crossframe)
    write_concept_cards(crossframe)
    update_concept_card_readme(crossframe)
    update_read_routing(crossframe, version)

    print(f"generated {version} source continuity files")
    print(f"headings: {len(headings)}")
    print(f"patch paragraphs: {len(patch_paragraphs)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
