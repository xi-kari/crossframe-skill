# CrossFrame v5 Suite Smoke Tests

## 1. 默认长文保持

Prompt：写一篇“解释劳动为什么会耗竭”的文章。

失败表现：最终只输出 `CrossFrame v5 Review`，丢失结构洞察底稿或文章正文。

期望：工作流一次性包含 `crossframe-v5 -> crossframe-v5-essay -> crossframe-v5-review -> final assembly`；输出档位是 `full-visible-v5-longform`；suite 只列 `selection_state`、`workflow_state` 和必要 sibling 顺序，`crossframe-v5` 再列 v5 source modules、v5 连读包和 `v5-read-state-capsule` 摘要；最终可见输出保留 `结构洞察底稿`、`文章正文` 和 `CrossFrame v5 Review`；不得停在短推理提纲、底稿或正文后要求用户说“继续”。

## 2. 显式短答关闭文章

Prompt：只要三句话短答，不要文章。

期望：不追加 `crossframe-v5-essay`；仍列 v5 连读包和 review-lite。

## 3. 过度触发失败

Prompt：写一篇普通关系文章。

失败表现：读取全部 sibling skills。

期望：只读取必要链路，并在“不读取”说明未触发的 sibling skills。

## 4. 连读先行失败

Prompt：用 CrossFrame v5 判断这个 AI 合规报告是否证明平台申诉有效。

失败表现：直接读 AI 概念卡或 public skill。

期望：先触发 `v5-evidence-ai-process-pack` 与 `v5-public-power-institution-pack`，再调度 sibling skills。

## 5. 角色弹窗完整性

Prompt：`/crossframe-v5-suite` 分析一下这个现象。

失败表现：没有模式/角色触发词时直接开始；或只提供 3 个角色；或要求用户手打组合而不优先使用原生选择弹窗。

期望：优先弹出原生选择 UI；完整覆盖 4 个输出模式和 6 个角色。若 UI 单题只能放 2-3 个选项，必须用二段式分组弹窗覆盖全部模式和角色，不得删减 `战略决策者`、`批判反思者` 或 `未来探索者`。

## 6. 未来探索者推演链路

Prompt：`/crossframe-v5-suite` 用未来探索者角色推演这个组织如果继续把反馈留在表格和 AI 合规报告里，三年后可能怎么走。

失败表现：只输出趋势判断或三条好/坏分支；没有触发 `v5-root-evolution-deep-pack`；没有状态坐标、反馈写回、承接者生成、反向信号和撤回条件。

期望：读取 `v5-use-boundary-low-power-pack`、`v5-seven-gates-diagnosis-pack`、`v5-root-evolution-deep-pack`，并因 AI 合规报告追加 `v5-evidence-ai-process-pack`；使用 `inference-protocol.md` 与 `inference-output.md` 输出至少两条条件路径，每条包含触发条件、阶段移动、关键承接者、保护变量、反向信号和停止/撤回条件。

## 7. 一次选择后自动全链路

Prompt：`/crossframe-v5-suite` 选择“客观 + 学术专家”后，写一篇“倘若生来软弱，弱者向何处寻安宁”的文章。

失败表现：选择后只输出 `CrossFrame v5 诊断：短推理提纲`；或完成 essay 后停下；或要求用户输入“继续”才进入 `crossframe-v5-essay` 或 `crossframe-v5-review`；或最终只输出 `CrossFrame v5 Review`，把底稿和正文省略。

期望：选择只发生一次；同一轮继续输出结构洞察底稿、文章正文和 review；review 作为第三部分附在文章后，不覆盖上游内容；正文不得出现“长文契约”“调度提纲”等流程文字。

## 8. 连读包摘要传递

Prompt：`/crossframe-v5-suite` 写一篇低风险哲学随笔，题目是“弱者如何寻安宁”。

失败表现：suite、core、essay、review 各自整块读取 `v5-source-spine.md`、`v5-section-digest-index.md` 或完整连读包；prompt token 接近重复吞源；底稿没有统一源摘要。

期望：suite 不读取 v5 源索引、不展开完整选材图或连读包、不生成 `v5-read-state-capsule`；`crossframe-v5` 生成统一胶囊，且胶囊先列 `v5_source_modules` 再列 `v5_continuity_bundles`。下游只消费胶囊和自身协议。若需要补读，只按具体 source module 或源锚点定向补读，并说明原因。

## 9. 源锚点防编造

Prompt：`/crossframe-v5-suite` 写一篇带概念上升的文章，比较庄子、斯多葛和能力进路如何照亮“软弱与安宁”。

失败表现：把外部思想参照写成 CrossFrame v5 原文内容；或中心命题、机制候选、行动边界没有源锚点却写成 v5 框架判断。

期望：底稿包含源锚点校验；CrossFrame v5 判断回指胶囊源锚点；庄子、斯多葛、能力进路只作为思想映射或外部参照，不替代 v5 源结构。
