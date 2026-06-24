---
name: crossframe-history
description: 经由 crossframe-suite 调度或用户显式命令使用，不隐式响应。历史、文明连续史、王朝制度、史料闭合、archive-access/FOIA backlog 与历史领域接口边界的中文专项 skill。
trigger: explicit-or-suite
---

# CrossFrame History

> **本 skill 不应被普通任务隐式触发。** 推荐从 `crossframe-suite` 入口调度；但允许用户显式调用 `/crossframe-history`、`crossframe-history`，或由 suite 路由到历史领域时读取本 skill。

CrossFrame History 是 `crossframe` 的历史/文明连续史领域接口层。它负责把 v5 主干变量接入历史材料、断代尺度、史料等级、制度连续性/断裂和 archive-access/FOIA backlog；它不发布正式历史适配器，不修改 v5 主干变量，不把本地 C5 收敛写成百科式历史完成。

中文为权威语义。英文只作为 skill id、文件名或对外简介。

## 必须读取

每次触发后按顺序读取：

1. `../crossframe/SKILL.md`
2. `../crossframe/references/runtime-read-policy.md`
3. `../crossframe/references/read-routing-map.md`
4. `../crossframe/references/continuity-closure-map.md`
5. `../crossframe/templates/read-state-capsule.md`
- 若本 skill 产生新的中心命题、机制句、高风险概念判断、公共定性、行动建议、案例复用判断、组织处置建议或可成文材料，必须把这些内容作为 `claim ledger delta` 交回 `../crossframe/templates/claim-ledger.md` 与 `../crossframe/worksheets/claim-ledger-check.md`。本 skill 不得新增未登记判断；若无法登记 `claim_id`、判断档位、行动上限、撤回条件和发布边界，只能删除、降档，或标为“本文推断 / 表达转译 / 外部思想映射”。
6. `protocols/history-domain-protocol.md`
7. `protocols/history-source-ledger-protocol.md`
8. `references/history-c5-boundary.md`

按任务追加：

- 史料闭合、档案路径、finding aid、个案事实补证、FOIA：读 `protocols/archive-foia-backlog-protocol.md` 与 `references/archive-foia-backlog-ledger.md`。
- 需要内部研究摘要：读 `templates/history-interface-summary.md`。
- 需要对外表达：读 `templates/public-c5-boundary-summary.md`；若要成文，再由 suite 转入 `../crossframe-essay/SKILL.md`。
- 需要申请档案或 FOIA 文案：读 `templates/archive-request-packet.md`；本 skill 只生成申请包，不自动提交申请。
- 正式交付、公开摘要、强判断：最后追加 `../crossframe-review/SKILL.md`。

## 核心原则

- 史料优先：优先使用正史、编年、制度文本、诏令、奏议、法律文书、出土简牍、碑刻、考古报告、同时代文集、档案原件、官方记录和可复核数据库。
- 现代解读降档：论文、专著、百科、课程、评论只能用于定位史料、提示争议、提供反方校验；不能直接承担机制结论。
- 主干变量限量：一次历史解释只选 3-6 个 CrossFrame v5 主干变量，不堆概念。
- 断代与尺度先行：先说明时间窗口、地理范围、制度对象、材料距离和可观察结果，再做机制翻译。
- 失败要登记：解释不了的部分必须区分史料不足、尺度错位、时间因果问题、领域概念缺失和框架误读。
- backlog 不等于闭合：source path、finding aid、档案馆目录、FOIA 入口只能提升下一步可核验性，不能写成事实闭合。

## 调用完成硬闸

不得用“已读取”“已闭包”“质量闸通过”“源锚点已回指”这类声明替代可见产物。一次历史调用只有在输出中留下以下证据时，才算完成：

- 具体史料台账：不能只写“官方文件、回忆录、现代研究、公开史料”这类来源族；至少要列出承担关键事实的具体史料、档案系列、文献名、法规/会议记录名、数据库记录或明确待核 source path。
- 输出档位：必须标注 `历史草稿档`、`历史接口分析档` 或 `正式历史分析档`，并说明为什么只能到这个档位。
- 变量清单：明确本次使用的 3-6 个 v5 主干变量；超过 6 个或不列变量清单时，降为草稿档。
- 解释质量：必须分出解释顺畅、解释高成本、解释不了/待证，且解释不了处登记失败类型。
- 升降级条件：写清哪些材料会使中心判断升级、降级或撤回。
- review 边界：`crossframe-review` 不能自我盖章；若没有具体史料台账，只能给 `structural_pass` 或 `draft_pass`，不得给 `substantive_pass`。

## 历史输出档位

| 档位 | 允许内容 | 禁止内容 |
| --- | --- | --- |
| 历史草稿档 | 可基于用户材料、常识性背景或已有知识写文章草稿；必须声明未完成史料闭合 | 不得称为完整历史接口分析，不得写“史料台账通过”或“质量闸通过” |
| 历史接口分析档 | 有具体来源或 source path、证据档位、不能证明什么、3-6 个变量、解释质量和失败登记 | 不得把现代解释直接当机制证据，不得把类别台账写成具体史料台账 |
| 正式历史分析档 | 关键事实有 H0/H1 或可核验 H2 逐条台账，多源互证或说明单源足够，反向条件清楚 | 不得越过未开放档案、未核实个体结果或低权力主体材料缺口 |

若无法列出具体史料，必须主动写：`本次为历史草稿档，未完成 crossframe-history 的史料台账硬闸`。

## 禁止表述

- 不得说“人类全部历史已经研究完”。
- 不得说“历史适配器已经正式发布”。
- 不得说“CrossFrame v5 已吸收 C5 全部成果”。
- 不得说“所有个案已经事实闭合”。
- 不得把 `history-kb-v9.9` 当作本轮证据来源或 v5 已吸收内容。
- 不得把单一朝代经验升格为历史规律。
- 不得把“王朝周期”写成结构必然。
- 不得为了证明 CrossFrame 裁剪历史。

## 默认输出

按用户意图选择一个主输出：

- 历史节点接口分析：时间线、制度/人物/资源/冲突、史料台账、3-6 个主干变量、解释质量、失败登记、反向条件。
- 史料闭合台账：现有材料能证明什么、不能证明什么、缺哪些原件、如何申请、收到材料后如何升级/降级。
- C5 边界摘要：说明本地历史领域接口层的收敛状态、剩余缺口、禁止夸大表达和下一步研究责任。
- 公开边界文本：普通读者可读，但必须保留事实边界和未闭合项。
- 申请包草稿：档案馆/机构/FOIA 请求文案、目标字段、不可声明边界和追踪记录。

## 最低合格输出

一次合格历史输出至少回答：

- 讨论的是哪个历史节点或个案，时间/空间/制度边界是什么？
- 主要事实来自哪些史料，哪些只是后世编纂或现代定位材料？
- 本次历史输出档位是什么，为什么不能更高或必须降档？
- 本次只用了哪 3-6 个 CrossFrame 主干变量？
- 哪些地方解释顺畅，哪些解释成本高，哪些解释不了？
- 解释失败属于史料不足、尺度错位、时间因果问题、领域概念缺失，还是框架误读？
- 哪些结论只能保持为候选，什么材料会使它升级、降级或撤回？
- 是否存在 archive-access/FOIA backlog；如果有，它能提升什么，不能证明什么？

若以上任一项缺失，输出不能写“完整历史分析”“质量闸通过”或“调用完成”，只能写为草稿、待核或结构草案。
