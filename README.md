# P07 — Semantic POI Enrichment for Task-Oriented Wayfinding

## Status
**P07-05: Schema Validation & Final Route-Event Delivery — v0.5**

## Project type
Independent GIScience portfolio project focused on semantic spatial modelling and task-oriented pedestrian wayfinding.

## Study area
Wujiaochang Subdistrict, Yangpu District, Shanghai.

## Core question
**How can mapped spatial objects be transformed into structured, route-relevant semantic cues for pedestrian wayfinding?**

P07 separates raw spatial objects, semantic POIs, network decision points, route-context cue relations and structured route events. The final v0.5 delivery provides a validated machine-readable representation that can be handed to a later route-expression stage without generating natural-language instructions prematurely.

## Analytical progression
- **v0.1:** semantic POI foundation
- **v0.2:** decision points and local semantic association
- **v0.3:** route-context spatial relations
- **v0.4:** structured route-cue representation
- **v0.5:** schema validation and final delivery

## Final representation
Each route event contains:
- route ID and event sequence;
- decision-point reference;
- maneuver and turn angle;
- junction type and network degree;
- chainage along route;
- semantic-cue availability;
- cue semantic class and Tier A/B status where available;
- cue lateral relation;
- cue longitudinal offset and `before / at / after decision` relation;
- cue-function candidate.

## Validation
The final route-event representation passed all **10** core consistency checks.

| check                                  |   observed |   expected | status   |
|:---------------------------------------|-----------:|-----------:|:---------|
| unique_route_event_id                  |         36 |         36 | PASS     |
| all_route_ids_resolve                  |         36 |         36 | PASS     |
| all_decision_ids_resolve               |         36 |         36 | PASS     |
| route_sequence_contiguous              |          3 |          3 | PASS     |
| decision_chainage_monotonic            |          3 |          3 | PASS     |
| supported_event_cue_fields_complete    |         17 |         17 | PASS     |
| unsupported_event_cue_fields_null      |         19 |         19 | PASS     |
| supported_cues_resolve_to_semantic_poi |         17 |         17 | PASS     |
| supported_cue_tiers_valid              |         17 |         17 | PASS     |
| longitudinal_relation_consistent       |         17 |         17 | PASS     |

These checks cover identifier uniqueness, route and decision references, route-event sequence continuity, chainage ordering, cue-field completeness, null handling for unsupported events, POI reference consistency, cue-tier constraints and longitudinal-relation consistency.

## Demonstration-route completeness

| route_id   |   total_events |   supported_events |   turning_events |   supported_turns |   unsupported_turns |   event_support_pct |   turn_support_pct |
|:-----------|---------------:|-------------------:|-----------------:|------------------:|--------------------:|--------------------:|-------------------:|
| P07_R01    |             19 |                  6 |                7 |                 3 |                   4 |                31.6 |               42.9 |
| P07_R02    |              6 |                  5 |                3 |                 3 |                   0 |                83.3 |              100   |
| P07_R03    |             11 |                  6 |                6 |                 3 |                   3 |                54.5 |               50   |

The three routes remain reproducible demonstration cases rather than a statistical sample of all trips.

## Final v0.5 visual outputs
The final public visual set uses one global numbering sequence across map and chart directories:

1. `outputs/maps/01_route_event_cue_gaps.png`
2. `outputs/charts/02_structured_route_event_sequence.png`

The two figures answer different questions:
- **01** identifies where actual turning events lack an eligible semantic cue.
- **02** shows how the final event schema represents route order, maneuvers and cue-supported events.

Plot and legend / explanation regions are physically separated. Simplified Chinese text is rendered with an SC CJK font to avoid regional glyph variants.

## Structured delivery
- `outputs/structured_route_events_v0.5.json`
- `docs/route_event_schema_v0.5.json`
- `outputs/tables/route_event_validation_v0.5.csv`
- `outputs/tables/route_representation_completeness_v0.5.csv`

The JSON delivery preserves the route → event sequence → cue hierarchy and provides a clean hand-off for later route-expression or prototype work.

## GeoPackage
`p07_wujiaochang_semantic_poi.gpkg` contains the spatial layers accumulated through the project, including:
- `study_boundary`
- `semantic_poi_candidates`
- `pedestrian_network_context`
- `decision_point_candidates`
- `primary_semantic_cues`
- `demonstration_routes`
- `route_context_decisions`
- `route_context_cues`
- `structured_route_events`

## Main findings
The project shows that semantic POI availability and route-event support are not equivalent. A route can contain many mapped objects while still lacking an eligible semantic anchor at specific direction-changing events.

Across the three demonstration routes, turning-event cue support ranges from **42.9%** to **100.0%**. This makes cue gaps visible at the event level rather than hiding them inside route-level POI counts.

## Limitations
- OSM POI completeness is uneven.
- Network degree is a structural proxy for potential decision points.
- Demonstration routes are reproducible examples rather than observed user trips.
- Cue tiers, distance thresholds, longitudinal partitions and cue-function labels are transparent internal analytical rules rather than validated perceptual standards.
- A missing A/B cue can reflect true local scarcity, incomplete tagging or limitations of the screening model.
- The project does not claim that selected cues are preferred by blind or low-vision travellers without user validation.

## Technology
Python · GeoPandas · NetworkX · SciPy · Shapely · GeoPackage · OpenStreetMap-derived data · Git/GitHub

## Version
**v0.5 — Schema validation and final route-event delivery**
