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

## 当前支持的接口

| 接口 | 入口文件 | 说明 |
| --- | --- | --- |
| Codex | `skills/crossframe/` | 可直接用 skill-installer 安装 |
| Claude Code | `.claude/skills/crossframe/SKILL.md` + `.claude/commands/crossframe.md` + `CLAUDE.md` | 仓库内直接调用 `/crossframe` |
| Gemini CLI | `GEMINI.md` | 仓库级上下文入口 |
| Cursor | `.cursor/rules/crossframe.mdc` + `AGENTS.md` | 规则文件与通用入口 |
| GitHub Copilot | `.github/copilot-instructions.md` | 仓库级说明 |
| 通用 agent | `AGENTS.md` | 默认入口 |

## 迁移到别的项目

如果要把 CrossFrame 带到另一个项目：

- Codex：复制 `skills/crossframe/` 到 `$HOME/.codex/skills/crossframe`
- Claude Code：复制 `.claude/skills/crossframe/`、`.claude/commands/crossframe.md`、`CLAUDE.md`，并保留 `skills/crossframe/`
- Gemini CLI：复制 `GEMINI.md`，并保留 `skills/crossframe/`
- Cursor：复制 `.cursor/rules/crossframe.mdc` 或 `AGENTS.md`，并保留 `skills/crossframe/`
- GitHub Copilot：复制 `.github/copilot-instructions.md` 和 `AGENTS.md`

## 维护顺序

1. `skills/crossframe/SKILL.md`
2. `skills/crossframe/protocols/`
3. `skills/crossframe/worksheets/`
4. `skills/crossframe/templates/`
5. `skills/crossframe/references/concept-cards/`
6. `README.md`
7. `AGENTS.md`
8. 其他接口入口文件
