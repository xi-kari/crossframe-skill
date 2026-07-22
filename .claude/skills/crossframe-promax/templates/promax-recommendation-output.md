# Recommendation lock 生成合同

产物：`promax-recommendation.locked.json`
生成阶段：`P8`，在 position lock 之后
Schema：`promax-recommendation.schema.json`

先读取 run contract 的 `recommendation_required`，只能选择一个闭合分支。

## 未请求分支

当 `recommendation_required=false`，完整文件必须严格等于：

```json
{"status":"not_requested"}
```

不得增加 run binding、解释字段或方案。dossier 与 essay 也不得出现 `OPTION-*`、首选或推荐性语言。

## 必须建议分支

当 `recommendation_required=true`，根对象只包含：`schema_id`、`schema_version`、`run_id`、`source_snapshot_sha256`、`position_sha256`、`options`、`evaluation_dimensions`、`ranking`、`preferred_option_id`、`second_option_id`、`switch_conditions`、`inaction_consequences`、`authorization_status`、`locked_at`。

- `schema_id` 固定为 `crossframe.promax.v8.recommendation`，`schema_version=1`。
- `position_sha256` 必须由当前 position 的规范 JSON 字节计算，不能手抄旧值。
- `locked_at` 必须严格晚于 position 的 `locked_at`。
- `evaluation_dimensions` 非空，至少覆盖结构解释力、风险、可逆性、时间、受影响位置与授权边界中实际相关维度。

## 六类方案全集

`options` 至少六项，并且 `action_kind` 集合必须精确覆盖：

- `proactive_action`
- `delay`
- `probe`
- `exit_or_transfer`
- `status_quo`
- `inaction`

每条 option 只含 `option_id`、`action_kind`、`description`、`benefits`、`costs`、`risks`、`authorization_status`、`stop_conditions`、`rollback`。

- `option_id` 使用唯一 `OPTION-*`。
- `benefits`、`costs`、`risks`、`stop_conditions`、`rollback` 都必须为非空数组，且针对本方案写实质内容。
- option 的 `authorization_status` 只能诚实取 `requires_authorized_decision_maker`、`not_authorized` 或 `authorization_unknown`；分析不能自行登记为 `authorized`。
- 停止条件必须可观察，回滚必须说明可恢复状态或不可逆边界。

## 排序闭包

- `ranking` 必须是所有 option IDs 的完整排列，不漏项、不重复。
- `preferred_option_id=ranking[0]`，`second_option_id=ranking[1]`，二者不同。
- `switch_conditions` 至少一项明确写出 `second_option_id` 和触发切换的证据或路径信号。
- `inaction_consequences` 非空，说明时间、机会、保护、外部性或路径锁定成本；不行动不能被当作零成本。
- 根 `authorization_status` 只能是 `conditional_recommendation_only`、`not_authorized` 或 `authorization_unknown`；不得自我授予现实行动权限。

写盘后执行 `validate_recommendation_semantics()`。P7 的 `option_ranking_after` 必须与本 ranking 完全相同；P10 essay 必须按首次出现顺序表达完整 ranking，并逐项携带每个方案的全部字段语义。
