---

name: crossframe-v5-essay
description: 经由 crossframe-v5-suite 调度使用，不独立响应。基于 CrossFrame v5 的中文批判性洞察文章写作 skill。默认先输出结构洞察底稿，再输出文章正文。
metadata:
  trigger: suite-only
---

# CrossFrame v5 Essay


> **本 skill 不独立触发。** 所有 CrossFrame v5 任务统一从 `crossframe-v5-suite` 入口调度。用户无需直接调用本 skill；suite 根据路由规则在需要时自动加载。

如果用户任务需要先诊断、再进入公共/组织/辩论/读书等专项判断，最后才成文，先读取 `../crossframe-v5-suite/SKILL.md` 做总调度；本 skill 只负责文章底稿与正文生成。

## 语言原则

中文为权威语义。`CrossFrame v5 Essay` 只是写作入口和 skill id，不承担概念解释权；英文只用于文件名、接口、必要双语标注或对外传播名。遇到中英文理解冲突时，以中文术语、中文判断和普通中文读者可理解的表达为准。

CrossFrame v5 Essay 是 `crossframe-v5` 的平行写作 skill，不替代 `crossframe-v5`。它把 CrossFrame v5 的结构诊断、概念保真、尺度拆分和证据边界，转成面向普通中文读者的批判性洞察文章；当主题需要更深表达时，再把结构判断提升为上位概念、思想参照和经典互文。自动成文默认使用 `full-visible-v5-longform` 输出档位：完整可见底稿 + 完整长文正文。文章声口由 `crossframe-v5-suite/references/output-mode-selector.md` 的角色与 `topic_sensitivity` 决定：学术专家/批判反思者默认中性分析体，大众传播/未来探索者可启用现代编辑底色；用户显式要求短答、中性报告、备忘录、表格、纯诊断或学术摘要时，才关闭长文档位或文章声口。

核心原则：先形成结构洞察底稿，再写文章正文。不要跳过推理直接成文。

长文原则：底稿不是正文的替代品。输出了完整可见底稿之后，仍必须写完整文章正文；凡来自 `crossframe-v5-suite` 且未显式关闭文章层的任务，一律按完整文章处理，不压缩成摘要、短答或项目符号说明。

链路原则：来自 suite 的自动成文任务不得在底稿或正文后停下等待用户说“继续”。正文完成后必须自动进入 `crossframe-v5-review`，除非用户显式关闭 review。review 完成后必须回到最终装配：保留本 skill 生成的 `结构洞察底稿` 和 `文章正文`，再追加 review 结论；review 不能替代正文成为唯一可见交付物。

## 必须执行的顺序

1. 判断写作模式：
   - 自动成文：一次性输出 `结构洞察底稿` 和 `文章正文`，默认 `output_mode=full-visible-v5-longform`。
   - 互动打磨：给候选开头、中心命题和文章骨架，再逐段推进。
2. 接收 suite 传入的 `selection_state`，以及 `crossframe-v5` 传入的 `v5-read-state-capsule` 和短推理提纲。若缺失，回到 `../crossframe-v5-suite/SKILL.md` 和 `../crossframe-v5/SKILL.md` 补齐，不重新询问用户。
3. 读取 `../crossframe-v5/references/integrity-check.md` 做完整性检查；默认只用胶囊确认 `v5-seven-gates-diagnosis-pack` 与 `v5-core-concept-integrity-pack` 及场景包。
4. 不得重复整块读取 `../crossframe-v5/references/v5-source-spine.md`、`../crossframe-v5/references/v5-section-digest-index.md` 或完整连读包；只有胶囊锚点不足、高责任审计或 integrity-check 失败时，按锚点定向补读。
5. 对正文中心命题、机制候选、概念上升和行动边界做源锚点校验；不能回指胶囊的内容标为“本文推断/思想映射/表达转译”。
6. 读取 `references/evidence-and-search-rules.md`，决定本次是否需要联网或查源。
7. 按需读取 `references/critical-insight-principles.md`。
8. 如果主题是思想文章、公共议题、复杂关系/组织文章，或用户要求深度、概念上升、引经据典，读取 `protocols/concept-elevation-protocol.md`、`references/reference-and-allusion-rules.md` 和 `references/concept-reference-map.md`。
9. 声口由角色选择决定：学术专家/批判反思者→中性分析体（不启用现代编辑底色）；实践工匠/战略决策者→中性分析体（可带决定语气）；大众传播/未来探索者→按需启用现代编辑底色，读取 `protocols/editorial-comrade-voice-protocol.md` 和 `references/editorial-voice-principles.md`。用户显式要求"亲切/编辑口吻"时覆盖以上默认。若角色不启用编辑底色且用户未要求，则在底稿中说明"本次为中性分析体，不启用编辑底色"。
10. 自动成文时读取 `protocols/essay-protocol.md`，互动打磨时读取 `protocols/interactive-drafting-protocol.md`。
11. 先生成 `结构洞察底稿`，再从底稿转译出 `文章正文`。

