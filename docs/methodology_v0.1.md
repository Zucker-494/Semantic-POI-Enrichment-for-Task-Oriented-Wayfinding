# Methodology — v0.1

## Conceptual distinction
P07 distinguishes three levels:

1. **Spatial object** — an OSM geometry and its source tags.
2. **Semantic POI** — a spatial object mapped into a stable functional/navigation class.
3. **Navigation cue** — a semantic POI that becomes relevant in a specific route context.

v0.1 implements levels 1–2. Route-context relevance is intentionally deferred.

## Semantic classes
The first-pass taxonomy contains:
- retail
- food_drink
- transport
- health
- education
- civic
- leisure
- accommodation
- finance
- office_service
- visitor_landmark
- other_named

The taxonomy is designed for wayfinding analysis rather than for reproducing the full OSM tagging ontology.

## Preliminary navigation roles
`landmark_candidate` is assigned to named transport, civic, education, leisure or visitor-landmark features.
Named retail, food, health, finance, accommodation and office/service POIs are initially treated as `destination_candidate`.
Other named features remain `context_candidate`.

These are candidate roles only. A route-specific cue model will later incorporate proximity to decision points, local distinctiveness and relative spatial position.
