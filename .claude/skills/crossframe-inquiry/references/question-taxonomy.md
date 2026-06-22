# Question Taxonomy / 追问类型表

## 一、按认知动作分类

| question_type | 作用 | 适合对象 |
| --- | --- | --- |
| clarify_object | 澄清对象 | 任务边界不清 |
| separate_scale | 拆尺度 | 多尺度混合问题 |
| test_mechanism | 检验机制 | mechanism_candidate |
| seek_counterexample | 找反例 | open_assertion / strong claim |
| evidence_upgrade | 补证升级 | weak evidence |
| evidence_downgrade | 证据降级 | overclaimed output |
| concept_fidelity | 概念保真 | high-risk concept |
| action_boundary | 行动边界 | action advice |
| responsibility_position | 责任位置 | org / relationship / public |
| transfer_conditions | 迁移条件 | casebook / history / public |
| value_conflict | 价值冲突 | philosophy / public / relationship |
| stop_condition | 停止条件 | vulnerable / high-stakes |

## 二、按输出后的使用阶段分类

| stage | 问题目标 |
| --- | --- |
| after_diagnosis | 确认用户理解中心机制 |
| after_essay | 检查文章是否让用户产生误读或过强判断 |
| after_review | 处理 review warning |
| after_user_pushback | 吸收用户反对意见 |
| before_action | 降低行动风险 |
| before_transfer | 检查迁移条件 |
| before_publish | 检查发布边界 |

## 三、好追问标准

好追问必须具体、可回答、不诱导、有对象、有边界，并能改变后续路径。

坏追问：

```text
你怎么看？
你觉得呢？
你还有什么想法？
这对你意味着什么？
为什么你会这样想？
```

这些可以作为暖场，但不能作为 CrossFrame 结构追问。

## 四、问题强度

| 强度 | 适用场景 |
| --- | --- |
| light | 用户刚接触概念、短答、脆弱场景 |
| medium | 普通结构分析 |
| strong | 研究、论辩、组织复盘、历史比较 |
| adversarial | 只用于用户要求批判/反证，不用于关系或脆弱主题 |

默认 `medium`。高风险场景自动降为 `light` 或 `medium`。
