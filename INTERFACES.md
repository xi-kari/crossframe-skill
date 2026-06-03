# 多接口适配说明

这个仓库的权威 skill 主体位于：

- `skills/crossframe/SKILL.md`
- `skills/crossframe-suite/SKILL.md`
- `skills/crossframe-essay/SKILL.md`
- `skills/crossframe-review/SKILL.md`
- `skills/crossframe-dialogue/SKILL.md`
- `skills/crossframe-casebook/SKILL.md`
- `skills/crossframe-public/SKILL.md`
- `skills/crossframe-org/SKILL.md`
- `skills/crossframe-teach/SKILL.md`
- `skills/crossframe-debate/SKILL.md`
- `skills/crossframe-notebook/SKILL.md`

`crossframe-suite` 负责复杂任务的连续调度；`crossframe` 负责结构诊断；`crossframe-essay` 负责把结构诊断转成中文批判性洞察文章；其它 `crossframe-*` 负责评审、答复、案例、公共议题、组织修复、教学、辩论和研究笔记。其他接口文件只是薄适配层，用来告诉不同 AI 工具如何读取与调用这些 skill。不要把完整协议复制成多份，以免内容漂移。

## 适配原则

- 中文为权威语义；`CrossFrame` 只是英文传播名与 skill id。
- 新增接口只负责入口、路由和最小约束。
- 多 skill 连续任务先读取 `skills/crossframe-suite/SKILL.md`；suite 只调度，不替代专项 skill。
- `crossframe-suite` 是推荐默认入口；开放式分析且未指定交付物时，默认走 `crossframe -> crossframe-essay -> crossframe-review` 输出可读文章。
- 明确要求评审、案例库、组织备忘录、反馈写回方案、命题辩论表、概念教学练习、来源台账、表格、清单、一句话结论、低条件行动方案或纯诊断时，不要擅自生成文章。
- 若需要更新框架主体，优先更新 `skills/crossframe/`，再回填薄适配层。
- 若需要更新文章写作主体，优先更新 `skills/crossframe-essay/`，并确认它仍通过相对路径读取 `skills/crossframe/`。
- 若需要更新平行专项主体，优先更新对应 `skills/crossframe-*/`，并确认它仍通过相对路径读取 `skills/crossframe/`。
- 用户可见输出默认先给推理提纲，再说人话。
- 文章输出默认先给 `结构洞察底稿`，再给 `文章正文`；从 `crossframe-suite` 默认成文时默认启用现代编辑底色；需要深度时可按需加入概念上升和中西经典/理论参照。
- 直接引用必须可核验；不确定原句时只做意译、典故或思想映射。
- 现代编辑同志口吻是前台声口层，不改变结构判断；亲切不能和稀泥，严厉不能人格审判。
- 高风险概念必须按需读取 `skills/crossframe/references/concept-cards/`，不要只按字面理解。
- 防失真材料以 `skills/crossframe/references/read-routing-map.md`、`skills/crossframe/references/v3-term-fidelity.md`、`skills/crossframe/references/continuity-bundles.md`、`skills/crossframe/references/v3-source-spine.md`、`skills/crossframe/references/v3-section-digest-index.md`、`skills/crossframe/worksheets/concept-fidelity-check.md` 和 `skills/crossframe/worksheets/source-continuity-check.md` 为入口。
- 高责任、公共制度、亲密关系、长期演化、深度分析和文章输出场景，不能只读单张概念卡；必须检查对应 3.0 连续联读包。
- 深水区模块以命题验证、高反身性、亲密关系轻量入口、疗愈转移、公共制度专项、框架边界、生命周期、递进闭环、势场解离、治理连续性、超大规模压力测试、表达翻译和理论后台索引为入口。
- `skills/crossframe/references/v3-coverage-map.md` 用于维护时核对 v3.0 覆盖状态，不作为普通输出材料。

## 当前支持的接口

| 接口 | 入口文件 | 说明 |
| --- | --- | --- |
| Codex | `skills/crossframe*/` | 可直接用 skill-installer 安装；复杂任务优先触发 `crossframe-suite` |
| Claude Code | `.claude/skills/crossframe*/SKILL.md` + `.claude/commands/crossframe*.md` + `CLAUDE.md` | 自动触发 skill，也可调用 `/crossframe`、`/crossframe-explain`、`/crossframe-audit`、`/crossframe-essay` |
| Gemini CLI | `GEMINI.md` | 仓库级上下文入口 |
| Cursor | `.cursor/rules/crossframe-suite.mdc` + `.cursor/rules/crossframe.mdc` + `.cursor/rules/crossframe-essay.mdc` + `AGENTS.md` | 规则文件与通用入口 |
| GitHub Copilot | `.github/copilot-instructions.md` | 仓库级说明 |
| Windsurf / Cascade | `.windsurf/rules/crossframe.md` + `AGENTS.md` | Workspace rule，支持手动 `@crossframe` 或自动规则场景 |
| Cline | `.clinerules/crossframe.md` | Project rule |
| Roo Code | `.roo/rules/crossframe.md` | Workspace-wide rule |
| Continue | `.continue/rules/crossframe.md` | Local rule |
| Aider | `CONVENTIONS.md` + `.aider.conf.yml` | 自动读取 conventions |
| LLM 索引 | `llms.txt` | 机器可读入口索引 |
| 通用 agent | `AGENTS.md` | 默认入口 |

## 迁移到别的项目

如果要把 CrossFrame 带到另一个项目：

- Codex：复制所有 `skills/crossframe*/` 到 `$HOME/.codex/skills/`
- Claude Code：复制 `.claude/skills/crossframe*/`、`.claude/commands/`、`CLAUDE.md`，并保留所有 `skills/crossframe*/`
- Gemini CLI：复制 `GEMINI.md`，并保留所有 `skills/crossframe*/`
- Cursor：复制 `.cursor/rules/crossframe*.mdc` 或 `AGENTS.md`，并保留所有 `skills/crossframe*/`
- GitHub Copilot：复制 `.github/copilot-instructions.md` 和 `AGENTS.md`，并保留所有 `skills/crossframe*/`
- Windsurf / Cascade：复制 `.windsurf/rules/crossframe.md`，并保留所有 `skills/crossframe*/`
- Cline：复制 `.clinerules/crossframe.md`，并保留所有 `skills/crossframe*/`
- Roo Code：复制 `.roo/rules/crossframe.md`，并保留所有 `skills/crossframe*/`
- Continue：复制 `.continue/rules/crossframe.md`，并保留所有 `skills/crossframe*/`
- Aider：复制 `CONVENTIONS.md` 和 `.aider.conf.yml`，并保留所有 `skills/crossframe*/`

## 维护顺序

1. `skills/crossframe-suite/SKILL.md` 与 `skills/crossframe-suite/references/workflow-routing-map.md`
2. `skills/crossframe/SKILL.md`
3. `skills/crossframe/references/read-routing-map.md`、`references/v3-term-fidelity.md`、`references/continuity-bundles.md`、`references/v3-source-spine.md`
4. `skills/crossframe-essay/SKILL.md`
5. 各 `skills/crossframe-*/SKILL.md`
6. 各 `skills/crossframe-*/protocols/` 与 `references/`
7. `skills/crossframe/references/theory-backend-index.md`
8. `skills/crossframe/references/v3-coverage-map.md`
9. `skills/crossframe/protocols/`
10. `skills/crossframe/worksheets/`
11. `skills/crossframe/templates/`
12. `skills/crossframe/references/concept-cards/`
13. `README.md`
14. `AGENTS.md`
15. `INTERFACES.md`
16. 其他接口入口文件
