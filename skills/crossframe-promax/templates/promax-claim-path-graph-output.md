# Claim/path graph 生成合同

产物：`promax-claim-path-graph.json`
生成阶段：`P5`
Schema：`promax-claim-path-graph.schema.json`

`schema_id` 固定为 `crossframe.promax.v8.claim-path-graph`，`schema_version=1`。根对象必须包含 `run_id`、`source_snapshot_sha256`、`central_claim_id`、`central_claim_cycle`、`claims`、`mechanisms`、`path_nodes`、`path_edges`、`forecast_conditions`、`choice_boundary`、`updated_at`。

## Claim 闭包

- `claims[]` 至少一条，`claim_id` 使用 `CLAIM-*` 且唯一。
- `statement` 是可被支持或推翻的完整命题；`claim_type` 只能是 `factual`、`structural`、`mechanistic`、`path`、`forecast`、`normative`、`authorization`。
- 每条 claim 写 `evidence_refs`、至少一个 canonical `concept_ids`、`confidence` 和 `authorization_ceiling`。
- `confidence` 只能是 `low`、`medium`、`high`、`indeterminate`；事实置信不能替代规范或授权判断。
- `central_claim_id` 必须唯一指向 claims；中心 claim 的 `evidence_refs` 非空。

## 中心判断循环

`central_claim_cycle` 只能包含 `central_claim_id`、`initial_judgment`、`strongest_attack`、`revision`、`counterfactual`、`withdrawal_conditions`。六项都要有实质内容，并保持同一中心 claim。`revision` 必须说明攻击改变了什么或为何未改变，不能复述初判。

## 竞争机制

- 默认至少三个 `mechanisms`，绝对下限为两个；每个 `mechanism_id` 使用 `MECH-*`。
- 每个机制具有不同的 `label`、绑定中心 claim 的 `claim_ids`、非空 `distinguishing_conditions`。
- 区分条件必须能够产生不同的早期信号、反向信号或路径排序；同义改写不算竞争机制。
- 明确简单基线，防止所有证据只在复杂机制之间循环解释。

## 路径 DAG

- `path_nodes[]` 的 `node_id` 使用 `NODE-*`；`node_type` 只能是 `state`、`event`、`decision`、`outcome`。
- 每个作为出边源的节点都必须有非空 `trigger_conditions`、`early_signals`、`reverse_signals`、`stop_conditions`。
- `path_edges[]` 的 `edge_id` 使用 `EDGE-*`；每条边写已存在的 `from_node_id`、`to_node_id`、非空且有效的 `mechanism_ids`、`condition`、`outcome_writeback`。
- 图必须无环、无孤立节点，并至少有一条分支边。路径是条件图，不是确定预言或故事续写。
- `forecast_conditions` 写出所有预测升格条件；`choice_boundary` 写出哪些比较可由分析完成、哪些必须由授权主体选择。

## 封存前检查

先过 schema，再执行 `validate_claim_path_saturation()`。确认中心循环、默认三个竞争机制、所有分叉信号、停止点、写回接口和 DAG 闭包均通过后，才登记 P5 输出散列。
