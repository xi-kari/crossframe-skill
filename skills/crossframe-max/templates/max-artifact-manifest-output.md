# max-artifact-manifest

- run_id：run-001
- delivery_label：pending-validator
- phase-lock gate：recorded
- phase artifacts：see inventory
- artifact-first gate：satisfied
- 产物目录：current workspace
- 生成时间：ISO-8601
- 输入摘要：
- 读态摘要：
- 校验状态：not_run
- 下一轮入口：max-continuation-index.md
- control-plane sidecars：max-run-contract.json、max-validator-report.json、max-repair-plan.json 不进入 analysis artifact inventory。

```manifest-contract
{
  "manifest_version": "v2",
  "run_id": "run-001",
  "artifacts": [
    {
      "path": "max-dossier.md",
      "sha256": "0000000000000000000000000000000000000000000000000000000000000000"
    },
    {
      "path": "max-essay.md",
      "sha256": "0000000000000000000000000000000000000000000000000000000000000000"
    },
    {
      "path": "max-continuation-ledger.md",
      "sha256": "0000000000000000000000000000000000000000000000000000000000000000"
    },
    {
      "path": "max-continuation-index.md",
      "sha256": "0000000000000000000000000000000000000000000000000000000000000000"
    }
  ]
}
```
