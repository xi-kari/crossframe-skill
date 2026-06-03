# Suite Reasoning Outline

默认输出：

```text
调度提纲
- 任务类型：
- 工作流：
- 必读 skill：
- 按需读取：
- 连续联读包：
- 正文声口：
- 输出档位：
- 不读取：
- 质量闸：
```

## 字段说明

- `任务类型`：用普通话说明用户真正要的交付物。
- `工作流`：写 skill id 链路，例如 `crossframe -> crossframe-public -> crossframe-essay -> crossframe-review`。
- `必读 skill`：本次必须读取的 skill。
- `按需读取`：只列触发了条件的概念卡、专项协议或模板。
- `连续联读包`：只列 `continuity-bundles.md` 中本次触发的包名；未触发时写“未触发”。
- `正文声口`：开放式可读分析默认写“现代编辑底色”；问题型主题写“答复体”；公共评论/思想文章写“评论体”；显式中性报告写“关闭文章声口”。
- `输出档位`：开放式可读分析和文章类默认写 `full-visible-v3-longform / 3.0混合长文`；明确短答、表格、备忘录、纯诊断时写对应交付物。
- `不读取`：列 1-3 个容易误触发但本次不需要的 skill，防止全量加载。
- `质量闸`：完整评审、轻量自检或无需评审，并写原因。

如果用户没有指定格式，但看起来想要可读分析，`任务类型` 写“开放式可读分析”，`工作流` 默认写 `crossframe -> crossframe-essay -> crossframe-review`，`正文声口` 默认写“现代编辑底色”，`输出档位` 默认写 `full-visible-v3-longform / 3.0混合长文`。

## 轻量版

当用户只要最终结果：

```text
本次按 `crossframe -> crossframe-essay -> crossframe-review` 处理，输出档位为 `full-visible-v3-longform`：先诊断，再确认连续联读包，再给完整可见底稿和完整长文正文，最后过质量闸。
```

## 禁止写法

不要写：

```text
我会读取全部 CrossFrame skills 以确保完整。
```

应写：

```text
本次不读取 `crossframe-casebook` 和 `crossframe-teach`，因为目标是公共评论文章，不是案例沉淀或概念教学。
```
