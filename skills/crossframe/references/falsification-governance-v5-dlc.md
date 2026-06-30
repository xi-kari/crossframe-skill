# v5.0 半量化 DLC 反例、撤回与治理写回

半量化 DLC 把反例视为治理事件，而不是附录材料。反例、评分者分歧和误用案例必须改变判断边界、行动上限、模板、checker、版本记录或发布口径。

## 反例分级

| counterexample_type | 处理方式 | 必须写回 |
| --- | --- | --- |
| `minor` | 加边界说明或补证要求 | 文本边界 |
| `repeated` | 降级判断或修订校准锚点 | 锚点与案例库 |
| `high_harm` | 暂停相关用法，启动误用复核 | 行动上限与工具阻断 |
| `systemic` | 引入替代机制或替代框架竞争 | 机制候选与文档边界 |
| `misuse` | 阻断发布、加工具红线或改模板 | checker、模板、使用说明 |
| `unrecoverable` | 退出转移，保存演化记忆 | 停止条件与转移记录 |

## 撤回触发

以下情况必须撤回或降档：

- 关键事实被证伪。
- 低权力主体提交的反例改变责任链。
- 新证据显示尺度窗口错误。
- 机制候选不能解释关键材料。
- 工具输出被用于处分、封禁、资格判断、资源剥夺或公共名誉定性。
- 评分者分歧改变 `judgment_grade` 或 `action_ceiling`，但锚点未修订。
- 公开发布会制造报复、沉默、表演或证据污染。

## 评分者分歧治理

评分者一致性只验证协议稳定性，不验证现实真相。处理流程：

1. 保留 `rater_a` 和 `rater_b` 原始读数。
2. 标记 gate_state、score、judgment_grade 和 action_ceiling 的分歧。
3. 判断分歧是否改变发布边界或行动上限。
4. 若改变，优先修订锚点、模板或证据要求。
5. 不要求评分者为了好看而收敛。

## 误用复核

以下行为必须进入误用复核：

- 把半量化表包装成完整诊断。
- 把评分者一致性包装成现实正确性。
- 把案例库覆盖率包装成外部有效性。
- 内部压力测试结果不能用于营销、认证或证明安全。
- 让委托方单方控制证据入口、反馈入口和发布口径。
- 把低权力主体无法提交反例解释为“无反例”。
- 将 AI 自动评分用于强判断、公开定性或组织处置。

## 版本写回

每条需要写回的反例至少记录：

```text
counterexample_id:
related_claim_ids:
related_construct_ids:
related_mechanism_ids:
source_id:
counterexample_type:
impact_scope:
text_consequence:
tool_consequence:
action_ceiling_change:
version_writeback:
withdrawal_condition:
```

写回目标可以是：

- `docs/CROSSFRAME_V5_DLC.md`
- `skills/crossframe/references/construct-map-v5-dlc.md`
- `skills/crossframe/references/judgment-action-matrix-v5-dlc.md`
- `skills/crossframe/worksheets/*`
- `skills/crossframe-casebook/examples/v5-dlc-quant-trials/*`
- `scripts/check_v5_dlc_*`
- release notes 或后续版本变更说明

## 停止使用条件

以下条件成立时，应暂停相关 v5 DLC 工具或模板：

- 反复出现同类误用，且 checker 没有阻断。
- 高伤害反例指向同一构念或同一行动上限。
- 评分者在关键闸口长期无法理解同一锚点。
- 使用方试图把结果接入绩效、审核、封禁、处分或风控系统。
- 受影响位置无法安全补证或反驳。

本工具只帮助整理结构判断，不替代现实调查、专业判断、受影响位置反馈、外部复核和最终责任承担。分数只能触发降级、复核或补证，不能单独授权处置。
