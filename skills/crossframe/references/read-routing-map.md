# 读取路由图

本文件决定一次 CrossFrame 调用应该读取哪些材料。默认先读最少必要内容；当概念承担判断作用时，再加载完整概念卡、保真材料和必要的连续联读包。

当前权威源为 `v3.0`。`v2.0` 文件保留为历史基线；默认连续性检查读取 `v3-source-spine.md`、`v3-section-digest-index.md`、`v3-coverage-map.md` 与 `v3-term-fidelity.md`。当某个概念属于 v3.0 连续板块时，不得只读单个 protocol 或 concept card。

## 联读包索引

| 联读包 ID | 中文名 | 何时强制读取 |
| --- | --- | --- |
| `framework-use-discipline-pack` | 框架使用纪律包 | 约束 CrossFrame 如何使用：防概念武器化、防教条化、防万能化、防 AI 文本替代证据。 |
| `judgment-responsibility-pack` | 判断责任包 | 约束开放断言、强判断、命题验证和高责任处置，防止可撤回判断被当成终局裁决。 |
| `diagnosis-mainline-pack` | 诊断主线包 | 保持对象、事实、尺度、机制候选、五闸、工具箱和诊断维度的连续主线。 |
| `intimate-love-care-pack` | 亲密关系/爱/照护包 | 处理关系、照护、爱、解释劳动和疗愈时，先保护痛苦、安全和边界。 |
| `public-power-governance-pack` | 公共制度与权力包 | 处理平台、制度、公共承诺、程序有效性、权力封闭和低权力主体保护。 |
| `long-evolution-deep-pack` | 长期演化深水区包 | 处理根假设、生命周期、递进、势场、自主解离、治理连续性和文明尺度压力测试。 |
| `expression-article-pack` | 表达与文章输出包 | 把后台概念翻译成人话、管理/制度/技术语境或文章输出，避免术语墙。 |
| `v3-framework-governance-falsification-pack` | 框架治理与证伪包 | 处理框架自诊、版本治理、根假设暂停、案例库偏差、框架良性消亡和替代框架接口。 |
| `v3-procedural-judgment-pack` | 程序与判断责任包 | 处理共识程序、概念有效性分级、强判断升级和开放断言被权力捕获后的退场。 |
| `v3-evidence-visibility-pack` | 证据可见性包 | 处理可见性偏误、缺席信号、正当/压制性不透明、弱信号保护和 AI 现实验证边界。 |
| `v3-power-capture-malicious-compliance-pack` | 权力捕获与恶意合规包 | 处理选择性证据、表演性合规、AI 合规幻觉和结构语言被用来洗白不作为。 |
| `v3-no-institution-middle-path-pack` | 无制度基础设施包 | 处理家庭、小团队、亲密关系、临时项目和非正式社群中没有正式复核但风险持续的场景。 |
| `v3-trapped-trauma-baseline-pack` | 无法退出与复杂创伤包 | 处理无法退出主体、复杂创伤、无健康基准、初建型修复和创伤建材型结构。 |
| `v3-love-generative-action-pack` | 爱与开放行动生成包 | 把爱定位为不能由既有结构充分推出、但出现后可被追踪的生成事件，而不是解释失败的剩余。 |
| `v3-concept-migration-metaphor-pack` | 概念迁移与隐喻控制包 | 处理跨尺度迁移前概念闸、隐喻漂移、规范性前提声明和知识谱系透明。 |
| `v3-toolization-accessibility-pack` | 工具化与可及性包 | 处理使用门槛债、可及性审计、商业化工具化风险、认证垄断和分支分裂协议。 |
| `v3-observation-entropy-contraction-pack` | 观测收束与熵增边界包 | 处理阶段 6、熵增操作边界、观测递归扩张条件和必须收束的元规则。 |

## 基础路由

