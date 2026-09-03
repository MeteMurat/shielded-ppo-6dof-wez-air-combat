#!/usr/bin/env python3
"""Read-only consistency check for the P0-7F2/P0-7F3 publication state.

This script does not train a controller, run the 6-DoF simulator, or recompute
scientific results. It verifies that the publication-facing summary files carry
the frozen values and conservative inference statuses cited by the manuscript.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RESULTS = ROOT / "results"

EXPECTED_AGG = {
    "ppo": {
        "effective_win": 0.6883333333333334,
        "own_wez": 0.009367506679786985,
        "opp_wez": 0.004779284669935975,
        "max_G": 9.166519089014791,
        "G_integral": 582.4997718601679,
    },
    "ppo_shield": {
        "effective_win": 0.7816666666666666,
        "own_wez": 0.019123775307726156,
        "opp_wez": 0.003670285115272355,
        "max_G": 9.370249124368586,
        "G_integral": 597.9596212524121,
    },
}


def close(a: float, b: float, tol: float = 1e-12) -> bool:
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


with (RESULTS / "P0_7F2_CONTROLLER_SUMMARY.csv").open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
agg = {r["controller"]: r for r in rows if r["scope"] == "aggregate_theta_3_5"}
assert set(agg) == {"ppo", "ppo_shield"}
for controller, expected in EXPECTED_AGG.items():
    for metric, value in expected.items():
        assert close(float(agg[controller][metric]), value), (controller, metric)

with (RESULTS / "P0_7F3_FINAL_ADJUDICATION.json").open(encoding="utf-8") as f:
    f3 = json.load(f)
assert f3["status"] == "PASS_SEED_BLOCK_INFERENCE_POSTFLIGHT"
for metric, item in f3["aggregate_results"].items():
    assert item["status"] == "UNRESOLVED_ACROSS_TRAINING_SEEDS", metric
assert f3["theta5_results"]["G_integral"]["status"] == "ROBUST_NEGATIVE"
assert close(f3["theta5_results"]["G_integral"]["delta"], -65.94497033234245)

with (RESULTS / "P0_7F2_FINAL_ADJUDICATION.json").open(encoding="utf-8") as f:
    f2 = json.load(f)
assert f2["status"] == "PASS_MATCHED_EVALUATION_TRUE_COORDINATE_FREEZE"
assert f2["evaluation_design"]["matched_initial_conditions"] is True
assert f2["new_training_performed"] is False

print("PASS: publication-facing P0-7F2/P0-7F3 values and guardrails are internally consistent.")
