# max-essay

`max-essay` 是 `crossframe-max` 的独立完整长文。它不设默认字数上限，承担最终完整解释，不能用摘要替代正文。

## 正文主导原则

- `max-essay` 是最终完整解释层，不是 `max-dossier` 的摘要。
- `max-essay` 必须建立在世界观前置运行时上：先说明预先设计的世界观如何进入对象，再展开局部世界的结构演化。
- 普通 `/crossframe-max` 默认生成 `max-runtime-answer`：可以输出完整长文式回答、source frontier、反向推演、撤回条件和续写索引，但不得宣称 `max-complete`。
- `max-complete` / artifact run 必须建立在阶段锁通过后：`max-run-contract.json`、`max-read-plan.json`、`max-source-snapshot.json`、`max-worldview-capsule.locked.md`、`max-local-world-model.locked.md`、`max-claim-board.json`、`max-audit-board.json` 和 `max-output-plan.locked.md` 必须已经存在。
- 没有 `max-output-plan.locked.md`，不得宣称完整 artifact run 或 `max-complete`；普通 runtime-answer 不得因此缩短为短答。
- `max-complete` 必须建立在 `max-full-source-read-ledger` 通过后：正文或结尾产物清单必须写明 `full-source exhaustive pass: satisfied`、`total paragraphs: 3273 / 3273`，并说明没有 `partial` / `missing` read status 进入 `max-complete`。
- 普通 runtime-answer 如果 full-source 尚未全部读取，必须写明 source frontier、未读文件、受影响 claim、降档条件和 continuation plan；不得把未达 `max-complete` 写成完成，也不得因此简化正文。
- 没有真实 `max-read-ledger.json` 时，不得输出读取百分比或估算已读段落数。
- `max-complete` essay 必须能回指四个结构化台账：`max-read-ledger.json`、`max-claim-ledger.json`、`max-concept-hit-ledger.json`、`max-evidence-reasoning-audit.json`。
- `max-essay` 不是省略式诊断，必须完成材料边界内的最大推演，把穷尽一切算力后的拆解、校准、路径和撤回条件写成连续解释。
- `artifact-first gate` 只在 artifact run 强制；文件写入不可用时，普通 runtime-answer 可以在聊天中输出完整长文式回答，但必须声明不是 `max-complete`。
- 自动校验的最低阈值是：`max-essay` 可见字符数不得低于 `max-dossier` 的 1.6 倍。
- 换言之，max-essay 必须至少达到 max-dossier 的 1.6 倍；强完成应达到 2.2 倍；最大完成应达到 3.0 倍，或剩余内容只属于非阻断续写分支。
- 如果短于这个阈值，只能算“结构底稿完成，完整解释正文未完成”。
- 正文必须把 dossier 的结构发现转化为连续解释，不能只是 dossier 的摘要、标题串联、表格改写或结论摘录。
- 正文必须完整展开运行机制、时间演化、主体位置、路径分叉、处理问题、反例、不可判断区、超越性窗口和续写入口。
- 正文必须体现 `max-evidence-reasoning-audit` 的结论：中心命题如何经过严密举证、严密推理、反向证据检查和反复推敲校准，哪些判断被保持、降档、拆分、撤回或留在补证队列。
- 解释覆盖率必须检查：局部世界、运行规律、问题形成、路径演化、处理问题、伪修复、资料前沿、主体位置矩阵、路径置信分层、反向推演、超越性窗口、不可判断区、撤回条件、不可穷尽声明和续写索引是否进入正文。

## 必须做到

- 从局部世界入口写起，不从术语开场。
- 完整解释这个局部世界如何运行。
- 写出核心概念如何被结构变量命中，而不是词命中；非当前术语必须先归一到 v6 分层。
- 说明 concept-registry lookup：哪些概念先查 registry 再读 full-source，哪些概念出现 neighbor hit、conflict hit 或 gap hit；概念注册表不替代 full-source。
- 说明 full-source exhaustive pass：普通 runtime-answer 说明 source frontier 和未完成处；max-complete 才写 `full-source exhaustive pass: satisfied` 与 `total paragraphs: 3273 / 3273`。
- 展开运行规律、问题定位、演化路径、处理问题和反例。
- 说明 `max-source-frontier`：retrieval-trigger-policy 状态、外部检索触发理由、资料快照时间、主动检索、反向检索、缺失材料、冲突材料、缺席主体和停止条件。
- 外部检索失败不得自动使整轮失败；只降档依赖该事实的 claim，结构解释与思想谱系可以继续写。
- 说明 `max-evidence-reasoning-audit`：举证链、推理链、反向证据、证据-推理-反例-降档循环和输出前状态。
- 说明 phase-lock gate：冻结型中间产物如何把候选命题、审计、输出计划串成状态链。
- 说明 `max-transcendence-window`：不能解释不等于超越性；只把开放行动、误读风险、撤回条件和不可升格的未知分开写清。
- 说明连续运行状态：本轮已读材料、已展开路径、未展开路径、已撤回判断和下一轮续写入口。
- 说明主体位置矩阵：行动者、承接者、受影响者、旁观者、制度主体、沉默者、退出者和未来主体不能被强势材料吞没。
- 说明路径置信分层：事实路径、机制候选路径、低置信想象实验、纯反事实路径和价值性解释路径不能混成同一种强度。
- 说明反向推演：如果这套解释是错的，最可能错在哪里，哪些地方存在框架偏好遮蔽和解释力幻觉。
- 说明不可穷尽声明：内心动机、未来自由行动、沉默主体经验、未公开材料、历史偶然性和超越性窗口不能被假装穷尽。
- 说明产物优先交付与输出分层：`max-artifact-manifest.md`、结构底稿、完整长文和续写索引如何互相承接。
- 若本轮经过 repair loop，正文结尾必须说明 validator failure 如何处理：哪些 claim 被降档、撤回，哪些阶段被重建，哪些问题进入 max-incomplete 或续写队列。
- 正文不得把 repair plan 当作完成证明；只有 validator pass 且 final_output_allowed=true 才能宣称 max-complete。
- 保留不可判断区、撤回条件和行动上限。
- 不把框架写成现实终审，不把世界观写成万能解释机器。

