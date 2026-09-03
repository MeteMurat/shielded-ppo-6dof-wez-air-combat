# Shielded PPO 6-DoF WEZ Air-Combat Audit

This repository is the reproducibility package for the manuscript:

**Supervisory Shielding for Proximal Policy Optimization in Six-Degree-of-Freedom Autonomous Air Combat: A Reproducible Matched Weapon-Engagement-Zone Audit**

## Scientific scope

The study compares standard Proximal Policy Optimization (PPO) and shielded PPO in a common six-degree-of-freedom (6-DoF) within-visual-range autonomous air-combat simulator.

The work does **not** claim a new PPO algorithm, a new canonical air-combat manoeuvre, or a formally verified safety controller. The contribution is an evaluation methodology that combines frozen post-training checkpoints, explicitly matched initial engagement geometries, directional weapon-engagement-zone (WEZ) metrics, training-seed-aware inference, and descriptive true-coordinate replay evidence.

## Final publication authority

The manuscript is governed by the final P0-7F2/P0-7F3 evaluation and inference state.

- WEZ thresholds: `theta in {3 deg, 5 deg}`.
- Training seeds: `{0, 1, 2}` for each controller-threshold configuration.
- Training budget: `50,000` environment interaction steps per training unit.
- Final evaluation: `600` controller episodes arranged as `300` exactly matched PPO--shielded-PPO episode pairs.
- Evaluation episodes per controller-threshold-seed cell: `50`.
- Independent controller-level replication unit: the independently trained policy realisation (training seed), not the repeated evaluation episode.
- Final aggregate uncertainty: P0-7F3 seed-block bootstrap preserving seed and matched-episode identity across the two WEZ strata, supplemented by a three-seed Student-t interval.

The publication-authoritative record is `results/PUBLICATION_AUTHORITY_P0_7F2_P0_7F3.md`, with machine-readable publication files in `results/final_publication/`.

## Final quantitative interpretation

Aggregate shield-minus-PPO point estimates are:

| Metric | PPO | Shielded PPO | Difference |
|---|---:|---:|---:|
| Effective win rate | 0.6883 | 0.7817 | +0.0933 |
| Ownship WEZ occupancy | 0.00937 | 0.01912 | +0.00976 |
| Opponent-WEZ exposure | 0.00478 | 0.00367 | -0.00111 |
| Mean maximum load factor | 9.167 | 9.370 | +0.204 |
| Integrated load-factor exposure | 582.50 | 597.96 | +15.46 |

None of these aggregate controller differences is resolved across the independent training seeds under the final conservative inference rule.

The sole robust directional controller difference occurs at the `5 deg` WEZ threshold:

- integrated load-factor exposure difference: `-65.945 g s`;
- seed-block 95% CI: `[-118.30, -14.26]`;
- three-seed Student-t 95% CI: `[-94.05, -37.84]`.

This threshold-specific result does not establish a general safety improvement or controller dominance.

## Supervisory-intervention audit

No action-changing supervisory interventions occur in the final `3 deg` matched evaluation. At `5 deg`, 68 action-changing interventions are observed, all in one independently trained shielded-PPO realisation:

- adversary-WEZ egress: 58;
- minimum-altitude recovery: 6;
- low-altitude manoeuvre restriction: 4;
- high-angle-of-attack recovery: 0.

These event counts are mechanistic descriptors and are not treated as independent policy replicates.

## Representative matched replay authority

The final manuscript uses the following representative matched true-coordinate replay selections:

| Role | WEZ threshold | Training seed | Matched episode |
|---|---:|---:|---:|
| Combined-audit representative | 3 deg | 2 | 7 |
| 3 deg threshold representative | 3 deg | 2 | 40 |
| 5 deg threshold representative | 5 deg | 1 | 33 |

Representative replays are descriptive trajectory-level evidence only. They are not additional inferential samples and are not evidence of a new canonical manoeuvre.

The exact publication figure filenames, byte sizes, and SHA-256 digests are recorded under `supplementary/true3d_replays/`. The manuscript submission package contains those exact vector-PDF figure assets. Superseded seed-0 replay artefacts are isolated under `supplementary/legacy_seed0/` and are not final publication evidence.

## Repository structure

- `src/`: 6-DoF air-combat simulator and PPO / shielded-PPO source material.
- `results/PUBLICATION_AUTHORITY_P0_7F2_P0_7F3.md`: human-readable publication authority and claim guardrails.
- `results/final_publication/`: publication-facing P0-7F2/P0-7F3 summaries, adjudications, seed-aware inference, checkpoint hashes, replay-selection records, and frozen-data SHA-256 manifest.
- `results/legacy_pre_P0_7F2/`: historical pre-final campaign outputs retained only for provenance.
- `supplementary/true3d_replays/`: publication replay selections and exact figure hash manifest.
- `supplementary/legacy_seed0/`: superseded seed-0 replay material retained only for provenance.
- `requirements-repro.txt`: compact dependency set for the publication reproducibility environment.

Large frozen raw matched-evaluation artefacts are identified by filename and SHA-256 in `results/final_publication/FINAL_DATA_SHA256_MANIFEST.csv`. Publication-facing summaries and final adjudication/inference records are stored directly in the repository.

## Reproducibility environment

The publication environment is based on Python 3.11. Principal package versions are:

- PyTorch 2.7.1
- NumPy 2.3.2
- SciPy 1.16.2
- pandas 2.3.1
- Matplotlib 3.10.3

The broader historical environment remains recorded under `src/requirements.txt`; `requirements-repro.txt` is the publication-facing compact dependency record.

## Claim guardrail

The final publication may state that supervisory filtering can reshape the acquired policy regime and that shielded PPO shows a robust reduction in integrated load-factor exposure at the 5 deg WEZ threshold. It must not claim universal controller dominance, a universal safety improvement, a universal safety--effectiveness trade-off, formal safety verification, or discovery of a new canonical manoeuvre.

## Citation

Please cite the associated manuscript once publication details become available.
