---
name: crossframe-promax
description: "Use when the user explicitly names crossframe-promax, CrossFrame ProMax, $crossframe-promax, or /crossframe-promax; never infer activation from generic requests for depth, completeness, maximum effort, or long output."
---

# CrossFrame ProMax

把本 skill 作为 v8-only、artifact-first 的结构推演运行时。先建立可验证工件，再交付完整中文解释；以固定源快照、概念闭包、命题路径、检索台账、反方攻击、立场锁和验证报告约束模型风格差异。不要声称拥有无限算力或已经穷尽现实；只声明验证器能够证明的预算内饱和。

## 激活硬门

- `PROMAX-NAMED-ONLY`：只接受 `crossframe-promax`、`CrossFrame ProMax`、`$crossframe-promax`、`/crossframe-promax` 四种明确点名。
- 路由：泛化的“最大算力”“完整长文”“全尺度”“穷尽分析”等表达不是 ProMax 名称，不得触发 ProMax。
- `PROMAX-PRIORITY-OVER-MAX`：同时点名 ProMax 与 Max 时，ProMax 优先并记录路由冲突已解决。
- `PROMAX-NO-FALLBACK-TO-MAX`：进入 ProMax 后禁止回退到 Max，不得把失败、材料不足或能力缺口改写为回退理由。
- 没有命中四种名称时立即退出本运行时；不要用相似拼写、语义近似或模型判断补足触发。

先运行确定性路由检查，并把用户原始请求作为单一参数安全传入：

```text
python skills/crossframe-promax/scripts/crossframe_promax_runtime.py route --request <原始请求>
```

路由检查失败即不使用本 skill。检查通过后，本次运行不得切换到 brief、快速答复、自选轻量档，也不得加载任何 sibling knowledge。唯一理论知识面是本 skill 随附的 v8 源快照、注册表、合同和路由；外部材料只能校准事实与案例，不能改写 v8 定义。

## 不可绕过的输出边界

- 默认执行 `promax-artifact-run`，不是聊天短答。
- 只有全部严格门通过后才输出 `promax-complete`。
- 只有源不可访问、文件系统不可写、必需工具被禁止、用户中止或更高优先级安全边界阻断时，才使用 `promax-blocked/progress`。
- `promax-artifact-incomplete:<reason>` 只能由验证结果产生，不是模型自选档位。
- `PROMAX-NO-TEST-FIXTURE-RUNTIME`：`crossframe_promax_fixture_factory.py` 与 `tests/fixtures/promax-runtime` 只服务仓库 TDD；真实运行禁止执行、复制、改名或派生其中的测试夹具，`promax-fixture-*` 也不是可交付的生产 run ID。
- 禁止先锁定与用户请求无关的通用冻结工件，再追加主题附录来伪装请求绑定；通用冻结工件 + 主题附录不是同一轮结构推演。
- `PROMAX-NO-EARLY-FINAL`：`init`/`P0` 后禁止给出最终聊天、完成或未完成状态；必须继续推进可执行阶段，不能把“尚未运行验证器”改写成 `promax-artifact-incomplete:validation-failed`。
- `PROMAX-MATERIALIZE-BEFORE-INCOMPLETE`：文件与相应能力可用时，先生成所有可生成的 P1–P10 工件，尤其是完整 P10 长文与控制面，再运行验证器；某项能力缺失只限制依赖该能力的内容，不许可跳过其余可生成工件。
- 材料不足时继续做条件分支、竞争机制、敏感性分析、当前排序和补证设计；降低结论强度，不取消分析。
- 不公开隐藏思维链、英文自我规划、工具试错或逐步私有推理。用事实边界、v8 锚点、概念处置、claim-path、反证、判断理由、撤回条件和验证报告提供可审计性。
- 不用术语数量、篇幅、marker 或概念 ID 堆积冒充理解。每个概念和案例都必须承担可验证的结构作用。

