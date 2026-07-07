---
name: crossframe-max
description: "Use when the user explicitly invokes crossframe-max, /crossframe-max, $crossframe-max, maximum CrossFrame mode, exhaustive structural projection, full-scale world-model interpretation, no word-limit complete explanation, or v6 meta-runtime design review for skills, prompts, agents, tools, templates, scripts, and runtime protocols. explicit-only."
disable-model-invocation: true
---

# CrossFrame Max

`crossframe-max` 是 CrossFrame v6 世界观前置的 meta-runtime。它不是超长回答模板，也不是省略式诊断模板；它先让 AI 拥有用户预先设计的世界观，再把对象当作局部世界建模，在材料、工具、上下文和行动边界内完成最大推演、校准回合、举证推理、反向证据、产物交付和续写索引。

## max-clean-runtime-entry

运行入口保持正向、精简，并优先服务前台生成稳定性。`SKILL.md` 只放触发边界、运行档位、运行时必读顺序、交付闸门和维护态校验入口。失败样本和反例压力测试放在 `evals/`；长细则放在 `protocols/`、`templates/` 和脚本。

普通 `/crossframe-max` 运行不得在启动阶段预读 repair loop、validator schema、contract map 或维护脚本；这些只在 artifact validation、repository maintenance、显式 repair 或 validator 已实际失败后进入。

## 触发边界

这是 explicit-only skill。只有用户明确要求 `crossframe-max`、最大尺度、穷尽推演、完整解释、无限制长文、全尺度世界观解释，或明确要求用 v6 meta-runtime 审查 skill、prompt、agent、工具、模板、脚本、运行协议时使用。

## 运行档位

- `max-runtime-answer`：普通 `/crossframe-max` 默认档位。目标是材料边界内的最大连续解释、source frontier、反向推演、撤回条件和续写索引；不得因为任务庞大、单轮输出压力、3273 段尚未全部读取、validator 未运行而自动缩短成摘要。该档位不得宣称 `max-complete`。
- `max-complete`：用户显式要求完整 artifact run，且环境支持完整文件写入、full-source exhaustive pass、阶段锁、artifact-first、template-fidelity、longform-dominance、route-ledger gate 和 validator。只有全部满足后才可宣称完成。
- `max-design-review`：用于 skill、prompt、agent、工具、模板、脚本和运行时设计。必须使用 `skill_design` route，登记 `route_key`、route concepts、design decision、v6 rule、反向证据、撤回条件和行动上限；不得伪称完整 max 长文完成。
- `max-incomplete/progress`：只在必需文件不可访问、工具权限缺失、用户中止、外部事实检索连续失败且核心结论完全依赖该事实，或显式 artifact-validation 模式下 validator 已实际失败时使用。任务大、上下文长、需要多轮读取、写作长度高、未运行 validator，不构成自动 incomplete 理由。

## 世界观层先行

第一动作是建立 `max-worldview-capsule`。先加载 v6 世界观运行协议和本轮相关源库线索，再进入局部世界建模、概念命中、证据审计、路径推演和正文生成。

执行时必须把对象当作一个局部世界来对待：

- 先做局部世界建模，再做判断。
- 先识别运行规律，再定位问题。
- 先查 registry 再读相关 full-source。
- `max-complete` 和 artifact run 保持先查 registry 再读 full-source；普通 runtime 可以先读相关 full-source，但必须登记 source frontier。
- 先完成举证链、推理链、反向证据和证据-推理-反例-降档循环，再进入最终表达。
- 先保留撤回条件、行动上限和不可穷尽声明，再写完整长文或设计审查结论。

## 运行时必读顺序

普通 `max-runtime-answer` 的启动顺序：

1. `protocols/max-worldview-protocol.md`
2. `references/source_manifest.json`
3. `references/v6-route-map.yaml`
4. `references/concept-registry/index.md`
5. `references/concept-contracts/v6-core-contracts.md`
6. `references/retrieval-trigger-policy.md`
7. `references/v6-full-source/00-index.md`
8. `references/v6-full-source/00-heading-index.md`
9. `references/v6-full-source/00-term-index.md`
10. `references/v6-full-source/00-table-index.md`
11. route 指定的 v6 full-source 分层文件与必要 `tables/`
12. `templates/` 中本轮产物对应 contract

维护态 / 显式校验态才读取：

- `protocols/max-repair-loop-protocol.md`
- `references/concept-contracts/v6-contract-map.json`
- `schemas/max-validator-report.schema.json`
- `schemas/max-repair-plan.schema.json`
- `scripts/` 中对应 validator 和 repair planner

校验失败后的 repair loop 必须生成或读取 `max-validator-report.json` 与 `max-repair-plan.json`，并登记 `affected_phase`、`downstream_reset`、`repair_action`；普通 runtime 不预读这些维护态材料。

任务路由以 `references/v6-route-map.yaml` 为准。route map 决定阶段读取顺序，不能降低 `max-complete` 的 full-source exhaustive pass 要求；但普通 `max-runtime-answer` 允许先以 source frontier、read status 和 continuation plan 输出完整解释，不得把未达 `max-complete` 误写为完成。

## 阶段锁

完整 artifact run 必须依次冻结：

- `max-run-contract.json`
- `max-read-plan.json`
- `max-source-snapshot.json`
- `max-worldview-capsule.locked.md`
- `max-local-world-model.locked.md`
- `max-claim-board.json`
- `max-audit-board.json`
- `max-output-plan.locked.md`

