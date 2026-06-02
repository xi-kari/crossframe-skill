# v2.0 连续联读包

本文件规定哪些 2.0 原文板块不能被拆成孤立概念读取。它的目的不是增加输出术语，而是防止 agent 只读一张概念卡就下判断，丢掉原文的相邻约束、责任边界和降档规则。

使用顺序：

1. 先读 `read-routing-map.md` 判断任务路由。
2. 再读本文件，确认本次是否触发连续联读包。
3. 需要定位原文结构时，读 `v2-source-spine.md`；需要逐节摘要时，读 `v2-section-digest-index.md`。
4. 输出前用 `worksheets/source-continuity-check.md` 自检。

## 总规则

- 一旦某个概念承担判断作用，不只读取概念卡，还要读取它所属的连续联读包。
- 一旦判断影响名誉、权利、资源、处罚、公共记忆、亲密关系安全或组织处置，必须读取判断责任包。
- 一旦用户要求深度、审计、文章、公开表达或跨平台复用，必须读取表达与文章输出包。
- 若当前上下文不足以读取联读包，不得用孤立概念做强判断；应降为轻量观察、开放断言或低条件试探行动。

## 联读包

| 联读包 ID | 中文名 | 触发条件 | 必须同读 | 孤立读取风险 |
| --- | --- | --- | --- | --- |
| `framework-use-discipline-pack` | 框架使用纪律包 | 框架边界、概念武器化、模型替代专业、AI 合规材料、输出禁忌、适用性分级 | `framework-ontology-protection.md`、`guardrails.md`、`v2-term-fidelity.md`、`framework-boundary-protocol.md`、`framework-boundary-check.md` | 把 CrossFrame 用成万能审判、领域替代品或漂亮话合规工具 |
| `judgment-responsibility-pack` | 判断责任包 | 开放断言、强判断、名誉/权利/资源/处罚/公共记忆、反俘获、弱信号、申诉复核 | `open-assertion-protocol.md`、`proposition-verification-protocol.md`、`anti-capture-protocol.md`、`evidence-cost.md`、`judgment-grades.md`、`open-assertion-record.md`、`proposition-verification.md`、`prospective-registration.md` | 把可撤回判断包装成终局裁决，或用开放断言绕开命题验证 |
| `diagnosis-mainline-pack` | 诊断主线包 | 完整诊断、深度分析、组织/关系/制度反复失衡、机制候选、五闸、诊断维度 | `diagnosis-protocol.md`、`intake-worksheet.md`、`five-gates-worksheet.md`、`evidence-ledger.md`、`mechanism-candidates.md`、`diagnostic-dimensions.md`、`diagnostic-toolbox-index.md` | 只套机制标签，跳过对象、证据、尺度、责任和观测影响 |
| `intimate-love-care-pack` | 亲密关系/爱/照护包 | 亲密关系、家庭、朋友、照护、解释劳动、爱、牺牲、修复、疗愈、退出转移 | `intimate-relationship-protocol.md`、`healing-transfer-protocol.md`、`love-open-action.md`、`repair-byproduct.md`、`responsibility-chain.md`、`intimate-relationship-light-check.md`、`healing-transfer-map.md` | 把爱写成忍耐命令，把修复责任压回受伤者，或用结构词抹掉痛苦 |
| `public-power-governance-pack` | 公共制度与权力包 | 公共制度、平台治理、申诉、合规、公共承诺、权力封闭、低权力主体保护、公共评论 | `public-institution-protocol.md`、`anti-capture-protocol.md`、`governance-continuity-protocol.md`、`evidence-cost.md`、`power-closure.md`、`exit-transfer.md`、`public-institution-check.md`、`governance-continuity-check.md` | 把程序外观当有效程序，把 AI 文本当强证据，或忽略弱信号安全 |
| `long-evolution-deep-pack` | 长期演化深水区包 | 生命周期、阶段判断、递进闭环、势场、自主解离、治理连续性、文明/历史尺度、根假设 | `theory-backend-index.md`、`lifecycle-diagnosis-protocol.md`、`progression-protocol.md`、`field-dissociation-protocol.md`、`large-scale-stress-test-protocol.md`、`anchor-group.md`、`dynamics-group.md`、`structure-process-group.md` | 把阶段写成宿命，把势场写成氛围，把文明尺度写成绝对结论 |
| `expression-article-pack` | 表达与文章输出包 | 面向普通读者、文章、评论、思想文章、对外发布、管理/制度/技术语境翻译 | `expression-translation-protocol.md`、`expression-translation-table.md`、`user-facing-language.md`、`reasoning-outline-output.md`；文章任务再读 `../crossframe-essay/SKILL.md` | 后台推理存在但前台变成术语墙，或文章只剩概念姿态没有现实入口 |

## 必须联读的高风险组合

- `open-assertion.md` + 名誉/权利/处罚/资源：必须追加 `judgment-responsibility-pack`。
- `love-open-action.md` + 亲密关系/照护/解释劳动：必须追加 `intimate-love-care-pack`。
- `scale-transfer.md` + 个体痛苦/组织责任/公共事件：必须追加 `diagnosis-mainline-pack`，高权力场景再追加 `public-power-governance-pack`。
- `theory-backend-index.md` + 文明/历史/长期演化判断：必须追加 `long-evolution-deep-pack` 和超大规模压力测试。
- `public-institution-protocol.md` + 合规材料/平台申诉/机构自评：必须追加 `framework-use-discipline-pack` 和 `public-power-governance-pack`。
- `crossframe-essay` 成文：必须至少追加 `diagnosis-mainline-pack` 和 `expression-article-pack`；公共、亲密、组织或长期演化主题再追加对应场景包。

## 降档规则

若 agent 发现自己只读了单个概念卡，而本文件要求联读：

- 不能输出强判断。
- 不能把判断用于处置、公开定性或人格评价。
- 可以输出“轻量观察”或“开放断言”，但必须声明需要补读的联读包。
- 如果用户要求文章，必须在结构洞察底稿中标注“概念连续性缺口”，再决定是否成文。

