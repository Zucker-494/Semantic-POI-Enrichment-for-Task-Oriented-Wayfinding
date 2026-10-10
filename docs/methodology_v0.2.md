# Methodology — v0.2

## 1. Analytical entities
P07 separates:
1. spatial objects,
2. semantic POIs,
3. topological decision-point candidates,
4. decision–POI associations,
5. route-specific navigation cues.

v0.2 implements levels 1–4. Route-specific direction and relative-position reasoning are deferred to the next stage.

## 2. Decision-point extraction
The pedestrian routing network is represented as an undirected graph.

- degree 3 → three-leg junction candidate
- degree >=4 → multi-leg intersection candidate

Degree 2 is excluded because it usually represents continuity of the network rather than a topological choice point. This is a structural rule only; a later route can still require a turn at another location.

## 3. Semantic association window
All semantic POIs within 100 m Euclidean distance of a decision-point candidate are retrieved.

This distance is used only to create an auditable local candidate set. It is not claimed as a perceptual threshold.

## 4. Local distinctiveness
Within each 100 m candidate set, a semantic class is considered locally unique when it occurs only once. Local uniqueness is used as supporting evidence for cue selection.

## 5. Cue tiers
No weighted composite salience score is used.

### Tier A
- named `landmark_candidate` within 40 m; or
- locally unique named `landmark_candidate` within 60 m.

### Tier B
- named `landmark_candidate` or `destination_candidate` within 60 m; or
- locally unique named feature within 80 m.

### Tier C
- other named feature within 100 m.

### Tier D
- does not meet the above semantic / naming rules.

## 6. Primary cue selection
For each decision point, a primary cue is selected only from tiers A and B.

Selection order:
1. A before B;
2. locally unique class before repeated class;
3. shorter spatial distance.

The result is a reproducible screening hierarchy rather than a claim of experimentally validated landmark salience.

## 7. Interpretation
A/B support indicates that the current spatial dataset contains a plausible named semantic anchor near a topological decision point. Absence of A/B support can reflect genuine local scarcity, incomplete OSM tagging, or limitations of the rule system.
