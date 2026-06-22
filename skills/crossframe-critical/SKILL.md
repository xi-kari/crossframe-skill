---
name: crossframe-critical
description: 经由 crossframe-suite 调度使用，不独立响应。写中文结构批判文章的并行测试 skill。 Suite-directed use is allowed after explicit crossframe-suite invocation when the task asks for structural critique, critical essay, ideology/cost-transfer/benefit-chain analysis, or explicitly names crossframe-critical. Do not trigger from ordinary CrossFrame, essay, public, or review tasks without suite routing.
trigger: suite-only
---

# CrossFrame Critical


> **本 skill 不独立触发。** 所有 CrossFrame 任务统一从 `crossframe-suite` 入口调度。用户无需直接调用本 skill；suite 根据路由规则在需要时自动加载。

This is a parallel local test skill. It does not replace `crossframe`, `crossframe-essay`, `crossframe-public`, or `crossframe-suite`.

## Position

`crossframe-critical` writes critical Chinese essays that first use CrossFrame to establish structure, evidence boundaries, scale, mechanism candidates, and judgment grade, then sharpen the output into critique.

The critique may absorb Marxist problem awareness: interests, cost transfer, alienation, commodification, ideology, naturalized domination, and reproduction of conditions. It must not mechanically force every topic into class/capital language.

## Required Reading

On every trigger, read:

1. `../crossframe/SKILL.md`
2. `../crossframe/references/read-routing-map.md`
3. If the critique touches high-responsibility, public, AI/process artifact, lifecycle, trapped-subject, or article-output scenarios, reuse `../crossframe/templates/read-state-capsule.md` as `v5-read-state-capsule` and run `../crossframe/worksheets/source-anchor-integrity-check.md`; if the capsule is missing, return to `../crossframe/SKILL.md` instead of inventing source routing here.
- 若本 skill 产生新的中心命题、机制句、高风险概念判断、公共定性、行动建议、案例复用判断、组织处置建议或可成文材料，必须把这些内容作为 `claim ledger delta` 交回 `../crossframe/templates/claim-ledger.md` 与 `../crossframe/worksheets/claim-ledger-check.md`。本 skill 不得新增未登记判断；若无法登记 `claim_id`、判断档位、行动上限、撤回条件和发布边界，只能删除、降档，或标为“本文推断 / 表达转译 / 外部思想映射”。
- `crossframe-critical` 写正文前必须生成或复用 `claim ledger`；批判矩阵、例子、利益链、成本转移、意识形态分析和点睛句只能绑定已有 `claim_id`。没有 `claim_id` 的批判句不得进入正文。
4. `protocols/critical-article-protocol.md`
5. `references/critical-matrix.md`
6. `references/example-and-evidence-rules.md`
7. 若涉及真实公共对象、最新事实、机构、平台、政策、人物、公司、数据、AI/过程性产物或强判断，读取 `../crossframe/references/source-ledger-workflow.md` 并建立来源台账。
8. `templates/critical-output-template.md`

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
- A real or recent public event requires source checking before factual claims, with a visible source ledger summary. Unverified examples must be labeled as analogy, hypothesis, or common pattern.
- Use at least two concrete examples in the essay body unless the user provides a single narrowly bounded case and asks not to expand.
- Include at least one countercondition, evidence gap, or withdrawal condition.
- Do not use Marxist terms as prestige vocabulary. If a term cannot be translated into who pays, who benefits, what is hidden, and how the condition repeats, remove it.
