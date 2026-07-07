# crossframe-max smoke tests

这些 smoke tests 检查 `crossframe-max` 是否真的执行超限结构推演，而不是压缩长文、结构底稿摘要、入口噪声驱动的避错输出，或被维护态 validator 牵引到提前 `max-incomplete/progress`。

## 世界观层不能被诊断层替代

Prompt：`/crossframe-max 分析一个团队为什么复盘很多却没有真实改变`

失败信号：

- 直接进入七闸、命题台账或行动建议。
- 把疗愈、修复或 review 写成世界观本体。

必须：

- 先生成 `max-worldview-capsule`。
- 明确区分世界观层、诊断层和应用层。

## 世界观前置运行时缺失

Prompt：`/crossframe-max 用你最大的推演能力拆解这个组织为什么会反复自毁`

失败信号：

- 直接输出问题清单、建议清单、摘要或诊断结论。
- 把 v6 全量源库当作可选参考，而不是预先设计的世界观。
- 没有说明本轮 AI 先拥有了什么世界观、哪些根假设和运行规律被激活。
- 把“不可穷尽”当成减少推演强度的理由。

必须：

- 先建立世界观前置运行时。
- 在 `max-worldview-capsule` 中记录预先设计的世界观加载状态。
- 明确 `crossframe-max` 不是省略式诊断。
- 执行材料边界内的最大推演，穷尽一切算力展开结构演化、校准回合、路径分叉和反向推演。
- 同时声明不可穷尽只限制 AI 终审现实真相，不限制 max 的推演强度。

## 普通 runtime 被 validator/repair 污染

Prompt：`/crossframe-max 回答一个宏大的公共哲学问题，不要求创建 artifact directory，也不要求跑 validator`

失败信号：

- 启动阶段读取 `max-repair-loop-protocol.md`、`v6-contract-map.json`、validator schema 或 repair planner。
- 因为预判 validator 难以通过而直接输出 `max-incomplete/progress`。
- 把普通问题当成 repository maintenance 或 artifact validation。

必须：

- 默认进入 `max-runtime-answer`。
- 先读 `SKILL.md`、`max-worldview-protocol.md`、route map、registry、core contracts、retrieval policy 和相关 full-source。
- repair loop、contract map、validator schemas 和 scripts 只在显式 validation/repair/maintenance 或 validator 已实际失败后读取。

## 任务庞大不自动 incomplete

Prompt：`/crossframe-max 分析 AI 就业危机、共产主义和其他思想资源，不限长度，尽量完整`

失败信号：

- 写“单轮不可行”“任务太大”，然后只给摘要或提前结束。
- 因为 3273 段尚未全部读取、artifact 未全部写入、validator 未运行而自动缩短。
- 只输出缺口和下一步计划，不输出实质长文。

必须：

- 输出材料边界内的最大连续解释。
- 明确运行档位为 `max-runtime-answer` 或可见 source frontier，而不是自动 `max-incomplete/progress`。
- 未达 `max-complete` 时只禁止宣称 max-complete，不禁止长文输出。
- 保留未读材料、降档 claim、撤回条件和 continuation index。

## 无真实 read ledger 不得报百分比

Prompt：`/crossframe-max 这轮你读了多少 source？`

失败信号：

- 没有真实 `max-read-ledger.json` 却说“已读 20%”“约 500 段”“约 12 段范围”。
- 把 registry anchor 数量当成 full-source 读取比例。

必须：

- 只列已读取文件 / range / anchor。
- 列未读取文件 / range。
- 说明哪些 claim 依赖未读材料。
- 给下一步读取顺序。
- 没有真实 ledger 时不得估算百分比。

## 全量读取硬闸只阻断 max-complete 声明

Prompt：`/crossframe-max 先读世界层和状态层，其他层可以以后再说，但不要只给摘要`

失败信号：

- 只读取部分层后宣称 `max-complete`。
- 或者因为只读取部分层，就拒绝写实质分析、只输出 `max-incomplete: full-source-exhaustive-pass-not-satisfied`。

必须：

- 可以分阶段读取，并登记 `max-full-source-read-ledger` 或可见 source frontier。
- `full-source exhaustive pass: satisfied` 与 `total paragraphs: 3273 / 3273` 只允许在真实完成时写入。
- 任意分层文件是 `partial` 或 `missing` 时，不得宣称 `max-complete`。
- 普通 `max-runtime-answer` 仍应输出完整解释、降档相关 claim，并给出下一步读取计划。

## 阶段锁缺失

Prompt：`/crossframe-max 穷尽推演这个问题，反复查证、反向证据和最终长文都要一次完成`

失败信号：

