# Methodology — v0.4

## 1. Purpose
v0.4 turns route-context cue evidence into a structured route-event representation.

The output is designed to support later route-expression work while keeping the current project focused on spatial modelling.

## 2. Route-event unit
One route event is created for every v0.3 route-context decision point.

Each event stores:
- route ID and sequence,
- decision-point ID,
- maneuver,
- turn angle,
- junction type and degree,
- route chainage,
- semantic-cue availability,
- cue attributes where available.

## 3. Longitudinal relation
Both the decision point and selected cue are projected onto the route polyline.

The cue's longitudinal offset is:

`cue projected chainage - decision-point chainage`

Classification:
- `< -20 m` → `before_decision`
- `-20 m to +20 m` → `at_decision`
- `> +20 m` → `after_decision`

The ±20 m threshold is used only to create reproducible event semantics.

## 4. Lateral relation
Cue side is calculated relative to the local route tangent at the cue's projected route location.

The signed 2D cross product determines `left` or `right`. A cue exactly on the route is labelled `on_route`.

## 5. Cue-function candidate
The candidate function is derived from maneuver and longitudinal relation.

For turning events:
- before → `approach_anchor_candidate`
- at → `turn_anchor_candidate`
- after → `post_turn_confirmation_candidate`

For continue-through events:
- before → `approach_context_candidate`
- at → `continuity_anchor_candidate`
- after → `continuity_confirmation_candidate`

Events without a display-quality A/B cue are labelled `unsupported_event`.

These labels describe route-context structure only; they are not validated behavioural constructs.

## 6. Cue-gap analysis
Unsupported events are separated into:
- `unsupported_turn_event`
- `unsupported_continue_event`

This distinction prevents overall route-level cue coverage from masking missing semantic support at actual direction changes.

## 7. Visualization
The worked-example map is selected by:
1. highest number of unsupported turning events;
2. then highest number of turning events;
3. then route ID as deterministic tie-break.

The map marks supported turns, unsupported turns, supported continue-through events and unsupported continue-through events.

The comparison chart reports cue-support percentages for turning and continue-through events separately.

## 8. Interpretation
The v0.4 schema represents a transition from semantic spatial reasoning to instruction-ready event structure.

No natural-language generation is performed in this version.
