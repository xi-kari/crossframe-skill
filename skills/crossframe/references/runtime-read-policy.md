# Runtime Read Policy

本文件控制 CrossFrame 正常运行时的读取成本。默认目标是：保留 v5 连续性和审计能力，但不把完整源索引、eval、examples 或成功/失败长案例塞进每次上下文。

本文档中的相对路径默认以当前 skill 目录为语义基准；协议子文件中出现的 sibling skill 路径也按 `skills/<skill-id>/...` 解释，不按子文件物理目录逐级解析。

## 默认读取层级

正常 `/crossframe-suite`、`/crossframe`、`/crossframe-essay` 运行只读：

1. 当前入口 `SKILL.md`。
2. 本文件。
3. `references/read-routing-map.md`。
4. `references/continuity-closure-map.md`。
5. 被路由命中的 protocol / worksheet / template。
6. 被命中的 v5 连读包文件。
7. 若触发 v5 DLC，读取 `construct-map-v5-dlc.md`、`seven-gates-quant-rubric.md` 和 `judgment-action-matrix-v5-dlc.md` 的最小组合。
8. 若成文，`crossframe-essay` 的文章类型选择器、技法路由表和最多 5 张技法卡。

## 默认不读

以下文件默认不在正常产出路径读取：

- `evals/`
- `examples/`
- 完整成功案例和完整失败案例
- `v5-source-spine.md`
- `v5-section-digest-index.md`
- `v5-coverage-map.md`
- 退役版本材料
- v5 DLC 半量化文件，除非用户明确要求量化、评分、比较、校准、一致性、审计、DLC，或高责任/公开发布前需要内部边界审计
- 全量 `writing-techniques/` 50 张卡

这些材料只在验证、调试、回退审计、源锚点失败、用户显式要求过程审计或需要原文/章节定位时读取。

## 大 source module 读取规则

`v5-source-spine.md` 和 `v5-section-digest-index.md` 是重资料，不全量打开。需要源锚点时：

1. 先在 `v5-material-selection-map.md`、`v5-term-fidelity.md` 或当前连读包中确定关键词、包名或 V5-H 范围。
2. 用搜索定位相关 V5-H 或标题。
3. 只读取命中的局部段落、相邻标题或必要范围。
4. 在 `v5-read-state-capsule` 写明 source module、V5-H/源范围和降档边界。

无法定位稳定锚点时，不补全大索引，不硬装权威；写“锚点缺失，降档”。

## v5 DLC 读取边界

默认不读取 v5 DLC 半量化文件。触发后也不绕过 v5 主流程；必须先有对象边界、七闸状态、机制候选、source_anchor、claim ledger 和判断档位，DLC 才能解释闸状态或行动上限。

- 显式触发：用户要求量化、评分、半量化、打分、比较、排序、校准、一致性、rubric、audit、DLC、七闸分值或案例库试跑。
- 内部触发：高责任、组织处置、公共发布、真实机构/平台/人物、AI 合规或工具发布前边界审计，只用于降档、补证、阻断公开或收窄行动上限。
- 不触发：普通关系、组织复盘、公共议题、概念解释和短诊断不自动读取 DLC，不自动显示分数。
- 可见性：必须登记 `score_visibility: hidden / profile_only / user_requested_profile`。默认 `hidden`；用户明确要求量化审计时最多展示结构剖面。
- 禁止：不得输出对象总分、关系分、组织健康分、文明阶段分、预测概率、排名、发布合格分或用分值判定 `substantive_pass`。
- 高责任：分值只能触发降档、补证、反例入口、行动上限收窄或 `block_publication`；不能授权处分、封禁、开除、资格、公开定性或发布通过。

## eval / examples 使用规则

- `evals/` 只用于开发、压测、回归验证和 review-agent 审计，不进入用户正常答案。
- `examples/` 只用于风格对齐或调试，不作为默认上下文。
- 失败案例保留为短压力样例，不写成长篇历史叙述。
- 成功案例只保留最小合格片段；完整样稿放到 `work/` 或归档，不放入默认读取链。

## 输出层减负

后台可以执行完整检查，但前台只展示摘要：

- 胶囊摘要，不展开完整闭包表。
- 命题台账状态，只列关键 claim_id 和是否降档，不展开完整台账。
- 概念契约状态，只列 pass / partial / fail 和降档决定。
- 来源台账状态，不堆所有来源字段；高责任或用户要求时再展开。
- 技法落地摘要，不展示全部技法卡内容。
- 质量闸短摘要，不替代底稿和正文。

若触发高责任、公共发布、真实机构事故、名誉资源处分、AI 合规或用户要求审计过程，可展开相应表格。
