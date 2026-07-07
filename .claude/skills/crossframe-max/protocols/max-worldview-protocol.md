# Max Worldview Protocol

本协议定义 `crossframe-max` 的最大展开顺序。核心原则：先加载用户预先设计的世界观，让 AI 拥有 CrossFrame 的世界结构视野，再把对象当作局部世界推演其运行和演化。

在本模式中，哪怕用户只给出“一件事”，也要先把这件事当作一个局部世界来对待，再展开概念命中、运行规律、问题结构、处理路径和演化分支。max 不是省略式诊断，而是材料边界内的最大推演：穷尽一切算力拆解对象、校准判断、展开路径，并把不能终审的现实部分留在不可穷尽声明中。

## 0. 世界观前置运行时

`crossframe-max` 的第一动作是建立世界观前置运行时，而不是直接回答用户问题。执行顺序：

1. 读取 `references/v6-full-source/00-index.md`，建立本轮 source inventory。
2. 读取 `references/source_manifest.json` 和 `references/v6-route-map.yaml`，确认 full-source primary knowledge base、任务路由和本轮优先层。
3. 读取与当前任务最相关的 v6 分层源文件，先形成 `max-worldview-capsule`。
4. 将 `max-worldview-capsule` 明确写成“本轮 AI 使用的预先设计的世界观”，登记根假设、元约束、运行规律、可证伪边界和禁用误读。
5. 再进入局部世界建模，把用户对象放入世界结构演化中推演。
6. 在输出前登记 source frontier：已读、未读、需补读、需降档、需续写。

这意味着世界观不是参考资料，也不是输出附录，而是 max 的运行前置条件。任何只套用诊断表、只给结论、只做摘要、只写行动建议或跳过世界观加载的输出，都不能算作 `crossframe-max` 的合格运行。

## 0.1 运行入口降噪

`max-clean-runtime-entry`：运行入口只保留正向执行地图、读法顺序和交付闸门。失败样本、错误案例、反例压力测试和回归样本放在 `evals/`；长细则放在本协议、模板和校验脚本中。执行时以本协议的正向流程为主，不把错误样本当作生成模板。

维护态材料不得污染普通运行入口：`max-repair-loop-protocol.md`、`v6-contract-map.json`、validator schemas、repair planner 和脚本只在 repository maintenance、显式 artifact validation、显式 repair 或 validator 已实际失败后读取。

## 0.2 运行档位

`crossframe-max` 有四个运行档位。档位必须写入 `max-run-contract.json`，或在无法写文件时写入最终回答的运行状态区：

- `max-runtime-answer`：普通 `/crossframe-max` 默认档位。目标是最大连续解释、局部世界建模、source frontier、red-team、不可穷尽声明和续写索引。该档位可以输出完整长文式回答，但不得宣称 `max-complete`。
- `max-complete`：完整 full-source exhaustive pass、阶段锁、artifact-first、template-fidelity、longform-dominance、route-ledger gate 和 validator 全部满足后才可宣称完成。
- `max-design-review`：用于 skill、prompt、agent、工具、模板、脚本和运行时设计。必须使用 `skill_design` route，登记 route concepts、design decision、v6 rule、反向证据、撤回条件和行动上限。该档位可以完成设计审查，但不得伪称完整 max 长文完成。
- `max-incomplete/progress`：只在必需文件不可访问、工具权限缺失、用户中止、外部事实检索连续失败且核心结论完全依赖该事实，或显式 artifact-validation 模式下 validator 已实际失败时使用。任务庞大、单轮输出长、3273 段尚未读完、validator 未运行、上下文压力高，不是自动 incomplete 理由。

## 0.3 max-complete-source-gate

只有宣称 `max-complete` 时，才必须同时满足：

```text
full-source exhaustive pass: satisfied
total paragraphs: 3273 / 3273
all layered files read status: full
max-full-source-read-ledger: complete
stage 8 final read audit: complete
```

