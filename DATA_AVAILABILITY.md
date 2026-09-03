# Data availability and publication scope

The publication-facing quantitative record is stored under `results/final_publication/` and is governed by `results/PUBLICATION_AUTHORITY_P0_7F2_P0_7F3.md`.

Directly stored publication files include controller summaries, per-training-seed summaries, sanitized checkpoint hashes, representative replay selections, replay-pair summaries, P0-7F2 and P0-7F3 adjudication/report files, and the final P0-7F3 seed-block inference table.

The complete frozen raw P0-7F2/P0-7F3 data package contains larger episode-level metrics, explicit matched initial-condition records, matched paired-episode records, and associated manifests. Their exact filenames and SHA-256 digests are recorded in `results/final_publication/FINAL_DATA_SHA256_MANIFEST.csv` so the frozen scientific objects can be unambiguously identified.

The final manuscript uses three vector-PDF matched replay figures. Their exact filenames, sizes, and SHA-256 digests are recorded in `supplementary/true3d_replays/PUBLICATION_REPLAY_FIGURE_MANIFEST.csv`; the manuscript submission package contains those exact vector-PDF assets.

Historical pre-P0-7F2 numerical outputs are isolated under `results/legacy_pre_P0_7F2/`, and superseded seed-0 replay material is isolated under `supplementary/legacy_seed0/`. Neither legacy location is publication-authoritative.

For manuscript-level inference, P0-7F3 supersedes earlier hierarchical uncertainty records. All aggregate controller differences remain unresolved across the three independent training seeds; the sole robust directional controller difference is the reduction in integrated load-factor exposure for shielded PPO at the 5 deg WEZ threshold.
