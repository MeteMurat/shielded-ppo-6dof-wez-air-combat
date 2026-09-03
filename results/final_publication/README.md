# Final publication data: P0-7F2 / P0-7F3

This directory contains the publication-facing final matched-evaluation and seed-aware inference records for the manuscript.

Scientific authority is defined by `../PUBLICATION_AUTHORITY_P0_7F2_P0_7F3.md`.

## Authority hierarchy

1. **P0-7F2** is the final matched-evaluation authority. It uses frozen corrected checkpoints, explicit identical initial engagement geometries inside every PPO--shielded-PPO evaluation pair, and the same geometry records across the 3 deg and 5 deg WEZ strata.
2. **P0-7F3** is the final inferential authority. It supersedes the earlier P0-7F2 hierarchical-uncertainty intervals for manuscript-level directional claims by preserving training-seed identity and matched-episode identity as common resampling blocks across the two WEZ strata.
3. Earlier exploratory, pre-correction, or pre-P0-7F3 result files elsewhere in the repository are retained only for provenance and must not be used as publication-authoritative evidence.

## Final design

- 12 independently trained controller-threshold-seed units;
- 50 deterministic evaluation episodes per cell;
- 600 controller episodes;
- 300 exactly matched PPO--shielded-PPO episode pairs;
- WEZ thresholds 3 deg and 5 deg;
- three independent training seeds;
- seed-block bootstrap plus three-seed Student-t inference.

## Publication-facing files in this directory

- `P0_7F2_CONTROLLER_SUMMARY.csv`: aggregate P0-7F2 controller point estimates.
- `P0_7F2_UNIT_SUMMARY.csv`: per-threshold, per-controller, per-training-seed summaries.
- `P0_7F2_CHECKPOINT_HASHES.csv`: sanitized checkpoint SHA-256 binding without local filesystem paths.
- `P0_7F2_REPRESENTATIVE_SELECTIONS.csv`: representative replay selection rule and selected matched episode identifiers.
- `P0_7F2_SELECTED_REPLAY_SUMMARY.csv`: metrics and trajectory hashes for the selected replay pairs.
- `P0_7F2_FINAL_ADJUDICATION.json`: final P0-7F2 matched-evaluation authority.
- `P0_7F2_REPORT.txt`: P0-7F2 execution/adjudication summary.
- `P0_7F3_SEED_BLOCK_INFERENCE.csv`: final publication-level aggregate and 5 deg inference table.
- `P0_7F3_FINAL_ADJUDICATION.json`: final P0-7F3 inference authority.
- `P0_7F3_REPORT.txt`: P0-7F3 postflight summary.
- `FINAL_DATA_SHA256_MANIFEST.csv`: SHA-256 identifiers for the complete frozen P0-7F2/P0-7F3 data package, including larger raw matched-evaluation records.

The complete raw episode-level metrics, explicit matched initial-condition table, and matched paired-episode table are identified by SHA-256 in `FINAL_DATA_SHA256_MANIFEST.csv`. Publication-facing summaries and final adjudication/inference records are stored directly in this directory.

## Replay figures

Publication replay selections and the SHA-256 identifiers of the three exact vector-PDF manuscript figures are documented in `../../supplementary/true3d_replays/`. The manuscript submission package uses those exact vector-PDF assets. Superseded seed-0 replay material is isolated under `../../supplementary/legacy_seed0/`.

## Claim guardrail

All aggregate PPO-versus-shielded-PPO differences remain unresolved across the three independent training seeds. The sole robust directional controller difference is the reduction in integrated load-factor exposure for shielded PPO at the 5 deg WEZ threshold. No universal controller dominance, universal safety improvement, universal safety--effectiveness trade-off, formal safety guarantee, or discovery of a new canonical manoeuvre is claimed.
