# CrossFrame Agent Conventions

This repository is a publishable AI skill repo. The canonical implementation lives in `skills/crossframe/`.

When a user asks for CrossFrame、跨尺度结构诊断、结构诊断、推演、开放断言、反俘获审查、低条件试探行动、强判断、高反身性、亲密关系、疗愈转移、公共制度、长期演化或概念解释:

1. Read `skills/crossframe/SKILL.md`.
2. Read `skills/crossframe/references/read-routing-map.md`.
3. Load only the routed protocol, worksheet, concept card, and template.
4. Start the final answer with a short 推理提纲 unless the user explicitly asks for an ultra-short answer.
5. Speak plain Chinese first; use terms only as optional internal mapping.

Do not copy the full v2.0 text into adapters. Do not duplicate the full skill body across root instruction files. Keep adapters thin and point back to `skills/crossframe/`.

CrossFrame must not become personality judgment, fate prediction, professional advice replacement, responsibility dilution, or AI compliance theater.
