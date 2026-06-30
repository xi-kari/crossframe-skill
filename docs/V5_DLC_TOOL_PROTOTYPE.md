# v5.0 半量化 DLC 工具原型说明

v5.0 半量化 DLC 工具原型是一组 Markdown 模板、JSON schema、fixtures、校验脚本和发布 bundle 脚本。它用于整理结构判断和暴露风险，不用于自动判断现实。

## 包含内容

| 类型 | 文件 |
| --- | --- |
| 构念图谱 | `skills/crossframe/references/construct-map-v5-dlc.md` |
| 七闸半量化 | `skills/crossframe/worksheets/seven-gates-quant-rubric.md` 与 `skills/crossframe/schemas/seven-gates-quant.schema.json` |
| 证据台账 | `skills/crossframe/worksheets/evidence-ledger-v5-dlc.md` 与 `skills/crossframe/schemas/evidence-ledger-v5-dlc.schema.json` |
| 校准锚点 | `skills/crossframe/worksheets/calibration-anchor-card.md` 与 `skills/crossframe/schemas/calibration-anchor.schema.json` |
| 机制更新 | `skills/crossframe/worksheets/mechanism-update-rules.md` 与 `skills/crossframe/schemas/mechanism-update.schema.json` |
| 反例登记 | `skills/crossframe/worksheets/counterexample-register.md` 与 `skills/crossframe/schemas/counterexample-register.schema.json` |
| 案例库验证 | `skills/crossframe-casebook/examples/v5-dlc-quant-trials/` |
| 发布源稿 | `docs/CROSSFRAME_V5_DLC.md` |
| 构建脚本 | `scripts/build_v5_dlc_publication_bundle.py` |
| DOCX 导出 | `scripts/build_v5_dlc_docx.py` |
| 发布检查 | `scripts/check_v5_dlc_publication_bundle.py` |
| 审计 manifest | 发布 bundle manifest 会记录文档源、工具脚本、v5 DLC validators 和 schema 的 SHA256 |

## 常用命令

```powershell
$env:PYTHONPATH='work/pydeps'; python scripts/validate_v5_dlc_quantification_schema_fixtures.py --repo .
python scripts/check_v5_dlc_casebook_trials.py --repo .
python scripts/check_v5_dlc_publication_bundle.py --repo .
python scripts/build_v5_dlc_publication_bundle.py --repo .
python scripts/build_v5_dlc_docx.py --repo .
```

## 输入

- 脱敏材料边界。
- 来源台账和证据台账。
- 七闸状态和锚点评分。
- 机制候选与反向条件。
- 反例登记与评分者分歧。
- 需要发布或内部使用的文本草案。

## 输出

- 结构剖面。
- 缺证清单。
- 强制降档原因。
- 行动上限。
- 撤回条件。
- 版本写回建议。
- 发布 bundle 和 manifest。
- 可发布 DOCX 文档。

## 禁止用途

- 不得把工具输出作为完整诊断。
- 不得把 checker 通过作为现实正确性证明。
- 不得把半量化结果作为处置依据。
- 不得把内部试跑包装成认证、营销材料或“已经证明安全”。
- 不得把无法提交反例解释为没有反例。

## Smoke Test 期望

一次合格 smoke test 至少证明：

- schema fixtures 能发现缺撤回条件、缺行动上限、强判断缺来源台账、低成本证据越界和总分字段。
- casebook checker 能发现缺领域覆盖、缺分歧记录、缺降档写回和证明性语言。
- publication checker 能发现缺章节、缺工具边界、缺 manifest、未受控的总分/预测/认证/处置语言。
- publication manifest 能核对发布文档源、工具脚本、validator 和 schema 是否与当前仓库一致。
- DOCX 导出能从受控 Markdown 源生成可视觉复核的发布文档。

本工具只帮助整理结构判断，不替代现实调查、专业判断、受影响位置反馈、外部复核和最终责任承担。分数只能触发降级、复核或补证，不能单独授权处置。
