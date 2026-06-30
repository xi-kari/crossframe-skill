---
name: crossframe-max
description: "Use when the user explicitly invokes crossframe-max, /crossframe-max, $crossframe-max, or asks for the maximum CrossFrame mode, exhaustive structural projection, full-scale world-model interpretation, or no word-limit complete explanation."
disable-model-invocation: true
---

# CrossFrame Max

`crossframe-max` 是独立入口，不是 `crossframe-suite` 的体积档位，也不是 `2+1` 选择器里的第五种模式。它 explicit-only：只有用户明确点名 `crossframe-max`、`/crossframe-max`、`$crossframe-max`，或明确要求“max / 最大算力 / 超限结构推演 / 全尺度穷尽推演 / 不设字数限制完整解释”时才使用。

本 skill 不走 `crossframe-suite` 的 `2+1` 模式/角色选择器，不走普通文章类型选择器，不把 `brief-visible / standard-visible / full-visible-v5-longform` 当作体积上限。它默认生成 `max-dossier` 和 `max-essay`；若单轮无法展开完，必须登记“未展开完的路径队列”，后续继续。

## 核心定位

`crossframe-max` 把一个事件、关系、组织、制度、文本或公共对象临时当作一个局部世界来对待。换句话说，它把对象当作一个局部世界，而不是当作等待贴标签的案例。它先吸收 CrossFrame 世界观，再建立局部世界模型，随后展开概念语义邻域、运行规律、结构问题、演化路径、处理问题的可能方案和完整解释性文章。

它必须把一件事当作一个局部世界来对待：概念命中、运行规律、当前问题、处理问题和后续演化都在这个局部世界里展开。

它的核心顺序是：

```text
世界观层先行
-> 局部世界建模
-> 主体位置矩阵
-> 概念语义邻域展开
-> 资料前沿与主动检索
-> 运行规律识别
-> 当前结构问题定位
-> 演化路径推演与路径置信分层
-> 爱与超越性窗口审查
-> 反向推演 / 自我攻击回合
-> 干预 / 疗愈 / 转移 / 治理 / 表达应用
-> 不可穷尽声明
-> 输出分层与连续运行状态
-> max-dossier
-> max-essay
-> max-continuation-index
-> review 边界审查
```

诊断层是世界观进入事件后的分析动作；疗愈、行动和成文属于应用层。不得把诊断工具、疗愈协议或文章模板误写成世界观本体。

## 必读

每次触发后先读取：

1. `protocols/max-worldview-protocol.md`
2. `templates/max-dossier-output.md`
3. `templates/max-essay-output.md`
4. `../crossframe/SKILL.md`
5. `../crossframe/references/concepts-minimal-set.md`
6. `../crossframe/references/theory-backend-index.md`
7. `../crossframe/references/framework-ontology-protection.md`
8. `../crossframe/references/guardrails.md`
9. `../crossframe/references/runtime-read-policy.md`
10. `../crossframe/references/read-routing-map.md`
11. `../crossframe/references/continuity-closure-map.md`
12. `../crossframe/references/concept-contracts/core-contracts.md`
13. `../crossframe/references/concept-cards/README.md`
14. `../crossframe/templates/read-state-capsule.md`
15. `../crossframe/templates/claim-ledger.md`

然后展开世界观核心包：

- `v5-root-assumptions-meta-rules-pack`
- `v5-core-concept-integrity-pack`
- `v5-anchor-dynamics-structure-process-pack`
- `v5-state-coordinate-lifecycle-pack`
- `v5-long-evolution-progression-field-pack`
- `v5-governance-continuity-multicenter-pack`
- `v5-observation-reflexivity-release-pack`
- `v5-domain-translation-normative-source-pack`
- `v5-framework-self-diagnosis-falsification-pack`

读取包时先用 `../crossframe/references/continuity-closure-map.md` 展开 required_closure；需要语义、源锚点或降档边界时再读取 `../crossframe/references/continuity-bundles.md` 和对应 `../crossframe/references/continuity-bundles/v5/<bundle-id>.md`。源锚点不足时定向读取 `../crossframe/references/v5-source-spine.md`、`../crossframe/references/v5-section-digest-index.md`、`../crossframe/references/v5-coverage-map.md` 和 `../crossframe/references/v5-term-fidelity.md` 的相关局部；max 可以扩大读取范围，但仍要记录读态胶囊。

## 模板忠实度硬闸