没有 `max-output-plan.locked.md`，不得生成 `max-essay.md`；也不得宣称完整 artifact run 或 `max-complete`。普通 `max-runtime-answer` 若环境不能写入这些文件，必须在回答中保留相同状态链的可见结构，不得因此缩短为短答或只输出 incomplete。

后续阶段不得直接改写前序冻结产物；异常登记为 `phase_exception_record`，并按 `affected phase reset` 回到受影响阶段。validator failure 只在显式 validation / repair 模式触发 repair loop；普通 runtime 不因预判 validator 难以通过而提前放弃生成。

## 必建模块

完整运行必须生成并互相回指：

- `max-worldview-capsule`
- `max-local-world-model`
- `max-concept-graph`
- `max-scale-map`
- `max-source-frontier`
- `max-position-matrix`
- `max-path-tree`
- `max-path-confidence-layers`
- `max-evidence-reasoning-audit`
- `max-red-team-pass`
- `max-transcendence-window`
- `max-unexhaustible-declaration`
- `max-output-layers`
- `max-continuation-ledger` / `max-run-state`
- `max-continuation-index`
- `max-dossier`
- `max-essay`

## 结构化台账

`max-complete` artifact run 的最终产物必须生成：

- `max-read-ledger.json`
- `max-claim-ledger.json`
- `max-concept-hit-ledger.json`
- `max-evidence-reasoning-audit.json`

普通 `max-runtime-answer` 如果不能真实创建 JSON 台账，必须用可见 `max-source-frontier` 和 `max-continuation-ledger` 登记：已读文件、已读 range、未读文件、需要补证处、claim_id、source_anchor、反向证据状态和撤回条件。不得伪造 JSON 文件、不得自报读取百分比。

`max-read-plan.json` 必须登记 `route_key`、`route_map_version`、`route_required_layers`、`route_required_concepts`、`route_required_outputs`、`route_forbidden_outputs_checked`。`skill_design` route 的设计判断必须登记 `design_decision_id`、`v6_rule_ids`、`action_limit`、`source_anchor`、`counterevidence`、`withdrawal_condition`。

Markdown 章节不能替代 JSON 台账。source paragraph id 必须存在于 v6 full-source；route concepts 必须来自 concept registry；强判断、设计建议和行动路径必须有反向证据、降档条件、撤回条件和行动上限。

## 资料前沿

涉及真实机构、公共事实、历史事件、法律政策、平台规则、技术标准、人物、公司或最新情况时，主动检索与反向检索并行。运行时读取 `references/retrieval-trigger-policy.md`，区分内部概念检索和外部事实检索。资料穷尽不等于现实穷尽，不能假装穷尽现实真相。

外部检索失败不得自动使整轮 `crossframe-max` 失败。它只影响依赖外部事实的 claim 强度；结构解释、路径推演、思想谱系、概念比较可以继续输出，但必须标注事实缺口、降档条件和后续补证入口。

## 读取百分比规则

没有真实 `max-read-ledger.json` 时，不得输出“已读 20% / 500 段 / 12 段范围”这类估算百分比。只能写：

- 已读取的文件 / range / anchor；
- 未读取的文件 / range；
- 哪些 claim 依赖未读材料；
- 下一步读取顺序。

## 产物优先硬闸

`max-complete` 和显式 artifact run 先写入产物目录，再给聊天索引。最低产物：

- `max-artifact-manifest.md`
- `max-dossier.md`
- `max-essay.md`
- `max-continuation-ledger.md`
- `max-continuation-index.md`
- 全部阶段锁文件
- 全部结构化台账

`max-artifact-manifest.md` 必须最后生成；若后续又生成、修改或失败任何 artifact，必须重写 manifest。Manifest status 必须反映最终文件状态，不得写计划状态。

文件写入不可用时，普通 `max-runtime-answer` 可以在聊天中输出完整长文式回答和 continuation index，但必须明确“未创建 artifact directory；不是 max-complete”。不得把短答当作 artifact 代替。

## 模板与校验

运行时执行：

- `artifact-first gate`（仅 artifact run 强制）
- `template-fidelity gate`
- `longform-dominance gate`
- `route-ledger gate`

正文完整性按三档判断：

- 最低通过：`max-essay` 可见字符数至少达到 `max-dossier` 的 1.6 倍。
- 强完成：`max-essay` 至少达到 2.2 倍，并把主要路径写入连续解释。
- 最大完成：`max-essay` 至少达到 3.0 倍，或剩余内容只属于非阻断续写分支。

显式 artifact validation / repository maintenance 时运行：

```bash
python scripts/check_crossframe_max_artifacts.py --workspace <artifact-dir>
python scripts/build_crossframe_max_repair_plan.py --workspace <artifact-dir> --write-report --write-repair-plan
```

源库维护或发布前运行：

```bash
python scripts/check_crossframe_max_v6_full_source.py --repo <repo> --source-docx <v6-docx> --allow-source-path-mismatch
python scripts/check_crossframe_max_v6_registry_anchors.py --repo <repo>
python scripts/check_crossframe_max_route_ledgers.py --workspace <artifact-dir>
python scripts/validate_crossframe_max_route_ledger_fixtures.py
python scripts/validate_crossframe_max_repair_fixtures.py
```

## 前台输出卫生

最终用户可见回答不得包含：

- `### Reasoning`
- `Tool:` / `Args:` / `read_file` / `write_file` / `bash` 调用日志
- 内部路径试错、执行流水、自我提示词
- “我先读某文件”“Let me...” 形式的内部运行自述

最终聊天回复只承担交付索引、核心结论、状态声明、可继续讨论分支和必要的 source frontier。
