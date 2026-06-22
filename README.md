<div align="center">

# CrossFrame Skill Suite

### 面向 AI 的中文结构诊断、连续联读、文章成文与质量审查 skill 家族

**先拆清事实、尺度、证据、责任和机制，再输出普通人能读懂的判断、答复、案例、备忘录或完整中文文章。**

<br>

![License](https://img.shields.io/badge/license-MIT-f3d7e6?style=flat-square&labelColor=fff7fb&color=f3d7e6)
![Trigger](https://img.shields.io/badge/trigger-explicit_only-d8ebff?style=flat-square&labelColor=fafcff&color=d8ebff)
![Framework](https://img.shields.io/badge/framework-v5.0-e4ddff?style=flat-square&labelColor=fffaff&color=e4ddff)
![Output](https://img.shields.io/badge/output-dossier_%2B_article_%2B_review-d9f2df?style=flat-square&labelColor=fbfffb&color=d9f2df)
![Runtime](https://img.shields.io/badge/runtime-progressive_disclosure-f8efcf?style=flat-square&labelColor=fffdf6&color=f8efcf)

<p align="center">
  <a href="#overview"><strong>快速理解</strong></a>
  ·
  <a href="#workflow"><strong>完整流程</strong></a>
  ·
  <a href="#skills"><strong>Skill 地图</strong></a>
  ·
  <a href="#runtime"><strong>运行成本</strong></a>
  ·
  <a href="#install"><strong>安装</strong></a>
  ·
  <a href="#verify"><strong>验证</strong></a>
</p>

</div>

---

<a id="overview"></a>
## 快速理解

CrossFrame Skill Suite 是一组给 AI 使用的本地 skills。它让 AI 在回答复杂中文问题时先完成结构诊断，再进入答复、评论、复盘、案例、读书笔记、趋势推演或完整文章输出。

它适合处理：

- 关系、家庭、照护、解释劳动、无法退出、低权力主体保护。
- 团队、项目、组织复盘、授权链、反馈写回、责任链修复。
- 平台治理、公共制度、政策、监管、机构责任、公共评论。
- 事故、合规材料、AI 报告、自评文本、来源证据边界。
- 哲学概念、思想文章、读书互读、趋势推演和中性机制分析。
- 把结构诊断转成完整中文文章，并在输出前做质量闸。

整套 CrossFrame 是 **explicit-only**：只有用户明确点名 `crossframe-suite`、`crossframe`、某个 `crossframe-*`，或使用 `$crossframe-*` / `/crossframe-*` 命令时才启动。普通聊天、普通写作、普通评论不应自动召回它。

---

## 当前仓库内容

权威框架源是 **跨尺度结构诊断框架 v5.0**。仓库内的核心内容包括：

- `skills/crossframe/`：结构诊断核心层。
- `skills/crossframe-suite/`：推荐总入口与模式/角色选择器。
- `skills/crossframe-essay/`：文章类型选择器、结构洞察底稿、正文生成和 50 个写作技法卡。
- `skills/crossframe-review/`：质量闸、源锚点审查、正文吞没防护和失败分类。
- `skills/crossframe-public/`：公共议题、平台治理、政策和机构责任分析。
- `skills/crossframe-org/`：团队、项目、组织复盘和修复。
- `skills/crossframe-debate/`：命题拆解、反驳、最强反方和撤回条件。
- `skills/crossframe-critical/`：点名调用的结构批判长文。
- `skills/crossframe-dialogue/`：读者答复、咨询式短答和编辑回信。
- `skills/crossframe-casebook/`：案例库条目、脱敏材料和复用索引。
- `skills/crossframe-history/`：历史材料、文明连续史、史料闭合和 archive/FOIA backlog 的领域接口层。
- `skills/crossframe-notebook/`：读书、理论、文章和材料互读笔记。
- `skills/crossframe-teach/`：概念讲解、误读边界和练习。
- `.claude/skills/`：Claude 兼容镜像。
- `.claude/commands/`、`.cursor/`、`.continue/`、`.clinerules/`、`.roo/`、`.windsurf/`、`.github/`：多种 AI 工具的规则和入口适配。
- `scripts/`：结构连续性和 skill 完整性检查脚本。

仓库不需要运行服务。它提供的是本地 agent / IDE / AI 工具可读取的 skill 文件、协议、模板、参考材料和校验脚本。

---

<a id="workflow"></a>
## 完整流程

推荐入口是 `crossframe-suite`。

完整链路：

```text
/crossframe-suite
-> 模式/角色选择器
-> suite 调度提纲
-> crossframe 核心层
-> v5-read-state-capsule
-> 源锚点完整性检查
-> 专项 skill 拆解
-> 结构洞察底稿
-> 文章类型选择器
-> 写作技法读取
-> 文章正文
-> review 质量闸摘要
```

入口选择器只选择两件事：

```text
输出模式：保守 / 客观 / 激进 / 批判
角色：学术专家 / 编辑 / 组织顾问 / 公共议题分析者 / 咨询式答复者 / 教学解释者
```

常用选择是：

```text
2+1 = 客观 + 学术专家
```

文章类型不在入口选择。只有当流程进入成文层、并且用户没有显式指定文章类型时，才展示文章类型选择器。

---

## 运行读法

CrossFrame 使用渐进读取，不要求一次性加载全部资料。

运行时优先读取：

1. `skills/crossframe/SKILL.md`
2. `skills/crossframe/references/runtime-read-policy.md`
3. `skills/crossframe/references/read-routing-map.md`
4. `skills/crossframe/references/continuity-closure-map.md`
5. 命中的协议、工作表、模板和 v5 连读包
6. essay 层命中的文章类型路由和最多 5 个写作技法卡

默认不读取：

- 全量 v5 大索引
- 全量 evals
- 全量 examples
- 全量案例库
- 全量 50 个写作技法卡

需要深查时才按路由补读对应文件。

---

## v5-read-state-capsule

`v5-read-state-capsule` 是核心层传给 essay、专项 skill 和 review 的读态摘要。它避免下游 skill 重复整块读取源材料，也避免文章层脱离源边界自行发挥。

模板位置：

```text
skills/crossframe/templates/read-state-capsule.md
```

固定字段：

- `selection_state`
- `workflow_state`
- `user_task`
- `v5_source_modules`
- `v5_continuity_bundles`
- `required_closure`
- `adjacent_candidates`
- `source_grounding`
- `downstream_read_policy`
- `integrity_risks`
- `post_body_risk_sweep`

胶囊只记录选择状态、源模块、入口包、必须同读闭包、源锚点和下游读取策略，不复制大段正文。

---

## 源锚点完整性

源锚点完整性检查用于确认输出里的中心命题、机制判断、概念上升、行动边界、文章转译和写作技法都能回指读态胶囊或连读包。

规则位置：

```text
skills/crossframe/worksheets/source-anchor-integrity-check.md
```

不能回指源锚点的内容必须标记为：

- `本文推断`
- `表达转译`
- `外部思想映射`

不能写成 CrossFrame v5 的原义。

---

## 来源台账

公共议题、真实机构、平台、政策、人物、公司、事故、AI 合规材料和最新事实进入文章层时，必须写来源台账摘要。

规则位置：

```text
skills/crossframe/references/source-ledger-workflow.md
```

字段：

```text
来源
时间
来源类型
支持的命题
不能证明什么
证据档位
使用位置
降档理由
仍需补证处
```

如果不能联网或不能核验，只能降档为待核验分析，不得编造来源。

---

## 文章类型

文章类型选择器位置：

```text
skills/crossframe-essay/templates/article-type-selection-dialog.md
```

9 种文章类型：

1. 答复体文章
2. 公共评论文章
3. 思想/概念阐释文章
4. 组织复盘/修复文章
5. 案例叙事/案例分析文章
6. 论辩/反驳文章
7. 读书互读/吸收文章
8. 趋势推演文章
9. 中性分析长文

文章类型决定成文形态和技法路由，不改变事实边界、证据责任、判断档位和源锚点。

---

## 写作技法库

写作技法库位置：

```text
skills/crossframe-essay/references/writing-techniques/
```

共 50 个独立技法文件。运行时先读：

```text
skills/crossframe-essay/references/article-technique-routing-map.md
skills/crossframe-essay/references/writing-techniques/index.md
```

再按文章类型和题材问题读取少量技法卡。每次最多读取：

```text
3 个核心技法 + 2 个辅助技法
```

技法只负责表达结构，例如入口、段落动作、转折、论证层次、点睛句和结尾余味。技法不能新增事实，不能制造强判断，不能越过读态胶囊和源锚点。

---

<a id="skills"></a>
## Skill 地图

| Skill | 主要职责 | 常见输出 |
| --- | --- | --- |
| `crossframe-suite` | 总入口、模式/角色选择、路由、专项链路组织 | 调度提纲、工作流链路 |
| `crossframe` | 核心结构诊断、v5 source modules、连读包、胶囊 | 结构判断、源锚点、诊断底稿 |
| `crossframe-essay` | 文章类型选择、技法路由、底稿与正文 | 结构洞察底稿、文章正文 |
| `crossframe-review` | 输出审查、质量闸、失败分类 | 简短质量闸摘要、修复建议 |
| `crossframe-public` | 公共议题、制度、平台、政策、机构责任 | 公共议题诊断、来源台账 |
| `crossframe-org` | 组织复盘、责任链、授权链、反馈写回 | 组织诊断备忘录、修复方案 |
| `crossframe-debate` | 命题拆解、论辩、反驳、撤回条件 | 正反结构、最强反方 |
| `crossframe-critical` | 点名调用的结构批判长文 | 批判底稿、批判文章 |
| `crossframe-dialogue` | 读者答复、咨询式回应、编辑回信 | 短答、回信、咨询答复 |
| `crossframe-casebook` | 案例整理、脱敏、机制提取 | 案例条目、案例索引 |
| `crossframe-history` | 历史材料、史料等级、断代尺度、archive/FOIA backlog | 历史接口分析、史料闭合台账、公开边界摘要 |
| `crossframe-notebook` | 读书、理论、文章和材料互读 | 研究笔记、吸收/冲突表 |
| `crossframe-teach` | 概念教学、误读边界、练习 | 概念课、小练习 |

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
- 默认运行已经有渐进读取策略，不全量读取大索引、eval/examples、完整案例或全部 50 个技法卡。

---

<a id="install"></a>
## 安装

### Codex

把需要的 skill 目录复制到：

```text
C:\Users\<you>\.codex\skills
```

推荐复制：

```text
skills\crossframe
skills\crossframe-suite
skills\crossframe-essay
skills\crossframe-review
skills\crossframe-public
skills\crossframe-org
skills\crossframe-debate
skills\crossframe-critical
skills\crossframe-dialogue
skills\crossframe-casebook
skills\crossframe-history
skills\crossframe-notebook
skills\crossframe-teach
```

### Claude

仓库提供 Claude 兼容镜像：

```text
.claude\skills
.claude\commands
```

可按 Claude Code 的项目规则加载。

### Reasonix

可把 `skills\crossframe*` 同步到：

```text
D:\deepseek\.reasonix\skills
```

### 其他 AI 工具

仓库内包含多种适配规则：

```text
.cursor\rules
.continue\rules
.clinerules
.roo\rules
.windsurf\rules
.github\copilot-instructions.md
AGENTS.md
CLAUDE.md
GEMINI.md
INTERFACES.md
llms.txt
```

---

## 使用示例

推荐入口：

```text
/crossframe-suite
```

带选择器：

```text
/crossframe-suite 2+1
```

指定文章类型：

```text
/crossframe-suite 2+1，写成公共评论文章：平台“有申诉入口”为什么不等于治理有效？
```

只做诊断：

```text
/crossframe 2+1，只做结构诊断，不进入文章层。
```

专项调用：

```text
/crossframe-org 2+1，分析团队为什么越复盘越失真。
/crossframe-debate 2+1，反驳“流程存在就说明组织已经负责”。
/crossframe-history 2+1，分析唐中后期安史之乱、藩镇与两税法的史料边界和历史接口层。
/crossframe-notebook 2+1，互读这篇文章和 CrossFrame 的相通与冲突处。
```

---

<a id="verify"></a>
## 验证

在仓库根目录运行：

```powershell
python scripts\check_crossframe_skill_integrity.py --repo .
python scripts\check_source_continuity.py --version v5 --source-docx "E:\世界模型\跨尺度结构诊断框架v5.0.docx" --repo .
```

预期结果：

```text
ok: crossframe skill integrity checks passed
ok: v5 source continuity files match DOCX heading structure
```

---

## 许可

MIT License. See [LICENSE](LICENSE).