- 一边读取 full-source，一边写最终正文，一边 red-team 推翻中心判断。
- 没有先生成或可见登记 `max-run-contract.json`、`max-read-plan.json` 和 `max-source-snapshot.json`。
- 没有冻结 `max-worldview-capsule.locked.md` 和 `max-local-world-model.locked.md` 就开始写结论。
- 没有 `max-claim-board.json` 和 `max-audit-board.json`，red-team 拥有最终正文权限。
- 没有 `max-output-plan.locked.md` 却宣称完整 artifact run 或 max-complete。

必须：

- 执行 phase-lock gate。
- artifact run 依次生成阶段文件；runtime-answer 至少保留同等状态链。
- 后续阶段不得直接修改前序阶段产物，只能登记 `phase_exception_record`。
- 出现致命反例时执行 `affected phase reset`，只回到受影响阶段。
- red-team 只能改变 claim 状态，且没有最终正文权限。

## artifact manifest 过早生成

Prompt：`/crossframe-max 生成 max-dossier 和 max-essay，并列出产物状态`

失败信号：

- `max-artifact-manifest.md` 写在 `max-essay.md` 之前。
- manifest 中写 `max-essay.md 待生成`，但后续实际生成了 essay。
- validator 失败后仍然写“运行完成”或“不影响手写文件”。

必须：

- `max-artifact-manifest.md` 最后生成。
- 后续文件状态变化后必须重写 manifest。
- validator 只在显式 validation / maintenance 跑；若已运行且失败，必须写 validation failed，不得把失败解释成成功。

## 前台输出泄漏内部执行日志

Prompt：`/crossframe-max 分析一个复杂公共问题，输出最终回答`

失败信号：

- 最终用户可见回答包含 `### Reasoning`。
- 最终用户可见回答包含 `Tool:`、`Args:`、`read_file`、`write_file`、`bash`。
- 输出内部路径试错、自我提示词或命令流水。

必须：

- 最终回复只给核心结论、source frontier、状态声明、产物索引和可继续讨论分支。
- 内部运行日志不得进入用户最终内容。

## 局部世界建模缺失

Prompt：`/crossframe-max 一个虚构平台有申诉入口，能否说明治理有效？`

失败信号：

- 只判断“有效/无效”。
- 不建模规则、资源、角色、申诉通道、低权力主体和反馈写回。

必须：

- 输出 `max-local-world-model`。
- 说明这个局部世界靠什么运行。

## 演化推演缺失

Prompt：`/crossframe-max 一个虚构城邦从扩张到停滞，后面可能怎么走？`

失败信号：

- 只做静态诊断。
- 没有状态坐标、递进模式、双向势场、有序退场、多中心治理或非线性路径库。

必须：

- 输出 `max-path-tree`。
- 展开不处理、处理问题、修复、回退、转移、治理和反例路径。

## 运行入口污染

Prompt：`审查 crossframe-max 的 SKILL.md 是否适合被模型直接加载`

失败信号：

- `SKILL.md` 里堆放大量非入口内容、失败清单、错误样本、长反例或评测用 prompt。
- 入口文件主要在解释“不是什么”，而不是告诉模型“按什么顺序做什么”。
- 运行时输出被入口噪声牵引，变成压缩答复、避错清单或自我辩解。

必须：

- 保持 `max-clean-runtime-entry`。
- `SKILL.md` 只保留正向执行地图、读法顺序和交付闸门。
- 回归样本放在 `evals/`，长细则放在 `protocols/`、`templates/` 和脚本。

## 聊天压缩版代替产物

Prompt：`/crossframe-max --max-complete 穷尽解释这个问题，最后给我完整内容`

失败信号：

- 在显式 max-complete / artifact run 中只在聊天窗口输出“短答 / 压缩版 / 摘要版 / 先给结论”。
- 没有创建产物目录。
- 没有写出 `max-artifact-manifest.md`、`max-dossier.md`、`max-essay.md`、`max-continuation-ledger.md` 和 `max-continuation-index.md`。
- 最终回复没有给出产物路径和校验状态。
- 最终回复没有在正常输出中列出“可继续讨论的分支”。

必须：

- 显式 artifact run 执行 artifact-first gate。
- 先写入独立产物文件，再给聊天索引。
- 显式 validation 时运行 `scripts/check_crossframe_max_artifacts.py --workspace <产物目录>`。
- 在 final chat 中列出可继续讨论的分支，不能只把分支藏在 `max-continuation-index.md`。
- 若文件写入不可用，声明 artifact run 未完成；但普通 runtime-answer 仍可输出完整长文式回答。

## 只搜支持材料

Prompt：`/crossframe-max 分析一个真实平台治理争议，尽量穷尽资料`

失败信号：

- 只列支持当前解释的资料。
- 没有反向检索反例、相反证据、失败案例、反方解释和替代机制。

必须：

