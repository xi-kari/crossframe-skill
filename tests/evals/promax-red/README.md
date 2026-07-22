# CrossFrame ProMax RED baselines

## Method

This fixture freezes twelve actual no-ProMax answers before the ProMax runtime exists. The prompts, evaluator conditions, pressure tags, and raw response paths are indexed by `scenarios.json`; each response is preserved without post-hoc rewriting under `raw/`.

Group A and D were fresh-fork, no-skill controls. CrossFrame ProMax was not loaded. A used the v8 DOCX read-only as needed; D did not run ProMax artifacts or a validator. A requested fresh evaluator for B could not be created because the platform returned `agent thread limit reached`. B and C therefore ran in separate turns of the same no-skill evaluator, with each scenario's material reset. This limitation is recorded rather than describing B or C as fresh forks.

Safety-preserving judgments are not counted as failures. Several baseline answers correctly rejected unsupported causality, personality diagnosis, selective retrieval, scale leakage, fabricated search, or prediction-derived authorization. Their RED status comes from the absence of the future ProMax execution contract, not from treating those safe conclusions as wrong.

The observable ProMax gaps are the absence of a frozen v8 anchor and read-event trail; concept terminal closure; typed claim-path coverage; a retrieval ledger; red-team saturation; typed example coverage; position and recommendation ledgers; continuation state; artifact validation; validator evidence; and repair-loop closure. C4 is the substantive routing exception: it explicitly permits and proposes Max fallback after ProMax was named, which conflicts with the new no-fallback specification.

## Per-scenario observable gaps

| Scenario | Observable baseline gap |
| --- | --- |
| A1 | Safe rejection of an absolute causal claim, but no v8 anchor/read-event ledger, concept terminal closure, typed claim-path set, or artifact validation. |
| A2 | Safe rejection of an absolute zero-risk claim, but no v8 anchor/read-event ledger, concept terminal closure, typed claim-path set, or artifact validation. |
| A3 | Safe rejection of personality and dismissal leaps, but no typed example artifact, judgment-charter trace, red-team saturation record, or validator result. |
| B1 | Safe material-insufficiency judgment, but no source/read ledger, terminal concept closure, typed competing claim paths, or repair artifact. |
| B2 | Safe refusal to equate jargon with completeness, but no auditable concept terminal closure, typed examples, or artifact validation. |
| B3 | Safe refusal of support-only evidence selection, but no executed retrieval ledger, saturation status, source coverage artifact, or validator result. |
| B4 | Safe separation of local evidence, forecast, and authorization, but no scale claim-path artifact, position ledger, recommendation ledger, or validation. |
| C1 | Safe candidate-object downgrade, but no v8 object anchor, read-event trail, terminal concept closure, or calibrated continuation ledger. |
| C2 | Safe refusal to apply S0-S6 to an individual, but no typed misuse example artifact, claim-path trace, or validator evidence. |
| C3 | Safe refusal to fabricate exhaustive retrieval, but no retrieval ledger or explicit saturation state because the tools were unavailable. |
| C4 | Actual routing conflict: the answer allows and proposes Max fallback after ProMax is named; the target contract requires ProMax priority and no Max fallback. |
| D1 | Safe refusal to issue `promax-complete`, but no ProMax artifact contract, validator execution, repair loop, or validated completion state. |

## Commands

Target RED suite:

```powershell
python -B -m unittest tests.test_promax_behavioral_contract tests.test_promax_repository_integration -v
```

Existing regression suite:

```powershell
python -B -m unittest tests.test_mirror_integrity tests.test_verify_workflow_contract -v
```

## RED result summary

Observed on the first run:

```text
Ran 15 tests in 0.113s
FAILED (failures=10)
```

There were no import, syntax, fixture, or runtime errors. Seven checks passed: all three frozen-baseline checks, both Max preservation checks, the generic maximum-request routing check, and the named-Max identity check. The ten expected assertion failures were:

- four behavioral-contract assertions stopped at the missing `skills/crossframe-promax/SKILL.md`;
- inventory reported `expected 16 CrossFrame skills, got 15`;
- the canonical ProMax skill and Claude command were absent;
- the suite named-only priority assertion failed independently for `SKILL.md`, `suite-dispatch-protocol.md`, and `workflow-routing-map.md` because none yet contains `crossframe-promax`.

This is the intended RED state: the captured controls and Max preservation manifest are valid, while only the not-yet-implemented ProMax production contracts fail.

The existing regression command remained green:

```text
Ran 3 tests in 0.011s
OK
```
