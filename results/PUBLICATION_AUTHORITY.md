# Publication authority and precedence

## Final quantitative chain

The manuscript-level controller comparison is governed by the following precedence order:

1. **P0-7F2** (`PASS_MATCHED_EVALUATION_TRUE_COORDINATE_FREEZE`) is the authority for final frozen matched-evaluation point estimates, explicit matched initial conditions, matched episode records, and representative true-coordinate replay selection.
2. **P0-7F3** (`PASS_SEED_BLOCK_INFERENCE_POSTFLIGHT`) is the authority for final uncertainty intervals and directional-claim adjudication. It supersedes the P0-7F2 hierarchical resampling intervals for manuscript inference while leaving P0-7F2 point estimates, checkpoints, and replay selections unchanged.
3. P0-7D remains the checkpoint authority underlying P0-7F2. No new training was performed in P0-7F2 or P0-7F3.

Older R3A2C/P0-7C/P0-7E numerical summaries are historical evidence only and must not be used for final manuscript claims.

## Final design

- WEZ thresholds: 3 deg and 5 deg
- training seeds: 0, 1, 2
- controllers: PPO and shielded PPO
- evaluation episodes per controller/threshold/seed: 50
- total controller episodes: 600
- exactly matched PPO–shielded-PPO pairs: 300
- maximum evaluation horizon: 300 decision steps
- deterministic post-training evaluation: yes
- identical explicit initial geometry within every controller pair: yes
- same explicit initial geometries reused across theta strata: yes

## Final inferential guardrail

A strong directional controller claim requires all of the following:

1. the P0-7F3 seed-block bootstrap 95% CI excludes zero;
2. the three-training-seed mean Student-t 95% CI excludes zero in the same direction;
3. all three training-seed mean differences share that non-zero direction.

All aggregate controller differences remain unresolved under this rule. The sole robust directional result is the reduction in integrated load-factor exposure at the 5 deg WEZ threshold.

## Files

P0-7F2 primary publication records are included directly in `results/` or inside the publication bundle under `scripts/publication/`:

- `P0_7F2_FINAL_ADJUDICATION.json`
- `P0_7F2_REPORT.txt`
- `P0_7F2_CONTROLLER_SUMMARY.csv`
- `P0_7F2_MATCHED_INITIAL_CONDITIONS.csv`
- `P0_7F2_MATCHED_PAIRED_EPISODES.csv`
- `P0_7F2_ALL_EPISODE_METRICS.csv`
- `P0_7F2_REPRESENTATIVE_SELECTIONS.csv`
- `P0_7F2_SELECTED_REPLAY_SUMMARY.csv`
- `P0_7F2_CHECKPOINT_BINDING.csv`
- `P0_7F2_UNIT_SUMMARY.csv`
- `P0_7F2_OUTPUT_SHA256.csv`

P0-7F3 primary publication records are included directly in `results/` or inside the publication bundle:

- `P0_7F3_FINAL_ADJUDICATION.json`
- `P0_7F3_REPORT.txt`
- `P0_7F3_SEED_BLOCK_INFERENCE.csv`
- `P0_7F3_OUTPUT_SHA256.csv`

The P0-7F2 hierarchical uncertainty file is retained inside the publication bundle for provenance, but its inferential intervals are superseded by P0-7F3.
