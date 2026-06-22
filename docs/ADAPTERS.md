# 适配说明

| 工具 | 入口 | 推荐用法 | 注意事项 |
| --- | --- | --- | --- |
| Codex | `skills/crossframe*/` | 安装 14 个 skill 后显式点名 `crossframe-suite` | 不被动触发 |
| Claude Code | `.claude/skills/crossframe*/` + `.claude/commands/crossframe*.md` + `CLAUDE.md` | 使用 `/crossframe-suite`、`/crossframe-essay`、`/crossframe-history`、`/crossframe-inquiry` | 仓库命令和全局命令可同步 |
| Gemini CLI | `GEMINI.md` | 读取仓库级上下文后按 skill 路由 | 不要一次加载全部 skill |
| Cursor | `.cursor/rules/crossframe*.mdc` | 规则只做入口提示，主体仍读 `skills/` | `alwaysApply: false` |
| GitHub Copilot | `.github/copilot-instructions.md` | 仓库内文档分析和维护时使用 | 不能替代完整 skill 文件 |
| Windsurf / Cascade | `.windsurf/rules/crossframe.md` | 手动点名 CrossFrame 后使用 | 不做自动常驻规则 |
| Cline | `.clinerules/crossframe.md` | 项目规则入口 | 保持薄适配 |
| Roo Code | `.roo/rules/crossframe.md` | Workspace rule | 保持 explicit-only |
| Continue | `.continue/rules/crossframe.md` | Local rule | 只提示路由 |
| Aider | `CONVENTIONS.md` + `.aider.conf.yml` | 维护仓库时读取约定 | 不复制主体协议 |
| 通用 agent | `AGENTS.md` | 第一个入口文件 | 仍需回到 `skills/` |
| LLM 索引 | `llms.txt` | 机器可读入口 | 适合快速定位 |

如果工具不支持 skill 文件夹，也可以只读取 `AGENTS.md`、`CLAUDE.md`、`GEMINI.md` 或 `llms.txt`。但薄入口只负责路由，效果不如完整保留 `skills/crossframe*`。

所有薄适配都必须保留两条新路由：历史材料、史料边界和长时段制度问题进入 `crossframe-history`；完整分析、成文和 review 已完成后，下一轮未明确换题或退出的用户输入默认进入 `crossframe-inquiry`，并可定向检索 1-3 个 sibling skill 的必要材料。

维护镜像时运行：

```powershell
python scripts\sync_skill_mirrors.py --check
python scripts\sync_skill_mirrors.py
```

默认会同步仓库内 `skills/crossframe*` 到 `.claude/skills`。
