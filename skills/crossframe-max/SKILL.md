---
name: crossframe-max
description: "Use when the user explicitly invokes crossframe-max, /crossframe-max, $crossframe-max, maximum CrossFrame mode, exhaustive structural projection, full-scale world-model interpretation, no word-limit complete explanation, or v6 meta-runtime design review for skills, prompts, agents, tools, templates, scripts, and runtime protocols. explicit-only."
disable-model-invocation: true
---

# CrossFrame Max

`crossframe-max` 是 CrossFrame v6 世界观前置的 meta-runtime。它不是超长回答模板，也不是省略式诊断模板；它先让 AI 拥有用户预先设计的世界观，再把对象当作局部世界建模，在材料、工具、上下文和行动边界内完成最大推演、校准回合、举证推理、反向证据、产物交付和续写索引。

## max-clean-runtime-entry

运行入口保持正向、精简：`SKILL.md` 只放触发边界、运行档位、必读顺序、交付闸门和校验命令。失败样本和反例压力测试放在 `evals/`；长细则放在 `protocols/`、`templates/` 和脚本。

**默认目标不是聊天短答，也不是先判定自己做不到。默认目标是 `max-artifact-run`：先创建产物目录，先生成阶段文件、dossier、essay、continuation 和 manifest，再登记未满足项。**

## 触发边界

这是 explicit-only skill。只有用户明确要求 `crossframe-max`、最大尺度、穷尽推演、完整解释、无限制长文、全尺度世界观解释，或明确要求用 v6 meta-runtime 审查 skill、prompt、agent、工具、模板、脚本、运行协议时使用。

## 运行档位

- `max-artifact-run`：普通 `/crossframe-max` 默认档位。必须尽力创建独立产物目录和最小产物集，写出 `max-dossier.md`、`max-essay.md`、`max-continuation-ledger.md`、`max-continuation-index.md` 和 `max-artifact-manifest.md`。如果 full-source、结构化台账或 validator 未满足，产物状态写为 `max-artifact-incomplete:*`，但不得因此省略长文或只输出读态。
- `max-complete`：完整 full-source exhaustive pass、阶段锁、artifact-first、template-fidelity、longform-dominance、route-ledger gate 和 validator 全部满足后才可宣称完成。
- `max-design-review`：用于 skill、prompt、agent、工具、模板、脚本和运行时设计。必须使用 `skill_design` route，登记 `route_key`、route concepts、design decision、v6 rule、反向证据、撤回条件和行动上限；不得伪称完整 max 长文完成。
- `max-blocked/progress`：只有文件系统不可写、必需材料不可访问、用户明确中止、工具权限缺失，或安全/政策边界阻断时使用。任务庞大、3273/3273 未完成、validator 未通过、外部检索不完整，不是只输出 `max-incomplete` 的理由；这些只阻断 `max-complete` 声明。

## 世界观层先行

第一动作是建立 `max-worldview-capsule`。先加载 v6 全量分层源库作为本轮预先设计的世界观，再进入局部世界建模、概念命中、证据审计、路径推演和正文生成。

执行时必须把对象当作一个局部世界来对待：

- 先做局部世界建模，再做判断。
- 先识别运行规律，再定位问题。
- 先查 registry 再读 full-source。
- 先完成举证链、推理链、反向证据和证据-推理-反例-降档循环，再进入最终表达。
- 先保留撤回条件、行动上限和不可穷尽声明，再写完整长文或设计审查结论。

## 必读顺序

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
11. route 指定的 v6 full-source 分层文件与 `tables/`
12. `templates/` 中本轮产物对应 contract
13. `scripts/` 中对应 validator

任务路由以 `references/v6-route-map.yaml` 为准。route map 决定阶段读取顺序，不能降低 `max-complete` 的 full-source exhaustive pass 要求。概念注册表只做定位、别名、邻域和触发，不替代 full-source。

## 阶段锁

`max-artifact-run` 必须尽力依次生成或登记：

- `max-run-contract.json`
- `max-read-plan.json`
- `max-source-snapshot.json`
- `max-worldview-capsule.locked.md`
- `max-local-world-model.locked.md`
- `max-claim-board.json`
- `max-audit-board.json`
- `max-output-plan.locked.md`

