# v5.0 与半量化 DLC 变更说明

半量化 DLC 不替换 v5.0。它把 v5.0 中已经存在的结构判断动作转成可审计的半量化记录方式，用于降档、补证、复核和写回。

| v5.0 连续结构 | 半量化 DLC 新增 | 当前文件 | 误用风险 | 防护 |
| --- | --- | --- | --- | --- |
| 七闸复核 | `pass / weak / fail / blocked` 加 0-4 锚点 | `skills/crossframe/worksheets/seven-gates-quant-rubric.md` | 把分值当成总分 | 分值只能解释闸口状态 |
| 来源、事实、证据分离 | 证据成本、直接性、独立性、可复核性 | `skills/crossframe/worksheets/evidence-ledger-v5-dlc.md` | 低成本材料支撑强判断 | 低成本证据强制降档 |
| 概念契约 | 构念图谱和校准锚点 | `skills/crossframe/references/construct-map-v5-dlc.md` | 新构念反向改写 v5.0 概念 | 构念必须回指 v5 源锚点和工作表 |
| 机制候选 | 局部机制边更新 | `skills/crossframe/worksheets/mechanism-update-rules.md` | 机制概率化或排序化 | 只记录 strengthen/weaken/neutral/pending/withdraw |
| 判断档位 | 判断档位与行动上限矩阵 | `skills/crossframe/references/judgment-action-matrix-v5-dlc.md` | 高分自动授权行动 | 矩阵只降档，不自动升级 |
| 框架治理与证伪 | 反例、撤回、版本写回 | `skills/crossframe/references/falsification-governance-v5-dlc.md` | 把反例当附录 | 反例必须改变文本、工具或边界 |
| 案例库 | 失败发现 trial 与评分者分歧记录 | `skills/crossframe-casebook/examples/v5-dlc-quant-trials/validation-summary.md` | 把覆盖率当有效性证明 | 摘要只报告失败、降档和修订 |
| 工具化边界 | schema、fixtures、checker、publication bundle | `docs/V5_DLC_TOOL_PROTOTYPE.md` | 把工具通过当现实证明 | checker 只证明格式和边界，不证明现实正确 |

## 保留不变的 v5.0 原则

- 先界定对象、事实边界、尺度窗口和材料来源。
- 证据不足时保留机制候选，不急于定性。
- 高风险概念必须通过概念卡、概念契约和源锚点。
- 强判断不能绕过来源台账、命题台账、撤回条件和受影响位置反馈。
- 亲密关系、公共制度、组织处置和高反身性对象必须优先保护低权力位置。
- 框架本身必须接受证伪、降档、退出和良性消亡。

## 半量化 DLC 新增的硬边界

- 分数只能触发降档、补证、复核或写回。
- 案例库只用于失败发现，不能证明框架正确。
- 评分者一致性只说明协议稳定性，不能证明现实判断为真。
- 工具原型不得接入绩效、审核、封禁、处分、资格判断或资源分配系统。
- 发布前必须有 manifest，列明构成文档的源文件和 SHA256。
