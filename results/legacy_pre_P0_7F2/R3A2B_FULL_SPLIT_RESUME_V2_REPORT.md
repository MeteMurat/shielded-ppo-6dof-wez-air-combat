# R3A2B Full Split/Resume Recalculation V2

- Status: PASS_R3A2B_FULL_SPLIT_RESUME_V2_ALL_UNITS_COMPLETE
- RunRoot: D:\dogfightproject\_review_revision\R3A2B_FULL_SPLIT_RESUME_V1_20260810_222629
- CampaignPath: D:\dogfightproject\_review_revision\R3A2B_FULL_SPLIT_RESUME_V1_20260810_222629\repaired_source\train_recalc_campaign.py
- Controllers: ppo,ppo_shield
- Seeds: 0,1,2
- ThetaList: 3,5
- TrainSteps: 50000
- EvalEpisodes: 50
- MaxSteps: 300
- UnitTimeoutMinutes: 360
- MaxUnitsPerRun: 1
- UnitsRunThisInvocation: 1
- CompletedUnits: 12 / 12
- AggregationStatePass: True
- AggregationExitCode: 

## Notes
- This script does not mutate original source or manuscript files.
- Existing completed units are detected from episode_metrics.csv and skipped.
- Re-run with -ResumeRoot pointing to this RunRoot until ALL_UNITS_COMPLETE.
