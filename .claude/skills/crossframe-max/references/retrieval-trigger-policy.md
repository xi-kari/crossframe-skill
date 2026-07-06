# CrossFrame Max Retrieval Trigger Policy

This policy defines when `crossframe-max` must search beyond memory and full-source.

It separates two retrieval types:

- internal concept retrieval: searching CrossFrame source files and registry for concept fidelity
- external fact retrieval: searching outside the skill for real-world facts, current context, counterevidence, and source material

## Runtime Rule

Use `retrieval-trigger-policy` before final output and whenever a new strong claim appears.

Do not use retrieval as decoration. Retrieval must change one of these:

- source frontier
- claim ledger
- evidence-reasoning audit
- path confidence layer
- withdrawal or downgrade condition
- continuation index

## Internal Concept Retrieval

Internal concept retrieval is mandatory when:

1. A user uses a CrossFrame term, near term, or renamed concept.
2. The analysis introduces a core concept, root assumption, state coordinate, gate, or intervention path.
3. A concept is used to justify a strong judgment.
4. Multiple concepts can explain the same signal.
5. The model feels it "remembers" a concept but has not cited paragraph ids.

Required chain:

```text
structural variable -> concept-registry lookup -> full-source paragraph read -> concept contract -> claim ledger
```

If the concept is absent from registry, search full-source, cite the paragraph ids, and record `concept-registry gap`.

## External Retrieval Trigger Conditions

External retrieval is mandatory when any of the following is true:

1. The object involves a real person, organization, company, school, platform, institution, policy, law, rule, event, public controversy, product, technical standard, or current situation.
2. The user asks for latest, current, today, recent, verify, search, source, quote, citation, evidence, or comparison.
3. A center claim depends on facts not present in the user material.
4. A path prediction depends on timeline, rule, policy, market, legal, platform, technical, or institutional context.
5. The output may be used for public posting, appeal, governance, accusation, organizational action, relationship decision, or high-impact judgment.
6. User material is one-sided, promotional, self-reporting, anonymous, emotionally charged, or missing affected positions.
7. The evidence-reasoning audit finds a missing source, conflict, unsupported causal link, or high-impact strong judgment.
8. The red-team pass asks what would falsify the explanation.

## Reverse Retrieval Is Mandatory When

For every center claim and strong judgment, search for:

- counterexample
- opposite explanation
- failed case
- affected-position account
- low-power subject signal
- timeline contradiction
- source controlled by an interested party
- expert disagreement or rule exception

If reverse retrieval is impossible, register that impossibility. Do not treat absence of found evidence as evidence of absence.

## Do Not Trigger External Retrieval When

External retrieval may be skipped only when all of these hold:

1. The object is fictional, hypothetical, purely conceptual, or fully supplied by the user.
2. No real-world fact, public claim, institutional rule, current status, or external accusation is needed.
3. The output will not be used as a strong public or action-guiding judgment.
4. The evidence-reasoning audit can stay inside user material plus full-source.

Even then, internal concept retrieval remains mandatory for CrossFrame concepts.

## Timing

1. Triage pass: decide whether external retrieval is mandatory, optional, or skipped.
2. Source frontier pass: retrieve supporting and background material.
3. Reverse retrieval pass: retrieve counterevidence and alternative explanations.
4. Evidence-reasoning audit: check whether more retrieval is required for any center claim.
5. Red-team pass: trigger one more targeted retrieval if falsification depends on missing facts.
6. Final output: record retrieval status, source snapshot time, missing material, stop condition, and downgraded claims.

## Required Artifact Fields

`max-source-frontier` must record:

- retrieval-trigger-policy status
- internal concept retrieval status
- external retrieval trigger decision
- why retrieval was mandatory, optional, or skipped
- active retrieval queries or lookup targets
- reverse retrieval queries or lookup targets
- source snapshot time
- missing materials
- inaccessible materials
- stop condition

`max-evidence-reasoning-audit` must record which claims required retrieval and how retrieval changed claim strength.
