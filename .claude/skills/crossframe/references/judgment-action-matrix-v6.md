# v6.0 判断档位与行动上限矩阵

本矩阵把七闸状态、证据台账、命题台账、概念契约和反例压力连接到最高允许 `judgment_grade` 与 `action_ceiling`。它不是升级器；它只限制判断和行动。

## 基本原则

- 分数只能解释为什么某一闸处于 `pass / weak / fail / blocked`。
- 高分不能自动升级判断档位。
- 任一关键闸失败时，判断必须降档，行动上限必须收窄。
- 高责任场景即使七闸都显示较强，也必须追加强判断八件套、来源台账、受影响位置反馈和外部复核。

## 判断档位

| judgment_grade | 使用条件 | 不允许 |
| --- | --- | --- |
| `light_observation` | 对象或证据不足，只能记录低风险观察 | 不允许定性、追责、发布或处置 |
| `open_assertion` | 对象边界基本清楚，有可撤回机制候选和反向条件 | 不得作为处置依据 |
| `full_diagnosis` | 七闸无 fail/blocked，有中高成本证据和机制候选 | 不允许绕过外部复核或受影响位置反馈 |
| `strong_judgment` | 高责任八件套、来源台账、claim ledger、反例搜索和复核条件齐备 | 不自动授权处分、封禁、开除或公共定性 |
| `low_condition_action` | 问题紧急但证据不完整，只能做可撤回低风险动作 | 不允许扩大为强判断 |
| `exit_transfer` | 内部修复不可行或权力封闭，需要保护、保存证据、转移承接 | 不允许把退出写成道德判决 |

## 行动上限

| action_ceiling | 允许动作 | 触发条件 |
| --- | --- | --- |
| `observe` | 观察、记录、整理材料 | 对象不清或证据混乱 |
| `ask_for_evidence` | 补证、追问反例、建立材料边界 | 证据不足但对象边界可见 |
| `internal_review` | 内部复盘、低风险调整、机制修补 | 完整诊断草案但不适合公开或处置 |
| `publish_with_boundary` | 带来源、撤回条件、不能证明边界的公开表达 | 公共材料可核验且低权力反例入口存在 |
| `block_publication` | 阻断公开发布、阻断评分输出或阻断工具使用 | 权力闸、行动闸、反身性或公共风险不足以支撑发布 |
| `exit_transfer` | 保护、外部承接、证据保存、停止内部消耗 | 权力封闭、修复窗口关闭或安全风险上升 |

## 强制降档规则

| 条件 | 最高 judgment_grade | 最高 action_ceiling |
| --- | --- | --- |
| 对象闸 `fail` 或 `blocked` | `light_observation` | `observe` |
| 证据闸分值低于 3 | `open_assertion` | `ask_for_evidence` |
| 尺度闸 `fail`，且高尺度叙事压低低尺度痛苦 | `open_assertion` | `block_publication` |
| 责任闸 `fail`，且结论影响资格、名誉、资源或权利 | `open_assertion` | `block_publication` |
| 观测闸 `blocked`，且公开会改变对象处境 | `light_observation` | `block_publication` |
| 权力闸分值低于 3，且存在低权力主体 | `open_assertion` | `block_publication` |
| 行动闸分值低于 3 | `open_assertion` | `ask_for_evidence` |
| `claim ledger` 缺失 | `light_observation` | `observe` |
| 高风险概念缺少概念契约 | `open_assertion` | `ask_for_evidence` |
| 来源台账缺少“不能证明什么” | `open_assertion` | `ask_for_evidence` |
| 反例搜索缺失且会影响公共记忆 | `open_assertion` | `block_publication` |
| 案例库试跑或 checker 通过 | 不提高档位 | 不提高行动上限 |

## 高责任强判断候选

`strong_judgment` 只能被申请，不能被分数自动推出。申请前必须同时具备：

- 七闸无 `fail` 或 `blocked`。
- 证据闸、权力闸、行动闸均不低于 3。
- 来源台账、证据台账和 claim ledger 可回指。
- 高风险概念通过概念卡和概念契约。
- 反例搜索状态不是 `missing`。
- 有撤回条件、复核入口和停止条件。
- 受影响位置能安全补证或反驳。

## 输出约束

输出时只能呈现结构剖面，例如“证据可支撑度弱、低权力反例入口不足、行动上限阻断公开发布”。不得把多个维度合成对象总分、关系质量分、组织健康分或文明阶段分。

本矩阵只帮助整理结构判断，不替代现实调查、专业判断、受影响位置反馈、外部复核和最终责任承担。分数只能触发降级、复核或补证，不能单独授权处置。
