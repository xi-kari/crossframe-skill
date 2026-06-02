# Suite Reasoning Outline

默认输出：

```text
调度提纲
- 任务类型：
- 工作流：
- 必读 skill：
- 按需读取：
- 不读取：
- 质量闸：
```

## 字段说明

- `任务类型`：用普通话说明用户真正要的交付物。
- `工作流`：写 skill id 链路，例如 `crossframe -> crossframe-public -> crossframe-essay -> crossframe-review`。
- `必读 skill`：本次必须读取的 skill。
- `按需读取`：只列触发了条件的概念卡、专项协议或模板。
- `不读取`：列 1-3 个容易误触发但本次不需要的 skill，防止全量加载。
- `质量闸`：完整评审、轻量自检或无需评审，并写原因。

## 轻量版

当用户只要最终结果：

```text
本次按 `crossframe -> crossframe-essay -> crossframe-review` 处理：先诊断，再成文，最后过质量闸。
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
