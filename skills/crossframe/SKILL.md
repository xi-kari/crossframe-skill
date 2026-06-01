---
name: crossframe
description: |
  CrossFrame 是“跨尺度结构诊断框架 v2.0”的中文结构推理协议型 skill，用于诊断关系、团队、组织、制度、公共争议和长期演化中的复杂失衡。它要求先抽取事实、过尺度与责任闸、形成机制候选，再输出开放断言、推演分支、反俘获判断、低条件行动、生命周期/递进判断、治理连续性或超大规模压力测试。适用于用户提到 CrossFrame、跨尺度结构诊断、结构诊断、推演、开放断言、高责任判断、反俘获、亲密关系、疗愈转移、公共制度、长期演化，或希望分析复杂反复问题而不是套概念时。
---

# CrossFrame

## 语言原则

本 skill 的权威语义是中文。`CrossFrame` 只是英文传播名与 skill id，不承担概念解释权。

遇到中英文可能冲突时，以中文术语为准：承接、回流、开放断言、尺度转移、责任链、观测反身性、低条件试探行动、退出转移、不浪费爱。

英文可以用于文件名、别名、对外简介或必要的双语标注；不要把中文概念硬译成英文后再反向理解。

## 核心定位

CrossFrame 不是“把 v2.0 文本塞进上下文”的提示词包，而是一个可执行的结构推理协议。

每次使用都必须先形成内部推理产物，再输出结论。结论可以很短，但不能跳过事实抽取、闸门检查、机制候选和判断档位。

## 必须执行的顺序

1. 判断用户请求类型：快速诊断、完整诊断、推演、开放断言、强判断验证、高反身性对象、亲密关系轻量入口、疗愈与转移、公共制度专项、低条件行动、高责任反俘获审查、框架边界、生命周期、递进闭环、势场/自主解离、治理连续性、超大规模压力测试、表达翻译、理论后台，或概念解释。
2. 读取 `references/read-routing-map.md`，确定本次需要加载的协议、工作表、概念卡和模板。
3. 填写内部 intake：对象、尺度、事实、证据缺口、用户用途、受影响对象、观测影响。
4. 通过五闸：对象闸、证据闸、尺度闸、责任闸、观测闸。
5. 形成至少两个机制候选；除非证据足以说明只有一个机制。
6. 对承担判断作用的概念做完整吸收：读取对应概念卡，并用 `worksheets/concept-fidelity-check.md` 做保真检查。
7. 决定判断档位：轻量观察、开放断言、完整诊断、强判断、低条件试探行动、退出转移。
8. 先输出可见推理提纲，再选择模板输出：先说现实语言，再按需要附内部映射。

## 读取规则

