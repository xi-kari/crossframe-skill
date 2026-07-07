# Max Worldview Protocol

本协议定义 `crossframe-max` 的最大展开顺序。核心原则：先加载用户预先设计的世界观，让 AI 拥有 CrossFrame 的世界结构视野，再把对象当作局部世界推演其运行和演化。

在本模式中，哪怕用户只给出“一件事”，也要先把这件事当作一个局部世界来对待，再展开概念命中、运行规律、问题结构、处理路径和演化分支。max 不是省略式诊断，而是材料边界内的最大推演：穷尽一切算力拆解对象、校准判断、展开路径，并把不能终审的现实部分留在不可穷尽声明中。

## 0. 世界观前置运行时

`crossframe-max` 的第一动作是建立世界观前置运行时，而不是直接回答用户问题。执行顺序：

1. 读取 `references/v6-full-source/00-index.md`，建立 full-source read ledger。
2. 读取 `references/source_manifest.json` 和 `references/v6-route-map.yaml`，确认 3273 / 3273 全量源库、任务路由和本轮优先层。
3. 读取与当前任务最相关的 v6 分层源文件，先形成 `max-worldview-capsule`。
4. 将 `max-worldview-capsule` 明确写成“本轮 AI 使用的预先设计的世界观”，登记根假设、元约束、运行规律、可证伪边界和禁用误读。
5. 再进入局部世界建模，把用户对象放入世界结构演化中推演。
6. 在输出前完成 full-source exhaustive pass，确认所有分层源文件均已进入 read ledger。

这意味着世界观不是参考资料，也不是输出附录，而是 max 的运行前置条件。任何只套用诊断表、只给结论、只做摘要、只写行动建议或跳过世界观加载的输出，都不能算作 `crossframe-max` 完成。

## 0.1 运行入口降噪

`max-clean-runtime-entry`：运行入口只保留正向执行地图、读法顺序和交付闸门。失败样本、错误案例、反例压力测试和回归样本放在 `evals/`；长细则放在本协议、模板和校验脚本中。执行时以本协议的正向流程为主，不把错误样本当作生成模板。

## 0.2 运行档位

`crossframe-max` 有三个运行档位。档位必须写入 `max-run-contract.json` 和 `max-artifact-manifest.md`：

- `max-complete`：完整 full-source exhaustive pass、阶段锁、artifact-first、template-fidelity、longform-dominance、route-ledger gate 和 validator 全部满足后才可宣称完成。
- `max-design-review`：用于 skill、prompt、agent、工具、模板、脚本和运行时设计。必须使用 `skill_design` route，登记 route concepts、design decision、v6 rule、反向证据、撤回条件和行动上限。该档位可以完成设计审查，但不得伪称完成完整 max 长文。
- `max-incomplete/progress`：环境、上下文、权限、工具或时间不足时，只输出读态、缺口、下一阶段读取计划和 `max-incomplete:*`，不得宣称完成。

`max-design-review` 的对象也是局部世界。skill、prompt、agent、模板、脚本和 validator 必须被建模为过程性结构对象：入口边界、协议顺序、知识源、产物接口、反馈写回、反例库、模型适配和行动上限都要进入局部世界模型。

## Phase Lock Rule / 阶段锁规则

`crossframe-max` 不得把读取、审计和最终写作作为同时进行的义务。每个阶段先形成冻结型中间产物，再进入下一阶段。

