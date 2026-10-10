# Data Dictionary Addendum — v0.4

## `structured_route_events`

| Field | Meaning |
|---|---|
| route_event_id | Stable route-event identifier |
| route_id | Demonstration route |
| sequence | Event order along route |
| decision_id | Traversed decision point |
| maneuver | `continue`, `left`, or `right` |
| turn_angle_deg | Route deflection angle |
| junction_type | Topological junction class |
| network_degree | Graph-node degree |
| decision_chainage_m | Distance along route to the decision point |
| has_semantic_cue | Whether an eligible display-quality A/B cue exists |
| cue_name | Selected cue name |
| cue_semantic_class | Harmonised semantic class |
| cue_tier | A or B |
| cue_distance_m | Decision-to-cue Euclidean distance |
| cue_lateral_relation | `left`, `right`, or `on_route` |
| cue_longitudinal_offset_m | Cue projected chainage minus decision chainage |
| cue_longitudinal_relation | `before_decision`, `at_decision`, or `after_decision` |
| cue_cross_track_m | Cue-to-route perpendicular distance |
| cue_function_candidate | Route-context function candidate |
| geometry | Decision-point geometry |

## `route_cue_gap_events_v0.4.csv`
Contains route events without an eligible semantic cue and distinguishes unsupported turns from unsupported continue-through events.
