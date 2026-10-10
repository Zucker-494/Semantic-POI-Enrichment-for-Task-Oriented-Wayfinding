# Methodology — v0.5

## 1. Purpose
v0.5 closes P07 by validating and packaging the structured route-event representation.

No new POI class, route-selection rule or navigation-language model is introduced. The focus is delivery quality and internal consistency.

## 2. Validation dimensions
The final representation is checked for:

1. unique route-event identifiers;
2. valid route references;
3. valid decision-point references;
4. contiguous event sequence within each route;
5. non-decreasing route chainage;
6. complete cue attributes for cue-supported events;
7. clean null handling for unsupported events;
8. resolution of supported cues to the semantic POI layer;
9. valid A/B cue tiers;
10. consistency between numeric longitudinal offset and categorical longitudinal relation.

A failed core check blocks final delivery.

## 3. Structured JSON hand-off
The JSON output follows a nested hierarchy:

`route -> events -> optional cue`

Each event stores route order, decision reference, maneuver, junction attributes and cue information when available.

This structure is designed to support downstream route-expression or prototype work without embedding a particular natural-language template.

## 4. Visual selection
The final visual set is intentionally minimal.

### Figure 01
`01_route_event_cue_gaps.png`

Question:
Where do actual route turns lack an eligible semantic cue?

### Figure 02
`02_structured_route_event_sequence.png`

Question:
How is the validated route-event representation organised along an example route?

The map and chart use one shared numbering sequence rather than restarting figure numbering inside separate folders.

## 5. Typography and layout
Simplified Chinese text is rendered with a Simplified-Chinese CJK font rather than a Japanese CJK variant.

Analytical and explanatory regions are physically separated:
- left: map / chart;
- middle: fixed divider;
- right: legend, event details or interpretation.

## 6. Project boundary
P07 ends with structured route-event delivery.

Natural-language route instruction generation, user validation and prototype interaction belong to a later project stage rather than being added to P07.
