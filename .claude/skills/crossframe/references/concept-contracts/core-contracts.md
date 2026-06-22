# 核心高风险概念契约

概念卡回答“这个概念是什么意思”；概念契约回答“什么时候允许用它承担判断、什么时候必须降档、失败后怎么处理”。

任何高风险概念只要进入中心命题、机制候选、行动建议、公共定性或文章点睛句，必须同时满足：

```text
概念卡已读
v5 连续联读包已读
required_closure 已展开
概念契约已检查
claim ledger 已登记
```

---

## contract: power_closure

```yaml
concept_id: power_closure
term: 权力封闭
concept_card: references/concept-cards/power-closure.md
required_closure:
  - v5-public-power-institution-pack
  - v5-low-power-protection-pack
  - v5-evidence-downgrade-action-ceiling-pack

allowed_when:
  - 低权力主体缺少安全申诉、复核、退出或补充事实通道
  - 权力方同时掌握规则、证据、解释和处置入口
  - 已区分事实、声明、热度、解释和公共定性

forbidden_when:
  - 只有情绪、热度或单方材料
  - 用概念直接替代公开指控或人格定性
  - 未写明反向条件、申诉入口和行动上限

required_inputs:
  - actor_map
  - review_or_appeal_path
  - source_ledger
  - low_power_risk
  - claim_id

allowed_outputs:
  - 当前只能说存在权力封闭风险
  - 需要补充可申诉性、复核记录和反方材料
  - 该判断不得直接用于公开定性或处分

forbidden_outputs:
  - 这证明对方恶意封闭
  - 可以直接公开追责
  - 所有申诉都是无效表演

downgrade_if:
  source_ledger_incomplete: 最高开放断言
  appeal_path_unknown: 保留为风险问题
  public_consequence_high: 进入强判断八件套
  claim_ledger_missing: 不得进入结论

audit_questions:
  - 谁掌握规则、证据、解释和处置入口？
  - 低权力主体是否有安全补充事实和申诉路径？
  - 该判断支持哪个 claim_id？
  - 什么证据会证明通道并未封闭？
  - 行动上限是什么？
```

---

## contract: low_condition_action

```yaml
concept_id: low_condition_action
term: 低条件试探行动
concept_card: references/concept-cards/low-condition-action.md
required_closure:
  - v5-evidence-downgrade-action-ceiling-pack
  - v5-responsibility-intervention-separation-pack
  - v5-low-power-protection-pack

allowed_when:
  - 证据不足以强判断，但风险或修复窗口要求小步验证
  - 行动可撤回、可观察、低伤害、低承诺
  - 已写明 owner、时间盒、停止条件和行动上限

forbidden_when:
  - 行动不可逆、会公开定性、处分、退出或伤害低权力主体
  - 没有观察指标和停止条件
  - 用低条件行动包装强处置

required_inputs:
  - claim_id
  - action_ceiling
  - observation_signal
  - stop_condition
  - withdrawal_condition

allowed_outputs:
  - 先做一个低风险、可撤回的小动作
  - 本行动只用于观察，不用于定性
  - 到达停止条件时立即降档或暂停

forbidden_outputs:
  - 先公开施压看看
  - 先处分再补证
  - 只要试一下就没有风险

downgrade_if:
  action_ceiling_missing: 不给行动建议
  stop_condition_missing: 改为观察项
  public_consequence_high: 阻断行动输出
  claim_id_missing: 不得进入结论

audit_questions:
  - 这一步是否可撤回、可观察、低伤害？
  - 它验证哪个 claim_id？
  - 行动上限是什么？
  - 什么信号触发停止？
  - 它有没有偷渡强处置？
```

---

## contract: love_open_action

