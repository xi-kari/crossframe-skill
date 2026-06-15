<div align="center">

# CrossFrame Skill Suite

### 面向 AI 的中文结构诊断、连续联读、文章成文与质量审查 skill 家族

**先拆清事实、尺度、证据、责任和机制，再输出普通人能读懂的判断、答复、案例、备忘录或完整中文文章。**

<br>

![License](https://img.shields.io/badge/license-MIT-f3d7e6?style=flat-square&labelColor=fff7fb&color=f3d7e6)
![Trigger](https://img.shields.io/badge/trigger-explicit_only-d8ebff?style=flat-square&labelColor=fafcff&color=d8ebff)
![Version](https://img.shields.io/badge/framework-v5.0-e4ddff?style=flat-square&labelColor=fffaff&color=e4ddff)
![Output](https://img.shields.io/badge/output-dossier_%2B_article_%2B_review-d9f2df?style=flat-square&labelColor=fbfffb&color=d9f2df)
![Runtime](https://img.shields.io/badge/runtime-progressive_disclosure-f8efcf?style=flat-square&labelColor=fffdf6&color=f8efcf)

<p align="center">
  <a href="#overview"><strong>快速理解</strong></a>
  ·
  <a href="#current-version"><strong>当前版本</strong></a>
  ·
  <a href="#workflow"><strong>完整流程</strong></a>
  ·
  <a href="#skills"><strong>Skill 地图</strong></a>
  ·
  <a href="#runtime"><strong>运行成本</strong></a>
  ·
  <a href="#install"><strong>安装</strong></a>
  ·
  <a href="#release"><strong>发布说明</strong></a>
</p>

</div>

---

<a id="overview"></a>
## 快速理解

CrossFrame Skill Suite 是一组本地 AI skills，用来让 AI 在处理复杂中文问题时先做结构判断，再输出可读结果。

它适合这些任务：

- 关系、家庭、照护、解释劳动、无法退出、低权力主体保护。
- 团队、项目、组织复盘、授权链、反馈写回、责任链修复。
- 平台治理、公共制度、政策、监管、机构责任、公共评论。
- 事故、合规材料、AI 报告、自评文本、来源证据边界。
- 哲学概念、思想文章、读书互读、趋势推演和中性机制分析。
- 把结构诊断转成完整中文文章，并在输出前做质量闸。

它不适合被动触发。整套 CrossFrame 是 **explicit-only**：用户必须明确点名 `crossframe-suite`、`crossframe`、某个 `crossframe-*`，或使用 `$crossframe-*` / `/crossframe-*` 命令。普通聊天、普通写作、普通评论不应自动召回它。

---

<a id="current-version"></a>
## 当前版本

当前权威源是 **跨尺度结构诊断框架 v5.0**。

本仓库当前已经从旧的 v3 连读体系升级为 v5 原位体系：

- `skills/crossframe/references/v5-source-spine.md`：v5 标题、段落范围、相邻关系和表格索引。
- `skills/crossframe/references/v5-section-digest-index.md`：v5 逐节摘要、不可误读边界和相邻提醒。
- `skills/crossframe/references/v5-term-fidelity.md`：v5 术语保真表。
- `skills/crossframe/references/v5-material-selection-map.md`：v5 source modules、协议、包和模板选择图。
- `skills/crossframe/references/continuity-bundles/v5/`：26 个独立 v5 连读包。
- `skills/crossframe/references/continuity-closure-map.md`：运行时轻量闭包图。
- `skills/crossframe/references/runtime-read-policy.md`：默认运行读取成本控制策略。

v3/v2 文件只作为历史基线和演化对照。默认判断以 v5 为准。

---

<a id="workflow"></a>
## 完整流程

推荐入口是 `crossframe-suite`。

完整链路如下：

```text
/crossframe-suite
-> 模式/角色选择器（4 个输出模式 + 6 个角色）
-> suite 路由与专项拆解
-> crossframe 生成 v5-read-state-capsule
-> 源锚点完整性检查
-> 结构洞察底稿
-> 文章类型选择器（9 类文章）
-> 写作技法读取（最多 5 张技法卡）
-> 文章正文
-> crossframe-review 质量闸摘要
```

开头只选两件事：

- 输出模式：保守、客观、激进、批判。
- 角色：学术专家、实践工匠、战略决策者、大众传播、批判反思者、未来探索者。

文章类型不在开头选。只有当结构洞察底稿已经形成、最终确认要进入成文层时，才弹出文章类型选择器。

九类文章类型：

1. 答复体文章
2. 公共评论文章
3. 思想/概念阐释文章
4. 组织复盘/修复文章
5. 案例叙事/案例分析文章
6. 论辩/反驳文章
7. 读书互读/吸收文章
8. 趋势推演文章
9. 中性分析长文

---

<a id="skills"></a>
## Skill 地图

本仓库当前包含 12 个 active CrossFrame skill。

| Skill | 适合什么任务 | 默认输出 |
| --- | --- | --- |
| `crossframe-suite` | 总入口，判断任务应该连续读取哪些 sibling skill。 | 调度提纲 + 专项产物 + 文章链路 + review 质量闸。 |
| `crossframe` | 结构诊断、推演、开放断言、强判断、低条件行动、v5 胶囊生成。 | 推理提纲 + 人话判断 / 开放断言 / 行动边界。 |
| `crossframe-essay` | 把结构判断写成中文批判性洞察文章。 | 结构洞察底稿 + 完整文章正文。 |
| `crossframe-critical` | 点名触发的结构批判长文。 | 批判底稿 + 篇章方案 + 1800-2800 字正文。 |
| `crossframe-review` | 审查 CrossFrame 输出有没有真的推理。 | 评审报告 / 质量闸摘要 / 修复建议。 |
| `crossframe-dialogue` | 答读者问、编辑回信、咨询式回应。 | 短答复 / 编辑回信 / 意见回复。 |
| `crossframe-casebook` | 把材料沉淀成案例。 | 案例条目、案例索引、脱敏来源台账。 |
| `crossframe-public` | 公共议题、平台治理、制度评论、政策/监管/机构责任。 | 公共议题诊断、证据边界摘要、公共评论底稿。 |
| `crossframe-org` | 团队、项目、组织复盘与修复。 | 组织诊断备忘录、反馈写回方案、低风险试点。 |
| `crossframe-teach` | 把 CrossFrame 概念讲给普通人。 | 概念课、误读边界、现实信号和练习。 |
| `crossframe-debate` | 检验命题、争论和正反论证。 | 正反结构、隐藏前提、最强反驳、撤回条件。 |
| `crossframe-notebook` | 读书、理论、文章研究笔记。 | 研究笔记、来源台账、关联/不同/可吸收/冲突处。 |

简单记法：

- 复杂任务用 `crossframe-suite`。
- 只要固定产物时点名对应专项 skill。
- 只要评审时用 `crossframe-review`。
- 更锋利的批判长文用 `$crossframe-critical` 点名触发。

---

## v5 连读包

v5 连读包不是关键词检索，而是连续语义约束。

当前有 26 个包，放在：

```text
skills/crossframe/references/continuity-bundles/v5/
```

运行时先读轻量闭包图：

```text
skills/crossframe/references/continuity-closure-map.md
```

命中一个入口包后，必须递归展开它的“必须同读闭包”。这个闭包不受“最多 3 个核心包 + 2 个辅助包”的限制。相邻候选包只在硬依赖闭包完成后追加。

高责任、公共制度、组织处置、公开判断、AI 合规、亲密关系/无法退出、长期演化和文章输出，都会触发更严格的闭包与降档规则。

---

## v5-read-state-capsule

`v5-read-state-capsule` 是当前体系的核心运行产物。

它由 `crossframe` 核心层生成，传给 essay、public、org、debate、review 等下游 skill 复用。

胶囊记录：

- `selection_state`
- `workflow_state`
- `user_task`
- `v5_source_modules`
- `v5_continuity_bundles`
- `required_closure`
- `adjacent_candidates`
- `source_grounding`
- `post_body_risk_sweep`
- `downstream_read_policy`
- `integrity_risks`

它解决的是同一个问题：不要让 core、essay、review 各自重新发明源路由。下游默认复用胶囊，只有源锚点缺失、高责任审计或完整性检查失败时才定向补读。

---

## 来源台账与证据边界

涉及公共事实、真实机构、平台、政策、公司、人物、最新事实、AI 报告、合规材料、批判文章或强判断时，必须建立来源台账。

每条来源必须记录九字段：

1. 来源
2. 时间
3. 来源类型
4. 支持的命题
5. 不能证明什么
6. 证据档位
7. 使用位置
8. 降档理由
9. 仍需补证处

当前版本增加了硬校验：

- 不得合并“降档理由”和“仍需补证处”。
- 不得用“官方页面”“官方列表”“机构网站”等来源描述伪填“时间”。
- `使用位置` 不能只写“正文自然提及”，必须能定位到标题、段落、短摘或命题强度。
- 单一来源族、二手入口、未完成调查、未来节点未落地时，最高只能写“待核验分析 / 内部压测可用 / 条件趋势推演”。

---

## 文章输出

`crossframe-essay` 默认输出：

```text
# 结构洞察底稿

# 文章正文
```

默认正文是 `full-visible-v5-longform`：

- 完整可见底稿。
- 完整长文正文。
- 正文一般 1200-2200 中文字。
- 有标题、具体入口、中心命题、递进段、概念上升、现实回落、边界段和余味结尾。

底稿不能替代正文。review 也不能吞掉正文。

---

## 写作技法库

当前版本吸收了《文章写作技法》的 50 个技法卡，放在：

```text
skills/crossframe-essay/references/writing-techniques/
```

运行时不全量读取 50 张卡。

正确流程是：

```text
文章类型
-> article-technique-routing-map.md
-> 选择 3 个核心技法
-> 必要时追加 0-2 个辅助技法
-> 只读取最终选中的 3-5 张技法卡
```

技法只改变表达结构，不改变事实边界、判断档位、连续联读包、证据责任和 review 质量闸。

当前版本还要求“技法落地证据表”：

```text
技法 -> 负责段落动作 -> 正文短摘/段落编号 -> 它不能证明什么 -> 越界反查
```

没有正文短摘时，只能说“读取了技法”，不能说“技法已落地”。

---

<a id="runtime"></a>
## 运行成本与模型建议

推荐模型：

```text
deepseekv4pro
```

推荐原因：CrossFrame v5 的完整链路会涉及长上下文、连续联读、来源边界、文章成文和 review 反向审计。需要模型有较强长上下文保持能力、中文推理稳定性和较低长上下文成本。

经验消耗：

- 一轮完整 CrossFrame Suite 流程：约 **40 万 token**。
- 全量推理、重审计、源锚点细查、长文成文和 review 全展开：约 **100 万 token**。
- 价格通常在 **0.1 元到 0.15 元人民币** 之间浮动。

说明：

- 这里是本地使用经验值，不是固定报价。
- 实际成本会随模型供应商、上下文缓存、输入材料长度、是否联网查源、是否展开 review 和是否读取大 source modules 变化。
- 正常运行已经加入 `runtime-read-policy.md`，默认不全量读取大索引、eval/examples、完整案例或全部 50 个技法卡。

---

## 运行时瘦身策略

本版本新增运行时渐进读取规则。

默认读取：

1. 当前入口 `SKILL.md`
2. `runtime-read-policy.md`
3. `read-routing-map.md`
4. `continuity-closure-map.md`
5. 被命中的 protocol / worksheet / template
6. 被命中的 v5 连读包文件
7. 成文时最多 5 张技法卡

默认不读：

- `evals/`
- `examples/`
- 完整成功案例
- 完整失败案例
- 全量 `v5-source-spine.md`
- 全量 `v5-section-digest-index.md`
- 全量 50 个技法卡
- v2/v3 历史基线

这些材料只在开发压测、回归验证、风格调试、源锚点失败、高责任源审计或用户显式要求过程审计时读取。

---

## Review 质量闸

`crossframe-review` 不是正文作者。默认成文链路里，它只做质量闸。

当前 review 必须区分：

- `structural_pass`：字段和顺序是否存在。
- `substantive_pass`：命题、来源、胶囊、技法和正文是否互相支撑。
- `publish_boundary`：内部压测、待核验分析、可发布需补证、不得用于强判断。

review 还必须执行“反向否决最小块”：

1. 一个最可能硬失败候选。
2. 一个中心命题过强候选。
3. 一个来源/技法越界候选。

如果只检查标题、底稿、正文、胶囊、来源台账和质量闸是否存在，只能算 `structural_pass`，不能写成总通过。

---

<a id="install"></a>
## 安装

### Codex

把 `skills/crossframe*` 复制到 Codex skill 目录：

```text
C:\Users\<you>\.codex\skills
```

### Claude / Claude Code

把 `skills/crossframe*` 复制到：

```text
~/.claude/skills
```

仓库中也保留了 `.claude/skills` 镜像，用于本地同步和 Claude 适配。

### Reasonix / DeepSeek 本地环境

本地常用同步目录：

```text
D:\deepseek\.reasonix\skills
```

### 其他 AI 软件

仓库中保留多个适配目录：

- `.cursor/`
- `.roo/`
- `.windsurf/`
- `.continue/`
- `.clinerules/`

这些适配文件不是权威源。权威源始终是：

```text
skills/*
```

---

## 本地验证

常用检查命令：

```powershell
python scripts\check_crossframe_skill_integrity.py --repo .
python scripts\check_source_continuity.py --version v5 --source-docx "E:\世界模型\跨尺度结构诊断框架v5.0.docx" --repo .
```

当前完整性检查覆盖：

- 12 个 active CrossFrame skill 是否存在。
- 旧 `crossframe-v5*` / `crossframe-v3.1` 是否仍作为 active skill 存在。
- v5 连读包是否完整。
- 50 个写作技法卡是否完整。
- 文章类型选择器、技法路由、来源台账、胶囊、源锚点规则是否存在。
- runtime 轻量读取策略和闭包图是否存在。
- review 失败分类、反向否决、结构/实质/发布边界是否存在。

---

<a id="release"></a>
## 发布说明

当前 Release 版本包含：

- 12 个 CrossFrame active skill。
- v5 source spine / section digest / coverage / term fidelity / material selection。
- 26 个 v5 连读包。
- `v5-read-state-capsule`。
- `source-anchor-integrity-check`。
- `source-ledger-workflow`。
- 9 类文章类型选择器。
- 50 个写作技法卡。
- runtime 轻量读取策略。
- review 反向否决质量闸。
- Codex / Claude / Reasonix / Cursor / Roo / Windsurf / Continue 等本地适配文件。

历史 `crossframe-v5*` 目录已经退休，不再作为 active 入口。当前使用现有 `crossframe*` 家族原位承载 v5。

---

## License

MIT