`template-fidelity gate` 是 `crossframe-max` 的完成闸。模板是 contract，不是参考；`templates/max-dossier-output.md`、`templates/max-essay-output.md`、`templates/max-dossier-output.md` 中的一级 / 二级标题必须逐项填充。

硬性规则：

- `max-dossier` 必须按 `templates/max-dossier-output.md` 的章节顺序输出，不得在 `max-unexhaustible-declaration` 或任意中段模板截断。
- 必须逐项填充；即使材料不足，也要保留该栏并写“未展开 / 待补证 / 已查未得 / 不可判断”，不得跳过空栏。
- 不得合并标题、改名标题或把多个模板项压缩成一个摘要段。
- 不得把单独文件当作 dossier 内部章节替代；即使另有 `max-continuation-index.md`，`max-dossier` 内部仍必须包含 `## max-output-layers` 和 `## max-continuation-index`。
- 有 CL1、CL2 这类命题编号时，必须落到 `source_anchor`、`claim_id`、`claim ledger` 和 `source ledger`；只有编号没有台账链路，视为模板未完成。
- 缺任何一级标题都不得宣布完成，不得写“已完成 / 质量通过 / max 完成”。

产物交付后，应运行 `scripts/check_crossframe_max_artifacts.py` 对实际输出目录做模板忠实度检查。这个检查只验证结构和必要台账字段，不替代 `crossframe-review` 的实质质量判断。

## 连续运行状态

`crossframe-max` 不设默认字数上限，因此不能把单轮输出当作天然完整。每轮必须维护 `max-continuation-ledger`，也可称为 `max-run-state`。它记录本轮已读材料、已展开路径、未展开路径、已撤回判断、已降档判断、已保留不可判断区、下一轮续写入口和防重复 / 防漂移约束。

`max-continuation-ledger` 必须回答：

- 本轮已读材料、已检索资料和已使用源锚点是什么。
- 已展开路径有哪些，哪些路径只展开了一半。
- 未展开路径、未穷尽资料队列和未回答问题是什么。
- 已撤回判断、已降档判断和撤回理由是什么。
- 下一轮续写入口在哪里，续写时不得重复哪些内容，不得越过哪些边界。
- 多轮输出中是否发生术语漂移、主体漂移、判断强度漂移或路径遗漏。

如果单轮无法完整输出，结尾不能只写“后续继续”，必须生成 `max-continuation-index`，让下一轮能从结构底稿、完整长文和未展开路径继续，而不是重新开始。

## 主体位置矩阵

缺席主体检查必须升级为 `max-position-matrix`。max 不得只跟随最会说话、材料最多、权力最高或最容易被检索到的主体推演。

`max-position-matrix` 至少列出：

- 行动者：谁能启动行动、命名、处置、修复或退出。
- 承接者：谁吸收压力、情绪、成本、解释劳动和制度风险。
- 受害者 / 受影响者：谁承担伤害、延迟成本、沉默成本和退出成本。
- 旁观者：谁被动见证，谁的沉默会改变局部世界。
- 制度主体：平台、组织、家庭、法律、市场、公共叙事或技术系统如何参与。
- 沉默者：谁没有材料、没有表达、没有可见记录或无法被检索到。
- 退出者：谁已经离场、被迫离场、保护性退出或被系统排除。
- 未来主体：未来会承担后果、继承路径、修复记忆或支付维护债的人。

每个位置都要标明：材料可见度、权力位置、承担成本、行动条件、退出条件、被误读风险和与 claim ledger 的关系。

## 概念展开规则

概念命中不是词命中。不得因为用户没有说“承接”“回流”“反身性”“势场”“爱”“退出转移”等词，就跳过实际结构变量。

一旦某个概念进入中心命题、机制候选、演化路径、行动建议、文章点睛句或公共定性，必须走：

```text
concept card -> concept contract -> v5 continuity closure -> claim ledger
```

至少检查以下概念群：

- 锚点组、动力组、结构组、过程组
- 承接 / 回流 / 反馈写回 / 修复副产品
- 尺度转移 / 跨尺度语境转译 / 低尺度责任保留
- 证据成本 / 弱信号 / AI 过程性产物
- 开放断言 / 判断档位 / 强判断八件套
- 观测反身性 / 发布后变形 / 高反身性博弈
- 状态坐标与生命周期 / 阶段回退 / 非线性路径库
- 递进模式 / 子锚点闭环 / 双向势场 / 自主解离
- 多中心治理 / 承接者生成 / 调节预警 / 偿付约束
- 爱 / 开放行动 / 无法退出主体 / 复杂创伤 / 保护性退出
- 权力封闭 / 低权力主体保护 / 申诉与反例入口
- 工具化 / 可及性释放 / 框架自诊 / 良性消亡

