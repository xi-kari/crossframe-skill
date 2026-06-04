---
name: crossframe-essay
description: CrossFrame Essay 是基于 CrossFrame 的中文批判性洞察文章写作 skill。Use when the user asks to write or shape a 中文文章、长文、评论、思想文章、批判性洞察文章、结构洞察文章，或想把关系、团队、组织、制度、公共议题、哲学概念和复杂现实问题写成面向普通读者、先推理后表达、可按需概念上升并引入中西经典/理论参照的文章。也适合用户要求亲切、编辑、同志口吻、报刊答复、耐心解答或给出意见的中文洞察文章。默认先输出结构洞察底稿，再输出文章正文；也支持互动打磨、候选开头、逐段推进和保留用户编辑。
---

# CrossFrame Essay

如果用户任务需要先诊断、再进入公共/组织/辩论/读书等专项判断，最后才成文，先读取 `../crossframe-suite/SKILL.md` 做总调度；本 skill 只负责文章底稿与正文生成。

## 语言原则

中文为权威语义。`CrossFrame Essay` 只是写作入口和 skill id，不承担概念解释权；英文只用于文件名、接口、必要双语标注或对外传播名。遇到中英文理解冲突时，以中文术语、中文判断和普通中文读者可理解的表达为准。

CrossFrame Essay 是 `crossframe` 的平行写作 skill，不替代 `crossframe`。它把 CrossFrame 的结构诊断、概念保真、尺度拆分和证据边界，转成面向普通中文读者的批判性洞察文章；当主题需要更深表达时，再把结构判断提升为上位概念、思想参照和经典互文。自动成文默认使用 `full-visible-v3-longform` 输出档位：完整可见底稿 + 完整长文正文。自动成文也默认使用现代编辑底色：耐心、谦逊、认真、果敢，像一位中文编辑认真回应读者问题；只有用户明确要求短答、中性报告、备忘录、表格、纯诊断或学术摘要时，才关闭长文档位或文章声口。

核心原则：先形成结构洞察底稿，再写文章正文。不要跳过推理直接成文。

长文原则：底稿不是正文的替代品。输出了完整可见底稿之后，仍必须写完整文章正文；凡来自 `crossframe-suite` 且未显式关闭文章层的任务，一律按完整文章处理，不压缩成摘要、短答或项目符号说明。

## 必须执行的顺序

1. 判断写作模式：
   - 自动成文：一次性输出 `结构洞察底稿` 和 `文章正文`，默认 `output_mode=full-visible-v3-longform`。
   - 互动打磨：给候选开头、中心命题和文章骨架，再逐段推进。
2. 读取 `../crossframe/SKILL.md`。
3. 读取 `../crossframe/references/read-routing-map.md`，把主题路由到相应 CrossFrame protocol。
4. 读取 `../crossframe/references/continuity-bundles.md`，至少确认 `diagnosis-mainline-pack` 与 `expression-article-pack`；公共、亲密、长期演化或高责任主题追加对应联读包。
5. 用 `../crossframe/worksheets/source-continuity-check.md` 检查是否只读了孤立概念卡；深度文章按需读取 `../crossframe/references/v3-source-spine.md`、`../crossframe/references/v3-section-digest-index.md` 或 `../crossframe/references/v3-term-fidelity.md`。
6. 读取 `references/evidence-and-search-rules.md`，决定本次是否需要联网或查源。
7. 按需读取 `references/critical-insight-principles.md`。
8. 如果主题是思想文章、公共议题、复杂关系/组织文章，或用户要求深度、概念上升、引经据典，读取 `protocols/concept-elevation-protocol.md`、`references/reference-and-allusion-rules.md` 和 `references/concept-reference-map.md`。
9. 自动成文默认读取 `protocols/editorial-comrade-voice-protocol.md` 和 `references/editorial-voice-principles.md`，并在底稿中写出 `正文声口方案`。如果用户明确要求中性报告、备忘录、表格、纯诊断或学术摘要，才可关闭现代编辑底色，并说明关闭原因。
10. 自动成文时读取 `protocols/essay-protocol.md`，互动打磨时读取 `protocols/interactive-drafting-protocol.md`。
11. 先生成 `结构洞察底稿`，再从底稿转译出 `文章正文`。

## 读取规则

