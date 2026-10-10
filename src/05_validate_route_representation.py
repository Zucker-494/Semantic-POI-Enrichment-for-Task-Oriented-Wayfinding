"""P07 v0.5 representation validation.

The final delivery is blocked if a core consistency check fails.
"""
from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

def validate_json_delivery(path):
    payload = json.loads(Path(path).read_text(encoding="utf-8"))

    route_ids = set()
    event_ids = set()

    for route in payload["routes"]:
        assert route["route_id"] not in route_ids
        route_ids.add(route["route_id"])

        expected_sequence = 1
        for event in route["events"]:
            assert event["route_event_id"] not in event_ids
            event_ids.add(event["route_event_id"])

            assert event["sequence"] == expected_sequence
            expected_sequence += 1

            if event["has_semantic_cue"]:
                assert event["cue"] is not None
                assert event["cue"]["tier"] in {"A", "B"}
            else:
                assert event["cue"] is None

    return {
        "routes": len(route_ids),
        "events": len(event_ids)
    }

if __name__ == "__main__":
    result = validate_json_delivery(
        ROOT / "outputs/structured_route_events_v0.5.json"
    )
    print(result)
