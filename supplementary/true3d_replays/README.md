# True-Coordinate Replay Evidence

## Publication-facing replay authority

The final manuscript uses only matched true-coordinate trajectories selected from the frozen P0-7F2 evaluation:

| Role | WEZ threshold | Training seed | Matched episode |
|---|---:|---:|---:|
| Combined-audit representative | 3 deg | 2 | 7 |
| 3 deg threshold representative | 3 deg | 2 | 40 |
| 5 deg threshold representative | 5 deg | 1 | 33 |

Within each replay case, standard PPO and shielded PPO begin from the same explicitly specified initial engagement geometry. These trajectories are descriptive evidence only and are not additional inferential samples.

The publication figure source filenames are:

- `aggregate_theta_3_5__theta_3__seed_2__episode_7__MATCHED_3D.pdf`
- `theta_3__theta_3__seed_2__episode_40__MATCHED_3D.pdf`
- `theta_5__theta_5__seed_1__episode_33__MATCHED_3D.pdf`

Their exact file sizes and SHA-256 digests are recorded in `PUBLICATION_REPLAY_FIGURE_MANIFEST.csv`. The manuscript submission package uses those exact vector-PDF assets.

## Legacy artefacts

Superseded seed-0 replay images, animations, and trajectory CSV files have been moved out of the publication-facing directory to `../legacy_seed0/`. They are retained only for historical traceability and are **not** part of the final P0-7F2/P0-7F3 evidence.

Do not use legacy seed-0 replay outcomes to support claims about controller dominance, manoeuvre discovery, safety improvement, or the final matched evaluation.

## Interpretation guardrail

Replay evidence can illustrate differences in trajectory organisation, manoeuvre timing, persistence, and recombination of the fixed BFM library. Statistical claims must instead be based on the matched seed-aware evaluation documented in `results/PUBLICATION_AUTHORITY_P0_7F2_P0_7F3.md` and `results/final_publication/`.
