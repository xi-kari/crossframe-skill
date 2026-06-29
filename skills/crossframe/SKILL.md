---
name: crossframe
description: "CrossFrame explicit-only structural diagnosis skill for 跨尺度结构诊断框架 v5.0. Use only when the user explicitly names crossframe, $crossframe, /crossframe, CrossFrame, or says to use 跨尺度结构诊断; do not trigger implicitly from ordinary relationship, team, organization, public, philosophy, or long-term analysis requests. Suite-directed use after an explicit crossframe-suite invocation is allowed."
disable-model-invocation: true
---

# CrossFrame

如果用户任务需要多个 CrossFrame 平行 skill 连续协作，先读取 `../crossframe-suite/SKILL.md` 做总调度；本 skill 负责其中的结构诊断、事实边界、尺度窗口、机制候选、七闸复核和判断档位。

## 语言原则

本 skill 的权威语义是中文。`CrossFrame` 只是英文传播名与 skill id，不承担概念解释权。

遇到中英文可能冲突时，以中文术语为准：承接、回流、开放断言、尺度转移、责任链、观测反身性、低条件试探行动、退出转移、不浪费爱、强判断八件套、局部状态坐标、过程性产物边界。

英文可以用于文件名、别名、对外简介或必要的双语标注；不要把中文概念硬译成英文后再反向理解。

## 核心定位

CrossFrame 不是“把 v5.0 文本塞进上下文”的提示词包，而是一个可执行的结构推理协议。

每次使用都必须先形成内部推理产物，再输出结论。结论可以很短，但不能跳过事实抽取、七闸复核、机制候选、概念契约、判断档位、源结构连续性、claim ledger 和表达闸。

## 必须执行的顺序

