# 读取路由图

本文件决定一次 CrossFrame 调用应该读取哪些材料。默认先读最少必要内容；当概念承担判断作用时，再加载完整概念卡和保真材料。

## 基础路由

| 用户请求 | 必读 | 按需追加 |
| --- | --- | --- |
| 快速诊断 | `protocols/diagnosis-protocol.md`、`worksheets/intake-worksheet.md`、`worksheets/five-gates-worksheet.md`、`templates/quick-diagnosis-output.md` | 涉及高风险概念时读对应概念卡 |
| 完整诊断 / 审计 / 深度分析 | `protocols/diagnosis-protocol.md`、全部核心 worksheets、`templates/full-diagnosis-output.md`、`references/v2-term-fidelity.md` | `references/diagnostic-dimensions.md`、`references/diagnostic-toolbox-index.md` |
| 推演 / 后续走向 / 分支终点 | `protocols/inference-protocol.md`、`templates/inference-output.md`、`references/concept-cards/mechanism-candidates.md` | 尺度、反身性、权力封闭相关概念卡 |
| 开放断言 | `protocols/open-assertion-protocol.md`、`worksheets/open-assertion-record.md`、`templates/open-assertion-output.md`、`references/concept-cards/open-assertion.md` | `references/concept-cards/evidence-cost.md`、`references/concept-cards/judgment-grades.md` |
| 低条件行动 | `protocols/low-condition-action-protocol.md`、`references/concept-cards/low-condition-action.md` | `references/concept-cards/evidence-cost.md`、`references/concept-cards/judgment-grades.md` |
| 高责任 / 权力密度 / 处分 / 名誉 / 权利 / 公共记忆 | `protocols/anti-capture-protocol.md`、`worksheets/high-responsibility-check.md`、`references/concept-cards/power-closure.md`、`references/concept-cards/evidence-cost.md`、`references/concept-cards/judgment-grades.md` | `references/concept-cards/exit-transfer.md`、`references/diagnostic-toolbox-index.md` |
| 强判断 / 处置依据 / 资格名誉资源权利 | `protocols/proposition-verification-protocol.md`、`worksheets/proposition-verification.md`、`worksheets/prospective-registration.md`、`templates/strong-judgment-output.md` | `protocols/anti-capture-protocol.md`、`references/concept-cards/judgment-grades.md` |
| 高反身性 / 表演 / 反制 / 研究诊断规则 | `protocols/high-reflexivity-protocol.md`、`worksheets/reflexivity-state-transfer.md`、`templates/high-reflexivity-output.md` | `references/concept-cards/reflexivity.md`、`references/concept-cards/evidence-cost.md` |
| 亲密关系 / 家庭 / 照护 / 解释劳动 / 单方承接 | `protocols/intimate-relationship-protocol.md`、`worksheets/intimate-relationship-light-check.md`、`templates/intimate-relationship-output.md` | `references/concept-cards/love-open-action.md`、`references/concept-cards/repair-byproduct.md`、`references/concept-cards/responsibility-chain.md` |
| 疗愈 / 修复路线 / 退出转移 / 长期重建 | `protocols/healing-transfer-protocol.md`、`worksheets/healing-transfer-map.md`、`templates/healing-transfer-output.md` | `references/concept-cards/exit-transfer.md`、`references/concept-cards/repair-byproduct.md` |
| 公共制度 / 平台治理 / 公共承诺 / 高权力公共议题 | `protocols/public-institution-protocol.md`、`worksheets/public-institution-check.md`、`templates/public-institution-output.md` | `protocols/anti-capture-protocol.md`、`references/concept-cards/evidence-cost.md`、`references/concept-cards/power-closure.md` |
| 框架边界 / 万能理论 / 专业替代 / 概念武器化 | `protocols/framework-boundary-protocol.md`、`worksheets/framework-boundary-check.md`、`references/framework-ontology-protection.md`、`templates/framework-boundary-output.md` | `references/concept-cards/evidence-cost.md`、`protocols/anti-capture-protocol.md` |
| 生命周期 / 阶段判断 / 长期演化过程 | `protocols/lifecycle-diagnosis-protocol.md`、`worksheets/lifecycle-stage-record.md`、`templates/lifecycle-output.md` | `references/theory-backend-index.md`、`references/concept-cards/structure-process-group.md` |
| 递进模式 / 子锚点闭环 / 忙但没积累 | `protocols/progression-protocol.md`、`worksheets/sub-anchor-progression.md`、`templates/progression-output.md` | `references/concept-cards/anchor-group.md`、`references/concept-cards/structure-process-group.md` |
| 势场 / 沉积基本盘 / 自主解离 | `protocols/field-dissociation-protocol.md`、`worksheets/field-dissociation-check.md`、`references/field-management-and-dissociation.md`、`templates/field-dissociation-output.md` | `references/concept-cards/exit-transfer.md`、`references/concept-cards/repair-byproduct.md` |
| 治理连续性 / 偿付约束 / 多中心治理 / 承接者生成 | `protocols/governance-continuity-protocol.md`、`worksheets/governance-continuity-check.md`、`templates/governance-continuity-output.md` | `protocols/public-institution-protocol.md`、`references/theory-backend-index.md` |
| 超大规模圈层 / 文明尺度 / 历史尺度压力测试 | `protocols/large-scale-stress-test-protocol.md`、`worksheets/large-scale-stress-test.md`、`templates/large-scale-stress-output.md` | `references/theory-backend-index.md`、`references/concept-cards/scale-transfer.md` |
| 对外表达 / 说人话 / 管理制度技术语境翻译 | `protocols/expression-translation-protocol.md`、`references/expression-translation-table.md`、`templates/expression-translation-output.md`、`templates/user-facing-language.md` | 对应诊断协议和概念卡 |
| 概念解释 / 思想解释 / 某概念怎么看 | `protocols/concept-explanation-protocol.md`、`references/concepts-minimal-set.md`、`references/v2-term-fidelity.md`、`templates/concept-explanation-output.md` | 与概念相关的概念卡 |
| 爱、牺牲、照护、公共承诺 | `references/concept-cards/love-open-action.md`、`references/love-as-open-action.md` | `references/concept-cards/repair-byproduct.md`、`references/concept-cards/responsibility-chain.md` |
| 文明尺度 / 长期演化 / 制度生成 / 多中心治理 / 深层理论 | 对应专项协议 + `references/theory-backend-index.md` | `references/diagnostic-dimensions.md`、`references/diagnostic-toolbox-index.md`、`references/v2-coverage-map.md` |

