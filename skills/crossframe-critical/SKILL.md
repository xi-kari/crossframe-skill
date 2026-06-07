---
name: crossframe-critical
description: "CrossFrame Critical explicit-only skill for writing Chinese structural critique essays from a CrossFrame diagnosis, with sharper attention to cost chains, benefit chains, ideology, alienation, reproduction mechanisms, and rhetorical concealment. Use only when the user explicitly invokes $crossframe-critical, says crossframe-critical, or clearly asks to test this critical parallel skill; do not trigger implicitly for ordinary CrossFrame, essay, public, or review tasks."
disable-model-invocation: true
---

# CrossFrame Critical

This is a parallel local test skill. It does not replace `crossframe`, `crossframe-essay`, `crossframe-public`, or `crossframe-suite`.

## Position

`crossframe-critical` writes critical Chinese essays that first use CrossFrame to establish structure, evidence boundaries, scale, mechanism candidates, and judgment grade, then sharpen the output into critique.

The critique may absorb Marxist problem awareness: interests, cost transfer, alienation, commodification, ideology, naturalized domination, and reproduction of conditions. It must not mechanically force every topic into class/capital language.

## Required Reading

On every trigger, read:

1. `../crossframe/SKILL.md`
2. `../crossframe/references/read-routing-map.md`
3. `protocols/critical-article-protocol.md`
4. `references/critical-matrix.md`
5. `references/example-and-evidence-rules.md`
6. `templates/critical-output-template.md`

If the topic needs long-form style control, also read `../crossframe-essay/SKILL.md` and reuse only its article discipline, not its whole output contract.

## Workflow

1. Build the CrossFrame base: object, fact boundary, scale window, mechanism candidates, judgment grade, and evidence gaps.
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

- Start from CrossFrame structure, then become critical; do not begin from indignation and decorate it with structure words.
- Critique mechanisms, interests, rhetoric, institutions, and responsibility chains; do not turn structural critique into personal condemnation.
- A real or recent public event requires source checking before factual claims. Unverified examples must be labeled as analogy, hypothesis, or common pattern.
- Use at least two concrete examples in the essay body unless the user provides a single narrowly bounded case and asks not to expand.
- Include at least one countercondition, evidence gap, or withdrawal condition.
- Do not use Marxist terms as prestige vocabulary. If a term cannot be translated into who pays, who benefits, what is hidden, and how the condition repeats, remove it.
