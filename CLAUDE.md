# Claude Code 适配入口

@AGENTS.md

这个仓库提供 Claude Code 项目级 skill：

- `.claude/skills/crossframe/SKILL.md`
- `.claude/skills/crossframe-essay/SKILL.md`
- `.claude/commands/crossframe.md`
- `.claude/commands/crossframe-explain.md`
- `.claude/commands/crossframe-audit.md`
- `.claude/commands/crossframe-essay.md`

在仓库根目录运行 `claude` 后，可以直接使用：

```text
/crossframe 帮我分析这个组织为什么复盘很多但没有真实修复
/crossframe-explain 解释一下虚无主义
/crossframe-audit 检查这个高责任判断能不能公开
/crossframe-essay 写一篇“团队越复盘越失真”的批判性洞察文章
```

本文件保持轻量。若任务确实涉及 CrossFrame 使用、文档修订或适配层维护，再按需读取：

- `README.md`
- `skills/crossframe/SKILL.md`
- `skills/crossframe-essay/SKILL.md`
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
- `skills/crossframe-essay/protocols/essay-protocol.md`
- `skills/crossframe-essay/protocols/interactive-drafting-protocol.md`
- `skills/crossframe-essay/references/evidence-and-search-rules.md`
- `skills/crossframe-essay/references/critical-insight-principles.md`
- `skills/crossframe-essay/protocols/concept-elevation-protocol.md`
- `skills/crossframe-essay/references/reference-and-allusion-rules.md`
- `skills/crossframe-essay/references/concept-reference-map.md`
- `skills/crossframe-essay/protocols/editorial-comrade-voice-protocol.md`
- `skills/crossframe-essay/references/editorial-voice-principles.md`
- `skills/crossframe-essay/templates/insight-dossier-template.md`
- `skills/crossframe-essay/templates/essay-output-template.md`

额外约束：

- 中文为权威语义。
- 默认先给推理提纲，再输出人话判断。
- 不要把术语堆砌当成结构分析。
- 不要把开放断言写成终局审判。
- 使用高风险概念前，先读对应概念卡，并用概念保真检查避免压缩失真。
- 强判断、高反身性、亲密关系、疗愈转移、公共制度、框架边界、生命周期、递进、势场解离、治理连续性、超大规模压力测试和长期演化问题，必须按 `read-routing-map.md` 进入对应深水区模块。
- 当用户要写文章、长文、评论、思想文章或批判性洞察文章时，使用 `crossframe-essay`：先形成 `结构洞察底稿`，再写 `文章正文`；需要深度时按需概念上升和引入中西经典/理论参照，但引用必须可核验并回到现实责任链。
- 当用户要求亲切、编辑、同志口吻、报刊答复、耐心解答或给意见时，`crossframe-essay` 还要读取现代编辑口吻协议：问题型主题可用答复体，普通评论只吸收亲切、负责、果敢的声口；不要口号化，不要把亲切写成和稀泥，也不要把严厉写成人格审判。
