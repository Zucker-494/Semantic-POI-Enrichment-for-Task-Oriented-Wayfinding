# Data Dictionary Addendum — v0.3

## `demonstration_routes`
| Field | Meaning |
|---|---|
| route_id | Stable demonstration-route identifier |
| origin_name | Named transport origin |
| destination_name | Named semantic destination |
| destination_class | Destination semantic class |
| route_length_m | Shortest pedestrian-network route length |
| geometry | Route geometry |

## `route_context_decisions`
| Field | Meaning |
|---|---|
| route_id | Demonstration route |
| decision_id | Traversed topological decision point |
| sequence | Order along the route |
| maneuver | `continue`, `left`, or `right` |
| turn_angle_deg | Route deflection angle |
| has_primary_cue | Whether a display-quality A/B cue is available |
| cue_name | Selected semantic cue name |
| cue_tier | A or B |
| cue_distance_m | Decision-to-cue distance |
| cue_relative_position | `left`, `right`, `ahead`, or `behind` |
| geometry | Decision-point geometry |

## `route_context_cues`
Route-specific selected cue points.

## `route_context_cue_connectors`
Decision-to-cue connector lines retained for spatial QA and worked-example visualization.