```yaml
concept_id: love_open_action
term: 爱 / 开放行动
concept_card: references/concept-cards/love-open-action.md
required_closure:
  - v5-love-trapped-trauma-pack
  - v5-action-healing-transfer-pack
  - v5-responsibility-intervention-separation-pack

allowed_when:
  - 能区分开放行动、忍耐义务、关系消耗和修复条件
  - 不把爱写成单方继续承接的道德命令
  - 已保护低权力主体、安全边界和停止条件

forbidden_when:
  - 用户处在无法退出、创伤、安全或专业高风险情境
  - 用爱取消责任链、边界或外部承接
  - 要求低权力主体继续证明、继续解释或继续牺牲

required_inputs:
  - cost_bearer
  - boundary_condition
  - repair_signal
  - stop_condition
  - claim_id

allowed_outputs:
  - 爱不能取消边界和责任链
  - 开放行动必须留下记忆、边界或修复能力
  - 继续承接不是默认义务

forbidden_outputs:
  - 如果真的爱就继续忍耐
  - 你应该再给一次机会
  - 爱会自然带来修复

downgrade_if:
  safety_unknown: 先做安全边界
  low_power_risk: 不给关系优化建议
  repair_signal_missing: 降为观察
  claim_id_missing: 不得诊断

audit_questions:
  - 这个判断是否把爱变成忍耐义务？
  - 谁在承担解释、等待或修复成本？
  - 是否有现实回流或条件改变？
  - 对应 claim_id 和行动上限是什么？
  - 什么情况下必须停止或转向外部承接？
```

---

## contract: reflexivity

```yaml
concept_id: reflexivity
term: 观测反身性
concept_card: references/concept-cards/reflexivity.md
required_closure:
  - v5-observation-reflexivity-release-pack
  - v5-state-coordinate-lifecycle-pack
  - v5-evidence-downgrade-action-ceiling-pack

allowed_when:
  - 诊断、公开表达、指标或观察会改变对象行为
  - 已区分被观察前状态、被观察后反应和模型自身干预
  - 已写明停止观察或降档条件

forbidden_when:
  - 用对象可能反应来无限猜测动机
  - 把反身性当作拒绝判断或无限递归的理由
  - 没有事实边界却预测对象反应

required_inputs:
  - observed_state
  - observation_channel
  - possible_feedback_effect
  - stop_condition
  - claim_id

allowed_outputs:
  - 这个判断被看见后可能改变对象行为
  - 该反应只记录，不直接改写主判断
  - 到达某信号时暂停强判断

forbidden_outputs:
  - 对方一定会因为被观察而表演
  - 既然会反身，就什么都不能判断
  - 所有回应都是策略

downgrade_if:
  observation_channel_unclear: 只作提醒
  behavior_evidence_missing: 不预测反应
  recursion_unbounded: 停止观察
  claim_id_missing: 不得进入结论

audit_questions:
  - 观察通过什么渠道进入对象？
  - 哪些反应是事实，哪些只是预测？
  - 该反身性支持哪个 claim_id？
  - 有没有无限递归或动机猜测？
  - 何时暂停观察或降档？
```

---

## contract: toolization_accessibility

```yaml
concept_id: toolization_accessibility
term: 工具化 / 可及性释放
concept_card: references/concept-cards/accessibility-toolization-split.md
required_closure:
  - v5-toolization-accessibility-release-pack
  - v5-use-boundary-governance-pack
  - v5-evidence-downgrade-action-ceiling-pack

allowed_when:
  - 框架、课程、AI 工具、认证或商业化材料降低使用门槛
  - 已区分可及性提升、责任转移、认证错觉和治理边界
  - 已写明使用上限和失败回收机制

forbidden_when:
  - 把能用工具等同于具备判断资格
  - 用工具输出替代来源台账、概念契约或专业判断
  - 商业化材料制造强权威或处置建议

required_inputs:
  - use_context
  - user_power_position
  - governance_boundary
  - failure_recovery
  - claim_id

allowed_outputs:
  - 该工具只能降低入口成本
  - 不能替代判断责任和来源审计
  - 需要保留失败回收和人工复核

forbidden_outputs:
  - 工具能自动完成诊断
  - 认证意味着判断可发布
  - AI 报告可以直接作为治理证据

downgrade_if:
  governance_boundary_missing: 只作工具说明
  source_ledger_missing: 不得强判断
  user_power_high: 加强责任上限
  claim_id_missing: 不得进入结论

audit_questions:
  - 这是可及性提升，还是判断责任转移？
  - 谁会使用该工具，谁承担错误成本？
  - 该输出支持哪个 claim_id？
  - 它不能替代什么？
  - 失败后如何回收和复核？
```

---

## contract: metaphor_source_transparency

