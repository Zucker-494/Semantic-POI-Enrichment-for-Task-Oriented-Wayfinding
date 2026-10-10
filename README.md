# P07 — Semantic POI Enrichment for Task-Oriented Wayfinding

## Status
**P07-04: Structured Route-Cue Representation — v0.4**

## Project type
Independent GIScience portfolio project focused on semantic spatial modelling and task-oriented pedestrian wayfinding.

## Study area
Wujiaochang Subdistrict, Yangpu District, Shanghai.

## Core question
**How can mapped spatial objects be transformed into structured, route-relevant semantic cues for pedestrian wayfinding?**

P07 separates five analytical entities:
1. raw spatial objects,
2. semantic POIs,
3. topological decision points,
4. route-context cue relations,
5. structured route events.

The project intentionally stops before natural-language route instruction generation.

## Analytical progression

### v0.1 — semantic data foundation
OSM objects were harmonised into navigation-oriented semantic classes and preliminary navigation-role candidates.

### v0.2 — decision points and semantic cue association
Topological junction candidates were extracted from the pedestrian network and associated with nearby semantic POIs using transparent A/B/C/D screening rules.

### v0.3 — route-context spatial relations
Reproducible demonstration routes were introduced. Traversed decision points were linked to display-quality A/B cues and cue position was represented relative to the incoming travel direction.

### v0.4 — structured route-cue representation
v0.4 converts route-context relationships into a structured event schema.

For every traversed route decision, the dataset records:
- route and sequence position,
- maneuver,
- turn angle,
- junction type,
- cue availability,
- cue tier,
- cue semantic class,
- lateral relation,
- longitudinal route relation,
- cue-function candidate.

## Longitudinal route relation
Cue position is compared with the decision point along route chainage:

- `before_decision`: projected cue position is more than 20 m before the decision;
- `at_decision`: projected cue position lies within ±20 m of the decision;
- `after_decision`: projected cue position is more than 20 m after the decision.

The ±20 m partition is an internal analytical parameter for reproducible representation, not a perceptual standard.

## Cue-function candidates
The structured representation distinguishes several candidate functions, for example:
- `turn_anchor_candidate`
- `post_turn_confirmation_candidate`
- `continuity_anchor_candidate`
- `continuity_confirmation_candidate`
- `approach_context_candidate`
- `unsupported_event`

These are analytical labels describing the cue's route context. They are not experimentally validated cognitive categories.

## Current results

| route_id   |   route_events |   supported_events |   turning_events |   supported_turns |   continue_events |   supported_continue |   overall_support_pct |   turn_support_pct |   continue_support_pct |
|:-----------|---------------:|-------------------:|-----------------:|------------------:|------------------:|---------------------:|----------------------:|-------------------:|-----------------------:|
| P07_R01    |             19 |                  6 |                7 |                 3 |                12 |                    3 |                  31.6 |               42.9 |                   25   |
| P07_R02    |              6 |                  5 |                3 |                 3 |                 3 |                    2 |                  83.3 |              100   |                   66.7 |
| P07_R03    |             11 |                  6 |                6 |                 3 |                 5 |                    3 |                  54.5 |               50   |                   60   |

Across the three demonstration routes:
- structured route events: **36**
- route events with a display-quality semantic cue: **17**
- unsupported route events: **19**
- unsupported turning events: **7**

The route-level results show that overall cue availability can hide important differences between turning events and continue-through events.

## Final v0.4 visual outputs
- `outputs/maps/01_route_event_cue_gaps.png`
- `outputs/charts/01_turn_vs_continue_cue_support.png`

The map and chart use physically separated plot and legend / interpretation panels. Superseded v0.1–v0.3 figures are not retained in the v0.4 public visual directories.

## Core tables
- `outputs/tables/structured_route_events_v0.4.csv`
- `outputs/tables/route_event_support_summary_v0.4.csv`
- `outputs/tables/cue_function_counts_v0.4.csv`
- `outputs/tables/route_cue_gap_events_v0.4.csv`

## GeoPackage
`p07_wujiaochang_semantic_poi.gpkg` now includes `structured_route_events` in addition to the earlier semantic POI, decision-point, route and route-context layers.

## Interpretation
The main contribution of v0.4 is a machine-readable route-event representation. It provides a clean hand-off from spatial reasoning to a later route-expression stage without generating language prematurely.

## Important limitations
- OSM POI completeness is uneven.
- Network degree is a structural proxy for possible decision points.
- Demonstration routes are reproducible examples rather than observed user trips.
- Cue tiers, the ±20 m longitudinal partition and cue-function labels are transparent internal analytical rules.
- A missing A/B cue can reflect local semantic scarcity, incomplete OSM tagging or limitations of the screening rules.
- The project does not claim that selected cues are preferred by blind or low-vision travellers without user validation.

## Technology
Python · GeoPandas · NetworkX · SciPy · Shapely · GeoPackage · OpenStreetMap-derived data · Git/GitHub

## Version
**v0.4 — Structured route-cue representation**
