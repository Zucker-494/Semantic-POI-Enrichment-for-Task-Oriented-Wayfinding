# Methodology — v0.3

## 1. Purpose
v0.3 converts local decision–POI associations into route-specific semantic relations.

The key distinction is:

`near a junction` is not the same as `relevant to a route decision`.

A route provides direction of travel, sequence and maneuver context. These allow a semantic POI to be described relative to the traveller's current movement.

## 2. Demonstration-route generation
Eligible origins are named transport features already classified as `landmark_candidate`.
Eligible destinations are named non-transport semantic POIs.

Candidate routes must have a shortest-path network length between 700 and 1,800 m.

A deterministic selection procedure then:
1. sorts candidate routes by absolute deviation from 1,200 m;
2. requires distinct destination classes;
3. requires distinct origin names;
4. requires distinct destination names;
5. retains the first three routes.

The 1,200 m target provides comparable worked examples only.

## 3. Route decision points
A topological decision-point candidate from v0.2 becomes a route-context decision point when its graph node lies on the calculated route.

A traversed decision point can therefore represent either:
- an actual left/right turn; or
- a junction passed through while continuing.

The latter can still be relevant for confirmation cues.

## 4. Display-name QA
Before route-specific cue selection, A/B POIs with names that are purely numeric, extremely short or predominantly numeric are excluded from the public cue layer.

This is a presentation and semantic-quality rule; the source POI record remains in the underlying semantic dataset.

## 5. Route-specific cue selection
At each traversed decision point, eligible A/B candidates are ordered by:
1. Tier A before Tier B;
2. locally unique semantic class before repeated class;
3. shorter decision–POI distance.

The first eligible cue becomes the route-specific primary cue.

## 6. Relative-position model
Let the incoming route direction be the unit vector `u`, and the decision-to-cue direction be the unit vector `v`.

The signed 2D cross product determines lateral side; the dot product determines forward/backward orientation.

Operational classification:
- if `|cross(u,v)| >= 0.5`, classify as `left` or `right` from the sign;
- otherwise classify as `ahead` when `dot(u,v) > 0`;
- otherwise classify as `behind`.

This corresponds to a transparent angular partition and is not presented as a perceptual standard.

## 7. Visualization
The worked-example route is selected from routes with at least 50% A/B cue coverage, then by:
1. most turning decisions;
2. most cue-supported decisions;
3. higher cue coverage;
4. route ID as deterministic tie-break.

If the same semantic POI supports multiple route decisions, it is drawn once as a cue symbol while each decision–cue connector is retained.

## 8. Interpretation
The v0.3 outputs demonstrate a reproducible transition from:
semantic POI → local junction association → route-context spatial relation.

They do not yet generate verbal instructions or claim that every selected cue would be preferred by blind or low-vision travellers.