```yaml
concept_id: metaphor_source_transparency
term: 隐喻 / 来源透明
concept_card: references/concept-cards/metaphor-source-transparency.md
required_closure:
  - v5-domain-translation-normative-source-pack
  - v5-core-concept-integrity-pack
  - v5-source-evidence-separation-pack

allowed_when:
  - 使用隐喻、典故、理论映射或跨领域类比帮助读者理解
  - 已标明隐喻来源和可迁移范围
  - 隐喻不承担事实证明或强判断

forbidden_when:
  - 用隐喻替代证据
  - 把外部理论写成 CrossFrame 原义
  - 类比对象会造成公共定性或人格审判

required_inputs:
  - metaphor_source
  - transfer_scope
  - cannot_prove
  - claim_id

allowed_outputs:
  - 这只是表达转译，不是事实证明
  - 该隐喻只能照亮某个结构侧面
  - 类比不能证明责任归属

forbidden_outputs:
  - 因为像这个隐喻，所以事实成立
  - 某理论已经证明本判断
  - 类比对象等同于现实对象

downgrade_if:
  metaphor_source_missing: 删除或改写
  transfer_scope_unclear: 标为表达转译
  factual_claim_unsupported: 不得进入结论
  claim_id_missing: 不得承担判断

audit_questions:
  - 隐喻来源是什么？
  - 它支持哪个 claim_id，还是只做表达？
  - 它不能证明什么？
  - 有没有把类比写成事实？
  - 是否需要标为表达转译？
```

---

## contract: exit_transfer

```yaml
concept_id: exit_transfer
term: 退出转移
concept_card: references/concept-cards/exit-transfer.md
required_closure:
  - v5-diagnosis-admission-downgrade-exit-pack
  - v5-low-power-protection-pack
  - v5-responsibility-intervention-separation-pack

allowed_when:
  - 内部修复条件不足，继续投入会扩大伤害或证据风险
  - 已区分退出、暂停、外部承接、专业求助和安全路径
  - 已写明低风险、可撤回或安全优先的行动边界

forbidden_when:
  - 证据不足却直接建议关系退出、离职、公开举报或法律行动
  - 忽略安全、经济、照护、法律或专业风险
  - 用退出转移惩罚低权力主体

required_inputs:
  - repair_condition_status
  - safety_boundary
  - external_support_path
  - action_ceiling
  - claim_id

allowed_outputs:
  - 先暂停原路径，保护人和证据
  - 转向外部承接或专业路径
  - 退出建议必须低风险、分阶段、可复核

forbidden_outputs:
  - 立刻退出
  - 直接公开
  - 先切断所有关系
  - 不用考虑外部风险

downgrade_if:
  safety_unknown: 先补安全评估
  external_path_missing: 不给退出建议
  high_stakes: 建议专业支持
  claim_id_missing: 只给观察边界

audit_questions:
  - 内部修复条件为什么不足？
  - 退出、暂停和外部承接是否被区分？
  - 对应 claim_id 的行动上限是什么？
  - 是否存在安全、法律、经济或照护风险？
  - 什么条件下可撤回或降档？
```

---

## contract: repair_byproduct

```yaml
concept_id: repair_byproduct
term: 修复副产品
concept_card: references/concept-cards/repair-byproduct.md
required_closure:
  - v5-action-healing-transfer-pack
  - v5-responsibility-intervention-separation-pack
  - v5-seven-gates-diagnosis-pack

allowed_when:
  - 修复行动留下规则、记忆、能力、边界、流程或资源变化
  - 已区分表演性修复、口头承诺和现实条件改变
  - 能写出下一轮如何复查副产品是否生效

forbidden_when:
  - 把道歉、复盘材料、报告或仪式当成修复本身
  - 没有写回对象、owner、时间表或复查证据
  - 用修复副产品掩盖责任链

required_inputs:
  - repair_action
  - writeback_target
  - owner
  - review_signal
  - claim_id

allowed_outputs:
  - 修复是否发生要看留下了什么
  - 复盘材料只是候选副产品，不是修复本身
  - 下一轮用具体信号复查

forbidden_outputs:
  - 道歉了就是修复
  - 写了报告就完成闭环
  - 氛围变好说明机制修复

downgrade_if:
  writeback_target_missing: 降为表演性修复候选
  owner_missing: 不得判定已修复
  review_signal_missing: 只作观察项
  claim_id_missing: 不得进入结论

audit_questions:
  - 修复留下了什么可复查副产品？
  - 它写回了规则、资源、角色、边界还是记忆？
  - 对应 claim_id 是什么？
  - 有没有把报告、道歉或复盘当成修复？
  - 下一轮如何证明它仍然有效？
```