## 正文结构

```text
# 标题

开篇：这个局部世界正在发生什么。

第一部分：它靠什么运行。

第二部分：它的问题不是单点故障，而是哪组运行规律出了偏差。

第三部分：如果不处理，会出现哪些演化路径。

第四部分：路径置信分层：哪些是事实路径，哪些是机制候选路径，哪些只是低置信想象实验、纯反事实路径或价值性解释路径。

第五部分：如果处理，哪些路径能改变结构，哪些只是伪修复。

第六部分：概念注册表命中、资料前沿、主体位置矩阵、超越性窗口、反向推演、不可判断区和撤回条件。

第七部分：举证链、推理链、反向证据与反复推敲校准后，哪些判断保持，哪些降档、撤回或待补证。

结尾：把解释回落到现实行动边界，并附产物清单与续写索引。

普通 runtime-answer 产物清单必须包含：运行档位；phase-lock gate 状态；局部世界；资料前沿；retrieval-trigger-policy；max-continuation-index；不可穷尽声明；未读材料和续写入口。

max-complete 产物清单必须额外包含：max-run-contract.json；max-read-plan.json；max-source-snapshot.json；max-worldview-capsule.locked.md；max-local-world-model.locked.md；max-claim-board.json；max-audit-board.json；max-output-plan.locked.md；full-source exhaustive pass: satisfied；total paragraphs: 3273 / 3273；max-full-source-read-ledger；max-read-ledger.json；max-claim-ledger.json；max-concept-hit-ledger.json；max-evidence-reasoning-audit.json；max-validator-report.json；max-repair-plan.json（如本轮发生 validation failure）；read status: full / partial / missing；stage 8 final read audit。
```

## 禁止

- 禁止只输出提纲或项目符号。
- 禁止只在聊天里输出压缩版、摘要版或短答后宣称 max 完成。
- 禁止因为任务庞大、单轮输出压力、3273 段尚未全部读取、artifact 未全部写入或 validator 未运行而自动缩短为摘要。
- 禁止没有真实 `max-read-ledger.json` 时自报读取百分比或估算段落数。
- 禁止没有 `max-output-plan.locked.md` 就宣称完整 artifact run 或 max-complete。
- red-team 没有最终正文权限；反向证据必须先改变 claim 状态。
- 禁止用一个合并阅读版替代 `max-artifact-manifest.md`、`max-dossier.md`、`max-essay.md`、`max-continuation-ledger.md` 和 `max-continuation-index.md`。
- 禁止把 `max-dossier` 当正文。
- 禁止为了显得完整而不加区分地堆概念。
- 禁止跳过 concept-registry lookup 后凭记忆使用概念。
- 禁止把 registry 条目当作定义，概念定义必须回到 full-source paragraph id。
- 禁止在触发 retrieval-trigger-policy 时跳过主动检索或反向检索；若检索失败，登记失败并降档相关 claim。
- 禁止在 full-source exhaustive pass 未写明 `full-source exhaustive pass: satisfied` 和 `total paragraphs: 3273 / 3273` 时宣称 max-complete。
- 禁止让 `partial` 或 `missing` read status 进入 max-complete；普通 runtime-answer 必须登记并降档，而不是直接短答。
- 禁止让宏观解释取消低尺度事实和责任链。
- 禁止把演化路径写成命运预言。
- 禁止把处理问题写成处置授权。
- 禁止把未找到证据写成证据不存在。
- 禁止把框架推演、类比或想象实验写成事实材料。
- 禁止把不可解释处直接写成爱或超越性。
- 禁止把爱写成忍耐义务；原则是：不把爱写成忍耐义务，必须保留退出保护。
- 禁止用超越性取消责任链、伤害事实、补证义务或边界保护。
- 禁止省略反向推演、自我攻击和解释力幻觉检查。
- 禁止省略 `max-evidence-reasoning-audit`，不得在没有举证链、推理链、反向证据和降档记录时输出最终强判断。
- 禁止让强势主体、可检索主体或材料最多者吞没主体位置矩阵。
- 禁止把事实路径、机制候选路径、低置信想象实验、纯反事实路径和价值性解释路径写成同一强度。
- 禁止把原则上不可穷尽的对象写成已经穷尽。
- 禁止超长输出缺少输出分层和续写索引。
- 禁止在最终用户可见回答中包含 `### Reasoning`、`Tool:`、`Args:`、`read_file`、`write_file`、`bash` 或内部路径试错。