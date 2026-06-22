# CrossFrame Skill Suite

CrossFrame Skill Suite is a Chinese structural diagnosis and writing skill suite for AI agents.

It is designed for tasks where a plain answer is not enough: complex relationships, teams, institutions, public disputes, historical materials, arguments, reader replies, research notes, and long-form Chinese essays.

The suite asks the agent to separate facts, evidence, scale, responsibility, mechanism, and expression before producing a readable answer.

## What It Does

- Diagnoses complex social, organizational, relational, and institutional situations.
- Turns structural analysis into readable Chinese essays, replies, reports, memos, and case notes.
- Reviews generated answers for evidence boundaries, overclaiming, source drift, and weak reasoning.
- Supports public-issue analysis, organization repair, debate analysis, historical-source handling, concept teaching, and research-note workflows.
- Preserves explicit invocation: CrossFrame should be used only when the user asks for it.

## When To Use It

Use CrossFrame when the user asks for one of these:

- structural diagnosis or cross-scale analysis
- public issue, platform governance, policy, or institutional responsibility analysis
- team, project, or organization repair
- relationship or responsibility-chain analysis
- historical materials, source-ledger boundaries, or archive/FOIA backlog handling
- argument testing, debate mapping, or withdrawal conditions
- turning analysis into a complete Chinese article
- reviewing whether an answer actually reasons from evidence
- follow-up inquiry after a completed analysis or article

Do not use it for simple factual lookup, arithmetic, ordinary chat, or tasks where the user did not ask for CrossFrame-style reasoning.

## Main Entry

For multi-step work, start with:

```text
crossframe-suite
```

The suite chooses the workflow and then routes to the needed specialist skills.

Common workflows:

```text
crossframe -> crossframe-review
crossframe -> crossframe-essay -> crossframe-review
crossframe -> crossframe-public -> crossframe-essay -> crossframe-review
crossframe -> crossframe-org -> crossframe-essay -> crossframe-review
crossframe -> crossframe-history -> crossframe-essay -> crossframe-review
crossframe -> crossframe-dialogue
crossframe -> crossframe-notebook
crossframe -> crossframe-inquiry
```

## Skill Areas

| Skill | Purpose |
| --- | --- |
| `crossframe-suite` | Workflow router for multi-step CrossFrame tasks |
| `crossframe` | Core structural diagnosis |
| `crossframe-essay` | Converts analysis into complete Chinese essays |
| `crossframe-review` | Checks reasoning, evidence boundaries, and output quality |
| `crossframe-dialogue` | Reader replies, editorial responses, and short consultation answers |
| `crossframe-casebook` | Turns materials into reusable case entries |
| `crossframe-history` | Historical materials, source ledgers, and archive/FOIA boundaries |
| `crossframe-public` | Public issues, institutions, platforms, policies, and compliance materials |
| `crossframe-org` | Team, project, and organization repair |
| `crossframe-teach` | Plain-language concept explanation and exercises |
| `crossframe-debate` | Proposition testing, opposing arguments, and withdrawal conditions |
| `crossframe-notebook` | Reading notes for books, theories, articles, and excerpts |
| `crossframe-critical` | Named-only long-form structural critique |
| `crossframe-inquiry` | Follow-up questions after a completed CrossFrame workflow |

## Output Principles

CrossFrame outputs should:

- show a concise reasoning outline before the final answer
- distinguish fact, interpretation, mechanism candidate, and judgment level
- avoid turning structural analysis into personality judgment
- avoid presenting uncertain claims as closure
- keep specialist terms mostly in the background and write for ordinary readers
- preserve evidence boundaries when discussing public, institutional, historical, or current events

## License

MIT License. See [LICENSE](LICENSE).
