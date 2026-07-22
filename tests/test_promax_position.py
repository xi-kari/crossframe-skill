from __future__ import annotations

import copy
import hashlib
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
RUNTIME_SCRIPTS = ROOT / "skills/crossframe-promax/scripts"
sys.path.insert(0, str(RUNTIME_SCRIPTS))

from promax_runtime.artifacts import (
    build_capability_disclosure,
    initialize_run,
)
from promax_runtime.jsonio import sha256_json
from promax_runtime.position import (
    validate_position_semantics,
    validate_recommendation_semantics,
)
from promax_runtime.source_integrity import V8_SOURCE_SNAPSHOT_SHA256


STAMP = "2026-07-23T02:00:00Z"
RUN_ID = "promax-position-test"
HASH_A = hashlib.sha256(b"evidence-a").hexdigest()
HASH_B = hashlib.sha256(b"evidence-b").hexdigest()


def claim_graph() -> dict[str, object]:
    return {
        "schema_id": "crossframe.promax.v8.claim-path-graph",
        "schema_version": 1,
        "run_id": RUN_ID,
        "source_snapshot_sha256": V8_SOURCE_SNAPSHOT_SHA256,
        "central_claim_id": "CLAIM-1",
        "central_claim_cycle": {
            "central_claim_id": "CLAIM-1",
            "initial_judgment": "当前结构最符合机制甲。",
            "strongest_attack": "对象边界是否被错误冻结？",
            "revision": "降低判断强度并加入对象边界重置",
            "counterfactual": "若对象边界改变，机制乙将成为更合理解释。",
            "withdrawal_conditions": [
                "若对象边界并不稳定得到新证据证实，则撤回当前判断。"
            ],
        },
        "claims": [
            {
                "claim_id": "CLAIM-1",
                "statement": "当前结构最符合机制甲。",
                "claim_type": "structural",
                "evidence_refs": ["EVIDENCE-1"],
                "concept_ids": ["V8-CANON-OBJECT"],
                "confidence": "medium",
                "authorization_ceiling": "分析判断不授权现实行动。",
            }
        ],
        "mechanisms": [
            {
                "mechanism_id": "MECH-1",
                "label": "机制甲",
                "claim_ids": ["CLAIM-1"],
                "distinguishing_conditions": ["对象边界保持稳定"],
            },
            {
                "mechanism_id": "MECH-2",
                "label": "机制乙",
                "claim_ids": ["CLAIM-1"],
                "distinguishing_conditions": ["对象边界发生改变"],
            },
        ],
        "path_nodes": [
            {
                "node_id": "NODE-1",
                "label": "当前状态",
                "node_type": "state",
                "trigger_conditions": ["对象进入观察范围"],
                "early_signals": ["边界持续稳定"],
                "reverse_signals": ["边界发生改变"],
                "stop_conditions": ["授权边界触发"],
            }
        ],
        "path_edges": [],
        "forecast_conditions": ["只作条件排序"],
        "choice_boundary": "预测不产生行动授权。",
        "updated_at": "2026-07-23T02:00:00Z",
    }


def red_team_report() -> dict[str, object]:
    return {
        "schema_id": "crossframe.promax.v8.red-team-report",
        "schema_version": 1,
        "run_id": RUN_ID,
        "source_snapshot_sha256": V8_SOURCE_SNAPSHOT_SHA256,
        "central_claim_id": "CLAIM-1",
        "attacks": [
            {
                "attack_id": "ATTACK-1",
                "attack_class": "boundary_error",
                "target_id": "CLAIM-1",
                "challenge": "对象边界是否被错误冻结？",
                "counterevidence_refs": ["EVIDENCE-2"],
                "strongest_counterposition": "对象边界并不稳定",
                "result": "survived_with_revision",
                "revision": "降低判断强度并加入对象边界重置",
                "position_impact": "high",
            },
            {
                "attack_id": "ATTACK-2",
                "attack_class": "prediction_authorization_leakage",
                "target_id": "CLAIM-1",
                "challenge": "是否由预测偷渡了行动授权？",
                "counterevidence_refs": [],
                "strongest_counterposition": "预测不能生成现实授权",
                "result": "survived",
                "revision": "保留独立授权上限",
                "position_impact": "medium",
            },
        ],
        "stability_checks": [
            {
                "prompt_pair_id": "PAIR-1",
                "pro_prompt_sha256": HASH_A,
                "anti_prompt_sha256": HASH_B,
                "evidence_before_sha256": HASH_A,
                "evidence_after_sha256": HASH_A,
                "central_position_id_before": "CLAIM-1",
                "central_position_id_after": "CLAIM-1",
                "judgment_strength_before": "moderate",
                "judgment_strength_after": "moderate",
                "option_ranking_before": [
                    "OPTION-1",
                    "OPTION-2",
                    "OPTION-3",
                    "OPTION-4",
                    "OPTION-5",
                    "OPTION-6",
                ],
                "option_ranking_after": [
                    "OPTION-1",
                    "OPTION-2",
                    "OPTION-3",
                    "OPTION-4",
                    "OPTION-5",
                    "OPTION-6",
                ],
                "position_drift": "none",
                "explanation": "证据未变，因此立场不随用户赞成或反对而改变。",
            }
        ],
        "revision_summary": ["降低判断强度并加入对象边界重置"],
        "completed_at": "2026-07-23T03:00:00Z",
    }