- 普通诊断：读 `protocols/diagnosis-protocol.md`，并使用 `worksheets/intake-worksheet.md`、`worksheets/five-gates-worksheet.md`、`worksheets/evidence-ledger.md`、`worksheets/mechanism-candidates.md`。
- 推演、后续走向、路径展开、分支终点：读 `protocols/inference-protocol.md` 和 `templates/inference-output.md`。
- 低到中等把握的判断：读 `protocols/open-assertion-protocol.md`、`worksheets/open-assertion-record.md` 和 `templates/open-assertion-output.md`。
- 高责任、强权力密度、处分、名誉、权利、资源、公共记忆类问题：读 `protocols/anti-capture-protocol.md` 和 `worksheets/high-responsibility-check.md`。
- 影响资格、名誉、资源、权利、处置、公共记忆的强判断：读 `protocols/proposition-verification-protocol.md`、`worksheets/proposition-verification.md`、`worksheets/prospective-registration.md` 和 `templates/strong-judgment-output.md`。
- 会因被观察、命名、公开或处置而改变行为、身份、证据或边界的对象：读 `protocols/high-reflexivity-protocol.md`、`worksheets/reflexivity-state-transfer.md` 和 `templates/high-reflexivity-output.md`。
- 亲密关系、家庭、朋友、照护、单方承接、解释劳动和爱被要求的场景：读 `protocols/intimate-relationship-protocol.md`、`worksheets/intimate-relationship-light-check.md` 和 `templates/intimate-relationship-output.md`。
- 系统停滞、创伤、修复、退出转移和重建场景：读 `protocols/healing-transfer-protocol.md`、`worksheets/healing-transfer-map.md` 和 `templates/healing-transfer-output.md`。
- 公共制度、平台治理、公共承诺和高权力密度公共议题：读 `protocols/public-institution-protocol.md`、`worksheets/public-institution-check.md` 和 `templates/public-institution-output.md`。
- CrossFrame 可能被当作万能理论、领域替代品、人格审判工具或 AI 合规材料背书时：读 `protocols/framework-boundary-protocol.md`、`worksheets/framework-boundary-check.md` 和 `references/framework-ontology-protection.md`。
- 长期演化、阶段判断、组织/关系/制度周期变化：读 `protocols/lifecycle-diagnosis-protocol.md`、`worksheets/lifecycle-stage-record.md` 和 `templates/lifecycle-output.md`。
- 战略推进、长期修复、子锚点闭环、为什么忙但没有积累：读 `protocols/progression-protocol.md`、`worksheets/sub-anchor-progression.md` 和 `templates/progression-output.md`。
- 正负势场、沉积基本盘、自主解离、保护性退出：读 `protocols/field-dissociation-protocol.md`、`worksheets/field-dissociation-check.md` 和 `references/field-management-and-dissociation.md`。
- 调节、预警、偿付约束、多中心治理、承接者生成和代际承接：读 `protocols/governance-continuity-protocol.md`、`worksheets/governance-continuity-check.md` 和 `templates/governance-continuity-output.md`。
- 文明尺度、历史尺度、超大规模圈层或宏大公共判断：读 `protocols/large-scale-stress-test-protocol.md`、`worksheets/large-scale-stress-test.md` 和 `templates/large-scale-stress-output.md`。
- 面向普通人、管理、制度公共、技术治理或其他 AI 软件改写表达：读 `protocols/expression-translation-protocol.md`、`references/expression-translation-table.md` 和 `templates/expression-translation-output.md`。
- 证据不足但风险紧急：读 `protocols/low-condition-action-protocol.md`。
- 概念解释、概念边界、思想解释类问题：读 `protocols/concept-explanation-protocol.md`、`references/concepts-minimal-set.md`、`references/v2-term-fidelity.md`，再读必要概念卡。
- 复杂诊断或用户要求深度时：按需读 `references/diagnostic-dimensions.md` 和 `references/diagnostic-toolbox-index.md`，但不要把工具箱术语堆到前台输出。
- 文明尺度、长期演化、制度生成、系统持续性、多中心治理或用户要求深层理论时：先读对应专项协议；需要根假设和核心推论时再读 `references/theory-backend-index.md`；不要让理论后台进入普通前台输出。
- 如果最终输出要使用承接/回流、开放断言、尺度转移、观测反身性、权力封闭、低条件试探行动、爱/开放行动、主体/责任链、证据成本、机制候选、判断档位、退出转移、修复副产品等高风险概念，必须先读取对应概念卡；不能只凭最小概念集作精细判断。
- 输出前使用 `worksheets/concept-fidelity-check.md` 检查：本次概念是否读全、是否保留中文语义、是否落回现实行为、是否避免压缩失真。

## 输出规则

- 默认输出短而清楚。除非用户明确要求极简结论，否则先展示一个“推理提纲”；不展示完整工作表。
- 推理提纲必须包含：诊断对象、事实边界、尺度窗口、机制候选、判断档位、本次读取的概念或保真检查、下一步观察或行动。
- 推理提纲只能写提纲，不写冗长内心推理；它用于让用户看见推理路径，也用于约束后续输出不跳步。
- 只有用户要求“完整推理过程”“内部映射”“工作表”“审计”时，才展开完整工作表。
- 默认先说人话，不堆术语。第一段必须让没有读过框架的人也能明白“发生了什么、为什么卡住、下一步看什么”。
- 永远区分：事实、解释、机制候选、判断档位。
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
- 机制候选：
- 判断档位：
- 本次读取的概念：
- 下一步：