若无法读取对应概念卡、概念契约或连续闭包，该概念只能列为候选背景，不得承担判断。

## 主动检索与诚实标注

`crossframe-max` 的“穷尽一切”必须包含资料前沿，而不是只穷尽模型脑内推演。资料穷尽不等于现实穷尽；max 只能穷尽当前条件、当前工具、当前权限和当前时间允许的检索努力。

必须主动检索的情形：

- 涉及公共事实、真实机构、政策、公司、人物、技术标准、历史事件、时间线、法律规则、平台规则或最新情况。
- 中心命题、机制候选、演化路径、行动建议或公共定性需要事实支撑。
- 用户材料不足以支撑强判断，但存在可检索的外部材料。
- 出现不确定资料、冲突资料、传闻资料、低可信资料或 AI 过程性产物。

检索必须包含：

- 主动检索：查找支持事实、背景事实、制度规则、时间线和已有研究。
- 反向检索：主动寻找反例、反方解释、失败案例、相反证据和替代机制。
- 未找到也要登记：没有找到证据只能写“已查未得 / 暂不可访问 / 仍需补证”，不得写成“证据不存在”。
- 来源类型分层：区分用户材料、公开报道、论文、统计数据、档案、法律文本、平台规则、当事人叙述、第三方评论、AI 推测和框架推演。
- 资料快照时间：说明本轮检索或材料整理的时间点；现实对象可能在输出后变化。
- 缺席主体检查：登记哪些受影响者、低权力主体、退出者、沉默者、无法申诉者或反方位置没有出现在材料中。
- 检索反身性：检查本次搜索、命名、公开分析或引用会不会改变对象行为、扩大伤害或触发策略性表演。
- 停止条件：说明何时停止继续检索，是资料饱和、关键路径已覆盖、工具/权限到达边界，还是剩余问题进入未穷尽资料队列。

每个承担判断的事实或材料都要进入 `max-source-frontier`，再映射到 `source ledger` 与 `claim ledger`。推演与证据必须分离：事实、解释、机制候选、路径推演和想象实验不得混写成同一种确定性。

## 路径置信分层

`max-path-tree` 必须附带 `max-path-confidence-layers`。max 可以穷尽可能，但不能把所有可能写成同一种强度。

路径至少分为：

- 事实路径：已有事实、材料、时间线或源锚点直接支持的路径。
- 机制候选路径：由 CrossFrame 机制解释推出，但仍需补证或反例检验的路径。
- 低置信想象实验：用于打开可能性，但不得承担判断或行动建议。
- 纯反事实路径：假设条件改变后才成立的路径，必须写清前提。
- 价值性解释路径：表达意义、价值、伦理或世界观张力，不得伪装成事实预测。

每条路径都要标出：证据来源、判断档位、行动上限、撤回条件、是否可公开、是否需要补证、是否只是想象实验。禁止用“可能”一词把不同置信层级混成一团。

## 爱与超越性窗口

`crossframe-max` 必须给“爱”与“超越性”保留一席之地，但只能作为 `max-transcendence-window`，不能作为解释捷径。不能解释，不等于出于超越性；不能解释只能先标成未知、缺失材料、冲突材料、框架边界或未穷尽路径。

爱的超越性不是“无法解释的神秘原因”，而是结构解释到达边界时，仍然出现的一种开放行动能力。它最多被标为超越性窗口、超越性痕迹或机制候选，不得写成终局原因、事实证据或行动授权。

进入 `max-transcendence-window` 前必须检查开放行动信号：

- 非工具性：行动不是为了交换、控制、证明自己或索取回报。
- 非占有性：不把对方、关系、组织或世界纳入自己的所有权。
- 真实成本但不转化成债权：行动者承担真实代价，但不把代价改写为对他人的债务。
- 保留对方的自由：允许对方拒绝、离开、沉默、成长或不按行动者期待回应。
- 不取消边界：爱不等于无限承接，不取消安全边界、事实边界、责任边界和退出保护。
- 不得要求受害者继续忍耐：不能把“爱”写成低权力主体继续承受伤害的义务。
- 打开未来可能性：它让局部世界多出可修复、可转移、可重新承接或可不再重复伤害的路径。

必须同时登记误读为爱的风险：