若这些条件未满足，禁止使用 `max-complete` 字样；但普通 `max-runtime-answer` 不得因此缩短为摘要或提前终止。正确动作是继续分阶段读取、登记 source frontier、降档依赖未读材料的 claim、给出 continuation plan，并输出材料边界内的最大解释。

## 0.4 读取百分比规则

没有真实 `max-read-ledger.json` 时，禁止输出读取百分比、估算已读段落数或“约 20% / 500 段 / 12 段范围”这类数字。只能登记：

```text
已读取文件 / range / anchor：
未读取文件 / range：
依赖未读材料的 claim：
已降档判断：
下一步读取顺序：
```

## Phase Lock Rule / 阶段锁规则

`crossframe-max` 不得把读取、审计和最终写作作为互相污染的义务。每个阶段先形成中间状态，再进入下一阶段。

完整 artifact run 的强制顺序：

```text
max-run-contract.json
-> max-read-plan.json
-> max-source-snapshot.json
-> max-worldview-capsule.locked.md
-> max-local-world-model.locked.md
-> max-claim-board.json
-> max-audit-board.json
-> max-output-plan.locked.md
-> max-dossier.md / max-essay.md / max-continuation-index.md
-> max-artifact-manifest.md
```

阶段产物：

- `max-run-contract.json`：用户请求、运行模式、禁止行为、最终输出许可状态。
- `max-read-plan.json`：本轮读取计划、route key、route version、优先层、最终必须补齐层、概念触发、route required fields 和检索触发。
- `max-source-snapshot.json`：本轮 source base、P0001-P3273 覆盖状态、60 个表格索引状态、`source_snapshot_id`。
- `max-worldview-capsule.locked.md`：本轮预先设计的世界观启动核。
- `max-local-world-model.locked.md`：局部世界模型；只建模对象、边界、尺度、主体位置、承接链、反馈通道和运行规律候选，不下最终判断。
- `max-claim-board.json`：冻结候选命题板；所有判断先是 `candidate`，不得直接进入正文。
- `max-audit-board.json`：冻结审计板；red-team 只能把 claim 状态转为 `supported`、`downgraded`、`split`、`withdrawn`、`needs_search`、`unexhaustible` 或 `final`，且没有最终正文权限。
- `max-output-plan.locked.md`：冻结输出计划，列明进入正文、降档表达、撤回、不可判断和不得写强的 claim。没有 `max-output-plan.locked.md`，不得宣称完整 artifact run。
- `max-artifact-manifest.md`：最终文件状态清单，必须最后生成；任何后续文件变化都必须重写 manifest。

普通 `max-runtime-answer` 如果环境不支持写文件，也要在可见回答里保留这些状态链的逻辑顺序，但不得因为无法创建文件而缩短为短答。

后续阶段不得直接改写已经冻结的前序产物；异常只登记为 `phase_exception_record`；处理规则为 `affected phase reset`，仅回到受影响阶段。反向证据只改变 claim 状态。

validator failure 只在显式 validation / repair 模式触发 repair loop。失败后不得直接 patch final Markdown，必须按 `max-repair-loop-protocol.md` 生成 repair plan，并回到 affected phase。普通 runtime 不预判 validator 失败，也不因预判 validator 难以通过而提前 `max-incomplete`。

状态表：

```text
candidate -> supported -> final
candidate -> downgraded
candidate -> split
candidate -> withdrawn
candidate -> needs_search
candidate -> unexhaustible
supported -> downgraded / split / withdrawn / final
needs_search -> supported / downgraded / withdrawn / unexhaustible
```

最终写作只允许使用已经分配状态的 claim。`max-red-team-pass` 和 `max-evidence-reasoning-audit` 可以改变 claim 状态，但不得绕过审计直接改写最终强判断。

## 1. 三层分离

### 世界观层