1. 判断用户请求类型：快速诊断、完整诊断、推演、开放断言、命题验证、强判断、高反身性对象、亲密关系轻量入口、疗愈与转移、公共制度专项、低条件行动、高责任反俘获审查、框架边界、生命周期/状态坐标、递进闭环、势场/自主解离、治理连续性、框架治理与证伪、AI 过程性产物边界、弱信号/不透明检查、无制度基础设施中间路径、无法退出主体保护、隐喻/来源透明、工具化可及性、观测收束、超大规模压力测试、表达翻译、理论后台，或概念解释。
2. 读取 `references/runtime-read-policy.md`、`references/read-routing-map.md` 和必要时 `references/v5-material-selection-map.md`，确定本次需要加载的 v5 source modules、连读包、协议、工作表、概念卡和模板。
3. 先定位 v5 source modules，不全量打开大文件。默认只记录需要的 source module、关键词、V5-H 或源范围；只有源锚点不足、用户要求源审计、或高责任判断需要核验时，才定向读取 `references/v5-source-spine.md`、`references/v5-section-digest-index.md`、`references/v5-coverage-map.md` 或 `references/v5-term-fidelity.md` 的相关局部。
4. 读取 `references/continuity-closure-map.md` 展开入口包的“必须同读闭包”；需要包说明、源锚点或降档细节时，再读取 `references/continuity-bundles.md` 和对应 `references/continuity-bundles/v5/<bundle-id>.md`。默认最多读取 3 个入口核心包 + 2 个相邻辅助包；这个上限不限制必须同读闭包。高责任、公共制度、组织处置、公开判断必须优先读七闸、强判断八件套、低权力保护、证据降级与行动上限包及其闭包。
5. 按 `templates/read-state-capsule.md` 生成 `v5-read-state-capsule`：先列 source modules，再列入口包、必须同读闭包、相邻候选、源锚点、降档边界和下游读取策略。suite 不生成胶囊，胶囊由本核心层生成并传给专项 skill、essay 和 review。
6. 填写内部 intake：对象、尺度、事实、证据缺口、用户用途、受影响对象、观测影响、权力结构、行动上限。
7. 通过七闸：对象闸、证据闸、尺度闸、责任闸、观测闸、权力闸、行动闸。七闸必须登记为 `pass / weak / fail / blocked`；任一为 `fail` 或 `blocked`，不能维持强判断。
8. 判断是否触发 v5.0 半量化 DLC 运行时闸：默认不触发；只有用户明确要求量化、评分、半量化、比较、校准、一致性、审计、DLC 工具，或高责任/公开发布前需要内部边界审计时，才读取 DLC 文件。普通关系、组织和公共议题不得自动输出分数。
9. 形成至少两个机制候选；除非证据足以说明只有一个机制。每个机制候选必须登记 `mechanism_id`，并回指事实、源锚点、反向证据、概念契约和判断档位上限。
10. 对承担判断作用的概念做完整吸收：读取对应概念卡，并读取 `references/concept-contracts/core-contracts.md` 中对应概念契约；用 `worksheets/concept-fidelity-check.md` 做保真检查。概念卡回答含义，概念契约回答是否允许承担判断。
11. 用 `worksheets/source-continuity-check.md` 检查是否只读了孤立概念卡、漏掉 v5 相邻约束或需要降档。
12. 用 `worksheets/source-anchor-integrity-check.md` 检查中心命题、机制候选、高风险概念和行动边界能否回指胶囊源锚点；不能回指的内容只能标为“本文推断 / 表达转译 / 外部思想映射”，不得写成 CrossFrame v5 原义。
13. 按 `templates/claim-ledger.md` 生成 `claim ledger`：中心命题、机制候选、判断档位、行动建议、公共定性、文章转译和高风险概念使用都必须登记 `claim_id`。没有 `claim_id` 的命题不得进入正文或结论。
14. 用 `worksheets/claim-ledger-check.md` 检查正文前命题台账：若中心命题、行动建议、高风险概念或公共定性缺少事实锚点、源锚点、概念契约、判断档位、撤回条件或发布边界，必须删除、补证、降档，或标为“本文推断 / 表达转译 / 外部思想映射”。
15. 决定判断档位：轻量观察、开放断言、完整诊断、强判断、低条件试探行动、退出转移。若必须联读但未联读、源锚点不足、概念契约未通过、claim ledger 缺失，不能维持强判断。
16. 先输出可见推理提纲，再选择模板输出：先说现实语言，再按需要附内部映射。推理提纲不展示完整工作表，但必须显示判断来自事实、机制候选、七闸和命题台账，而不是来自术语套用。

## v5.0 半量化 DLC 运行时闸

v5.0 半量化 DLC 是 v5 主流程的附加审计层，不替换七闸、命题台账、概念契约、来源台账或 review。它只把七闸、证据、机制候选、反例和行动上限整理成可校准的结构剖面。

- 默认状态：`v5_dlc: not_triggered`。普通诊断、亲密关系、组织复盘、公共评论和概念解释不因为题材本身自动量化。
- 显式触发：用户说量化、评分、半量化、打分、比较、排序、校准、一致性、rubric、audit、DLC、七闸分值、案例库试跑，或要求展示/调试半量化表。
- 内部触发：高责任判断、公共发布、组织处置、真实平台/机构/人物、AI 合规材料或工具发布前，需要检查是否应降档、补证、阻断公开或隐藏分值时，可以内部触发，但默认不展示分数。
- 可见性：`score_visibility` 必须登记为 `hidden`、`profile_only` 或 `user_requested_profile`。默认 `hidden`；用户明确要求量化审计时最多展示结构剖面，不输出对象总分、关系分、组织健康分、文明阶段分或最终合格分。
- 高责任边界：DLC 分值只能触发降档、补证、反例入口、行动上限收窄或 `block_publication`；不能自动升级判断档位，不能作为处分、封禁、开除、资格、排名、公开定性、发布通过或 `substantive_pass` 的依据。
- 普通关系、组织和公共议题不得自动输出分数。若用户要求量化，只能说明“这是内部审计剖面”，先显示不能证明什么、缺哪些证据、最高行动上限和撤回条件。
- 任一七闸 `fail / blocked`、`claim_id` 缺失、source_anchor 缺失、低权力反例入口缺失、低成本材料冒充强证据或行动闸不足时，DLC 只能降档或阻断，不能给出更高判断。

