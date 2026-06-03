# CrossFrame Rule

When a task mentions CrossFrame, 跨尺度结构诊断, 结构诊断, 推演, 开放断言, 反俘获, 低条件试探行动, 强判断, 高反身性, 亲密关系, 疗愈转移, 公共制度, 生命周期, 递进闭环, 势场解离, 治理连续性, 超大规模压力测试, or concept explanation, use the CrossFrame skill.

For complex tasks that require multiple CrossFrame sibling skills in sequence, use `skills/crossframe-suite/SKILL.md` first and follow `skills/crossframe-suite/references/workflow-routing-map.md`. Do not trigger all sibling skills at once.

Use `crossframe-suite` as the default CrossFrame entry. For open-ended analysis without a specified artifact, default to `crossframe -> crossframe-essay -> crossframe-review` and write a readable article-style answer. Do not generate an article for review, casebook, memo, table, checklist, action plan, or pure diagnosis requests.

When a task asks for 中文文章、长文、评论、思想文章、批判性洞察文章, or asks to turn CrossFrame reasoning into prose, use `skills/crossframe-essay/SKILL.md`. It must produce `结构洞察底稿` before `文章正文`. If the article needs concept elevation, classic references, theory, or allusion, read `skills/crossframe-essay/protocols/concept-elevation-protocol.md` and require verifiable direct quotes. If the user asks for 亲切、编辑、同志口吻、报刊答复 or advice, read `skills/crossframe-essay/protocols/editorial-comrade-voice-protocol.md`; do not let the voice become empty comfort, slogan, or personality judgment.

For review, dialogue, casebook, public issue, organization repair, concept teaching, debate, or notebook tasks, use the matching `skills/crossframe-*/SKILL.md` sibling skill before falling back to the generic CrossFrame rule.

Start from:

- `skills/crossframe/SKILL.md`
- `skills/crossframe/references/read-routing-map.md`

Then load the specific routed files. Always produce a short visible 推理提纲 before the user-facing answer. Use plain Chinese; do not dump concepts. For high-risk concepts, read the corresponding concept card and run the concept-fidelity check.


For v3.0 source fidelity, high-responsibility, public institution, intimate relationship, long-term evolution, deep analysis, AI compliance, weak-signal, no-institution, trapped-subject, toolization, or essay/article tasks must read `skills/crossframe/references/continuity-bundles.md`; when needed, read `skills/crossframe/references/v3-source-spine.md`, `skills/crossframe/references/v3-section-digest-index.md`, `skills/crossframe/references/v3-term-fidelity.md`, and run `skills/crossframe/worksheets/source-continuity-check.md`. Do not rely on one isolated concept card for these cases.

Hard limits: no personality judgment, no fate prediction, no responsibility dilution, no professional replacement, no AI compliance theater.

For philosophical/meaning questions such as 第一因, 生命是什么, 虚无主义, or 存在意义, first use concept explanation, scale decomposition, and a structural open assertion. Use framework boundary only as a fallback.
