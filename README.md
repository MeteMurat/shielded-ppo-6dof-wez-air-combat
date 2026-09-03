# Supervisory Shielding for PPO in 6-DoF Autonomous Air Combat

This repository is the publication-facing reproducibility package for the manuscript:

**Supervisory Shielding for Proximal Policy Optimization in Six-Degree-of-Freedom Autonomous Air Combat: A Reproducible Matched Weapon-Engagement-Zone Audit**

## Scientific scope

The study compares standard Proximal Policy Optimization (PPO) and shielded PPO in the same six-degree-of-freedom (6-DoF) within-visual-range air-combat environment. It does **not** claim a new PPO objective, a new canonical air-combat manoeuvre, or a formally verified safety controller.

The publication contribution is an audit-oriented evaluation design: frozen post-training policies are compared using explicitly identical initial engagement geometries, directional weapon-engagement-zone (WEZ) metrics, and training-seed-aware uncertainty.

## Final publication authority

The manuscript-level quantitative authority is the two-stage frozen chain:

1. **P0-7F2 — matched evaluation + true-coordinate freeze**
   - no new training;
   - P0-7D corrected checkpoints retained;
   - WEZ thresholds: 3 deg and 5 deg;
   - training seeds: 0, 1, 2;
   - 50 deterministic evaluation episodes per controller/threshold/seed cell;
   - 600 controller episodes arranged as **300 exactly matched PPO–shielded-PPO pairs**;
   - identical explicit initial engagement geometry within every pair;
   - the same explicit geometries reused across the 3 deg and 5 deg strata.

2. **P0-7F3 — seed-block inference postflight**
   - no new training;
   - no new physics evaluation;
   - P0-7F2 point estimates, checkpoints, and replay authority unchanged;
   - training-seed identity and matched episode identity preserved as common blocks across the two WEZ strata;
   - strong directional claims require the seed-block bootstrap CI and three-seed mean t-CI to exclude zero in the same direction, with all three training-seed means sharing that direction.

Older R3A/P0-7C/P0-7E result files retained in repository history or legacy folders are **not** the final quantitative manuscript authority.

## Final aggregate point estimates

| Metric | PPO | Shielded PPO | Shield − PPO | Final inference |
|---|---:|---:|---:|---|
| Effective win rate | 0.6883 | 0.7817 | +0.0933 | unresolved across training seeds |
| Ownship WEZ occupancy | 0.00937 | 0.01912 | +0.00976 | unresolved across training seeds |
| Opponent-WEZ exposure | 0.00478 | 0.00367 | −0.00111 | unresolved across training seeds |
| Mean maximum load factor | 9.167 | 9.370 | +0.204 | unresolved across training seeds |
| Integrated load-factor exposure | 582.50 | 597.96 | +15.46 | unresolved across training seeds |

The only robust directional controller difference in the final inference occurs at the **5 deg WEZ threshold**, where shielded PPO reduces integrated load-factor exposure by **65.945 g·s**. The seed-block 95% CI is **[−118.30, −14.26]** and the three-seed t interval is **[−94.05, −37.84]**.

Accordingly, the repository and manuscript support neither universal controller dominance nor a universal safety–effectiveness trade-off.

## Publication-facing repository structure

- `src/` — 6-DoF simulator and PPO / shielded-PPO source tree.
- `results/` — historical campaign material plus the final P0-7F2/P0-7F3 publication authority files.
- `scripts/publication/` — scripts and PowerShell runners associated with the final matched-evaluation and seed-block postflight gates.
- `supplementary/true3d_replays/final/` — final representative matched true-coordinate replay PDFs used by the manuscript.
- `requirements-repro.txt` — compact publication-facing dependency list.
- `CITATION.cff` — citation metadata for the repository/manuscript.

See `results/PUBLICATION_AUTHORITY.md` for the exact precedence rules and `supplementary/true3d_replays/README.md` for replay provenance.

## Representative matched replays

The final manuscript uses only the following P0-7F2 matched true-coordinate replay selections:

- combined-audit representative: theta=3 deg, training seed 2, matched episode 7;
- 3 deg representative: training seed 2, matched episode 40;
- 5 deg representative: training seed 1, matched episode 33.

These replays are descriptive trajectory-level evidence. They are not additional inferential samples, do not demonstrate controller superiority or a formal safety guarantee, and do not establish discovery of a new canonical manoeuvre.

## Software environment

The publication-facing environment is Python 3.11. Principal package versions recorded for the reproducibility environment are:

- PyTorch 2.7.1
- NumPy 2.3.2
- SciPy 1.16.2
- pandas 2.3.1
- Matplotlib 3.10.3

The broader development environment is retained under `src/requirements.txt`; `requirements-repro.txt` provides the compact publication-facing set.

## Reproducibility guardrails

- Final controller-level claims use P0-7F2 point estimates and P0-7F3 seed-block inference.
- Repeated evaluation episodes improve within-policy precision but do not increase the number of independently trained policies beyond three seeds.
- True-coordinate replay evidence is descriptive, not inferential.
- No aggregate effectiveness, WEZ-exposure, maximum-load, or integrated-load difference is claimed as resolved across training seeds.
- The 5 deg integrated-load reduction is reported only as a threshold-specific result.

## Citation

Please cite the associated manuscript once publication details are available. Repository citation metadata are provided in `CITATION.cff`.
