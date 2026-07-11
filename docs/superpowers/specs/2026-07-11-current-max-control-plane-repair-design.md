# CrossFrame Max 现有控制平面修复设计

日期：2026-07-11

状态：设计方向及书面规格已获用户批准，进入实施计划

基线：`origin/main@e384c75cb8d657e6984f8506e658db8418fc08bb`

## 1. 背景

当前 `main` 的 CrossFrame Max 已把普通运行改为产物优先的 `max-artifact-run`，并把真正阻断态改名为 `max-blocked/progress`。但 README、phase 模板、完整性检查、repair 协议和部分 fixture 仍保留旧三档状态及 `max-incomplete/progress`。仓库完整性检查因此在第一步失败，GitHub Actions 后续检查全部跳过。

更深的问题是：运行目标、执行状态、产物完整度和校验结果被压在同一个 complete/incomplete 标签上。严格门禁会阻断正常产物生成；放松门禁又会让不完整产物缺少可验证的诚实状态。本次维护只解决现有 v6 runtime 的控制平面一致性，不引入 v7 理论内容。

## 2. 目标

本次维护完成后，现有 CrossFrame Max 应满足：

1. SKILL、agent prompt、协议、模板、validator、fixture、README、Quickstart、Changelog 和 CI 使用同一套运行状态合同。
2. `max-artifact-run` 可以交付诚实标记的不完整产物，但不能伪称 `max-complete`。
3. `max-complete` 继续保留 3273/3273、四类结构化台账、route closure、artifact-first、template fidelity 和 longform dominance 等严格要求。
4. canonical 模板生成的合法产物能够通过对应 validator。
5. marker-only、假 final、缺证据、状态冲突和 forbidden-output 绕过样例必须失败。
6. GitHub `main` 恢复绿色，并以 required checks 阻止失败提交再次直接合入。

## 3. 非目标

本轮明确不做：

- 不接入《跨尺度结构解释框架 v7.0》。
- 不修改 v6 full-source、3273 段、60 表、route map 或概念体系。
- 不重构安装器、发布包、Release 版本模型或本地 skill 安装副本。
- 不解决全部 skill-family 路由问题。
- 不重写 CrossFrame Max 正文风格或理论立场。
- 不删除历史分支或用户未明确授权删除的 worktree。

## 4. 设计原则

### 4.1 状态必须正交

一次 Max 运行至少区分四个维度：

| 维度 | 合法值 | 作用 |
| --- | --- | --- |
| `run_mode` | `max-artifact-run`、`max-complete`、`max-design-review`、`max-blocked/progress` | 说明本轮目标档位 |
| `execution_state` | `pending`、`running`、`blocked`、`finished` | 说明执行是否真正被阻断 |
| `artifact_state` | `absent`、`partial`、`core_complete`、`strict_complete` | 说明产物集合完整度 |
| `validation_state` | `not_run`、`failed`、`passed` | 说明 validator 结果 |

`max-artifact-incomplete:<reason>` 是由产物和严格门禁缺口推导出的交付标签，不再充当独立运行档位。`max-blocked/progress` 只在文件系统不可写、必需材料不可访问、权限或安全边界阻断、用户中止等真实阻断条件下使用。

### 4.2 完成声明必须由机器状态推导

- 只有 `run_mode=max-complete`、`execution_state=finished`、`artifact_state=strict_complete`、`validation_state=passed` 同时成立，才能输出 `max-complete`。
- `core_complete` 但严格条件未满足时，只能输出 `max-artifact-incomplete:<reason>`。
- `validation_state=failed` 不撤销已生成产物，但必须阻断 `max-complete` 声明。
- 任意 artifact、manifest、run contract 和 validator report 状态不一致时，validator 必须失败。

## 5. 机器合同

新增 `max-run-contract` JSON Schema，作为运行状态枚举和字段要求的唯一机器真源。文档、模板和完整性检查不得各自维护另一套状态列表。

最小字段包括：

- `contract_version`
- `run_id`
- `run_mode`
- `execution_state`
- `artifact_state`
- `validation_state`
- `target_profile`
- `incomplete_reasons`
- `blocked_reason`
- `final_output_allowed`

约束：

- `blocked_reason` 只允许在 `execution_state=blocked` 时非空。
- `incomplete_reasons` 在 `artifact_state` 不是 `strict_complete` 时必须显式登记。
- `final_output_allowed=true` 只表示允许交付当前状态产物，不等于允许宣称 `max-complete`。
- 旧 `max-incomplete/progress` 不再是合法值。

## 6. Validator 分层

### 6.1 Artifact-run profile

用于 `max-artifact-run`，检查：

- 五个核心 Markdown 产物存在且相互回指：manifest、dossier、essay、continuation ledger、continuation index。
- phase 文件能生成的均已生成；无法生成的有结构化缺口记录。
- manifest 反映实际文件，而不是计划文件。
- dossier 和 essay 符合 canonical 模板的核心章节合同。
- claim、source、route 与输出状态没有自相矛盾。
- 未满足 strict gate 时存在明确的 `incomplete_reasons`。
- 没有 `max-complete`、`3273/3273 satisfied` 或 validator passed 的虚假声明。

Artifact-run profile 不要求伪造四类 JSON 台账，也不把严格条件缺失误判为“整个产物无效”。

### 6.2 Complete profile

在 artifact-run profile 之上继续要求：

- full-source exhaustive pass 为真实 `3273/3273`。
- 四类结构化台账完整且通过交叉验证。
- phase lock、route-ledger、concept-contract、source-anchor 与 repair 状态全部闭合。
- artifact-first、template-fidelity 和 longform-dominance 全部通过。
- validator 执行结果为 passed，并在成功计算后写出 report；report 不是 validator 自身的前置输入。

