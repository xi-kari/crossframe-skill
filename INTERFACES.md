# 多接口适配说明

这个仓库的权威 skill 主体位于：

- `skills/crossframe/SKILL.md`

其他接口文件只是薄适配层，用来告诉不同 AI 工具如何读取与调用 CrossFrame。不要把完整协议复制成多份，以免内容漂移。

## 适配原则

- 中文为权威语义；`CrossFrame` 只是英文传播名与 skill id。
- 新增接口只负责入口、路由和最小约束。
- 若需要更新框架主体，优先更新 `skills/crossframe/`，再回填薄适配层。
- 用户可见输出默认先给推理提纲，再说人话。
- 高风险概念必须按需读取 `skills/crossframe/references/concept-cards/`，不要只按字面理解。
- 防失真材料以 `skills/crossframe/references/read-routing-map.md`、`skills/crossframe/references/v2-term-fidelity.md` 和 `skills/crossframe/worksheets/concept-fidelity-check.md` 为入口。
- 深水区模块以命题验证、高反身性、亲密关系轻量入口、疗愈转移、公共制度专项、框架边界、生命周期、递进闭环、势场解离、治理连续性、超大规模压力测试、表达翻译和理论后台索引为入口。
- `skills/crossframe/references/v2-coverage-map.md` 用于维护时核对 v2.0 覆盖状态，不作为普通输出材料。

## 当前支持的接口

| 接口 | 入口文件 | 说明 |
| --- | --- | --- |
| Codex | `skills/crossframe/` | 可直接用 skill-installer 安装 |
| Claude Code | `.claude/skills/crossframe/SKILL.md` + `.claude/commands/crossframe*.md` + `CLAUDE.md` | 自动触发 skill，也可调用 `/crossframe`、`/crossframe-explain`、`/crossframe-audit` |
| Gemini CLI | `GEMINI.md` | 仓库级上下文入口 |
| Cursor | `.cursor/rules/crossframe.mdc` + `AGENTS.md` | 规则文件与通用入口 |
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

- Codex：复制 `skills/crossframe/` 到 `$HOME/.codex/skills/crossframe`
- Claude Code：复制 `.claude/skills/crossframe/`、`.claude/commands/`、`CLAUDE.md`，并保留 `skills/crossframe/`
- Gemini CLI：复制 `GEMINI.md`，并保留 `skills/crossframe/`
- Cursor：复制 `.cursor/rules/crossframe.mdc` 或 `AGENTS.md`，并保留 `skills/crossframe/`
- GitHub Copilot：复制 `.github/copilot-instructions.md` 和 `AGENTS.md`
- Windsurf / Cascade：复制 `.windsurf/rules/crossframe.md`，并保留 `skills/crossframe/`
- Cline：复制 `.clinerules/crossframe.md`，并保留 `skills/crossframe/`
- Roo Code：复制 `.roo/rules/crossframe.md`，并保留 `skills/crossframe/`
- Continue：复制 `.continue/rules/crossframe.md`，并保留 `skills/crossframe/`
- Aider：复制 `CONVENTIONS.md` 和 `.aider.conf.yml`，并保留 `skills/crossframe/`

## 维护顺序

1. `skills/crossframe/SKILL.md`
2. `skills/crossframe/references/read-routing-map.md` 与 `references/v2-term-fidelity.md`
3. `skills/crossframe/references/theory-backend-index.md`
4. `skills/crossframe/references/v2-coverage-map.md`
5. `skills/crossframe/protocols/`
6. `skills/crossframe/worksheets/`
7. `skills/crossframe/templates/`
8. `skills/crossframe/references/concept-cards/`
9. `README.md`
10. `AGENTS.md`
11. `INTERFACES.md`
12. 其他接口入口文件
