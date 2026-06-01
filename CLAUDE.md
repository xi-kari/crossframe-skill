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
- `skills/crossframe/references/theory-backend-index.md`
- `skills/crossframe/references/v2-coverage-map.md`
- `skills/crossframe/protocols/framework-boundary-protocol.md`
- `skills/crossframe/protocols/lifecycle-diagnosis-protocol.md`
- `skills/crossframe/protocols/progression-protocol.md`
- `skills/crossframe/protocols/field-dissociation-protocol.md`
- `skills/crossframe/protocols/governance-continuity-protocol.md`
- `skills/crossframe/protocols/large-scale-stress-test-protocol.md`
- `skills/crossframe/protocols/expression-translation-protocol.md`
- `skills/crossframe/protocols/diagnosis-protocol.md`
- `skills/crossframe/protocols/proposition-verification-protocol.md`
- `skills/crossframe/protocols/high-reflexivity-protocol.md`
- `skills/crossframe/protocols/intimate-relationship-protocol.md`
- `skills/crossframe/protocols/healing-transfer-protocol.md`
- `skills/crossframe/protocols/public-institution-protocol.md`
- `skills/crossframe/templates/reasoning-outline-output.md`
- `skills/crossframe/templates/user-facing-language.md`
- `skills/crossframe/references/concept-cards/README.md`

额外约束：

- 中文为权威语义。
- 默认先给推理提纲，再输出人话判断。
- 不要把术语堆砌当成结构分析。
- 不要把开放断言写成终局审判。
- 使用高风险概念前，先读对应概念卡，并用概念保真检查避免压缩失真。
- 强判断、高反身性、亲密关系、疗愈转移、公共制度、框架边界、生命周期、递进、势场解离、治理连续性、超大规模压力测试和长期演化问题，必须按 `read-routing-map.md` 进入对应深水区模块。