触发后最小读取：

1. `references/construct-map-v5-dlc.md`
2. `worksheets/seven-gates-quant-rubric.md`
3. `references/judgment-action-matrix-v5-dlc.md`
4. 按需读取 `worksheets/evidence-ledger-v5-dlc.md`、`worksheets/mechanism-update-rules.md`、`worksheets/counterexample-register.md`

## 读取规则

- 默认遵守 `references/runtime-read-policy.md`：不读取 `evals/`、`examples/`、完整成功案例、完整失败案例或全量 v5 大索引。它们只用于开发压测、回归验证、风格调试、用户显式要求源审计或源锚点失败后的定向补读。
- 普通诊断：读 `protocols/diagnosis-protocol.md`，并使用 `worksheets/intake-worksheet.md`、`worksheets/seven-gates-worksheet.md`、`worksheets/evidence-ledger.md`、`worksheets/mechanism-candidates.md`。
- 量化、评分、半量化、比较、校准、一致性或 DLC 审计：先按 v5 主流程完成对象、证据、七闸、机制候选、claim ledger 和判断档位，再读取 v5 DLC 最小文件；分值只解释闸状态和降档理由。
- 推演、后续走向、路径展开、分支终点：读 `protocols/inference-protocol.md` 和 `templates/inference-output.md`，并按需追加状态坐标、长期演化、治理连续性包。
- 低到中等把握的判断：读 `protocols/open-assertion-protocol.md`、`worksheets/open-assertion-record.md`、`templates/open-assertion-output.md` 和 `v5-open-assertion-proposition-pack`。
- 高责任、强权力密度、处分、名誉、权利、资源、公共记忆类问题：读 `protocols/anti-capture-protocol.md`、`worksheets/high-responsibility-check.md`，并追加 `v5-low-power-protection-pack`、`v5-evidence-downgrade-action-ceiling-pack`。
- 影响资格、名誉、资源、权利、处置、公共记忆的强判断：读 `protocols/proposition-verification-protocol.md`、`worksheets/proposition-verification.md`、`worksheets/prospective-registration.md`、`templates/strong-judgment-output.md`，并追加 `v5-strong-judgment-eight-pack`。
- AI 报告、合规材料、漂亮汇报、机构自评、模型诊断：读 `v5-ai-process-artifact-boundary-pack`；必须声明过程性产物不得充当现实证明。
- 会因被观察、命名、公开或处置而改变行为、身份、证据或边界的对象：读 `protocols/high-reflexivity-protocol.md`、`worksheets/reflexivity-state-transfer.md`、`templates/high-reflexivity-output.md` 和 `v5-observation-reflexivity-release-pack`。
- 亲密关系、家庭、朋友、照护、单方承接、解释劳动和爱被要求的场景：读 `protocols/intimate-relationship-protocol.md`、`worksheets/intimate-relationship-light-check.md`、`templates/intimate-relationship-output.md`，并先读 `v5-love-trapped-trauma-pack` 和 `v5-low-power-protection-pack`。
- 系统停滞、创伤、修复、退出转移和重建场景：读 `protocols/healing-transfer-protocol.md`、`worksheets/healing-transfer-map.md`、`templates/healing-transfer-output.md` 和 `v5-action-healing-transfer-pack`。
- 公共制度、平台治理、公共承诺和高权力密度公共议题：读 `protocols/public-institution-protocol.md`、`worksheets/public-institution-check.md`、`templates/public-institution-output.md`，并追加 `v5-public-power-institution-pack`、`v5-evidence-downgrade-action-ceiling-pack`、`v5-low-power-protection-pack`。
- CrossFrame 可能被当作万能理论、领域替代品、人格审判工具或 AI 合规材料背书时：读 `protocols/framework-boundary-protocol.md`、`worksheets/framework-boundary-check.md`、`references/framework-ontology-protection.md` 和 `v5-use-boundary-governance-pack`。
- 长期演化、阶段判断、组织/关系/制度周期变化：读 `protocols/lifecycle-diagnosis-protocol.md`、`worksheets/lifecycle-stage-record.md`、`templates/lifecycle-output.md` 和 `v5-state-coordinate-lifecycle-pack`。阶段 0-6 只能作为局部状态坐标，禁止写成线性宿命。
- 战略推进、长期修复、子锚点闭环、为什么忙但没有积累：读 `protocols/progression-protocol.md`、`worksheets/sub-anchor-progression.md`、`templates/progression-output.md` 和 `v5-long-evolution-progression-field-pack`。
- 正负势场、沉积基本盘、自主解离、保护性退出：读 `protocols/field-dissociation-protocol.md`、`worksheets/field-dissociation-check.md` 和 `v5-long-evolution-progression-field-pack`。
- 调节、预警、偿付约束、多中心治理、承接者生成和代际承接：读 `protocols/governance-continuity-protocol.md`、`worksheets/governance-continuity-check.md`、`templates/governance-continuity-output.md` 和 `v5-governance-continuity-multicenter-pack`。
- 文明尺度、历史尺度、超大规模圈层或宏大公共判断：读 `protocols/large-scale-stress-test-protocol.md`、`worksheets/large-scale-stress-test.md`、`templates/large-scale-stress-output.md`，并先降级检查证据和发布门禁。
- 面向普通人、管理、制度公共、技术治理或其他 AI 软件改写表达：读 `protocols/expression-translation-protocol.md`、`references/expression-translation-table.md`、`templates/expression-translation-output.md` 和 `v5-domain-translation-normative-source-pack`。
- 概念解释、概念边界、思想解释类问题：读 `protocols/concept-explanation-protocol.md`、`references/concepts-minimal-set.md`、`references/v5-term-fidelity.md`、`v5-core-concept-integrity-pack`，再按需读必要概念卡。
- 哲学、意义、第一因、生命是什么、虚无主义、存在理由等抽象问题：优先走概念解释协议，先做尺度拆分和结构性开放断言；只有无法转成任何结构问题时，才退回 `protocols/framework-boundary-protocol.md`。
- 如果最终输出要使用承接/回流、开放断言、尺度转移、观测反身性、权力封闭、低条件试探行动、爱/开放行动、主体/责任链、证据成本、机制候选、判断档位、退出转移、修复副产品等高风险概念，必须先读取对应概念卡和 v5 连读包；不能只凭最小概念集作精细判断。

