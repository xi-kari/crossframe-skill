---
name: crossframe-suite
description: "CrossFrame Suite explicit-only router. Use only when the user explicitly names crossframe-suite, $crossframe-suite, /crossframe-suite, or asks to use the CrossFrame suite; do not trigger implicitly for ordinary analysis, writing, public, organization, debate, teaching, reading, or review tasks. After explicit invocation, it routes sibling CrossFrame skills and decides where to stop."
disable-model-invocation: true
---

# CrossFrame Suite for Claude Code

Thin adapter. Read `skills/crossframe-suite/SKILL.md` first, then follow `skills/crossframe-suite/references/workflow-routing-map.md`.

Default behavior: output a short dispatch outline, then read only the needed sibling skills. Do not trigger every `crossframe-*` skill at once.

For any CrossFrame content task through Suite, finish the needed sibling skills first, then append `crossframe-essay -> crossframe-review` and use `full-visible-v3-longform`: complete visible 3.0 dossier plus complete long-form article with the modern editor-comrade base voice. Only skip the article layer when the user explicitly says only/no article/short answer/table/checklist/pure diagnosis/action plan only.

For high-responsibility, public, intimate, long-evolution, deep-analysis, or article workflows, ensure the underlying `crossframe` step reads `skills/crossframe/references/integrity-check.md` before generation or review. Use `continuity-bundles.md` and `source-continuity-check.md` only when an expanded audit is needed.
