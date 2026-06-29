# CrossFrame v5 DLC Publication Prototype Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce the first publishable v5.0 半量化 DLC document source and reusable tool-prototype bundle without turning half-quantification into total scores, predictions, certification, or disposition authority.

**Architecture:** Keep the canonical v5.0 半量化 DLC publication source in tracked Markdown under `docs/`, with linked runtime references under `skills/crossframe/`. Add a lightweight standard-library builder/checker that assembles a release bundle into ignored `outputs/` artifacts and rejects total-score, proof-of-correctness, and action-authorizing language. DOCX generation is a follow-up output step from the Markdown source after the publication checker is green.

**Tech Stack:** Markdown, Python 3 standard library, existing CrossFrame verification scripts, optional `python-docx` for later DOCX output.

---

## Scope Split

This plan implements Phase 4 and the first half of Phase 5 from `docs/superpowers/specs/2026-06-30-crossframe-v5-dlc-quantification-design.md`.

This plan does not merge the branch, publish a release, update public GitHub Pages copy, or install global mirrors. It also does not treat generated DOCX as source of truth. The source of truth for this phase is tracked Markdown plus scripts and verification.

## File Structure

Create these files:

- `docs/CROSSFRAME_V5_DLC.md` is the publishable v5.0 半量化 DLC Markdown document.
- `docs/V5_DLC_INTEGRATION_NOTES.md` explains how v5.0 半量化 DLC extends v5.0 and what changed.
- `docs/V5_DLC_TOOL_PROTOTYPE.md` explains how to use the v5 DLC reusable tool prototype and what it cannot do.
- `skills/crossframe/references/judgment-action-matrix-v5-dlc.md` formalizes judgment-grade/action-ceiling mapping.
- `skills/crossframe/references/falsification-governance-v5-dlc.md` formalizes counterexample, misuse, rater-disagreement, and version-writeback governance.
- `scripts/build_v5_dlc_publication_bundle.py` assembles ignored `outputs/crossframe-v5-dlc-publication-<stamp>.md` and `outputs/crossframe-v5-dlc-publication-<stamp>.manifest.json`.
- `scripts/check_v5_dlc_publication_bundle.py` checks the tracked v5 DLC publication source and generated bundle.

Modify these files:

- `scripts/check_crossframe_skill_integrity.py` requires the new v5 DLC publication documents, matrix, governance reference, builder, and checker.
- `.github/workflows/verify.yml` runs `python scripts/check_v5_dlc_publication_bundle.py --repo .`.
- `README.md` links to `docs/CROSSFRAME_V5_DLC.md` and `docs/V5_DLC_TOOL_PROTOTYPE.md`.
- `docs/QUICKSTART.md` adds the publication checker and builder commands.

Mirror new `skills/crossframe/references/*.md` files into `.claude/skills/crossframe/references/` with `scripts/sync_skill_mirrors.py --repo .`.

## Publication Document Contract

`docs/CROSSFRAME_V5_DLC.md` must contain these sections:

```text
# 跨尺度结构诊断框架 v5.0 半量化 DLC
## 发布边界
## v5.0 半量化 DLC
## 半量化 DLC 不是什么
## 半量化层的四项责任
## 构念图谱
## 七闸半量化
## 证据台账
## 校准锚点
## 机制候选更新
## 判断档位与行动上限
## 反例、撤回与治理写回
## 案例库验证与评分者一致性
## 反误用红线
## 工具原型
## 发布前检查清单
```

It must reference these current files:

```text
skills/crossframe/references/construct-map-v5-dlc.md
skills/crossframe/worksheets/seven-gates-quant-rubric.md
skills/crossframe/worksheets/evidence-ledger-v5-dlc.md
skills/crossframe/worksheets/calibration-anchor-card.md
skills/crossframe/worksheets/mechanism-update-rules.md
skills/crossframe/worksheets/counterexample-register.md
skills/crossframe-casebook/examples/v5-dlc-quant-trials/validation-summary.md
scripts/validate_v5_dlc_quantification_schema_fixtures.py
scripts/check_v5_dlc_casebook_trials.py
```

