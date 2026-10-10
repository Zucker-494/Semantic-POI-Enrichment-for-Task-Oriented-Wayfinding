"""P07 v0.2 decision-point and semantic-cue association.

Required GeoPackage layers:
- semantic_poi_candidates
- pedestrian_network_context
- study_boundary

The implementation uses transparent topological and distance rules rather than a weighted salience score.
"""
from pathlib import Path
import pandas as pd
import numpy as np
import geopandas as gpd
import networkx as nx
from shapely.geometry import Point
from scipy.spatial import cKDTree

ROOT = Path(__file__).resolve().parents[1]
GPKG = ROOT / "p07_wujiaochang_semantic_poi.gpkg"

def build_graph(network):
    graph = nx.Graph()
    for geom in network.geometry:
        parts = list(geom.geoms) if geom.geom_type == "MultiLineString" else [geom]
        for line in parts:
            if line.length <= 0:
                continue
            coords = list(line.coords)
            u = (round(coords[0][0], 3), round(coords[0][1], 3))
            v = (round(coords[-1][0], 3), round(coords[-1][1], 3))
            if u != v:
                graph.add_edge(u, v, length_m=float(line.length))
    return graph

def cue_tier(named, role, distance_m, locally_unique):
    if named and role == "landmark_candidate" and (
        distance_m <= 40 or (locally_unique and distance_m <= 60)
    ):
        return "A"
    if named and role in {"landmark_candidate", "destination_candidate"} and distance_m <= 60:
        return "B"
    if named and locally_unique and distance_m <= 80:
        return "B"
    if named and distance_m <= 100:
        return "C"
    return "D"

def main():
    boundary = gpd.read_file(GPKG, layer="study_boundary").to_crs(32651)
    poi = gpd.read_file(GPKG, layer="semantic_poi_candidates").to_crs(32651)
    network = gpd.read_file(GPKG, layer="pedestrian_network_context").to_crs(32651)
    graph = build_graph(network)

    study = boundary.geometry.iloc[0]
    decisions = []
    for node, degree in graph.degree():
        if degree >= 3 and Point(node).within(study):
            decisions.append({
                "node": node,
                "network_degree": degree,
                "junction_type": "three_leg" if degree == 3 else "multi_leg"
            })

    xy = np.array([[g.x, g.y] for g in poi.geometry])
    tree = cKDTree(xy)

    rows = []
    for i, decision in enumerate(decisions, 1):
        point = Point(decision["node"])
        idxs = tree.query_ball_point([point.x, point.y], r=100.0)
        local = poi.iloc[idxs]
        counts = local["semantic_class"].value_counts().to_dict()

        for idx in idxs:
            item = poi.iloc[idx]
            distance = point.distance(item.geometry)
            named = isinstance(item["name"], str) and item["name"].strip() != ""
            unique = counts.get(item["semantic_class"], 0) == 1
            rows.append({
                "decision_id": f"P07_DP_{i:04d}",
                "semantic_poi_id": item["semantic_poi_id"],
                "distance_m": distance,
                "locally_unique_class": unique,
                "cue_tier": cue_tier(
                    named,
                    item["navigation_role_candidate"],
                    distance,
                    unique
                )
            })

    pd.DataFrame(rows).to_csv(
        ROOT / "outputs/tables/recomputed_decision_poi_associations.csv",
        index=False,
        encoding="utf-8-sig"
    )

if __name__ == "__main__":
    main()
