from __future__ import annotations

import copy
from datetime import datetime
import re
from typing import Mapping, Sequence

from .jsonio import sha256_json
from .validation import validate_bound_document


_IMPACT_RANK = {
    "none": 0,
    "low": 1,
    "medium": 2,
    "high": 3,
    "decisive": 4,
}
_ACTION_DENIAL_MARKERS = (
    "不授权",
    "不得授权",
    "未经授权",
    "需另行授权",
    "需要另行授权",
    "仅作分析",
    "analysis only",
    "not authorized",
    "requires separate authorization",
)
_ACTION_GRANT_MARKERS = (
    "已授权",
    "授权立即",
    "立即采取现实行动",
    "authorized to",
    "permission granted",
    "must act now",
)
_CONDITIONAL_MARKERS = ("若", "如果", "一旦", "when ", "if ", "unless ")
_WITHDRAWAL_MARKERS = ("撤回", "调整", "降级", "改变", "withdraw", "revise")
_EXPLANATION_MARKERS = (
    "若",
    "如果",
    "一旦",
    "条件",
    "因为",
    "由于",
    "在",
    "when ",
    "if ",
    "unless ",
    "because",
)
_POSITIVE_DRIFT_CLAIMS = (
    "均改变",
    "发生改变",
    "已经改变",
    "改变了",
    "发生漂移",
    "不同判断",
    "position changed",
    "ranking changed",
    "different position",
    "different ranking",
)
_REQUIRED_ACTION_KINDS = frozenset(
    {
        "proactive_action",
        "delay",
        "probe",
        "exit_or_transfer",
        "status_quo",
        "inaction",
    }
)


def _timestamp(value: object, *, field: str) -> datetime:
    if not isinstance(value, str):
        raise ValueError(f"{field} must be an ISO-8601 timestamp")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise ValueError(f"{field} must be an ISO-8601 timestamp") from error
    if parsed.tzinfo is None:
        raise ValueError(f"{field} must include a timezone")
    return parsed


def _mapping_items(value: object, *, field: str) -> list[Mapping[str, object]]:
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes)):
        raise ValueError(f"{field} must be an array")
    items: list[Mapping[str, object]] = []
    for index, item in enumerate(value):
        if not isinstance(item, Mapping):
            raise ValueError(f"{field}[{index}] must be an object")
        items.append(item)
    return items


def _text_items(value: object, *, field: str) -> list[str]:
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes)):
        raise ValueError(f"{field} must be an array")
    result: list[str] = []
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            raise ValueError(f"{field}[{index}] must be non-empty text")
        result.append(item.strip())
    return result


def _contains_any(text: str, markers: Sequence[str]) -> bool:
    folded = text.casefold()
    return any(marker.casefold() in folded for marker in markers)


def _all_text(value: object) -> list[str]:
    if isinstance(value, Mapping):
        result: list[str] = []
        for key, child in value.items():
            result.append(str(key))
            result.extend(_all_text(child))
        return result
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        result = []
        for child in value:
            result.extend(_all_text(child))
        return result
    return [value] if isinstance(value, str) else []


def _semantic_tokens(text: str) -> set[str]:
    tokens = {
        token.casefold()
        for token in re.findall(r"[A-Za-z0-9]+", text)
        if len(token) >= 4
    }
    for run in re.findall(r"[\u3400-\u9fff]+", text):
        for width in (4, 5, 6):
            tokens.update(
                run[index : index + width]
                for index in range(max(0, len(run) - width + 1))
            )
    return tokens


def validate_position_lock(
    document: Mapping[str, object],
    *,
    expected_run_id: str,
    expected_source_snapshot_sha256: str,
) -> dict[str, object]:
    return validate_bound_document(
        "promax-position.schema.json",
        document,
        expected_run_id=expected_run_id,
        expected_source_snapshot_sha256=expected_source_snapshot_sha256,
    )


