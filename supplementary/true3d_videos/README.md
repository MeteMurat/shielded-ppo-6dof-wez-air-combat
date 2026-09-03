# Supplementary matched true-coordinate 3D videos

This directory contains the publication-facing supplementary 3D replay-video record associated with the final P0-7F2 matched evaluation and the final P0-7F3 seed-aware interpretation state.

## Scientific status

The videos are descriptive trajectory-level visualisations generated only from frozen selected true-coordinate replay records. Generation performs no controller training and no new physics evaluation, and it does not alter the frozen P0-7F2/P0-7F3 quantitative authority.

The videos are **not** additional inferential samples and must not be used to establish controller superiority, formal safety improvement, a universal safety--effectiveness trade-off, or discovery of a new canonical air-combat manoeuvre.

## Frozen publication video set

The final publication video generator completed with
`PASS_PUBLICATION_3D_VIDEO_GENERATION_FROM_FROZEN_P0_7F2`.

| Video | Role | WEZ | Seed | Episode | Bytes | SHA-256 |
|---|---|---:|---:|---:|---:|---|
| `matched_true_coordinate_replay_aggregate_theta3_seed2_ep7.mp4` | combined-audit representative | 3 deg | 2 | 7 | 838855 | `134702B4F5C3799F627F07E75E39D8E75BD80FA8F83B181DE70B8BE32E2C59B2` |
| `matched_true_coordinate_replay_theta3_seed2_ep40.mp4` | 3 deg threshold representative | 3 deg | 2 | 40 | 641852 | `08BC3F000D5784A55C80A244CBAB021EFC2F87EF763F22150728C88C153474DF` |
| `matched_true_coordinate_replay_theta5_seed1_ep33.mp4` | 5 deg threshold representative | 5 deg | 1 | 33 | 233987 | `6BC15E9BB10118AA70781B519D8A998D3D9CC1200E06C7FAA402273DB22F65A3` |

The exact machine-generated manifest is retained as
`PUBLICATION_3D_VIDEO_MANIFEST.csv` and the generation summary as
`PUBLICATION_3D_VIDEO_REPORT.txt` once the binary publication assets are
synchronised to the repository.

## Provenance rule

The three videos correspond to the same frozen representative replay identities used by the manuscript:

1. combined-audit representative: theta = 3 deg, training seed = 2, matched episode = 7;
2. 3 deg representative: training seed = 2, matched episode = 40;
3. 5 deg representative: training seed = 1, matched episode = 33.

Video generation is a visualisation-only transformation of the frozen P0-7F2 selected replay records. Statistical claims remain governed exclusively by `results/PUBLICATION_AUTHORITY_P0_7F2_P0_7F3.md` and the machine-readable records under `results/final_publication/`.
