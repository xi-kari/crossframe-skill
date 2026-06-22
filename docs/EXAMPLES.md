# 使用样例

> 这些例子用于说明工作流，不代表项目对现实对象给出最终判断。
> 首页只使用安全模拟样例；真实/高敏主题只展示结构，不展示完整结论。
> 涉及历史、公共议题、现实组织、宗教/哲学争议时，必须保留 `source_id`、`claim_id`、`evidence grade`、`withdrawal condition` 和 `publish_boundary`。

这些样例只展示输入、工作流和输出摘要，不复制完整长文。

## 安全模拟样例

适合首页、README 和安装说明展示。

### 1. 概念追问

输入：

```text
/crossframe-suite 2+1，一个问题什么时候不该被直接回答？
```

工作流：

```text
crossframe -> concept explanation -> crossframe-essay -> crossframe-review
```

输出应把事实问题、概念问题和意义问题拆开。无法强证的部分使用开放断言，不把需要保留边界的问题硬写成终局答案。

### 2. 历史接口

输入：

```text
/crossframe-suite 分析一个虚构城邦从扩张到停滞的结构原因
```

工作流：

```text
crossframe -> crossframe-history -> crossframe-essay -> crossframe-review
```

如果没有具体史料台账，只能标为历史草稿档。历史机制候选需要 `source_id` 和 `claim_id`，不能把单一来源族写成史料闭合。

### 3. 公共证据

输入：

```text
/crossframe-suite 一个虚构平台有申诉入口，能否证明治理有效？
```

工作流：

```text
crossframe -> crossframe-public -> crossframe-essay -> crossframe-review
```

输出需要区分“有申诉入口”和“治理有效”。公共判断必须保留证据档位、降档理由和行动边界。

### 4. 组织机制

输入：

```text
/crossframe-suite 为什么一个虚构团队反复复盘，却没有真实改变？
```

工作流：

```text
crossframe -> crossframe-org -> crossframe-essay -> crossframe-review
```

输出应检查授权链、反馈写回、责任转移和低风险试点，不把问题压成“态度不好”或“执行力不足”。

### 5. 完成后追问

输入：

```text
刚才那篇匿名结构分析，还能往哪儿追问？
```

前提：上一轮已经完成诊断、文章和 review。

工作流：

```text
previous_context -> crossframe-inquiry
```

输出应复用上一轮 `claim ledger` 和 review warnings，给出 3-5 个追问点、反证方向、补证入口、迁移条件和行动边界。

mini 输出示例：

- Q1：如果要反驳中心命题，最强反例是什么？
- Q2：哪条 claim 最需要补 `source_id`？
- Q3：这个机制迁移到另一个组织时，哪些条件必须相同？

## 真实/高敏主题样例

真实历史、现实组织、公共争议或宗教/哲学争议不建议放在首页。仓库文档中如需保留，只展示工作流结构，不展示完整判断。

最小结构应包括：

- `source_id`：材料名称、时间、来源类型和使用位置。
- `claim_id`：每条中心命题对应的台账编号。
- `evidence grade`：证据能支撑到哪一档，不能支撑什么。
- `withdrawal condition`：什么情况下必须撤回或降档。
- `publish_boundary`：能否公开发布，以及需要保留哪些边界说明。
