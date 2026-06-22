# 使用样例

这些样例只展示输入、工作流和输出摘要，不复制完整长文。

## 1. 哲学概念

输入：

```text
/crossframe-suite 2+1，生命的第一因是什么？
```

工作流：

```text
crossframe -> concept explanation -> crossframe-essay -> crossframe-review
```

输出应区分科学层、结构层和意义层。无法强证的部分使用开放断言，不把哲学问题硬写成事实结论。

## 2. 历史分析

输入：

```text
/crossframe-suite 分析苏联的整个始末
```

工作流：

```text
crossframe -> crossframe-history -> crossframe-essay -> crossframe-review
```

如果没有具体史料台账，只能标为历史草稿档。历史机制候选需要 `source_id` 和 `claim_id`，不能把单一来源族写成史料闭合。

## 3. 平台治理

输入：

```text
/crossframe-suite 分析这个平台申诉机制是否只是表面治理
```

工作流：

```text
crossframe -> crossframe-public -> crossframe-essay -> crossframe-review
```

输出需要区分“有申诉入口”和“治理有效”。公共判断必须保留证据档位、降档理由和行动边界。

## 4. 团队复盘

输入：

```text
/crossframe-suite 为什么这个团队越复盘越失真？
```

工作流：

```text
crossframe -> crossframe-org -> crossframe-essay -> crossframe-review
```

输出应检查授权链、反馈写回、责任转移和低风险试点，不把问题压成“态度不好”。

## 5. 完成后追问

输入：

```text
那我还应该继续想什么？
```

前提：上一轮已经完成诊断、文章和 review。

工作流：

```text
previous_context -> crossframe-inquiry
```

输出应复用上一轮 `claim ledger` 和 review warnings，给出 3-5 个追问点、反证方向、补证入口、迁移条件和行动边界。
