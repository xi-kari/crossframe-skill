# Knowledge Retrieval Log / 知识库检索日志

本日志只记录 `crossframe-inquiry` 为了生成追问而定向读取的 sibling skill 内容。检索材料不能直接升级为新结论。

| 字段 | 内容 |
| --- | --- |
| retrieval_goal | 本轮为什么需要知识库检索 |
| user_input_anchor | 用户本轮输入 |
| upstream_anchor | 上一轮 claim_id / mechanism_id / review warning |
| knowledge_sources | skill_id + file_path |
| retrieved_boundary | 检索材料提供了什么边界 |
| question_use | 这些材料会用于哪些 q_id |
| cannot_prove | 检索材料不能证明什么 |
| route_back_condition | 何时必须回到 suite / sibling skill |

## retrieval_log

| skill_id | file_path | why_read | used_for_q_id | cannot_prove |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## 输出约束

- 只能用检索材料收紧问题、补边界、识别迁移条件或反证方向。
- 不得把 sibling skill 的规则当作已经完成的专项判断。
- 若需要组织修复、公共事实判断、历史史料判断、完整 review 或新文章，回到 suite。