- 自动成文：读取 `templates/insight-dossier-template.md` 和 `templates/essay-output-template.md`；默认执行 `full-visible-v3-longform`。
- 互动打磨：读取 `templates/interactive-session-template.md`。
- 如果主题涉及公共议题、最新事实、真实组织、平台、政策、公司、人物、法律、技术标准或数据，必须查源；来源只进入证据边界、反例、现实案例和事实限制，不接管文章命题。
- 如果主题是私人关系、泛论随笔、哲学概念或用户给出的虚构/概括性材料，默认不联网，除非用户要求或文章需要现实来源来避免误导。
- 如果启用概念上升，先从 CrossFrame 机制抽象上位概念，再选择中西经典、历史经验、理论或文学互文，最后回落到现实判断。
- 自动成文默认启用现代编辑底色，先写 `正文声口方案`，再成文。问题型主题写成答复体；公共评论、思想文章、概念文章写成评论体；只有显式短答/中性报告/备忘录/表格/纯诊断/学术摘要才关闭声口或长文档位。
- `full-visible-v3-longform` 默认要求正文 1200-2200 中文字，不能用“如果只要一句话”“换成人话说”或项目符号回答替代文章开篇。
- 如果文章判断使用高风险 CrossFrame 概念，按 `../crossframe/references/read-routing-map.md` 读取对应概念卡，并用 `../crossframe/worksheets/concept-fidelity-check.md` 做保真检查。
- 如果文章判断触发 v3.0 连续板块，按 `../crossframe/references/continuity-bundles.md` 读取对应联读包，并在底稿中写出“源结构连续性检查”。
- 如果文章使用引经据典、概念上升、隐喻、来源谱系或规范性前提，读取 `../crossframe/references/concept-cards/metaphor-source-transparency.md`；直接引用必须可核验，不确定时只做意译或思想映射。
- 如果文章涉及 AI 合规、弱信号、无法退出、无制度基础设施、工具化或开放断言退场，必须按 v3.0 对应联读包先完成现实保护检查，再成文。

## 硬规则

- 不准只写正文，不出底稿。
- 不准用检索材料决定文章立场；检索只能佐证、限定、反驳或补现实感。
- 不准把批判写成人格审判、嘲讽、道德宣判或情绪宣泄。
- 不准把术语当结论。前台说人话，后台保留概念链。
- 不准伪造原文、出处、页码、作者观点；不确定原句时只能意译或写思想映射。
- 不准让经典参照接管文章命题；引用只能照亮现实机制，不能压过证据。
- 不准把亲切写成和稀泥，不准把严厉写成人格审判，不准用“同志”称呼和口号替代分析。
- 不准把 CrossFrame 写成万能解释机器；超出结构判断能力时要写边界。
- 不准把文章写成新闻综述、资料拼贴或百科解释，除非用户明确要这种体裁。
- 文章的段落顺序必须服从信息依赖：读者先需要知道什么，后面的判断才能成立。
- 不准把完整底稿当成正文；底稿之后必须有完整文章。
- 不准把 suite 默认文章压缩成 600 字以内短答，除非用户明确要求短答。

## 默认输出

自动成文默认输出两个连续部分，输出档位为 `full-visible-v3-longform / 3.0混合长文`：

```text
# 结构洞察底稿

# 文章正文
```

`结构洞察底稿` 至少包含：

- 分析对象与事实边界
- 表面现象与高成本信号
- CrossFrame 路由与本次读取
- 源结构连续性检查：触发的连续联读包、是否读取源脊柱/逐节摘要、是否存在读少风险
- v3.0 源结构保真与概念风险：哪些概念不能孤立读取，哪些相邻约束进入本文判断
- 尺度窗口与机制候选
- 责任链、受益链、成本链
- 权力、证据与弱信号检查
- 检索材料与证据边界
- 反向条件与证据缺口
- 概念上升与参照系：上位概念、思想参照、引用方式、回落到现实的句子、引用风险
- 正文声口方案：默认启用现代编辑底色；选择答复体/评论体/中性说明体；写明读者处境、情绪入口、批评对象、劝告边界、结尾姿态
- 文章中心命题、开头入口、递进顺序、结尾余味

`文章正文` 至少包含：

- 一个具体入口
- 一个清楚的中心命题
- 3-5 个递进段落或小节
- 按需加入概念上升、经典/理论参照和回落现实的段落
- 按题切换答复体或评论体；默认先接住问题，再给判断、批评和意见；显式中性说明体可更克制，但仍不能退回概念堆砌
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
