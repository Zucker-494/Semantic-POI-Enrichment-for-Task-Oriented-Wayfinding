"""P07 v0.3 route-context spatial relations.

This module contains the deterministic route-context relation rules used by v0.3.
It is designed to be run against the project GeoPackage and v0.2 association tables.
"""
from pathlib import Path
import math
import re
import numpy as np

ROOT = Path(__file__).resolve().parents[1]

def display_name_ok(value):
    if not isinstance(value, str):
        return False
    value = value.strip()
    if len(value) < 2:
        return False
    if re.fullmatch(r"[\d\s\-_/\.]+", value):
        return False
    digit_share = sum(ch.isdigit() for ch in value) / len(value)
    return digit_share <= 0.6

def relative_position(incoming_vector, cue_vector):
    """Classify cue position relative to incoming travel direction."""
    u = np.asarray(incoming_vector, dtype=float)
    v = np.asarray(cue_vector, dtype=float)
    u = u / np.linalg.norm(u)
    v = v / np.linalg.norm(v)

    cross = u[0] * v[1] - u[1] * v[0]
    forward = float(np.dot(u, v))

    if abs(cross) >= 0.5:
        return "left" if cross > 0 else "right"
    return "ahead" if forward > 0 else "behind"

def select_candidate(candidates):
    """Select one display-quality A/B cue using the documented hierarchy."""
    candidates = candidates[
        candidates["cue_tier"].isin(["A", "B"]) &
        candidates["poi_name"].map(display_name_ok)
    ].copy()
    if candidates.empty:
        return None
    candidates["tier_rank"] = candidates["cue_tier"].map({"A": 0, "B": 1})
    candidates = candidates.sort_values(
        ["tier_rank", "locally_unique_class", "distance_m"],
        ascending=[True, False, True]
    )
    return candidates.iloc[0]
