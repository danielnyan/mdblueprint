---
id: cutter-isEnvyFree-of-fair
title: cutter_isEnvyFree_of_fair
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.CutAndChoose
  declarations:
    - cutter_isEnvyFree_of_fair
uses:
  - IsFairCutPoint
  - MeasureValuation
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# cutter_isEnvyFree_of_fair

## Lean type

```lean
theorem cutter_isEnvyFree_of_fair (μ : Fin 2 → Measure I) (t : I) (hfair : IsFairCutPoint μ t) : (MeasureValuation μ).val 0 (cutAndChooseAlloc μ t 1) ≤ (MeasureValuation μ).val 0 (cutAndChooseAlloc μ t 0)
```

## Dependencies

- IsFairCutPoint
- MeasureValuation
- IsPositiveAffineOf.symm
- Indifferent.symm
