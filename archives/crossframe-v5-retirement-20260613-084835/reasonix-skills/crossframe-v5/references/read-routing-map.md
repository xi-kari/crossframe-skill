# v5 读取路由图

本文件决定一次 CrossFrame v5 调用应该读取哪些材料。路由顺序固定为：

```text
请求场景 -> v5 source modules -> v5 连读包 -> protocol / worksheet / concept card / template -> integrity-check -> sibling skill
```

不得从请求直接跳到连读包或孤立 concept card。连读包必须由 `v5-material-selection-map.md` 中命中的 source modules 推出。

| 用户请求/场景 | 必读 source modules | 由模块推出的连读包 | 按需追加 source modules | 降档规则 |
| --- | --- | --- | --- | --- |
| 任何 v5 诊断 | `sm-use-boundary-entry`, `sm-seven-gates-mainline` | `v5-use-boundary-low-power-pack`, `v5-seven-gates-diagnosis-pack` | `sm-core-concept-layers` | 七闸未过：不得进入实质判断或行动建议。 |
| 弱者如何寻安宁、脆弱、承接/回流、哲学随笔 | `sm-use-boundary-entry`, `sm-seven-gates-mainline`, `sm-core-concept-layers` | `v5-use-boundary-low-power-pack`, `v5-seven-gates-diagnosis-pack`, `v5-core-concept-integrity-pack` | 只有出现亲密伤害/无法退出才追加 `sm-love-trapped-trauma` | 不自动追加 AI、公共制度或框架治理模块。 |
| 亲密伤害、照护、爱、无法退出 | `sm-use-boundary-entry`, `sm-love-trapped-trauma`, `sm-healing-transfer-t0-t4` | `v5-love-trapped-trauma-pack`, `v5-action-healing-transfer-pack` | `sm-observation-reflexivity` | 安全/最小自主未处理：先承接处境并降档。 |
| AI 报告、合规材料、表格流程、平台指标 | `sm-use-boundary-entry`, `sm-seven-gates-mainline`, `sm-evidence-ai-process` | `v5-evidence-ai-process-pack`, `v5-seven-gates-diagnosis-pack` | `sm-public-institution`, `sm-framework-governance` | 缺失现实证据：只能问题清单、风险提示或保护性开放断言。 |
| 公开强判断、处分、名誉、资源、资格 | `sm-use-boundary-entry`, `sm-seven-gates-mainline`, `sm-judgment-responsibility`, `sm-evidence-ai-process` | `v5-judgment-responsibility-pack`, `v5-seven-gates-diagnosis-pack`, `v5-evidence-ai-process-pack` | `sm-public-institution` | 八件套缺任一项：暂停强判断。 |
| 高权力密度、公共制度、平台治理 | `sm-use-boundary-entry`, `sm-seven-gates-mainline`, `sm-public-institution`, `sm-evidence-ai-process` | `v5-public-power-institution-pack`, `v5-evidence-ai-process-pack`, `v5-seven-gates-diagnosis-pack` | `sm-action-hard-rules` | 申诉/反报复不可成立：降为风险假设或外部复核请求。 |
| 长期演化、阶段、文明尺度 | `sm-use-boundary-entry`, `sm-seven-gates-mainline`, `sm-root-assumptions`, `sm-lifecycle-governance-dynamics` | `v5-root-evolution-deep-pack`, `v5-seven-gates-diagnosis-pack` | `sm-framework-governance` | 不能写全称规律或命运判断。 |
| 推演、未来探索者、后续走向、路径展开、分支终点 | `sm-use-boundary-entry`, `sm-seven-gates-mainline`, `sm-root-assumptions`, `sm-lifecycle-governance-dynamics` | `v5-use-boundary-low-power-pack`, `v5-seven-gates-diagnosis-pack`, `v5-root-evolution-deep-pack` | `sm-observation-reflexivity`, `sm-evidence-ai-process`, `sm-public-institution`, `sm-judgment-responsibility`, `sm-action-hard-rules` | 必要模块未完成：不得给主路径排序、5-10 年趋势或行动建议，只能输出变量清单、近窗口观察和撤回条件。 |
| 阶级、资本、国家、意识形态、社会主义/共产主义、物理隐喻 | `sm-domain-translation`, `sm-core-concept-layers` | `v5-domain-translation-pack`, `v5-core-concept-integrity-pack` | `sm-public-institution` | 未翻译成结构变量：不得进入正式判断。 |
| 修改框架、设计 skill、工具化/商业化/课程化 | `sm-use-boundary-entry`, `sm-framework-governance` | `v5-framework-governance-pack`, `v5-use-boundary-low-power-pack` | `sm-evidence-ai-process` | 不得用框架自证安全；必须保留外部评审。 |
| 文章/评论/长文输出 | `sm-use-boundary-entry`, `sm-seven-gates-mainline`, `sm-core-concept-layers` | `v5-seven-gates-diagnosis-pack`, `v5-core-concept-integrity-pack` | 按主题追加场景模块，再进入 `crossframe-v5-essay` | 文章不能吞掉 source modules、连读包、概念风险和反向条件。 |

## Concept Card 读取规则

- 只有确定必读 source modules 和连读包之后，才读取具体 concept card。
- 每张 concept card 只承担局部解释；最终判断必须由连读包和 `integrity-check.md` 收束。
- 若时间不足，宁可降档为开放断言、轻量观察或问题清单，也不得用单卡维持强判断。

## Source Module 读取规则

- 优先读取 `v5-material-selection-map.md` 中命中的 source module 条目。
- source module 是选材依据；连读包是连续读取约束；concept card 只是局部解释。
- 若 source module 与连读包冲突，以更高保护要求的一侧为准，并在 capsule 的 `integrity_risks` 里说明。
