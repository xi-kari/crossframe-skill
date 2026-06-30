# v5.0 半量化 DLC 构念图谱

v5.0 半量化 DLC 构念图谱只定义可观察结构变量，不新增本体概念。构念用于限制判断、暴露不确定性、触发补证和记录写回，不用于生成对象总分、人格分、组织健康总分或文明阶段总分。

## 运行时接入边界

- DLC 不触发时，不读取本表，不补写分数。
- 触发 DLC 后，构念只解释七闸、证据、机制、反例和行动上限；不得替代 claim ledger、source_anchor、概念契约或 review。
- 普通关系、组织和公共议题不得自动输出分数。用户要求量化时，只能输出结构剖面，并先说明不能证明什么、缺哪些证据、最高行动上限和撤回条件。
- 高责任判断只能用于降档、补证、阻断发布或收窄行动上限，不能用构念读数授权处分、排名、资格、公开定性、发布通过或 `substantive_pass`。
- `score_visibility` 必须登记为 `hidden`、`profile_only` 或 `user_requested_profile`。默认 `hidden`；公开输出只允许剖面，不允许合成总分。

| construct_id | 中文名 | 来源接口 | 现实问题 | 禁止误用 | 升格条件 | 可观察信号 | 最低证据 | 撤回条件 | 相关工作表 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| object_boundary_clarity | 对象边界清晰度 | intake / 对象闸 | 本次诊断对象、时间窗和不判断事项是否清楚 | 对象价值判断 | 能改变对象界定或不判断事项 | 对象、时间窗、受影响对象、不判断事项可列明 | intake 记录和对象边界说明 | 对象被扩大、缩小或替换时重跑 | seven-gates-quant-rubric.md |
| evidence_support_degree | 证据可支撑度 | evidence ledger / 证据闸 | 材料能支撑什么判断档位 | 来源权威崇拜 | 能改变判断档位或撤回条件 | 来源、证据、解释和判断分离 | 来源台账、证据台账、反例搜索状态 | 关键来源不可核验或反例成立时撤回 | evidence-ledger-v5-dlc.md |
| scale_consistency | 尺度一致性 | 尺度闸 | 是否发生跨尺度偷换 | 宏大叙事正确性 | 能改变尺度窗口或不可外推边界 | 个人、关系、组织、制度尺度被分开说明 | 尺度窗口和转译条件 | 高尺度叙事抹掉低尺度痛苦或责任时撤回 | seven-gates-quant-rubric.md |
| responsibility_chain_traceability | 责任链可追踪度 | mechanism candidates / 责任闸 | 谁造成、受益、承接、能改变 | 人格责任总分 | 能改变责任链或授权链 | 造成、受益、承接、改变条件可回指 | 责任链材料和机制候选 | 关键责任主体或授权链变化时撤回 | mechanism-update-rules.md |
| observation_reflexivity_risk | 观测反身性风险 | 观测闸 | 诊断、评分、发布是否改变对象 | 对象本质判断 | 能改变发布边界或停止条件 | 表演、污名、报复、自证风险可列明 | 观测前基线和发布边界 | 评分或发布改变对象行为时重跑 | seven-gates-quant-rubric.md |
| low_power_counterexample_entry | 低权力反例入口 | 权力闸 | 受影响者是否能安全申诉、补证、反驳 | 形式程序存在证明 | 能改变判断、行动上限、工具或版本写回 | 代理提交、匿名、反报复、反馈写回路径存在 | 入口说明、保护机制、实际写回记录 | 入口无法改变判断或带来报复风险时撤回 | counterexample-register.md |
| action_ceiling_clarity | 行动上限清晰度 | action ceiling / 行动闸 | 当前最多能做什么、不能做什么 | 行动授权 | 能改变行动边界、停止条件或扩大条件 | 行动上限、停止条件、撤回条件清楚 | 命题台账和行动边界 | 行动被用于处分、排名或公开定性时撤回 | seven-gates-quant-rubric.md |
| feedback_writeback_degree | 反馈写回程度 | 核心概念 / 回流 | 反馈是否改变规则、资源、角色、边界或记忆 | 满意度 | 能改变机制候选或修复判断 | 反馈进入规则、资源、角色、记忆的证据 | 前后版本、授权链、资源变化记录 | 反馈只被记录但不改变条件时降级 | mechanism-update-rules.md |
| repair_window_feasibility | 修复窗口可行度 | healing / low condition action | 是否存在低风险、可撤回、可观察动作 | 和解命令 | 能改变低条件行动或退出转移边界 | 有小范围、低风险、可观察、可停止动作 | 行动资源、风险边界、承接条件 | 行动风险超过当前证据档位时撤回 | seven-gates-quant-rubric.md |
| counterexample_writeback_strength | 反例写回强度 | framework governance | 反例是否改变文本、流程、工具或边界 | 反例收集数量 | 能改变版本日志、模板、校验器或发布边界 | 反例导致降档、修订或暂停使用 | 反例登记、版本写回、工具修改 | 反例只被附录化、不改变规则时撤回 | counterexample-register.md |

## 禁止合并项

- 不得把对象边界、证据可支撑度和责任链追踪度合并成“可信度总分”。
- 不得把低权力反例入口和行动上限清晰度合并成“治理成熟度总分”。
- 不得把反馈写回程度和修复窗口可行度合并成“修复成功率”。
- 不得把任何构念转写为人格、组织健康、关系质量或文明阶段分数。