It must include this exact tool boundary:

```text
本工具只帮助整理结构判断，不替代现实调查、专业判断、受影响位置反馈、外部复核和最终责任承担。分数只能触发降级、复核或补证，不能单独授权处置。
```

## Forbidden Language Gate

The checker must reject these markers in tracked v5 DLC publication documents and generated bundle unless they appear inside an explicit forbidden-language list:

```text
total_score
overall_score
average_score
weighted_score
final_score
prediction_probability
success_rate
reliability_proved
validated_framework
casebook_coverage_proves
总分系统
预测模型
认证系统
处置依据
证明框架正确
一致性证明现实判断为真
覆盖率证明外部有效性
```

When the phrase appears as a negation or forbidden-use warning, use wording that includes `不得`, `不能`, `不是`, `不作为`, `禁止`, or `反误用`.

## Task 1: Add Judgment Matrix And Falsification Governance

**Files:**
- Create: `skills/crossframe/references/judgment-action-matrix-v5-dlc.md`
- Create: `skills/crossframe/references/falsification-governance-v5-dlc.md`

- [ ] Create `judgment-action-matrix-v5-dlc.md` with the mapping from seven-gate/evidence/claim-ledger state to `judgment_grade` and `action_ceiling`.
- [ ] Include forced downgrade rules for failed/blocked gates, evidence gate below 3, power gate below 3, action gate below 3, missing claim ledger, missing concept contract, and missing cannot-prove boundary.
- [ ] Create `falsification-governance-v5-dlc.md` with counterexample categories, rater-disagreement handling, misuse review, version writeback, and stop-use conditions.
- [ ] Include the exact tool boundary sentence from this plan.

## Task 2: Add Publishable V5 DLC Markdown Source

**Files:**
- Create: `docs/CROSSFRAME_V5_DLC.md`
- Create: `docs/V5_DLC_INTEGRATION_NOTES.md`
- Create: `docs/V5_DLC_TOOL_PROTOTYPE.md`

- [ ] Create `docs/CROSSFRAME_V5_DLC.md` with all required section headings from the publication contract.
- [ ] Ground the document in v5.0 continuity: seven-part v5 structure, seven gates, source/fact/evidence/mechanism/judgment/action separation, framework governance, and anti-misuse boundaries.
- [ ] Explain v5.0 半量化 DLC as a half-quantification audit layer with four responsibilities: calibrate judgment, expose uncertainty, limit action ceiling, trigger review/writeback.
- [ ] Include the casebook validation summary as failure-discovery evidence, not reliability proof.
- [ ] Include the exact tool boundary sentence.
- [ ] Create `docs/V5_DLC_INTEGRATION_NOTES.md` with a table of v5.0 continuity, v5.0 半量化 DLC addition, source file, and misuse risk.
- [ ] Create `docs/V5_DLC_TOOL_PROTOTYPE.md` with commands, inputs, outputs, forbidden uses, and smoke-test expectations.

## Task 3: Add Publication Bundle Builder

**Files:**
- Create: `scripts/build_v5_dlc_publication_bundle.py`

- [ ] Implement a standard-library Python script with `--repo`, `--output-dir`, and optional `--stamp` arguments.
- [ ] Read the tracked publication files and referenced worksheets.
- [ ] Write one Markdown bundle to `outputs/crossframe-v5-dlc-publication-<stamp>.md`.
- [ ] Write one manifest JSON to `outputs/crossframe-v5-dlc-publication-<stamp>.manifest.json` listing source files and SHA256 hashes.
- [ ] Print the created file paths and source count.

## Task 4: Add Publication Checker

**Files:**
- Create: `scripts/check_v5_dlc_publication_bundle.py`

