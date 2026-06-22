# Changelog

## v5.1.1 - 2026-06-22

### Changed

- Cursor、Continue、Cline、Roo、Windsurf、Copilot 和通用适配入口补齐 `crossframe-history` 与完成态 `crossframe-inquiry` 路由。
- 完整链路完成后，未明确换题或退出的下一轮用户输入默认进入 `crossframe-inquiry`；追问层可定向检索 1-3 个 sibling skill 的必要材料。
- 对外说明统一使用 `full-visible-v5-longform`，不再使用容易误判为旧版的混合长文叫法。

### Verification

- 完整性校验新增适配入口断裂检查、旧叫法禁用检查和 history/inquiry 覆盖检查。

## v5.1.0 - 2026-06-22

### Added

- 面向普通用户的 `docs/` 文档层：快速开始、概念说明、工作流、样例、适配、安全边界和 FAQ。
- `scripts/sync_skill_mirrors.py`：同步 `skills/crossframe*` 到 `.claude/skills` 等镜像。
- `scripts/package_crossframe_skill.py`：生成公开发布 zip。

### Changed

- README 改为面向大众的入口页，详细说明迁移到 `docs/`。
- 公开验证命令默认使用 `--materials-only`，不依赖维护者本机私有 DOCX 路径。
- Suite 与适配入口明确禁止向用户暴露内部 reasoning、工具调用参数、路径试错、错误栈或英文自我规划。

### Removed

- 旧 v2 连续性脚本不再作为公开维护入口。

## v5.0.2 - 2026-06-22

### Added

- `crossframe-history`：历史材料、史料边界、长时段制度问题和 archive/FOIA backlog 接口层。
- `crossframe-inquiry`：完成态后的结构追问层，支持反证、补证、迁移应用和行动边界确认。
- `claim ledger`、`concept contract`、`source_id -> claim_id` 回指和正文强于台账回扫。
- Claude、Cursor、Gemini、Copilot、Windsurf、Cline、Roo、Continue、Aider 和通用 agent 的 14-skill 薄适配。

### Changed

- Suite 默认链路加入 read-state capsule、source-anchor 检查、claim-ledger-check、review 和 completion inquiry 接管。
- 来源台账升级为十字段口径，要求稳定 `source_id` 和“支持的 `claim_id` / 命题”。
- `crossframe-review(lite)` 明确为 `crossframe-review` 的轻量用法，不再作为独立 skill 名称。
- 运行时不再使用旧 `integrity-check.md` 入口。
- 运行时不再使用 `five-gates-worksheet.md`。

## v5.0.1 - 2026-06-15

- 发布旧稳定版 CrossFrame Skill Suite。
- 包含 suite、core、essay、review、public、org、debate、critical、dialogue、casebook、notebook、teach 等早期 skill。
