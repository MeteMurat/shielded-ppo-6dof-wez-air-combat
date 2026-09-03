# R3A2B Full Split/Resume Recalculation V1

- Status: FAIL_R3A2B_FULL_SPLIT_RESUME_V1_AGGREGATION_FAILED
- RunRoot: D:\dogfightproject\_review_revision\R3A2B_FULL_SPLIT_RESUME_V1_20260810_222629
- CampaignPath: D:\dogfightproject\_review_revision\R3A2B_FULL_SPLIT_RESUME_V1_20260810_222629\repaired_source\train_recalc_campaign.py
- Controllers: rule,dqn,ppo,ppo_shield
- Seeds: 0,1,2,3,4
- ThetaList: 1,3,5
- TrainSteps: 50000
- EvalEpisodes: 50
- MaxSteps: 300
- UnitTimeoutMinutes: 240
- MaxUnitsPerRun: 6
- UnitsRunThisInvocation: 6
- CompletedUnits: 6 / 60

## Notes
- This script does not mutate original source or manuscript files.
- Unit outputs remain in unit_out; the review ZIP excludes heavy trajectory/checkpoint folders.
- Re-run with -ResumeRoot pointing to this RunRoot to continue incomplete units.
