---

name: crossframe-v5-critical
description: 经由 crossframe-v5-suite 调度使用，不独立响应。写中文结构批判文章的并行测试 skill。 Use only when the user explicitly invokes `$crossframe-v5-critical`, says "crossframe-v5-critical", or clearly asks to test this critical parallel skill; do not trigger implicitly for ordinary CrossFrame v5, essay, public, or review tasks.
metadata:
  trigger: suite-only
---

# CrossFrame v5 Critical


> **本 skill 不独立触发。** 所有 CrossFrame v5 任务统一从 `crossframe-v5-suite` 入口调度。用户无需直接调用本 skill；suite 根据路由规则在需要时自动加载。

This is a parallel local test skill. It does not replace `crossframe-v5`, `crossframe-v5-essay`, `crossframe-v5-public`, or `crossframe-v5-suite`.

## Position

`crossframe-v5-critical` writes critical Chinese essays that first use CrossFrame v5 to establish structure, evidence boundaries, scale, mechanism candidates, and judgment grade, then sharpen the output into critique.

The critique may absorb Marxist problem awareness: interests, cost transfer, alienation, commodification, ideology, naturalized domination, and reproduction of conditions. It must not mechanically force every topic into class/capital language.

## Required Reading

On every trigger, read:

1. `../crossframe-v5/SKILL.md`
2. `../crossframe-v5/references/read-routing-map.md`
3. `protocols/critical-article-protocol.md`
4. `references/critical-matrix.md`
5. `references/example-and-evidence-rules.md`
6. `templates/critical-output-template.md`

If the topic needs long-form style control, also read `../crossframe-v5-essay/SKILL.md` and reuse only its article discipline, not its whole output contract.

## Workflow

1. Build the CrossFrame v5 base: object, fact boundary, scale window, mechanism candidates, judgment grade, and evidence gaps.
2. Apply the critical matrix: cost chain, benefit chain, power/resource distribution, concept concealment, reproduction mechanism, weak signals, and counterconditions.
3. Plan the article: central thesis, reader position, examples, section sequence, word allocation, and ending aftertaste.
4. Write the full essay from the dossier. Default body length is 1800-2800 Chinese characters unless the user overrides it.
5. Run a final boundary check: no personality judgment, no hat-labeling, no conspiracy claim, no unverified strong judgment, no slogan replacing analysis.

## Output

Default output has exactly three visible sections:

```text
# 批判底稿
# 篇章方案
# 正文
```

Do not collapse the result into a short answer, checklist, memo, or diagnosis summary unless the user explicitly asks for that.

## Hard Rules

- Start from CrossFrame v5 structure, then become critical; do not begin from indignation and decorate it with structure words.
- Critique mechanisms, interests, rhetoric, institutions, and responsibility chains; do not turn structural critique into personal condemnation.
- A real or recent public event requires source checking before factual claims. Unverified examples must be labeled as analogy, hypothesis, or common pattern.
- Use at least two concrete examples in the essay body unless the user provides a single narrowly bounded case and asks not to expand.
- Include at least one countercondition, evidence gap, or withdrawal condition.
- Do not use Marxist terms as prestige vocabulary. If a term cannot be translated into who pays, who benefits, what is hidden, and how the condition repeats, remove it.


## v5 连读要求

本专项 skill 不独立决定源结构。进入本 skill 前，必须已经由 `crossframe-v5-suite` 和 `../crossframe-v5/references/read-routing-map.md` 选定 v5 连读包；输出前必须回到 `../crossframe-v5/references/integrity-check.md` 做完整性检查。不得只读本 skill 或单张 concept card 就输出强判断。
