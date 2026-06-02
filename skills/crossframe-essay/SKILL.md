---
name: crossframe-essay
description: CrossFrame Essay 是基于 CrossFrame 的中文批判性洞察文章写作 skill。Use when the user asks to write or shape a 中文文章、长文、评论、思想文章、批判性洞察文章、结构洞察文章，或想把关系、团队、组织、制度、公共议题、哲学概念和复杂现实问题写成面向普通读者、先推理后表达、可按需概念上升并引入中西经典/理论参照的文章。默认先输出结构洞察底稿，再输出文章正文；也支持互动打磨、候选开头、逐段推进和保留用户编辑。
---

# CrossFrame Essay

CrossFrame Essay 是 `crossframe` 的平行写作 skill，不替代 `crossframe`。它把 CrossFrame 的结构诊断、概念保真、尺度拆分和证据边界，转成面向普通中文读者的批判性洞察文章；当主题需要更深表达时，再把结构判断提升为上位概念、思想参照和经典互文。

核心原则：先形成结构洞察底稿，再写文章正文。不要跳过推理直接成文。

## 必须执行的顺序

1. 判断写作模式：
   - 自动成文：一次性输出 `结构洞察底稿` 和 `文章正文`。
   - 互动打磨：给候选开头、中心命题和文章骨架，再逐段推进。
2. 读取 `../crossframe/SKILL.md`。
3. 读取 `../crossframe/references/read-routing-map.md`，把主题路由到相应 CrossFrame protocol。
4. 读取 `references/evidence-and-search-rules.md`，决定本次是否需要联网或查源。
5. 按需读取 `references/critical-insight-principles.md`。
6. 如果主题是思想文章、公共议题、复杂关系/组织文章，或用户要求深度、概念上升、引经据典，读取 `protocols/concept-elevation-protocol.md`、`references/reference-and-allusion-rules.md` 和 `references/concept-reference-map.md`。
7. 自动成文时读取 `protocols/essay-protocol.md`，互动打磨时读取 `protocols/interactive-drafting-protocol.md`。
8. 先生成 `结构洞察底稿`，再从底稿转译出 `文章正文`。

## 读取规则

- 自动成文：读取 `templates/insight-dossier-template.md` 和 `templates/essay-output-template.md`。
- 互动打磨：读取 `templates/interactive-session-template.md`。
- 如果主题涉及公共议题、最新事实、真实组织、平台、政策、公司、人物、法律、技术标准或数据，必须查源；来源只进入证据边界、反例、现实案例和事实限制，不接管文章命题。
- 如果主题是私人关系、泛论随笔、哲学概念或用户给出的虚构/概括性材料，默认不联网，除非用户要求或文章需要现实来源来避免误导。
- 如果启用概念上升，先从 CrossFrame 机制抽象上位概念，再选择中西经典、历史经验、理论或文学互文，最后回落到现实判断。
- 如果文章判断使用高风险 CrossFrame 概念，按 `../crossframe/references/read-routing-map.md` 读取对应概念卡，并用 `../crossframe/worksheets/concept-fidelity-check.md` 做保真检查。

## 硬规则

- 不准只写正文，不出底稿。
- 不准用检索材料决定文章立场；检索只能佐证、限定、反驳或补现实感。
- 不准把批判写成人格审判、嘲讽、道德宣判或情绪宣泄。
- 不准把术语当结论。前台说人话，后台保留概念链。
- 不准伪造原文、出处、页码、作者观点；不确定原句时只能意译或写思想映射。
- 不准让经典参照接管文章命题；引用只能照亮现实机制，不能压过证据。
- 不准把 CrossFrame 写成万能解释机器；超出结构判断能力时要写边界。
- 不准把文章写成新闻综述、资料拼贴或百科解释，除非用户明确要这种体裁。
- 文章的段落顺序必须服从信息依赖：读者先需要知道什么，后面的判断才能成立。

## 默认输出

自动成文默认输出两个连续部分：

```text
# 结构洞察底稿

# 文章正文
```

`结构洞察底稿` 至少包含：

- 分析对象与事实边界
- 表面现象与高成本信号
- CrossFrame 路由与本次读取
- 尺度窗口与机制候选
- 责任链、受益链、成本链
- 权力、证据与弱信号检查
- 检索材料与证据边界
- 反向条件与证据缺口
- 概念上升与参照系：上位概念、思想参照、引用方式、回落到现实的句子、引用风险
- 文章中心命题、开头入口、递进顺序、结尾余味

`文章正文` 至少包含：

- 一个具体入口
- 一个清楚的中心命题
- 3-5 个递进段落或小节
- 按需加入概念上升、经典/理论参照和回落现实的段落
- 至少一个边界、反例、撤回条件或证据缺口
- 一个不喊口号、不把问题封死的结尾

## 写作气质

- 有锋利判断，但不装作全知。
- 有批判性，但保留证据边界和反向条件。
- 能指出责任链，但不把复杂问题压成某个人的坏。
- 面向普通读者，第一段删掉所有术语后仍能读懂。
- 结尾要有余味，不用宏大口号替代思考。