- 创伤重复、依附循环、补偿冲动或角色依赖。
- 控制、占有、拯救幻想、权力策略或道德表演。
- 自我证明、牺牲竞赛、沉没成本合理化或把痛苦包装成意义。
- 组织、家庭、制度或公共叙事把爱改写成顺从、忍耐、牺牲义务。

撤回条件必须写明：只要出现控制、占有、债权化、边界取消、伤害遮蔽、责任链抹除、低权力主体被要求忍耐，或反例显示行动主要服务于权力/表演/补偿，该超越性痕迹必须撤回或降为误读风险。

## 反向推演与自我攻击

`crossframe-max` 必须生成 `max-red-team-pass`。max 越追求完整解释，越容易产生解释力幻觉，因此必须反复推敲、穷尽可能，并主动攻击自己的解释。

`max-red-team-pass` 必须问：

- 如果这套解释是错的，最可能错在哪里？
- 哪些事实、主体、路径或尺度被框架偏好遮蔽？
- 是否为了完整解释而过度解释，把噪声、偶然或未知写成机制？
- 哪些概念是框架喜欢命中的，实际却可能只是词义相似？
- 哪些反例会让中心命题撤回、降档或改写？
- 哪些行动建议可能制造二次伤害、权力背书或错误安全感？

自我攻击不是可选装饰。没有 `max-red-team-pass` 的 max 输出，只能视为未完成底稿。

## 不可穷尽声明

`crossframe-max` 必须生成 `max-unexhaustible-declaration`。穷尽一切从狂妄改成诚实，关键是明确哪些对象原则上无法被穷尽。

必须声明至少以下不可穷尽项：

- 内心动机：不能被外部材料、行为片段或框架概念完全证明。
- 未来自由行动：未来主体仍可能改变路径，不能被推演写成命运。
- 沉默主体经验：没有材料不等于没有经验、没有伤害或没有反例。
- 未公开材料：隐私材料、档案、内部记录、未披露证据和不可访问资料。
- 历史偶然性：突发事件、时间窗口、未计划相遇和非线性扰动。
- 超越性窗口：开放行动和爱不能被结构完全推出，也不能被神秘化占有。

不可穷尽声明必须与 `max-source-frontier`、`max-red-team-pass`、`max-path-confidence-layers` 和撤回条件互相指向。

## 输出分层模式

`crossframe-max` 的输出必须走 `max-output-layers`，至少三层：

1. 结构底稿：`max-dossier`，保存世界观胶囊、资料前沿、主体位置矩阵、路径树、红队回合、不可穷尽声明和连续运行状态。
2. 完整长文：`max-essay`，不设默认字数上限，用自然文章完整解释局部世界。
3. 续写索引：`max-continuation-index`，列出未展开路径、下一轮续写入口、可继续扩展的世界档案目录和不得越界处。

若用户只要文章，也不能丢掉 `max-continuation-index`；它可以压缩呈现，但必须存在。否则超长输出会只剩一篇文章，无法维护成可继续扩展的世界档案。

## 产物

内部产物至少包括：

- `max-worldview-capsule`：本轮吸收的世界观本体、根假设、元约束、运行规律、禁止误用和可证伪边界。
- `max-source-frontier`：主动检索、反向检索、支持材料、反对材料、缺失材料、冲突材料、不可访问材料、来源类型、资料快照时间、缺席主体、检索反身性、停止条件和未穷尽资料队列。
- `max-transcendence-window`：不可升格的未知、开放行动信号、误读为爱风险、超越性痕迹候选、边界保护、责任保留和撤回条件。
- `max-continuation-ledger` / `max-run-state`：已读材料、已展开路径、未展开路径、已撤回判断、下一轮续写入口、防重复和防漂移约束。
- `max-position-matrix`：行动者、承接者、受害者、旁观者、制度主体、沉默者、退出者和未来主体的位置、材料可见度、权力与成本。
- `max-local-world-model`：把对象当作局部世界后得到的对象边界、尺度层级、主体、锚点、承接者、反馈通道、记忆、资源、规则和外部扰动。
- `max-concept-graph`：核心概念、邻接概念、概念张力、禁止偷换和需要补读的概念卡。
- `max-scale-map`：个人、关系、组织、制度、历史、文明等尺度如何连接，哪些尺度不能跨越。
- `max-path-tree`：机制候选、分支路径、演化终点、回退路径、反例路径、处理问题路径和撤回条件。
- `max-path-confidence-layers`：事实路径、机制候选路径、低置信想象实验、纯反事实路径和价值性解释路径的分层。
- `max-red-team-pass`：解释错误点、框架偏好遮蔽、过度解释、解释力幻觉、反例和行动风险的自我攻击。
- `max-unexhaustible-declaration`：内心动机、未来自由行动、沉默主体经验、未公开材料、历史偶然性和超越性窗口等原则不可穷尽处。
- `max-output-layers`：结构底稿、完整长文和续写索引的输出分层。
- `max-dossier`：完整结构底稿。
- `max-essay`：不设默认字数上限的完整解释性文章。
- `max-continuation-index`：未展开路径、下一轮续写入口、可继续扩展的世界档案目录。

