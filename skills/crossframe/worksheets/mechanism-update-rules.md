# v6.0 机制候选更新表

机制候选不输出总排序，不输出“某机制 82 分”，也不输出精确预测概率。v6.0 只记录具体证据如何增强、削弱、保留、待证或撤回某一条机制边。

## 更新方向

| 值 | 含义 |
| --- | --- |
| strengthen | 证据增强该机制边 |
| weaken | 证据削弱该机制边 |
| neutral | 证据相关但诊断力不足 |
| pending | 需要补证 |
| withdraw | 关键反例成立，应撤回该机制候选或机制边 |

## 字段

```text
mechanism_id:
mechanism_edge_id:
机制描述:
支持事实:
反向证据:
证据诊断力:
更新方向:
当前状态:
能解释什么:
不能解释什么:
可观察预测:
撤回条件:
对应 claim_id:
行动上限:
```

## 规则

- 一条证据只能更新它实际命中的机制边。
- `smoking-gun` 式强证据只能增强命中的边，不能替整套结构背书。
- `hoop-test` 式必要证据失败时，应削弱或撤回对应机制候选。
- 没有反向证据和“不能解释什么”的机制候选，最高开放断言。
- 机制更新不能替代命题台账、来源台账、七闸复核或概念契约。

## 输出摘要

```text
mechanism_id:
mechanism_edge_id:
update_direction:
diagnostic_force:
current_state:
claim_id:
action_ceiling:
withdrawal_condition:
```
