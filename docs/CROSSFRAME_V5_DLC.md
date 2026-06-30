# 跨尺度结构诊断框架 v5.0 半量化 DLC

## 发布边界

半量化 DLC 是在 v5.0 结构诊断协议之上增加的半量化审计层。它不替代 v5.0 的事实边界、七闸、机制候选、命题台账、概念契约、行动上限和框架治理，也不把复杂现实压缩成可排名的单一数字。

本工具只帮助整理结构判断，不替代现实调查、专业判断、受影响位置反馈、外部复核和最终责任承担。分数只能触发降级、复核或补证，不能单独授权处置。

## 与 v5.0 原文的关系

v5.0 已经建立七大部分：极简导读、使用准则与边界、核心概念与根假设、诊断流程与工具箱、闭环与转移协议、应用专项、框架治理与证伪。半量化 DLC 保留这些结构，只增加一层可审计的半量化记录方式。

半量化 DLC 的新增部分对应当前仓库文件：

- `skills/crossframe/references/construct-map-v5-dlc.md`
- `skills/crossframe/worksheets/seven-gates-quant-rubric.md`
- `skills/crossframe/worksheets/evidence-ledger-v5-dlc.md`
- `skills/crossframe/worksheets/calibration-anchor-card.md`
- `skills/crossframe/worksheets/mechanism-update-rules.md`
- `skills/crossframe/worksheets/counterexample-register.md`
- `skills/crossframe/references/judgment-action-matrix-v5-dlc.md`
- `skills/crossframe/references/falsification-governance-v5-dlc.md`
- `skills/crossframe-casebook/examples/v5-dlc-quant-trials/validation-summary.md`
- `scripts/validate_v5_dlc_quantification_schema_fixtures.py`
- `scripts/check_v5_dlc_casebook_trials.py`

## 半量化 DLC 不是什么

半量化 DLC 不是总分系统，不是预测模型，不是认证系统，也不作为处置依据。它不得用于开除、封禁、惩戒、拘束、拒绝服务、剥夺资源、资格判断或人格定性。案例库覆盖、评分者一致或 checker 通过都不能证明现实判断正确。

## 半量化层的四项责任

1. 校准判断：说明一个结构变量在当前材料中处于什么程度，而不是给对象定性。
2. 暴露不确定性：把证据缺口、反例压力、复核条件和撤回条件显式化。
3. 限制行动上限：证据和七闸不足时自动降级，不允许分数越权授权行动。
4. 触发复核和写回：发现反例、评分分歧或误用时，必须改变台账、案例库、工具或文本边界。

## 构念图谱

半量化 DLC 首批构念来自 v5.0 已有诊断动作，不新增本体概念。构念只描述可观察结构变量：对象边界清晰度、证据可支撑度、尺度一致性、责任链可追踪度、观测反身性风险、低权力反例入口、行动上限清晰度、反馈写回程度、修复窗口可行度、反例写回强度。

构念必须说明现实问题、禁止误用、可观察信号、最低证据和撤回条件。没有这些字段的构念不得进入正式工具。完整表见 `skills/crossframe/references/construct-map-v5-dlc.md`。

## 七闸半量化

七闸继续保留 `pass / weak / fail / blocked`。半量化 DLC 新增 0-4 锚点评分，但分值只解释状态来源：

- 0：缺失、不可判断或材料被阻断。
- 1：低成本线索，边界、来源或反例不足。
- 2：可形成开放断言，必须保留替代解释。
- 3：可支撑完整诊断，高责任场景仍需追加强判断八件套。
- 4：材料、反例、复核和行动边界较完整，可申请强判断流程。

任一闸 `fail` 或 `blocked` 都不能维持强判断。证据闸、权力闸、行动闸不足时，优先降档、补证或阻断发布。完整表见 `skills/crossframe/worksheets/seven-gates-quant-rubric.md`。

## 证据台账

半量化 DLC 在来源台账和证据台账中增加证据成本、直接性、独立性、可复核性、反例搜索状态、诊断力、机制边、降档理由、撤回条件和不能证明边界。