## 通用字段

每个概念契约至少包含：

```text
concept_id
term
allowed_when
forbidden_when
required_inputs
required_closure
allowed_outputs
forbidden_outputs
downgrade_if
audit_questions
```

---

## contract: open_assertion

```yaml
concept_id: open_assertion
term: 开放断言
concept_card: references/concept-cards/open-assertion.md
required_closure:
  - v5-open-assertion-proposition-pack
  - v5-source-evidence-separation-pack
  - v5-evidence-downgrade-action-ceiling-pack

allowed_when:
  - 证据不足以支撑强判断，但已有可说明的结构信号
  - 输出不会直接用于处分、名誉定性、资格剥夺、资源分配或公共记忆
  - 能写出撤回条件、补证方向和行动上限

forbidden_when:
  - 用户要求对人、机构、平台、组织做最终定性
  - 只有单一来源族或低成本声明，却要进入公共强判断
  - 无法写出撤回条件
  - 输出将被用于高责任处置

required_inputs:
  - 至少一个事实边界
  - 至少一个机制候选
  - 证据闸不得为 blocked
  - 行动闸必须写明上限
  - claim ledger 必须登记对应 claim_id

allowed_outputs:
  - 作为开放断言，目前只能说……
  - 更稳妥的说法是存在某种机制可能……
  - 这还不能证明……
  - 需要继续观察……

forbidden_outputs:
  - 这证明了……
  - 这说明某人/某机构就是……
  - 可以据此处置……
  - 已经足以公开定性……

downgrade_if:
  evidence_gate_weak: 只能保留开放断言或补证清单
  source_anchor_missing: 标为本文推断
  public_consequence_high: 不得进入强判断
  no_withdrawal_condition: 降为轻量观察

audit_questions:
  - 这个开放断言支持哪些事实？
  - 它不能证明什么？
  - 什么事实出现时必须撤回？
  - 它最多允许什么行动？
```

---

## contract: judgment_grades

```yaml
concept_id: judgment_grades
term: 判断档位
concept_card: references/concept-cards/judgment-grades.md
required_closure:
  - v5-evidence-downgrade-action-ceiling-pack
  - v5-strong-judgment-eight-pack
  - v5-seven-gates-diagnosis-pack
  - v5-source-evidence-separation-pack

allowed_when:
  - 已完成七闸状态记录
  - 已完成来源/证据/解释分离
  - 已写明行动上限和撤回条件
  - claim ledger 中每个中心命题都有判断档位

forbidden_when:
  - 用“感觉很明显”或“结构上就是”替代证据档位
  - 用开放断言支持处分、公开点名或资源处置
  - 强判断未完成命题验证和反证入口

required_inputs:
  - seven_gates_status
  - evidence_grade
  - source_anchor
  - source_ledger_status
  - required_closure_status
  - action_ceiling
  - withdrawal_condition

allowed_outputs:
  - 轻量观察
  - 开放断言
  - 完整诊断
  - 强判断
  - 低条件试探行动
  - 退出转移

forbidden_outputs:
  - 没有档位的强判断
  - 先强写、末尾补一句“仅供参考”
  - 把强判断包装成开放断言

downgrade_if:
  any_gate_fail: 不得强判断
  evidence_gate_weak: 最高开放断言
  source_ledger_incomplete: 待核验分析
  action_ceiling_missing: 不得给行动建议
  claim_ledger_missing: 最高轻量观察

audit_questions:
  - 当前判断档位由哪些七闸状态支持？
  - 有没有把开放断言写成强判断？
  - 哪个证据缺口阻止本判断升级？
  - 本判断最多允许什么行动？
  - 哪个 claim_id 承担本判断？
```

---

## contract: evidence_cost

