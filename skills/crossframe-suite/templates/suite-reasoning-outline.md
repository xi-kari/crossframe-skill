# Suite Reasoning Outline

默认输出：

```text
调度提纲
- 任务类型：
- 工作流：
- 必读 skill：
- 按需读取：
- 连续联读包：
- 主题敏感度：
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
- `主题敏感度`：写 `low / normal / vulnerable / high-stakes`；若为 `vulnerable` 或 `high-stakes`，说明先承接人或先审计的保护动作。
- `正文声口`：按角色和 `topic_sensitivity` 写“中性分析体 / 中性决定体 / 答复体 / 评论体”；显式要求编辑口吻时说明覆盖原因。
- `输出档位`：suite 默认写 `full-visible-v3-longform / 3.0混合长文`；只有用户显式要求短答、表格、清单、纯诊断或不要文章时写对应交付物。
- `不读取`：列 1-3 个容易误触发但本次不需要的 skill，防止全量加载。
- `质量闸`：完整评审、轻量自检或无需评审，并写原因。

只要用户没有显式关闭文章层，`输出档位` 默认写 `full-visible-v3-longform / 3.0混合长文`，`工作流` 默认在必要专项 skill 后追加 `crossframe-essay -> crossframe-review`。

## 轻量版

当用户只要最终结果：

```text
本次按 `crossframe -> [needed sibling skills] -> crossframe-essay -> crossframe-review` 处理，输出档位为 `full-visible-v3-longform`：先完成必要专项判断，再给完整可见底稿和完整长文正文，最后过质量闸。
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
