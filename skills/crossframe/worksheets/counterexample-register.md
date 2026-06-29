# v5.0 半量化 DLC 反例登记表

反例是治理事件，不是附录材料。它必须改变边界说明、判断档位、行动上限、校准锚点、工具行为或版本记录中的至少一项。

## 反例类型

| 类型 | 处理 |
| --- | --- |
| minor | 加入边界说明 |
| repeated | 判断降级或校准锚点修订 |
| high_harm | 暂停相关用法并启动误用复核 |
| systemic | 引入替代机制或替代框架竞争 |
| misuse | 发布阻断、工具红线或模板修改 |
| unrecoverable | 退出转移、保存演化记忆 |

## 字段

```text
counterexample_id:
关联 claim_id:
关联 construct_id:
关联 mechanism_id:
材料来源:
反例类型:
影响范围:
文本后果:
工具后果:
行动上限变化:
版本写回:
撤回条件:
```

## 强制写回

- `misuse` 和 `high_harm` 必须写明工具后果和行动上限变化。
- 重复反例必须检查锚点是否过松。
- 系统性反例必须允许替代机制或替代框架竞争。
- 不可修复案例不得被包装成框架成功案例。
- 低权力主体无法安全提交反例时，不得解释为“无反例”。

## 输出摘要

```text
counterexample_id:
counterexample_type:
impact_scope:
text_consequence:
tool_consequence:
action_ceiling_change:
version_writeback:
withdrawal_condition:
```
