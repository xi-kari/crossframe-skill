# Bad Overtrigger Case

## 坏输出

本次我将读取 `crossframe-v5`、`crossframe-v5-essay`、`crossframe-v5-review`、`crossframe-v5-dialogue`、`crossframe-v5-casebook`、`crossframe-v5-public`、`crossframe-v5-org`、`crossframe-v5-teach`、`crossframe-v5-debate`、`crossframe-v5-notebook`，以确保完整。

## 为什么失败

这不是严谨，而是调度失效：

- 没有先判断用户的最终交付物。
- 把所有 skill 都读入，会稀释真正关键的协议。
- 容易让输出变成术语拼贴。
- 无法解释为什么某个专项 skill 被读取。

## 好输出

本次目标是公共评论文章，所以走：

```text
crossframe-v5 -> crossframe-v5-public -> crossframe-v5-essay -> crossframe-v5-review -> final assembly
```

不读取 `crossframe-v5-org`、`crossframe-v5-casebook`、`crossframe-v5-teach`，因为这次不是组织修复、案例沉淀或概念教学。