- [ ] Implement a standard-library Python checker with `--repo` and optional `--bundle` arguments.
- [ ] Check required tracked source files exist.
- [ ] Check required section headings in `docs/CROSSFRAME_V5_DLC.md`.
- [ ] Check required file references and exact tool boundary sentence.
- [ ] Reject forbidden language unless it is negated by a nearby anti-misuse marker.
- [ ] Run the builder into `outputs/` when no `--bundle` path is passed, then check the generated bundle and manifest.
- [ ] Verify manifest paths exist and hashes match current source files.
- [ ] Print concise file-specific errors and return non-zero on failure.

## Task 5: Wire Verification And Docs

**Files:**
- Modify: `scripts/check_crossframe_skill_integrity.py`
- Modify: `.github/workflows/verify.yml`
- Modify: `README.md`
- Modify: `docs/QUICKSTART.md`

- [ ] Add `check_v5_dlc_publication_prototype(root, label)` to `scripts/check_crossframe_skill_integrity.py`.
- [ ] Require `docs/CROSSFRAME_V5_DLC.md`, `docs/V5_DLC_INTEGRATION_NOTES.md`, `docs/V5_DLC_TOOL_PROTOTYPE.md`, `judgment-action-matrix-v5-dlc.md`, `falsification-governance-v5-dlc.md`, builder, and checker.
- [ ] Add `python scripts/check_v5_dlc_publication_bundle.py --repo .` to `.github/workflows/verify.yml`.
- [ ] Add README links to the v5 DLC document and tool prototype guide.
- [ ] Add QUICKSTART commands for checker and builder.

## Task 6: Mirror, Verify, Package

**Files:**
- Modify: `.claude/skills/crossframe/references/judgment-action-matrix-v5-dlc.md`
- Modify: `.claude/skills/crossframe/references/falsification-governance-v5-dlc.md`

- [ ] Run `python scripts/sync_skill_mirrors.py --repo .`.
- [ ] Run `python scripts/check_v5_dlc_publication_bundle.py --repo .`.
- [ ] Run existing v5 DLC schema and casebook validators.
- [ ] Run `python scripts/check_crossframe_skill_integrity.py --repo . --mirror .claude/skills`.
- [ ] Run `python scripts/check_source_continuity.py --materials-only --repo .`.
- [ ] Run `python scripts/sync_skill_mirrors.py --repo . --check`.
- [ ] Run Python compile, shell syntax check, and `git diff --check`.
- [ ] Run package smoke and confirm the zip contains `docs/CROSSFRAME_V5_DLC.md`, `scripts/check_v5_dlc_publication_bundle.py`, and `skills/crossframe/references/judgment-action-matrix-v5-dlc.md`.

## Acceptance Criteria

Run these commands from `E:\世界模型\skill\crossframe-skill`:

```powershell
python scripts/check_v5_dlc_publication_bundle.py --repo .
$env:PYTHONPATH='work/pydeps'; python scripts/validate_v5_dlc_quantification_schema_fixtures.py --repo .
python scripts/check_v5_dlc_casebook_trials.py --repo .
python scripts/check_crossframe_skill_integrity.py --repo . --mirror .claude/skills
python scripts/check_source_continuity.py --materials-only --repo .
python scripts/sync_skill_mirrors.py --repo . --check
Get-ChildItem scripts -Filter *.py | ForEach-Object { python -m py_compile $_.FullName }
bash -n scripts/install-codex.sh
git diff --check
```

Expected result:

- The v5.0 半量化 DLC Markdown source is publishable as an audit-layer document.
- The publication source references all current v5 DLC foundation and casebook artifacts.
- The builder creates an ignored Markdown bundle and manifest with source hashes.
- The checker rejects unbounded total-score/proof/action-authorizing language.
- Existing v5 DLC schema, casebook, integrity, source-continuity, mirror, compile, shell, and whitespace checks stay green.

## Review Notes

Use one independent semantic review after implementation:

- Does the v5 DLC document preserve v5.0 continuity instead of replacing it with a scoring system?
- Does any generated or tracked text imply empirical validation, reliability proof, certification, or disposition authority?
- Are action ceilings still lower than evidence, power, and public-boundary risks require?
- Do the tool prototype commands make misuse harder, not easier?
- Does the publication bundle include enough source manifest information for audit?