### 6.3 Design-review 与 blocked

- `max-design-review` 复用 artifact-run 的状态一致性检查，并额外执行 `skill_design` route 的 design decision、v6 rule、反向证据、撤回条件和行动上限要求；不得映射成 `max-complete`。
- `max-blocked/progress` 只验证阻断原因、已完成读态、禁止性完成声明和下一步恢复入口，不要求生成完整长文产物。

## 7. 模板与来源一致性

1. 修复 `max-dossier-output.md`，使 continuation index 等 validator 必需章节真实存在。
2. `max-phase-lock-output.md` 使用机器合同中的四档状态和正交字段。
3. validator 的必需标题必须由模板合同生成或接受模板一致性测试，不再与模板手工维护两套列表。
4. README、Quickstart、Changelog、SKILL、agent prompt、worldview protocol 与 repair protocol 使用同一术语。
5. canonical `skills/crossframe-max` 修改后，通过同步脚本更新 `.claude` 镜像；不得直接手工形成两套权威源。
6. 根脚本与 skill 内同名脚本必须增加内容一致性检查，避免 CI 与安装后 runtime 执行不同实现。

产物生命周期固定为：先生成分析产物，再生成覆盖这些分析产物的 manifest，随后由 validator 读取 manifest 并写出独立的 validator report。Validator report 不属于 manifest 的被校验分析产物集合，因此不会形成“manifest 必须包含尚未生成的 report”的循环。若 repair 修改任何分析产物，必须重新生成 manifest，并重新运行 validator；旧 report 自动失效。

## 8. Fixture 与自动测试

新增真正的 Python 单元测试层，继续保留现有脚本型集成检查。

### 8.1 Gold fixtures

- 一个最小但语义闭合的 `max-artifact-run` fixture。
- 一个满足全部严格条件的 `max-complete` fixture。
- fixture 从 canonical 模板和 schema 构造，不复制 validator 内部 marker 常量。

### 8.2 Adversarial fixtures

至少覆盖：

- 旧状态名 `max-incomplete/progress`。
- `final_output_allowed=false` 却宣称 complete。
- `needs_evidence=true` 的 claim 预先进入 final。
- marker-only dossier/essay。
- 缺失 canonical 标题。
- `present=false` 掩盖 forbidden output。
- artifact manifest 与真实文件不一致。
- artifact-run 与 complete profile 混写。
- validator failed 却宣称 passed。
- duplicate claim/source ID 和失配回指。

### 8.3 回归要求

- 现有完整性检查、source continuity、v6 full-source、registry anchors、route fixtures、repair fixtures、mirror sync 和 package smoke 均继续通过。
- 新测试先复现当前失败，再由实现修复。
- 测试不得只验证字符串存在；状态转换和跨文件一致性必须由结构化断言验证。

## 9. CI 设计

把单一串行 verify job 拆为可独立观察的稳定检查：

1. `repository-integrity`
2. `max-contracts-and-artifacts`
3. `schemas-and-fixtures`
4. `mirrors-and-package`

每个 job 独立运行；一个失败不应让其它门禁状态变成 unknown。Python 语法、PowerShell/Bash 语法和 JSON Schema 解析归入相应 job。

GitHub `main` 恢复绿色后启用保护：

- 合并必须经过 PR。
- 上述 required checks 必须全部通过。
- 禁止 force push 和 branch deletion。
- 保护规则启用前先验证检查名称稳定，避免把仓库锁死。

## 10. 错误处理

- Schema 或状态冲突：直接失败，报告精确字段和涉及文件。
- Artifact-run 缺严格材料：通过 artifact-run profile，但输出明确 incomplete reasons；complete profile 必须失败。
- 核心 artifact 缺失或模板不合格：artifact-run profile 失败。
- Validator 失败后：保留已经生成的产物，生成或更新 validator report；repair loop 只重置受影响阶段。
- CI 中任一 job 失败：禁止合并，但保留其它 job 的独立结果供诊断。
- branch protection 配置失败：不强行修改主分支，保留已合并绿色状态并单独报告。

## 11. 交付流程

1. 在隔离 worktree、`codex/repair-current-max-control-plane` 分支工作。
2. 先提交本设计文档并由用户复核。
3. 设计获书面复核后编写实施计划。
4. 实现阶段采用测试先行：先增加失败测试，再做最小修复。
5. 运行全部本地门禁和镜像一致性检查。
6. 提交、推送并创建 PR。
7. 等待 GitHub 全部检查通过；不得在红灯状态下合并。
8. 合并后复验 `main`，再启用 required checks 与分支保护。
9. 原始本地 checkout 和本地安装版 skills 保持不变，除非用户另行授权同步。

## 12. 验收标准

- 本地与 GitHub `main` 的全部规定检查为绿色。
- 完整性脚本不再要求旧 `max-incomplete/progress`。
- 运行状态只由一份机器合同定义。
- canonical 模板可生成通过相应 profile 的 fixture。
- Artifact-run 可以诚实交付不完整结果，但不能通过 complete profile。
- Complete profile 保持原有严格 full-source 和台账闭合要求。
- marker-only 和所有列出的 adversarial fixtures 均失败。
- canonical、Claude 镜像、根脚本和 skill 内脚本不存在实现漂移。
- README、Quickstart、Changelog、SKILL、协议和模板术语一致。
- PR 在全部 required checks 通过前无法合并。
- v7 文件、v7 合同和本地 skill 安装副本没有变化。
