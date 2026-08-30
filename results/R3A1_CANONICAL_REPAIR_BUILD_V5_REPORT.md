# DOGFIGHT R3A1 Canonical Repair Build

Status: PASS_R3A1_CANONICAL_REPAIR_BUILD_V5_CREATED
Smoke: PASS

## Paths
- BaseTrainRoot: D:\dogfightproject\dogfight-kod-chatatılacak\ppo-Dogfight\ppo-Dogfight\train
- RepairedSource: D:\dogfightproject\_review_revision\R3A1_CANONICAL_REPAIR_BUILD_V5_20260810_151628\repaired_source
- State: D:\dogfightproject\_review_revision\R3A1_CANONICAL_REPAIR_BUILD_V5_20260810_151628\R3A1_CANONICAL_REPAIR_BUILD_STATE.json
- Manifest: D:\dogfightproject\_review_revision\R3A1_CANONICAL_REPAIR_BUILD_V5_20260810_151628\tables\R3A1_repaired_source_manifest.csv

## Scientific Fixes Encoded
- Blue is the evaluated learning agent; Red is the fixed rule-based opponent.
- PPO/DDQN mixed stepping is removed in the new campaign script.
- PPO now has GAE-lambda, clip=0.2, gamma=0.99, entropy coefficient=0.01 and advantage normalization.
- The shielded method is RL-primary, not RL fallback.
- Altitude thresholds are explicit in feet; range/WEZ metrics are explicit in metres.
- Step/evaluation logs include proposed action, executed action, shield intervention, veto reason, done cause, ATA/AA/range, altitude, alpha, Mach and G metrics.