世界观层回答“框架如何理解世界”。它包括：对象不是孤立物；世界由多尺度嵌套系统组成；承接者、锚点、保护变量、反馈通道、资源、记忆和边界共同维持局部世界；反馈只有写回规则、资源、角色、边界、记忆或能力，才改变结构；时间不可逆；观测、命名、诊断、评分和发布会进入对象行动链；爱和开放行动不能被结构完全推出，也不能被制度命令；根假设只是可证伪、可边界收缩、可暂停使用的工作假设。

### 诊断层

诊断层是世界观进入事件后的分析动作。它包括对象界定、事实/证据分离、七闸、机制候选、判断档位、claim ledger、反例、撤回条件和行动上限。

### 应用层

应用层包括处理问题、疗愈、转移、低条件试探行动、组织修复、公共治理、DLC 审计、写作表达和 review。应用层不能反向改写世界观本体。

## 2. 局部世界建模

把用户对象当作一个局部世界，而不是一个等待贴标签的案例。

必须建模：

- 对象边界：本次局部世界是什么，不是什么。
- 尺度层级：个人、关系、组织、制度、历史、文明中哪些层级被激活。
- 主体与位置：谁能行动，谁承担成本，谁获益，谁缺少退出或申诉。
- 锚点与保护变量：什么维持方向、记忆、判断、资源和信任。
- 承接与回流：谁吸收压力、风险、情绪、解释劳动或责任，这些是否写回结构。
- 动力与通道：行动为什么启动，如何被转译，支撑通道是否足够。
- 结构负荷：哪些维护债、隐藏成本、虚稳态和熵增正在累积。
- 观测入口：本次分析、命名、发布或行动会怎样改变对象。
- 外部扰动：哪些制度、技术、历史、平台、市场、家庭或公共力量进入局部世界。

## 3. 主体位置矩阵

max 模式必须把缺席主体检查扩展为主体位置矩阵，输出 `max-position-matrix`。不能只沿着可见材料、强势主体、材料最多者、最会说话者或权力最高者推演。

必须列出行动者、承接者、受害者 / 受影响者、旁观者、制度主体、沉默者、退出者和未来主体。每个位置必须登记材料可见度、权力位置、承担成本、行动条件、退出条件、被误读风险和对应 claim_id。

## 4. 全量源库读取与概念语义邻域

概念命中不是词命中；它是结构变量命中。

读取原则：

- registry 只做定位，不替代 full-source。
- `layer digest` 只做阶段连续性的临时摘要，不能替代源文件逐段读取、paragraph id 回指和最终回查。
- `00-table-index.md` 与 `tables/` 保留 Word 表格行列结构；当 `source_paragraph_ids` 属于表格或表格关系影响意义时，必须读取对应 table 文件并同时记录 table id。
- 读取可以按问题阶段分层推进；`max-complete` 输出前必须完成 `max-full-source-read-ledger`。
- `max-complete` 最终硬闸是 `full-source exhaustive pass: satisfied` 与 `total paragraphs: 3273 / 3273` 同时成立。
- 普通 `max-runtime-answer` 中，partial / missing 读态只阻断 `max-complete` 声明，不阻断最大解释；但必须登记 source frontier、降档相关 claim、给出下一步读取计划。
- Markdown 读态不能替代结构化台账；`max-complete` 产物必须生成 `max-read-ledger.json`、`max-claim-ledger.json`、`max-concept-hit-ledger.json` 和 `max-evidence-reasoning-audit.json`。

分阶段读取策略：