## 输出纪律

- 不走普通文章类型选择器；如果用户要求某种文体，可作为表达偏好，不得改变结构推演链。
- 不设默认字数上限；不得用摘要、提纲、项目符号或“如果只要一句话”替代 `max-essay`。
- 可以穷尽结构推演，不能假装穷尽现实真相；必须写明不可判断区、反例、撤回条件和未展开完的路径队列。
- 可以主动检索资料，不能假装穷尽全部资料；必须写明 `max-source-frontier`、未穷尽资料队列和停止条件。
- 可以保留超越性窗口，不能把不可解释处写成超越性结论；必须写明 `max-transcendence-window`、误读风险和撤回条件。
- 可以穷尽可能，不能把所有可能写成同一种强度；必须写明 `max-path-confidence-layers`。
- 可以连续多轮展开，不能让多轮输出重复、漂移或遗忘边界；必须写明 `max-continuation-ledger` 和 `max-continuation-index`。
- 可以追求解释力，不能跳过自我攻击；必须写明 `max-red-team-pass`。
- 可以从可见材料出发，不能让强势主体吞没沉默者、退出者和未来主体；必须写明 `max-position-matrix`。
- 可以说“穷尽一切”，不能假装原则上不可穷尽之物已经穷尽；必须写明 `max-unexhaustible-declaration`。
- 不能用世界观取消证据边界；不能用宏观尺度抹掉低尺度痛苦、失职和责任链。
- 不能用爱取消边界、责任、伤害、补证、退出或保护；不能把爱写成忍耐义务。
- `v5 DLC` 可以作为内部审计层触发，默认 `score_visibility: hidden`；分数只用于降档、补证、阻断公开或收窄行动上限。
- 若涉及公共事实、真实机构、政策、公司、人物、技术标准或最新情况，必须查源或降档。
- 生成层不得宣布质量闸通过、完全通过、A档、合格、`structural_pass`、`substantive_pass` 或发布通过；这些只归 `crossframe-review`。

## 完成标准

一次合格的 `crossframe-max` 输出必须回答：

- 这个局部世界是什么，边界在哪里？
- 它靠什么锚点、承接者、资源、规则、反馈、记忆和外部通道运行？
- 哪些世界观根假设和运行规律被激活？
- 哪些概念不是词命中，而是结构变量命中？
- 当前问题是什么，为什么反复卡住？
- 不处理会如何演化？处理会打开哪些路径？哪些是假修复？
- 哪些路径会回退、转移、自主解离或进入多中心承接？
- 什么反例会推翻当前解释？
- 最多能提出什么行动、疗愈、转移、治理或表达建议？
- 哪些内容必须保留为不可判断区？
- 哪些资料已经主动检索，哪些反向检索已经做过，哪些仍在未穷尽资料队列？
- 哪些主体或受影响位置在材料中缺席？
- 当前停止检索的条件是什么？
- 哪些不可解释处只能保留为未知，哪些最多能标为开放行动或超越性痕迹候选？
- 哪些迹象可能只是创伤重复、控制、补偿、角色依赖、道德表演或误读为爱？
- 本轮已读材料、已展开路径、未展开路径、已撤回判断和下一轮续写入口是什么？
- 如果这套解释是错的，最可能错在哪里？哪些路径被框架偏好遮蔽？
- 行动者、承接者、受害者、旁观者、制度主体、沉默者、退出者和未来主体分别在哪里？
- 哪些路径属于事实路径、机制候选路径、低置信想象实验、纯反事实路径或价值性解释路径？
- 哪些内心动机、未来自由行动、沉默主体经验、未公开材料、历史偶然性和超越性窗口原则上不可穷尽？
- 输出是否分为结构底稿、完整长文和续写索引？
- 文章是否完整解释了全部主要路径，而不是只给结论？
