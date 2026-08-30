# Shielded PPO 6-DoF WEZ Air-Combat Audit

This repository contains the reproducibility package for the manuscript:

**Quantifying the Safety--Effectiveness Trade-off of Shielded PPO in 6-DoF WEZ-Based Autonomous Air Combat**

## Scope

This repository supports a reproducible six-degree-of-freedom (6-DoF) weapon-engagement-zone (WEZ) audit comparing standard Proximal Policy Optimization (PPO) and shielded PPO in a within-visual-range unmanned combat aerial vehicle (UCAV) air-combat simulator.

The study does not claim a new PPO algorithm, a new canonical air-combat maneuver, or a formal HJB-optimal WEZ controller. The purpose is to quantify the empirical safety--effectiveness trade-off introduced by adding a rule-based safety shield to PPO.

## Repository structure

- src/: 6-DoF air-combat simulator and PPO / shielded-PPO source code.
- esults/: final postflight audit tables, manifests, and summary files.
- supplementary/true3d_replays/: true-coordinate 3D replay CSV files, representative figures, and supplementary replay videos/GIFs.
- scripts/: helper scripts for reproducibility and postflight analysis.

## Main reported result

Across the targeted WEZ thresholds theta in {3 deg, 5 deg}, standard PPO achieved an aggregate effective win rate of 0.788, whereas shielded PPO achieved 0.603. Shielded PPO reduced selected exposure and aggressiveness indicators, including the recorded WEZ exposure indicator and mean maximum load factor, but this came at a measurable combat-effectiveness cost.

## Supplementary replay evidence

The true-coordinate replay artefacts were generated from frozen PPO and shielded-PPO checkpoints without additional training or policy updates. The replay CSV files contain earth-frame aircraft trajectories for both aircraft.

## Citation

If you use this repository, please cite the associated manuscript once publication details are available.