1. `stage 0 source inventory`：读取 `references/source_manifest.json`、`references/v6-route-map.yaml`、`references/v6-full-source/00-index.md`、`00-heading-index.md`、`00-term-index.md` 和 `00-table-index.md`，核对 full-source primary knowledge base、文件清单、paragraph 总数、表格结构索引、任务路由和每个分层文件的范围。
2. `stage 1 boundary guide`：读取 `00-source-envelope.md`、`01-guide.md`、`02-boundary-layer.md`，建立材料来源边界、使用边界、准入条件、误用防护和本轮不可越界处。
3. `stage 2 worldview layer`：读取 `03-world-layer.md`，建立世界观层、核心概念、根假设、结构动力学和本轮 `max-worldview-capsule`。
4. `stage 3 state layer`：读取 `04-state-layer.md`，建立状态坐标、生命周期、双向势场、非线性路径和演化推演基础。
5. `stage 4 interface layer`：读取 `05-interface-layer.md`，建立证据、判断、交互、反馈写回和观测反身性接口。
6. `stage 5 tool layer`：读取 `06-tool-layer.md`，建立诊断工具、开放断言、输出层和工具使用边界。
7. `stage 6 intervention and application`：读取 `07-intervention-layer.md`、`08-application-layer.md`，建立处理问题、疗愈、修复、转移、治理、表达和领域应用路径。
8. `stage 7 governance layer`：读取 `09-governance-layer.md`，建立证伪、误用防护、治理边界、替代接口和公开表达上限。
9. `stage 8 final read audit`：只在 `max-complete` / artifact validation 中强制。按 `00-source-envelope.md` 到 `09-governance-layer.md` 顺序回查全部分层文件，确认每个文件的 `read status`、首尾 paragraph id、已读 chunks、`layer digest` 和未闭合缺口。

`max-full-source-read-ledger` 字段：

```text
file:
expected paragraph range:
chunks read:
first paragraph id:
last paragraph id:
read status: full / partial / missing
layer digest:
unresolved gaps:
audit result:
```

判断流程：

1. 从局部世界模型中识别结构变量。
2. 读取 `references/v6-route-map.yaml`，按问题类型确定优先读取层、必查概念和禁用输出。
3. 读取 `references/concept-registry/index.md`，执行 concept-registry lookup，将结构变量映射到概念邻域、候选概念、冲突概念和 gap hit。
4. 每个命中都必须继续读取对应 full-source paragraph ids 和相邻段落，并把命中写回 `max-concept-graph`；在 `max-complete` / artifact run 中还要写入 `max-concept-hit-ledger.json`。
5. 按当前任务阶段先读相关分层文件；普通 runtime 不因尚未读完全部 3273 段而停止解释，但不得宣称全量完成。
6. 进入 `max-evidence-reasoning-audit`，对中心命题执行严密举证、严密推理、反向证据检查和反复推敲校准。
7. 进入 `route-ledger gate`，按 `references/v6-route-map.yaml` 校验 `route_key`、required layers、required concepts、required outputs、forbidden outputs、concept registry 命中、行动上限和审计回指。

若 validator 在显式 validation 模式发现 `concept_id` 存在但 `source_ranges_from_registry` 与 registry anchor 不匹配，必须回到 `concept_hit` phase。若 validator 发现 `contract_id` 不存在或不对应 `concept_id`，必须回到 concept contract maintenance；本轮不得通过补写 Markdown 完成。

`route-ledger gate` 在维护态也是 repair classifier 的输入。每个 route-ledger failure 必须映射到 `error_type`、`affected_phase`、`downstream_reset` 和 `repair_action`。

最低链路：

```text
v6-route-map -> concept-registry lookup -> full-source index -> worldview-runtime capsule -> staged layer reads -> source frontier -> concept contract -> claim ledger -> evidence-reasoning audit -> route-ledger gate
```

未完成全量读取时，不得宣称 `max-complete`。普通 `max-runtime-answer` 必须输出 source frontier、缺失分层、下一步读取计划、降档判断和不可穷尽声明，而不是缩成短答。

### 4.1 skill_design route

当对象是 skill、prompt、agent、工具、模板、脚本、产物协议或运行时设计时，必须使用 `skill_design` route。

`max-read-plan.json` 必须登记：`route_key`、`route_map_version`、`route_required_layers`、`route_required_concepts`、`route_required_outputs`、`route_forbidden_outputs_checked`。

`max-concept-hit-ledger.json` 必须登记：`concept_id`、`trigger_variable`、`registry_anchor`、`source_ranges_from_registry`、`source_ranges_read`、`contract_id`、`contract_checked`。

