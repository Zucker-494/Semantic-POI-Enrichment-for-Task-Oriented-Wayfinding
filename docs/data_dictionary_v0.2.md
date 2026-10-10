# Data Dictionary Addendum — v0.2

## `decision_point_candidates`
| Field | Meaning |
|---|---|
| decision_id | Stable decision-point identifier |
| network_degree | Number of graph edges incident to the network node |
| junction_type | `three_leg` or `multi_leg` |
| nearby_poi_count | Semantic POIs within the 100 m screening window |
| tier_a_count | Nearby Tier A cue candidates |
| tier_b_count | Nearby Tier B cue candidates |
| has_primary_cue | Whether an A/B primary cue was selected |
| geometry | Decision-point location |

## `primary_semantic_cues`
Contains the selected primary A/B semantic POI for decision points where such evidence exists.

## `decision_poi_associations_ab`
Line layer connecting decision points to all Tier A/B associated POIs. It is retained for spatial QA and is not intended as a route layer.

## Key table
`outputs/tables/decision_poi_associations_v0.2.csv` contains the complete 100 m candidate associations, including Tier C/D evidence.