def validate_recommendation_lock(
    document: Mapping[str, object],
    *,
    expected_run_id: str,
    expected_source_snapshot_sha256: str,
) -> dict[str, object]:
    return validate_bound_document(
        "promax-recommendation.schema.json",
        document,
        expected_run_id=expected_run_id,
        expected_source_snapshot_sha256=expected_source_snapshot_sha256,
    )


def validate_position_semantics(
    document: Mapping[str, object],
    *,
    red_team_report: Mapping[str, object],
    claim_path_graph: Mapping[str, object],
    expected_run_id: str,
    expected_source_snapshot_sha256: str,
) -> dict[str, object]:
    """Validate the evidence-bound position created after adversarial review."""

    position = validate_position_lock(
        document,
        expected_run_id=expected_run_id,
        expected_source_snapshot_sha256=expected_source_snapshot_sha256,
    )
    red_team = validate_bound_document(
        "promax-red-team-report.schema.json",
        red_team_report,
        expected_run_id=expected_run_id,
        expected_source_snapshot_sha256=expected_source_snapshot_sha256,
    )
    graph = validate_bound_document(
        "promax-claim-path-graph.schema.json",
        claim_path_graph,
        expected_run_id=expected_run_id,
        expected_source_snapshot_sha256=expected_source_snapshot_sha256,
    )

    central_claim_id = graph.get("central_claim_id")
    if (
        position.get("central_claim_id") != central_claim_id
        or red_team.get("central_claim_id") != central_claim_id
    ):
        raise ValueError("position, red-team report, and claim graph disagree on the central claim")

    graph_time = _timestamp(graph.get("updated_at"), field="claim_path_graph.updated_at")
    red_time = _timestamp(red_team.get("completed_at"), field="red_team_report.completed_at")
    locked_time = _timestamp(position.get("locked_at"), field="position.locked_at")
    if red_time < graph_time:
        raise ValueError("red-team report predates the claim graph it attacks")
    if locked_time <= red_time:
        raise ValueError("position.locked_at must be later than red-team completion")

    claims = _mapping_items(graph.get("claims"), field="claim_path_graph.claims")
    central_claims = [claim for claim in claims if claim.get("claim_id") == central_claim_id]
    if len(central_claims) != 1:
        raise ValueError("claim graph must contain exactly one central claim record")
    statement = central_claims[0].get("statement")
    reasons = _text_items(position.get("primary_reasons"), field="position.primary_reasons")
    position_text = str(position.get("position", ""))
    if not isinstance(statement, str) or not statement.strip():
        raise ValueError("central claim statement is missing")
    if statement not in "\n".join([position_text, *reasons]):
        raise ValueError("locked position does not carry its central claim statement")

    attacks = _mapping_items(red_team.get("attacks"), field="red_team_report.attacks")
    if not attacks:
        raise ValueError("red-team report must contain at least one attack")
    try:
        strongest = max(attacks, key=lambda item: _IMPACT_RANK[str(item.get("position_impact"))])
    except KeyError as error:
        raise ValueError("red-team attack has an invalid position impact") from error
    counterposition = strongest.get("strongest_counterposition")
    if not isinstance(counterposition, str) or not counterposition.strip():
        raise ValueError("strongest attack has no counterposition")
    counters = _text_items(
        position.get("strongest_counterevidence"),
        field="position.strongest_counterevidence",
    )
    if not any(counterposition in item or item in counterposition for item in counters):
        raise ValueError("position omits the strongest red-team counterposition")
    why_not = _text_items(
        position.get("why_not_adopted"),
        field="position.why_not_adopted",
    )
    counter_tokens = _semantic_tokens("\n".join([counterposition, *counters]))
    if not counter_tokens or not any(
        _semantic_tokens(reason) & counter_tokens for reason in why_not
    ):
        raise ValueError(
            "why_not_adopted is not semantically tied to the strongest counterposition"
        )

    withdrawals = _text_items(
        position.get("withdrawal_conditions"),
        field="position.withdrawal_conditions",
    )
    linked_withdrawals = [item for item in withdrawals if counterposition in item]
    if not linked_withdrawals:
        raise ValueError("withdrawal conditions are not tied to the strongest counterposition")
    if not all(
        _contains_any(item, _CONDITIONAL_MARKERS)
        and _contains_any(item, _WITHDRAWAL_MARKERS)
        for item in linked_withdrawals
    ):
        raise ValueError("strongest-counter withdrawal must state a conditional judgment change")

    revision = strongest.get("revision")
    if (
        strongest.get("result") == "survived_with_revision"
        and isinstance(revision, str)
        and revision.strip()
        and revision not in "\n".join([*reasons, *withdrawals])
    ):
        raise ValueError("locked position does not carry the strongest attack revision")

    mechanisms = _mapping_items(graph.get("mechanisms"), field="claim_path_graph.mechanisms")
    labels = [item.get("label") for item in mechanisms if isinstance(item.get("label"), str)]
    runner_up = str(position.get("runner_up_explanation", ""))
    runner_labels = {label for label in labels if label in runner_up}
    leading_text = "\n".join([statement, position_text, *reasons])
    leading_labels = {label for label in labels if label in leading_text}
    runner_remainder = runner_up
    for label in runner_labels:
        runner_remainder = runner_remainder.replace(label, "")
    runner_remainder = re.sub(r"[\s\W_]+", "", runner_remainder)
    if (
        len(labels) < 2
        or not runner_labels
        or not (runner_labels - leading_labels)
        or len(runner_remainder) < 8
        or not _contains_any(runner_up, _EXPLANATION_MARKERS)
    ):
        raise ValueError("runner-up explanation must name a competing mechanism")

    action_ceiling = str(position.get("action_ceiling", ""))
    if not _contains_any(action_ceiling, _ACTION_DENIAL_MARKERS):
        raise ValueError("action ceiling must explicitly preserve the authorization boundary")
    if _contains_any(action_ceiling, _ACTION_GRANT_MARKERS):
        raise ValueError("position analysis may not grant real-world authorization")

    checks = _mapping_items(
        red_team.get("stability_checks"),
        field="red_team_report.stability_checks",
    )
    for index, check in enumerate(checks):
        if check.get("pro_prompt_sha256") == check.get("anti_prompt_sha256"):
            raise ValueError(
                f"stability check {index} must use distinct pro and anti prompts"
            )
        before = check.get("evidence_before_sha256")
        after = check.get("evidence_after_sha256")
        drift = check.get("position_drift")
        before_position = check.get("central_position_id_before")
        after_position = check.get("central_position_id_after")
        before_strength = check.get("judgment_strength_before")
        after_strength = check.get("judgment_strength_after")
        before_ranking = _text_items(
            check.get("option_ranking_before"),
            field=f"red_team_report.stability_checks[{index}].option_ranking_before",
        )
        after_ranking = _text_items(
            check.get("option_ranking_after"),
            field=f"red_team_report.stability_checks[{index}].option_ranking_after",
        )
        if after_position != position.get("central_claim_id"):
            raise ValueError(
                f"stability check {index} after-position does not bind the locked position"
            )
        if after_strength != position.get("judgment_strength"):
            raise ValueError(
                f"stability check {index} after-strength does not bind the locked position"
            )
        state_changed = (
            before_position != after_position
            or before_strength != after_strength
            or before_ranking != after_ranking
        )
        if drift == "unjustified":
            raise ValueError(f"stability check {index} records unjustified position drift")
        if before == after and (drift != "none" or state_changed):
            raise ValueError(
                f"stability check {index} changes position without changed evidence"
            )
        if drift == "none" and state_changed:
            raise ValueError(
                f"stability check {index} self-reports no drift but changes locked state"
            )
        if drift == "justified_by_evidence" and not state_changed:
            raise ValueError(
                f"stability check {index} reports evidence-driven drift without a state change"
            )
        if before != after and drift not in {"none", "justified_by_evidence"}:
            raise ValueError(f"stability check {index} has an invalid evidence-bound drift")
        explanation = str(check.get("explanation", ""))
        if not state_changed and _contains_any(explanation, _POSITIVE_DRIFT_CLAIMS):
            raise ValueError(
                f"stability check {index} explanation contradicts its frozen probe states"
            )

    return copy.deepcopy(position)