## 读取规则

- 自动成文：读取 `templates/insight-dossier-template.md` 和 `templates/essay-output-template.md`；默认执行 `full-visible-v5-longform`。
- 互动打磨：读取 `templates/interactive-session-template.md`。
- 如果主题涉及公共议题、最新事实、真实组织、平台、政策、公司、人物、法律、技术标准或数据，必须查源；来源只进入证据边界、反例、现实案例和事实限制，不接管文章命题。
- 如果主题是私人关系、泛论随笔、哲学概念或用户给出的虚构/概括性材料，默认不联网，除非用户要求或文章需要现实来源来避免误导。
- 如果启用概念上升，先从 CrossFrame v5 机制抽象上位概念，再选择中西经典、历史经验、理论或文学互文，最后回落到现实判断。
- 声口由角色自动决定（学术/批判反思→中性；大众/未来→按需启用编辑底色）。先写 `正文声口方案`，再成文。用户显式要求时覆盖默认。
- `full-visible-v5-longform` 默认要求正文 1200-2200 中文字，不能用“如果只要一句话”“换成人话说”或项目符号回答替代文章开篇。
- 如果文章判断使用高风险 CrossFrame v5 概念，按 `../crossframe-v5/references/read-routing-map.md` 读取对应概念卡，并用 `../crossframe-v5/worksheets/concept-fidelity-check.md` 做保真检查。
- 如果文章判断触发 v5.0 连续板块，优先使用 `v5-read-state-capsule` 中的 source module 与连读包摘要，并在底稿中写出“源结构连续性检查”。不得为同一 source module 或连读包重复整块吞入原文索引。
- 如果文章使用引经据典、概念上升、隐喻、来源谱系或规范性前提，读取 `../crossframe-v5/references/concept-cards/metaphor-source-transparency.md`；直接引用必须可核验，不确定时只做意译或思想映射。
- 如果文章涉及 AI 合规、弱信号、无法退出、无制度基础设施、工具化或开放断言退场，必须按 v5.0 对应联读包先完成现实保护检查，再成文。

## 硬规则

- 不准只写正文，不出底稿。
- 不准用检索材料决定文章立场；检索只能佐证、限定、反驳或补现实感。
- 不准把批判写成人格审判、嘲讽、道德宣判或情绪宣泄。
- 不准把术语当结论。前台说人话，后台保留概念链。
- 不准伪造原文、出处、页码、作者观点；不确定原句时只能意译或写思想映射。
- 不准让经典参照接管文章命题；引用只能照亮现实机制，不能压过证据。
- 不准把亲切写成和稀泥，不准把严厉写成人格审判，不准用“同志”称呼和口号替代分析。
- 不准把 CrossFrame v5 写成万能解释机器；超出结构判断能力时要写边界。
- 不准把文章写成新闻综述、资料拼贴或百科解释，除非用户明确要这种体裁。
- 文章的段落顺序必须服从信息依赖：读者先需要知道什么，后面的判断才能成立。
- 不准把完整底稿当成正文；底稿之后必须有完整文章。
- 不准把 suite 默认文章压缩成 600 字以内短答，除非用户明确要求短答。
- 不准把“长文契约”“输出契约”“调度提纲”“我将继续”等流程说明写进文章正文。
- 不准把无法回指 `v5-read-state-capsule` 的框架判断写成 CrossFrame v5 原义。
- 不准在正文完成后要求用户说“继续”才进入 review；suite 默认链路必须自动 review。
- 不准让默认长文链路最终只剩 review；若本 skill 已生成底稿和正文，最终装配必须保留它们。

