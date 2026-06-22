# Claim Ledger / 命题台账

本模板用于把 CrossFrame 输出中的中心命题、机制判断、行动建议、高风险概念使用、文章转译和公共定性，登记成可审计的命题台账。

它不是正文，也不是完整推理链。它的作用是防止模型只模仿 CrossFrame 语气，而没有交代每个判断从哪里来、最多能说到哪一档、不能证明什么。

## 使用位置

- `crossframe` 核心层在完成事实边界、七闸、机制候选、概念保真和源锚点完整性检查后生成。
- `crossframe-essay` 只能从本台账展开正文，不得新增未登记的中心命题、强机制句、行动建议、公共定性或高风险概念判断。
- `crossframe-review` 必须抽取正文 3-5 个承担判断作用的句子，反查是否存在对应 `claim_id`。
- 若正文出现未登记命题，只能删除、降档、补台账，或标为“本文推断 / 表达转译 / 外部思想映射”。

## 命题类型

```text
fact_boundary：事实边界
mechanism_candidate：机制候选
open_assertion：开放断言
judgment_boundary：判断边界
action_ceiling：行动上限
concept_use：高风险概念使用
expression_translation：表达转译
external_mapping：外部思想映射
source_limited_context：来源限定背景
```

## 规范化字段

面向用户或底稿展示时可以使用中文标签；面向 schema、脚本或结构化检查时必须使用以下规范值。

| 中文显示 | normalized value |
| --- | --- |
| 轻量观察 | `light_observation` |
| 开放断言 | `open_assertion` |
| 完整诊断 | `full_diagnosis` |
| 强判断 | `strong_judgment` |
| 低条件行动 | `low_condition_action` |
| 退出转移 | `exit_transfer` |
| 内部使用 | `internal_only` |
| 可发布但需边界 | `publishable_with_boundary` |
| 阻断 | `blocked` |

## 前台摘要与完整台账

前台可以只展示命题台账摘要，但不得把摘要伪装成完整台账。若展示表缺少 `source_anchor`、`mechanism_id`、`concept_contract`、`source_ledger_id` 或 `publish_boundary`，只能命名为“命题台账摘要”，并说明完整台账仍在后台或待补齐。

完整台账至少保留以下字段：`claim_id`、`claim_type`、`visible_claim/body_excerpt`、`source_anchor`、`mechanism_id`、`concept_contract`、`source_ledger_id`、`judgment_grade`、`action_ceiling`、`撤回条件`、`publish_boundary`、`body_mappings`。

字段级要求：

- `mechanism_candidate` 必须有 `mechanism_id`，不能只写“机制一/机制二”。
- `concept_use` 必须有 `concept_contract`，否则只能作为表达提示，不能承担判断。
- `open_assertion` 必须触发 `contract-open_assertion`；若没有触发，必须解释为什么不是开放断言，否则按伪未触发处理。
- `strong_judgment` 必须有 `source_ledger_id`，并能说明来源能支持什么、不能证明什么和行动上限。

## 台账字段

| claim_id | 可见命题 / 正文短摘 | claim_type | 支持事实 / source_anchor | 机制候选 | 概念契约 | 来源台账 | judgment_grade | action_ceiling | 撤回条件 | publish_boundary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CL1 |  | fact_boundary / mechanism_candidate / open_assertion / judgment_boundary / action_ceiling / concept_use / expression_translation / external_mapping / source_limited_context | F1 / V5-H / bundle_id / source-ledger-id | M1 / M2 / 不适用 | concept_id / contract_id / 不适用 | S1 / 不适用 | light_observation / open_assertion / full_diagnosis / strong_judgment / low_condition_action / exit_transfer | 观察 / 补证 / 低风险试探 / 暂停建议 / 不得行动 |  | internal_only / publishable_with_boundary / blocked |

## 必填规则

每条承担判断作用的命题必须至少填写：

```text
claim_id
可见命题 / 正文短摘
claim_type
支持事实 / source_anchor
judgment_grade
action_ceiling
撤回条件
publish_boundary
```

涉及高风险概念时，必须追加：

```text
概念契约
对应概念卡
对应 v5 连续联读包
降档条件
```

涉及真实公共对象、最新事实、机构、平台、人物、公司、政策、AI/过程性产物时，必须追加：

```text
来源台账
来源能支持什么
来源不能证明什么
证据档位
使用位置
```

## 禁止升级

以下情况不得把命题升级为强判断：

* 没有 source_anchor。
* 没有来源台账，且命题涉及真实公共对象或最新事实。
* 七闸中任一闸为 `fail` 或 `blocked`。
* 证据闸为 `weak`，且没有补证清单或撤回条件。
* 概念契约为 `partial` 或 `fail`。
* required_closure 未读完。
* 正文命题没有对应 `claim_id`。
* 写作技法、隐喻、经典参照或外部理论成为判断来源。

## 正文映射

成文前填写：

| body_excerpt | claim_id | mapping_status | handling | 正文位置 |
| --- | --- | --- | --- | --- |
|  | CL1 / null | same_strength / downgraded / stronger_than_claim / unmapped | keep / delete / downgrade / mark_expression_translation / needs_rewrite | 段落 / 小节 / 标题 |

`mapping_status=unmapped` 时，`claim_id` 必须为 `null`，且 `handling` 必须说明删除、降档、表达转译或重写。

## 失败处理

| 失败类型 | 处理 |
| --- | --- |
| 没有 claim ledger | 不进入正文或 review 合格判定 |
| 中心命题无 claim_id | 删除、补台账或降档 |
| 正文强于台账 | 重写正文或降低判断档位 |
| 行动建议无行动上限 | 改为观察、补证或暂停建议 |
| 高风险概念无契约 | 补读概念契约；不能补则改为表达转译 |
| 来源只能支持背景却支撑强判断 | 降为来源限定背景或开放断言 |
| 撤回条件写不出 | 不得高于开放断言 |
| 台账摘要冒充完整台账 | 改名为命题台账摘要，或补齐完整台账字段 |
| mechanism_candidate 无 mechanism_id | 补机制编号和事实/反证回指；补不出则降为解释提示 |
| open_assertion 未触发概念契约 | 读取 `contract-open_assertion`；不能通过则降档、删除或表达转译 |
| 标题强于台账 | 改写标题、降档标题或补台账；不得用标题偷渡强判断 |
| 生成层自称质量闸通过 | 改为自检摘要，交由 review 执行反向否决最小块 |
