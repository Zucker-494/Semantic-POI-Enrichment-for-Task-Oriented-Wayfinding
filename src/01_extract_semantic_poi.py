"""P07 v0.1 semantic POI extraction.

Inputs:
- Shanghai OSM PBF snapshot
- audited operational Wujiaochang boundary

Produces:
- study_boundary
- semantic_poi_candidates

The script intentionally separates generic spatial objects from route-context navigation cues.
"""
# Delivered outputs were generated from the frozen project inputs.
# See docs/methodology_v0.1.md and docs/source_registry.csv for the operational rules.