## 必读顺序

开始实质分析前，按顺序完整读取：

1. `protocols/promax-runtime-protocol.md`
2. `protocols/promax-judgment-constitution.md`
3. `protocols/promax-retrieval-red-team-protocol.md`
4. `protocols/promax-repair-loop-protocol.md`
5. `references/source_manifest.json`
6. `references/runtime-routing-map.md`
7. `references/retrieval-policy.md`
8. `references/v8-full-source/00-index.md`
9. `references/v8-full-source/00-heading-index.md`
10. `references/v8-full-source/00-term-index.md`
11. `references/v8-full-source/00-table-index.md`
12. `references/concept-registry/index.md`
13. `references/concept-registry/v8-concept-registry.json`
14. `references/concept-contracts/v8-contract-map.json` 及合同文件
15. `references/v8-route-map.json`

索引只用于定位，不替代正文。route 只决定优先读取与概念闭包起点，不降低全源连续读取要求。不得把运行胶囊、注册表摘要、外部案例或模型常识当作 v8 原文定义。

## 初始化工件运行

创建一个全新的、不覆盖既有目录的 artifact 目录。按实际能力选择参数；用户要求建议或选择时必须加入 `--recommendation-required`。

```text
python skills/crossframe-promax/scripts/crossframe_promax_runtime.py init --repo <仓库根目录> --run-dir <新工件目录> --request <原始请求> --mode promax-artifact-run
```

有网络能力时加入 `--network`；有隔离子代理能力时加入 `--subagents`，并按该 CLI 的 `--help` 设置并发上限。能力不存在时如实登记，不要冒充工具已运行。`init` 负责生成并绑定 `promax-run-contract.json`、`promax-source-snapshot.json` 和初始 `promax-phase-events.jsonl`。

## 固定阶段

严格按 `P0` 至 `P11` 运行，不跳步、不覆盖上游冻结工件：

| 阶段 | 责任 | 冻结或派生工件 |
| --- | --- | --- |
| `P0` | 冻结请求、档位、能力、角色、预算与完成标准 | `promax-run-contract.json`, `promax-source-snapshot.json`, `promax-phase-events.jsonl` |
| `P1` | 验证源、知识图与逐项读取覆盖 | `promax-read-events.jsonl` |
| `P2` | 连续读取全源并形成不替代原文的运行胶囊 | `promax-worldview-capsule.locked.md` |
| `P3` | 冻结对象、行动者、圈层、尺度、双通道、时钟、事件、证据和未知项 | `promax-local-world-model.locked.json` |
| `P4` | 处置全 registry，完成 route 与 neighbor closure | `promax-concept-disposition-ledger.json` |
| `P5` | 建立中心命题、竞争机制、路径 DAG、条件前瞻和选择边界 | `promax-claim-path-graph.json` |
| `P6` | 完成五向真实检索或诚实记录能力缺口 | `promax-retrieval-ledger.json` |
| `P7` | 完成最强反方、误用攻击和正反立场稳定性检查 | `promax-red-team-report.json` |
| `P8` | 在攻击后冻结判断、行动上限和建议排序 | `promax-position.locked.json`, `promax-recommendation.locked.json` |
| `P9` | 把概念、机制、路径、例子、反例和判断映射到章节 | `promax-output-plan.locked.json` |
| `P10` | 先生成完整长文工件，再生成 manifest 与续跑控制面 | dossier、atlas、case/countercase、essay、continuation、manifest |
| `P11` | 运行验证器；失败时只重置最早受影响阶段及下游 | `promax-validator-report.json`，失败时另有 `promax-repair-plan.json` |

每次阶段封存都使用 `promax_runtime.state_machine` 的验证、封存与 append-only 写入函数。不要手工伪造父 hash、事件 hash、reset 事件或完成状态。控制面工件必须服从相应 schema；不要为 run contract、source snapshot、read events、phase events 或 continuation ledger 创造散文替代品。

