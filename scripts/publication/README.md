# Publication reproducibility notes

This directory belongs to the P0-7F2/P0-7F3 publication state.

The final manuscript authority is defined in `results/PUBLICATION_AUTHORITY.md`.

The scientific workflow is separated into two frozen stages:

- **P0-7F2:** deterministic matched post-training evaluation and true-coordinate replay freeze using the retained P0-7D corrected checkpoints.
- **P0-7F3:** read-only seed-block statistical inference applied to the P0-7F2 matched records; no new training and no new physics evaluation.

The publication branch deliberately removes superseded pre-P0-7F2 result summaries and legacy seed-0 replay artefacts from the visible final evidence tree. Git history retains those historical materials.

Final controller summaries, adjudication files, statistical inference output, replay selection metadata, and SHA-256 provenance are under `results/` and `supplementary/true3d_replays/`.