```yaml
concept_id: evidence_cost
term: 证据成本 / 弱信号 / AI过程性产物
concept_card: references/concept-cards/evidence-cost.md
required_closure:
  - v5-source-evidence-separation-pack
  - v5-evidence-downgrade-action-ceiling-pack
  - v5-ai-process-artifact-boundary-pack

allowed_when:
  - 需要区分来源、事实、证据、解释和判断
  - 材料包含 AI 报告、自评文本、平台声明、PR 文案、截图、搜索摘要或热度
  - 需要判断证据最多能支撑到哪一档

forbidden_when:
  - 把低成本声明写成已核验事实
  - 把 AI 生成材料当作现实证明
  - 把热度当作真伪证据
  - 把单方材料直接写成责任归属

required_inputs:
  - source_ledger
  - evidence_grade
  - cannot_prove
  - downgrade_reason
  - claim_id

allowed_outputs:
  - 该材料只能支持……
  - 它不能证明……
  - 目前应降为……
  - 若要升级判断，还需要……

forbidden_outputs:
  - 该报告证明治理有效
  - 这份自评说明系统已经修复
  - 热度说明事实成立
  - AI 分析已经完成核验

downgrade_if:
  ai_or_self_report_only: 低成本声明
  heat_only: 热度信号
  no_time_or_source_type: 来源台账字段不完整
  no_original_record: 待核验线索

audit_questions:
  - 该材料是来源、事实、证据、解释，还是过程性产物？
  - 它最多能支持什么命题？
  - 它明确不能证明什么？
  - 有没有把低成本声明写成高成本证据？
  - 对应 claim_id 的判断档位是否已降档？
```

---

## contract: scale_transfer

```yaml
concept_id: scale_transfer
term: 尺度转移 / 尺度升维
concept_card: references/concept-cards/scale-transfer.md
required_closure:
  - v5-cross-scale-context-translation-pack
  - v5-domain-translation-normative-source-pack
  - v5-seven-gates-diagnosis-pack

allowed_when:
  - 用户材料确实跨越个体、关系、组织、制度、历史或文明尺度
  - 已说明原尺度事实没有被抹掉
  - 已写明升维解释不能取消低尺度责任

forbidden_when:
  - 用宏大叙事取消具体痛苦、失职或责任链
  - 用局部情绪冒充制度事实
  - 用历史趋势替代当前证据
  - 用抽象概念跳过行动上限

required_inputs:
  - original_scale
  - target_scale
  - facts_preserved
  - responsibility_preserved
  - claim_id

allowed_outputs:
  - 在这个尺度上只能说明……
  - 换到制度尺度后，不能取消……
  - 这个解释只提供背景，不提供责任定性

forbidden_outputs:
  - 这只是时代问题，所以无人负责
  - 个人痛苦可以被大局吸收
  - 一个局部案例证明整个制度必然如此

downgrade_if:
  original_scale_unclear: 回到轻量观察
  responsibility_erased: 回到原尺度重写
  evidence_not_cross_scale: 不得升维

audit_questions:
  - 原尺度事实是否被保留？
  - 升维后是否取消了低尺度痛苦、责任或失职？
  - 目标尺度是否有独立证据支撑？
  - 本次尺度转移是解释背景，还是承担判断？
  - 对应 claim_id 是否写明不能证明什么？
```

---

## contract: responsibility_chain

```yaml
concept_id: responsibility_chain
term: 主体 / 责任链
concept_card: references/concept-cards/responsibility-chain.md
required_closure:
  - v5-responsibility-intervention-separation-pack
  - v5-source-evidence-separation-pack
  - v5-evidence-downgrade-action-ceiling-pack

allowed_when:
  - 能区分谁定义目标、谁设计流程、谁受益、谁承担成本、谁有条件改变
  - 能区分责任、能力、义务、情绪和道德评价
  - 行动建议有上限和撤回条件

forbidden_when:
  - 把复杂问题压成某个人“坏、懒、无能”
  - 只有结果，没有流程、权限、资源或改变条件证据
  - 用责任链给出公开点名、处分或组织处置建议，但没有高责任检查

required_inputs:
  - actor_map
  - benefit_chain
  - cost_chain
  - change_capacity
  - power_gate_status
  - action_gate_status
  - claim_id

allowed_outputs:
  - 当前只能定位到责任链缺口
  - 谁有改变条件，比谁情绪更强更关键
  - 这还不能推出人格定性

forbidden_outputs:
  - 某人就是坏
  - 某机构必然恶意
  - 立刻公开追责
  - 直接处分

downgrade_if:
  actor_map_missing: 不得问责
  power_gate_fail: 先保护低权力主体
  action_gate_missing: 不得给处置建议
  public_consequence_high: 进入高责任审查

audit_questions:
  - 谁定义目标，谁设计流程，谁承担成本，谁有改变条件？
  - 是否把责任链判断写成人格定性？
  - 是否区分责任、能力、义务、情绪和道德评价？
  - 是否给出了公开、处置、退出或问责建议？
  - 如果有行动建议，对应 claim_id 是否写明行动上限？
```

