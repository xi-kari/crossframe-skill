# Claude Code 适配入口

@AGENTS.md

这个仓库提供 Claude Code 项目级 skill：

- `.claude/skills/crossframe/SKILL.md`
- `.claude/commands/crossframe.md`

在仓库根目录运行 `claude` 后，可以直接使用：

```text
/crossframe 帮我分析这个组织为什么复盘很多但没有真实修复
```

本文件保持轻量。若任务确实涉及 CrossFrame 使用、文档修订或适配层维护，再按需读取：

- `README.md`
- `skills/crossframe/SKILL.md`
- `skills/crossframe/references/read-routing-map.md`
- `skills/crossframe/references/v2-term-fidelity.md`
- `skills/crossframe/protocols/diagnosis-protocol.md`
- `skills/crossframe/templates/reasoning-outline-output.md`
- `skills/crossframe/templates/user-facing-language.md`
- `skills/crossframe/references/concept-cards/README.md`

额外约束：

- 中文为权威语义。
- 默认先给推理提纲，再输出人话判断。
- 不要把术语堆砌当成结构分析。
- 不要把开放断言写成终局审判。
- 使用高风险概念前，先读对应概念卡，并用概念保真检查避免压缩失真。
