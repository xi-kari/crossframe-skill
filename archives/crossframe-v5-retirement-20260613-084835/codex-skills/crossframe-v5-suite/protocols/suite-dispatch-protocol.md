# CrossFrame v5 Suite Dispatch Protocol

本协议把用户请求转成连续 skill 工作流。suite 本身仅通过 `/crossframe-v5-suite` 斜杠命令触发。

## 0. 模式与角色判定（原生弹窗优先）

读取 `../crossframe-v5-suite/references/output-mode-selector.md` 和 `../crossframe-v5-suite/templates/mode-selection-dialog.md`。先根据用户触发词自动判定 `output_mode`（保守/客观/激进/批判）、`role`（学术专家/实践工匠/战略决策者/大众传播/批判反思者/未来探索者）和 `topic_sensitivity`（low/normal/vulnerable/high-stakes）。

若用户已明确写出模式和角色，直接沿用；若用户写“默认”“直接开始”“随便”“都行”“不用选”，使用 `客观 + 学术专家`。若用户没有给出模式或角色，也没有放弃选择，必须先弹出选择器并等待选择，不得直接跑完全程。

原生选择弹窗规则：

- 如果当前环境提供 `request_user_input` 或等价选择 UI，优先用点击选择，不要求用户手打 `2+1`。
- 如果单个弹窗支持 4 个以上选项，直接给出 4 个输出模式和 6 个角色。
- 如果单个问题最多只能放 2-3 个选项，用分组二段式弹窗覆盖完整选项，不得删减角色：
  - 输出模式先问：`客观` / `保守` / `更强判断`；若选择 `更强判断`，再问 `激进` / `批判`。
  - 角色先问：`学术/反思` / `实践/决策` / `传播/未来`；再按所选分组问精确角色：`学术专家` / `批判反思者`，或 `实践工匠` / `战略决策者`，或 `大众传播` / `未来探索者`。
- `topic_sensitivity` 不弹给用户选择，由题材自动判定；涉及痛苦、创伤、无法退出、求助暗示或高责任现实处置时，必须在调度提纲写明。

无原生选择 UI 时，展示 `templates/mode-selection-dialog.md` 的文本降级，并在此处停止等待用户回复。用户回复后继续本协议，不重新要求用户描述任务。

选择完成后立即锁定 `selection_state`：

- `output_mode`
- `role`
- `topic_sensitivity`
- `voice`
- `user_closed_article_layer`
- `user_closed_review`

除非用户主动改选，后续 sibling skill 不得再次询问模式、角色或是否继续。`selection_state` 必须传给 `crossframe-v5`，并由 `crossframe-v5` 写入后续 `v5-read-state-capsule`。

## 1. 建立轻量 workflow_state

suite 只读取 `../crossframe-v5-suite/references/workflow-routing-map.md`，判断本次任务的主目标、默认链路、需要的 sibling skill、输出档位和是否显式关闭文章层或 review。

suite 不读取以下 v5 源结构文件：

- `../crossframe-v5/references/read-routing-map.md`
- `../crossframe-v5/references/v5-material-selection-map.md`
- `../crossframe-v5/references/v5-continuity-bundles.md`
- `../crossframe-v5/references/v5-source-spine.md`
- `../crossframe-v5/references/v5-section-digest-index.md`

suite 生成并传递的 `workflow_state` 只包含：

- 主目标：`diagnose`、`essay`、`dialogue`、`casebook`、`public`、`org`、`teach`、`debate`、`notebook`、`review`。
- 默认链路和必要 sibling skill。
- 输出模式、角色、主题敏感度和正文声口。
- 用户是否显式关闭文章层或 review。
- 题材线索：公共权力、AI/过程材料、亲密伤害、无法退出、强判断、领域词、框架治理、推演/未来探索等。

v5 source module 选择、连读包选择、源结构摘要、源锚点校验和 `v5-read-state-capsule` 生成，全部交给 `crossframe-v5` 中枢完成。

## 2. 判断任务主目标

主目标包括：`diagnose`、`essay`、`dialogue`、`casebook`、`public`、`org`、`teach`、`debate`、`notebook`、`review`。

