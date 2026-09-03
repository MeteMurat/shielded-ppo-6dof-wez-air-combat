# Supplementary matched true-coordinate 3D videos

This directory is reserved for publication-facing supplementary 3D replay videos associated with the final P0-7F2 matched evaluation and the final P0-7F3 seed-aware interpretation state.

## Scientific status

The videos are descriptive trajectory-level visualisations generated from frozen selected true-coordinate replay records. They do not perform new controller training, do not perform new physics evaluation, and do not alter the frozen P0-7F2/P0-7F3 quantitative authority.

The videos are **not** additional inferential samples and must not be used to establish controller superiority, formal safety improvement, a universal safety--effectiveness trade-off, or discovery of a new canonical air-combat manoeuvre.

## Final video targets

The publication-facing video set corresponds to the same three frozen representative replay selections used by the manuscript:

1. `matched_true_coordinate_replay_aggregate_theta3_seed2_ep7.mp4`
   - combined-audit representative;
   - WEZ threshold: 3 deg;
   - training seed: 2;
   - matched episode: 7.

2. `matched_true_coordinate_replay_theta3_seed2_ep40.mp4`
   - 3 deg threshold representative;
   - training seed: 2;
   - matched episode: 40.

3. `matched_true_coordinate_replay_theta5_seed1_ep33.mp4`
   - 5 deg threshold representative;
   - training seed: 1;
   - matched episode: 33.

## Generation rule

Videos must be generated only from the frozen selected replay CSV records produced by P0-7F2. Regenerating the videos from those frozen records is a visualisation operation, not a new scientific evaluation.

A video manifest should record filename, selected replay identity, byte size, SHA-256 digest, generation script, and generation timestamp.