def validate_recommendation_semantics(
    run_contract: Mapping[str, object],
    recommendation: Mapping[str, object],
    *,
    position: Mapping[str, object],
    expected_run_id: str,
    expected_source_snapshot_sha256: str,
) -> dict[str, object]:
    """Validate the closed recommendation/not-requested branch for one run."""

    if not isinstance(run_contract, Mapping):
        raise ValueError("run contract must be a structured object")
    if run_contract.get("run_id") != expected_run_id:
        raise ValueError("run contract is bound to a different run")
    if run_contract.get("source_snapshot_sha256") != expected_source_snapshot_sha256:
        raise ValueError("run contract is bound to a different source snapshot")
    required = run_contract.get("recommendation_required")
    if type(required) is not bool:
        raise ValueError("run contract recommendation_required must be a real boolean")
    if not isinstance(recommendation, Mapping):
        raise ValueError("recommendation artifact must be a structured object")
    normalized_input = copy.deepcopy(dict(recommendation))
    if not required:
        if normalized_input != {"status": "not_requested"}:
            raise ValueError(
                "recommendation_required=false requires the exact closed not_requested artifact"
            )
        return normalized_input
    if normalized_input == {"status": "not_requested"}:
        raise ValueError("a required recommendation cannot use the not_requested branch")

    locked_position = validate_position_lock(
        position,
        expected_run_id=expected_run_id,
        expected_source_snapshot_sha256=expected_source_snapshot_sha256,
    )
    normalized = validate_recommendation_lock(
        normalized_input,
        expected_run_id=expected_run_id,
        expected_source_snapshot_sha256=expected_source_snapshot_sha256,
    )
    if normalized.get("position_sha256") != sha256_json(locked_position):
        raise ValueError("recommendation is bound to a stale or different position")
    if _timestamp(normalized.get("locked_at"), field="recommendation.locked_at") <= _timestamp(
        locked_position.get("locked_at"), field="position.locked_at"
    ):
        raise ValueError("recommendation must be locked after the position")

    options = _mapping_items(normalized.get("options"), field="recommendation.options")
    option_ids = [item.get("option_id") for item in options]
    if any(not isinstance(item, str) for item in option_ids) or len(set(option_ids)) != len(option_ids):
        raise ValueError("recommendation option IDs must be unique text")
    action_kinds = {item.get("action_kind") for item in options}
    if action_kinds != _REQUIRED_ACTION_KINDS:
        raise ValueError("recommendation must cover all six action kinds")

    ranking = _text_items(normalized.get("ranking"), field="recommendation.ranking")
    if len(ranking) != len(option_ids) or set(ranking) != set(option_ids):
        raise ValueError("recommendation ranking must be a permutation of every option")
    preferred = normalized.get("preferred_option_id")
    second = normalized.get("second_option_id")
    if preferred != ranking[0] or second != ranking[1] or preferred == second:
        raise ValueError("preferred and second options must match ranking positions one and two")

    switch_conditions = _text_items(
        normalized.get("switch_conditions"), field="recommendation.switch_conditions"
    )
    if not any(str(second) in condition for condition in switch_conditions):
        raise ValueError("switch conditions must identify the ranked second option")
    _text_items(
        normalized.get("inaction_consequences"),
        field="recommendation.inaction_consequences",
    )

    if normalized.get("authorization_status") == "authorized":
        raise ValueError("analysis cannot grant recommendation authorization")
    for option in options:
        _text_items(option.get("stop_conditions"), field="recommendation option stop_conditions")
        _text_items(option.get("rollback"), field="recommendation option rollback")
        if option.get("authorization_status") == "authorized":
            raise ValueError("an option cannot self-grant real-world authorization")
    joined_text = "\n".join(_all_text(normalized))
    if _contains_any(joined_text, _ACTION_GRANT_MARKERS):
        raise ValueError("recommendation text leaks real-world authorization")

    return copy.deepcopy(normalized)