只要用户通过 v5 suite 进入内容任务，默认最终交付物为 `essay`，输出档位为 `full-visible-v5-longform`。只有显式关闭文章层时才停在专项交付物。

输出声口由角色决定：

- 学术专家、批判反思者：`neutral-analysis`。
- 实践工匠、战略决策者：`neutral-decisive`。
- 大众传播：`editorial-reply` 或 `editorial-commentary`。
- 未来探索者：`editorial-commentary`，并触发推演、生命周期和表达翻译路由。

这些声口只改变前台表达，不改变 v5 连读包、七闸、概念保真、机制候选、判断档位和完整性检查。

## 3. 基础 skill

多数复杂任务先读取 `../crossframe-v5/SKILL.md`。`crossframe-v5` 接收 `selection_state` 与 `workflow_state` 后，必须先选择 v5 source modules，再由 source modules 推出 v5 连读包并生成 `v5-read-state-capsule`，再带出最小内部产物：

- 对象
- 事实边界
- 尺度窗口
- 至少两个机制候选
- 判断档位
- 本次 v5 source modules
- 本次 v5 连读包
- 七闸状态
- 需要追加的专项 skill

该最小内部产物不得作为 suite 默认终点。除非用户显式要求“只要诊断/不要文章/不要 review”，它必须连同 `v5-read-state-capsule` 继续传给 scene sibling、essay 和 review。不得输出“短推理提纲”后停止等待用户说“继续”。

## 4. 排序规则

```text
selection_state -> workflow_state -> crossframe-v5(source modules + 连读包 + v5-read-state-capsule) -> scene sibling -> integrity-check -> essay/dialogue -> review -> final assembly
```

任何成文任务必须在 `essay` 前完成 v5 完整性检查。若只读孤立概念卡，先补读或降档。

## 5. 自动全链路规则

默认链路必须在同一轮完成：

```text
selection_state -> workflow_state -> crossframe-v5 选择 source modules、生成 v5-read-state-capsule 与内部诊断 -> needed sibling -> integrity-check -> crossframe-v5-essay -> crossframe-v5-review -> final assembly
```

- 不得在 `crossframe-v5` 的最小诊断后停下。
- 不得在 `crossframe-v5-essay` 的文章正文后停下，除非用户显式关闭 review。
- 若上下文压力过高，压缩底稿和 review 的可见篇幅，但保留正文、源锚点校验和 review 结论；不得把链路拆成“继续”。
- 若用户显式关闭文章层，仍要执行 `review-lite` 或最小完整性检查，除非用户也明确关闭 review。

## 6. 最终装配规则

默认长文链路的最终可见输出不是 review 报告本身，而是 review 通过后的装配稿：

```text
# 结构洞察底稿
# 文章正文
# CrossFrame v5 Review
```

- `crossframe-v5-review` 接收上游底稿和正文后，只返回 `review_result` 与必要修复建议；不得覆盖或丢弃上游交付物。
- 若 review 判定 A/B/B+ 且只有小修，优先把小修吸收进正文，再追加精简 review；也可保留原文并把小修列入 review 附录，但不得最终只输出 review。
- 若 review 判定 C/D/F 或触发硬失败，最终输出可以标记“不可交付”，但仍要说明上游正文是否可展示、应如何修复；不得让用户误以为 review 就是文章正文。
- 上下文压力过高时，压缩底稿和 review，正文仍保持完整文章形态；用户明确只要评审时，才允许 review-only 输出。

## 7. 源锚点校验

输出中心命题、机制候选、关键概念和行动边界前，必须检查它们是否能回指 `crossframe-v5` 生成的 `v5-read-state-capsule` 中的源锚点。

- 能回指：可写为 CrossFrame v5 判断。
- 只能由作者推导：标为“本文推断”，并写撤回条件。
- 来自外部经典或理论：标为“思想映射”，不能替代 v5 源结构。
- 无源、无证据、无题设支持：删除或降档。

review 阶段必须检查“源锚点校验”是否完成；未完成时，判为连续性保真失败或条件不合格。
