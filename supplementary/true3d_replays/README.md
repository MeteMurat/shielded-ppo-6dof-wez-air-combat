# Final matched true-coordinate replay evidence

This directory contains publication-facing replay material from the **P0-7F2 matched-evaluation and true-coordinate freeze**.

## Authoritative manuscript selections

Only the following three representative replay figures are used for final manuscript interpretation:

1. `aggregate_theta_3_5__theta_3__seed_2__episode_7__MATCHED_3D.pdf`
   - combined-audit representative
   - theta = 3 deg
   - training seed = 2
   - matched episode = 7

2. `theta_3__theta_3__seed_2__episode_40__MATCHED_3D.pdf`
   - 3 deg threshold representative
   - training seed = 2
   - matched episode = 40

3. `theta_5__theta_5__seed_1__episode_33__MATCHED_3D.pdf`
   - 5 deg threshold representative
   - training seed = 1
   - matched episode = 33

The selection metadata and trajectory hashes are retained in the P0-7F2 publication records and the publication bundle under `scripts/publication/`.

## Interpretation guardrail

The replay figures are descriptive trajectory-level evidence. They are not additional independent evaluation samples, are not used to establish controller superiority or formal safety, and do not support discovery of a new canonical air-combat manoeuvre. Both controllers remain restricted to the same eight predefined BFM primitives.

Legacy seed-0 replay artefacts from the superseded pre-P0-7F2 evaluation have been removed from the publication-facing branch. They remain recoverable through Git history if needed for audit provenance.