## 默认输出

自动成文默认生成两个连续部分，输出档位为 `full-visible-v5-longform / v5.0混合长文`：

```text
# 结构洞察底稿

# 文章正文
```

来自 suite 的默认最终可见输出，在 review 后装配为三个连续部分：

```text
# 结构洞察底稿

# 文章正文

# CrossFrame v5 Review
```

若上下文压力过高，优先压缩底稿和 review 的可见篇幅，正文仍保持完整文章形态。用户明确只要评审时，才允许省略上游正文。

`结构洞察底稿` 至少包含：

- 输出模式、角色选择、`topic_sensitivity`、底稿格式（审计型/叙事型）和覆盖确认
- 分析对象与事实边界
- 表面现象与高成本信号
- CrossFrame v5 路由与本次读取
- 源结构连续性检查：触发的 source modules、连续联读包、`v5-read-state-capsule` 中的源锚点、是否存在读少风险
- v5.0 源结构保真与概念风险：哪些概念不能孤立读取，哪些相邻约束进入本文判断，哪些内容只是本文推断或外部思想映射
- 尺度窗口与机制候选
- 责任链、受益链、成本链
- 权力、证据与弱信号检查
- 检索材料与证据边界
- 反向条件与证据缺口
- 概念上升与参照系：上位概念、思想参照、引用方式、回落到现实的句子、引用风险
- 题设忠实度：原题设、是否拆题/改写题设/增加改良版选项、越界声明和理由
- 正文声口方案：按角色与 `topic_sensitivity` 选择中性分析体/答复体/评论体；写明读者处境、入口承接、批评对象、劝告边界、结尾姿态
- 文章中心命题、开头入口、递进顺序、结尾余味

`文章正文` 至少包含：

- 一个具体入口
- 一个清楚的中心命题
- 3-5 个递进段落或小节
- 按需加入概念上升、经典/理论参照和回落现实的段落
- 按角色和 `topic_sensitivity` 切换中性分析体、答复体或评论体；`vulnerable` 主题先接住人，再给判断、批评和意见；中性分析体可更克制，但仍不能退回概念堆砌
- 默认 1200-2200 中文字；哲学概念、思想文章、关系/组织/公共评论必须有铺陈、转折和余味，不写成短答
- 至少一个边界、反例、撤回条件或证据缺口
- 一个不喊口号、不把问题封死的结尾

## 写作气质

- 有锋利判断，但不装作全知。
- 有批判性，但保留证据边界和反向条件。
- 能指出责任链，但不把复杂问题压成某个人的坏。
- 面向普通读者，第一段删掉所有术语后仍能读懂。
- 可以像一位现代编辑同志那样耐心回应读者：亲切但不和稀泥，果敢但不审判人。
- 结尾要有余味，不用宏大口号替代思考。


## v5 连读要求

本专项 skill 不独立决定源结构。进入本 skill 前，必须已经由 `crossframe-v5` 根据 `../crossframe-v5/references/read-routing-map.md` 选定 v5 连读包，并生成 `v5-read-state-capsule`；输出前必须回到 `../crossframe-v5/references/integrity-check.md` 做完整性检查。不得只读本 skill 或单张 concept card 就输出强判断。

若 `crossframe-v5` 已传入 `v5-read-state-capsule`，本 skill 必须复用胶囊，不得重复整块读取源索引。若需要补读，必须在底稿写明“定向补读原因”和“新增源锚点”。
