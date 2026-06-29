# v6 半量化案例试跑模板

```text
trial_id:
source_case:
case_domain:
trial_status:
primary_scale:
judgment_grade:
action_ceiling:
downgrade_triggered:
anchor_revision_required:
template_revision_required:
counterexample_pressure:
rater_record:
```

## 源案例边界

- 源案例：
- 本次只使用的材料：
- 本次不新增的事实：
- 缺失材料：

## 试跑目的

说明本案例要测试哪个 v6 构念、哪一闸、哪类证据台账问题或哪种误用风险。

## 七闸半量化剖面

| gate | gate_state | score | 本案依据 | 降档或补证要求 |
| --- | --- | --- | --- | --- |
| 对象闸 |  |  |  |  |
| 证据闸 |  |  |  |  |
| 尺度闸 |  |  |  |  |
| 责任闸 |  |  |  |  |
| 观测闸 |  |  |  |  |
| 权力闸 |  |  |  |  |
| 行动闸 |  |  |  |  |

## 证据台账摘记

| evidence_id | 来源类型 | directness | independence | verifiability | 不能证明什么 | diagnostic_force |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

## 构念剖面

只写本案例实际命中的构念，不做总分、不做排名。

| construct_id | 当前读数 | 支撑材料 | 反向条件 | 是否需要校准修订 |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## 机制候选更新

| mechanism_id | 机制候选 | 支持材料 | 反例压力 | update_direction | 撤回条件 |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## 判断档位与行动上限

- judgment_grade：
- action_ceiling：
- 不能升级的原因：
- 可撤回的小动作：

## 反例压力与撤回条件

- 已发现反例：
- 仍缺失的反例入口：
- 哪些新材料会撤回判断：
- 哪些新材料会降级行动上限：

## 评分者原始记录

如果本 trial 使用双评分者，保留 `rater_a` 与 `rater_b` 的原始读数。不要先合并。

## 写回结果

- downgrade_triggered：
- anchor_revision_required：
- template_revision_required：
- 写回到哪个锚点、模板、checker 或文本边界：

## 本案例不能证明

列出本案例不能证明的内容，尤其是外部有效性、现实正确性、方法优越性和可处置性。