没有 `max-output-plan.locked.md`，不得宣称 `max-complete`。但如果模型能够写入文件，必须先生成一个最小 output plan，再写 `max-essay.md`；不得把“没有 output plan”作为停止写长文的理由。后续阶段不得直接改写前序冻结产物；异常登记为 `phase_exception_record`，并按 `affected phase reset` 回到受影响阶段。

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

`max-complete` 最终产物必须生成：

- `max-read-ledger.json`
- `max-claim-ledger.json`
- `max-concept-hit-ledger.json`
- `max-evidence-reasoning-audit.json`

普通 `max-artifact-run` 若无法在本轮填满四个 JSON 台账，必须先生成可读的 `max-dossier.md` 和 `max-essay.md`，并在 `max-artifact-manifest.md` 中登记缺口。JSON 台账缺失不允许被伪造为通过，也不允许阻断长文产物。

`max-read-plan.json` 必须登记 `route_key`、`route_map_version`、`route_required_layers`、`route_required_concepts`、`route_required_outputs`、`route_forbidden_outputs_checked`。`skill_design` route 的设计判断必须登记 `design_decision_id`、`v6_rule_ids`、`action_limit`、`source_anchor`、`counterevidence`、`withdrawal_condition`。

Markdown 章节不能替代 JSON 台账。source paragraph id 必须存在于 v6 full-source；route concepts 必须来自 concept registry；强判断、设计建议和行动路径必须有反向证据、降档条件、撤回条件和行动上限。

## 资料前沿

涉及真实机构、公共事实、历史事件、法律政策、平台规则、技术标准、人物、公司或最新情况时，主动检索与反向检索并行。运行时读取 `references/retrieval-trigger-policy.md`，区分内部概念检索和外部事实检索。资料穷尽不等于现实穷尽，不能假装穷尽现实真相。

外部检索失败只影响依赖外部事实的 claim 强度。它必须写入 `max-source-frontier` 和 `max-evidence-reasoning-audit`，但不得自动取消 `max-dossier.md` 或 `max-essay.md` 的生成。

## 产物优先硬闸

完整输出先写入产物目录，再给聊天索引。最低产物：

- `max-artifact-manifest.md`
- `max-dossier.md`
- `max-essay.md`
- `max-continuation-ledger.md`
- `max-continuation-index.md`
- 全部可生成的阶段锁文件
- 全部可生成的结构化台账或缺口登记

文件必须分开交付；完整文章必须单独放在 `max-essay.md`。最终聊天回复只承担交付索引和继续讨论入口功能，并列出可继续讨论的分支。

`max-artifact-manifest.md` 必须最后生成。若后续生成或修改了任何 artifact，必须重写 manifest，使其反映最终文件状态，而不是计划状态。

## 模板与校验

执行：

- `artifact-first gate`
- `template-fidelity gate`
- `longform-dominance gate`
- `route-ledger gate`

正文完整性按三档判断：

- 最低通过：`max-essay` 可见字符数至少达到 `max-dossier` 的 1.6 倍。
- 强完成：`max-essay` 至少达到 2.2 倍，并把主要路径写入连续解释。
- 最大完成：`max-essay` 至少达到 3.0 倍，或剩余内容只属于非阻断续写分支。

交付后运行 validator。validator 失败时，状态为 `max-artifact-incomplete: validation-failed`，不得把失败写成通过；但已经生成的 dossier / essay / continuation 仍然是本轮交付对象。

```bash
python scripts/check_crossframe_max_artifacts.py --workspace <artifact-dir>
```

源库维护或发布前运行：

```bash
python scripts/check_crossframe_max_v6_full_source.py --repo <repo> --source-docx <v6-docx> --allow-source-path-mismatch
python scripts/check_crossframe_max_v6_registry_anchors.py --repo <repo>
python scripts/check_crossframe_max_route_ledgers.py --workspace <artifact-dir>
python scripts/validate_crossframe_max_route_ledger_fixtures.py
```

## 前台输出卫生

最终用户可见回复不得包含 `### Reasoning`、`Tool:`、`Args:`、`read_file`、`write_file`、`bash` 或内部路径试错。调试日志可以存在于独立 transcript，但 final chat 只输出产物索引、运行状态、核心结论摘要和续写入口。

未完成全量读取、route-ledger、举证推理、阶段锁或 artifact validation 时，不得宣称 `max-complete`；应输出 `max-artifact-incomplete:*` 与完整产物索引，而不是停止产物生成。