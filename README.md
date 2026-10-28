# Route-Relevant Semantic Cue Availability at Pedestrian Decision Points

## Study

This repository contains the initial spatial representation developed for a study of semantic cues at pedestrian decision points in Shanghai. The publicly available spatial data currently cover Wujiaochang Subdistrict, Yangpu District. The repository's existing release contains three demonstration routes and 36 structured route events.

The study distinguishes semantic objects recorded in geographic data from candidate cues available at particular route decisions. Decision-point associations are derived from pedestrian-network topology and proximity to named semantic POIs. Route context determines the selected candidate's spatial relation to travel direction.

The Tier A/B criteria identify candidate support under explicit screening rules. They do not measure pedestrian perception or demonstrated navigation effectiveness.

## Data

`p07_wujiaochang_semantic_poi.gpkg` contains the Wujiaochang study boundary, semantic POI candidates, pedestrian network, decision points, route-context relations and demonstration routes.

The source registry is in [docs/source_registry.csv](docs/source_registry.csv). The analysis uses an OpenStreetMap-derived Shanghai snapshot dated 29 September 2026 and an operational Wujiaochang boundary. The boundary is not a legal cadastral boundary.

The structured records for the three demonstration routes are in [outputs/structured_route_events_v0.5.json](outputs/structured_route_events_v0.5.json). Their schema is in [docs/route_event_schema_v0.5.json](docs/route_event_schema_v0.5.json).

## Spatial representation

The existing implementation uses pedestrian-network vertices with degree ≥ 3 as decision-point candidates. Nearby semantic POIs are assigned tier labels using their names, candidate roles, local class uniqueness and spatial distance. Route-context attributes include maneuver, chainage, lateral relation and position before, at or after a decision.

The screening rules and validation procedures are recorded in [docs/methodology_v0.2.md](docs/methodology_v0.2.md), [docs/methodology_v0.3.md](docs/methodology_v0.3.md), [docs/methodology_v0.4.md](docs/methodology_v0.4.md) and [docs/methodology_v0.5.md](docs/methodology_v0.5.md).

## Code and outputs

The `src/` directory contains the extraction specification, decision-point association analysis, spatial-relation functions and route-event validation. The initial extraction file does not yet implement a complete raw-data-to-GeoPackage pipeline. The current scripts therefore do not reproduce all published files from the original OSM snapshot.

Numerical summaries are in `outputs/tables/`. Existing maps and charts are in `outputs/maps/` and `outputs/charts/`. Some files retain earlier development-version suffixes.

## Current coverage

| Measure | Wujiaochang demonstration data |
|---|---:|
| Routes | 3 |
| Structured route events | 36 |
| Cue-supported events | 17 |
| Events without a selected cue | 19 |

These are demonstration data, not the district-wide analysis population. Results from the subsequent Yangpu District study, including its route sample, event population and sensitivity analyses, are not yet deposited in this repository.

## Source and interpretation

OpenStreetMap data are © OpenStreetMap contributors and subject to the Open Database License. The analysis treats mapped POIs as an incomplete observation of the environment. Network junctions are structural candidates, and a cue class represents modelled availability rather than observed pedestrian use.
