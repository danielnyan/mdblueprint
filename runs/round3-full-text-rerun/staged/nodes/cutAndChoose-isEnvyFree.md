---
id: cutAndChoose-isEnvyFree
title: cutAndChoose_isEnvyFree
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.CutAndChoose
  declarations:
    - cutAndChoose_isEnvyFree
uses:
  - IsFairCutPoint
  - IsEnvyFree
  - MeasureValuation
  - cutter_isEnvyFree_of_fair
  - chooser_isEnvyFree
---

# cutAndChoose_isEnvyFree

## Lean type

```lean
theorem cutAndChoose_isEnvyFree (μ : Fin 2 → Measure I) (t : I) (hfair : IsFairCutPoint μ t) : IsEnvyFree (MeasureValuation μ) (cutAndChooseAlloc μ t)
```

## Dependencies

- IsFairCutPoint
- IsEnvyFree
- MeasureValuation
- cutter_isEnvyFree_of_fair
- chooser_isEnvyFree
