<div align="center">

# CrossFrame Skill Suite

### 给 AI 装上的中文结构思考系统：诊断、成文、审查与追问

**先拆清事实、证据、尺度、责任与机制，再输出普通读者能读懂的中文判断、答复、案例、备忘录或完整文章。**

<br>

![Language](https://img.shields.io/badge/language-%E4%B8%AD%E6%96%87%E8%BE%93%E5%87%BA-f3d7e6?style=flat-square&labelColor=fff7fb&color=f3d7e6)
![Trigger](https://img.shields.io/badge/trigger-explicit_only-d8ebff?style=flat-square&labelColor=fafcff&color=d8ebff)
![Framework](https://img.shields.io/badge/framework-CrossFrame_v5.1.7-e4ddff?style=flat-square&labelColor=fffaff&color=e4ddff)
![Workflow](https://img.shields.io/badge/workflow-diagnosis_%E2%86%92_writing_%E2%86%92_review_%E2%86%92_inquiry-d9f2df?style=flat-square&labelColor=fbfffb&color=d9f2df)
![License](https://img.shields.io/badge/license-MIT-f8efcf?style=flat-square&labelColor=fffdf6&color=f8efcf)

<p align="center">
  <a href="https://xi-kari.github.io/crossframe-skill/"><strong>网页介绍</strong></a>
  ·
  <a href="https://github.com/xi-kari/crossframe-skill/releases"><strong>下载 Release</strong></a>
</p>

<p align="center">
  <a href="#what"><strong>它是什么</strong></a>
  ·
  <a href="#quickstart"><strong>快速开始</strong></a>
  ·
  <a href="#use-cases"><strong>适用场景</strong></a>
  ·
  <a href="#closure"><strong>质量闭环</strong></a>
  ·
  <a href="#workflow"><strong>工作流</strong></a>
  ·
  <a href="#skills"><strong>Skill 地图</strong></a>
  ·
  <a href="#docs"><strong>文档</strong></a>
</p>

</div>

---

<a id="what"></a>
## 它是什么

CrossFrame Skill Suite 是一组给 AI agent 使用的中文结构诊断与成文 skills。

它适合处理那些不能只靠“给建议”“写一段评论”“简单总结”解决的问题：关系、团队、组织、制度、公共争议、历史材料、命题辩论、读者来信、研究笔记，以及需要写成完整中文文章的复杂议题。

当前仓库包含 14 个 `crossframe-*` skills；它们都是 explicit-only，不会在普通任务中自动触发。推荐入口是 `crossframe-suite`；部分专项 skill 只应由 suite 或显式命令路由进入。完整分析、成文和 review 结束后，后续追问默认交给 `crossframe-inquiry`。

安全边界先行：

- CrossFrame 不替代法律、医疗、财务、心理危机处置、正式调查或机构审查。
- 高责任结论必须保留 `source_id`、`claim_id`、证据档位、撤回条件和行动上限。
- 不做人格审判、命运预言或无证据公共定性；证据不足时只能降档、补证或撤回。

它的核心目标不是堆术语，而是让 AI 在输出前先完成几件事：

- 分清事实、解释、证据和推断。
- 看清问题发生在哪个尺度：个人、关系、组织、制度、历史阶段或公共场域。
- 找到责任链、授权链、反馈链和机制候选。
- 判断哪些结论可以说，哪些只能保留为开放断言。
- 把结构判断翻译成普通人能读懂的中文表达。

---

<a id="quickstart"></a>
## 快速开始

Codex 安装：

Windows PowerShell：

```powershell
.\scripts\install-codex.ps1
```

macOS / Linux：

```bash
bash scripts/install-codex.sh
```

Claude Code 项目内常用命令：

```text
/crossframe-suite 分析这个团队为什么复盘很多但没有真实修复
/crossframe-essay 写一篇关于平台治理的中文评论文章
/crossframe-inquiry 基于刚才的文章继续追问反证和迁移条件
```

公开仓库日常验证：

```bash
python scripts/check_crossframe_skill_integrity.py --repo .
python scripts/check_source_continuity.py --materials-only --repo .
python -m json.tool skills/crossframe/schemas/claim-ledger.schema.json
python -m pip install jsonschema
python scripts/validate_claim_ledger_schema_fixtures.py --repo .
python scripts/validate_v5_dlc_quantification_schema_fixtures.py --repo .
python scripts/check_v5_dlc_casebook_trials.py --repo .
python scripts/check_v5_dlc_publication_bundle.py --repo .
python scripts/sync_skill_mirrors.py --check
bash -n scripts/install-codex.sh
python -m py_compile scripts/*.py
git diff --check
```

v5.0 半量化 DLC 基础层只是内部审计层：它用锚点评分、schema fixtures 和降档检查暴露不确定性、撤回条件和行动上限。它不是总分系统、预测模型、认证系统或处置工具。

v5.0 半量化 DLC 案例库验证是失败发现 shakedown：它用组织、关系、公共争议和误用反例试跑来暴露降档压力、评分者分歧、锚点修订和模板阻断需求。它不能证明框架现实正确，也不能替代调查、受影响位置反馈或外部复核。

v5.0 半量化 DLC 发布源稿见 [docs/CROSSFRAME_V5_DLC.md](docs/CROSSFRAME_V5_DLC.md)，工具原型说明见 [docs/V5_DLC_TOOL_PROTOTYPE.md](docs/V5_DLC_TOOL_PROTOTYPE.md)。需要生成可分发 DOCX 时运行 `python scripts/build_v5_dlc_docx.py --repo .`。

完整上手说明见 [docs/QUICKSTART.md](docs/QUICKSTART.md)。

---

<a id="use-cases"></a>
## 适用场景

CrossFrame 适合用于：

- **关系与责任链**：亲密关系、家庭、照护、解释劳动、退出困难、低权力主体保护。
- **团队与组织**：项目复盘、授权失衡、反馈写回、责任转移、组织修复备忘录。
- **公共议题**：平台治理、政策评论、机构责任、公共承诺、合规材料和申诉文本。
- **历史材料**：史料边界、断代尺度、制度连续性、archive / FOIA backlog。
- **命题辩论**：正反结构、隐藏前提、最强反方、证据要求和撤回条件。
- **读书与研究**：理论、文章、摘录和案例材料的互读笔记。
- **中文成文**：把结构诊断转成评论、思想文章、读者答复、案例、备忘录或长文。
- **输出审查**：检查 AI 回答有没有真正推理、是否越界、是否把材料写成了空话。
- **完成后追问**：在一轮分析、成文或质量闸完成后，继续追问、反证、补证和迁移应用。

不适合用于：

- 单纯事实查询。
- 纯工具执行等非结构诊断任务。
- 普通聊天、普通改写、普通摘要。
- 用户没有要求 CrossFrame 式结构分析的场景。

---

<a id="language"></a>
## 中文输出

CrossFrame 默认面向中文问题和中文读者。

使用时应保持：

- **主要输出使用中文**。
- 结构判断、文章正文、读者答复、案例和审查报告都应以中文完成。
- `crossframe-*` 这类英文只作为 skill id 或路由标签使用，不应替代中文解释。
- 术语尽量放在后台，前台先说人话。
- 需要引用外部材料时，引用和证据边界必须可核验。

---

<a id="workflow"></a>
## 工作流

多步骤任务推荐从总入口开始：

```text
crossframe-suite
```

它会先判断任务类型，再选择需要读取的专项 skill。常见链路如下：

```text
结构诊断      crossframe -> crossframe-review
中文长文      crossframe -> crossframe-essay -> crossframe-review
公共评论      crossframe -> crossframe-public -> crossframe-essay -> crossframe-review
组织复盘      crossframe -> crossframe-org -> crossframe-essay -> crossframe-review
历史研究      crossframe -> crossframe-history -> crossframe-essay -> crossframe-review
答读者问      crossframe -> crossframe-dialogue
读书研究      crossframe -> crossframe-notebook
完成后追问    crossframe -> crossframe-review(lite) -> crossframe-inquiry
```

CrossFrame 是 **explicit-only**：只有用户明确点名 CrossFrame、`crossframe-suite`、`crossframe`、某个 `crossframe-*`，或使用对应命令时才应启动。

`crossframe-suite` 默认是重型链路：未指定时使用 `full-visible-v5-longform`，会输出完整可见底稿、完整长文正文和 review。用户可以显式要求 `brief-visible` 或 `standard-visible` 来控制体积；体积降低不取消事实边界、`claim_id`、撤回条件和行动上限。

---

<a id="closure"></a>
## 质量闭环

CrossFrame 的关键不是“多写几个步骤”，而是让 AI 对自己的判断交账：

```text
source_id -> claim_id -> concept contract -> source anchor -> review -> inquiry
```

- `source ledger` 使用十字段口径，必须说明每个 `source_id` 支持哪个 `claim_id`，以及不能证明什么。
- `claim ledger` 约束中心命题、机制句、行动建议、公共定性、文章转译和高风险概念判断。
- `concept contract` 防止责任链、开放断言、权力封闭、低条件行动等概念被当成口号或标签。
- `crossframe-review` 检查正文是否强于台账、生成层是否自我盖章、证据档位是否越界。
- `crossframe-inquiry` 在完整链路后复用上游台账和 review 结果，继续追问、反证、补证和迁移。

默认不展示内部 reasoning、工具调用参数、路径试错、错误栈或英文自我规划。用户可见输出只保留必要的推理提纲、证据边界、判断档位、结论和下一步。

---

<a id="skills"></a>
## Skill 地图

| Skill | 用途 |
| --- | --- |
| `crossframe-suite` | 总调度入口，决定连续工作流 |
| `crossframe` | 结构诊断核心层 |
| `crossframe-essay` | 把结构诊断转成完整中文文章 |
| `crossframe-review` | 审查推理、证据边界和输出质量 |
| `crossframe-dialogue` | 读者答复、编辑回信、咨询式短答 |
| `crossframe-casebook` | 把材料整理成可复用案例 |
| `crossframe-history` | 历史材料、史料边界、长时段制度问题 |
| `crossframe-public` | 公共议题、平台治理、政策和机构责任 |
| `crossframe-org` | 团队、项目和组织修复 |
| `crossframe-teach` | 概念讲解、误读纠偏和练习 |
| `crossframe-debate` | 命题辩论、正反结构和撤回条件 |
| `crossframe-notebook` | 读书、理论、文章和摘录研究笔记 |
| `crossframe-critical` | 点名调用的结构批判长文 |
| `crossframe-inquiry` | 完成态后的结构追问、反证、补证和迁移 |

---

<a id="docs"></a>
## 文档

| 文档 | 内容 |
| --- | --- |
| [WHAT_IS_CROSSFRAME.md](docs/WHAT_IS_CROSSFRAME.md) | 普通人版介绍 |
| [QUICKSTART.md](docs/QUICKSTART.md) | 5 分钟上手和验证命令 |
| [CONCEPTS.md](docs/CONCEPTS.md) | claim ledger、source ledger、concept contract、review、inquiry |
| [WORKFLOWS.md](docs/WORKFLOWS.md) | 常见任务链路 |
| [EXAMPLES.md](docs/EXAMPLES.md) | 精简输入、工作流和输出摘要 |
| [ADAPTERS.md](docs/ADAPTERS.md) | Codex、Claude、Cursor、Gemini、Copilot 等适配方式 |
| [SAFETY_AND_LIMITS.md](docs/SAFETY_AND_LIMITS.md) | 安全边界和公开发布限制 |
| [FAQ.md](docs/FAQ.md) | 常见问题 |
| [CHANGELOG.md](CHANGELOG.md) | 版本变更 |

---

<a id="principles"></a>
## 输出原则

CrossFrame 输出应当：

- 先给简短推理提纲，再给正式回答。
- 区分事实、解释、机制候选和判断档位。
- 不把结构诊断写成人格审判。
- 不把证据不足的判断写成已经闭合。
- 不把复杂问题压缩成口号、鸡汤或责任稀释。
- 面向普通中文读者，尽量少堆术语。
- 公共、机构、历史和现实事实相关内容必须保留证据边界。
- 文章输出要先有结构洞察，再进入正文。

---

## License

MIT License. See [LICENSE](LICENSE).