## 输出规则

- 默认输出短而清楚。除非用户明确要求极简结论，否则先展示一个“推理提纲”；不展示完整工作表。
- 推理提纲必须包含：诊断对象、事实边界、尺度窗口、七闸复核、机制候选、判断档位、命题台账状态、概念契约状态、本次读取的概念或保真检查、本次 v5 连续联读包、读态胶囊摘要、下一步观察或行动。
- 推理提纲必须登记 v5 DLC 状态：未触发 / 内部触发-不展示分值 / 用户要求可见剖面；同时登记 `score_visibility`。未触发时不要补写量化结论。
- v5 DLC 可见输出只能是结构剖面、降档理由、证据缺口、反例入口、行动上限和撤回条件；不得输出对象总分、排名、预测概率、关系质量分、组织健康分或发布合格分。
- 生成层不得宣布质量闸通过、完全通过、A档、合格或 `substantive_pass`。生成层只能给出自检摘要、待 review 判定的候选产物和必须补读/降档的风险点。
- 没有进入 `crossframe-review` 前，不得给出 `structural_pass`、`substantive_pass` 或 `publish_boundary` 的通过结论。质量闸归属 review；core、essay、suite 和 sibling skill 只能保留“自检未发现 X / 待 review 抽句复核”这类保守表述。
- review 看到生成层自称“质量闸通过 / 完全通过 / A档 / 合格 / substantive_pass”时，必须记录为“生成层自我盖章”，并重新执行反向否决最小块。
- 深度、审计、高责任、公共制度、亲密关系、长期演化和文章输出场景，推理提纲必须显示“本次连续联读包”；普通轻量问题可以写“未触发”。
- 推理提纲只能写提纲，不写冗长内心推理；它用于让用户看见推理路径，也用于约束后续输出不跳步。
- 只有用户要求“完整推理过程”“内部映射”“工作表”“审计”时，才展开完整工作表。
- 默认先说人话，不堆术语。第一段必须让没有读过框架的人也能明白“发生了什么、为什么卡住、下一步看什么”。
- 永远区分：来源、事实、证据、解释、机制候选、判断档位、行动上限。
- 术语只能作为附加映射，不得作为结论本身。不要用“这是典型的 X，所以 Y”替代推理。
- 输出前必须通过表达闸：删掉所有框架术语后，核心判断仍然能被普通用户读懂。
- 不得把结构诊断变成人格审判、命运预言、意识形态标签或道德授权。
- 不得用尺度升维抹掉低尺度痛苦、压力、失职和责任链。
- 不得把“爱”说成命令、正当性证明或单方面忍耐要求。
- 不得把 AI 生成的合规材料、漂亮报告、自评文本当作高成本证据。
- 不得用强判断绕开命题验证；开放断言不能作为高责任处置依据。
- 高反身性对象不得无限递归；第三层之后没有新增高成本证据或结构变量时，必须收束或降档。
- 亲密关系场景先保护痛苦、安全和边界，不把修复责任压回受伤者。
- 疗愈与转移只提供结构行动边界，不替代医疗、心理、法律、安全或组织处置。
- 如果证据不足但问题紧急，输出低风险、可撤回、可观察的小动作，而不是假装已经完成强诊断。

