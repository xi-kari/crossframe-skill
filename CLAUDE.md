# Claude Code 适配入口

@AGENTS.md

这个仓库提供 Claude Code 项目级 skill：

- `.claude/skills/crossframe/SKILL.md`
- `.claude/skills/crossframe-suite/SKILL.md`
- `.claude/skills/crossframe-essay/SKILL.md`
- `.claude/skills/crossframe-review/SKILL.md`
- `.claude/skills/crossframe-dialogue/SKILL.md`
- `.claude/skills/crossframe-casebook/SKILL.md`
- `.claude/skills/crossframe-public/SKILL.md`
- `.claude/skills/crossframe-org/SKILL.md`
- `.claude/skills/crossframe-teach/SKILL.md`
- `.claude/skills/crossframe-debate/SKILL.md`
- `.claude/skills/crossframe-notebook/SKILL.md`
- `.claude/commands/crossframe.md`
- `.claude/commands/crossframe-suite.md`
- `.claude/commands/crossframe-explain.md`
- `.claude/commands/crossframe-audit.md`
- `.claude/commands/crossframe-essay.md`
- `.claude/commands/crossframe-review.md`
- `.claude/commands/crossframe-dialogue.md`
- `.claude/commands/crossframe-casebook.md`
- `.claude/commands/crossframe-public.md`
- `.claude/commands/crossframe-org.md`
- `.claude/commands/crossframe-teach.md`
- `.claude/commands/crossframe-debate.md`
- `.claude/commands/crossframe-notebook.md`

在仓库根目录运行 `claude` 后，可以直接使用：

```text
/crossframe 帮我分析这个组织为什么复盘很多但没有真实修复
/crossframe-suite 写一篇公共评论文章，并安排诊断、查源、成文和评审顺序
/crossframe-explain 解释一下虚无主义
/crossframe-audit 检查这个高责任判断能不能公开
/crossframe-essay 写一篇“团队越复盘越失真”的批判性洞察文章
/crossframe-review 评审这段输出有没有真的推理
/crossframe-dialogue 像编辑回信一样回答这个读者问题
/crossframe-casebook 把这些复盘材料整理成案例库
/crossframe-public 分析这个平台申诉机制是否只是表面治理
/crossframe-org 给这个项目失败写组织修复备忘录
/crossframe-teach 用人话解释开放断言
/crossframe-debate 检验这个命题的正反结构和撤回条件
/crossframe-notebook 读这篇文章，写与 CrossFrame 的关联与不同
```

本文件保持轻量。若任务确实涉及 CrossFrame 使用、文档修订或适配层维护，再按需读取：

- `README.md`
- `skills/crossframe-suite/SKILL.md`
- `skills/crossframe-suite/references/workflow-routing-map.md`
- `skills/crossframe/SKILL.md`
- `skills/crossframe-essay/SKILL.md`
- `skills/crossframe/references/read-routing-map.md`
- `skills/crossframe/references/continuity-bundles.md`
- `skills/crossframe/references/v3-source-spine.md`
- `skills/crossframe/references/v3-section-digest-index.md`
- `skills/crossframe/references/v3-term-fidelity.md`
- `skills/crossframe/references/theory-backend-index.md`
- `skills/crossframe/references/v3-coverage-map.md`
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
- `skills/crossframe-review/SKILL.md`
- `skills/crossframe-dialogue/SKILL.md`
- `skills/crossframe-casebook/SKILL.md`
- `skills/crossframe-public/SKILL.md`
- `skills/crossframe-org/SKILL.md`
- `skills/crossframe-teach/SKILL.md`
- `skills/crossframe-debate/SKILL.md`
- `skills/crossframe-notebook/SKILL.md`

额外约束：

- 中文为权威语义。
- 默认先给推理提纲，再输出人话判断。
- 不要把术语堆砌当成结构分析。
- 不要把开放断言写成终局审判。
- 使用高风险概念前，先读对应概念卡，并用概念保真检查避免压缩失真。
- 高责任、公共制度、亲密关系、长期演化、深度分析和文章输出，还要读取连续联读包，并用源结构连续性检查避免只读单概念卡导致 3.0 失真。
- 强判断、高反身性、亲密关系、疗愈转移、公共制度、框架边界、生命周期、递进、势场解离、治理连续性、超大规模压力测试和长期演化问题，必须按 `read-routing-map.md` 进入对应深水区模块。
- 当用户要写文章、长文、评论、思想文章或批判性洞察文章时，使用 `crossframe-essay`：先形成 `结构洞察底稿`，再写 `文章正文`；需要深度时按需概念上升和引入中西经典/理论参照，但引用必须可核验并回到现实责任链。
- `crossframe-essay` 自动成文默认读取现代编辑口吻协议：问题型主题用答复体，公共评论、思想文章和概念文章用评论体；只有用户明确要求中性报告、备忘录、表格、清单、纯诊断或学术摘要时才关闭。不要口号化，不要把亲切写成和稀泥，也不要把严厉写成人格审判。
- 当用户要求评审、短答复、案例库、公共议题、组织修复、概念教学、命题辩论或研究笔记时，优先使用对应 `crossframe-*` 平行 skill；所有平行 skill 仍须读取 `skills/crossframe/SKILL.md` 与 `skills/crossframe/references/read-routing-map.md`。
- 默认优先考虑 `crossframe-suite` 作为总入口。当用户任务需要多个 CrossFrame skill 连续协作时，先用 `crossframe-suite` 决定顺序；常见链路包括 `crossframe -> crossframe-public -> crossframe-essay -> crossframe-review`、`crossframe -> crossframe-org -> crossframe-essay -> crossframe-review`、`crossframe -> crossframe-notebook -> crossframe-essay -> crossframe-review`。不要一次读取全部 skill。
- 当用户没有指定交付物，只是要求开放式分析、怎么看、讲讲或写一下时，suite 默认输出带现代编辑底色的可读文章或文章式回答：`crossframe -> crossframe-essay -> crossframe-review`。用户明确要评审、案例库、备忘录、表格、清单、行动方案或纯诊断时，不要擅自生成文章。
