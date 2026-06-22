# Inquiry State / 追问状态

| 字段 | 内容 |
| --- | --- |
| post_completion_inquiry_armed | true / false |
| upstream_task | 原任务 |
| upstream_output | diagnosis / essay / review / history / public / org / other |
| 上游上下文索引 | claim ledger / mechanism_candidates / source ledger / concept_contracts / insight dossier / article body / review warning |
| sibling_knowledge_retrieval | none / needed / completed / route_back_to_suite |
| knowledge_sources | skill_id + file_path |
| retrieval_log | 已记录 / 不需要 / 需补充 |
| current_user_input_role | 完成态后续输入 / 显式追问 / 反对结论 / 迁移请求 / 行动边界 / 收束 / 新任务退出 |
| user_goal_now | 继续理解 / 反驳 / 迁移 / 行动 / 补证 / 教学 / 收束 |
| selected_claims | CL / claim_id |
| selected_mechanisms | M / mechanism_id |
| selected_concepts | C |
| review_warnings | R |
| evidence_gaps | S |
| risk_level | low / normal / vulnerable / high-stakes |
| inquiry_mode | clarify / counterexample / evidence / transfer / self-position / action-boundary / concept-fidelity |
| max_questions | 3 / 5 |
| stop_condition | 用户要求停止 / 两轮已满 / 进入行动风险 / 需要 review |