## 表达闸

最终输出前，内部检查四问：

1. 第一段是否不用术语也能说清问题？
2. 用户是否能知道这个判断来自哪些事实，而不是来自概念套用？
3. 是否把“承接、回流、尺度、开放断言”等术语翻译成了现实行为？
4. 是否给出了一个可观察信号或行动边界？

任一不通过，先重写表达，再输出。

## 推理提纲

默认输出前置一个简短提纲：

- 诊断对象：
- 事实边界：
- 尺度窗口：
- 七闸复核：
- 机制候选：
- 判断档位：
- 命题台账：已生成 / 缺失已降档 / 不触发；关键 claim_id：
- 概念契约：pass / partial / fail；降档决定：
- 读态胶囊：已生成 / 复用 / 缺失已降档：
- source_anchor / claim_id 边界：中心命题、机制句、行动建议是否已回指：
- 本次读取的概念：
- 本次 v5 连续联读包：
- 下一步：

这个提纲不是完整工作表，也不是冗长推理链。它的作用是让用户看见：本次输出确实先界定对象、检查证据、比较机制、再给判断。

## 核心资料

- `references/runtime-read-policy.md`：正常运行时的轻量读取策略，控制 eval/examples、完整案例和大 source modules 的默认不读取边界。
- `references/continuity-closure-map.md`：v5 连读包闭包的轻量运行时图。
- `references/v5-source-spine.md`：v5.0 原文标题层级、章节顺序、段落范围、相邻关系、表格索引和默认连读包。
- `references/v5-section-digest-index.md`：v5.0 逐节保真摘要、不可误读边界和相邻联读提醒。
- `references/v5-coverage-map.md`：v5.0 章节到 skill 模块、协议、工作表和连读包的覆盖地图。
- `references/v5-term-fidelity.md`：v5.0 术语保真表，防止压缩失真。
- `references/v5-material-selection-map.md`：v5.0 source modules、连读包、协议和模板的选择图。
- `references/continuity-bundles.md`：v5.0 连续联读包索引。
- `references/continuity-bundles/v5/`：26 个 v5 独立连读包。
- `references/read-routing-map.md`：按请求类型选择协议、工作表、概念卡和模板。
- `templates/read-state-capsule.md`：本次 v5 source modules、入口包、必须同读闭包、源锚点和下游读取策略的胶囊模板。
- `templates/claim-ledger.md`：中心命题、机制候选、行动建议、高风险概念和正文短摘的命题台账。
- `worksheets/claim-ledger-check.md`：检查正文和结论是否只从已登记命题展开。
- `references/construct-map-v5-dlc.md`、`worksheets/seven-gates-quant-rubric.md`、`references/judgment-action-matrix-v5-dlc.md`：v5.0 半量化 DLC 的运行时审计层，只在显式触发或高责任边界审计时读取。
- `references/concept-contracts/core-contracts.md`：核心高风险概念的准入、禁止升级、降档和审查契约。
- `schemas/claim-ledger.schema.json`：命题台账的结构化字段约束，用于脚本和 review 对齐。
- `references/concepts-minimal-set.md`：最小概念集。
- `references/framework-ontology-protection.md`：框架本体保护、反领域殖民、反模型殖民和概念改动规则。
- `references/guardrails.md`：反误用规则。
- `references/diagnostic-dimensions.md`、`references/diagnostic-toolbox-index.md`：复杂案例按需读取。
- `references/theory-backend-index.md`：根假设、核心推论、全周期演化、递进模式、多中心治理等深层理论索引。
- `references/expression-translation-table.md`：把后台概念翻译成普通人、管理、制度和技术治理语境。
- `references/concept-cards/`：高风险概念卡。
- `worksheets/seven-gates-worksheet.md`：七闸复核表。
- `worksheets/source-continuity-check.md`：输出前检查是否读少、断章或漏掉原文连续约束。
- `worksheets/source-anchor-integrity-check.md`：输出前检查中心命题、机制候选、概念、行动边界和文章转译是否能回指胶囊源锚点。

