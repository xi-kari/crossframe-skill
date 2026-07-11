# max-repair-plan

## 触发条件

仅当 validator failed 时生成。

## 必须字段

```json
{
  "repair_plan_version": "v2",
  "workspace": "",
  "validation_attempt": 1,
  "retry_count": 0,
  "final_output_allowed": false,
  "max_retry_count": 2,
  "errors": [],
  "affected_phases": [],
  "must_regenerate": [],
  "must_not_patch_only": [],
  "repair_actions": [],
  "downgrade_required": [],
  "withdraw_required": [],
  "external_search_required": false,
  "repository_maintenance_required": false,
  "artifact_incomplete_if_unresolved": true
}
```

## 输出原则

- repair plan 是控制文件，不是文章。
- repair plan 不得把缺证据改写成强判断。
- repair plan 必须说明哪些文件可以重建，哪些文件不能只 patch。
- strict-only 缺口使用 `mark_artifact_incomplete`；修复分析产物前把 run contract 重置为 `not_run`，重写 manifest 后再校验。
