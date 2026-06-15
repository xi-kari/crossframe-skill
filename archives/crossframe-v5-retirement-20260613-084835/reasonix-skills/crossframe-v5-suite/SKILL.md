---

name: crossframe-v5-suite
description: CrossFrame v5 Suite 是 CrossFrame v5 skill family 的总调度入口。仅通过 /crossframe-v5-suite 斜杠命令触发，不被任何自然语言被动触发。内部只做一次选择、轻量工作流调度和 sibling skills 连续读取顺序编排。
metadata:
  trigger: slash-only
---

# CrossFrame v5 Suite

`crossframe-v5-suite` 是 v5 总调度 skill，不替代任何专项 skill。它保持轻量，只做四件事：

1. 通过原生选择弹窗或文本降级确认输出模式与角色。
2. 判断用户任务属于哪条工作流。
3. 安排 sibling skill 连续读取顺序。
4. 自动跑完整链路，直到最终交付物和 review 完成。

> **本 skill 仅通过 `/crossframe-v5-suite` 斜杠命令触发。** 不被自然语言被动触发。

## 默认行为

suite 被触发后，默认最终进入 `full-visible-v5-longform`，即完整可见底稿 + 完整长文正文 + review。只有用户明确说“只要/不要文章/短答/表格/清单/纯诊断/仅行动方案”等，才关闭文章层。

```text
crossframe-v5 -> [needed sibling skills] -> crossframe-v5-essay(full-visible-v5-longform) -> crossframe-v5-review -> final assembly
```

最终可见输出默认按以下顺序装配：

```text
# 结构洞察底稿
# 文章正文
# CrossFrame v5 Review
```

review 是输出前总闸和附录，不是正文替代品。若 review 只提出小修，优先把小修吸收进正文或在 review 附录中列出；不得用一份评审报告覆盖上游底稿和正文。

## 四条硬规则

1. **一次选择。** 模式、角色和主题敏感度只在 suite 入口确定一次。除非用户主动改选，下游 skill 不得再次弹窗、再次询问角色，或要求用户重新描述任务。
2. **自动全链路。** 选择完成后必须在同一轮工作中继续执行 `crossframe-v5 -> needed sibling skills -> crossframe-v5-essay -> crossframe-v5-review -> final assembly`。中间的诊断提纲、调度提纲、底稿和专项结论都是链路状态，不得作为终点停下并要求用户说“继续”。只有用户显式关闭文章层或 review，才允许缩短链路。
3. **轻量调度。** suite 不读取 v5 源索引、不生成 `v5-read-state-capsule`、不直接选择孤立概念卡。suite 只把 `selection_state` 与 `workflow_state` 传给 `crossframe-v5`；由 `crossframe-v5` 选择连读包、生成读态胶囊并执行源锚点校验。
4. **最终装配。** 默认长文链路的最终可见输出必须保留 `结构洞察底稿` 与 `文章正文`，再追加 `CrossFrame v5 Review`。上下文压力过高时，先压缩 review 和底稿摘要，不得丢正文；除非用户明确只要评审，否则只输出 review 判为装配失败。

## 源文本锚点规则

- `crossframe-v5` 生成的 `v5-read-state-capsule` 必须列出本次判断依赖的 v5 source modules、源段落锚点、所属连读包、相邻约束和降档边界。
- 所有承担判断作用的 CrossFrame v5 概念，必须能回指到胶囊中的源锚点；不能回指的内容只能标为“本文推断 / 外部思想映射 / 表达转译”，不得写成框架原义。
- 源锚点校验由 `crossframe-v5` 建立，并在 essay/review 前复核：若中心命题、机制候选或行动边界找不到源锚点，要删除、降档或显式标注为非框架推断。
- 正文不得出现“长文契约”“调度提纲”“我将继续”等流程说明；这些只能存在于底稿或内部状态。

## 必须读取

每次触发后读取：

1. `references/workflow-routing-map.md`
2. `references/output-mode-selector.md`
3. `protocols/suite-dispatch-protocol.md`
4. `templates/mode-selection-dialog.md`
5. `templates/suite-reasoning-outline.md`

然后按路由读取对应 sibling skill。基础结构判断通常先读 `../crossframe-v5/SKILL.md`。

## 调度提纲

```text
调度提纲
- 任务类型：
- 工作流：
- 输出模式：
- 角色：
- 主题敏感度：
- 必读 skill：
- workflow_state：
- 按需读取：
- 正文声口：
- 输出档位：
- 不读取：
- 质量闸：
```

调度提纲只作为链路状态。除非用户要求审计流程，不要把调度提纲作为最终输出独立展示，更不要展示后停下等待“继续”。

## 禁止

- 禁止为了完整感触发全部 skill。
- 禁止跳过 v5 连读包直接读 concept card。
- 禁止跳过 `crossframe-v5` 的七闸与判断档位直接写文章。
- 禁止公共议题不查源却做强判断。
- 禁止把 `crossframe-v5-review` 当形式收尾。
- 禁止自然语言触发 suite；入口必须由用户显式使用 `/crossframe-v5-suite`。
- 禁止在选择完成后要求用户输入“继续”才进入 essay 或 review。
- 禁止 suite 承担轻量调度之外的源结构工作；v5 source modules、连读包与 `v5-read-state-capsule` 必须交给 `crossframe-v5` 中枢处理。
- 禁止默认长文链路最终只输出 `CrossFrame v5 Review`，丢失 `结构洞察底稿` 或 `文章正文`。
