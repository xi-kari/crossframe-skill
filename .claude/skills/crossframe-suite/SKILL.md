---
name: crossframe-suite
description: |
  Use for complex CrossFrame tasks that need multiple sibling skills in sequence: essay after diagnosis, public commentary, organization repair writing, reader replies, debate-to-article, casebook extraction, reading notes, and review after generation.
---

# CrossFrame Suite for Claude Code

Thin adapter. Read `skills/crossframe-suite/SKILL.md` first, then follow `skills/crossframe-suite/references/workflow-routing-map.md`.

Default behavior: output a short dispatch outline, then read only the needed sibling skills. Do not trigger every `crossframe-*` skill at once.

For open-ended analysis without a specified artifact, default to `crossframe -> crossframe-essay -> crossframe-review` and produce a readable article-style answer. Do not generate an article for review, casebook, memo, table, checklist, action plan, or pure diagnosis requests.

For high-responsibility, public, intimate, long-evolution, deep-analysis, or article workflows, ensure the underlying `crossframe` step reads `skills/crossframe/references/continuity-bundles.md` and performs `skills/crossframe/worksheets/source-continuity-check.md` before generation or review.
