---
name: crossframe-suite
description: |
  Use for complex CrossFrame tasks that need multiple sibling skills in sequence: essay after diagnosis, public commentary, organization repair writing, reader replies, debate-to-article, casebook extraction, reading notes, and review after generation.
---

# CrossFrame Suite for Claude Code

Thin adapter. Read `skills/crossframe-suite/SKILL.md` first, then follow `skills/crossframe-suite/references/workflow-routing-map.md`.

Default behavior: output a short dispatch outline, then read only the needed sibling skills. Do not trigger every `crossframe-*` skill at once.

For any CrossFrame content task through Suite, finish the needed sibling skills first, then append `crossframe-essay -> crossframe-review` and use `full-visible-v3-longform`: complete visible 3.0 dossier plus complete long-form article with the modern editor-comrade base voice. Only skip the article layer when the user explicitly says only/no article/short answer/table/checklist/pure diagnosis/action plan only.

For high-responsibility, public, intimate, long-evolution, deep-analysis, or article workflows, ensure the underlying `crossframe` step reads `skills/crossframe/references/continuity-bundles.md` and performs `skills/crossframe/worksheets/source-continuity-check.md` before generation or review.