def position_lock() -> dict[str, object]:
    return {
        "schema_id": "crossframe.promax.v8.position",
        "schema_version": 1,
        "run_id": RUN_ID,
        "source_snapshot_sha256": V8_SOURCE_SNAPSHOT_SHA256,
        "central_claim_id": "CLAIM-1",
        "position": "当前条件下，机制甲是最合理解释。",
        "judgment_strength": "moderate",
        "primary_reasons": [
            "当前结构最符合机制甲。",
            "降低判断强度并加入对象边界重置。",
        ],
        "runner_up_explanation": "机制乙在对象边界发生改变时成为次优解释。",
        "strongest_counterevidence": ["对象边界并不稳定"],
        "why_not_adopted": ["现有证据尚未证明对象边界已经改变"],
        "withdrawal_conditions": [
            "若对象边界并不稳定得到新证据证实，则撤回当前判断。"
        ],
        "action_ceiling": "仅作分析判断；不授权现实行动，现实处置需另行授权。",
        "locked_at": "2026-07-23T04:00:00Z",
    }


def run_contract(recommendation_required: bool) -> dict[str, object]:
    return {
        "run_id": RUN_ID,
        "source_snapshot_sha256": V8_SOURCE_SNAPSHOT_SHA256,
        "recommendation_required": recommendation_required,
    }


def recommendation(position: dict[str, object]) -> dict[str, object]:
    kinds = (
        "proactive_action",
        "delay",
        "probe",
        "exit_or_transfer",
        "status_quo",
        "inaction",
    )
    options = [
        {
            "option_id": f"OPTION-{index}",
            "action_kind": kind,
            "description": f"方案{index}：{kind}",
            "benefits": ["保留结构收益"],
            "costs": ["承担可比较成本"],
            "risks": ["存在条件性风险"],
            "authorization_status": "requires_authorized_decision_maker",
            "stop_conditions": ["边界证据失效时停止"],
            "rollback": ["回到冻结前状态"],
        }
        for index, kind in enumerate(kinds, start=1)
    ]
    return {
        "schema_id": "crossframe.promax.v8.recommendation",
        "schema_version": 1,
        "run_id": RUN_ID,
        "source_snapshot_sha256": V8_SOURCE_SNAPSHOT_SHA256,
        "position_sha256": sha256_json(position),
        "options": options,
        "evaluation_dimensions": ["结构解释力", "可逆性", "风险"],
        "ranking": [option["option_id"] for option in options],
        "preferred_option_id": "OPTION-1",
        "second_option_id": "OPTION-2",
        "switch_conditions": ["对象边界改变时切换到 OPTION-2"],
        "inaction_consequences": ["不行动会继续累积机会成本"],
        "authorization_status": "conditional_recommendation_only",
        "locked_at": "2026-07-23T05:00:00Z",
    }


class ProMaxRecommendationIntentTests(unittest.TestCase):
    def test_run_contract_freezes_recommendation_intent_as_a_real_boolean(self) -> None:
        capabilities = build_capability_disclosure(
            subagents_available=False,
            max_parallelism=0,
            validator_ids=("schema",),
        )
        for required in (False, True):
            with self.subTest(required=required):
                initialized = initialize_run(
                    ROOT,
                    "请用 CrossFrame ProMax。",
                    mode="promax-artifact-run",
                    capabilities=capabilities,
                    created_at=STAMP,
                    run_id=f"promax-recommendation-{str(required).lower()}",
                    recommendation_required=required,
                )
                self.assertIs(
                    initialized["run_contract"]["recommendation_required"],
                    required,
                )
        with self.assertRaises((TypeError, ValueError)):
            initialize_run(
                ROOT,
                "请用 CrossFrame ProMax。",
                mode="promax-artifact-run",
                capabilities=capabilities,
                created_at=STAMP,
                run_id="promax-recommendation-invalid",
                recommendation_required="yes",
            )


