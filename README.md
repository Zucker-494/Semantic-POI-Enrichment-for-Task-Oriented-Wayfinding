# P07 — Semantic POI Enrichment for Task-Oriented Wayfinding

## Status
**P07-03: Route-Context Spatial Relations — v0.3**

## Project type
Independent GIScience portfolio project focused on semantic spatial modelling and task-oriented pedestrian wayfinding.

## Study area
Wujiaochang Subdistrict, Yangpu District, Shanghai.

## Core question
**How can raw spatial objects be transformed into route-relevant semantic cues for pedestrian wayfinding?**

P07 separates mapped objects, semantic POIs, topological decision points, and route-specific navigation cues. A POI is not treated as a navigation cue merely because it is nearby; its semantic role and its spatial relationship to an actual route decision are made explicit.

## Analytical progression

### v0.1 — semantic data foundation
OSM point and polygon objects were harmonised into navigation-oriented semantic classes and preliminary navigation-role candidates.

### v0.2 — decision points and semantic cue association
Topological junction candidates were extracted from the pedestrian network and associated with nearby semantic POIs using transparent A/B/C/D cue rules.

### v0.3 — route-context spatial relations
v0.3 introduces explicit route context.

Three reproducible demonstration routes are generated between named transport origins and named non-transport destinations. For each route:
1. the shortest pedestrian-network path is calculated;
2. topological decision points traversed by the route are identified;
3. eligible A/B semantic cues are re-screened with display-name QA;
4. cue position is classified relative to the incoming travel direction as `left`, `right`, `ahead`, or `behind`;
5. route-level semantic-cue coverage is summarised.

## Demonstration routes

| route_id   | origin_name    | destination_name   | destination_class   |   route_length_m |   decision_points |   cue_supported_decisions |   cue_coverage_pct |
|:-----------|:---------------|:-------------------|:--------------------|-----------------:|------------------:|--------------------------:|-------------------:|
| P07_R01    | 国定路政立路   | 小喜田             | food_drink          |           1200.9 |                19 |                         6 |               31.6 |
| P07_R02    | 政立路国权北路 | 国定路邮政所       | civic               |           1201.3 |                 6 |                         5 |               83.3 |
| P07_R03    | 武东路武川路   | 校史馆             | visitor_landmark    |           1203.6 |                11 |                         6 |               54.5 |

The routes are demonstration cases, not a statistical sample of all trips in Wujiaochang.

## Route selection rule
Candidate routes satisfy all of the following:
- origin: named transport `landmark_candidate`;
- destination: named non-transport semantic POI;
- network distance: 700–1,800 m;
- display-quality names only.

From the eligible set, routes are selected deterministically by proximity to a 1.2 km target length while enforcing distinct destination classes, origin names and destination names. The 1.2 km target is used only to produce comparable worked examples; it is not a planning or behavioural standard.

## Relative spatial relation
Cue position is calculated from the incoming route direction at each decision point.

- `ahead`: cue lies approximately along the incoming travel direction;
- `behind`: cue lies approximately opposite the incoming direction;
- `left` / `right`: cue is laterally offset from the incoming direction.

The angular partition is an internal analytical rule used to create reproducible route-context semantics. It is not claimed as a validated perceptual threshold.

## Current results
- Demonstration routes: **3**
- Route-context decision points: **36**
- Route-specific A/B cue relations: **17**
- Cue coverage ranges from **31.6%** to **83.3%** across the three demonstration routes.

## Final v0.3 visual outputs
- `outputs/maps/01_route_context_worked_example.png`
- `outputs/charts/01_route_semantic_cue_coverage.png`

The plotting region and legend / interpretation region are physically separated. Superseded v0.1/v0.2 figures are not retained in the v0.3 public visual directories.

## GeoPackage layers
- `study_boundary`
- `semantic_poi_candidates`
- `pedestrian_network_context`
- `decision_point_candidates`
- `primary_semantic_cues`
- `decision_poi_associations_ab`
- `demonstration_routes`
- `route_context_decisions`
- `route_context_cues`
- `route_context_cue_connectors`

## Planned analytical chain
Raw spatial object → semantic harmonisation → decision-point detection → local semantic association → route-context relation → cue-selection refinement → structured route-cue representation.

Natural-language instruction generation remains outside v0.3 and is intentionally reserved for a later project stage.

## Important limitations
- OSM POI completeness is uneven.
- Network degree is only a structural proxy for potential decision points.
- Demonstration routes are reproducible examples, not observed user trips.
- Cue tiers and angular relation rules are transparent internal parameters rather than validated cognitive-salience models.
- A repeated landmark may support more than one nearby route decision; the worked-example map merges duplicate cue symbols while retaining separate decision–cue connectors.
- Polygon representative points are analytical anchors and are not automatically equivalent to physical entrances.

## Technology
Python · GeoPandas · NetworkX · SciPy · Shapely · GeoPackage · OpenStreetMap-derived data · Git/GitHub

## Version
**v0.3 — Route-context spatial relations**