## 高风险概念触发

| 触发词或判断动作 | 必读概念卡 |
| --- | --- |
| 证据、材料、报告、弱信号、AI 合规、自评 | `concept-cards/evidence-cost.md` |
| 机制、原因、解释候选、为什么反复 | `concept-cards/mechanism-candidates.md` |
| 档位、能否强判断、能否处置、能否公开 | `concept-cards/judgment-grades.md` |
| 退出、转移、外部承接、保护现场 | `concept-cards/exit-transfer.md` |
| 修复、副产品、复盘、道歉、承诺、合规 | `concept-cards/repair-byproduct.md` |
| 尺度升维、换层解释、大局、历史、制度 | `concept-cards/scale-transfer.md` |
| 被诊断后变化、表演、反制、策略反应 | `concept-cards/reflexivity.md` |
| 爱、牺牲、忍耐、照护、开放行动 | `concept-cards/love-open-action.md` |
| 预测、强判断、处置、申诉、复核 | `protocols/proposition-verification-protocol.md` |
| 关系、家庭、照护、边界、解释劳动 | `protocols/intimate-relationship-protocol.md` |
| 创伤、疗愈、重建、维护窗口 | `protocols/healing-transfer-protocol.md` |
| 公共承诺、平台治理、制度、分配回流 | `protocols/public-institution-protocol.md` |
| 万能解释、领域替代、人格审判、概念武器化 | `protocols/framework-boundary-protocol.md` |
| 锚点、保护变量、多层锚、跨域互操作、重锚定 | `concept-cards/anchor-group.md` |
| 启动、转译、让渡职责、支撑通道、条件场、环境势场 | `concept-cards/dynamics-group.md` |
| 行动承接、中层耗竭、高责任主体耗竭、结构负荷 | `concept-cards/structure-process-group.md` |
| 阶段、生命周期、回退、混合阶段 | `protocols/lifecycle-diagnosis-protocol.md` |
| 子锚点、递进、闭环、忙但没有积累 | `protocols/progression-protocol.md` |
| 势场、沉积基本盘、自主解离、保护性退出 | `protocols/field-dissociation-protocol.md` |
| 偿付、预警、多中心、承接者生成、代际承接 | `protocols/governance-continuity-protocol.md` |
| 文明、历史、超大规模、宏大结论、公共记忆 | `protocols/large-scale-stress-test-protocol.md` |
| 说人话、对外发布、管理语境、技术治理语境 | `protocols/expression-translation-protocol.md` |

## 输出路由

默认输出使用 `templates/reasoning-outline-output.md` 作为前置提纲。然后按任务选择：

- 快速诊断：`templates/quick-diagnosis-output.md`
- 完整诊断：`templates/full-diagnosis-output.md`
- 推演：`templates/inference-output.md`
- 开放断言：`templates/open-assertion-output.md`
- 概念解释：`templates/concept-explanation-output.md`
- 强判断：`templates/strong-judgment-output.md`
- 高反身性：`templates/high-reflexivity-output.md`
- 亲密关系轻量入口：`templates/intimate-relationship-output.md`
- 疗愈与转移：`templates/healing-transfer-output.md`
- 公共制度专项：`templates/public-institution-output.md`
- 框架边界：`templates/framework-boundary-output.md`
- 生命周期：`templates/lifecycle-output.md`
- 递进模式：`templates/progression-output.md`
- 势场与自主解离：`templates/field-dissociation-output.md`
- 治理连续性：`templates/governance-continuity-output.md`
- 超大规模压力测试：`templates/large-scale-stress-output.md`
- 对外表达翻译：`templates/expression-translation-output.md`

输出前必须读或内化 `templates/user-facing-language.md` 的表达闸。