强制顺序：

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
```

阶段产物：

- `max-run-contract.json`：用户请求、运行模式、禁止行为、最终输出许可状态。
- `max-read-plan.json`：本轮读取计划、route key、route version、优先层、最终必须补齐层、概念触发、route required fields 和检索触发。
- `max-source-snapshot.json`：本轮 source base、P0001-P3273 覆盖状态、60 个表格索引状态、`source_snapshot_id`。
- `max-worldview-capsule.locked.md`：本轮预先设计的世界观启动核。
- `max-local-world-model.locked.md`：局部世界模型；只建模对象、边界、尺度、主体位置、承接链、反馈通道和运行规律候选，不下最终判断。
- `max-claim-board.json`：冻结候选命题板；所有判断先是 `candidate`，不得直接进入正文。
- `max-audit-board.json`：冻结审计板；red-team 只能把 claim 状态转为 `supported`、`downgraded`、`split`、`withdrawn`、`needs_search`、`unexhaustible` 或 `final`，且没有最终正文权限。
- `max-output-plan.locked.md`：冻结输出计划，列明进入正文、降档表达、撤回、不可判断和不得写强的 claim。没有 `max-output-plan.locked.md`，不得生成 `max-essay`。

后续阶段不得直接改写已经冻结的前序产物；异常只登记为 `phase_exception_record`；处理规则为 `affected phase reset`，仅回到受影响阶段。反向证据只改变 claim 状态。

validator failure 也必须遵守 phase lock。失败后不得直接 patch final Markdown，必须登记失败原因，并回到 affected phase。

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

最终写作只允许使用 `max-output-plan.locked.md` 中已经分配状态的 claim。`max-red-team-pass` 和 `max-evidence-reasoning-audit` 可以改变 claim 状态，但不得绕过 `max-audit-board.json` 直接改写最终正文。

## 1. 三层分离

### 世界观层

世界观层回答“框架如何理解世界”。它包括：对象不是孤立物，而是结构过程；世界由多尺度嵌套系统组成；承接者、锚点、保护变量、反馈通道、资源、记忆和边界共同维持局部世界；反馈只有写回规则、资源、角色、边界、记忆或能力，才改变结构；时间不可逆；观测、命名、诊断、评分和发布会进入对象行动链；爱和开放行动不能被结构完全推出，也不能被制度命令；根假设只是可证伪、可边界收缩、可暂停使用的工作假设。

### 诊断层

诊断层是世界观进入事件后的分析动作。它包括对象界定、事实/证据分离、七闸、机制候选、判断档位、claim ledger、反例、撤回条件和行动上限。

### 应用层

应用层包括处理问题、疗愈、转移、低条件试探行动、组织修复、公共治理、DLC 审计、写作表达和 review。应用层不能反向改写世界观本体。

## 2. 局部世界建模

把用户对象当作一个局部世界，而不是一个等待贴标签的案例。

必须建模：对象边界、尺度层级、主体与位置、锚点与保护变量、承接与回流、动力与通道、结构负荷、观测入口和外部扰动。

## 3. 主体位置矩阵

max 模式必须把缺席主体检查扩展为主体位置矩阵，输出 `max-position-matrix`。不能只沿着可见材料、强势主体、材料最多者、最会说话者或权力最高者推演。

必须列出行动者、承接者、受影响者、旁观者、制度主体、沉默者、退出者和未来主体。每个位置必须登记材料可见度、权力位置、承担成本、行动条件、退出条件、被误读风险和对应 claim_id。

## 4. 全量源库读取与概念语义邻域

概念命中不是词命中；它是结构变量命中。

读取原则：

- registry 只做定位，不替代 full-source。
- `layer digest` 只做阶段连续性的临时摘要，不能替代源文件逐段读取、paragraph id 回指和最终回查。
- `00-table-index.md` 与 `tables/` 保留 Word 表格行列结构；当 `source_paragraph_ids` 属于表格或表格关系影响意义时，必须读取对应 table 文件并同时记录 table id。
- 读取可以按问题阶段分层推进；最终结果输出前必须完成 `max-full-source-read-ledger`。
- 最终硬闸是 `full-source exhaustive pass: satisfied` 与 `total paragraphs: 3273 / 3273` 同时成立。
- 任何 full-source 文件的 `read status: full / partial / missing` 不是 `full` 时，只能输出读取进度或 `max-incomplete: full-source-exhaustive-pass-not-satisfied`，不得输出最终结果。
- Markdown 读态不能替代结构化台账；最终产物必须生成 `max-read-ledger.json`、`max-claim-ledger.json`、`max-concept-hit-ledger.json` 和 `max-evidence-reasoning-audit.json`。

分阶段读取策略：

1. `stage 0 source inventory`：读取 source manifest、route map、00-index、heading index、term index 和 table index。
2. `stage 1 boundary guide`：读取 source envelope、guide、boundary layer。
3. `stage 2 worldview layer`：读取 world layer，建立 worldview capsule。
4. `stage 3 state layer`：读取 state layer，建立演化推演基础。
5. `stage 4 interface layer`：读取 interface layer，建立证据、判断和反馈写回接口。
6. `stage 5 tool layer`：读取 tool layer，建立诊断工具、开放断言、输出层和工具边界。
7. `stage 6 intervention and application`：读取 intervention 与 application layer。
8. `stage 7 governance layer`：读取 governance layer。
9. `stage 8 final read audit`：回查全部分层文件，确认 read status、首尾 paragraph id、chunks、layer digest 和未闭合缺口。

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
3. 读取 `references/concept-registry/index.md`，执行 concept-registry lookup。
4. 每个命中都必须继续读取对应 full-source paragraph ids 和相邻段落，并写回 `max-concept-graph` 与 `max-concept-hit-ledger.json`。
5. 读取 full-source index，建立 exhaustive pass 计划。
6. 按当前任务阶段先读相关分层文件。
7. 无论阶段读取顺序如何，最终结果输出前必须全量读取并完成全量读取登记。
8. 读取 v6-core-contracts，确认 allowed_when、forbidden_when、required_inputs、downgrade_if。
9. 在 `max-claim-ledger.json` 中登记 claim_id、source_anchor、判断档位、行动上限、撤回条件、source paragraph id、反向证据状态和 full-source exhaustive pass 状态。
10. 进入 `max-evidence-reasoning-audit`。
11. 进入 `route-ledger gate`。

未完成全量读取不得输出最终结果。只能输出读取进度、缺失分层、下一步读取计划或 `max-incomplete: full-source-exhaustive-pass-not-satisfied`。

### 4.1 skill_design route

当对象是 skill、prompt、agent、工具、模板、脚本、产物协议或运行时设计时，必须使用 `skill_design` route。`max-read-plan.json` 必须登记 route key、route version、required layers、required concepts、required outputs 和 forbidden outputs checked。

## 5. 概念注册表命中

输出 `max-concept-graph`，包括 direct hit、neighbor hit、conflict hit、gap hit、已读取概念卡、已检查概念契约、source paragraph id、需要补读或降档的概念。概念注册表不能直接替代正文定义。

## 6. 资料前沿与外部检索

凡涉及真实机构、真实政策、当前事实、公共判断、历史事实、法律、医疗、金融、平台规则、公司、人物或最新资料，必须读取 `references/retrieval-trigger-policy.md`。未找到证据不得写成证据不存在。检索失败不得写成现实不存在。

## 7. 路径置信分层

所有路径必须分成事实路径、机制候选路径、低置信想象实验、纯反事实路径、价值性解释路径。每条路径必须写明证据来源、判断档位、行动上限、撤回条件和公开边界。

## 8. 举证推理审计

对中心命题、强判断、路径终点和行动建议执行：

```text
材料 -> 结构变量 -> 概念命中 -> 机制判断 -> 路径推演 -> 行动上限
```

每个中心 claim 必须登记举证链、推理链、反向证据、证据-推理-反例-降档循环、已保持判断、已拆分命题、已降档判断、已撤回判断、已进入不可判断区和已进入补证队列。

## 9. Red Team Pass

最终表达前必须自我攻击：如果这套解释是错的，最可能错在哪里；哪些主体被框架偏好遮蔽；哪些概念只是词义相似；哪些反例会撤回中心命题；哪些行动建议会制造二次风险。

## 10. 超越性窗口

不能解释不等于爱、意义或超越性。超越性窗口只登记候选痕迹。不得用超越性取消责任链、伤害事实、补证义务或退出保护。

## 11. 不可穷尽声明

每次 `crossframe-max` 都必须写不可穷尽声明。不可穷尽包括内心动机、未来自由行动、沉默主体经验、未公开材料、历史偶然性、超越性窗口和现实资料本身。

## 12. 输出分层

`max-output-layers` 必须包含 `max-dossier`、`max-essay`、`max-continuation-ledger`、`max-continuation-index` 和 `max-artifact-manifest.md`。`max-essay` 不能只是 dossier 摘要，必须是连续完整长文。