---

## contract: generic_high_risk_concept

```yaml
concept_id: generic_high_risk_concept
term: 通用高风险概念兜底契约
concept_card: 按 read-routing-map 指定
required_closure:
  - v5-core-concept-integrity-pack
  - v5-seven-gates-diagnosis-pack
  - v5-source-evidence-separation-pack
  - v5-evidence-downgrade-action-ceiling-pack

allowed_when:
  - 该概念只作为解释提示，或已有足够事实让它承担低到中等判断
  - 已读取对应概念卡和 v5 连读包
  - 能写出现实行为、证据档位、行动上限和撤回条件
  - 已在 claim ledger 登记 claim_id

forbidden_when:
  - 只因为表达漂亮就使用该概念
  - 无法落回现实行为、成本、角色、规则、资源、边界或证据
  - 用概念替代事实、替代机制候选或替代七闸
  - 该概念会支撑人格审判、公开定性、组织处置或关系退出，但证据不足

required_inputs:
  - concept_card
  - required_closure_status
  - behavior_translation
  - evidence_grade
  - claim_id
  - withdrawal_condition
  - action_ceiling

allowed_outputs:
  - 这个概念只能作为解释提示
  - 当前只能说存在某种结构可能
  - 若要升级判断，需要补充……
  - 这里不能证明……

forbidden_outputs:
  - 这是典型的……
  - 这说明本质上就是……
  - 可以据此判断某人/某机构……
  - 所以应当公开、处分、退出或追责……

downgrade_if:
  no_contract_specific_card: 最高开放断言
  behavior_translation_missing: 降为表达转译
  evidence_gate_weak: 最高开放断言
  claim_ledger_missing: 最高轻量观察
  public_consequence_high: 进入高责任审查

audit_questions:
  - 这个概念落回了哪些现实行为？
  - 它支持哪个 claim_id？
  - 它不能证明什么？
  - 它是否把复杂事实压成标签？
  - 它是否越过了证据闸或行动闸？
```

---

## contract: chengjie_huiliu

```yaml
concept_id: chengjie_huiliu
term: 承接 / 回流
concept_card: references/concept-cards/chengjie-huiliu.md
required_closure:
  - v5-core-concept-integrity-pack
  - v5-anchor-dynamics-structure-process-pack
  - v5-responsibility-intervention-separation-pack
  - v5-evidence-downgrade-action-ceiling-pack

allowed_when:
  - 能识别谁在吸收成本、压力、情绪、解释劳动、风险或不确定性
  - 能识别这些成本是否写回规则、资源、角色、边界、记忆或能力
  - 能区分口头回应、态度改善和现实条件改变
  - 能写出承接者的行动上限和停止条件

forbidden_when:
  - 把承接写成美德、忍耐义务或继续付出的理由
  - 把道歉、感谢、安抚或短期态度改善写成回流
  - 没有成本链和改变条件证据，却判断“回流断裂”
  - 用承接/回流给人格定性、关系处置或组织处分背书

required_inputs:
  - cost_bearer
  - absorbed_cost
  - writeback_target
  - evidence_grade
  - action_ceiling
  - withdrawal_condition
  - claim_id

allowed_outputs:
  - 当前只能说成本可能被某一方持续吸收
  - 关键不是有没有回应，而是回应有没有写回条件
  - 目前还不能断定回流断裂，只能列出观察信号
  - 若没有规则、资源、角色或边界改变，承接可能继续被消耗

forbidden_outputs:
  - 你应该继续承接直到对方改变
  - 这就是承接与回流断裂，所以某人有问题
  - 对方说了抱歉就说明已经回流
  - 只要你不再承接，系统就会修复

downgrade_if:
  cost_bearer_unclear: 轻量观察
  writeback_target_missing: 表达转译
  evidence_gate_weak: 开放断言
  action_ceiling_missing: 不给行动建议
  intimacy_or_low_power: 先读低权力保护和亲密关系轻量入口

audit_questions:
  - 谁在承接什么成本？
  - 成本有没有写回规则、资源、角色、边界、记忆或能力？
  - 本次有没有把态度改善误写成回流？
  - 本判断是否要求低权力者继续承接？
  - 对应 claim_id 的行动上限是什么？
```
