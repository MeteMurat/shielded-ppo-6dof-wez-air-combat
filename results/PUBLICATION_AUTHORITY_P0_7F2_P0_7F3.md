# Final Publication Authority: P0-7F2 / P0-7F3

This file records the publication-facing scientific authority for the manuscript and supersedes earlier exploratory, pilot, or pre-correction result summaries.

## Evaluation authority: P0-7F2

Final deterministic evaluation uses frozen post-training checkpoints and exactly matched initial engagement geometries.

- Controllers: standard PPO and shielded PPO
- WEZ thresholds: 3 deg and 5 deg
- Training seeds: 0, 1, 2
- Evaluation episodes per controller-threshold-seed cell: 50
- Total controller episodes: 600
- Exactly matched PPO--shielded-PPO pairs: 300
- Matching is based on explicit initial geometry, not nominal equality of random-number state after training.
- The same explicit episode geometries are reused across the 3 deg and 5 deg strata.

### Aggregate point estimates

| Metric | PPO | Shielded PPO | Shield-minus-PPO |
|---|---:|---:|---:|
| Effective win rate | 0.6883333333 | 0.7816666667 | +0.0933333333 |
| Ownship WEZ occupancy | 0.00936750668 | 0.01912377531 | +0.00975626863 |
| Opponent-WEZ exposure | 0.00477928467 | 0.00367028512 | -0.00110899955 |
| Mean maximum load factor | 9.166519089 | 9.370249124 | +0.203730035 |
| Integrated load-factor exposure | 582.49977186 | 597.95962125 | +15.4598494 |
| Mean episode intervention rate | 0 | 0.00224571296 | +0.00224571296 |

### Final representative true-coordinate replay selections

| Role | WEZ threshold | Training seed | Matched episode |
|---|---:|---:|---:|
| Combined-audit representative | 3 deg | 2 | 7 |
| 3 deg threshold representative | 3 deg | 2 | 40 |
| 5 deg threshold representative | 5 deg | 1 | 33 |

These replays are descriptive evidence only.

### Action-changing supervisory interventions

- 3 deg matched evaluation: 0 interventions.
- 5 deg matched evaluation: 68 interventions.
- All 68 interventions occur in training seed 0 of the shielded-PPO 5 deg evaluation.
- Adversary-WEZ egress: 58.
- Minimum-altitude recovery: 6.
- Low-altitude manoeuvre restriction: 4.
- High-angle-of-attack recovery: 0.

Intervention counts are mechanistic event counts, not independent inferential samples.

## Inferential authority: P0-7F3

Final aggregate inference preserves training-seed identity and matched episode identity as common blocks across the 3 deg and 5 deg WEZ strata.

A strong directional manuscript claim requires all three conditions:

1. seed-block bootstrap 95% CI excludes zero;
2. three-seed Student-t 95% CI excludes zero in the same direction;
3. all three training-seed mean differences have the same non-zero direction.

### Aggregate shield-minus-PPO inference

| Metric | Difference | Seed-block 95% CI | Three-seed t 95% CI | Final status |
|---|---:|---:|---:|---|
| Effective win rate | +0.0933333333 | [-0.236666667, 0.370000000] | [-0.683266018, 0.869932685] | unresolved across training seeds |
| Ownship WEZ occupancy | +0.00975626863 | [0.00449951733, 0.0164325832] | [-0.00590102245, 0.0254135597] | unresolved across training seeds |
| Opponent-WEZ exposure | -0.00110899955 | [-0.00403463764, 0.00186935424] | [-0.00847019334, 0.00625219423] | unresolved across training seeds |
| Mean maximum load factor | +0.203730035 | [-0.553588743, 0.944778585] | [-1.68667948, 2.09413955] | unresolved across training seeds |
| Integrated load-factor exposure | +15.4598494 | [-201.935927, 232.762250] | [-541.101559, 572.021258] | unresolved across training seeds |
| Mean episode intervention rate | +0.00224571296 | [0, 0.00638756885] | [-0.00741681002, 0.0119082359] | unresolved across training seeds |

### 5 deg threshold-specific result

| Metric | Difference | Seed-block 95% CI | Three-seed t 95% CI | Final status |
|---|---:|---:|---:|---|
| Effective win rate | +0.120 | [-0.193, 0.527] | [-0.824, 1.064] | unresolved |
| Ownship WEZ occupancy | +0.01743819 | [-0.00264, 0.03122] | [-0.02676, 0.06164] | unresolved |
| Opponent-WEZ exposure | -0.00163822 | [-0.00673, 0.00419] | [-0.01523, 0.01195] | unresolved |
| Mean maximum load factor | +0.281096 | [-0.0465, 0.6286] | [-0.5467, 1.1089] | unresolved |
| Integrated load-factor exposure | -65.9449703 | [-118.302617, -14.2622387] | [-94.0525457, -37.8373949] | robust negative |
| Mean episode intervention rate | +0.00449 | [0, 0.01282] | [-0.01483, 0.02382] | unresolved |

The 5 deg integrated load-factor exposure reduction is the sole robust directional controller difference in the final audit.

## Superseded claims

The following earlier claims are not publication-authoritative and must not be used in the manuscript, README, captions, or publication-facing summaries:

- aggregate PPO effective win rate 0.788 versus shielded PPO 0.603;
- a general shield-induced effectiveness loss;
- a general lower maximum load factor for shielded PPO;
- episode-level bootstrap intervals treated as controller-level inference;
- the older 5 deg seed-0 48-step PPO / 278-step shielded-PPO replay pair as the final representative replay;
- a universal safety--effectiveness trade-off.

## Claim guardrail

The final publication may state that supervisory filtering can reshape the acquired policy regime and that shielded PPO shows a robust reduction in integrated load-factor exposure at the 5 deg WEZ threshold. It must not claim universal controller dominance, a universal safety improvement, a universal safety--effectiveness trade-off, formal safety verification, or discovery of a new canonical manoeuvre.
