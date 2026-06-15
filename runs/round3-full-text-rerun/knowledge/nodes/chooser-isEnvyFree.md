---
id: chooser-isEnvyFree
title: chooser_isEnvyFree
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.CutAndChoose
  declarations:
    - chooser_isEnvyFree
uses:
  - MeasureValuation
---

# chooser_isEnvyFree

## Lean type

```lean
theorem chooser_isEnvyFree (μ : Fin 2 → Measure I) (t : I) : (MeasureValuation μ).val 1 (cutAndChooseAlloc μ t 0) ≤ (MeasureValuation μ).val 1 (cutAndChooseAlloc μ t 1)
```

## Dependencies

- MeasureValuation
