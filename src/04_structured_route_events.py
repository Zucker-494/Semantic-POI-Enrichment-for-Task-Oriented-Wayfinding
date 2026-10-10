"""P07 v0.4 structured route-event relations."""
import numpy as np

def longitudinal_class(offset_m):
    if offset_m < -20:
        return "before_decision"
    if offset_m > 20:
        return "after_decision"
    return "at_decision"

def cue_function_candidate(maneuver, longitudinal):
    if maneuver in {"left", "right"}:
        if longitudinal == "before_decision":
            return "approach_anchor_candidate"
        if longitudinal == "at_decision":
            return "turn_anchor_candidate"
        return "post_turn_confirmation_candidate"

    if longitudinal == "after_decision":
        return "continuity_confirmation_candidate"
    if longitudinal == "at_decision":
        return "continuity_anchor_candidate"
    return "approach_context_candidate"

def side_from_cross_product(route_tangent, cue_vector):
    u = np.asarray(route_tangent, dtype=float)
    v = np.asarray(cue_vector, dtype=float)

    if np.linalg.norm(v) == 0:
        return "on_route"

    u = u / np.linalg.norm(u)
    v = v / np.linalg.norm(v)
    cross = u[0] * v[1] - u[1] * v[0]

    if abs(cross) < 1e-9:
        return "on_route"
    return "left" if cross > 0 else "right"
