<div align="center">

# CrossFrame Skill Suite

### 给 AI 用的中文结构诊断与成文技能组。

**先拆清事实、尺度、证据和责任，再输出普通人能读懂的判断、答复、案例、备忘录或文章。**

<br>

![许可证](https://img.shields.io/badge/许可证-MIT-f3d7e6?style=flat-square&labelColor=fff7fb&color=f3d7e6)
![触发](https://img.shields.io/badge/触发-显式调用_only-d8ebff?style=flat-square&labelColor=fafcff&color=d8ebff)
![输出](https://img.shields.io/badge/输出-推理提纲_%2B_人话判断-e4ddff?style=flat-square&labelColor=fffaff&color=e4ddff)
![文章](https://img.shields.io/badge/文章-洞察底稿_%2B_正文-d9f2df?style=flat-square&labelColor=fbfffb&color=d9f2df)
![适配](https://img.shields.io/badge/适配-Codex_Claude_Cursor_Gemini_Copilot-f8efcf?style=flat-square&labelColor=fffdf6&color=f8efcf)

<p align="center">
  <a href="#overview"><strong>快速理解</strong></a>
  ·
  <a href="#usage"><strong>快速使用</strong></a>
  ·
  <a href="#skills"><strong>Skill 地图</strong></a>
  ·
  <a href="#output"><strong>输出方式</strong></a>
  ·
  <a href="#install"><strong>安装</strong></a>
  ·
  <a href="#adapters"><strong>其他 AI 软件</strong></a>
</p>

</div>

---

<a id="overview"></a>
## 快速理解

CrossFrame 是一组中文 AI skills，用来处理关系、团队、组织、制度、公共争议、长期演化和思想文章这类复杂问题。

它的核心不是“套一堆概念”，而是让 AI 先完成四件事：

1. 分清事实、猜测、证据成本和责任边界。
2. 判断问题发生在哪个尺度：个人、关系、团队、组织、制度或公共场域。
3. 按任务读取必要 protocol、concept card、连续联读包和完整性检查。
4. 先给可见推理提纲，再输出人话判断；写文章时先给结构洞察底稿，再写正文。

整套 CrossFrame 只能显式触发。用户必须点名 `crossframe-suite`、`crossframe`、某个 `crossframe-*`，或使用 `$crossframe-*` / `/crossframe-*` 命令。普通分析、写作、评论、组织修复、读书或辩论任务不应自动召回它。

## 当前内容

本仓库当前包含 12 个 CrossFrame skill：

`crossframe-suite`、`crossframe`、`crossframe-essay`、`crossframe-critical`、`crossframe-review`、`crossframe-dialogue`、`crossframe-casebook`、`crossframe-public`、`crossframe-org`、`crossframe-teach`、`crossframe-debate`、`crossframe-notebook`。

`skills/crossframe/references/integrity-check.md` 是日常完整性检查入口；`continuity-bundles.md`、`concept-fidelity-check.md` 和 `source-continuity-check.md` 用于展开审计或追踪源结构。

---

<a id="usage"></a>
## 快速使用

复杂任务优先用总入口：

```text
请用 crossframe-suite 分析这段团队复盘材料，并写成一篇完整文章。
```

只要结构诊断：

```text
请用 crossframe 诊断这个关系问题，只要推理提纲和人话判断，不要文章。
```

只要文章：

```text
请用 crossframe-essay，把这个组织问题写成一篇中文批判性洞察文章。
```

只要评审：

```text
请用 crossframe-review 审查下面这段 CrossFrame 输出是否真的完成了推理。
```

点名批判长文：

```text
请用 $crossframe-critical 写一篇更锋利的结构批判长文，先给底稿和篇章方案。
```

如果你从 `crossframe-suite` 进入，内容任务默认会在必要专项 skill 之后追加：

```text
crossframe-essay -> crossframe-review
```

也就是默认产出完整可见底稿 + 完整长文正文。只有你明确说“只要/不要文章/短答/表格/清单/纯诊断/仅行动方案”时，才关闭文章层。

---

<a id="skills"></a>
## Skill 地图

| Skill | 适合什么任务 | 默认输出 |
| --- | --- | --- |
| `crossframe-suite` | 复杂任务总入口，决定读取哪些 sibling skill。 | 调度提纲 + 专项产物 + 文章链路 + 评审。 |
| `crossframe` | 结构诊断、推演、开放断言、强判断、低条件行动。 | 推理提纲 + 人话判断 / 开放断言 / 行动边界。 |
| `crossframe-essay` | 把结构判断写成中文批判性洞察文章。 | 结构洞察底稿 + 完整文章正文。 |
| `crossframe-critical` | 点名触发的结构批判长文。 | 批判底稿 + 篇章方案 + 1800-2800 字正文。 |
| `crossframe-review` | 审查 CrossFrame 输出质量。 | 评审报告、风险点和修复建议。 |
| `crossframe-dialogue` | 答读者问、编辑回信、咨询式短答复。 | 短答复 / 编辑回信 / 意见回复。 |
| `crossframe-casebook` | 把材料沉淀成可复用案例。 | 案例条目、索引和脱敏来源台账。 |
| `crossframe-public` | 公共议题、平台申诉、制度评论、合规材料。 | 公共议题诊断、证据边界摘要、评论底稿。 |
| `crossframe-org` | 团队、项目、组织修复。 | 组织诊断备忘录、反馈写回方案、低风险试点。 |
| `crossframe-teach` | 把 CrossFrame 概念讲给普通人。 | 概念课、误读边界、现实信号和练习。 |
| `crossframe-debate` | 检验命题、争论和正反论证。 | 正反结构、隐藏前提、最强反驳、撤回条件。 |
| `crossframe-notebook` | 读书、理论、文章研究笔记。 | 研究笔记、来源台账、可吸收与冲突处。 |

最简单的记法：**复杂任务用 `crossframe-suite`；只要固定产物时点名对应专项 skill。**

`crossframe-critical` 是例外。它不进入 `crossframe-suite` 默认调度，只能在用户明确点名 `$crossframe-critical`、`crossframe-critical` 或要求测试这个批判 skill 时使用。

---

<a id="output"></a>
## 输出方式

CrossFrame 默认先给推理提纲：

```text
推理提纲
- 诊断对象：这次到底在分析什么
- 事实边界：哪些是已知事实，哪些只是猜测
- 尺度窗口：个人、关系、团队、组织、制度还是公共场域
- 机制候选：至少列出两种可能原因
- 判断档位：现在能不能下强判断
- 下一步：观察什么，或做什么低风险动作
```

然后再说人话。例如用户问：

> 我们团队每次复盘都能说出问题，但下一轮还是一样。中层越来越累，基层觉得没人听。

不应该只回答：

> 这是反馈写回失败。

更应该先说明：

> 这个团队不一定缺少反思，真正缺的可能是“说出来以后有没有改变”。如果复盘只增加会议和解释成本，却不改变资源、角色和时间表，大家就会慢慢学会沉默。

写文章时，`crossframe-essay` 会先生成 `结构洞察底稿`，再写完整正文。底稿会记录事实边界、机制候选、连续联读包、源结构保真、概念风险、责任链、成本链、证据缺口和文章递进顺序。

常见 suite 链路：

```text
普通洞察文章：
crossframe -> crossframe-essay -> crossframe-review

公共评论文章：
crossframe -> crossframe-public -> crossframe-essay -> crossframe-review

组织复盘/修复文章：
crossframe -> crossframe-org -> crossframe-essay -> crossframe-review

读书后成文：
crossframe -> crossframe-notebook -> crossframe-essay -> crossframe-review
```

它不会把所有 skill 一起触发。没用到的 skill 会写在“不读取”里，避免上下文变重和判断跑偏。

---

## 核心约束

- **显式触发**：不因为普通任务自动启用 CrossFrame。
- **先说人话**：术语只能解释判断，不能冒充判断。
- **不人格审判**：结构诊断不能写成“某人就是坏/没救/没主体性”。
- **判断可撤回**：证据不足时必须降低判断档位，写出撤回或升级条件。
- **高风险概念要读卡**：如承接/回流、开放断言、尺度转移、观测反身性、责任链、证据成本、退出转移、爱/开放行动等。
- **完整性检查**：日常使用 `integrity-check.md`，需要审计时再展开连续联读包、概念保真和源结构连续性工作表。
- **专业边界**：不能替代法律、医疗、工程、安全等专业判断。
- **反合规表演**：不能把 AI 生成报告当成独立强证据或合规证明。

---

<a id="install"></a>
## 安装

### Codex 一键安装

克隆仓库后运行：

```powershell
git clone https://github.com/xi-kari/crossframe-skill.git
cd crossframe-skill
.\scripts\install-codex.ps1
```

脚本会安装全部 12 个 skill 到 `$HOME\.codex\skills\`。如果目标目录已有同名 skill，脚本会先临时备份，安装失败时自动恢复。

### Codex 逐个安装

如果只想用 Codex skill-installer：

```powershell
$repo = "xi-kari/crossframe-skill"
$installer = "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py"
$paths = @(
  "skills/crossframe-suite",
  "skills/crossframe",
  "skills/crossframe-essay",
  "skills/crossframe-critical",
  "skills/crossframe-review",
  "skills/crossframe-dialogue",
  "skills/crossframe-casebook",
  "skills/crossframe-public",
  "skills/crossframe-org",
  "skills/crossframe-teach",
  "skills/crossframe-debate",
  "skills/crossframe-notebook"
)

foreach ($path in $paths) {
  py -3 $installer --repo $repo --path $path
}
```

安装后 Codex 应显示：

```text
crossframe-suite
crossframe
crossframe-essay
crossframe-critical
crossframe-review
crossframe-dialogue
crossframe-casebook
crossframe-public
crossframe-org
crossframe-teach
crossframe-debate
crossframe-notebook
```

### 手动复制

```powershell
$skills = @(
  "crossframe-suite",
  "crossframe",
  "crossframe-essay",
  "crossframe-critical",
  "crossframe-review",
  "crossframe-dialogue",
  "crossframe-casebook",
  "crossframe-public",
  "crossframe-org",
  "crossframe-teach",
  "crossframe-debate",
  "crossframe-notebook"
)

foreach ($skill in $skills) {
  Copy-Item -Path ".\skills\$skill" -Destination "$HOME\.codex\skills\$skill" -Recurse -Force
}
```

---

<a id="adapters"></a>
## 其他 AI 软件

这个仓库也提供薄适配文件，让不同 AI 工具读取同一套 CrossFrame skill。适配层只负责入口、路由和边界，不复制完整协议。

| 工具 | 入口文件 |
| --- | --- |
| Codex | `skills/crossframe*/` 全部可安装 skill |
| Claude Code | `CLAUDE.md`、`.claude/skills/crossframe*/SKILL.md`、`.claude/commands/crossframe*.md` |
| Cursor | `.cursor/rules/crossframe-suite.mdc`、`.cursor/rules/crossframe.mdc`、`.cursor/rules/crossframe-essay.mdc`、`AGENTS.md` |
| Gemini CLI | `GEMINI.md` |
| GitHub Copilot | `.github/copilot-instructions.md` |
| Windsurf / Cascade | `.windsurf/rules/crossframe.md`、`AGENTS.md` |
| Cline | `.clinerules/crossframe.md` |
| Roo Code | `.roo/rules/crossframe.md` |
| Continue | `.continue/rules/crossframe.md` |
| Aider | `CONVENTIONS.md`、`.aider.conf.yml` |
| LLM 索引 | `llms.txt` |
| 通用 agent | `AGENTS.md` |

更多维护说明见 [INTERFACES.md](INTERFACES.md)。

---

## 仓库结构

```text
crossframe-skill/
├─ skills/
│  ├─ crossframe-suite/
│  ├─ crossframe/
│  ├─ crossframe-essay/
│  ├─ crossframe-critical/
│  ├─ crossframe-review/
│  ├─ crossframe-dialogue/
│  ├─ crossframe-casebook/
│  ├─ crossframe-public/
│  ├─ crossframe-org/
│  ├─ crossframe-teach/
│  ├─ crossframe-debate/
│  └─ crossframe-notebook/
├─ .claude/
├─ .clinerules/
├─ .continue/
├─ .cursor/
├─ .github/
├─ .roo/
├─ .windsurf/
├─ scripts/
├─ AGENTS.md
├─ CLAUDE.md
├─ CONVENTIONS.md
├─ GEMINI.md
├─ INTERFACES.md
├─ llms.txt
└─ README.md
```

每个 skill 目录通常包含 `SKILL.md`、`protocols/`、`references/`、`templates/`、`evals/`、`examples/` 或 `agents/`。具体文件以各目录实际内容为准。

## 许可

MIT License. See [LICENSE](LICENSE).
