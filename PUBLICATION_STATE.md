# Publication State: P0-7F2 / P0-7F3

This file defines the publication-facing state of the repository for the manuscript:

**Supervisory Shielding for Proximal Policy Optimization in Six-Degree-of-Freedom Autonomous Air Combat: A Reproducible Matched Weapon-Engagement-Zone Audit**

## Authoritative scientific chain

The final manuscript is governed by two frozen stages:

1. **P0-7F2 — matched post-training evaluation and true-coordinate replay freeze**
   - no new training;
   - final frozen controller checkpoints retained;
   - WEZ thresholds: 3 deg and 5 deg;
   - training seeds: 0, 1, 2;
   - 50 deterministic evaluation episodes per controller-threshold-seed cell;
   - 600 controller episodes arranged as 300 exactly matched PPO--shielded-PPO episode pairs;
   - identical explicit initial engagement geometry within every matched pair;
   - the same explicit initial geometries reused across the 3 deg and 5 deg strata.

2. **P0-7F3 — seed-block postflight inference**
   - no new training;
   - no new physics evaluation;
   - P0-7F2 point estimates, checkpoints, matched geometries, and representative replay selections unchanged;
   - training-seed identity and matched-episode identity preserved as common blocks across the two final WEZ strata;
   - directional claims require both the seed-block 95% interval and three-seed Student-t 95% interval to exclude zero in the same direction, with all three training-seed mean differences sharing that direction.

## Final publication interpretation

All aggregate shield-minus-PPO controller differences remain unresolved across independently trained policy realisations under the final seed-aware inference rule.

The sole robust directional controller difference is the reduction in integrated load-factor exposure for shielded PPO at the 5 deg WEZ threshold:

- difference: -65.9449703 g s;
- seed-block 95% CI: [-118.302617, -14.2622387];
- three-seed Student-t 95% CI: [-94.0525457, -37.8373949].

The final publication therefore does **not** claim universal controller dominance, a universal safety improvement, a universal safety--effectiveness trade-off, formal safety verification, or discovery of a new canonical manoeuvre.

## Final representative replay authority

The final manuscript uses only the following matched true-coordinate representatives:

| Role | WEZ threshold | Training seed | Matched episode |
|---|---:|---:|---:|
| Combined-audit representative | 3 deg | 2 | 7 |
| 3 deg threshold representative | 3 deg | 2 | 40 |
| 5 deg threshold representative | 5 deg | 1 | 33 |

Replay figures and supplementary videos are descriptive trajectory-level evidence only. They are not additional inferential samples.

## Final supplementary 3D-video freeze

The following MP4 assets are synchronized on the `main` branch under `supplementary/true3d_videos/final/` and are generated only from the frozen P0-7F2 selected true-coordinate replay records:

| File | Role | Bytes | SHA-256 |
|---|---|---:|---|
| `matched_true_coordinate_replay_aggregate_theta3_seed2_ep7.mp4` | combined-audit representative | 838855 | `134702B4F5C3799F627F07E75E39D8E75BD80FA8F83B181DE70B8BE32E2C59B2` |
| `matched_true_coordinate_replay_theta3_seed2_ep40.mp4` | 3 deg threshold representative | 641852 | `08BC3F000D5784A55C80A244CBAB021EFC2F87EF763F22150728C88C153474DF` |
| `matched_true_coordinate_replay_theta5_seed1_ep33.mp4` | 5 deg threshold representative | 233987 | `6BC15E9BB10118AA70781B519D8A998D3D9CC1200E06C7FAA402273DB22F65A3` |

The synchronized video set performs no new training and no new physics evaluation. Video generation is a postflight visualisation of frozen trajectory records. The authoritative video manifest is `supplementary/true3d_videos/PUBLICATION_3D_VIDEO_MANIFEST.csv`.

## Repository precedence

Publication-facing quantitative authority is:

1. `results/PUBLICATION_AUTHORITY_P0_7F2_P0_7F3.md`;
2. `results/final_publication/`;
3. `supplementary/true3d_replays/` for representative replay provenance;
4. `supplementary/true3d_videos/` for descriptive supplementary video material.

Older exploratory or pre-P0-7F2 outputs are retained only for provenance and must not be used to support final manuscript claims.

## Publication freeze status

- scientific interpretation: **FINAL P0-7F2 / P0-7F3**;
- aggregate point estimates: frozen;
- seed-aware inference: frozen;
- representative replay selections: frozen;
- publication replay PDF assets: final selection fixed;
- supplementary 3D videos: **SYNCHRONIZED AND HASH-RECORDED ON `main`**;
- new training for video generation: **FALSE**;
- new physics evaluation for video generation: **FALSE**;
- manuscript Code/Data Availability statement: may now reference this frozen repository state.
