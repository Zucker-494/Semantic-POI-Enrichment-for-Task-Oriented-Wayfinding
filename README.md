# P07 — Semantic POI Enrichment for Task-Oriented Wayfinding

## Status
**P07-02: Decision Points & Semantic Cue Association — v0.2**

## Project type
Independent GIScience portfolio project focused on semantic spatial modelling and task-oriented pedestrian wayfinding.

## Study area
Wujiaochang Subdistrict, Yangpu District, Shanghai.

## Core question
**How can raw spatial objects be transformed into task-relevant semantic cues for pedestrian wayfinding?**

P07 treats mapped objects, network decision points and route-context cues as different analytical entities. A POI becomes useful for navigation only when its semantics and spatial relationship to a decision context make it relevant.

## v0.1 — semantic data foundation
The first stage extracted and harmonised OSM point and polygon objects into 12 navigation-oriented semantic classes and preliminary navigation-role candidates.

## v0.2 — decision points and semantic support
v0.2 connects the semantic POI model to the pedestrian network.

### Decision-point candidates
Topological intersections are extracted from the validated pedestrian routing network:
- degree 3 → `three_leg`
- degree ≥4 → `multi_leg`

Degree-1 endpoints and ordinary degree-2 network vertices are not treated as decision-point candidates in this stage.

### POI association
For every decision point, semantic POIs within a 100 m screening window are identified. The 100 m radius is an internal analytical search window, not a cognitive or planning standard.

### Cue tiers
Cue suitability is assigned through transparent rule tiers rather than a weighted composite score:

- **A — strong cue support:** named landmark candidate within 40 m, or a locally unique named landmark within 60 m.
- **B — usable cue support:** named landmark/destination within 60 m, or a locally unique named feature within 80 m.
- **C — contextual evidence:** other named features within 100 m.
- **D — weak/unusable in the current rule set.**

For each decision point, one primary A/B cue is selected where available, prioritising A over B, local semantic uniqueness, and then shorter distance.

## Current results
- Semantic POI candidates: **381**
- Decision-point candidates: **798**
- Three-leg junction candidates: **574**
- Multi-leg intersection candidates: **224**
- Decision–POI associations within 100 m: **1,587**
- Decision points with an A/B primary semantic cue: **295**

The map shows where pedestrian decision points have stronger semantic support in the current OSM-derived evidence. Grey points are not interpreted as deficient intersections; they simply do not have an A/B cue under the current rule set.

## Final v0.2 visual outputs
- `outputs/maps/01_decision_point_semantic_support.png`
- `outputs/charts/01_semantic_support_by_junction_type.png`

The plotting region and legend / interpretation region are physically separated in both figures.

## GeoPackage layers
- `study_boundary`
- `semantic_poi_candidates`
- `pedestrian_network_context`
- `decision_point_candidates`
- `primary_semantic_cues`
- `decision_poi_associations_ab`

## Planned analytical chain
Raw spatial object → semantic harmonisation → decision-point detection → POI association → route-specific relative spatial relation → cue selection → structured route-cue representation.

## Important limitations
- OSM POI completeness is uneven and should not be interpreted as a complete real-world inventory.
- Network degree is a topological proxy for potential decision points; actual route decisions are route-dependent.
- Cue tiers are transparent screening rules, not validated measures of cognitive salience.
- The 100 m association radius and tier distance thresholds are internal analytical parameters.
- Polygon representative points are analytical anchors and are not automatically equivalent to physical entrances.
- Natural-language route generation remains outside the v0.2 scope.

## Technology
Python · GeoPandas · NetworkX · SciPy · Shapely · GeoPackage · OpenStreetMap-derived data · Git/GitHub

## Version
**v0.2 — Decision points and semantic cue association**
