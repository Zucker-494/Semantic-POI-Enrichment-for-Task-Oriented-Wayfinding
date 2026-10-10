# Data Dictionary — v0.1

## `semantic_poi_candidates`

| Field | Meaning |
|---|---|
| semantic_poi_id | Stable project identifier |
| osm_id | Source OSM identifier |
| source_geom_type | Original point or polygon geometry |
| name | OSM name where available |
| amenity/shop/tourism/leisure/... | Recovered source semantic tags |
| semantic_class | Harmonised P07 semantic class |
| navigation_role_candidate | Preliminary role before route-context reasoning |
| source_snapshot | Source snapshot provenance |
| source_geometry_wkt | Original geometry retained as text when representative-point conversion is applied |
| geometry | Representative point used for later spatial reasoning |