| 用户请求 | 必读 | 按需追加 | 连续联读包 |
| --- | --- | --- | --- |
| 快速诊断 | `protocols/diagnosis-protocol.md`、核心 worksheets、`templates/quick-diagnosis-output.md` | 涉及高风险概念时读对应概念卡 | `diagnosis-mainline-pack` |
| 完整诊断 / 审计 / 深度分析 | `protocols/diagnosis-protocol.md`、全部核心 worksheets、`templates/full-diagnosis-output.md`、`references/v3-term-fidelity.md` | `references/diagnostic-dimensions.md`、`references/diagnostic-toolbox-index.md`、`references/v3-source-spine.md`、`references/v3-section-digest-index.md` | `diagnosis-mainline-pack`、`framework-use-discipline-pack` |
| 开放断言 | `protocols/open-assertion-protocol.md`、`worksheets/open-assertion-record.md`、`references/concept-cards/open-assertion.md` | `references/concept-cards/procedural-judgment-responsibility.md` | `judgment-responsibility-pack`、`v3-procedural-judgment-pack` |
| 强判断 / 资格名誉资源权利 | `protocols/proposition-verification-protocol.md`、`worksheets/proposition-verification.md`、`worksheets/prospective-registration.md` | `protocols/anti-capture-protocol.md`、`references/concept-cards/procedural-judgment-responsibility.md` | `judgment-responsibility-pack`、`v3-procedural-judgment-pack`、`v3-evidence-visibility-pack` |
| AI 合规 / 漂亮报告 / 机构自评 | `references/concept-cards/malicious-compliance-ai-validation.md`、`references/concept-cards/visibility-opacity-weak-signals.md` | `protocols/anti-capture-protocol.md`、`references/concept-cards/evidence-cost.md` | `v3-power-capture-malicious-compliance-pack`、`v3-evidence-visibility-pack`、`framework-use-discipline-pack` |
| 弱信号 / 沉默 / 缺席 / 不透明 | `references/concept-cards/visibility-opacity-weak-signals.md`、`references/concept-cards/evidence-cost.md` | `protocols/public-institution-protocol.md` 或 `protocols/intimate-relationship-protocol.md` | `v3-evidence-visibility-pack` |
| 无制度基础设施 / 家庭小团队 / 非正式关系 | `references/concept-cards/no-institution-middle-path.md`、`protocols/low-condition-action-protocol.md` | `protocols/intimate-relationship-protocol.md`、`templates/open-assertion-output.md` | `v3-no-institution-middle-path-pack`、`intimate-love-care-pack` |
| 无法退出 / 复杂创伤 / 无健康基准 | `references/concept-cards/trapped-subject-trauma-baseline.md`、`protocols/healing-transfer-protocol.md` | `references/concept-cards/exit-transfer.md`、`references/concept-cards/repair-byproduct.md` | `v3-trapped-trauma-baseline-pack`、`intimate-love-care-pack` |
| 爱 / 照护 / 牺牲 / 开放行动 | `references/concept-cards/love-generative-action.md`、`references/concept-cards/love-open-action.md` | `references/concept-cards/responsibility-chain.md`、`references/concept-cards/repair-byproduct.md` | `v3-love-generative-action-pack`、`intimate-love-care-pack` |
| 隐喻 / 引经据典 / 来源透明 / 规范性前提 | `references/concept-cards/metaphor-source-transparency.md`、`references/v3-term-fidelity.md` | `../crossframe-essay/protocols/concept-elevation-protocol.md` | `v3-concept-migration-metaphor-pack`、`expression-article-pack` |
| 工具化 / 商业化 / 课程 / AI 工具 / 认证 | `references/concept-cards/accessibility-toolization-split.md`、`references/framework-ontology-protection.md` | `references/v3-change-rationale-from-patch.md` | `v3-toolization-accessibility-pack`、`framework-use-discipline-pack` |
| 阶段 6 / 熵增 / 观测递归 / 高反身追踪 | `references/concept-cards/observation-entropy-contraction.md`、`protocols/high-reflexivity-protocol.md` | `protocols/lifecycle-diagnosis-protocol.md`、`references/theory-backend-index.md` | `v3-observation-entropy-contraction-pack`、`long-evolution-deep-pack` |
| 框架是否失效 / 证伪 / 良性消亡 | `references/concept-cards/framework-governance-falsification.md`、`references/v3-change-rationale-from-patch.md` | `references/v3-coverage-map.md`、`references/framework-ontology-protection.md` | `v3-framework-governance-falsification-pack` |
| 公共制度 / 平台治理 / 公共承诺 | `protocols/public-institution-protocol.md`、`worksheets/public-institution-check.md` | `references/concept-cards/malicious-compliance-ai-validation.md`、`references/concept-cards/visibility-opacity-weak-signals.md` | `public-power-governance-pack`、`v3-evidence-visibility-pack`、`v3-power-capture-malicious-compliance-pack` |
| 文章 / 评论 / 可读输出 | `../crossframe-essay/SKILL.md`、`templates/user-facing-language.md` | `references/v3-section-digest-index.md`、对应场景概念卡 | `expression-article-pack`、对应场景联读包 |

## 连续联读执行规则

- 只要上表的“连续联读包”不是空，就先读 `references/integrity-check.md`，确认同读材料和降档规则。`continuity-bundles.md` 和 `v3-source-spine.md` 保留为历史详参，按需查阅。
- 深度、审计、高责任、公共制度、亲密关系、长期演化、框架治理和文章输出场景，按需查阅 `references/v3-source-spine.md` 或 `references/v3-section-digest-index.md`（历史详参），确认原文相邻章节。日常完整性检查优先使用 `references/integrity-check.md`。
- 若 v3.0 与 v2.0 的理解冲突，以 v3.0 为准；若需要追踪演化，再读取 `v2-source-spine.md`、`v2-section-digest-index.md` 和 `v3-change-rationale-from-patch.md`。
- 输出前使用 `references/integrity-check.md` 做完整性检查：若发现只读了单张概念卡，且本节要求联读，必须补读或降档。
- `templates/reasoning-outline-output.md` 中的“本次连续联读包”只列包名，不展开完整工作表。

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
| 第一因、生命是什么、存在意义、虚无主义、自由意志 | `protocols/concept-explanation-protocol.md`，并优先形成结构性开放断言 |

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
