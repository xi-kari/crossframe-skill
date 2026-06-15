# CrossFrame v5 Workflow Routing Map

本文件规定 CrossFrame v5 skill family 的连续触发规则。suite 默认保持完整长文链路，但 suite 只做轻量调度；所有 v5 连读包选择与源结构摘要由 `crossframe-v5` 中枢完成。

## 核心链路

| 用户目标 | 默认工作流 | 传给 crossframe-v5 的题材线索 |
| --- | --- | --- |
| 结构诊断 | `crossframe-v5 -> crossframe-v5-essay(full-visible-v5-longform) -> crossframe-v5-review -> final assembly` | 基础诊断 |
| 公共评论文章 | `crossframe-v5 -> crossframe-v5-public -> crossframe-v5-essay -> crossframe-v5-review -> final assembly` | 公共权力、制度、平台、AI/过程材料 |
| 组织复盘/修复文章 | `crossframe-v5 -> crossframe-v5-org -> crossframe-v5-essay -> crossframe-v5-review -> final assembly` | 组织、高权力密度、行动闭环、证据包 |
| 答读者问/编辑回信 | `crossframe-v5 -> crossframe-v5-dialogue -> crossframe-v5-essay -> crossframe-v5-review -> final assembly` | 亲密、照护、无法退出、观测影响 |
| 案例沉淀 | `crossframe-v5 -> crossframe-v5-casebook -> crossframe-v5-essay -> crossframe-v5-review -> final assembly` | 案例库、证据追踪、版本写回 |
| 概念教学 | `crossframe-v5 -> crossframe-v5-teach -> crossframe-v5-essay -> crossframe-v5-review -> final assembly` | 概念解释、高风险术语 |
| 命题辩论 | `crossframe-v5 -> crossframe-v5-debate -> crossframe-v5-essay -> crossframe-v5-review -> final assembly` | 强判断、反例、撤回条件 |
| 读书/理论研究 | `crossframe-v5 -> crossframe-v5-notebook -> crossframe-v5-essay -> crossframe-v5-review -> final assembly` | 领域词、来源透明、思想映射 |
| 评审已有输出 | `crossframe-v5-review -> crossframe-v5-essay -> crossframe-v5-review-lite` | 漏读检查、源锚点检查、链路检查 |

## 默认成文规则

suite 被触发且用户未明确关闭文章层时，默认进入 `full-visible-v5-longform`：完整可见底稿、完整长文正文和 review。

选择完成后必须自动完成完整链路。不得停在短推理提纲、专项产物、底稿或正文后等待用户输入“继续”。若上下文压力较高，压缩底稿和 review 的可见篇幅，但不能拆断链路。

最终可见输出必须执行 final assembly：保留 `结构洞察底稿` 与 `文章正文`，再追加 `CrossFrame v5 Review`。review 不得覆盖上游文章交付物。

## 轻量调度规则

suite 入口只产生 `selection_state` 与 `workflow_state`，不读取 v5 源索引、不展开连读包表、不生成 `v5-read-state-capsule`。

`crossframe-v5` 必须根据 `workflow_state` 选择 v5 连读包，并生成统一的 `v5-read-state-capsule`。胶囊必须包含本次连读包、源锚点、相邻约束、不可单读风险、降档规则和源锚点校验对象。中心命题、机制候选和行动边界无法回指胶囊锚点时，必须标为本文推断、外部思想映射，或降档。

## 不读取规则

- 不因出现一个概念就读取全部 sibling skill。
- 不因出现领域词就把领域理论升格为框架本体。
- 不因输出长文就跳过 v5 连读包。
- 不因 suite 入口调度就读取 v5 源索引或生成读态胶囊。
- 不因进入 essay 或 review 就重复整块读取 v5 源索引。
