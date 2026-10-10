# P07 — Semantic POI Enrichment for Task-Oriented Wayfinding

## Status
**P07-01: Semantic Data Foundation — v0.1**

## Project type
Independent GIScience portfolio project focused on semantic spatial modelling and task-oriented wayfinding.

## Study area
Wujiaochang Subdistrict, Yangpu District, Shanghai.

## Core question
**How can raw spatial objects be transformed into task-relevant semantic cues for pedestrian wayfinding?**

The project does not treat a POI merely as a mapped object. It asks which spatial entities may function as destinations, landmarks, contextual anchors or later decision-point cues in a route representation.

## Why this project
Earlier projects demonstrated network accessibility, remote sensing / spatial machine learning, and multi-source planning-oriented decision support. P07 adds a different capability: **semantic spatial data modelling and rule-based spatial reasoning**.

P07 deliberately stops before natural-language route generation. The planned next-stage project will use the structured semantic representation as input to route-description generation.

## Data
- Geofabrik Shanghai OpenStreetMap PBF snapshot: 2026-09-29.
- Operational Wujiaochang subdistrict boundary reused from the audited P06 spatial database.

## v0.1 implementation
1. Extract point and polygon spatial objects within Wujiaochang.
2. Recover OSM semantic tags from explicit fields and `other_tags`.
3. Harmonize heterogeneous OSM tags into navigation-oriented semantic classes.
4. Assign a preliminary navigation-role candidate:
   - `landmark_candidate`
   - `destination_candidate`
   - `context_candidate`
   - `unclassified`
5. Convert polygon POIs to representative points for later network and relative-position reasoning while preserving source geometry as WKT.
6. Store the result in a GeoPackage with an auditable semantic POI table.

## Current output
- Semantic POI candidates: **381**
- Semantic classes: **12**
- GeoPackage: `p07_wujiaochang_semantic_poi.gpkg`

## Planned analytical chain
Raw OSM object → semantic harmonisation → decision-point detection → POI/decision-point association → relative spatial relation → cue salience → structured route cue representation.

## Important limitations
- OSM POI completeness is uneven and should not be interpreted as a complete business or facility register.
- The v0.1 navigation role is a transparent rule-based candidate label, not a validated cognitive-salience measure.
- Polygon representative points are analytical anchors for semantic reasoning; they are not automatically equivalent to real entrances.
- The Wujiaochang boundary is operational OSM geometry rather than a legal cadastral boundary.
- Natural-language instructions are outside the v0.1 scope.

## Technology
Python · GeoPandas · Shapely · GeoPackage · OpenStreetMap PBF · Git/GitHub

## Version
**v0.1 — Semantic data foundation**
