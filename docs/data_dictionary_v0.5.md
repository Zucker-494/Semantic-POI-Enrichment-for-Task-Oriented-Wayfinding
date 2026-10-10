# Data Dictionary Addendum — v0.5

## `outputs/structured_route_events_v0.5.json`

Top-level fields:
- `project`
- `representation_version`
- `study_area`
- `routes`

Each route contains:
- `route_id`
- `origin_name`
- `destination_name`
- `destination_class`
- `route_length_m`
- `events`

Each event contains:
- `route_event_id`
- `sequence`
- `decision_id`
- `maneuver`
- `turn_angle_deg`
- `junction_type`
- `network_degree`
- `decision_chainage_m`
- `has_semantic_cue`
- `cue`

When no eligible cue exists, `cue` is null.

When a cue exists, the nested cue object contains:
- `name`
- `semantic_class`
- `tier`
- `distance_m`
- `lateral_relation`
- `longitudinal_offset_m`
- `longitudinal_relation`
- `cross_track_m`
- `function_candidate`

## Validation tables
`route_event_validation_v0.5.csv` records project-level consistency checks.

`route_representation_completeness_v0.5.csv` reports event and turning-event support by demonstration route.