class ProMaxPositionSemanticTests(unittest.TestCase):
    def test_position_is_locked_after_red_team_and_carries_the_strongest_attack(self) -> None:
        result = validate_position_semantics(
            position_lock(),
            red_team_report=red_team_report(),
            claim_path_graph=claim_graph(),
            expected_run_id=RUN_ID,
            expected_source_snapshot_sha256=V8_SOURCE_SNAPSHOT_SHA256,
        )
        self.assertEqual(result["central_claim_id"], "CLAIM-1")

    def test_position_rejects_stale_lock_countercase_omission_and_authorization_leak(self) -> None:
        cases: list[dict[str, object]] = []
        stale = position_lock()
        stale["locked_at"] = "2026-07-23T02:59:59Z"
        cases.append(stale)

        no_countercase = position_lock()
        no_countercase["strongest_counterevidence"] = ["另一个较弱反例"]
        cases.append(no_countercase)

        no_withdrawal_link = position_lock()
        no_withdrawal_link["withdrawal_conditions"] = ["若天气变化则撤回"]
        cases.append(no_withdrawal_link)

        authorization_leak = position_lock()
        authorization_leak["action_ceiling"] = "已经授权立即采取现实行动"
        cases.append(authorization_leak)

        for candidate in cases:
            with self.subTest(candidate=candidate):
                with self.assertRaises(ValueError):
                    validate_position_semantics(
                        candidate,
                        red_team_report=red_team_report(),
                        claim_path_graph=claim_graph(),
                        expected_run_id=RUN_ID,
                        expected_source_snapshot_sha256=V8_SOURCE_SNAPSHOT_SHA256,
                    )

    def test_user_stance_drift_requires_a_changed_evidence_hash(self) -> None:
        unchanged = red_team_report()
        unchanged["stability_checks"][0]["position_drift"] = "justified_by_evidence"
        with self.assertRaises(ValueError):
            validate_position_semantics(
                position_lock(),
                red_team_report=unchanged,
                claim_path_graph=claim_graph(),
                expected_run_id=RUN_ID,
                expected_source_snapshot_sha256=V8_SOURCE_SNAPSHOT_SHA256,
            )

    def test_runner_up_why_not_and_stance_probe_are_genuinely_competing(self) -> None:
        same_winner = position_lock()
        same_winner["runner_up_explanation"] = "机制甲仍然是次优解释。"

        label_only = position_lock()
        label_only["runner_up_explanation"] = "机制乙"

        unrelated_why_not = position_lock()
        unrelated_why_not["why_not_adopted"] = ["天气预报没有发生变化"]

        generic_overlap = position_lock()
        generic_overlap["why_not_adopted"] = ["对象完全无关。"]

        identical_probe = red_team_report()
        identical_probe["stability_checks"][0]["anti_prompt_sha256"] = HASH_A

        contradictory_probe = red_team_report()
        contradictory_probe["stability_checks"][0]["explanation"] = (
            "同证据下赞成选甲、反对选乙，中心判断和排序均改变。"
        )

        cases = (
            (same_winner, red_team_report()),
            (label_only, red_team_report()),
            (unrelated_why_not, red_team_report()),
            (generic_overlap, red_team_report()),
            (position_lock(), identical_probe),
            (position_lock(), contradictory_probe),
        )
        for candidate_position, candidate_red_team in cases:
            with self.subTest(
                position=candidate_position,
                red_team=candidate_red_team,
            ):
                with self.assertRaises(ValueError):
                    validate_position_semantics(
                        candidate_position,
                        red_team_report=candidate_red_team,
                        claim_path_graph=claim_graph(),
                        expected_run_id=RUN_ID,
                        expected_source_snapshot_sha256=V8_SOURCE_SNAPSHOT_SHA256,
                    )

    def test_stance_probe_binds_position_strength_and_option_ranking(self) -> None:
        mutations = (
            ("central_position_id_after", "CLAIM-2"),
            ("judgment_strength_after", "strong"),
            (
                "option_ranking_after",
                [
                    "OPTION-2",
                    "OPTION-1",
                    "OPTION-3",
                    "OPTION-4",
                    "OPTION-5",
                    "OPTION-6",
                ],
            ),
        )
        for field, value in mutations:
            report = red_team_report()
            report["stability_checks"][0][field] = value
            with self.subTest(field=field):
                with self.assertRaises(ValueError):
                    validate_position_semantics(
                        position_lock(),
                        red_team_report=report,
                        claim_path_graph=claim_graph(),
                        expected_run_id=RUN_ID,
                        expected_source_snapshot_sha256=V8_SOURCE_SNAPSHOT_SHA256,
                    )

        changed = red_team_report()
        changed["stability_checks"][0]["evidence_after_sha256"] = HASH_B
        changed["stability_checks"][0]["judgment_strength_after"] = "strong"
        changed["stability_checks"][0]["position_drift"] = "justified_by_evidence"
        changed_position = position_lock()
        changed_position["judgment_strength"] = "strong"
        validate_position_semantics(
            changed_position,
            red_team_report=changed,
            claim_path_graph=claim_graph(),
            expected_run_id=RUN_ID,
            expected_source_snapshot_sha256=V8_SOURCE_SNAPSHOT_SHA256,
        )

        unjustified = red_team_report()
        unjustified["stability_checks"][0]["evidence_after_sha256"] = HASH_B
        unjustified["stability_checks"][0]["position_drift"] = "unjustified"
        with self.assertRaises(ValueError):
            validate_position_semantics(
                position_lock(),
                red_team_report=unjustified,
                claim_path_graph=claim_graph(),
                expected_run_id=RUN_ID,
                expected_source_snapshot_sha256=V8_SOURCE_SNAPSHOT_SHA256,
            )