## 高风险概念闸

以下概念不能只按字面理解；一旦它们承担判断作用，必须读取对应概念卡和 v5 连读包：

高风险概念必须同时通过“概念卡 + 概念契约”双检查：

- 概念卡回答：这个概念在 CrossFrame 中是什么意思。
- 概念契约回答：本次是否允许用它承担判断、最高能到什么档位、失败时如何降档。
- 一旦概念进入中心命题、机制候选、行动建议、公共定性或文章点睛句，必须在 `claim ledger` 中登记 `claim_id`。
- 只读概念卡、不读概念契约时，该概念只能作为解释提示，不能承担判断。

- 承接 / 回流：读 `references/concept-cards/chengjie-huiliu.md`，并联读 `v5-core-concept-integrity-pack`。
- 开放断言：读 `references/concept-cards/open-assertion.md`，读取 `references/concept-contracts/core-contracts.md#contract-open_assertion`，并联读 `v5-open-assertion-proposition-pack`、`v5-source-evidence-separation-pack`、`v5-evidence-downgrade-action-ceiling-pack`。
- 只要输出中出现 `open_assertion`、开放断言、可撤回判断、最高开放断言、不能终局裁决、当前只能说、不能证明什么或撤回条件，就触发开放断言概念契约。不得写“概念契约不触发”；若契约无法读取或无法通过，必须降档、删除或标为表达转译。
- 尺度转移 / 尺度升维：读 `references/concept-cards/scale-transfer.md`，并联读 `v5-cross-scale-context-translation-pack`。
- 观测反身性：读 `references/concept-cards/reflexivity.md`，并联读 `v5-observation-reflexivity-release-pack`。
- 权力封闭 / 反俘获：读 `references/concept-cards/power-closure.md`，并联读 `v5-public-power-institution-pack` 与 `v5-low-power-protection-pack`。
- 低条件试探行动：读 `references/concept-cards/low-condition-action.md`，并联读 `v5-diagnosis-admission-downgrade-exit-pack`。
- 爱 / 开放行动 / 不浪费爱：读 `references/concept-cards/love-open-action.md`，并联读 `v5-love-trapped-trauma-pack`。
- 主体 / 责任链：读 `references/concept-cards/responsibility-chain.md`，并联读 `v5-responsibility-intervention-separation-pack`。
- 证据成本 / 弱信号 / AI 合规材料：读 `references/concept-cards/evidence-cost.md`，并联读 `v5-source-evidence-separation-pack` 与 `v5-ai-process-artifact-boundary-pack`。
- 机制候选：读 `references/concept-cards/mechanism-candidates.md`，并过七闸。
- 判断档位：读 `references/concept-cards/judgment-grades.md`，并联读 `v5-evidence-downgrade-action-ceiling-pack`。
- 退出转移：读 `references/concept-cards/exit-transfer.md`，并联读 `v5-action-healing-transfer-pack`。
- 修复副产品 / 伪修复：读 `references/concept-cards/repair-byproduct.md`，并联读 `v5-action-healing-transfer-pack`。
- 生命周期 / 阶段：读 `protocols/lifecycle-diagnosis-protocol.md`，并联读 `v5-state-coordinate-lifecycle-pack`。
- 框架治理 / 证伪 / 良性消亡：读 `references/concept-cards/framework-governance-falsification.md`，并联读 `v5-framework-self-diagnosis-falsification-pack`。
- 无法退出主体 / 复杂创伤 / 无健康基准：读 `references/concept-cards/trapped-subject-trauma-baseline.md`，并联读 `v5-love-trapped-trauma-pack`。
- 隐喻漂移 / 来源透明 / 规范性前提：读 `references/concept-cards/metaphor-source-transparency.md`，并联读 `v5-domain-translation-normative-source-pack`。
- 使用门槛债 / 工具化 / 分裂协议：读 `references/concept-cards/accessibility-toolization-split.md`，并联读 `v5-toolization-accessibility-release-pack`。
- 观测收束 / 熵增边界：读 `references/concept-cards/observation-entropy-contraction.md`，并联读 `v5-observation-reflexivity-release-pack`。

