---

name: crossframe-v5
description: 经由 crossframe-v5-suite 调度使用，不独立响应。"跨尺度结构诊断框架 v5.0"的中文结构推理协议型 skill，用于先按 v5 原文连读包恢复连续结构，再诊断关系、团队、组织、制度、公共争议和长期演化中的复杂失衡。
metadata:
  trigger: suite-only
---

# CrossFrame v5

> **本 skill 不独立触发。** 所有 CrossFrame v5 任务统一从 `crossframe-v5-suite` 入口调度。用户无需直接调用本 skill；suite 根据路由规则在需要时自动加载。

## 核心定位

CrossFrame v5 不是把 v5 文档拆成孤立概念卡，而是一个以“原文连读包”为先导的结构推理协议。

每次使用都必须先确定本次触发的 v5 连读包，再读取协议、工作表、概念卡和模板。任何只读单张概念卡就输出强判断、行动建议或公开定性的结果，视为不合格。

## 必须执行的顺序

1. 通过 `../crossframe-v5-suite/SKILL.md` 确认工作流、输出档位和是否默认进入文章层。
2. 接收 suite 传入的 `selection_state` 与 `workflow_state`，不得重新询问模式、角色或是否继续。
3. 读取 `references/read-routing-map.md` 先识别候选 v5 source modules，再在 `references/v5-material-selection-map.md` 中按 `source_module_id` 定向读取对应条目；不得从用户请求直接跳到连读包或孤立 concept card。
4. 由命中的 source modules 推出 `references/v5-continuity-bundles.md` 中的连读包 ID，再按包 ID 定向读取对应条目；不得整块加载全表。
5. 读取 `templates/read-state-capsule.md`，生成 `v5-read-state-capsule`。胶囊必须先列 `v5_source_modules`，再列 `v5_continuity_bundles`，只摘要必要源结构，不复制大段原文，并作为下游默认源结构输入。
6. 优先使用 `v5-read-state-capsule` 中的源锚点、相邻约束和降档规则。不得重复整块读取 `references/v5-source-spine.md`、`references/v5-section-digest-index.md` 或完整连读包。
7. 若胶囊缺少关键锚点、高责任审计需要复核或完整性检查失败，只按具体 source module、连读包或章节锚点定向补读相关摘要，并说明补读原因。
8. 过七闸：有效对象、证据追踪、受影响位置、权力与反报复、中介与反身性、强判断程序、行动上限。
9. 再读取必要 protocol、worksheet、concept card 或 template。
10. 输出前读取 `references/integrity-check.md` 做总闸检查；若只读单卡、漏读前置包或七闸未过，必须补读或降档。
11. 决定判断档位：轻量观察、开放断言、完整诊断、强判断、低条件试探行动、退出转移或退场/转接。

## 默认前置连读包

任何 v5 诊断默认至少触发：

- `v5-use-boundary-low-power-pack`
- `v5-seven-gates-diagnosis-pack`

文章、评论、思想输出还必须触发：

- `v5-core-concept-integrity-pack`

场景包按 `references/read-routing-map.md` 追加。

## 输出规则

- 默认形成短推理提纲：对象、事实边界、尺度窗口、机制候选、判断档位、本次 v5 source modules、本次 v5 连读包、下一步。
- 当任务来自 suite 且未显式关闭文章层时，短推理提纲是内部链路状态，不得作为最终输出停下；必须继续进入必要专项 skill、`crossframe-v5-essay`、`crossframe-v5-review` 和最终装配。
- 只有用户明确要求“只要诊断/不要文章/短答/表格/清单/纯诊断”时，才可把短推理提纲作为可见主产物；即便如此也要执行最小完整性检查或 review-lite。
- 第一段必须不用术语也能读懂。
- 不得把结构诊断变成人格审判、命运预言、意识形态标签或道德授权。
- 不得把 AI、表格、流程、报告、内部自评或漂亮文本当作现实证明。
- 不得用尺度升维取消低尺度痛苦、具体责任和低权力主体保护。
- 不得用爱、使命、大局或修复要求低权力主体继续承压。
- 不得把无法回指 `v5-read-state-capsule` 源锚点的内容写成 CrossFrame v5 原义；只能标为本文推断、表达转译或外部思想映射，并写撤回条件。

## 核心资料

- `references/v5-source-spine.md`：v5 原文标题层级、段落范围、连读包归属。
- `references/v5-section-digest-index.md`：v5 分节保真摘要与相邻提醒。
- `references/v5-continuity-bundles.md`：v5 不可分割连读包。
- `references/v5-material-selection-map.md`：请求到 v5 source modules，再到连读包和专项 skill 的材料选择中间层。
- `references/v5-coverage-map.md`：v5 板块到 skill family 的覆盖地图。
- `references/v5-term-fidelity.md`：v5 高风险术语保真表。
- `references/read-routing-map.md`：请求到连读包、协议、工作表、概念卡和模板的路由图。
- `references/integrity-check.md`：输出前总闸。
- `templates/read-state-capsule.md`：由本 skill 生成并传递的统一源结构摘要。

## 源结构读取预算

- suite 只提供 `selection_state` 与 `workflow_state`；本 skill 是 `v5-read-state-capsule` 的生成者。
- 本 skill 生成胶囊时，只读取路由图、候选 source module 条目、候选连读包条目和必要源摘要；不得把全量 `v5-material-selection-map.md`、`v5-continuity-bundles.md`、`v5-source-spine.md`、`v5-section-digest-index.md` 或完整连读包原文传给下游。
- 普通文章或低风险诊断优先控制在 2-5 个连读包、800-1500 中文字胶囊；只有高责任、公开判断、框架审计或用户要求审计时才扩展。
- 若必须补读源结构，只补读与胶囊缺口对应的锚点或章节摘要。
- 补读后的新增判断必须写回胶囊或短推理提纲，供 essay 和 review 复用。

## 最低合格标准

一次合格的 CrossFrame v5 输出必须能回答：

- 本次先读了哪些 v5 连读包？
- 本次先命中了哪些 v5 source modules？这些模块如何推出连读包？
- 是否过了七闸，若跳闸如何补偿或降档？
- 是否区分事实、解释、证据缺口、机制候选和判断档位？
- 是否保护低权力主体、弱信号、申诉/反证入口和撤回路径？
- 是否把高风险概念放回源结构和相邻章节，而不是只读单卡？
- 如果判断会进入现实行动、公开表达或资源/名誉/资格影响，是否具备八件套？