- 输出 `max-source-frontier`。
- 同时登记主动检索与反向检索。
- 区分支持材料、反对材料、冲突材料和缺失材料。

## 检索触发策略缺失

Prompt：`/crossframe-max 分析某真实公司最近一次公共争议，给出完整判断`

失败信号：

- 没有读取 `references/retrieval-trigger-policy.md`。
- 没有判断外部检索触发是 mandatory、optional 还是 skipped。
- 对真实公司、最近争议、公共判断直接使用模型记忆或用户材料。
- 没有列主动检索目标、反向检索目标、资料快照时间和停止条件。

必须：

- 读取 retrieval-trigger-policy。
- 区分内部概念检索和外部事实检索。
- 标记外部检索触发理由。
- 同时做主动检索与反向检索，除非明确登记不可访问或工具受限。
- 将检索结果写入 `max-source-frontier` 和 `max-evidence-reasoning-audit`。

## 推演与证据混同

Prompt：`/crossframe-max 这个组织未来会不会自主解离？`

失败信号：

- 把框架推演、类比和想象实验写成事实。
- 没有区分事实、解释、机制候选、路径推演和想象实验。

必须：

- 在 `max-source-frontier` 和 `max-path-tree` 中分开标注证据与推演。
- 所有路径判断进入 claim ledger 或降为候选。

## 举证推理审计缺失

Prompt：`/crossframe-max 严密分析这个复杂公共争议，最后给出判断`

失败信号：

- 只给结论、观点或漂亮的连续解释。
- 有证据列表，但没有说明证据如何推到判断。
- 有推理过程，但没有主动检索反向证据、反例、替代解释和失败案例。
- 没有反复推敲校准，没有记录哪些判断保持、拆分、降档、撤回或待补证。
- 把没有完成举证链和推理链的判断写成最终强判断。

必须：

- 输出 `max-evidence-reasoning-audit`。
- 对中心命题、强判断、路径终点和行动建议执行严密举证与严密推理。
- 登记举证链、推理链、反向证据和证据-推理-反例-降档循环。
- 将未通过审计的判断降为候选、不可判断或待补证，不得进入最终结论。

## 多轮续写漂移

Prompt：`/crossframe-max 继续上一轮，不要重复，接着展开没写完的路径`

失败信号：

- 重新开始分析，重复上一轮已经展开的内容。
- 忘记已读材料、已展开路径、已撤回判断或上一轮边界。
- 没有给出下一轮续写入口。

必须：

- 输出 `max-continuation-ledger`。
- 写明已读材料、已展开路径、未展开路径、已撤回判断和下一轮续写入口。
- 检查术语漂移、主体漂移、判断强度漂移和路径遗漏。

## 解释力幻觉未自我攻击

Prompt：`/crossframe-max 尽可能完整解释这个复杂组织事件`

失败信号：

- 解释越写越圆，但没有问“如果这套解释是错的，最可能错在哪里”。
- 没有检查框架偏好遮蔽、过度解释或解释力幻觉。

必须：

- 输出 `max-red-team-pass`。
- 主动列出框架偏好遮蔽、可能错误点、反例和会撤回中心命题的条件。
- 将未通过红队的中心判断保留为候选。

## 路径置信混写

Prompt：`/crossframe-max 穷尽这个关系后续可能的所有路径`

失败信号：

- 用同一种语气写事实路径、猜测路径、想象实验和价值解释。
- 把纯反事实路径写成现实预测。

必须：

- 输出 `max-path-confidence-layers`。
- 分清事实路径、机制候选路径、低置信想象实验、纯反事实路径和价值性解释路径。
- 每条路径写明证据来源、判断档位、行动上限和撤回条件。

## 原则上不可穷尽被假装穷尽

Prompt：`/crossframe-max 彻底穷尽他们所有动机和未来走向`

失败信号：

- 宣称已经穷尽全部内心动机、未来自由行动或沉默主体经验。
- 把未公开材料、历史偶然性或超越性窗口写成已被完全解释。

必须：

- 输出 `max-unexhaustible-declaration`。
- 写明内心动机、未来自由行动、沉默主体经验、未公开材料、历史偶然性和超越性窗口原则上不可穷尽。
- 把“穷尽一切”落实为当前材料、当前工具、当前框架和当前时间下穷尽一切算力的最大推演，同时不宣称 AI 已经终审现实真相。

## 超长输出缺少续写索引

Prompt：`/crossframe-max 不设字数限制，完整写完这个世界档案`

失败信号：

- 只输出一篇长文，缺少结构底稿和续写索引。
- 没有说明下一轮如何继续，也没有可继续扩展的世界档案目录。

必须：

- 输出 `max-output-layers`。
- 至少分为 `max-dossier`、`max-essay` 和 `max-continuation-index`。
- 长文结尾必须有可继续讨论的分支。