class ProMaxRecommendationSemanticTests(unittest.TestCase):
    def test_required_recommendation_has_all_six_actions_and_is_position_bound(self) -> None:
        position = position_lock()
        result = validate_recommendation_semantics(
            run_contract(True),
            recommendation(position),
            position=position,
            expected_run_id=RUN_ID,
            expected_source_snapshot_sha256=V8_SOURCE_SNAPSHOT_SHA256,
        )
        self.assertEqual(result["preferred_option_id"], result["ranking"][0])
        self.assertEqual(result["second_option_id"], result["ranking"][1])

    def test_not_requested_branch_is_exact_and_cannot_hide_or_fabricate_advice(self) -> None:
        self.assertEqual(
            validate_recommendation_semantics(
                run_contract(False),
                {"status": "not_requested"},
                position=position_lock(),
                expected_run_id=RUN_ID,
                expected_source_snapshot_sha256=V8_SOURCE_SNAPSHOT_SHA256,
            ),
            {"status": "not_requested"},
        )
        for required, candidate in (
            (True, {"status": "not_requested"}),
            (False, recommendation(position_lock())),
            (False, {"status": "not_requested", "advice": "偷偷建议"}),
        ):
            with self.subTest(required=required):
                with self.assertRaises(ValueError):
                    validate_recommendation_semantics(
                        run_contract(required),
                        candidate,
                        position=position_lock(),
                        expected_run_id=RUN_ID,
                        expected_source_snapshot_sha256=V8_SOURCE_SNAPSHOT_SHA256,
                    )

    def test_recommendation_rejects_bad_ranking_switch_position_hash_and_authorization(self) -> None:
        position = position_lock()
        valid = recommendation(position)
        cases: list[dict[str, object]] = []

        bad_ranking = copy.deepcopy(valid)
        bad_ranking["ranking"][0], bad_ranking["ranking"][1] = (
            bad_ranking["ranking"][1],
            bad_ranking["ranking"][0],
        )
        cases.append(bad_ranking)

        bad_switch = copy.deepcopy(valid)
        bad_switch["switch_conditions"] = ["边界改变时再看"]
        cases.append(bad_switch)

        stale_position = copy.deepcopy(valid)
        stale_position["position_sha256"] = HASH_B
        cases.append(stale_position)

        authorized = copy.deepcopy(valid)
        authorized["authorization_status"] = "authorized"
        cases.append(authorized)

        missing_kind = copy.deepcopy(valid)
        missing_kind["options"][-1]["action_kind"] = "status_quo"
        cases.append(missing_kind)

        for candidate in cases:
            with self.subTest(candidate=candidate):
                with self.assertRaises(Exception):
                    validate_recommendation_semantics(
                        run_contract(True),
                        candidate,
                        position=position,
                        expected_run_id=RUN_ID,
                        expected_source_snapshot_sha256=V8_SOURCE_SNAPSHOT_SHA256,
                    )


if __name__ == "__main__":
    unittest.main()