`max-claim-ledger.json` 中每个设计判断必须登记：`design_decision_id`、`v6_rule_ids`、`claim_type`、`source_anchor`、`evidence_status`、`action_limit`、`downgrade_condition`、`withdrawal_condition`。

设计审查可以使用 `max-design-review` 完成，不要求生成完整长文，但必须保留 route-ledger gate、反向证据和行动上限。

## 5. 概念注册表命中

输出 `max-concept-graph`，包括 direct hit、neighbor hit、conflict hit、gap hit、已读取概念卡、已检查概念契约、source paragraph id、需要补读或降档的概念。

概念注册表不能直接替代正文定义。概念定义必须回到 v6 full-source paragraph ids；如果本轮尚未读取到对应段落，必须降档为 concept candidate，并进入 continuation index。

## 6. 资料前沿与外部检索

凡涉及真实机构、真实政策、当前事实、公共判断、历史事实、法律、医疗、金融、平台规则、公司、人物或最新资料，必须读取 `references/retrieval-trigger-policy.md`。

外部检索失败不得自动使整轮 `crossframe-max` 失败。它只影响依赖外部事实的 claim 强度。结构解释、路径推演、思想谱系和概念比较可以继续输出，但必须标注：检索尝试、失败原因、受影响 claim、降档条件、后续补证入口。

未找到证据不得写成证据不存在。检索失败不得写成现实不存在。

## 7. 路径置信分层

所有路径必须分成：事实路径、机制候选路径、低置信想象实验、纯反事实路径、价值性解释路径。不能把所有路径写成同一种强度。

每条路径必须写明：证据来源、判断档位、行动上限、撤回条件和公开边界。

## 8. 举证推理审计

对中心命题、强判断、路径终点和行动建议执行：

```text
材料 -> 结构变量 -> 概念命中 -> 机制判断 -> 路径推演 -> 行动上限
```

每个中心 claim 必须登记：举证链、推理链、反向证据、证据-推理-反例-降档循环、已保持判断、已拆分命题、已降档判断、已撤回判断、已进入不可判断区、已进入补证队列。

## 9. Red Team Pass

最终表达前必须自我攻击：

- 如果这套解释是错的，最可能错在哪里？
- 哪些主体被框架偏好遮蔽？
- 哪些概念看似命中，实际只是词义相似？
- 哪些反例会撤回中心命题？
- 哪些行动建议会制造二次伤害？

未通过 red-team 的判断必须降档、拆分、撤回或进入补证队列。

## 10. 超越性窗口

不能解释不等于爱、意义或超越性。超越性窗口只登记候选痕迹：开放行动、非工具性、非占有性、真实成本但不转化成债权、保留对方自由、保留边界。

不得把爱写成忍耐义务。不得用超越性取消责任链、伤害事实、补证义务或退出保护。

## 11. 不可穷尽声明

每次 `crossframe-max` 都必须写不可穷尽声明。不可穷尽包括：内心动机、未来自由行动、沉默主体经验、未公开材料、历史偶然性、超越性窗口和现实资料本身。

“穷尽一切”只意味着在当前材料、工具、框架和时间内穷尽一切算力，不意味着 AI 终审现实真相。

## 12. 输出分层

`max-output-layers` 必须包含：

- `max-dossier`：结构底稿。
- `max-essay`：连续完整长文，不得只是 dossier 摘要。
- `max-continuation-ledger`：已读、未读、已展开、未展开、已降档、已撤回。
- `max-continuation-index`：下一轮如何继续，不重复上一轮。
- `max-artifact-manifest.md`：仅 artifact run 必须存在，且必须最后生成。

## 13. 前台输出卫生

最终用户可见回答不得包含：

- `### Reasoning`
- `Tool:` / `Args:` / `read_file` / `write_file` / `bash`
- 内部路径试错、命令流水、自我提示词
- “Let me...” 或“我现在读取某文件”的内部执行自述

最终聊天回复承担交付索引、核心结论、状态声明、source frontier 和可继续讨论分支功能。