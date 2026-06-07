---
name: crossframe-review
description: "CrossFrame Review explicit-only audit skill. Use only when the user explicitly names crossframe-review, $crossframe-review, /crossframe-review, or asks to use CrossFrame Review; do not trigger implicitly for ordinary reviews, critiques, audits, grading, smoke tests, or repair tasks. Suite-directed use after an explicit crossframe-suite invocation is allowed."
disable-model-invocation: true
---

# CrossFrame Review for Claude Code

Thin adapter. Read `skills/crossframe-review/SKILL.md` first, then follow its routed reads into `skills/crossframe/` and, for article reviews, `skills/crossframe-essay/`.

Default output: review object, fact boundary, triggered rules, grade, key failures, evidence locations, repair steps, and pass/fail.