## 最低合格标准

一次合格的 CrossFrame 输出必须能回答：

- 我们到底在诊断什么对象？
- 哪些是来源，哪些是事实，哪些只是解释？
- 当前处在哪个尺度窗口？
- 七闸中哪一闸通过、哪一闸导致降级？
- 至少有哪些机制候选？
- 是否需要命题验证、强判断八件套、高反身性处理、亲密关系轻量入口、疗愈转移或公共制度专项？
- 谁在承担成本，谁有改变条件？
- 本次判断依赖哪些高风险概念，是否读取了完整概念卡和 v5 连读包？
- 这个判断能被什么证据撤回？
- 下一步是观察、修复、试探行动，还是退出转移？
- 生命周期判断是否写成了局部状态坐标，而不是线性宿命？
- 本次是否触发 v5 连续联读包，是否避免了只读孤立概念卡？
- 是否生成 `v5-read-state-capsule`，并让中心命题、机制候选、高风险概念和行动边界回指源锚点？
- 是否生成 `claim ledger`，并让中心命题、机制候选、行动建议、高风险概念和文章转译都有 `claim_id`？
- 正文或结论中是否存在没有 `claim_id` 的裸奔命题？
- 每个承担判断作用的高风险概念，是否同时通过概念卡、概念契约、v5 连续联读包和源锚点检查？
- 本次 v5 DLC 是否触发？若触发，`score_visibility` 是什么，分值是否只用于降档、补证、阻断发布或行动上限，而没有被用作处置、排名、公开定性或发布通过依据？