## 多角色隔离

能力允许时隔离运行五个角色：源与概念审计、外部事实检索、反例攻击、裁决与立场冻结、长文主笔。角色只通过冻结工件交换信息，并按 run contract 的 `role_plan` 登记输入、观测输入、输出和状态。

没有子代理能力时按同一角色顺序执行，登记 `single-agent-separated`，每个角色只读取其冻结输入。不得把单代理顺序执行声称为独立审查；能力允许却无故跳过隔离角色时不得声明严格完成。

## 长文交付硬门

在聊天回复前先生成并交叉绑定：

- `promax-dossier.md`
- `promax-concept-atlas.md`
- `promax-case-and-countercase.md`
- `promax-essay.md`
- `promax-continuation-index.md`
- `promax-artifact-manifest.json`
- `promax-continuation-ledger.json`

`promax-essay.md` 必须是连续、可读、有明确立场的完整中文正文，不能是台账转储或 dossier 摘要。解释每个 `applied` 概念的权威定义、当前作用、邻接关系、误用边界、相似结构和失效条件。每个主要机制至少提供两个显式标型的相似例子和一个反例或失效例子；例子类型只能按模板登记为真实案例、用户材料例子、条件情景或结构类比。真实案例不足时如实降档，不得伪造。

用户要求判断时给出当前最佳判断、判断强度、次优解释、最强反证、为何暂不采纳、撤回条件和行动上限。用户要求建议时比较主动行动、延迟、试探、退出或转移、维持现状、不行动六类方案，明确首选、次选、切换条件、不行动成本、授权状态、停止条件和回滚条件。

上下文或单次回复容量不足时，先保存完整已生成工件，再把未交付部分写入 `promax-continuation-ledger.json` 与 `promax-continuation-index.md`。续跑必须绑定当前 manifest，并从明确 section 恢复；不得用摘要替换剩余正文，不得静默截断。

## 验证与修复

先验证 v8 知识面，再验证当前 artifact workspace：

```text
python skills/crossframe-promax/scripts/check_crossframe_promax_v8_full_source.py --repo <仓库根目录>
python skills/crossframe-promax/scripts/check_crossframe_promax_v8_knowledge.py --repo <仓库根目录>
python skills/crossframe-promax/scripts/check_crossframe_promax_artifacts.py --workspace <工件目录> --repo <仓库根目录> --final-chat --write-report --json
```

验证失败时读取 `protocols/promax-repair-loop-protocol.md`，持久化机器可读 repair plan，按最早 `affected_phase` 局部重跑，重新生成 manifest，并运行全套验证。禁止只补 marker、只改报告、整轮重抽或删除已交付长文来伪装通过。

任何 validator-derived 状态都必须来自本次命令刚写入并通过新鲜度校验的 fresh validator report；不得根据 `init`、P0、缺文件、旧报告或模型自检自行命名状态。只有该报告的 `overall_status=pass` 且 `completion_status=promax-complete` 时，才能宣称严格完成。artifact-run 有能力缺口或未满足项时，仍先交付所有能力允许生成的完整工件，再引用 fresh report 的结构化未完成原因。

## 最终聊天合同

最终聊天只投影五项：

1. `run_status`
2. `center_judgment_summary`
3. `key_withdrawal_conditions`
4. `artifact_links`
5. `continuation_entry`

这五项必须从 checker JSON 的 `final_chat_projection` 逐值投影已验证的 `promax-final-chat.json`：保持每个字符串、数组、`null` 与顺序原值，不得改写、翻译、补充或用临时场景化判断替换。若 `final_chat_projection` 为空，禁止最终交付，先修复并重跑带 `--final-chat --write-report` 的验证命令。

完整解释留在 `promax-essay.md` 等独立工件中。若平台不能写文件，则严格按 continuation index 分段交付同一内容与顺序，不能把五项聊天索引冒充完整正文。