低成本材料不得单独支撑强判断。同源材料不能通过数量堆叠变成独立证据。AI 或过程性产物默认只能整理证据，不能证明现实安全、修复完成或制度有效。完整表见 `skills/crossframe/worksheets/evidence-ledger-v5-dlc.md`。

## 校准锚点

每个维度必须先有校准卡，再允许评分。校准卡至少包含定义、不是什么、相邻概念、0-4 锚点、最低证据、高责任升级条件、常见误用、撤回条件、对应 v5 源锚点、工作表和 schema 字段。

锚点不得由样本均值、使用者直觉或便利数据直接切分。完整模板见 `skills/crossframe/worksheets/calibration-anchor-card.md`。

## 机制候选更新

机制候选不做总排序，不输出“某机制 82 分”，也不输出精确概率。半量化 DLC 只记录证据如何增强、削弱、保留、待证或撤回某一条机制边。

每条机制候选必须说明能解释什么、不能解释什么、可观察信号和撤回条件。完整规则见 `skills/crossframe/worksheets/mechanism-update-rules.md`。

## 判断档位与行动上限

判断档位沿用 `light_observation`、`open_assertion`、`full_diagnosis`、`strong_judgment`、`low_condition_action`、`exit_transfer`。行动上限使用 `observe`、`ask_for_evidence`、`internal_review`、`publish_with_boundary`、`block_publication`、`exit_transfer`。

矩阵规则：高分不能自动升级，失败闸口必须降档，权力和行动边界不足时必须阻断公开或处置。完整矩阵见 `skills/crossframe/references/judgment-action-matrix-v5-dlc.md`。

## 反例、撤回与治理写回

反例不是附录，而是治理事件。轻微反例写入边界，重复反例修订锚点，高伤害反例暂停用法，系统性反例引入替代机制，误用反例修改模板或 checker，不可修复案例进入退出转移。

完整治理规则见 `skills/crossframe/references/falsification-governance-v5-dlc.md` 和 `skills/crossframe/worksheets/counterexample-register.md`。

## 案例库验证与评分者一致性

第一轮案例库验证只用于失败发现。已试跑组织、关系、公共争议和尺度升维误用四类案例。结果显示：公共争议在低权力反例入口不足时必须阻断发布；尺度升维误用必须触发降档和模板写回；评分者分歧需要保留为校准材料。

完整摘要见 `skills/crossframe-casebook/examples/v5-dlc-quant-trials/validation-summary.md`。案例库验证不能证明框架现实正确，评分者一致性不能证明现实判断为真，覆盖率不能证明外部有效性。

## 反误用红线

- 不得把半量化表包装成完整诊断。
- 不得把评分者一致性包装成现实正确性。
- 不得把案例库覆盖率包装成外部有效性。
- 不得把内部压力测试结果用于营销、认证或安全证明。
- 不得让付费方、委托方或被评估方单方控制证据入口、反馈入口和发布口径。
- 不得把低权力主体无法提交反例解释为“无反例”。
- 不得将 AI 自动评分用于强判断、公开定性或组织处置。

## 工具原型

第一版工具原型包括：Markdown 工作表、JSON schema、fixtures、`scripts/validate_v5_dlc_quantification_schema_fixtures.py`、`scripts/check_v5_dlc_casebook_trials.py`、`scripts/check_v5_dlc_publication_bundle.py`、`scripts/build_v5_dlc_publication_bundle.py` 和 `scripts/build_v5_dlc_docx.py`。

工具原型只能做结构校验、缺口暴露、降档提醒和发布前边界检查。它不替代人工审查。使用说明见 `docs/V5_DLC_TOOL_PROTOTYPE.md`。

## 发布前检查清单

- v5 DLC 文档是否仍把 v5.0 作为结构基础。
- 是否显式禁止总分、预测、认证和处置用途。
- 每个新构念是否有证据要求、误用风险和撤回条件。
- 七闸、证据、机制、判断、行动是否能回指台账。
- 反例和评分者分歧是否能写回文本、工具或版本记录。
- 发布 bundle 是否带 source manifest 和 SHA256。
- source manifest 是否覆盖发布文档源、工具脚本、validator 和 schema。
- 所有 checker、schema fixtures、casebook trials、integrity、source continuity 和 mirror checks 是否通过。