这个提纲不是完整工作表，也不是冗长推理链。它的作用是让用户看见：本次输出确实先界定对象、检查证据、比较机制、再给判断。

## 核心资料

- `references/crossframe-v2-core.md`：v2.0 的最小执行核心。
- `references/v2-coverage-map.md`：v2.0 章节到 skill 模块的覆盖地图。
- `references/concepts-minimal-set.md`：最小概念集。
- `references/v2-term-fidelity.md`：v2.0 术语保真表，防止压缩失真。
- `references/read-routing-map.md`：按请求类型选择协议、工作表、概念卡和模板。
- `references/framework-ontology-protection.md`：框架本体保护、反领域殖民、反模型殖民和概念改动规则。
- `references/guardrails.md`：反误用规则。
- `references/diagnostic-dimensions.md`：10 个基础诊断维度与 3 个扩展维度。
- `references/diagnostic-toolbox-index.md`：诊断工具箱索引，复杂案例按需读取。
- `references/theory-backend-index.md`：根假设、核心推论、全周期演化、递进模式、多中心治理等深层理论索引。
- `references/field-management-and-dissociation.md`：双向势场、沉积基本盘和自主解离。
- `references/expression-translation-table.md`：把后台概念翻译成普通人、管理、制度和技术治理语境。
- `references/scale-transfer-gate.md`：尺度转移检查。
- `references/reflexivity-and-observation.md`：观测反身性。
- `references/power-closure-and-exit.md`：权力封闭与退出转移。
- `references/love-as-open-action.md`：爱作为开放行动。
- `references/concept-cards/`：高风险概念卡，处理容易被压扁或误用的概念。

## 高风险概念闸

以下概念不能只按字面理解；一旦它们承担判断作用，必须读取对应概念卡：

- 承接 / 回流：读 `references/concept-cards/chengjie-huiliu.md`
- 开放断言：读 `references/concept-cards/open-assertion.md`
- 尺度转移 / 尺度升维：读 `references/concept-cards/scale-transfer.md`
- 观测反身性：读 `references/concept-cards/reflexivity.md`
- 权力封闭 / 反俘获：读 `references/concept-cards/power-closure.md`
- 低条件试探行动：读 `references/concept-cards/low-condition-action.md`
- 爱 / 开放行动 / 不浪费爱：读 `references/concept-cards/love-open-action.md`
- 主体 / 责任链：读 `references/concept-cards/responsibility-chain.md`
- 证据成本 / 弱信号 / AI 合规材料：读 `references/concept-cards/evidence-cost.md`
- 机制候选：读 `references/concept-cards/mechanism-candidates.md`
- 判断档位：读 `references/concept-cards/judgment-grades.md`
- 退出转移：读 `references/concept-cards/exit-transfer.md`
- 修复副产品 / 伪修复：读 `references/concept-cards/repair-byproduct.md`
- 锚点组 / 多层锚结构 / 跨域互操作：读 `references/concept-cards/anchor-group.md`
- 动力组 / 转译 / 支撑通道 / 条件场：读 `references/concept-cards/dynamics-group.md`
- 结构组与过程组 / 行动承接 / 结构负荷：读 `references/concept-cards/structure-process-group.md`

## 最低合格标准

一次合格的 CrossFrame 输出必须能回答：

- 我们到底在诊断什么对象？
- 哪些是事实，哪些只是解释？
- 当前处在哪个尺度窗口？
- 至少有哪些机制候选？
- 是否需要命题验证、高反身性处理、亲密关系轻量入口、疗愈转移或公共制度专项？
- 谁在承担成本，谁有改变条件？
- 本次判断依赖哪些高风险概念，是否读取了完整概念卡？
- 这个判断能被什么证据撤回？
- 下一步是观察、修复、试探行动，还是退出转移？
- 是否触发了框架边界、生命周期、递进、势场解离、治理连续性或超大规模压力测试？
