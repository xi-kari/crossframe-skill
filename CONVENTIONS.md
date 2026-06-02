# CrossFrame Agent Conventions

This repository is a publishable AI skill repo. The canonical implementations live in `skills/crossframe/` and `skills/crossframe-essay/`.

When a user asks for CrossFrame、跨尺度结构诊断、结构诊断、推演、开放断言、反俘获审查、低条件试探行动、强判断、高反身性、亲密关系、疗愈转移、公共制度、长期演化或概念解释:

1. Read `skills/crossframe/SKILL.md`.
2. Read `skills/crossframe/references/read-routing-map.md`.
3. Load only the routed protocol, worksheet, concept card, and template.
4. Start the final answer with a short 推理提纲 unless the user explicitly asks for an ultra-short answer.
5. Speak plain Chinese first; use terms only as optional internal mapping.

Do not copy the full v2.0 text into adapters. Do not duplicate the full skill body across root instruction files. Keep adapters thin and point back to `skills/crossframe/` and `skills/crossframe-essay/`.

CrossFrame must not become personality judgment, fate prediction, professional advice replacement, responsibility dilution, or AI compliance theater.

When a user asks for 中文文章、长文、评论、思想文章、批判性洞察文章 or structure-to-essay writing:

1. Read `skills/crossframe-essay/SKILL.md`.
2. Read `skills/crossframe/SKILL.md` and `skills/crossframe/references/read-routing-map.md`.
3. Build a `结构洞察底稿` before writing the article body.
4. Use search only for public/current/real-world evidence boundaries and examples; do not let sources decide the thesis.
5. When depth, concept elevation, 引经据典, or theory references are needed, read `skills/crossframe-essay/protocols/concept-elevation-protocol.md` and `skills/crossframe-essay/references/reference-and-allusion-rules.md`.
6. Direct quotes must be verifiable; uncertain source text should be paraphrased or mapped as a thought tradition.
7. Write plain Chinese for ordinary readers and keep CrossFrame terms mostly in the backend.
